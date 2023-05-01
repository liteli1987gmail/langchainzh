


 Llama.cpp
 [#](#llama-cpp "Permalink to this headline")
=========================================================



 This page covers how to use
 [llama.cpp](https://github.com/ggerganov/llama.cpp) 
 within LangChain.
It is broken into two parts: installation and setup, and then references to specific Llama-cpp wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Python package with
 `pip
 

 install
 

 llama-cpp-python`
* Download one of the
 [supported models](https://github.com/ggerganov/llama.cpp#description) 
 and convert them to the llama.cpp format per the
 [instructions](https://github.com/ggerganov/llama.cpp)





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 LLM
 [#](#llm "Permalink to this headline")



 There exists a LlamaCpp LLM wrapper, which you can access with
 





```
from langchain.llms import LlamaCpp

```




 For a more detailed walkthrough of this, see
 [this notebook](../modules/models/llms/integrations/llamacpp)





### 
 Embeddings
 [#](#embeddings "Permalink to this headline")



 There exists a LlamaCpp Embeddings wrapper, which you can access with
 





```
from langchain.embeddings import LlamaCppEmbeddings

```




 For a more detailed walkthrough of this, see
 [this notebook](../modules/models/text_embedding/examples/llamacpp)







