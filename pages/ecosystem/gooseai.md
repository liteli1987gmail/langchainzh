


 GooseAI
 [#](#gooseai "Permalink to this headline")
=====================================================



 This page covers how to use the GooseAI ecosystem within LangChain.
It is broken into two parts: installation and setup, and then references to specific GooseAI wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Python SDK with
 `pip
 

 install
 

 openai`
* Get your GooseAI api key from this link
 [here](https://goose.ai/) 
 .
* Set the environment variable (
 `GOOSEAI_API_KEY`
 ).





```
import os
os.environ["GOOSEAI_API_KEY"] = "YOUR_API_KEY"

```






 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 LLM
 [#](#llm "Permalink to this headline")



 There exists an GooseAI LLM wrapper, which you can access with:
 





```
from langchain.llms import GooseAI

```







