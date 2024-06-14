
# 处理不生成查询的情况

有时，查询分析技术可能允许生成任意数量的查询 - 包括没有查询！在这种情况下，我们整体的链条在决定是否调用检索器之前需要检查查询分析的结果。

我们将在这个示例中使用模拟数据。

## 设置
#### 安装依赖


```python
# %pip install -qU langchain langchain-community langchain-openai chromadb
```

#### 设置环境变量

我们将在这个示例中使用OpenAI:


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 可选的，取消注释以在LangSmith上进行跟踪运行。在此处注册：https://smith.langchain.com。
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

### 创建索引

我们将创建一个虚假信息的向量存储。


```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

texts = ["Harrison worked at Kensho"]
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma.from_texts(
    texts,
    embeddings,
)
retriever = vectorstore.as_retriever()
```

## 查询分析

我们将使用函数调用来结构化输出。然而，我们将配置LLM，使其不需要调用表示搜索查询的函数（如果它决定不需要）。然后，我们将使用提示来进行查询分析，明确指出它应该何时和何时不应该进行搜索。


```python
from typing import Optional

from langchain_core.pydantic_v1 import BaseModel, Field


class Search(BaseModel):
    """对一组作业记录进行搜索。"""

    query: str = Field(
        ...,
        description="应用于作业记录的相似性搜索查询。",
    )
```


```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

system = """您有能力发出搜索查询以获得帮助回答用户信息。

您不需要查找事物。如果您不需要，只需正常回答即可。"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
structured_llm = llm.bind_tools([Search])
query_analyzer = {"question": RunnablePassthrough()} | prompt | structured_llm
```

我们可以看到通过调用这个函数，我们得到一个有时但并不总是返回工具调用的消息。


```python
query_analyzer.invoke("Harrison在哪里工作")
```




    AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_ZnoVX4j9Mn8wgChaORyd1cvq', 'function': {'arguments': '{"query":"Harrison"}', 'name': 'Search'}, 'type': 'function'}]})




```python
query_analyzer.invoke("你好！")
```




    AIMessage(content='你好！有什么我可以帮助你的吗？')



## 使用查询分析进行检索

那么我们如何将这个加入到链条中呢？让我们看下面的例子。


```python
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.runnables import chain

output_parser = PydanticToolsParser(tools=[Search])
```


```python
@chain
def custom_chain(question):
    response = query_analyzer.invoke(question)
    if "tool_calls" in response.additional_kwargs:
        query = output_parser.invoke(response)
        docs = retriever.invoke(query[0].query)
        # 可以在这里添加更多逻辑 - 比如另一个LLM调用
        return docs
    else:
        return response
```


```python
custom_chain.invoke("Harrison在哪里工作")
```

    请求的结果数 4 超过了索引中的元素数 1，更新 n_results = 1
    




    [Document(page_content='Harrison worked at Kensho')]




```python
custom_chain.invoke("你好！")
```




    AIMessage(content='你好！有什么我可以帮助你的吗？')






