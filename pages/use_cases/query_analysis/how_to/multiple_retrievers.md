# 处理多个检索器

有时，查询分析技术可能允许选择要使用的检索器。为了使用它，您需要添加一些逻辑来选择要执行的检索器。我们将展示一个简单的示例（使用模拟数据）来说明如何做到这一点。

## 设置
#### 安装依赖


```python
# %pip install -qU langchain langchain-community langchain-openai chromadb
```

#### 设置环境变量

在本示例中，我们将使用OpenAI：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 可选, 取消注释以使用LangSmith对运行进行跟踪。在此注册: https://smith.langchain.com.
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

### 创建索引

我们将在虚假信息上创建一个向量存储。


```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

texts = ["Harrison worked at Kensho"]
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma.from_texts(texts, embeddings, collection_name="harrison")
retriever_harrison = vectorstore.as_retriever(search_kwargs={"k": 1})

texts = ["Ankush worked at Facebook"]
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma.from_texts(texts, embeddings, collection_name="ankush")
retriever_ankush = vectorstore.as_retriever(search_kwargs={"k": 1})
```

## 查询分析

我们将使用函数调用来结构化输出。我们将让它返回多个查询。


```python
from typing import List, Optional

from langchain_core.pydantic_v1 import BaseModel, Field


class Search(BaseModel):
    """搜索有关人员信息的内容。"""

    query: str = Field(
        ...,
        description="要查询的内容",
    )
    person: str = Field(
        ...,
        description="要查询的人员。应该是 `HARRISON` 或者 `ANKUSH`。",
    )
```


```python
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

output_parser = PydanticToolsParser(tools=[Search])

system = """您可以发出搜索查询以获取有助于回答用户信息的信息。"""
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

我们可以看到这允许在检索器之间进行路由


```python
query_analyzer.invoke("Harrison在哪里工作")
```




    Search(query='工作地点', person='HARRISON')




```python
query_analyzer.invoke("Ankush在哪里工作")
```




    Search(query='工作地点', person='ANKUSH')



## 使用查询分析进行检索

那么我们如何将其包含在链式结构中呢？我们只需要一些简单的逻辑来选择检索器并传入搜索查询。


```python
from langchain_core.runnables import chain
```


```python
retrievers = {
    "HARRISON": retriever_harrison,
    "ANKUSH": retriever_ankush,
}
```


```python
@chain
def custom_chain(question):
    response = query_analyzer.invoke(question)
    retriever = retrievers[response.person]
    return retriever.invoke(response.query)
```


```python
custom_chain.invoke("Harrison在哪里工作")
```




    [Document(page_content='Harrison worked at Kensho')]




```python
custom_chain.invoke("Ankush在哪里工作")
```




    [Document(page_content='Ankush worked at Facebook')]






