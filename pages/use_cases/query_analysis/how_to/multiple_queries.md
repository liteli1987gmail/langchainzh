# 多查询（MultipleQueries）
有时候，查询分析技术可能允许生成多个查询。在这些情况下，我们需要记得运行所有查询，然后组合结果。我们将展示一个简单的例子（使用模拟数据），说明如何做到这一点。

## 设置
#### 安装依赖

```python
# %pip install -qU langchain langchain-community langchain-openai chromadb
```

#### 设置环境变量

我们将在这个例子中使用 OpenAI：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# Optional, uncomment to trace runs with LangSmith. Sign up here: https://smith.langchain.com.
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

### 创建索引

我们将在虚假信息上创建一个向量存储。


```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

texts = ["Harrison worked at Kensho", "Ankush worked at Facebook"]
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma.from_texts(
    texts,
    embeddings,
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
```

## 查询分析

我们将使用函数调用来结构化输出。我们将让它返回多个查询。


```python
from typing import List, Optional

from langchain_core.pydantic_v1 import BaseModel, Field


class Search(BaseModel):
    """Search over a database of job records."""

    queries: List[str] = Field(
        ...,
        description="Distinct queries to search for",
    )
```


```python
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

output_parser = PydanticToolsParser(tools=[Search])

system = """You have the ability to issue search queries to get information to help answer user information.

If you need to look up two distinct pieces of information, you are allowed to do that!"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
structured_llm = llm.with_structured_output(Search)
query_analyzer = {"question": RunnablePassthrough()} | prompt | structured_llm
```

    /Users/harrisonchase/workplace/langchain/libs/core/langchain_core/_api/beta_decorator.py:86: LangChainBetaWarning: The function `with_structured_output` is in beta. It is actively being worked on, so the API may change.
      warn_beta(
    

我们可以看到，这允许创建多个查询。


```python
query_analyzer.invoke("where did Harrison Work")
```




    Search(queries=['Harrison work location'])




```python
query_analyzer.invoke("where did Harrison and ankush Work")
```




    Search(queries=['Harrison work place', 'Ankush work place'])



## 带查询分析的检索

那么，我们如何将此纳入链中呢？如果我们可以异步调用检索器，这将使事情变得更容易——这样我们可以循环遍历查询而不会被响应时间阻塞。


```python
from langchain_core.runnables import chain
```


```python
@chain
async def custom_chain(question):
    response = await query_analyzer.ainvoke(question)
    docs = []
    for query in response.queries:
        new_docs = await retriever.ainvoke(query)
        docs.extend(new_docs)
    # You probably want to think about reranking or deduplicating documents here
    # But that is a separate topic
    return docs
```


```python
await custom_chain.ainvoke("where did Harrison Work")
```




    [Document(page_content='Harrison worked at Kensho')]




```python
await custom_chain.ainvoke("where did Harrison and ankush Work")
```




    [Document(page_content='Harrison worked at Kensho'),
     Document(page_content='Ankush worked at Facebook')]




