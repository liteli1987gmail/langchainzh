


 AtlasDB
 [#](#atlasdb "Permalink to this headline")
=====================================================



 This page covers how to use Nomic’s Atlas ecosystem within LangChain.
It is broken into two parts: installation and setup, and then references to specific Atlas wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Python package with
 `pip
 

 install
 

 nomic`
* Nomic is also included in langchains poetry extras
 `poetry
 

 install
 

 -E
 

 all`





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 VectorStore
 [#](#vectorstore "Permalink to this headline")



 There exists a wrapper around the Atlas neural database, allowing you to use it as a vectorstore.
This vectorstore also gives you full access to the underlying AtlasProject object, which will allow you to use the full range of Atlas map interactions, such as bulk tagging and automatic topic modeling.
Please see
 [the Atlas docs](https://docs.nomic.ai/atlas_api) 
 for more detailed information.
 



 To import this vectorstore:
 





```
from langchain.vectorstores import AtlasDB

```




 For a more detailed walkthrough of the AtlasDB wrapper, see
 [this notebook](../modules/indexes/vectorstores/examples/atlas)







