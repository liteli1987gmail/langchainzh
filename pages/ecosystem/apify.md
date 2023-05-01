


 Apify
 [#](#apify "Permalink to this headline")
=================================================



 This page covers how to use
 [Apify](https://apify.com) 
 within LangChain.
 




 Overview
 [#](#overview "Permalink to this headline")
-------------------------------------------------------



 Apify is a cloud platform for web scraping and data extraction,
which provides an
 [ecosystem](https://apify.com/store) 
 of more than a thousand
ready-made apps called
 *Actors* 
 for various scraping, crawling, and extraction use cases.
 







 This integration enables you run Actors on the Apify platform and load their results into LangChain to feed your vector
indexes with documents and data from the web, e.g. to generate answers from websites with documentation,
blogs, or knowledge bases.
 





 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Apify API client for Python with
 `pip
 

 install
 

 apify-client`
* Get your
 [Apify API token](https://console.apify.com/account/integrations) 
 and either set it as
an environment variable (
 `APIFY_API_TOKEN`
 ) or pass it to the
 `ApifyWrapper`
 as
 `apify_api_token`
 in the constructor.





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 Utility
 [#](#utility "Permalink to this headline")



 You can use the
 `ApifyWrapper`
 to run Actors on the Apify platform.
 





```
from langchain.utilities import ApifyWrapper

```




 For a more detailed walkthrough of this wrapper, see
 [this notebook](../modules/agents/tools/examples/apify)
 .
 




### 
 Loader
 [#](#loader "Permalink to this headline")



 You can also use our
 `ApifyDatasetLoader`
 to get data from Apify dataset.
 





```
from langchain.document_loaders import ApifyDatasetLoader

```




 For a more detailed walkthrough of this loader, see
 [this notebook](../modules/indexes/document_loaders/examples/apify_dataset)
 .
 






