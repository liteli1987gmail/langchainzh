# 每用户检索

当构建一个检索应用时，通常需要考虑多个用户。这意味着您可能不仅为一个用户存储数据，而是为许多不同的用户存储数据，而他们不应该能够看到彼此的数据。这意味着您需要能够配置检索链以仅检索特定信息。这通常包括两个步骤。

**第一步：确保您正在使用的检索器支持多个用户**

目前，在LangChain中没有统一的标志或过滤器来实现这一点。相反，每个向量存储器和检索器可能有自己的标志，并且可能被称为不同的东西（命名空间、多租户等）。对于向量存储器，这通常作为一个关键字参数在`similarity_search`期间传入。通过阅读文档或源代码，弄清楚您正在使用的检索器是否支持多个用户，如果支持，请了解如何使用它。

注意：为不支持多个用户的检索器（或记录）添加文档和/或支持是为LangChain做出贡献的绝佳途径

**第二步：将该参数添加为链的可配置字段**

这将使您能够轻松调用链并在运行时配置任何相关的标志。有关配置的更多信息，请参见[此文档](/expression_language/primitives/configure)。

**第三步：使用可配置的字段调用链**

现在，在运行时，您可以使用可配置的字段调用此链。

## 代码示例

让我们看一个具体的代码示例，看看它在代码中是什么样子。我们将使用Pinecone作为示例。

要配置Pinecone，请设置以下环境变量：

- `PINECONE_API_KEY`：您的Pinecone API密钥


```python
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
```


```python
embeddings = OpenAIEmbeddings()
vectorstore = PineconeVectorStore(index_name="test-example", embedding=embeddings)

vectorstore.add_texts(["我在肯晓工作"], namespace="harrison")
vectorstore.add_texts(["我在Facebook工作"], namespace="ankush")
```




    ['ce15571e-4e2f-44c9-98df-7e83f6f63095']



`namespace`参数用于区分文档


```python
# 这将仅获取Ankush的文档
vectorstore.as_retriever(search_kwargs={"namespace": "ankush"}).get_relevant_documents(
    "我在哪里工作过？"
)
```




    [Document(page_content='我在Facebook工作')]




```python
# 这将仅获取Harrison的文档
vectorstore.as_retriever(
    search_kwargs={"namespace": "harrison"}
).get_relevant_documents("我在哪里工作过？")
```




    [Document(page_content='我在肯晓工作')]



现在，我们可以创建将用于进行问答的链条


```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    ConfigurableField,
    RunnableBinding,
    RunnableLambda,
    RunnablePassthrough,
)
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
```

这是基本的问答链设置。


```python
template = """基于以下上下文回答问题：
{context}
问题：{question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI()

retriever = vectorstore.as_retriever()
```

在这里，我们将检索器标记为具有可配置字段。所有向量存储检索器都具有`search_kwargs`字段。这只是一个字典，具有特定于向量存储的字段


```python
configurable_retriever = retriever.configurable_fields(
    search_kwargs=ConfigurableField(
        id="search_kwargs",
        name="搜索参数",
        description="要使用的搜索参数",
    )
)
```

现在，我们可以使用可配置的检索器创建链条


```python
chain = (
    {"context": configurable_retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)
```

现在，我们可以使用可配置选项调用链条。`search_kwargs`是可配置字段的ID。值是用于Pinecone的搜索参数


```python
chain.invoke(
    "用户在哪里工作？",
    config={"configurable": {"search_kwargs": {"namespace": "harrison"}}},
)
```




    '用户在肯晓工作。'




```python
chain.invoke(
    "用户在哪里工作？",
    config={"configurable": {"search_kwargs": {"namespace": "ankush"}}},
)
```




    '用户在Facebook工作。'



有关用于多用户的更多向量存储实现，请参考特定页面，例如[Milvus](/docs/integrations/vectorstores/milvus)。