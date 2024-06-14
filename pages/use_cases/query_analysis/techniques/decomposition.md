# 分解

当用户提出问题时，并不能保证可以通过单个查询返回相关的结果。有时为了回答一个问题，我们需要将其分解为独立的子问题，为每个子问题检索结果，然后使用累积上下文进行回答。

例如，如果用户问道：“Web Voyager和反射代理有什么不同”，我们有一个解释Web Voyager的文档和一个解释反射代理的文档，但没有一个文档对两者进行比较，那么我们通过检索“Web Voyager是什么”和“反射代理是什么”以及合并检索到的文档来获得更好的结果，而不是直接根据用户的问题来检索。

将输入拆分为多个独立的子查询的过程称为查询分解。有时也称为子查询生成。在本指南中，我们将通过一个示例来介绍如何进行分解，使用我们在[快速入门](/use_cases/query_analysis/quickstart)中针对LangChain YouTube视频的问答机器人的示例。

## 设置
#### 安装依赖项


```python
# %pip install -qU langchain langchain-openai
```

#### 设置环境变量

我们将在此示例中使用OpenAI：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 如果需要，可以取消注释以下行以使用LangSmith跟踪运行情况。在此处注册：https://smith.langchain.com.
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 查询生成

为了将用户的问题转换为一系列子问题，我们将使用OpenAI的函数调用API，该API可以每次返回多个函数：


```python
import datetime
from typing import Literal, Optional, Tuple

from langchain_core.pydantic_v1 import BaseModel, Field


class SubQuery(BaseModel):
    """在软件库的教程视频数据库中进行搜索。"""

    sub_query: str = Field(
        ...,
        description="针对数据库的一个非常具体的查询。",
    )
```


```python
from langchain.output_parsers import PydanticToolsParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

system = """您是将用户问题转换为数据库查询的专家。您可以访问一个教程视频数据库，该数据库用于构建基于LLM的应用程序的软件库。

执行查询分解。给定一个用户问题，将其拆分为不同的子问题，您需要回答这些子问题以回答原始问题。

如果有您不熟悉的缩写词或单词，请不要尝试重新表达它们。"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
llm_with_tools = llm.bind_tools([SubQuery])
parser = PydanticToolsParser(tools=[SubQuery])
query_analyzer = prompt | llm_with_tools | parser
```

让我们看看它的效果：


```python
query_analyzer.invoke({"question": "如何进行rag操作"})
```




    [SubQuery(sub_query='如何进行rag操作')]




```python
query_analyzer.invoke(
    {
        "question": "如何在链中使用多模型，并将链转为REST API"
    }
)
```




    [SubQuery(sub_query='如何在链中使用多模型？'),
     SubQuery(sub_query='如何将链转为REST API？')]




```python
query_analyzer.invoke(
    {
        "question": "Web Voyager和反射代理之间有什么区别？它们使用Langgraph吗？"
    }
)
```




    [SubQuery(sub_query='Web Voyager是什么，与反射代理有何不同？'),
     SubQuery(sub_query='Web Voyager和反射代理是否使用Langgraph？')]



## 添加示例和优化提示语

这个方法效果还不错，但我们可能希望进一步分解最后一个问题，将关于Web Voyager和反射代理的查询分开。如果我们不确定哪种类型的查询在我们的索引中效果最好，我们也可以故意在查询中包含一些冗余，以便返回子查询和更高级别的查询。

为了调整查询生成的结果，我们可以将一些输入问题和黄金标准输出查询的示例添加到我们的提示语中。我们还可以尝试改进我们的系统消息。


```python
examples = []
```


```python
question = "什么是chat langchain，它是一个langchain模板吗？"
queries = [
    SubQuery(sub_query="什么是chat langchain"),
    SubQuery(sub_query="什么是langchain模板"),
]
examples.append({"input": question, "tool_calls": queries})
```


```python
question = "如何使用LangGraph构建自动机"
queries = [
    SubQuery(sub_query="如何使用LangGraph构建自动机"),
]
examples.append({"input": question, "tool_calls": queries})
```


```python
question = "如何构建多代理系统并从中流式传输中间步骤"
queries = [
    SubQuery(sub_query="如何构建多代理系统"),
    SubQuery(sub_query="如何流式传输中间步骤"),
    SubQuery(sub_query="如何从多代理系统中流式传输中间步骤"),
]
examples.append({"input": question, "tool_calls": queries})
```


```python
question = "LangChain代理和LangGraph之间有什么区别？"
queries = [
    SubQuery(sub_query="LangChain代理和LangGraph之间有什么区别？"),
    SubQuery(sub_query="LangChain代理是什么"),
    SubQuery(sub_query="LangGraph是什么"),
]
examples.append({"input": question, "tool_calls": queries})
```

现在，我们需要更新我们的提示语模板和链，以便每个提示语中都包含示例。由于我们使用的是OpenAI的函数调用，我们需要进行一些额外的结构化操作，以便将示例输入和输出发送到模型。我们将创建一个`tool_example_to_messages`辅助函数来帮助我们处理：


```python
import uuid
from typing import Dict, List

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
>>>>>>> ac9e61da21d7b3b5a142b5a29fbc1aa73f9b57f8
    for call in example["tool_calls"]:
        tool_message = ToolMessage(
            content={"tools": [{"name": "SubQuery", "arguments": call}]},
            role=AIMessage.TOOL,
            uuid=str(uuid.uuid4()),
        )
        openai_tool_calls.append(tool_message)
    messages.extend(openai_tool_calls)
<<<<<<< HEAD
    last_uuid = str(uuid.uuid4())
    completion_message = AIMessage(
        role=AIMessage.SYSTEM,
        uuid=last_uuid,
        content={
            "messages": [
                {
                    "role": "instructor",
                    "content": {
                        "examples": [
                            {
                                "importance": "high",
                                "instruction": "Perform query decomposition. Given a user question, break it down into distinct sub questions that you need to answer in order to answer the original question.",
                                "query": query.sub_query
                            } for query in call.sub_query
                        ]
                    },
                    "uuid": last_uuid
                }
            ],
            "query_history": [
                {
                    "args": {
                        "turn_index": call.turn_index
                    }
                }
                for call in openai_tool_calls
            ]
        }
    )
=======
    completion_message = SystemMessage(
        content={
            "flow_entry_uuid": str(uuid.uuid4()),
            "graph_completion": {
                "flow_input": {
                    "examples": [
                        {
                            "importance": "high",
                            "instruction": "Perform query decomposition. Given a user question, break it down into distinct sub questions that you need to answer in order to answer the original question.",
                            "query": query.sub_query,
                        }
                        for query in example["tool_calls"]
                    ],
                },
                "flow_id": llm_with_tools.flow_id,
                "step_id": llm_with_tools.step_id,
            },
        },
    )
    messages.append(completion_message)
>>>>>>> ac9e61da21d7b3b5a142b5a29fbc1aa73f9b57f8
    return messages
=======

                我提供的mdx文档的内容需要翻译，只要翻译md语法中的标题、段落和列表的内容，驼峰和下划线单词不必翻译，请保留md语法标点符号，你翻译完后对原内容进行替换，将结果返回给我。mdx文档是:=======
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
        "This is an example of a correct usage of this tool. Make sure to continue using the tool this way."
    ] * len(openai_tool_calls)
    for output, tool_call in zip(tool_outputs, openai_tool_calls):
        messages.append(ToolMessage(content=output, tool_call_id=tool_call["id"]))
    return messages


example_msgs = [msg for ex in examples for msg in tool_example_to_messages(ex)]
```


```python
from langchain_core.prompts import MessagesPlaceholder

system = """You are an expert at converting user questions into database queries. \
You have access to a database of tutorial videos about a software library for building LLM-powered applications. \

Perform query decomposition. Given a user question, break it down into the most specific sub questions you can \
which will help you answer the original question. Each sub question should be about a single concept/fact/idea.

If there are acronyms or words you are not familiar with, do not try to rephrase them."""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        MessagesPlaceholder("examples", optional=True),
        ("human", "{question}"),
    ]
)
query_analyzer_with_examples = (
    prompt.partial(examples=example_msgs) | llm_with_tools | parser
)
```


```python
query_analyzer_with_examples.invoke(
    {
        "question": "what's the difference between web voyager and reflection agents? do they use langgraph?"
    }
)
```




    [SubQuery(sub_query="What's the difference between web voyager and reflection agents"),
     SubQuery(sub_query='Do web voyager and reflection agents use LangGraph'),
     SubQuery(sub_query='What is web voyager'),
     SubQuery(sub_query='What are reflection agents')]






