


 Google Search Wrapper
 [#](#google-search-wrapper "Permalink to this headline")
=================================================================================



 This page covers how to use the Google Search API within LangChain.
It is broken into two parts: installation and setup, and then references to the specific Google Search wrapper.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install requirements with
 `pip
 

 install
 

 google-api-python-client`
* Set up a Custom Search Engine, following
 [these instructions](https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search)
* Get an API Key and Custom Search Engine ID from the previous step, and set them as environment variables
 `GOOGLE_API_KEY`
 and
 `GOOGLE_CSE_ID`
 respectively





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 Utility
 [#](#utility "Permalink to this headline")



 There exists a GoogleSearchAPIWrapper utility which wraps this API. To import this utility:
 





```
from langchain.utilities import GoogleSearchAPIWrapper

```




 For a more detailed walkthrough of this wrapper, see
 [this notebook](../modules/agents/tools/examples/google_search)
 .
 




### 
 Tool
 [#](#tool "Permalink to this headline")



 You can also easily load this wrapper as a Tool (to use with an Agent).
You can do this with:
 





```
from langchain.agents import load_tools
tools = load_tools(["google-search"])

```




 For more information on this, see
 [this page](../modules/agents/tools/getting_started)







