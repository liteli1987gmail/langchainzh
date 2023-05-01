




 Tools
 [#](#module-langchain.tools "Permalink to this headline")
==================================================================



 Core toolkit implementations.
 




*pydantic
 

 model*


 langchain.tools.
 



 AIPluginTool
 

[[source]](../../_modules/langchain/tools/plugin#AIPluginTool)
[#](#langchain.tools.AIPluginTool "Permalink to this definition") 




*field*


 api_spec
 

*:
 




 str*
*[Required]*
[#](#langchain.tools.AIPluginTool.api_spec "Permalink to this definition") 






*field*


 args_schema
 

*:
 




 Type
 


 [
 


 AIPLuginToolSchema
 


 ]*
*=
 




 <class
 

 'langchain.tools.plugin.AIPLuginToolSchema'>*
[#](#langchain.tools.AIPluginTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 plugin
 

*:
 




 AIPlugin*
*[Required]*
[#](#langchain.tools.AIPluginTool.plugin "Permalink to this definition") 






*classmethod*


 from_plugin_url
 


 (
 
*url
 



 :
 





 str*

 )
 


 →
 

[langchain.tools.plugin.AIPluginTool](#langchain.tools.AIPluginTool "langchain.tools.plugin.AIPluginTool")


[[source]](../../_modules/langchain/tools/plugin#AIPluginTool.from_plugin_url)
[#](#langchain.tools.AIPluginTool.from_plugin_url "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 APIOperation
 

[[source]](../../_modules/langchain/tools/openapi/utils/api_models#APIOperation)
[#](#langchain.tools.APIOperation "Permalink to this definition") 



 A model for a single API operation.
 




*field*


 base_url
 

*:
 




 str*
*[Required]*
[#](#langchain.tools.APIOperation.base_url "Permalink to this definition") 



 The base URL of the operation.
 






*field*


 description
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.tools.APIOperation.description "Permalink to this definition") 



 The description of the operation.
 






*field*


 method
 

*:
 




 langchain.tools.openapi.utils.openapi_utils.HTTPVerb*
*[Required]*
[#](#langchain.tools.APIOperation.method "Permalink to this definition") 



 The HTTP method of the operation.
 






*field*


 operation_id
 

*:
 




 str*
*[Required]*
[#](#langchain.tools.APIOperation.operation_id "Permalink to this definition") 



 The unique identifier of the operation.
 






*field*


 path
 

*:
 




 str*
*[Required]*
[#](#langchain.tools.APIOperation.path "Permalink to this definition") 



 The path of the operation.
 






*field*


 properties
 

*:
 




 Sequence
 


 [
 


 langchain.tools.openapi.utils.api_models.APIProperty
 


 ]*
*[Required]*
[#](#langchain.tools.APIOperation.properties "Permalink to this definition") 






*field*


 request_body
 

*:
 




 Optional
 


 [
 


 langchain.tools.openapi.utils.api_models.APIRequestBody
 


 ]*
*=
 




 None*
[#](#langchain.tools.APIOperation.request_body "Permalink to this definition") 



 The request body of the operation.
 






*classmethod*


 from_openapi_spec
 


 (
 
*spec
 



 :
 




[langchain.tools.openapi.utils.openapi_utils.OpenAPISpec](#langchain.tools.OpenAPISpec "langchain.tools.openapi.utils.openapi_utils.OpenAPISpec")*
 ,
 *path
 



 :
 





 str*
 ,
 *method
 



 :
 





 str*

 )
 


 →
 

[langchain.tools.openapi.utils.api_models.APIOperation](#langchain.tools.APIOperation "langchain.tools.openapi.utils.api_models.APIOperation")


[[source]](../../_modules/langchain/tools/openapi/utils/api_models#APIOperation.from_openapi_spec)
[#](#langchain.tools.APIOperation.from_openapi_spec "Permalink to this definition") 



 Create an APIOperation from an OpenAPI spec.
 






*classmethod*


 from_openapi_url
 


 (
 
*spec_url
 



 :
 





 str*
 ,
 *path
 



 :
 





 str*
 ,
 *method
 



 :
 





 str*

 )
 


 →
 

[langchain.tools.openapi.utils.api_models.APIOperation](#langchain.tools.APIOperation "langchain.tools.openapi.utils.api_models.APIOperation")


[[source]](../../_modules/langchain/tools/openapi/utils/api_models#APIOperation.from_openapi_url)
[#](#langchain.tools.APIOperation.from_openapi_url "Permalink to this definition") 



 Create an APIOperation from an OpenAPI URL.
 








 to_typescript
 


 (
 

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/tools/openapi/utils/api_models#APIOperation.to_typescript)
[#](#langchain.tools.APIOperation.to_typescript "Permalink to this definition") 



 Get typescript string representation of the operation.
 






*static*


 ts_type_from_python
 


 (
 
*type_
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 Type
 


 ,
 




 tuple
 


 ,
 




 None
 


 ,
 




 enum.Enum
 


 ]*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/tools/openapi/utils/api_models#APIOperation.ts_type_from_python)
[#](#langchain.tools.APIOperation.ts_type_from_python "Permalink to this definition") 






*property*


 body_params
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.tools.APIOperation.body_params "Permalink to this definition") 






*property*


 path_params
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.tools.APIOperation.path_params "Permalink to this definition") 






*property*


 query_params
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.tools.APIOperation.query_params "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 BaseTool
 

[[source]](../../_modules/langchain/tools/base#BaseTool)
[#](#langchain.tools.BaseTool "Permalink to this definition") 



 Interface LangChain tools must implement.
 




*field*


 args_schema
 

*:
 




 Optional
 


 [
 


 Type
 


 [
 


 pydantic.main.BaseModel
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.tools.BaseTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 callback_manager
 

*:
 




 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]*
*=
 




 None*
[#](#langchain.tools.BaseTool.callback_manager "Permalink to this definition") 



 Deprecated. Please use callbacks instead.
 






*field*


 callbacks
 

*:
 




 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.tools.BaseTool.callbacks "Permalink to this definition") 



 Callbacks to be called during tool execution.
 






*field*


 description
 

*:
 




 str*
*[Required]*
[#](#langchain.tools.BaseTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*[Required]*
[#](#langchain.tools.BaseTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 






*field*


 return_direct
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.tools.BaseTool.return_direct "Permalink to this definition") 



 Whether to return the tool’s output directly. Setting this to True means
 



 that after the tool is called, the AgentExecutor will stop looping.
 






*field*


 verbose
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.tools.BaseTool.verbose "Permalink to this definition") 



 Whether to log the tool’s progress.
 






*async*


 arun
 


 (
 
*tool_input
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 Dict
 


 ]*
 ,
 *verbose
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *start_color
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'green'*
 ,
 *color
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'green'*
 ,
 *callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Any
 


[[source]](../../_modules/langchain/tools/base#BaseTool.arun)
[#](#langchain.tools.BaseTool.arun "Permalink to this definition") 



 Run the tool asynchronously.
 








 run
 


 (
 
*tool_input
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 Dict
 


 ]*
 ,
 *verbose
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *start_color
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'green'*
 ,
 *color
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'green'*
 ,
 *callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Any
 


[[source]](../../_modules/langchain/tools/base#BaseTool.run)
[#](#langchain.tools.BaseTool.run "Permalink to this definition") 



 Run the tool.
 






*property*


 args
 

*:
 




 dict*
[#](#langchain.tools.BaseTool.args "Permalink to this definition") 






*property*


 is_single_input
 

*:
 




 bool*
[#](#langchain.tools.BaseTool.is_single_input "Permalink to this definition") 



 Whether the tool only accepts a single input.
 








*pydantic
 

 model*


 langchain.tools.
 



 BingSearchResults
 

[[source]](../../_modules/langchain/tools/bing_search/tool#BingSearchResults)
[#](#langchain.tools.BingSearchResults "Permalink to this definition") 



 Tool that has capability to query the Bing Search API and get back json.
 




*field*


 api_wrapper
 

*:
 



[langchain.utilities.bing_search.BingSearchAPIWrapper](utilities#langchain.utilities.BingSearchAPIWrapper "langchain.utilities.bing_search.BingSearchAPIWrapper")*
*[Required]*
[#](#langchain.tools.BingSearchResults.api_wrapper "Permalink to this definition") 






*field*


 num_results
 

*:
 




 int*
*=
 




 4*
[#](#langchain.tools.BingSearchResults.num_results "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 BingSearchRun
 

[[source]](../../_modules/langchain/tools/bing_search/tool#BingSearchRun)
[#](#langchain.tools.BingSearchRun "Permalink to this definition") 



 Tool that adds the capability to query the Bing search API.
 




*field*


 api_wrapper
 

*:
 



[langchain.utilities.bing_search.BingSearchAPIWrapper](utilities#langchain.utilities.BingSearchAPIWrapper "langchain.utilities.bing_search.BingSearchAPIWrapper")*
*[Required]*
[#](#langchain.tools.BingSearchRun.api_wrapper "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 ClickTool
 

[[source]](../../_modules/langchain/tools/playwright/click#ClickTool)
[#](#langchain.tools.ClickTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.playwright.click.ClickToolInput'>*
[#](#langchain.tools.ClickTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Click
 

 on
 

 an
 

 element
 

 with
 

 the
 

 given
 

 CSS
 

 selector'*
[#](#langchain.tools.ClickTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'click_element'*
[#](#langchain.tools.ClickTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 CopyFileTool
 

[[source]](../../_modules/langchain/tools/file_management/copy#CopyFileTool)
[#](#langchain.tools.CopyFileTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 pydantic.main.BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.file_management.copy.FileCopyInput'>*
[#](#langchain.tools.CopyFileTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Create
 

 a
 

 copy
 

 of
 

 a
 

 file
 

 in
 

 a
 

 specified
 

 location'*
[#](#langchain.tools.CopyFileTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'copy_file'*
[#](#langchain.tools.CopyFileTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 CurrentWebPageTool
 

[[source]](../../_modules/langchain/tools/playwright/current_page#CurrentWebPageTool)
[#](#langchain.tools.CurrentWebPageTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 BaseModel
 


 ]*
*=
 




 <class
 

 'pydantic.main.BaseModel'>*
[#](#langchain.tools.CurrentWebPageTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Returns
 

 the
 

 URL
 

 of
 

 the
 

 current
 

 page'*
[#](#langchain.tools.CurrentWebPageTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'current_webpage'*
[#](#langchain.tools.CurrentWebPageTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 DeleteFileTool
 

[[source]](../../_modules/langchain/tools/file_management/delete#DeleteFileTool)
[#](#langchain.tools.DeleteFileTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 pydantic.main.BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.file_management.delete.FileDeleteInput'>*
[#](#langchain.tools.DeleteFileTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Delete
 

 a
 

 file'*
[#](#langchain.tools.DeleteFileTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'file_delete'*
[#](#langchain.tools.DeleteFileTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 DuckDuckGoSearchResults
 

[[source]](../../_modules/langchain/tools/ddg_search/tool#DuckDuckGoSearchResults)
[#](#langchain.tools.DuckDuckGoSearchResults "Permalink to this definition") 



 Tool that queries the Duck Duck Go Search API and get back json.
 




*field*


 api_wrapper
 

*:
 




 langchain.utilities.duckduckgo_search.DuckDuckGoSearchAPIWrapper*
*[Optional]*
[#](#langchain.tools.DuckDuckGoSearchResults.api_wrapper "Permalink to this definition") 






*field*


 num_results
 

*:
 




 int*
*=
 




 4*
[#](#langchain.tools.DuckDuckGoSearchResults.num_results "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 DuckDuckGoSearchRun
 

[[source]](../../_modules/langchain/tools/ddg_search/tool#DuckDuckGoSearchRun)
[#](#langchain.tools.DuckDuckGoSearchRun "Permalink to this definition") 



 Tool that adds the capability to query the DuckDuckGo search API.
 




*field*


 api_wrapper
 

*:
 




 langchain.utilities.duckduckgo_search.DuckDuckGoSearchAPIWrapper*
*[Optional]*
[#](#langchain.tools.DuckDuckGoSearchRun.api_wrapper "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 ExtractHyperlinksTool
 

[[source]](../../_modules/langchain/tools/playwright/extract_hyperlinks#ExtractHyperlinksTool)
[#](#langchain.tools.ExtractHyperlinksTool "Permalink to this definition") 



 Extract all hyperlinks on the page.
 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.playwright.extract_hyperlinks.ExtractHyperlinksToolInput'>*
[#](#langchain.tools.ExtractHyperlinksTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Extract
 

 all
 

 hyperlinks
 

 on
 

 the
 

 current
 

 webpage'*
[#](#langchain.tools.ExtractHyperlinksTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'extract_hyperlinks'*
[#](#langchain.tools.ExtractHyperlinksTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 






*static*


 scrape_page
 


 (
 
*page
 



 :
 





 Any*
 ,
 *html_content
 



 :
 





 str*
 ,
 *absolute_urls
 



 :
 





 bool*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/tools/playwright/extract_hyperlinks#ExtractHyperlinksTool.scrape_page)
[#](#langchain.tools.ExtractHyperlinksTool.scrape_page "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 ExtractTextTool
 

[[source]](../../_modules/langchain/tools/playwright/extract_text#ExtractTextTool)
[#](#langchain.tools.ExtractTextTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 BaseModel
 


 ]*
*=
 




 <class
 

 'pydantic.main.BaseModel'>*
[#](#langchain.tools.ExtractTextTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Extract
 

 all
 

 the
 

 text
 

 on
 

 the
 

 current
 

 webpage'*
[#](#langchain.tools.ExtractTextTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'extract_text'*
[#](#langchain.tools.ExtractTextTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 FileSearchTool
 

[[source]](../../_modules/langchain/tools/file_management/file_search#FileSearchTool)
[#](#langchain.tools.FileSearchTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 pydantic.main.BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.file_management.file_search.FileSearchInput'>*
[#](#langchain.tools.FileSearchTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Recursively
 

 search
 

 for
 

 files
 

 in
 

 a
 

 subdirectory
 

 that
 

 match
 

 the
 

 regex
 

 pattern'*
[#](#langchain.tools.FileSearchTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'file_search'*
[#](#langchain.tools.FileSearchTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 GetElementsTool
 

[[source]](../../_modules/langchain/tools/playwright/get_elements#GetElementsTool)
[#](#langchain.tools.GetElementsTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.playwright.get_elements.GetElementsToolInput'>*
[#](#langchain.tools.GetElementsTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Retrieve
 

 elements
 

 in
 

 the
 

 current
 

 web
 

 page
 

 matching
 

 the
 

 given
 

 CSS
 

 selector'*
[#](#langchain.tools.GetElementsTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'get_elements'*
[#](#langchain.tools.GetElementsTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 GooglePlacesTool
 

[[source]](../../_modules/langchain/tools/google_places/tool#GooglePlacesTool)
[#](#langchain.tools.GooglePlacesTool "Permalink to this definition") 



 Tool that adds the capability to query the Google places API.
 




*field*


 api_wrapper
 

*:
 



[langchain.utilities.google_places_api.GooglePlacesAPIWrapper](utilities#langchain.utilities.GooglePlacesAPIWrapper "langchain.utilities.google_places_api.GooglePlacesAPIWrapper")*
*[Optional]*
[#](#langchain.tools.GooglePlacesTool.api_wrapper "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 GoogleSearchResults
 

[[source]](../../_modules/langchain/tools/google_search/tool#GoogleSearchResults)
[#](#langchain.tools.GoogleSearchResults "Permalink to this definition") 



 Tool that has capability to query the Google Search API and get back json.
 




*field*


 api_wrapper
 

*:
 



[langchain.utilities.google_search.GoogleSearchAPIWrapper](utilities#langchain.utilities.GoogleSearchAPIWrapper "langchain.utilities.google_search.GoogleSearchAPIWrapper")*
*[Required]*
[#](#langchain.tools.GoogleSearchResults.api_wrapper "Permalink to this definition") 






*field*


 num_results
 

*:
 




 int*
*=
 




 4*
[#](#langchain.tools.GoogleSearchResults.num_results "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 GoogleSearchRun
 

[[source]](../../_modules/langchain/tools/google_search/tool#GoogleSearchRun)
[#](#langchain.tools.GoogleSearchRun "Permalink to this definition") 



 Tool that adds the capability to query the Google search API.
 




*field*


 api_wrapper
 

*:
 



[langchain.utilities.google_search.GoogleSearchAPIWrapper](utilities#langchain.utilities.GoogleSearchAPIWrapper "langchain.utilities.google_search.GoogleSearchAPIWrapper")*
*[Required]*
[#](#langchain.tools.GoogleSearchRun.api_wrapper "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 HumanInputRun
 

[[source]](../../_modules/langchain/tools/human/tool#HumanInputRun)
[#](#langchain.tools.HumanInputRun "Permalink to this definition") 



 Tool that adds the capability to ask user for input.
 




*field*


 input_func
 

*:
 




 Callable*
*[Optional]*
[#](#langchain.tools.HumanInputRun.input_func "Permalink to this definition") 






*field*


 prompt_func
 

*:
 




 Callable
 


 [
 



 [
 


 str
 


 ]
 



 ,
 




 None
 


 ]*
*[Optional]*
[#](#langchain.tools.HumanInputRun.prompt_func "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 IFTTTWebhook
 

[[source]](../../_modules/langchain/tools/ifttt#IFTTTWebhook)
[#](#langchain.tools.IFTTTWebhook "Permalink to this definition") 



 IFTTT Webhook.
 




 Parameters
 

* **name** 
 – name of the tool
* **description** 
 – description of the tool
* **url** 
 – url to hit with the json event.






*field*


 url
 

*:
 




 str*
*[Required]*
[#](#langchain.tools.IFTTTWebhook.url "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 ListDirectoryTool
 

[[source]](../../_modules/langchain/tools/file_management/list_dir#ListDirectoryTool)
[#](#langchain.tools.ListDirectoryTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 pydantic.main.BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.file_management.list_dir.DirectoryListingInput'>*
[#](#langchain.tools.ListDirectoryTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'List
 

 files
 

 and
 

 directories
 

 in
 

 a
 

 specified
 

 folder'*
[#](#langchain.tools.ListDirectoryTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'list_directory'*
[#](#langchain.tools.ListDirectoryTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 MoveFileTool
 

[[source]](../../_modules/langchain/tools/file_management/move#MoveFileTool)
[#](#langchain.tools.MoveFileTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 pydantic.main.BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.file_management.move.FileMoveInput'>*
[#](#langchain.tools.MoveFileTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Move
 

 or
 

 rename
 

 a
 

 file
 

 from
 

 one
 

 location
 

 to
 

 another'*
[#](#langchain.tools.MoveFileTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'move_file'*
[#](#langchain.tools.MoveFileTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 NavigateBackTool
 

[[source]](../../_modules/langchain/tools/playwright/navigate_back#NavigateBackTool)
[#](#langchain.tools.NavigateBackTool "Permalink to this definition") 



 Navigate back to the previous page in the browser history.
 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 BaseModel
 


 ]*
*=
 




 <class
 

 'pydantic.main.BaseModel'>*
[#](#langchain.tools.NavigateBackTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Navigate
 

 back
 

 to
 

 the
 

 previous
 

 page
 

 in
 

 the
 

 browser
 

 history'*
[#](#langchain.tools.NavigateBackTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'previous_webpage'*
[#](#langchain.tools.NavigateBackTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 NavigateTool
 

[[source]](../../_modules/langchain/tools/playwright/navigate#NavigateTool)
[#](#langchain.tools.NavigateTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.playwright.navigate.NavigateToolInput'>*
[#](#langchain.tools.NavigateTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Navigate
 

 a
 

 browser
 

 to
 

 the
 

 specified
 

 URL'*
[#](#langchain.tools.NavigateTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'navigate_browser'*
[#](#langchain.tools.NavigateTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 OpenAPISpec
 

[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec)
[#](#langchain.tools.OpenAPISpec "Permalink to this definition") 



 OpenAPI Model that removes misformatted parts of the spec.
 




*field*


 components
 

*:
 




 Optional
 


 [
 


 openapi_schema_pydantic.v3.v3_1_0.components.Components
 


 ]*
*=
 




 None*
[#](#langchain.tools.OpenAPISpec.components "Permalink to this definition") 



 An element to hold various schemas for the document.
 






*field*


 externalDocs
 

*:
 




 Optional
 


 [
 


 openapi_schema_pydantic.v3.v3_1_0.external_documentation.ExternalDocumentation
 


 ]*
*=
 




 None*
[#](#langchain.tools.OpenAPISpec.externalDocs "Permalink to this definition") 



 Additional external documentation.
 






*field*


 info
 

*:
 




 openapi_schema_pydantic.v3.v3_1_0.info.Info*
*[Required]*
[#](#langchain.tools.OpenAPISpec.info "Permalink to this definition") 



**REQUIRED** 
 . Provides metadata about the API. The metadata MAY be used by tooling as required.
 






*field*


 jsonSchemaDialect
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.tools.OpenAPISpec.jsonSchemaDialect "Permalink to this definition") 



 The default value for the
 
 $schema
 
 keyword within [Schema Objects](#schemaObject)
contained within this OAS document. This MUST be in the form of a URI.
 






*field*


 openapi
 

*:
 




 str*
*=
 




 '3.1.0'*
[#](#langchain.tools.OpenAPISpec.openapi "Permalink to this definition") 



**REQUIRED** 
 . This string MUST be the [version number](#versions)
of the OpenAPI Specification that the OpenAPI document uses.
The
 
 openapi
 
 field SHOULD be used by tooling to interpret the OpenAPI document.
This is
 *not* 
 related to the API [
 
 info.version
 
 ](#infoVersion) string.
 






*field*


 paths
 

*:
 




 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 openapi_schema_pydantic.v3.v3_1_0.path_item.PathItem
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.tools.OpenAPISpec.paths "Permalink to this definition") 



 The available paths and operations for the API.
 






*field*


 security
 

*:
 




 Optional
 


 [
 


 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ]
 



 ]
 



 ]*
*=
 




 None*
[#](#langchain.tools.OpenAPISpec.security "Permalink to this definition") 



 A declaration of which security mechanisms can be used across the API.
The list of values includes alternative security requirement objects that can be used.
Only one of the security requirement objects need to be satisfied to authorize a request.
Individual operations can override this definition.
To make security optional, an empty security requirement (
 
 {}
 
 ) can be included in the array.
 






*field*


 servers
 

*:
 




 List
 


 [
 


 openapi_schema_pydantic.v3.v3_1_0.server.Server
 


 ]*
*=
 




 [Server(url='/',
 

 description=None,
 

 variables=None)]*
[#](#langchain.tools.OpenAPISpec.servers "Permalink to this definition") 



 An array of Server Objects, which provide connectivity information to a target server.
If the
 
 servers
 
 property is not provided, or is an empty array,
the default value would be a [Server Object](#serverObject) with a [url](#serverUrl) value of
 
 /
 
 .
 






*field*


 tags
 

*:
 




 Optional
 


 [
 


 List
 


 [
 


 openapi_schema_pydantic.v3.v3_1_0.tag.Tag
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.tools.OpenAPISpec.tags "Permalink to this definition") 



 A list of tags used by the document with additional metadata.
The order of the tags can be used to reflect on their order by the parsing tools.
Not all tags that are used by the [Operation Object](#operationObject) must be declared.
The tags that are not declared MAY be organized randomly or based on the tools’ logic.
Each tag name in the list MUST be unique.
 






*field*


 webhooks
 

*:
 




 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Union
 


 [
 


 openapi_schema_pydantic.v3.v3_1_0.path_item.PathItem
 


 ,
 




 openapi_schema_pydantic.v3.v3_1_0.reference.Reference
 


 ]
 



 ]
 



 ]*
*=
 




 None*
[#](#langchain.tools.OpenAPISpec.webhooks "Permalink to this definition") 



 The incoming webhooks that MAY be received as part of this API and that the API consumer MAY choose to implement.
Closely related to the
 
 callbacks
 
 feature, this section describes requests initiated other than by an API call,
for example by an out of band registration.
The key name is a unique string to refer to each webhook,
while the (optionally referenced) Path Item Object describes a request
that may be initiated by the API provider and the expected responses.
An [example](../examples/v3.1/webhook-example.yaml) is available.
 






*classmethod*


 from_file
 


 (
 
*path
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 pathlib.Path
 


 ]*

 )
 


 →
 

[langchain.tools.openapi.utils.openapi_utils.OpenAPISpec](#langchain.tools.OpenAPISpec "langchain.tools.openapi.utils.openapi_utils.OpenAPISpec")


[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec.from_file)
[#](#langchain.tools.OpenAPISpec.from_file "Permalink to this definition") 



 Get an OpenAPI spec from a file path.
 






*classmethod*


 from_spec_dict
 


 (
 
*spec_dict
 



 :
 





 dict*

 )
 


 →
 

[langchain.tools.openapi.utils.openapi_utils.OpenAPISpec](#langchain.tools.OpenAPISpec "langchain.tools.openapi.utils.openapi_utils.OpenAPISpec")


[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec.from_spec_dict)
[#](#langchain.tools.OpenAPISpec.from_spec_dict "Permalink to this definition") 



 Get an OpenAPI spec from a dict.
 






*classmethod*


 from_text
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 

[langchain.tools.openapi.utils.openapi_utils.OpenAPISpec](#langchain.tools.OpenAPISpec "langchain.tools.openapi.utils.openapi_utils.OpenAPISpec")


[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec.from_text)
[#](#langchain.tools.OpenAPISpec.from_text "Permalink to this definition") 



 Get an OpenAPI spec from a text.
 






*classmethod*


 from_url
 


 (
 
*url
 



 :
 





 str*

 )
 


 →
 

[langchain.tools.openapi.utils.openapi_utils.OpenAPISpec](#langchain.tools.OpenAPISpec "langchain.tools.openapi.utils.openapi_utils.OpenAPISpec")


[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec.from_url)
[#](#langchain.tools.OpenAPISpec.from_url "Permalink to this definition") 



 Get an OpenAPI spec from a URL.
 






*static*


 get_cleaned_operation_id
 


 (
 
*operation
 



 :
 





 openapi_schema_pydantic.v3.v3_1_0.operation.Operation*
 ,
 *path
 



 :
 





 str*
 ,
 *method
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec.get_cleaned_operation_id)
[#](#langchain.tools.OpenAPISpec.get_cleaned_operation_id "Permalink to this definition") 



 Get a cleaned operation id from an operation id.
 








 get_methods_for_path
 


 (
 
*path
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec.get_methods_for_path)
[#](#langchain.tools.OpenAPISpec.get_methods_for_path "Permalink to this definition") 



 Return a list of valid methods for the specified path.
 








 get_operation
 


 (
 
*path
 



 :
 





 str*
 ,
 *method
 



 :
 





 str*

 )
 


 →
 


 openapi_schema_pydantic.v3.v3_1_0.operation.Operation
 


[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec.get_operation)
[#](#langchain.tools.OpenAPISpec.get_operation "Permalink to this definition") 



 Get the operation object for a given path and HTTP method.
 








 get_parameters_for_operation
 


 (
 
*operation
 



 :
 





 openapi_schema_pydantic.v3.v3_1_0.operation.Operation*

 )
 


 →
 


 List
 


 [
 


 openapi_schema_pydantic.v3.v3_1_0.parameter.Parameter
 


 ]
 



[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec.get_parameters_for_operation)
[#](#langchain.tools.OpenAPISpec.get_parameters_for_operation "Permalink to this definition") 



 Get the components for a given operation.
 








 get_referenced_schema
 


 (
 
*ref
 



 :
 





 openapi_schema_pydantic.v3.v3_1_0.reference.Reference*

 )
 


 →
 


 openapi_schema_pydantic.v3.v3_1_0.schema.Schema
 


[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec.get_referenced_schema)
[#](#langchain.tools.OpenAPISpec.get_referenced_schema "Permalink to this definition") 



 Get a schema (or nested reference) or err.
 








 get_request_body_for_operation
 


 (
 
*operation
 



 :
 





 openapi_schema_pydantic.v3.v3_1_0.operation.Operation*

 )
 


 →
 


 Optional
 


 [
 


 openapi_schema_pydantic.v3.v3_1_0.request_body.RequestBody
 


 ]
 



[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec.get_request_body_for_operation)
[#](#langchain.tools.OpenAPISpec.get_request_body_for_operation "Permalink to this definition") 



 Get the request body for a given operation.
 






*classmethod*


 parse_obj
 


 (
 
*obj
 



 :
 





 dict*

 )
 


 →
 

[langchain.tools.openapi.utils.openapi_utils.OpenAPISpec](#langchain.tools.OpenAPISpec "langchain.tools.openapi.utils.openapi_utils.OpenAPISpec")


[[source]](../../_modules/langchain/tools/openapi/utils/openapi_utils#OpenAPISpec.parse_obj)
[#](#langchain.tools.OpenAPISpec.parse_obj "Permalink to this definition") 






*property*


 base_url
 

*:
 




 str*
[#](#langchain.tools.OpenAPISpec.base_url "Permalink to this definition") 



 Get the base url.
 








*pydantic
 

 model*


 langchain.tools.
 



 ReadFileTool
 

[[source]](../../_modules/langchain/tools/file_management/read#ReadFileTool)
[#](#langchain.tools.ReadFileTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 pydantic.main.BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.file_management.read.ReadFileInput'>*
[#](#langchain.tools.ReadFileTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Read
 

 file
 

 from
 

 disk'*
[#](#langchain.tools.ReadFileTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'read_file'*
[#](#langchain.tools.ReadFileTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 SceneXplainTool
 

[[source]](../../_modules/langchain/tools/scenexplain/tool#SceneXplainTool)
[#](#langchain.tools.SceneXplainTool "Permalink to this definition") 



 Tool that adds the capability to explain images.
 




*field*


 api_wrapper
 

*:
 




 langchain.utilities.scenexplain.SceneXplainAPIWrapper*
*[Optional]*
[#](#langchain.tools.SceneXplainTool.api_wrapper "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 ShellTool
 

[[source]](../../_modules/langchain/tools/shell/tool#ShellTool)
[#](#langchain.tools.ShellTool "Permalink to this definition") 



 Tool to run shell commands.
 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 pydantic.main.BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.shell.tool.ShellInput'>*
[#](#langchain.tools.ShellTool.args_schema "Permalink to this definition") 



 Schema for input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Run
 

 shell
 

 commands
 

 on
 

 this
 

 Linux
 

 machine.'*
[#](#langchain.tools.ShellTool.description "Permalink to this definition") 



 Description of tool.
 






*field*


 name
 

*:
 




 str*
*=
 




 'terminal'*
[#](#langchain.tools.ShellTool.name "Permalink to this definition") 



 Name of tool.
 






*field*


 process
 

*:
 



[langchain.utilities.bash.BashProcess](utilities#langchain.utilities.BashProcess "langchain.utilities.bash.BashProcess")*
*[Optional]*
[#](#langchain.tools.ShellTool.process "Permalink to this definition") 



 Bash process to run commands.
 








*pydantic
 

 model*


 langchain.tools.
 



 StructuredTool
 

[[source]](../../_modules/langchain/tools/base#StructuredTool)
[#](#langchain.tools.StructuredTool "Permalink to this definition") 



 Tool that can operate on any number of inputs.
 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 pydantic.main.BaseModel
 


 ]*
*[Required]*
[#](#langchain.tools.StructuredTool.args_schema "Permalink to this definition") 



 The input arguments’ schema.
 



 The tool schema.
 






*field*


 coroutine
 

*:
 




 Optional
 


 [
 


 Callable
 


 [
 



 [
 



 ...
 



 ]
 



 ,
 




 Awaitable
 


 [
 


 Any
 


 ]
 



 ]
 



 ]*
*=
 




 None*
[#](#langchain.tools.StructuredTool.coroutine "Permalink to this definition") 



 The asynchronous version of the function.
 






*field*


 description
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.tools.StructuredTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 func
 

*:
 




 Callable
 


 [
 



 [
 



 ...
 



 ]
 



 ,
 




 Any
 


 ]*
*[Required]*
[#](#langchain.tools.StructuredTool.func "Permalink to this definition") 



 The function to run when the tool is called.
 






*classmethod*


 from_function
 


 (
 
*func
 



 :
 





 Callable*
 ,
 *name
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *description
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *return_direct
 



 :
 





 bool
 





 =
 





 False*
 ,
 *args_schema
 



 :
 





 Optional
 


 [
 


 Type
 


 [
 


 pydantic.main.BaseModel
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *infer_schema
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.tools.base.StructuredTool](#langchain.tools.StructuredTool "langchain.tools.base.StructuredTool")


[[source]](../../_modules/langchain/tools/base#StructuredTool.from_function)
[#](#langchain.tools.StructuredTool.from_function "Permalink to this definition") 






*property*


 args
 

*:
 




 dict*
[#](#langchain.tools.StructuredTool.args "Permalink to this definition") 



 The tool’s input arguments.
 








*pydantic
 

 model*


 langchain.tools.
 



 VectorStoreQATool
 

[[source]](../../_modules/langchain/tools/vectorstore/tool#VectorStoreQATool)
[#](#langchain.tools.VectorStoreQATool "Permalink to this definition") 



 Tool for the VectorDBQA chain. To be initialized with name and chain.
 




*field*


 llm
 

*:
 




 langchain.base_language.BaseLanguageModel*
*[Optional]*
[#](#langchain.tools.VectorStoreQATool.llm "Permalink to this definition") 






*field*


 vectorstore
 

*:
 



[langchain.vectorstores.base.VectorStore](vectorstores#langchain.vectorstores.VectorStore "langchain.vectorstores.base.VectorStore")*
*[Required]*
[#](#langchain.tools.VectorStoreQATool.vectorstore "Permalink to this definition") 






*static*


 get_description
 


 (
 
*name
 



 :
 





 str*
 ,
 *description
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/tools/vectorstore/tool#VectorStoreQATool.get_description)
[#](#langchain.tools.VectorStoreQATool.get_description "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 VectorStoreQAWithSourcesTool
 

[[source]](../../_modules/langchain/tools/vectorstore/tool#VectorStoreQAWithSourcesTool)
[#](#langchain.tools.VectorStoreQAWithSourcesTool "Permalink to this definition") 



 Tool for the VectorDBQAWithSources chain.
 




*field*


 llm
 

*:
 




 langchain.base_language.BaseLanguageModel*
*[Optional]*
[#](#langchain.tools.VectorStoreQAWithSourcesTool.llm "Permalink to this definition") 






*field*


 vectorstore
 

*:
 



[langchain.vectorstores.base.VectorStore](vectorstores#langchain.vectorstores.VectorStore "langchain.vectorstores.base.VectorStore")*
*[Required]*
[#](#langchain.tools.VectorStoreQAWithSourcesTool.vectorstore "Permalink to this definition") 






*static*


 get_description
 


 (
 
*name
 



 :
 





 str*
 ,
 *description
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/tools/vectorstore/tool#VectorStoreQAWithSourcesTool.get_description)
[#](#langchain.tools.VectorStoreQAWithSourcesTool.get_description "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 WikipediaQueryRun
 

[[source]](../../_modules/langchain/tools/wikipedia/tool#WikipediaQueryRun)
[#](#langchain.tools.WikipediaQueryRun "Permalink to this definition") 



 Tool that adds the capability to search using the Wikipedia API.
 




*field*


 api_wrapper
 

*:
 



[langchain.utilities.wikipedia.WikipediaAPIWrapper](utilities#langchain.utilities.WikipediaAPIWrapper "langchain.utilities.wikipedia.WikipediaAPIWrapper")*
*[Required]*
[#](#langchain.tools.WikipediaQueryRun.api_wrapper "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 WolframAlphaQueryRun
 

[[source]](../../_modules/langchain/tools/wolfram_alpha/tool#WolframAlphaQueryRun)
[#](#langchain.tools.WolframAlphaQueryRun "Permalink to this definition") 



 Tool that adds the capability to query using the Wolfram Alpha SDK.
 




*field*


 api_wrapper
 

*:
 



[langchain.utilities.wolfram_alpha.WolframAlphaAPIWrapper](utilities#langchain.utilities.WolframAlphaAPIWrapper "langchain.utilities.wolfram_alpha.WolframAlphaAPIWrapper")*
*[Required]*
[#](#langchain.tools.WolframAlphaQueryRun.api_wrapper "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 WriteFileTool
 

[[source]](../../_modules/langchain/tools/file_management/write#WriteFileTool)
[#](#langchain.tools.WriteFileTool "Permalink to this definition") 




*field*


 args_schema
 

*:
 




 Type
 


 [
 


 pydantic.main.BaseModel
 


 ]*
*=
 




 <class
 

 'langchain.tools.file_management.write.WriteFileInput'>*
[#](#langchain.tools.WriteFileTool.args_schema "Permalink to this definition") 



 Pydantic model class to validate and parse the tool’s input arguments.
 






*field*


 description
 

*:
 




 str*
*=
 




 'Write
 

 file
 

 to
 

 disk'*
[#](#langchain.tools.WriteFileTool.description "Permalink to this definition") 



 Used to tell the model how/when/why to use the tool.
 



 You can provide few-shot examples as a part of the description.
 






*field*


 name
 

*:
 




 str*
*=
 




 'write_file'*
[#](#langchain.tools.WriteFileTool.name "Permalink to this definition") 



 The unique name of the tool that clearly communicates its purpose.
 








*pydantic
 

 model*


 langchain.tools.
 



 ZapierNLAListActions
 

[[source]](../../_modules/langchain/tools/zapier/tool#ZapierNLAListActions)
[#](#langchain.tools.ZapierNLAListActions "Permalink to this definition") 




 Returns a list of all exposed (enabled) actions associated with
 


 current user (associated with the set api_key). Change your exposed
actions here:
 <https://nla.zapier.com/demo/start/>




 The return list can be empty if no actions exposed. Else will contain
a list of action objects:
 




 [{
 


 “id”: str,
“description”: str,
“params”: Dict[str, str]
 





 }]
 




 params
 
 will always contain an
 
 instructions
 
 key, the only required
param. All others optional and if provided will override any AI guesses
(see “understanding the AI guessing flow” here:
 <https://nla.zapier.com/api/v1/docs>
 )
 






 Parameters
 


**None** 
 –
 






*field*


 api_wrapper
 

*:
 




 langchain.utilities.zapier.ZapierNLAWrapper*
*[Optional]*
[#](#langchain.tools.ZapierNLAListActions.api_wrapper "Permalink to this definition") 








*pydantic
 

 model*


 langchain.tools.
 



 ZapierNLARunAction
 

[[source]](../../_modules/langchain/tools/zapier/tool#ZapierNLARunAction)
[#](#langchain.tools.ZapierNLARunAction "Permalink to this definition") 




 Executes an action that is identified by action_id, must be exposed
 


 (enabled) by the current user (associated with the set api_key). Change
your exposed actions here:
 <https://nla.zapier.com/demo/start/>




 The return JSON is guaranteed to be less than ~500 words (350
tokens) making it safe to inject into the prompt of another LLM
call.
 






 Parameters
 

* **action_id** 
 – a specific action ID (from list actions) of the action to execute
(the set api_key must be associated with the action owner)
* **instructions** 
 – a natural language instruction string for using the action
(eg. “get the latest email from Mike Knoop” for “Gmail: find email” action)
* **params** 
 – a dict, optional. Any params provided will
 *override* 
 AI guesses
from
 
 instructions
 
 (see “understanding the AI guessing flow” here:
 <https://nla.zapier.com/api/v1/docs>
 )






*field*


 action_id
 

*:
 




 str*
*[Required]*
[#](#langchain.tools.ZapierNLARunAction.action_id "Permalink to this definition") 






*field*


 api_wrapper
 

*:
 




 langchain.utilities.zapier.ZapierNLAWrapper*
*[Optional]*
[#](#langchain.tools.ZapierNLARunAction.api_wrapper "Permalink to this definition") 






*field*


 params
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.tools.ZapierNLARunAction.params "Permalink to this definition") 






*field*


 params_schema
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]*
*[Optional]*
[#](#langchain.tools.ZapierNLARunAction.params_schema "Permalink to this definition") 






*field*


 zapier_description
 

*:
 




 str*
*[Required]*
[#](#langchain.tools.ZapierNLARunAction.zapier_description "Permalink to this definition") 








