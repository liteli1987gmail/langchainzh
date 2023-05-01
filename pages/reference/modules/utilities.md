




 Utilities
 [#](#module-langchain.utilities "Permalink to this headline")
==========================================================================



 General utilities.
 




*pydantic
 

 model*


 langchain.utilities.
 



 ApifyWrapper
 

[[source]](../../_modules/langchain/utilities/apify#ApifyWrapper)
[#](#langchain.utilities.ApifyWrapper "Permalink to this definition") 



 Wrapper around Apify.
 



 To use, you should have the
 `apify-client`
 python package installed,
and the environment variable
 `APIFY_API_TOKEN`
 set with your API key, or pass
 
 apify_api_token
 
 as a named parameter to the constructor.
 




*field*


 apify_client
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.utilities.ApifyWrapper.apify_client "Permalink to this definition") 






*field*


 apify_client_async
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.utilities.ApifyWrapper.apify_client_async "Permalink to this definition") 






*async*


 acall_actor
 


 (
 
*actor_id
 



 :
 





 str*
 ,
 *run_input
 



 :
 





 Dict*
 ,
 *dataset_mapping_function
 



 :
 





 Callable
 


 [
 



 [
 


 Dict
 


 ]
 



 ,
 




 langchain.schema.Document
 


 ]*
 ,
 *\**
 ,
 *build
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *memory_mbytes
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 None*
 ,
 *timeout_secs
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 None*

 )
 


 →
 

[langchain.document_loaders.apify_dataset.ApifyDatasetLoader](document_loaders#langchain.document_loaders.ApifyDatasetLoader "langchain.document_loaders.apify_dataset.ApifyDatasetLoader")


[[source]](../../_modules/langchain/utilities/apify#ApifyWrapper.acall_actor)
[#](#langchain.utilities.ApifyWrapper.acall_actor "Permalink to this definition") 



 Run an Actor on the Apify platform and wait for results to be ready.
 




 Parameters
 

* **actor_id** 
 (
 *str* 
 ) – The ID or name of the Actor on the Apify platform.
* **run_input** 
 (
 *Dict* 
 ) – The input object of the Actor that you’re trying to run.
* **dataset_mapping_function** 
 (
 *Callable* 
 ) – A function that takes a single
dictionary (an Apify dataset item) and converts it to
an instance of the Document class.
* **build** 
 (
 *str* 
*,* 
*optional* 
 ) – Optionally specifies the actor build to run.
It can be either a build tag or build number.
* **memory_mbytes** 
 (
 *int* 
*,* 
*optional* 
 ) – Optional memory limit for the run,
in megabytes.
* **timeout_secs** 
 (
 *int* 
*,* 
*optional* 
 ) – Optional timeout for the run, in seconds.




 Returns
 




 A loader that will fetch the records from the
 


 Actor run’s default dataset.
 









 Return type
 


[ApifyDatasetLoader](document_loaders#langchain.document_loaders.ApifyDatasetLoader "langchain.document_loaders.ApifyDatasetLoader") 











 call_actor
 


 (
 
*actor_id
 



 :
 





 str*
 ,
 *run_input
 



 :
 





 Dict*
 ,
 *dataset_mapping_function
 



 :
 





 Callable
 


 [
 



 [
 


 Dict
 


 ]
 



 ,
 




 langchain.schema.Document
 


 ]*
 ,
 *\**
 ,
 *build
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *memory_mbytes
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 None*
 ,
 *timeout_secs
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 None*

 )
 


 →
 

[langchain.document_loaders.apify_dataset.ApifyDatasetLoader](document_loaders#langchain.document_loaders.ApifyDatasetLoader "langchain.document_loaders.apify_dataset.ApifyDatasetLoader")


[[source]](../../_modules/langchain/utilities/apify#ApifyWrapper.call_actor)
[#](#langchain.utilities.ApifyWrapper.call_actor "Permalink to this definition") 



 Run an Actor on the Apify platform and wait for results to be ready.
 




 Parameters
 

* **actor_id** 
 (
 *str* 
 ) – The ID or name of the Actor on the Apify platform.
* **run_input** 
 (
 *Dict* 
 ) – The input object of the Actor that you’re trying to run.
* **dataset_mapping_function** 
 (
 *Callable* 
 ) – A function that takes a single
dictionary (an Apify dataset item) and converts it to an
instance of the Document class.
* **build** 
 (
 *str* 
*,* 
*optional* 
 ) – Optionally specifies the actor build to run.
It can be either a build tag or build number.
* **memory_mbytes** 
 (
 *int* 
*,* 
*optional* 
 ) – Optional memory limit for the run,
in megabytes.
* **timeout_secs** 
 (
 *int* 
*,* 
*optional* 
 ) – Optional timeout for the run, in seconds.




 Returns
 




 A loader that will fetch the records from the
 


 Actor run’s default dataset.
 









 Return type
 


[ApifyDatasetLoader](document_loaders#langchain.document_loaders.ApifyDatasetLoader "langchain.document_loaders.ApifyDatasetLoader") 











*pydantic
 

 model*


 langchain.utilities.
 



 ArxivAPIWrapper
 

[[source]](../../_modules/langchain/utilities/arxiv#ArxivAPIWrapper)
[#](#langchain.utilities.ArxivAPIWrapper "Permalink to this definition") 



 Wrapper around ArxivAPI.
 



 To use, you should have the
 `arxiv`
 python package installed.
 <https://lukasschwab.me/arxiv.py/index>
 This wrapper will use the Arxiv API to conduct searches and
fetch document summaries. By default, it will return the document summaries
of the top-k results of an input search.
 




 Parameters
 

* **top_k_results** 
 – number of the top-scored document used for the arxiv tool
* **ARXIV_MAX_QUERY_LENGTH** 
 – the cut limit on the query used for the arxiv tool.
* **load_max_docs** 
 – a limit to the number of loaded documents
* **load_all_available_meta** 
 –
 

 if True: the
 
 metadata
 
 of the loaded Documents gets all available meta info
 


 (see
 <https://lukasschwab.me/arxiv.py/index#Result>
 ),
 





 if False: the
 
 metadata
 
 gets only the most informative fields.






*field*


 arxiv_exceptions
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.utilities.ArxivAPIWrapper.arxiv_exceptions "Permalink to this definition") 






*field*


 load_all_available_meta
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.utilities.ArxivAPIWrapper.load_all_available_meta "Permalink to this definition") 






*field*


 load_max_docs
 

*:
 




 int*
*=
 




 100*
[#](#langchain.utilities.ArxivAPIWrapper.load_max_docs "Permalink to this definition") 






*field*


 top_k_results
 

*:
 




 int*
*=
 




 3*
[#](#langchain.utilities.ArxivAPIWrapper.top_k_results "Permalink to this definition") 








 load
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/utilities/arxiv#ArxivAPIWrapper.load)
[#](#langchain.utilities.ArxivAPIWrapper.load "Permalink to this definition") 



 Run Arxiv search and get the PDF documents plus the meta information.
See
 <https://lukasschwab.me/arxiv.py/index#Search>




 Returns: a list of documents with the document.page_content in PDF format
 








 run
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/arxiv#ArxivAPIWrapper.run)
[#](#langchain.utilities.ArxivAPIWrapper.run "Permalink to this definition") 



 Run Arxiv search and get the document meta information.
See
 <https://lukasschwab.me/arxiv.py/index#Search>
 See
 <https://lukasschwab.me/arxiv.py/index#Result>
 It uses only the most informative fields of document meta information.
 








*class*


 langchain.utilities.
 



 BashProcess
 


 (
 
*strip_newlines
 



 :
 





 bool
 





 =
 





 False*
 ,
 *return_err_output
 



 :
 





 bool
 





 =
 





 False*
 ,
 *persistent
 



 :
 





 bool
 





 =
 





 False*

 )
 
[[source]](../../_modules/langchain/utilities/bash#BashProcess)
[#](#langchain.utilities.BashProcess "Permalink to this definition") 



 Executes bash commands and returns the output.
 






 process_output
 


 (
 
*output
 



 :
 





 str*
 ,
 *command
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/bash#BashProcess.process_output)
[#](#langchain.utilities.BashProcess.process_output "Permalink to this definition") 








 run
 


 (
 
*commands
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ]*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/bash#BashProcess.run)
[#](#langchain.utilities.BashProcess.run "Permalink to this definition") 



 Run commands and return final output.
 








*pydantic
 

 model*


 langchain.utilities.
 



 BingSearchAPIWrapper
 

[[source]](../../_modules/langchain/utilities/bing_search#BingSearchAPIWrapper)
[#](#langchain.utilities.BingSearchAPIWrapper "Permalink to this definition") 



 Wrapper for Bing Search API.
 



 In order to set this up, follow instructions at:
 <https://levelup.gitconnected.com/api-tutorial-how-to-use-bing-web-search-api-in-python-4165d5592a7e>





*field*


 bing_search_url
 

*:
 




 str*
*[Required]*
[#](#langchain.utilities.BingSearchAPIWrapper.bing_search_url "Permalink to this definition") 






*field*


 bing_subscription_key
 

*:
 




 str*
*[Required]*
[#](#langchain.utilities.BingSearchAPIWrapper.bing_subscription_key "Permalink to this definition") 






*field*


 k
 

*:
 




 int*
*=
 




 10*
[#](#langchain.utilities.BingSearchAPIWrapper.k "Permalink to this definition") 








 results
 


 (
 
*query
 



 :
 





 str*
 ,
 *num_results
 



 :
 





 int*

 )
 


 →
 


 List
 


 [
 


 Dict
 


 ]
 



[[source]](../../_modules/langchain/utilities/bing_search#BingSearchAPIWrapper.results)
[#](#langchain.utilities.BingSearchAPIWrapper.results "Permalink to this definition") 



 Run query through BingSearch and return metadata.
 




 Parameters
 

* **query** 
 – The query to search for.
* **num_results** 
 – The number of results to return.




 Returns
 


 snippet - The description of the result.
title - The title of the result.
link - The link to the result.
 




 Return type
 


 A list of dictionaries with the following keys
 










 run
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/bing_search#BingSearchAPIWrapper.run)
[#](#langchain.utilities.BingSearchAPIWrapper.run "Permalink to this definition") 



 Run query through BingSearch and parse result.
 








*pydantic
 

 model*


 langchain.utilities.
 



 GooglePlacesAPIWrapper
 

[[source]](../../_modules/langchain/utilities/google_places_api#GooglePlacesAPIWrapper)
[#](#langchain.utilities.GooglePlacesAPIWrapper "Permalink to this definition") 



 Wrapper around Google Places API.
 




 To use, you should have the
 `googlemaps`
 python package installed,
 


**an API key for the google maps platform** 
 ,
and the enviroment variable ‘’GPLACES_API_KEY’’
set with your API key , or pass ‘gplaces_api_key’
as a named parameter to the constructor.
 




 By default, this will return the all the results on the input query.
 


 You can use the top_k_results argument to limit the number of results.
 





 Example
 





```
from langchain import GooglePlacesAPIWrapper
gplaceapi = GooglePlacesAPIWrapper()

```





*field*


 gplaces_api_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.GooglePlacesAPIWrapper.gplaces_api_key "Permalink to this definition") 






*field*


 top_k_results
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.utilities.GooglePlacesAPIWrapper.top_k_results "Permalink to this definition") 








 fetch_place_details
 


 (
 
*place_id
 



 :
 





 str*

 )
 


 →
 


 Optional
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/utilities/google_places_api#GooglePlacesAPIWrapper.fetch_place_details)
[#](#langchain.utilities.GooglePlacesAPIWrapper.fetch_place_details "Permalink to this definition") 








 format_place_details
 


 (
 
*place_details
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*

 )
 


 →
 


 Optional
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/utilities/google_places_api#GooglePlacesAPIWrapper.format_place_details)
[#](#langchain.utilities.GooglePlacesAPIWrapper.format_place_details "Permalink to this definition") 








 run
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/google_places_api#GooglePlacesAPIWrapper.run)
[#](#langchain.utilities.GooglePlacesAPIWrapper.run "Permalink to this definition") 



 Run Places search and get k number of places that exists that match.
 








*pydantic
 

 model*


 langchain.utilities.
 



 GoogleSearchAPIWrapper
 

[[source]](../../_modules/langchain/utilities/google_search#GoogleSearchAPIWrapper)
[#](#langchain.utilities.GoogleSearchAPIWrapper "Permalink to this definition") 



 Wrapper for Google Search API.
 



 Adapted from: Instructions adapted from
 <https://stackoverflow.com/questions/>
 37083058/
programmatically-searching-google-in-python-using-custom-search
 



 TODO: DOCS for using it
1. Install google-api-python-client
- If you don’t already have a Google account, sign up.
- If you have never created a Google APIs Console project,
read the Managing Projects page and create a project in the Google API Console.
- Install the library using pip install google-api-python-client
The current version of the library is 2.70.0 at this time
 



 2. To create an API key:
- Navigate to the APIs & Services→Credentials panel in Cloud Console.
- Select Create credentials, then select API key from the drop-down menu.
- The API key created dialog box displays your newly created key.
- You now have an API_KEY
 



 3. Setup Custom Search Engine so you can search the entire web
- Create a custom search engine in this link.
- In Sites to search, add any valid URL (i.e. www.stackoverflow.com).
- That’s all you have to fill up, the rest doesn’t matter.
In the left-side menu, click Edit search engine → {your search engine name}
→ Setup Set Search the entire web to ON. Remove the URL you added from
 



> 
> 
> 
>  the list of Sites to search.
>  
> 
> 
> 
> 


* Under Search engine ID you’ll find the search-engine-ID.



 4. Enable the Custom Search API
- Navigate to the APIs & Services→Dashboard panel in Cloud Console.
- Click Enable APIs and Services.
- Search for Custom Search API and click on it.
- Click Enable.
URL for it:
 <https://console.cloud.google.com/apis/library/customsearch.googleapis>
 .com
 




*field*


 google_api_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.GoogleSearchAPIWrapper.google_api_key "Permalink to this definition") 






*field*


 google_cse_id
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.GoogleSearchAPIWrapper.google_cse_id "Permalink to this definition") 






*field*


 k
 

*:
 




 int*
*=
 




 10*
[#](#langchain.utilities.GoogleSearchAPIWrapper.k "Permalink to this definition") 






*field*


 siterestrict
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.utilities.GoogleSearchAPIWrapper.siterestrict "Permalink to this definition") 








 results
 


 (
 
*query
 



 :
 





 str*
 ,
 *num_results
 



 :
 





 int*

 )
 


 →
 


 List
 


 [
 


 Dict
 


 ]
 



[[source]](../../_modules/langchain/utilities/google_search#GoogleSearchAPIWrapper.results)
[#](#langchain.utilities.GoogleSearchAPIWrapper.results "Permalink to this definition") 



 Run query through GoogleSearch and return metadata.
 




 Parameters
 

* **query** 
 – The query to search for.
* **num_results** 
 – The number of results to return.




 Returns
 


 snippet - The description of the result.
title - The title of the result.
link - The link to the result.
 




 Return type
 


 A list of dictionaries with the following keys
 










 run
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/google_search#GoogleSearchAPIWrapper.run)
[#](#langchain.utilities.GoogleSearchAPIWrapper.run "Permalink to this definition") 



 Run query through GoogleSearch and parse result.
 








*pydantic
 

 model*


 langchain.utilities.
 



 GoogleSerperAPIWrapper
 

[[source]](../../_modules/langchain/utilities/google_serper#GoogleSerperAPIWrapper)
[#](#langchain.utilities.GoogleSerperAPIWrapper "Permalink to this definition") 



 Wrapper around the Serper.dev Google Search API.
 



 You can create a free API key at
 <https://serper.dev>
 .
 



 To use, you should have the environment variable
 `SERPER_API_KEY`
 set with your API key, or pass
 
 serper_api_key
 
 as a named parameter
to the constructor.
 



 Example
 





```
from langchain import GoogleSerperAPIWrapper
google_serper = GoogleSerperAPIWrapper()

```





*field*


 gl
 

*:
 




 str*
*=
 




 'us'*
[#](#langchain.utilities.GoogleSerperAPIWrapper.gl "Permalink to this definition") 






*field*


 hl
 

*:
 




 str*
*=
 




 'en'*
[#](#langchain.utilities.GoogleSerperAPIWrapper.hl "Permalink to this definition") 






*field*


 k
 

*:
 




 int*
*=
 




 10*
[#](#langchain.utilities.GoogleSerperAPIWrapper.k "Permalink to this definition") 






*field*


 serper_api_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.GoogleSerperAPIWrapper.serper_api_key "Permalink to this definition") 








 run
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/google_serper#GoogleSerperAPIWrapper.run)
[#](#langchain.utilities.GoogleSerperAPIWrapper.run "Permalink to this definition") 



 Run query through GoogleSearch and parse result.
 








*pydantic
 

 model*


 langchain.utilities.
 



 LambdaWrapper
 

[[source]](../../_modules/langchain/utilities/awslambda#LambdaWrapper)
[#](#langchain.utilities.LambdaWrapper "Permalink to this definition") 



 Wrapper for AWS Lambda SDK.
 



 Docs for using:
 


1. pip install boto3
2. Create a lambda function using the AWS Console or CLI
3. Run
 
 aws configure
 
 and enter your AWS credentials




*field*


 awslambda_tool_description
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.LambdaWrapper.awslambda_tool_description "Permalink to this definition") 






*field*


 awslambda_tool_name
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.LambdaWrapper.awslambda_tool_name "Permalink to this definition") 






*field*


 function_name
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.LambdaWrapper.function_name "Permalink to this definition") 








 run
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/awslambda#LambdaWrapper.run)
[#](#langchain.utilities.LambdaWrapper.run "Permalink to this definition") 



 Invoke Lambda function and parse result.
 








*pydantic
 

 model*


 langchain.utilities.
 



 OpenWeatherMapAPIWrapper
 

[[source]](../../_modules/langchain/utilities/openweathermap#OpenWeatherMapAPIWrapper)
[#](#langchain.utilities.OpenWeatherMapAPIWrapper "Permalink to this definition") 



 Wrapper for OpenWeatherMap API using PyOWM.
 



 Docs for using:
 


1. Go to OpenWeatherMap and sign up for an API key
2. Save your API KEY into OPENWEATHERMAP_API_KEY env variable
3. pip install pyowm




*field*


 openweathermap_api_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.OpenWeatherMapAPIWrapper.openweathermap_api_key "Permalink to this definition") 






*field*


 owm
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.utilities.OpenWeatherMapAPIWrapper.owm "Permalink to this definition") 








 run
 


 (
 
*location
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/openweathermap#OpenWeatherMapAPIWrapper.run)
[#](#langchain.utilities.OpenWeatherMapAPIWrapper.run "Permalink to this definition") 



 Get the current weather information for a specified location.
 








*pydantic
 

 model*


 langchain.utilities.
 



 PowerBIDataset
 

[[source]](../../_modules/langchain/utilities/powerbi#PowerBIDataset)
[#](#langchain.utilities.PowerBIDataset "Permalink to this definition") 



 Create PowerBI engine from dataset ID and credential or token.
 



 Use either the credential or a supplied token to authenticate.
If both are supplied the credential is used to generate a token.
The impersonated_user_name is the UPN of a user to be impersonated.
If the model is not RLS enabled, this will be ignored.
 




*field*


 aiosession
 

*:
 




 Optional
 


 [
 


 aiohttp.ClientSession
 


 ]*
*=
 




 None*
[#](#langchain.utilities.PowerBIDataset.aiosession "Permalink to this definition") 






*field*


 credential
 

*:
 




 Optional
 


 [
 


 TokenCredential
 


 ]*
*=
 




 None*
[#](#langchain.utilities.PowerBIDataset.credential "Permalink to this definition") 






*field*


 dataset_id
 

*:
 




 str*
*[Required]*
[#](#langchain.utilities.PowerBIDataset.dataset_id "Permalink to this definition") 






*field*


 group_id
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.PowerBIDataset.group_id "Permalink to this definition") 






*field*


 impersonated_user_name
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.PowerBIDataset.impersonated_user_name "Permalink to this definition") 






*field*


 sample_rows_in_table_info
 

*:
 




 int*
*=
 




 1*
[#](#langchain.utilities.PowerBIDataset.sample_rows_in_table_info "Permalink to this definition") 




 Constraints
 

* **exclusiveMinimum** 
 = 0
* **maximum** 
 = 10








*field*


 schemas
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]*
*[Optional]*
[#](#langchain.utilities.PowerBIDataset.schemas "Permalink to this definition") 






*field*


 table_names
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Required]*
[#](#langchain.utilities.PowerBIDataset.table_names "Permalink to this definition") 






*field*


 token
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.PowerBIDataset.token "Permalink to this definition") 






*async*


 aget_table_info
 


 (
 
*table_names
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ,
 




 str
 


 ]
 



 ]
 






 =
 





 None*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/powerbi#PowerBIDataset.aget_table_info)
[#](#langchain.utilities.PowerBIDataset.aget_table_info "Permalink to this definition") 



 Get information about specified tables.
 






*async*


 arun
 


 (
 
*command
 



 :
 





 str*

 )
 


 →
 


 Any
 


[[source]](../../_modules/langchain/utilities/powerbi#PowerBIDataset.arun)
[#](#langchain.utilities.PowerBIDataset.arun "Permalink to this definition") 



 Execute a DAX command and return the result asynchronously.
 








 get_schemas
 


 (
 

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/powerbi#PowerBIDataset.get_schemas)
[#](#langchain.utilities.PowerBIDataset.get_schemas "Permalink to this definition") 



 Get the available schema’s.
 








 get_table_info
 


 (
 
*table_names
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ,
 




 str
 


 ]
 



 ]
 






 =
 





 None*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/powerbi#PowerBIDataset.get_table_info)
[#](#langchain.utilities.PowerBIDataset.get_table_info "Permalink to this definition") 



 Get information about specified tables.
 








 get_table_names
 


 (
 

 )
 


 →
 


 Iterable
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/utilities/powerbi#PowerBIDataset.get_table_names)
[#](#langchain.utilities.PowerBIDataset.get_table_names "Permalink to this definition") 



 Get names of tables available.
 








 run
 


 (
 
*command
 



 :
 





 str*

 )
 


 →
 


 Any
 


[[source]](../../_modules/langchain/utilities/powerbi#PowerBIDataset.run)
[#](#langchain.utilities.PowerBIDataset.run "Permalink to this definition") 



 Execute a DAX command and return a json representing the results.
 






*property*


 headers
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]*
[#](#langchain.utilities.PowerBIDataset.headers "Permalink to this definition") 



 Get the token.
 






*property*


 request_url
 

*:
 




 str*
[#](#langchain.utilities.PowerBIDataset.request_url "Permalink to this definition") 



 Get the request url.
 






*property*


 table_info
 

*:
 




 str*
[#](#langchain.utilities.PowerBIDataset.table_info "Permalink to this definition") 



 Information about all tables in the database.
 








*pydantic
 

 model*


 langchain.utilities.
 



 PythonREPL
 

[[source]](../../_modules/langchain/utilities/python#PythonREPL)
[#](#langchain.utilities.PythonREPL "Permalink to this definition") 



 Simulates a standalone Python REPL.
 




*field*


 globals
 

*:
 




 Optional
 


 [
 


 Dict
 


 ]*
*[Optional]*
*(alias
 

 '_globals')*
[#](#langchain.utilities.PythonREPL.globals "Permalink to this definition") 






*field*


 locals
 

*:
 




 Optional
 


 [
 


 Dict
 


 ]*
*[Optional]*
*(alias
 

 '_locals')*
[#](#langchain.utilities.PythonREPL.locals "Permalink to this definition") 








 run
 


 (
 
*command
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/python#PythonREPL.run)
[#](#langchain.utilities.PythonREPL.run "Permalink to this definition") 



 Run command with own globals/locals and returns anything printed.
 








*pydantic
 

 model*


 langchain.utilities.
 



 SearxSearchWrapper
 

[[source]](../../_modules/langchain/utilities/searx_search#SearxSearchWrapper)
[#](#langchain.utilities.SearxSearchWrapper "Permalink to this definition") 



 Wrapper for Searx API.
 



 To use you need to provide the searx host by passing the named parameter
 `searx_host`
 or exporting the environment variable
 `SEARX_HOST`
 .
 



 In some situations you might want to disable SSL verification, for example
if you are running searx locally. You can do this by passing the named parameter
 `unsecure`
 . You can also pass the host url scheme as
 `http`
 to disable SSL.
 



 Example
 





```
from langchain.utilities import SearxSearchWrapper
searx = SearxSearchWrapper(searx_host="http://localhost:8888")

```





 Example with SSL disabled:
 




```
from langchain.utilities import SearxSearchWrapper
# note the unsecure parameter is not needed if you pass the url scheme as
# http
searx = SearxSearchWrapper(searx_host="http://localhost:8888",
                                        unsecure=True)

```







 Validators
 

* `disable_ssl_warnings`
 »
 [`unsecure`](searx_search#langchain.utilities.searx_search.SearxSearchWrapper.unsecure "langchain.utilities.searx_search.SearxSearchWrapper.unsecure")
* `validate_params`
 »
 `all
 

 fields`






*field*


 aiosession
 

*:
 




 Optional
 


 [
 


 Any
 


 ]*
*=
 




 None*
[#](#langchain.utilities.SearxSearchWrapper.aiosession "Permalink to this definition") 






*field*


 categories
 

*:
 




 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 []*
[#](#langchain.utilities.SearxSearchWrapper.categories "Permalink to this definition") 






*field*


 engines
 

*:
 




 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 []*
[#](#langchain.utilities.SearxSearchWrapper.engines "Permalink to this definition") 






*field*


 headers
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.utilities.SearxSearchWrapper.headers "Permalink to this definition") 






*field*


 k
 

*:
 




 int*
*=
 




 10*
[#](#langchain.utilities.SearxSearchWrapper.k "Permalink to this definition") 






*field*


 params
 

*:
 




 dict*
*[Optional]*
[#](#langchain.utilities.SearxSearchWrapper.params "Permalink to this definition") 






*field*


 query_suffix
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 ''*
[#](#langchain.utilities.SearxSearchWrapper.query_suffix "Permalink to this definition") 






*field*


 searx_host
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.utilities.SearxSearchWrapper.searx_host "Permalink to this definition") 






*field*


 unsecure
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.utilities.SearxSearchWrapper.unsecure "Permalink to this definition") 






*async*


 aresults
 


 (
 
*query
 



 :
 





 str*
 ,
 *num_results
 



 :
 





 int*
 ,
 *engines
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *query_suffix
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 ''*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 Dict
 


 ]
 



[[source]](../../_modules/langchain/utilities/searx_search#SearxSearchWrapper.aresults)
[#](#langchain.utilities.SearxSearchWrapper.aresults "Permalink to this definition") 



 Asynchronously query with json results.
 



 Uses aiohttp. See
 
 results
 
 for more info.
 






*async*


 arun
 


 (
 
*query
 



 :
 





 str*
 ,
 *engines
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *query_suffix
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 ''*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/searx_search#SearxSearchWrapper.arun)
[#](#langchain.utilities.SearxSearchWrapper.arun "Permalink to this definition") 



 Asynchronously version of
 
 run
 
 .
 








 results
 


 (
 
*query
 



 :
 





 str*
 ,
 *num_results
 



 :
 





 int*
 ,
 *engines
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *categories
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *query_suffix
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 ''*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 Dict
 


 ]
 



[[source]](../../_modules/langchain/utilities/searx_search#SearxSearchWrapper.results)
[#](#langchain.utilities.SearxSearchWrapper.results "Permalink to this definition") 



 Run query through Searx API and returns the results with metadata.
 




 Parameters
 

* **query** 
 – The query to search for.
* **query_suffix** 
 – Extra suffix appended to the query.
* **num_results** 
 – Limit the number of results to return.
* **engines** 
 – List of engines to use for the query.
* **categories** 
 – List of categories to use for the query.
* **\*\*kwargs** 
 – extra parameters to pass to the searx API.




 Returns
 




 {
 


 snippet: The description of the result.
 



 title: The title of the result.
 



 link: The link to the result.
 



 engines: The engines used for the result.
 



 category: Searx category of the result.
 





 }
 







 Return type
 


 Dict with the following keys
 










 run
 


 (
 
*query
 



 :
 





 str*
 ,
 *engines
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *categories
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *query_suffix
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 ''*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/searx_search#SearxSearchWrapper.run)
[#](#langchain.utilities.SearxSearchWrapper.run "Permalink to this definition") 



 Run query through Searx API and parse results.
 



 You can pass any other params to the searx query API.
 




 Parameters
 

* **query** 
 – The query to search for.
* **query_suffix** 
 – Extra suffix appended to the query.
* **engines** 
 – List of engines to use for the query.
* **categories** 
 – List of categories to use for the query.
* **\*\*kwargs** 
 – extra parameters to pass to the searx API.




 Returns
 


 The result of the query.
 




 Return type
 


 str
 




 Raises
 


**ValueError** 
 – If an error occured with the query.
 





 Example
 



 This will make a query to the qwant engine:
 





```
from langchain.utilities import SearxSearchWrapper
searx = SearxSearchWrapper(searx_host="http://my.searx.host")
searx.run("what is the weather in France ?", engine="qwant")

# the same result can be achieved using the `!` syntax of searx
# to select the engine using `query_suffix`
searx.run("what is the weather in France ?", query_suffix="!qwant")

```









*pydantic
 

 model*


 langchain.utilities.
 



 SerpAPIWrapper
 

[[source]](../../_modules/langchain/utilities/serpapi#SerpAPIWrapper)
[#](#langchain.utilities.SerpAPIWrapper "Permalink to this definition") 



 Wrapper around SerpAPI.
 



 To use, you should have the
 `google-search-results`
 python package installed,
and the environment variable
 `SERPAPI_API_KEY`
 set with your API key, or pass
 
 serpapi_api_key
 
 as a named parameter to the constructor.
 



 Example
 





```
from langchain import SerpAPIWrapper
serpapi = SerpAPIWrapper()

```





*field*


 aiosession
 

*:
 




 Optional
 


 [
 


 aiohttp.client.ClientSession
 


 ]*
*=
 




 None*
[#](#langchain.utilities.SerpAPIWrapper.aiosession "Permalink to this definition") 






*field*


 params
 

*:
 




 dict*
*=
 




 {'engine':
 

 'google',
 

 'gl':
 

 'us',
 

 'google_domain':
 

 'google.com',
 

 'hl':
 

 'en'}*
[#](#langchain.utilities.SerpAPIWrapper.params "Permalink to this definition") 






*field*


 serpapi_api_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.SerpAPIWrapper.serpapi_api_key "Permalink to this definition") 






*async*


 aresults
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 dict
 


[[source]](../../_modules/langchain/utilities/serpapi#SerpAPIWrapper.aresults)
[#](#langchain.utilities.SerpAPIWrapper.aresults "Permalink to this definition") 



 Use aiohttp to run query through SerpAPI and return the results async.
 






*async*


 arun
 


 (
 
*query
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/serpapi#SerpAPIWrapper.arun)
[#](#langchain.utilities.SerpAPIWrapper.arun "Permalink to this definition") 



 Run query through SerpAPI and parse result async.
 








 get_params
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



[[source]](../../_modules/langchain/utilities/serpapi#SerpAPIWrapper.get_params)
[#](#langchain.utilities.SerpAPIWrapper.get_params "Permalink to this definition") 



 Get parameters for SerpAPI.
 








 results
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 dict
 


[[source]](../../_modules/langchain/utilities/serpapi#SerpAPIWrapper.results)
[#](#langchain.utilities.SerpAPIWrapper.results "Permalink to this definition") 



 Run query through SerpAPI and return the raw result.
 








 run
 


 (
 
*query
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/serpapi#SerpAPIWrapper.run)
[#](#langchain.utilities.SerpAPIWrapper.run "Permalink to this definition") 



 Run query through SerpAPI and parse result.
 








*pydantic
 

 model*


 langchain.utilities.
 



 TextRequestsWrapper
 

[[source]](../../_modules/langchain/requests#TextRequestsWrapper)
[#](#langchain.utilities.TextRequestsWrapper "Permalink to this definition") 



 Lightweight wrapper around requests library.
 



 The main purpose of this wrapper is to always return a text output.
 




*field*


 aiosession
 

*:
 




 Optional
 


 [
 


 aiohttp.client.ClientSession
 


 ]*
*=
 




 None*
[#](#langchain.utilities.TextRequestsWrapper.aiosession "Permalink to this definition") 






*field*


 headers
 

*:
 




 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.utilities.TextRequestsWrapper.headers "Permalink to this definition") 






*async*


 adelete
 


 (
 
*url
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/requests#TextRequestsWrapper.adelete)
[#](#langchain.utilities.TextRequestsWrapper.adelete "Permalink to this definition") 



 DELETE the URL and return the text asynchronously.
 






*async*


 aget
 


 (
 
*url
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/requests#TextRequestsWrapper.aget)
[#](#langchain.utilities.TextRequestsWrapper.aget "Permalink to this definition") 



 GET the URL and return the text asynchronously.
 






*async*


 apatch
 


 (
 
*url
 



 :
 





 str*
 ,
 *data
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/requests#TextRequestsWrapper.apatch)
[#](#langchain.utilities.TextRequestsWrapper.apatch "Permalink to this definition") 



 PATCH the URL and return the text asynchronously.
 






*async*


 apost
 


 (
 
*url
 



 :
 





 str*
 ,
 *data
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/requests#TextRequestsWrapper.apost)
[#](#langchain.utilities.TextRequestsWrapper.apost "Permalink to this definition") 



 POST to the URL and return the text asynchronously.
 






*async*


 aput
 


 (
 
*url
 



 :
 





 str*
 ,
 *data
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/requests#TextRequestsWrapper.aput)
[#](#langchain.utilities.TextRequestsWrapper.aput "Permalink to this definition") 



 PUT the URL and return the text asynchronously.
 








 delete
 


 (
 
*url
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/requests#TextRequestsWrapper.delete)
[#](#langchain.utilities.TextRequestsWrapper.delete "Permalink to this definition") 



 DELETE the URL and return the text.
 








 get
 


 (
 
*url
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/requests#TextRequestsWrapper.get)
[#](#langchain.utilities.TextRequestsWrapper.get "Permalink to this definition") 



 GET the URL and return the text.
 








 patch
 


 (
 
*url
 



 :
 





 str*
 ,
 *data
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/requests#TextRequestsWrapper.patch)
[#](#langchain.utilities.TextRequestsWrapper.patch "Permalink to this definition") 



 PATCH the URL and return the text.
 








 post
 


 (
 
*url
 



 :
 





 str*
 ,
 *data
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/requests#TextRequestsWrapper.post)
[#](#langchain.utilities.TextRequestsWrapper.post "Permalink to this definition") 



 POST to the URL and return the text.
 








 put
 


 (
 
*url
 



 :
 





 str*
 ,
 *data
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/requests#TextRequestsWrapper.put)
[#](#langchain.utilities.TextRequestsWrapper.put "Permalink to this definition") 



 PUT the URL and return the text.
 






*property*


 requests
 

*:
 




 langchain.requests.Requests*
[#](#langchain.utilities.TextRequestsWrapper.requests "Permalink to this definition") 








*pydantic
 

 model*


 langchain.utilities.
 



 WikipediaAPIWrapper
 

[[source]](../../_modules/langchain/utilities/wikipedia#WikipediaAPIWrapper)
[#](#langchain.utilities.WikipediaAPIWrapper "Permalink to this definition") 



 Wrapper around WikipediaAPI.
 



 To use, you should have the
 `wikipedia`
 python package installed.
This wrapper will use the Wikipedia API to conduct searches and
fetch page summaries. By default, it will return the page summaries
of the top-k results of an input search.
 




*field*


 lang
 

*:
 




 str*
*=
 




 'en'*
[#](#langchain.utilities.WikipediaAPIWrapper.lang "Permalink to this definition") 






*field*


 top_k_results
 

*:
 




 int*
*=
 




 3*
[#](#langchain.utilities.WikipediaAPIWrapper.top_k_results "Permalink to this definition") 








 fetch_formatted_page_summary
 


 (
 
*page
 



 :
 





 str*

 )
 


 →
 


 Optional
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/utilities/wikipedia#WikipediaAPIWrapper.fetch_formatted_page_summary)
[#](#langchain.utilities.WikipediaAPIWrapper.fetch_formatted_page_summary "Permalink to this definition") 








 run
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/wikipedia#WikipediaAPIWrapper.run)
[#](#langchain.utilities.WikipediaAPIWrapper.run "Permalink to this definition") 



 Run Wikipedia search and get page summaries.
 








*pydantic
 

 model*


 langchain.utilities.
 



 WolframAlphaAPIWrapper
 

[[source]](../../_modules/langchain/utilities/wolfram_alpha#WolframAlphaAPIWrapper)
[#](#langchain.utilities.WolframAlphaAPIWrapper "Permalink to this definition") 



 Wrapper for Wolfram Alpha.
 



 Docs for using:
 


1. Go to wolfram alpha and sign up for a developer account
2. Create an app and get your APP ID
3. Save your APP ID into WOLFRAM_ALPHA_APPID env variable
4. pip install wolframalpha




*field*


 wolfram_alpha_appid
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.utilities.WolframAlphaAPIWrapper.wolfram_alpha_appid "Permalink to this definition") 








 run
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/utilities/wolfram_alpha#WolframAlphaAPIWrapper.run)
[#](#langchain.utilities.WolframAlphaAPIWrapper.run "Permalink to this definition") 



 Run query through WolframAlpha and parse result.
 








