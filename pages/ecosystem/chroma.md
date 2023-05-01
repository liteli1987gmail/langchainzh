


 Chroma
 [#](#chroma "Permalink to this headline")
===================================================



 This page covers how to use the Chroma ecosystem within LangChain.
It is broken into two parts: installation and setup, and then references to specific Chroma wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Python package with
 `pip
 

 install
 

 chromadb`





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 VectorStore
 [#](#vectorstore "Permalink to this headline")



 There exists a wrapper around Chroma vector databases, allowing you to use it as a vectorstore,
whether for semantic search or example selection.
 



 To import this vectorstore:
 





```
from langchain.vectorstores import Chroma

```




 For a more detailed walkthrough of the Chroma wrapper, see
 [this notebook](../modules/indexes/vectorstores/getting_started)







