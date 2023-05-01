


 Cohere
 [#](#cohere "Permalink to this headline")
===================================================



 This page covers how to use the Cohere ecosystem within LangChain.
It is broken into two parts: installation and setup, and then references to specific Cohere wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Python SDK with
 `pip
 

 install
 

 cohere`
* Get an Cohere api key and set it as an environment variable (
 `COHERE_API_KEY`
 )





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 LLM
 [#](#llm "Permalink to this headline")



 There exists an Cohere LLM wrapper, which you can access with
 





```
from langchain.llms import Cohere

```





### 
 Embeddings
 [#](#embeddings "Permalink to this headline")



 There exists an Cohere Embeddings wrapper, which you can access with
 





```
from langchain.embeddings import CohereEmbeddings

```




 For a more detailed walkthrough of this, see
 [this notebook](../modules/models/text_embedding/examples/cohere)







