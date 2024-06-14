# 扩展

信息检索系统对于措辞和特定关键词非常敏感。为了减轻这个问题，一种经典的检索技术是生成查询的多个释义版本，并返回所有版本的查询结果。这被称为**查询扩展**。 LL模型是生成查询的这些备选版本的强大工具。

让我们看看如何对我们的Q&A机器人在LangChain YouTube视频上进行查询扩展，我们在[快速入门](/use_cases/query_analysis/quickstart)中开始了这个项目。

## 设置
#### 安装依赖


```python
# %pip install -qU langchain langchain-openai
```

#### 设置环境变量

我们将在此示例中使用OpenAI：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 可选的，取消注释以使用LangSmith跟踪运行。在此处注册：https://smith.langchain.com。
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 查询生成

为了确保我们获得多个释义，我们将使用OpenAI的函数调用API。


```python
from langchain_core.pydantic_v1 import BaseModel, Field


class ParaphrasedQuery(BaseModel):
    """您已执行查询扩展以生成问题的释义副本。"""

    paraphrased_query: str = Field(
        ...,
        description="原始问题的独特释义副本。",
    )
```


```python
from langchain.output_parsers import PydanticToolsParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

system = """您是将用户问题转换为数据库查询的专家。\
您可以访问一个关于构建LLL应用程序的软件库的教程视频数据库。\

执行查询扩展。如果用户问题有多种常见措辞\
或问题中的关键词有常见的同义词，确保返回多个版本\
具有不同措辞的查询。

如果有您不熟悉的缩写或单词，请不要尝试重述它们。

返回至少3个问题的版本。"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
llm_with_tools = llm.bind_tools([ParaphrasedQuery])
query_analyzer = prompt | llm_with_tools | PydanticToolsParser(tools=[ParaphrasedQuery])
```

让我们看看我们的分析器为我们之前搜索的问题生成了哪些查询：


```python
query_analyzer.invoke(
    {
        "question": "如何在链式结构中使用多模型并将链式结构转换为REST API"
    }
)
```




    [ParaphrasedQuery(paraphrased_query='如何按顺序使用多模型并将序列转换为REST API'),
     ParaphrasedQuery(paraphrased_query='使用多模型的步骤，并将序列转换为RESTful API'),
     ParaphrasedQuery(paraphrased_query='关于在链式结构中使用多模型并将链式结构转换为RESTful API的指南')]




```python
query_analyzer.invoke({"question": "从LLM代理中流式传输事件"})
```




    [ParaphrasedQuery(paraphrased_query='如何从LLM代理中流式传输事件？'),
     ParaphrasedQuery(paraphrased_query='如何实时接收LLM代理的事件？'),
     ParaphrasedQuery(paraphrased_query='从LLM代理捕获事件的流程是什么？')]


