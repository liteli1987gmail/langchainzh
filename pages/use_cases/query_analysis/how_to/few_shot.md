# 为Prompt添加示例

随着查询分析的复杂性增加，LLM 在某些情况下可能会在如何应答上面临困难。为了提高性能，我们可以在Prompt中添加示例来指导LLM。

让我们看看如何为我们在 [快速入门](/use_cases/query_analysis/quickstart) 中构建的 LangChain YouTube 视频查询分析器添加示例。

## 设置
#### 安装依赖


```python
# %pip install -qU langchain-core langchain-openai
```

#### 设置环境变量

我们将在此示例中使用 OpenAI：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 可选的，取消下一行的注释以使用 LangSmith 进行跟踪运行情况。在此注册：https://smith.langchain.com。
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 查询模式

我们将定义一个查询模式，希望我们的模型输出这个模式。为了使我们的查询分析更加有趣，我们将添加一个包含从顶级问题派生出的更具体问题的 `sub_queries` 字段。


```python
from typing import List, Optional

from langchain_core.pydantic_v1 import BaseModel, Field

sub_queries_description = """\
如果原始问题包含多个不同的子问题，\
或者如果有更通用的问题对于回答原始问题可能有帮助，\
请编写所有相关子问题的列表。\
确保这个列表是全面的，并涵盖原始问题的所有部分。\
子问题中可以有冗余。\
确保子问题的焦点尽可能狭窄。"""


class Search(BaseModel):
    """搜索有关构建 LLM 引擎应用程序的软件库的教程视频的数据库。"""

    query: str = Field(
        ...,
        description="应用于视频转录的主要相似性搜索查询。",
    )
    sub_queries: List[str] = Field(
        default_factory=list, description=sub_queries_description
    )
    publish_year: Optional[int] = Field(None, description="视频的发布年份")
```

## 查询生成


```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

system = """您是一个将用户问题转换为数据库查询的专家。\
您可以访问一个关于构建 LLM 引擎应用程序的软件库的教程视频的数据库。\
给定一个问题，返回一个优化的数据库查询列表以检索最相关的结果。

如果有您不熟悉的首字母缩写或词汇，请不要试图改写它们。"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        MessagesPlaceholder("examples", optional=True),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
structured_llm = llm.with_structured_output(Search)
query_analyzer = {"question": RunnablePassthrough()} | prompt | structured_llm
```

让我们尝试一下没有任何示例的查询分析器：


```python
query_analyzer.invoke(
    "web voyager 和 reflection agents 之间有什么区别？它们是否都使用 langgraph？"
)
```




    Search(query='web voyager vs reflection agents', sub_queries=['difference between web voyager and reflection agents', 'do web voyager and reflection agents use langgraph'], publish_year=None)



## 添加示例和调整Prompt

这个效果还不错，但我们可能希望它进一步分解问题，将对 Web Voyager 和 Reflection Agents 的查询分开。

为了调整我们的查询生成结果，我们可以向 Prompt 中添加一些输入问题和黄金标准的输出查询的示例。


```python
examples = []
```


```python
question = "Chat LangChain 是什么，它是 LangChain 模板吗？"
query = Search(
    query="What is chat LangChain and is it a LangChain template?",
    sub_queries=["What is chat LangChain", "What is a LangChain template"],
)
examples.append({"input": question, "tool_calls": [query]})
```


```python
question = "如何构建多智能体系统并流式传输其中间步骤"
query = Search(
    query="How to build multi-agent system and stream intermediate steps from it",
    sub_queries=[
        "How to build multi-agent system",
        "How to stream intermediate steps from multi-agent system",
        "How to stream intermediate steps",
    ],
)

examples.append({"input": question, "tool_calls": [query]})
```


```python
question = "LangChain agents 和 LangGraph 有什么区别？如何部署它们？"
query = Search(
    query="What's the difference between LangChain agents and LangGraph? How do you deploy them?",
    sub_queries=[
        "What are LangChain agents",
        "What is LangGraph",
        "How do you deploy LangChain agents",
        "How do you deploy LangGraph",
    ],
)
examples.append({"input": question, "tool_calls": [query]})
```

现在我们需要更新我们的 Prompt 模板和链式操作，以便每个 Prompt 中都包含这些示例。由于我们正在使用 OpenAI 的函数调用，所以我们需要进行一些额外的结构化处理，以将示例的输入和输出发送给模型。我们将创建一个 `tool_example_to_messages` 辅助函数来处理这个操作：


```python
import uuid
from typing import Dict

from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)


def tool_example_to_messages(example: Dict) -> List[BaseMessage]:
    messages: List[BaseMessage] = [HumanMessage(content=example["input"])]
    openai_tool_calls = []
    for tool_call in example["tool_calls"]:
        openai_tool_calls.append(
            {
                "id": str(uuid.uuid4()),
                "type": "function",
                "function": {
                    "name": tool_call.__class__.__name__,
                    "arguments": tool_call.json(),
                },
            }
        )
    messages.append(
        AIMessage(content="", additional_kwargs={"tool_calls": openai_tool_calls})
    )
    tool_outputs = example.get("tool_outputs") or [
        "You have correctly called this tool."
    ] * len(openai_tool_calls)
    for output, tool_call in zip(tool_outputs, openai_tool_calls):
        messages.append(ToolMessage(content=output, tool_call_id=tool_call["id"]))
    return messages


example_msgs = [msg for ex in examples for msg in tool_example_to_messages(ex)]
=======
##### 我提供的mdx文档的内容需要翻译，只要翻译md语法中的标题、段落和列表的内容，驼峰和下划线单词不必翻译，请保留md语法标点符号，你翻译完后对原内容进行替换，将结果返回给我。mdx文档是:=======

```


```python
from langchain_core.prompts import MessagesPlaceholder

query_analyzer_with_examples = (
    {"question": RunnablePassthrough()}
    | prompt.partial(examples=example_msgs)
    | structured_llm
)
```

```python
query_analyzer_with_examples.invoke(
    "what's the difference between web voyager and reflection agents? do both use langgraph?"
)
```

结果如下：

```python
# 定义一个带有示例的查询分析器
query_analyzer_with_examples = (
    {"question": RunnablePassthrough()}
    | prompt.partial(examples=example_msgs)
    | structured_llm
)

# 调用查询分析器，以获得查询结果
query_analyzer_with_examples.invoke(
    "web voyager和reflection agents有什么区别？它们是否都使用LangGraph？"
)
```

借助我们的示例，我们得到了一个稍微更详细的搜索查询。通过进一步的提示工程和优化示例，我们可以进一步改进查询生成的效果。

通过[LangSmith跟踪](https://smith.langchain.com/public/aeaaafce-d2b1-4943-9a61-bc954e8fc6f2/r)中的消息，您可以看到示例是作为消息传递给模型的。




