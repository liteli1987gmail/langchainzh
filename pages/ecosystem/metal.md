

金属[#](#metal "到这个标题的永久链接")
==========================

本页介绍如何在LangChain内使用[Metal](https://getmetal.io)。

什么是Metal？[#](#what-is-metal "到这个标题的永久链接")
-----------------------------------------

Metal是一个为生产环境构建的托管检索和内存平台。将您的数据轻松索引到`Metal`并对其进行语义搜索和检索。



快速入门[#](#quick-start "到这个标题的永久链接")
----------------------------------

通过[创建一个Metal账号](https://app.getmetal.io/signup)开始入门。

然后，您可以轻松利用`MetalRetriever`类开始检索您的数据进行语义搜索、提示上下文等。该类需要一个`Metal`实例和一个要传递给Metal API的参数字典。

```
from langchain.retrievers import MetalRetriever
from metal_sdk.metal import Metal

metal = Metal("API_KEY", "CLIENT_ID", "INDEX_ID");
retriever = MetalRetriever(metal, params={"limit": 2})

docs = retriever.get_relevant_documents("search term")

```

