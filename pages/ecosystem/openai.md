


 OpenAI
 [#](#openai "Permalink to this headline")
===================================================



 This page covers how to use the OpenAI ecosystem within LangChain.
It is broken into two parts: installation and setup, and then references to specific OpenAI wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Python SDK with
 `pip
 

 install
 

 openai`
* Get an OpenAI api key and set it as an environment variable (
 `OPENAI_API_KEY`
 )
* If you want to use OpenAI’s tokenizer (only available for Python 3.9+), install it with
 `pip
 

 install
 

 tiktoken`





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 LLM
 [#](#llm "Permalink to this headline")



 There exists an OpenAI LLM wrapper, which you can access with
 





```
from langchain.llms import OpenAI

```




 If you are using a model hosted on Azure, you should use different wrapper for that:
 





```
from langchain.llms import AzureOpenAI

```




 For a more detailed walkthrough of the Azure wrapper, see
 [this notebook](../modules/models/llms/integrations/azure_openai_example)





### 
 Embeddings
 [#](#embeddings "Permalink to this headline")



 There exists an OpenAI Embeddings wrapper, which you can access with
 





```
from langchain.embeddings import OpenAIEmbeddings

```




 For a more detailed walkthrough of this, see
 [this notebook](../modules/models/text_embedding/examples/openai)





### 
 Tokenizer
 [#](#tokenizer "Permalink to this headline")



 There are several places you can use the
 `tiktoken`
 tokenizer. By default, it is used to count tokens
for OpenAI LLMs.
 



 You can also use it to count tokens when splitting documents with
 





```
from langchain.text_splitter import CharacterTextSplitter
CharacterTextSplitter.from_tiktoken_encoder(...)

```




 For a more detailed walkthrough of this, see
 [this notebook](../modules/indexes/text_splitters/examples/tiktoken)





### 
 Moderation
 [#](#moderation "Permalink to this headline")



 You can also access the OpenAI content moderation endpoint with
 





```
from langchain.chains import OpenAIModerationChain

```




 For a more detailed walkthrough of this, see
 [this notebook](../modules/chains/examples/moderation)







