
Databerry
=========================

该页面介绍了在LangChain中使用Databerry（https://databerry.ai）的方法。

Databerry是一个开源的文档检索平台，可以连接个人数据和大型语言模型。

快速入门
--------------------------------------

从LangChain检索存储在Databerry中的文档非常容易！

```
from langchain.retrievers import DataberryRetriever

retriever = DataberryRetriever(
    datastore_url="https://api.databerry.ai/query/clg1xg2h80000l708dymr0fxc",
    # api_key="DATABERRY_API_KEY", # optional if datastore is public
    # top_k=10 # optional
)

docs = retriever.get_relevant_documents("What's Databerry?")

```

