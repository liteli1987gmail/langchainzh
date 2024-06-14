# 使用参考示例

提供给LLM参考示例可以提高抽取的质量。

:::⚠⚠⚠

尽管此教程重点介绍如何在调用模型的工具中使用示例，但此技术通常适用，并且也适用于更多基于JSON或提示的技术。

:::


```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 定义一个自定义提示，提供说明和任何其他上下文。
# 1) 您可以将示例添加到提示模板中，以提高抽取质量
# 2) 引入其他参数以考虑上下文（例如，包含从抽取文本的文档中提取的元数据）
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "您是一个专家抽取算法。只从文本中提取相关信息。如果无法确定要提取的属性的值，请将属性的值返回为null。",
        ),
        # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        MessagesPlaceholder("examples"),  # <-- EXAMPLES!
        # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
        ("human", "{text}"),
    ]
)
```

测试模板：


```python
from langchain_core.messages import (
    HumanMessage,
)


prompt.invoke(
    {"text": "这是一些文本", "examples": [HumanMessage(content="测试 1 2 3")]}
)
```




    ChatPromptValue(messages=[SystemMessage(content='您是一个专家抽取算法。只从文本中提取相关信息。如果无法确定要提取的属性的值，请将属性的值返回为null。'), HumanMessage(content='测试 1 2 3'), HumanMessage(content='这是一些文本')])



## 定义模式

让我们重用快速入门中的人员模式。


```python
from typing import List, Optional

from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI


class Person(BaseModel):
    """关于人的信息。"""

    # ^ 实体Person的文档字符串。
    # 此文档字符串将作为模式Person的说明发送到LLM，并可以帮助提高抽取结果。

    # 请注意：
    # 1. 每个字段都是“optional”的-这允许模型拒绝进行抽取！
    # 2. 每个字段都有“description”-LLM会使用此描述。良好的描述可以帮助改善抽取结果。
    name: Optional[str] = Field(..., description="人的姓名")
    hair_color: Optional[str] = Field(
        ..., description="（如果已知）人的头发颜色"
    )
    height_in_meters: Optional[str] = Field(..., description="以米为单位的身高")


class Data(BaseModel):
    """关于人的提取数据。"""

    # 创建一个模型，以便我们可以提取多个实体。
    people: List[Person]
```

## 定义参考示例

示例可以定义为输入输出对的列表。

每个示例包含一个示例“input”文本和一个示例“output”，表示应从文本中提取的内容。

:::⚠⚠⚠


这有点复杂，请忽略如果您不理解！

示例的格式需要与所使用的API匹配（例如，调用工具或JSON模式等）。

在这里，格式化的示例将与工具调用API期望的格式匹配，因为这是我们使用的方式。

:::


```python
import uuid
from typing import Dict, List, TypedDict

from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)
from langchain_core.pydantic_v1 import BaseModel, Field


class Example(TypedDict):
    """由文本输入和预期工具调用组成的示例的表示形式。

    对于抽取，工具调用被表示为pydantic模型的实例。
    """

    input: str  # 这是示例文本
    tool_calls: List[BaseModel]  # 应该从中提取的pydantic模型的实例


def tool_example_to_messages(example: Example) -> List[BaseMessage]:
    """将示例转换为可以输入LLM的消息列表。

    此代码是一个适配器，将我们的示例转换为一系列可以输入到聊天模型中的消息。

    每个示例的消息列表对应于：

    1）HumanMessage：包含应从中提取内容的内容。
    2）AIMessage：包含从模型中提取的信息
    3）ToolMessage：包含对模型的确认，即模型正确请求了工具。

    由于某些聊天模型对代理而不是抽取用例进行了超优化，因此需要ToolMessage。
    """
    messages: List[BaseMessage] = [HumanMessage(content=example["input"])]
    openai_tool_calls = []
    for tool_call in example["tool_calls"]:
        openai_tool_calls.append(
            {
                "id": str(uuid.uuid4()),
                "type": "function",
                "function": {
                    # 函数名称现在对应于pydantic模型的名称
                    # 这在API中现在是隐含的，
                    # 并且将来会得到改进。
                    "name": tool_call.__class__.__name__,
                    "arguments": tool_call.json(),
                },
            }
        )
    messages.append(
        AIMessage(content="", additional_kwargs={"tool_calls": openai_tool_calls})
    )
    tool_outputs = example.get("tool_outputs") or [
        "您已正确调用了此工具。"
    ] * len(openai_tool_calls)
    for output, tool_call in zip(tool_outputs, openai_tool_calls):
        messages.append(ToolMessage(content=output, tool_call_id=tool_call["id"]))
    return messages
```

接下来让我们定义我们的示例，然后将它们转换为消息格式。


```python
examples = [
    (
        "海洋广阔而美丽。它的深度超过20000英尺。里面有很多鱼。",
        Person(name=None, height_in_meters=None, hair_color=None),
    ),
    (
        "Fiona从法国远行到西班牙。",
        Person(name="Fiona", height_in_meters=None, hair_color=None),
    ),
]


messages = []

for text, tool_call in examples:
    messages.extend(
        tool_example_to_messages({"input": text, "tool_calls": [tool_call]})
    )
```

测试提示


```python
prompt.invoke({"text": "这是一些文本", "examples": messages})
```




    ChatPromptValue(messages=[SystemMessage(content='您是一个专家抽取算法。只从文本中提取相关信息。如果无法确定要提取的属性的值，请将属性的值返回为null。'), HumanMessage(content='海洋广阔而美丽。它的深度超过20000英尺。里面有很多鱼。'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'c75e57cc-8212-4959-81e9-9477b0b79126', 'type': 'function', 'function': {'name': 'Person', 'arguments': '{"name": null, "hair_color": null, "height_in_meters": null}'}}]}), ToolMessage(content='您已正确调用了此工具。', tool_call_id='c75e57cc-8212-4959-81e9-9477b0b79126'), HumanMessage(content='Fiona从法国远行到西班牙。'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': '69da50b5-e427-44be-b396-1e56d821c6b0', 'type': 'function', 'function': {'name': 'Person', 'arguments': '{"name": "Fiona", "hair_color": null, "height_in_meters": null}'}}]}), ToolMessage(content='您已正确调用了此工具。', tool_call_id='69da50b5-e427-44be-b396-1e56d821c6b0'), HumanMessage(content='这是一些文本')])


------

## 创建一个提取器
在这里，我们将使用**gpt-4**来创建一个提取器。

```python
# 我们将使用工具调用模式，需要支持工具调用的模型。
llm = ChatOpenAI(
    # 考虑使用一个好的模型进行基准测试，以获得最佳质量的参考。
    model="gpt-4-0125-preview",
    # 记得将温度设置为0来进行提取！
    temperature=0,
)

runnable = prompt | llm.with_structured_output(
    schema=Data,
    method="function_calling",
    include_raw=False,
)
```

/Users/harrisonchase/workplace/langchain/libs/core/langchain_core/_api/beta_decorator.py:86: LangChainBetaWarning: 函数 `with_structured_output` 处于测试阶段。它正在积极开发中，因此API可能会发生变化。
  warn_beta(
    

## 没有示例 😿

请注意，尽管我们正在使用gpt-4，但它在一个非常简单的测试用例上失败了！

```python
for _ in range(5):
    text = "太阳系很大，但地球只有一个月亮。"
    print(runnable.invoke({"text": text, "examples": []}))
```

结果为:

    人=[]
    人=[Person(name='地球', hair_color=None, height_in_meters=None)]
    人=[Person(name='地球', hair_color=None, height_in_meters=None)]
    人=[]
    人=[]

## 有示例 😻

使用参考示例可以帮助修复失败的情况！

```python
for _ in range(5):
    text = "太阳系很大，但地球只有一个月亮。"
    print(runnable.invoke({"text": text, "examples": messages}))
```

结果为:

    人=[]
    人=[]
    人=[]
    人=[]
    人=[]


```python
runnable.invoke(
    {
        "text": "我叫Harrison。我有黑色的头发。",
        "examples": messages,
    }
)
```

结果为:

    Data(people=[Person(name='Harrison', hair_color='黑色', height_in_meters=None)])

------
