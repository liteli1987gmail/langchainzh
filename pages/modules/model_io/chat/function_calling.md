# 工具调用

```{=mdx}
:::🗒️
我们将术语工具调用与函数调用视为同义词。虽然函数调用有时指的是对单个函数的调用，
但我们将所有模型都视为可以在每个消息中返回多个工具或函数调用。
:::
```

工具调用允许模型通过生成与用户定义的模式匹配的输出来响应给定的提示。虽然名称暗示模型正在执行某些操作，但实际上并非如此！模型正在提出一个工具的参数，实际上运行工具（或不运行）取决于用户 - 例如，如果您想要从非结构化文本中[提取与某个模式匹配的输出](/use_cases/extraction/)，您可以给模型一个"提取"工具，该工具接受与所需模式匹配的参数，然后将生成的输出视为最终结果。

工具调用包括名称、参数字典和可选标识符。参数字典的结构为`{参数名: 参数值}`。

许多LLM提供者，包括[Anthropic](https://www.anthropic.com/)、
[Cohere](https://cohere.com/)、[Google](https://cloud.google.com/vertex-ai)、
[Mistral](https://mistral.ai/)、[OpenAI](https://openai.com/)等，
都支持工具调用功能的变体。这些功能通常允许LLM的请求包括可用工具及其模式，并且响应中包含对这些工具的调用。例如，给定一个搜索引擎工具，LLM可以通过首先发出对搜索引擎的调用来处理查询。调用LLM的系统可以接收工具调用，执行它，并将输出返回给LLM以通知其响应。LangChain包括一套[内置工具](/docs/integrations/tools/)，并支持几种定义自己的[自定义工具](/modules/tools/custom_tools)的方法。工具调用对于构建[使用工具的链和代理](/use_cases/tool_use)以及从模型获取结构化输出非常有用。

不同的供应商对于工具模式和工具调用的格式采用了不同的约定。例如，Anthropic将工具调用作为解析结构返回到较大内容块中：
```python
[
  {
    "text": "<thinking>\nI should use a tool.\n</thinking>",
    "type": "text"
  },
  {
    "id": "id_value",
    "input": {"arg_name": "arg_value"},
    "name": "tool_name",
    "type": "tool_use"
  }
]
```
而OpenAI将工具调用分离为一个独立的参数，参数为JSON字符串：
```python
{
  "tool_calls": [
    {
      "id": "id_value",
      "function": {
        "arguments": '{"arg_name": "arg_value"}',
        "name": "tool_name"
      },
      "type": "function"
    }
  ]
}
```
LangChain实现了定义工具的标准接口，将它们传递给LLM，并表示工具调用。

## 将工具传递给LLM

支持工具调用功能的聊天模型实现了`.bind_tools`方法，该方法接收LangChain [工具对象](https://api.python.langchain.com/en/latest/tools/langchain_core.tools.BaseTool.html#langchain_core.tools.BaseTool)列表，并将它们绑定到聊天模型中以符合预期的格式。对聊天模型的后续调用将在其调用LLM时包含工具模式。

例如，我们可以使用Python函数使用`@tool`装饰器定义自定义工具的模式：

```python
from langchain_core.tools import tool


@tool
def add(a: int, b: int) -> int:
    """将a和b相加。"""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """将a和b相乘。"""
    return a * b


tools = [add, multiply]
```

或者，我们可以使用Pydantic定义模式：

```python
from langchain_core.pydantic_v1 import BaseModel, Field


# 注意，这里的文档字符串非常重要，因为它们将与类名一起传递给模型。
class Add(BaseModel):
    """将两个整数相加。"""

    a: int = Field(..., description="第一个整数")
    b: int = Field(..., description="第二个整数")


class Multiply(BaseModel):
    """将两个整数相乘。"""

    a: int = Field(..., description="第一个整数")
    b: int = Field(..., description="第二个整数")


tools = [Add, Multiply]
```

我们可以将它们绑定到聊天模型：

```{=mdx}
import ChatModelTabs from "@theme/ChatModelTabs";

<ChatModelTabs
  customVarName="llm"
  fireworksParams={`model="accounts/fireworks/models/firefunction-v1", temperature=0`}
/>
```

我们可以使用`bind_tools()`方法来处理将`Multiply`转换为"tool"并将其绑定到模型（即每次调用模型时传递它）。

```python
# | echo: false
# | output: false

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
```


```python
llm_with_tools = llm.bind_tools(tools)
```

## 工具调用

如果工具调用包含在LLM响应中，它们将作为[消息](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.ai.AIMessage.html#langchain_core.messages.ai.AIMessage) 
或[消息块](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.ai.AIMessageChunk.html#langchain_core.messages.ai.AIMessageChunk)的属性`.tool_calls`中的[工具调用](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.tool.ToolCall.html#langchain_core.messages.tool.ToolCall)对象的列表附加到相应的消息或消息块上。`ToolCall`是一个类型化的字典，其中包括工具名称、参数值字典和（可选）标识符。没有工具调用的消息默认将该属性设置为空列表。

示例：

```python
query = "3 * 12是多少？此外，11 + 49是多少？"

llm_with_tools.invoke(query).tool_calls
```




    [{'name': 'Multiply',
      'args': {'a': 3, 'b': 12},
      'id': 'call_1Tdp5wUXbYQzpkBoagGXqUTo'},
     {'name': 'Add',
      'args': {'a': 11, 'b': 49},
      'id': 'call_k9v09vYioS3X0Qg35zESuUKI'}]



`.tool_calls`属性应包含有效的工具调用。请注意，有时模型提供者可能会输出格式不正确的工具调用（例如，无效的JSON参数）。在这些情况下，解析失败时，将在`.invalid_tool_calls`属性中填充[InvalidToolCall](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.tool.InvalidToolCall.html#langchain_core.messages.tool.InvalidToolCall)的实例。InvalidToolCall可以具有名称、字符串参数、标识符和错误消息。

如果需要，[输出解析器](/modules/model_io/output_parsers)可以进一步处理输出。例如，我们可以转换回原始的Pydantic类：

```python
from langchain_core.output_parsers.openai_tools import PydanticToolsParser

chain = llm_with_tools | PydanticToolsParser(tools=[Multiply, Add])
chain.invoke(query)
```




    [Multiply(a=3, b=12), Add(a=11, b=49)]





### 流式处理

当在流式处理上下文中调用工具时，[消息块](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.ai.AIMessageChunk.html#langchain_core.messages.ai.AIMessageChunk)将通过`.tool_call_chunks`属性以列表形式填充包含[工具调用块](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.tool.ToolCallChunk.html#langchain_core.messages.tool.ToolCallChunk)对象的内容。`ToolCallChunk`包括用于工具的可选字符串字段`name`、`args`和`id`，并包括可选的整数字段`index`，可用于合并块。字段是可选的，因为工具调用的部分可能在不同的块中进行流传输（例如，包含参数子字符串的块可能对工具名称和id具有空值）。

由于消息块从其父类消息类继承，因此具有工具调用块的[AIMessageChunk](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.ai.AIMessageChunk.html#langchain_core.messages.ai.AIMessageChunk)还将包括`.tool_calls`和`.invalid_tool_calls`字段。这些字段是从消息的工具调用块中最佳努力解析的。

请注意，目前并非所有提供程序都支持工具调用的流传输。

示例：

```python
async for chunk in llm_with_tools.astream(query):
    print(chunk.tool_call_chunks)
```

    []
    [{'name': 'Multiply', 'args': '', 'id': 'call_d39MsxKM5cmeGJOoYKdGBgzc', 'index': 0}]
    [{'name': None, 'args': '{"a"', 'id': None, 'index': 0}]
    [{'name': None, 'args': ': 3, ', 'id': None, 'index': 0}]
    [{'name': None, 'args': '"b": 1', 'id': None, 'index': 0}]
    [{'name': None, 'args': '2}', 'id': None, 'index': 0}]
    [{'name': 'Add', 'args': '', 'id': 'call_QJpdxD9AehKbdXzMHxgDMMhs', 'index': 1}]
    [{'name': None, 'args': '{"a"', 'id': None, 'index': 1}]
    [{'name': None, 'args': ': 11,', 'id': None, 'index': 1}]
    [{'name': None, 'args': ' "b": ', 'id': None, 'index': 1}]
    [{'name': None, 'args': '49}', 'id': None, 'index': 1}]
    []
    

请注意，添加消息块将合并它们对应的工具调用块。这是LangChain的各种[工具输出解析器](/modules/model_io/output_parsers/types/openai_tools/)支持流式处理的原则。

例如，下面我们累积工具调用块：

```python
first = True
async for chunk in llm_with_tools.astream(query):
    if first:
        gathered = chunk
        first = False
    else:
        gathered = gathered + chunk

    print(gathered.tool_call_chunks)
```

    []
    [{'name': 'Multiply', 'args': '', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}]
    [{'name': 'Multiply', 'args': '{"a"', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}]
    [{'name': 'Multiply', 'args': '{"a": 3, ', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}]
    [{'name': 'Multiply', 'args': '{"a": 3, "b": 1', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}]
    [{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}]
    [{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}]
    [{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '{"a"', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}]
    [{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '{"a": 11,', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}]
    [{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '{"a": 11, "b": ', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}]
    [{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '{"a": 11, "b": 49}', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}]
    [{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_erKtz8z3e681cmxYKbRof0NS', 'index': 0}, {'name': 'Add', 'args': '{"a": 11, "b": 49}', 'id': 'call_tYHYdEV2YBvzDcSCiFCExNvw', 'index': 1}]
    

```python
print(type(gathered.tool_call_chunks[0]["args"]))
```


    <class 'str'>



并且我们累积工具调用以演示部分解析：

```python
first = True
async for chunk in llm_with_tools.astream(query):
    if first:
        gathered = chunk
        first = False
    else:
        gathered = gathered + chunk

    print(gathered.tool_calls)
```

    []
    []
    [{'name': 'Multiply', 'args': {}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}]
    [{'name': 'Multiply', 'args': {'a': 3}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}]
    [{'name': 'Multiply', 'args': {'a': 3, 'b': 1}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}]
    [{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}]
    [{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}]
    [{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}, {'name': 'Add', 'args': {}, 'id': 'call_UjSHJKROSAw2BDc8cp9cSv4i'}]
    [{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}, {'name': 'Add', 'args': {'a': 11}, 'id': 'call_UjSHJKROSAw2BDc8cp9cSv4i'}]
    [{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}, {'name': 'Add', 'args': {'a': 11}, 'id': 'call_UjSHJKROSAw2BDc8cp9cSv4i'}]
    [{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}, {'name': 'Add', 'args': {'a': 11, 'b': 49}, 'id': 'call_UjSHJKROSAw2BDc8cp9cSv4i'}]
    [{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_BXqUtt6jYCwR1DguqpS2ehP0'}, {'name': 'Add', 'args': {'a': 11, 'b': 49}, 'id': 'call_UjSHJKROSAw2BDc8cp9cSv4i'}]
    

```python
print(type(gathered.tool_calls[0]["args"]))
```


    <class 'dict'>



## 将工具输出传递给模型

如果我们使用模型生成的工具调用来实际调用工具，并希望将工具结果传递回模型，可以使用`ToolMessage`。

```python
from langchain_core.messages import HumanMessage, ToolMessage

messages = [HumanMessage(query)]
ai_msg = llm_with_tools.invoke(messages)
messages.append(ai_msg)
for tool_call in ai_msg.tool_calls:
    selected_tool = {"add": add, "multiply": multiply}[tool_call["name"].lower()]
    tool_output = selected_tool.invoke(tool_call["args"])
    messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))
messages
```




    [HumanMessage(content='What is 3 * 12? Also, what is 11 + 49?'),
     AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_K5DsWEmgt6D08EI9AFu9NaL1', 'function': {'arguments': '{"a": 3, "b": 12}', 'name': 'Multiply'}, 'type': 'function'}, {'id': 'call_qywVrsplg0ZMv7LHYYMjyG81', 'function': {'arguments': '{"a": 11, "b": 49}', 'name': 'Add'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 50, 'prompt_tokens': 105, 'total_tokens': 155}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': 'fp_b28b39ffa8', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-1a0b8cdd-9221-4d94-b2ed-5701f67ce9fe-0', tool_calls=[{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_K5DsWEmgt6D08EI9AFu9NaL1'}, {'name': 'Add', 'args': {'a': 11, 'b': 49}, 'id': 'call_qywVrsplg0ZMv7LHYYMjyG81'}]),
     ToolMessage(content='36', tool_call_id='call_K5DsWEmgt6D08EI9AFu9NaL1'),
     ToolMessage(content='60', tool_call_id='call_qywVrsplg0ZMv7LHYYMjyG81')]




```python
llm_with_tools.invoke(messages)
```




    AIMessage(content='3 * 12 is 36 and 11 + 49 is 60.', response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 171, 'total_tokens': 189}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': 'fp_b28b39ffa8', 'finish_reason': 'stop', 'logprobs': None}, id='run-a6c8093c-b16a-4c92-8308-7c9ac998118c-0')



## 少量示例提示

对于更复杂的工具使用，添加少量示例提示非常有用。我们可以通过添加带有`ToolCall`和相应`ToolMessage`的`AIMessage`来实现。

例如，即使在一些特殊说明下，我们的模型也可能因为运算顺序而出错：

```python
llm_with_tools.invoke(
    "Whats 119 times 8 minus 20. Don't do any math yourself, only use tools for math. Respect order of operations"
).tool_calls
```




    [{'name': 'Multiply',
      'args': {'a': 119, 'b': 8},
      'id': 'call_Dl3FXRVkQCFW4sUNYOe4rFr7'},
     {'name': 'Add',
      'args': {'a': 952, 'b': -20},
      'id': 'call_n03l4hmka7VZTCiP387Wud2C'}]



由于不能知道119 * 8的结果，因此模型不应尝试进行任何加法运算。

通过添加一些示例提示，我们可以纠正这种行为：

```python
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

examples = [
    HumanMessage(
        "What's the product of 317253 and 128472 plus four", name="example_user"
    ),
    AIMessage(
        "",
        name="example_assistant",
        tool_calls=[
            {"name": "Multiply", "args": {"x": 317253, "y": 128472}, "id": "1"}
        ],
    ),
    ToolMessage("16505054784", tool_call_id="1"),
    AIMessage(
        "",
        name="example_assistant",
        tool_calls=[{"name": "Add", "args": {"x": 16505054784, "y": 4}, "id": "2"}],
    ),
    ToolMessage("16505054788", tool_call_id="2"),
    AIMessage(
        "The product of 317253 and 128472 plus four is 16505054788",
        name="example_assistant",
    ),
]

system = """You are bad at math but are an expert at using a calculator. 

Use past tool usage as an example of how to correctly use the tools."""
few_shot_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        *examples,
        ("human", "{query}"),
    ]
)

chain = {"query": RunnablePassthrough()} | few_shot_prompt | llm_with_tools
chain.invoke("Whats 119 times 8 minus 20").tool_calls
```




    [{'name': 'Multiply',
      'args': {'a': 119, 'b': 8},
      'id': 'call_MoSgwzIhPxhclfygkYaKIsGZ'}]



看起来这次我们得到了正确的输出。

下面是[LangSmith跟踪](https://smith.langchain.com/public/f70550a1-585f-4c9d-a643-13148ab1616f/r)的样子。



## 下一步

- **输出解析**：请查阅[OpenAI工具输出解析器](/modules/model_io/output_parsers/types/openai_tools/)和[OpenAI函数输出解析器](/modules/model_io/output_parsers/types/openai_functions/)，了解如何将函数调用API响应提取为各种格式。
- **结构化输出链**：[一些模型有构造函数](/modules/model_io/chat/structured_output/)，可以帮助您创建一个结构化输出链。
- **工具使用**：查看如何构建链条和代理，调用[这些指南中调用的工具](/use_cases/tool_use/)。