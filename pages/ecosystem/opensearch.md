


 OpenSearch
 [#](#opensearch "Permalink to this headline")
===========================================================



 This page covers how to use the OpenSearch ecosystem within LangChain.
It is broken into two parts: installation and setup, and then references to specific OpenSearch wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Python package with
 `pip
 

 install
 

 opensearch-py`





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 VectorStore
 [#](#vectorstore "Permalink to this headline")



 There exists a wrapper around OpenSearch vector databases, allowing you to use it as a vectorstore
for semantic search using approximate vector search powered by lucene, nmslib and faiss engines
or using painless scripting and script scoring functions for bruteforce vector search.
 



 To import this vectorstore:
 





```
from langchain.vectorstores import OpenSearchVectorSearch

```




 For a more detailed walkthrough of the OpenSearch wrapper, see
 [this notebook](../modules/indexes/vectorstores/examples/opensearch)







