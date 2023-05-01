


 Hazy Research
 [#](#hazy-research "Permalink to this headline")
=================================================================



 This page covers how to use the Hazy Research ecosystem within LangChain.
It is broken into two parts: installation and setup, and then references to specific Hazy Research wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* To use the
 `manifest`
 , install it with
 `pip
 

 install
 

 manifest-ml`





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 LLM
 [#](#llm "Permalink to this headline")



 There exists an LLM wrapper around Hazy Research’s
 `manifest`
 library.
 `manifest`
 is a python library which is itself a wrapper around many model providers, and adds in caching, history, and more.
 



 To use this wrapper:
 





```
from langchain.llms.manifest import ManifestWrapper

```







