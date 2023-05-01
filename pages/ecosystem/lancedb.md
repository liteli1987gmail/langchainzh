


 LanceDB
 [#](#lancedb "Permalink to this headline")
=====================================================



 This page covers how to use
 [LanceDB](https://github.com/lancedb/lancedb) 
 within LangChain.
It is broken into two parts: installation and setup, and then references to specific LanceDB wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Python SDK with
 `pip
 

 install
 

 lancedb`





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 VectorStore
 [#](#vectorstore "Permalink to this headline")



 There exists a wrapper around LanceDB databases, allowing you to use it as a vectorstore,
whether for semantic search or example selection.
 



 To import this vectorstore:
 





```
from langchain.vectorstores import LanceDB

```




 For a more detailed walkthrough of the LanceDB wrapper, see
 
 this notebook
 







