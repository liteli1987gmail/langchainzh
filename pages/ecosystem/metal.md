


 Metal
 [#](#metal "Permalink to this headline")
=================================================



 This page covers how to use
 [Metal](https://getmetal.io) 
 within LangChain.
 




 What is Metal?
 [#](#what-is-metal "Permalink to this headline")
------------------------------------------------------------------



 Metal is a managed retrieval & memory platform built for production. Easily index your data into
 `Metal`
 and run semantic search and retrieval on it.
 









 Quick start
 [#](#quick-start "Permalink to this headline")
-------------------------------------------------------------



 Get started by
 [creating a Metal account](https://app.getmetal.io/signup) 
 .
 



 Then, you can easily take advantage of the
 `MetalRetriever`
 class to start retrieving your data for semantic search, prompting context, etc. This class takes a
 `Metal`
 instance and a dictionary of parameters to pass to the Metal API.
 





```
from langchain.retrievers import MetalRetriever
from metal_sdk.metal import Metal


metal = Metal("API_KEY", "CLIENT_ID", "INDEX_ID");
retriever = MetalRetriever(metal, params={"limit": 2})

docs = retriever.get_relevant_documents("search term")

```






