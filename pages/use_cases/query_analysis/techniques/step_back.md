# 后退提示

有时候，在处理特定问题时，搜索质量和模型生成可能会出现问题。处理这个问题的一种方法是首先生成一个更抽象的“后退”问题，并基于原始问题和后退问题进行查询。

例如，如果我们提出一个形如“为什么我的LangGraph代理astream_events返回{LONG_TRACE}而不是{DESIRED_OUTPUT}”的问题，如果我们使用更通用的问题“LangGraph代理如何使用astream_events？”搜索，我们很可能会检索到更相关的文档，而不是使用具体的用户问题进行搜索。

让我们看看如何在LangChain YouTube视频的问答机器人中使用后退提示。

## 设置
#### 安装依赖


```python
# %pip install -qU langchain-core langchain-openai
```

#### 设置环境变量

在这个示例中我们将使用OpenAI：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 可选，取消注释以使用LangSmith进行追踪。在此注册: https://smith.langchain.com
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 生成后退问题

生成好的后退问题取决于良好的提示：


```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

system = """你是一个专家，擅长将特定问题转化为更通用的问题，从而找到回答特定问题所需的基本原则。

您将被问及一组用于构建以LLM为基础的应用程序的软件，包括LangChain、LangGraph、LangServe和LangSmith。

LangChain 是一个Python框架，提供了一组大型的集成，可以轻松组合构建LLM应用程序。
LangGraph 是一个基于 LangChain 的Python包，它使构建有状态的多角色LLM应用程序变得容易。
LangServe 是一个基于 LangChain 的Python包，它使将 LangChain 应用程序部署为 REST API 变得容易。
LangSmith 是一个平台，它使追踪和测试LLM应用程序变得容易。

针对这些产品中的一个或多个，给出一个特定用户问题的更通用问题，以便回答特定问题。

如果您不认识某个单词或首字母缩略词，请不要尝试重新编写它。

请写出简明扼要的问题。"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
step_back = prompt | llm | StrOutputParser()
```


```python
question = (
    "我使用Gemini Pro和类似vectorstores和duckduckgo search的工具构建了一个LangGraph代理。"
    "我该如何从事件流中获取仅包含LLM调用的内容"
)
result = step_back.invoke({"question": question})
print(result)
```

    LangGraph提供了用于从包括各种交互和数据源的事件流中提取LLM调用的特定方法或函数是什么？
    

## 返回后退问题和原始问题

为了增加我们的召回率，我们很可能会根据后退问题和原始问题分别检索文档。我们可以这样轻松地返回这两个问题：


```python
from langchain_core.runnables import RunnablePassthrough

step_back_and_original = RunnablePassthrough.assign(step_back=step_back)

step_back_and_original.invoke({"question": question})
```




    {'question': '我使用Gemini Pro和类似vectorstores和duckduckgo search的工具构建了一个LangGraph代理。我该如何从事件流中获取仅包含LLM调用的内容',
     'step_back': 'LangGraph提供了用于从由使用类似Gemini Pro、vectorstores和DuckDuckGo search等外部工具构建的代理生成的事件流中提取LLM调用的特定方法或函数是什么？'}



## 使用函数调用以获取结构化输出

如果我们将这个技巧与其他查询分析技术组合使用，我们很可能会使用函数调用来获取结构化查询对象。我们可以使用函数调用来实现后退提示，如下所示：


```python
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.pydantic_v1 import BaseModel, Field


class StepBackQuery(BaseModel):
    step_back_question: str = Field(
        ...,
        description="给定一个关于这些产品中一个或多个的特定用户问题，写出一个更通用的问题，以便回答特定问题。",
    )


llm_with_tools = llm.bind_tools([StepBackQuery])
hyde_chain = prompt | llm_with_tools | PydanticToolsParser(tools=[StepBackQuery])
hyde_chain.invoke({"question": question})
```




    [StepBackQuery(step_back_question='在类似LangGraph的Python框架中，从事件流中过滤和提取特定类型的调用的步骤是什么？')]

------



