


 Jina
 [#](#jina "Permalink to this headline")
===============================================



 This page covers how to use the Jina ecosystem within LangChain.
It is broken into two parts: installation and setup, and then references to specific Jina wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Python SDK with
 `pip
 

 install
 

 jina`
* Get a Jina AI Cloud auth token from
 [here](https://cloud.jina.ai/settings/tokens) 
 and set it as an environment variable (
 `JINA_AUTH_TOKEN`
 )





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 Embeddings
 [#](#embeddings "Permalink to this headline")



 There exists a Jina Embeddings wrapper, which you can access with
 





```
from langchain.embeddings import JinaEmbeddings

```




 For a more detailed walkthrough of this, see
 [this notebook](../modules/models/text_embedding/examples/jina)







