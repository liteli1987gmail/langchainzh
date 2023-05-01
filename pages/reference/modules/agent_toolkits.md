




 Agent Toolkits
 [#](#module-langchain.agents.agent_toolkits "Permalink to this headline")
===========================================================================================



 Agent toolkits.
 




*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 FileManagementToolkit
 

[[source]](../../_modules/langchain/agents/agent_toolkits/file_management/toolkit#FileManagementToolkit)
[#](#langchain.agents.agent_toolkits.FileManagementToolkit "Permalink to this definition") 



 Toolkit for interacting with a Local Files.
 




*field*


 root_dir
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.agents.agent_toolkits.FileManagementToolkit.root_dir "Permalink to this definition") 



 If specified, all file operations are made relative to root_dir.
 






*field*


 selected_tools
 

*:
 




 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.agents.agent_toolkits.FileManagementToolkit.selected_tools "Permalink to this definition") 



 If provided, only provide the selected tools. Defaults to all.
 








 get_tools
 


 (
 

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/agent_toolkits/file_management/toolkit#FileManagementToolkit.get_tools)
[#](#langchain.agents.agent_toolkits.FileManagementToolkit.get_tools "Permalink to this definition") 



 Get the tools in the toolkit.
 








*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 JiraToolkit
 

[[source]](../../_modules/langchain/agents/agent_toolkits/jira/toolkit#JiraToolkit)
[#](#langchain.agents.agent_toolkits.JiraToolkit "Permalink to this definition") 



 Jira Toolkit.
 




*field*


 tools
 

*:
 




 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
*=
 




 []*
[#](#langchain.agents.agent_toolkits.JiraToolkit.tools "Permalink to this definition") 






*classmethod*


 from_jira_api_wrapper
 


 (
 
*jira_api_wrapper
 



 :
 





 langchain.utilities.jira.JiraAPIWrapper*

 )
 


 →
 

[langchain.agents.agent_toolkits.jira.toolkit.JiraToolkit](#langchain.agents.agent_toolkits.JiraToolkit "langchain.agents.agent_toolkits.jira.toolkit.JiraToolkit")


[[source]](../../_modules/langchain/agents/agent_toolkits/jira/toolkit#JiraToolkit.from_jira_api_wrapper)
[#](#langchain.agents.agent_toolkits.JiraToolkit.from_jira_api_wrapper "Permalink to this definition") 








 get_tools
 


 (
 

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/agent_toolkits/jira/toolkit#JiraToolkit.get_tools)
[#](#langchain.agents.agent_toolkits.JiraToolkit.get_tools "Permalink to this definition") 



 Get the tools in the toolkit.
 








*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 JsonToolkit
 

[[source]](../../_modules/langchain/agents/agent_toolkits/json/toolkit#JsonToolkit)
[#](#langchain.agents.agent_toolkits.JsonToolkit "Permalink to this definition") 



 Toolkit for interacting with a JSON spec.
 




*field*


 spec
 

*:
 




 langchain.tools.json.tool.JsonSpec*
*[Required]*
[#](#langchain.agents.agent_toolkits.JsonToolkit.spec "Permalink to this definition") 








 get_tools
 


 (
 

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/agent_toolkits/json/toolkit#JsonToolkit.get_tools)
[#](#langchain.agents.agent_toolkits.JsonToolkit.get_tools "Permalink to this definition") 



 Get the tools in the toolkit.
 








*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 NLAToolkit
 

[[source]](../../_modules/langchain/agents/agent_toolkits/nla/toolkit#NLAToolkit)
[#](#langchain.agents.agent_toolkits.NLAToolkit "Permalink to this definition") 



 Natural Language API Toolkit Definition.
 




*field*


 nla_tools
 

*:
 




 Sequence
 


 [
 


 langchain.agents.agent_toolkits.nla.tool.NLATool
 


 ]*
*[Required]*
[#](#langchain.agents.agent_toolkits.NLAToolkit.nla_tools "Permalink to this definition") 



 List of API Endpoint Tools.
 






*classmethod*


 from_llm_and_ai_plugin
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *ai_plugin
 



 :
 





 langchain.tools.plugin.AIPlugin*
 ,
 *requests
 



 :
 





 Optional
 


 [
 


 langchain.requests.Requests
 


 ]
 






 =
 





 None*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent_toolkits.nla.toolkit.NLAToolkit](#langchain.agents.agent_toolkits.NLAToolkit "langchain.agents.agent_toolkits.nla.toolkit.NLAToolkit")


[[source]](../../_modules/langchain/agents/agent_toolkits/nla/toolkit#NLAToolkit.from_llm_and_ai_plugin)
[#](#langchain.agents.agent_toolkits.NLAToolkit.from_llm_and_ai_plugin "Permalink to this definition") 



 Instantiate the toolkit from an OpenAPI Spec URL
 






*classmethod*


 from_llm_and_ai_plugin_url
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *ai_plugin_url
 



 :
 





 str*
 ,
 *requests
 



 :
 





 Optional
 


 [
 


 langchain.requests.Requests
 


 ]
 






 =
 





 None*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent_toolkits.nla.toolkit.NLAToolkit](#langchain.agents.agent_toolkits.NLAToolkit "langchain.agents.agent_toolkits.nla.toolkit.NLAToolkit")


[[source]](../../_modules/langchain/agents/agent_toolkits/nla/toolkit#NLAToolkit.from_llm_and_ai_plugin_url)
[#](#langchain.agents.agent_toolkits.NLAToolkit.from_llm_and_ai_plugin_url "Permalink to this definition") 



 Instantiate the toolkit from an OpenAPI Spec URL
 






*classmethod*


 from_llm_and_spec
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *spec
 



 :
 




[langchain.tools.openapi.utils.openapi_utils.OpenAPISpec](tools#langchain.tools.OpenAPISpec "langchain.tools.openapi.utils.openapi_utils.OpenAPISpec")*
 ,
 *requests
 



 :
 





 Optional
 


 [
 


 langchain.requests.Requests
 


 ]
 






 =
 





 None*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent_toolkits.nla.toolkit.NLAToolkit](#langchain.agents.agent_toolkits.NLAToolkit "langchain.agents.agent_toolkits.nla.toolkit.NLAToolkit")


[[source]](../../_modules/langchain/agents/agent_toolkits/nla/toolkit#NLAToolkit.from_llm_and_spec)
[#](#langchain.agents.agent_toolkits.NLAToolkit.from_llm_and_spec "Permalink to this definition") 



 Instantiate the toolkit by creating tools for each operation.
 






*classmethod*


 from_llm_and_url
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *open_api_url
 



 :
 





 str*
 ,
 *requests
 



 :
 





 Optional
 


 [
 


 langchain.requests.Requests
 


 ]
 






 =
 





 None*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent_toolkits.nla.toolkit.NLAToolkit](#langchain.agents.agent_toolkits.NLAToolkit "langchain.agents.agent_toolkits.nla.toolkit.NLAToolkit")


[[source]](../../_modules/langchain/agents/agent_toolkits/nla/toolkit#NLAToolkit.from_llm_and_url)
[#](#langchain.agents.agent_toolkits.NLAToolkit.from_llm_and_url "Permalink to this definition") 



 Instantiate the toolkit from an OpenAPI Spec URL
 








 get_tools
 


 (
 

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/agent_toolkits/nla/toolkit#NLAToolkit.get_tools)
[#](#langchain.agents.agent_toolkits.NLAToolkit.get_tools "Permalink to this definition") 



 Get the tools for all the API operations.
 








*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 OpenAPIToolkit
 

[[source]](../../_modules/langchain/agents/agent_toolkits/openapi/toolkit#OpenAPIToolkit)
[#](#langchain.agents.agent_toolkits.OpenAPIToolkit "Permalink to this definition") 



 Toolkit for interacting with a OpenAPI api.
 




*field*


 json_agent
 

*:
 



[langchain.agents.agent.AgentExecutor](agents#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")*
*[Required]*
[#](#langchain.agents.agent_toolkits.OpenAPIToolkit.json_agent "Permalink to this definition") 






*field*


 requests_wrapper
 

*:
 



[langchain.requests.TextRequestsWrapper](utilities#langchain.utilities.TextRequestsWrapper "langchain.requests.TextRequestsWrapper")*
*[Required]*
[#](#langchain.agents.agent_toolkits.OpenAPIToolkit.requests_wrapper "Permalink to this definition") 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *json_spec
 



 :
 





 langchain.tools.json.tool.JsonSpec*
 ,
 *requests_wrapper
 



 :
 




[langchain.requests.TextRequestsWrapper](utilities#langchain.utilities.TextRequestsWrapper "langchain.requests.TextRequestsWrapper")*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent_toolkits.openapi.toolkit.OpenAPIToolkit](#langchain.agents.agent_toolkits.OpenAPIToolkit "langchain.agents.agent_toolkits.openapi.toolkit.OpenAPIToolkit")


[[source]](../../_modules/langchain/agents/agent_toolkits/openapi/toolkit#OpenAPIToolkit.from_llm)
[#](#langchain.agents.agent_toolkits.OpenAPIToolkit.from_llm "Permalink to this definition") 



 Create json agent from llm, then initialize.
 








 get_tools
 


 (
 

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/agent_toolkits/openapi/toolkit#OpenAPIToolkit.get_tools)
[#](#langchain.agents.agent_toolkits.OpenAPIToolkit.get_tools "Permalink to this definition") 



 Get the tools in the toolkit.
 








*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 PlayWrightBrowserToolkit
 

[[source]](../../_modules/langchain/agents/agent_toolkits/playwright/toolkit#PlayWrightBrowserToolkit)
[#](#langchain.agents.agent_toolkits.PlayWrightBrowserToolkit "Permalink to this definition") 



 Toolkit for web browser tools.
 




*field*


 async_browser
 

*:
 




 Optional
 


 [
 


 AsyncBrowser
 


 ]*
*=
 




 None*
[#](#langchain.agents.agent_toolkits.PlayWrightBrowserToolkit.async_browser "Permalink to this definition") 






*field*


 sync_browser
 

*:
 




 Optional
 


 [
 


 SyncBrowser
 


 ]*
*=
 




 None*
[#](#langchain.agents.agent_toolkits.PlayWrightBrowserToolkit.sync_browser "Permalink to this definition") 






*classmethod*


 from_browser
 


 (
 
*sync_browser
 



 :
 





 Optional
 


 [
 


 SyncBrowser
 


 ]
 






 =
 





 None*
 ,
 *async_browser
 



 :
 





 Optional
 


 [
 


 AsyncBrowser
 


 ]
 






 =
 





 None*

 )
 


 →
 

[PlayWrightBrowserToolkit](#langchain.agents.agent_toolkits.PlayWrightBrowserToolkit "langchain.agents.agent_toolkits.PlayWrightBrowserToolkit")


[[source]](../../_modules/langchain/agents/agent_toolkits/playwright/toolkit#PlayWrightBrowserToolkit.from_browser)
[#](#langchain.agents.agent_toolkits.PlayWrightBrowserToolkit.from_browser "Permalink to this definition") 



 Instantiate the toolkit.
 








 get_tools
 


 (
 

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/agent_toolkits/playwright/toolkit#PlayWrightBrowserToolkit.get_tools)
[#](#langchain.agents.agent_toolkits.PlayWrightBrowserToolkit.get_tools "Permalink to this definition") 



 Get the tools in the toolkit.
 








*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 PowerBIToolkit
 

[[source]](../../_modules/langchain/agents/agent_toolkits/powerbi/toolkit#PowerBIToolkit)
[#](#langchain.agents.agent_toolkits.PowerBIToolkit "Permalink to this definition") 



 Toolkit for interacting with PowerBI dataset.
 




*field*


 callback_manager
 

*:
 




 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]*
*=
 




 None*
[#](#langchain.agents.agent_toolkits.PowerBIToolkit.callback_manager "Permalink to this definition") 






*field*


 examples
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.agents.agent_toolkits.PowerBIToolkit.examples "Permalink to this definition") 






*field*


 llm
 

*:
 




 langchain.base_language.BaseLanguageModel*
*[Required]*
[#](#langchain.agents.agent_toolkits.PowerBIToolkit.llm "Permalink to this definition") 






*field*


 powerbi
 

*:
 



[langchain.utilities.powerbi.PowerBIDataset](utilities#langchain.utilities.PowerBIDataset "langchain.utilities.powerbi.PowerBIDataset")*
*[Required]*
[#](#langchain.agents.agent_toolkits.PowerBIToolkit.powerbi "Permalink to this definition") 








 get_tools
 


 (
 

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/agent_toolkits/powerbi/toolkit#PowerBIToolkit.get_tools)
[#](#langchain.agents.agent_toolkits.PowerBIToolkit.get_tools "Permalink to this definition") 



 Get the tools in the toolkit.
 








*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 SQLDatabaseToolkit
 

[[source]](../../_modules/langchain/agents/agent_toolkits/sql/toolkit#SQLDatabaseToolkit)
[#](#langchain.agents.agent_toolkits.SQLDatabaseToolkit "Permalink to this definition") 



 Toolkit for interacting with SQL databases.
 




*field*


 db
 

*:
 




 langchain.sql_database.SQLDatabase*
*[Required]*
[#](#langchain.agents.agent_toolkits.SQLDatabaseToolkit.db "Permalink to this definition") 






*field*


 llm
 

*:
 




 langchain.base_language.BaseLanguageModel*
*[Required]*
[#](#langchain.agents.agent_toolkits.SQLDatabaseToolkit.llm "Permalink to this definition") 








 get_tools
 


 (
 

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/agent_toolkits/sql/toolkit#SQLDatabaseToolkit.get_tools)
[#](#langchain.agents.agent_toolkits.SQLDatabaseToolkit.get_tools "Permalink to this definition") 



 Get the tools in the toolkit.
 






*property*


 dialect
 

*:
 




 str*
[#](#langchain.agents.agent_toolkits.SQLDatabaseToolkit.dialect "Permalink to this definition") 



 Return string representation of dialect to use.
 








*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 VectorStoreInfo
 

[[source]](../../_modules/langchain/agents/agent_toolkits/vectorstore/toolkit#VectorStoreInfo)
[#](#langchain.agents.agent_toolkits.VectorStoreInfo "Permalink to this definition") 



 Information about a vectorstore.
 




*field*


 description
 

*:
 




 str*
*[Required]*
[#](#langchain.agents.agent_toolkits.VectorStoreInfo.description "Permalink to this definition") 






*field*


 name
 

*:
 




 str*
*[Required]*
[#](#langchain.agents.agent_toolkits.VectorStoreInfo.name "Permalink to this definition") 






*field*


 vectorstore
 

*:
 



[langchain.vectorstores.base.VectorStore](vectorstores#langchain.vectorstores.VectorStore "langchain.vectorstores.base.VectorStore")*
*[Required]*
[#](#langchain.agents.agent_toolkits.VectorStoreInfo.vectorstore "Permalink to this definition") 








*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 VectorStoreRouterToolkit
 

[[source]](../../_modules/langchain/agents/agent_toolkits/vectorstore/toolkit#VectorStoreRouterToolkit)
[#](#langchain.agents.agent_toolkits.VectorStoreRouterToolkit "Permalink to this definition") 



 Toolkit for routing between vectorstores.
 




*field*


 llm
 

*:
 




 langchain.base_language.BaseLanguageModel*
*[Optional]*
[#](#langchain.agents.agent_toolkits.VectorStoreRouterToolkit.llm "Permalink to this definition") 






*field*


 vectorstores
 

*:
 




 List
 


 [
 

[langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreInfo](#langchain.agents.agent_toolkits.VectorStoreInfo "langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreInfo")


 ]*
*[Required]*
[#](#langchain.agents.agent_toolkits.VectorStoreRouterToolkit.vectorstores "Permalink to this definition") 








 get_tools
 


 (
 

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/agent_toolkits/vectorstore/toolkit#VectorStoreRouterToolkit.get_tools)
[#](#langchain.agents.agent_toolkits.VectorStoreRouterToolkit.get_tools "Permalink to this definition") 



 Get the tools in the toolkit.
 








*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 VectorStoreToolkit
 

[[source]](../../_modules/langchain/agents/agent_toolkits/vectorstore/toolkit#VectorStoreToolkit)
[#](#langchain.agents.agent_toolkits.VectorStoreToolkit "Permalink to this definition") 



 Toolkit for interacting with a vector store.
 




*field*


 llm
 

*:
 




 langchain.base_language.BaseLanguageModel*
*[Optional]*
[#](#langchain.agents.agent_toolkits.VectorStoreToolkit.llm "Permalink to this definition") 






*field*


 vectorstore_info
 

*:
 



[langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreInfo](#langchain.agents.agent_toolkits.VectorStoreInfo "langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreInfo")*
*[Required]*
[#](#langchain.agents.agent_toolkits.VectorStoreToolkit.vectorstore_info "Permalink to this definition") 








 get_tools
 


 (
 

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/agent_toolkits/vectorstore/toolkit#VectorStoreToolkit.get_tools)
[#](#langchain.agents.agent_toolkits.VectorStoreToolkit.get_tools "Permalink to this definition") 



 Get the tools in the toolkit.
 








*pydantic
 

 model*


 langchain.agents.agent_toolkits.
 



 ZapierToolkit
 

[[source]](../../_modules/langchain/agents/agent_toolkits/zapier/toolkit#ZapierToolkit)
[#](#langchain.agents.agent_toolkits.ZapierToolkit "Permalink to this definition") 



 Zapier Toolkit.
 




*field*


 tools
 

*:
 




 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
*=
 




 []*
[#](#langchain.agents.agent_toolkits.ZapierToolkit.tools "Permalink to this definition") 






*classmethod*


 from_zapier_nla_wrapper
 


 (
 
*zapier_nla_wrapper
 



 :
 





 langchain.utilities.zapier.ZapierNLAWrapper*

 )
 


 →
 

[langchain.agents.agent_toolkits.zapier.toolkit.ZapierToolkit](#langchain.agents.agent_toolkits.ZapierToolkit "langchain.agents.agent_toolkits.zapier.toolkit.ZapierToolkit")


[[source]](../../_modules/langchain/agents/agent_toolkits/zapier/toolkit#ZapierToolkit.from_zapier_nla_wrapper)
[#](#langchain.agents.agent_toolkits.ZapierToolkit.from_zapier_nla_wrapper "Permalink to this definition") 



 Create a toolkit from a ZapierNLAWrapper.
 








 get_tools
 


 (
 

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/agent_toolkits/zapier/toolkit#ZapierToolkit.get_tools)
[#](#langchain.agents.agent_toolkits.ZapierToolkit.get_tools "Permalink to this definition") 



 Get the tools in the toolkit.
 










 langchain.agents.agent_toolkits.
 



 create_csv_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *path
 



 :
 





 str*
 ,
 *pandas_kwargs
 



 :
 





 Optional
 


 [
 


 dict
 


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
 

[langchain.agents.agent.AgentExecutor](agents#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/csv/base#create_csv_agent)
[#](#langchain.agents.agent_toolkits.create_csv_agent "Permalink to this definition") 



 Create csv agent by loading to a dataframe and using pandas agent.
 








 langchain.agents.agent_toolkits.
 



 create_json_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *toolkit
 



 :
 




[langchain.agents.agent_toolkits.json.toolkit.JsonToolkit](#langchain.agents.agent_toolkits.JsonToolkit "langchain.agents.agent_toolkits.json.toolkit.JsonToolkit")*
 ,
 *callback_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]
 






 =
 





 None*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 'You
 

 are
 

 an
 

 agent
 

 designed
 

 to
 

 interact
 

 with
 

 JSON.\nYour
 

 goal
 

 is
 

 to
 

 return
 

 a
 

 final
 

 answer
 

 by
 

 interacting
 

 with
 

 the
 

 JSON.\nYou
 

 have
 

 access
 

 to
 

 the
 

 following
 

 tools
 

 which
 

 help
 

 you
 

 learn
 

 more
 

 about
 

 the
 

 JSON
 

 you
 

 are
 

 interacting
 

 with.\nOnly
 

 use
 

 the
 

 below
 

 tools.
 

 Only
 

 use
 

 the
 

 information
 

 returned
 

 by
 

 the
 

 below
 

 tools
 

 to
 

 construct
 

 your
 

 final
 

 answer.\nDo
 

 not
 

 make
 

 up
 

 any
 

 information
 

 that
 

 is
 

 not
 

 contained
 

 in
 

 the
 

 JSON.\nYour
 

 input
 

 to
 

 the
 

 tools
 

 should
 

 be
 

 in
 

 the
 

 form
 

 of
 

 `data["key"][0]`
 

 where
 

 `data`
 

 is
 

 the
 

 JSON
 

 blob
 

 you
 

 are
 

 interacting
 

 with,
 

 and
 

 the
 

 syntax
 

 used
 

 is
 

 Python.
 

 \nYou
 

 should
 

 only
 

 use
 

 keys
 

 that
 

 you
 

 know
 

 for
 

 a
 

 fact
 

 exist.
 

 You
 

 must
 

 validate
 

 that
 

 a
 

 key
 

 exists
 

 by
 

 seeing
 

 it
 

 previously
 

 when
 

 calling
 

 `json_spec_list_keys`.
 

 \nIf
 

 you
 

 have
 

 not
 

 seen
 

 a
 

 key
 

 in
 

 one
 

 of
 

 those
 

 responses,
 

 you
 

 cannot
 

 use
 

 it.\nYou
 

 should
 

 only
 

 add
 

 one
 

 key
 

 at
 

 a
 

 time
 

 to
 

 the
 

 path.
 

 You
 

 cannot
 

 add
 

 multiple
 

 keys
 

 at
 

 once.\nIf
 

 you
 

 encounter
 

 a
 

 "KeyError",
 

 go
 

 back
 

 to
 

 the
 

 previous
 

 key,
 

 look
 

 at
 

 the
 

 available
 

 keys,
 

 and
 

 try
 

 again.\n\nIf
 

 the
 

 question
 

 does
 

 not
 

 seem
 

 to
 

 be
 

 related
 

 to
 

 the
 

 JSON,
 

 just
 

 return
 

 "I
 

 don\'t
 

 know"
 

 as
 

 the
 

 answer.\nAlways
 

 begin
 

 your
 

 interaction
 

 with
 

 the
 

 `json_spec_list_keys`
 

 tool
 

 with
 

 input
 

 "data"
 

 to
 

 see
 

 what
 

 keys
 

 exist
 

 in
 

 the
 

 JSON.\n\nNote
 

 that
 

 sometimes
 

 the
 

 value
 

 at
 

 a
 

 given
 

 path
 

 is
 

 large.
 

 In
 

 this
 

 case,
 

 you
 

 will
 

 get
 

 an
 

 error
 

 "Value
 

 is
 

 a
 

 large
 

 dictionary,
 

 should
 

 explore
 

 its
 

 keys
 

 directly".\nIn
 

 this
 

 case,
 

 you
 

 should
 

 ALWAYS
 

 follow
 

 up
 

 by
 

 using
 

 the
 

 `json_spec_list_keys`
 

 tool
 

 to
 

 see
 

 what
 

 keys
 

 exist
 

 at
 

 that
 

 path.\nDo
 

 not
 

 simply
 

 refer
 

 the
 

 user
 

 to
 

 the
 

 JSON
 

 or
 

 a
 

 section
 

 of
 

 the
 

 JSON,
 

 as
 

 this
 

 is
 

 not
 

 a
 

 valid
 

 answer.
 

 Keep
 

 digging
 

 until
 

 you
 

 find
 

 the
 

 answer
 

 and
 

 explicitly
 

 return
 

 it.\n'*
 ,
 *suffix
 



 :
 





 str
 





 =
 





 'Begin!"\n\nQuestion:
 

 {input}\nThought:
 

 I
 

 should
 

 look
 

 at
 

 the
 

 keys
 

 that
 

 exist
 

 in
 

 data
 

 to
 

 see
 

 what
 

 I
 

 have
 

 access
 

 to\n{agent_scratchpad}'*
 ,
 *format_instructions
 



 :
 





 str
 





 =
 





 'Use
 

 the
 

 following
 

 format:\n\nQuestion:
 

 the
 

 input
 

 question
 

 you
 

 must
 

 answer\nThought:
 

 you
 

 should
 

 always
 

 think
 

 about
 

 what
 

 to
 

 do\nAction:
 

 the
 

 action
 

 to
 

 take,
 

 should
 

 be
 

 one
 

 of
 

 [{tool_names}]\nAction
 

 Input:
 

 the
 

 input
 

 to
 

 the
 

 action\nObservation:
 

 the
 

 result
 

 of
 

 the
 

 action\n...
 

 (this
 

 Thought/Action/Action
 

 Input/Observation
 

 can
 

 repeat
 

 N
 

 times)\nThought:
 

 I
 

 now
 

 know
 

 the
 

 final
 

 answer\nFinal
 

 Answer:
 

 the
 

 final
 

 answer
 

 to
 

 the
 

 original
 

 input
 

 question'*
 ,
 *input_variables
 



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
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.AgentExecutor](agents#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/json/base#create_json_agent)
[#](#langchain.agents.agent_toolkits.create_json_agent "Permalink to this definition") 



 Construct a json agent from an LLM and tools.
 








 langchain.agents.agent_toolkits.
 



 create_openapi_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *toolkit
 



 :
 




[langchain.agents.agent_toolkits.openapi.toolkit.OpenAPIToolkit](#langchain.agents.agent_toolkits.OpenAPIToolkit "langchain.agents.agent_toolkits.openapi.toolkit.OpenAPIToolkit")*
 ,
 *callback_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]
 






 =
 





 None*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 "You
 

 are
 

 an
 

 agent
 

 designed
 

 to
 

 answer
 

 questions
 

 by
 

 making
 

 web
 

 requests
 

 to
 

 an
 

 API
 

 given
 

 the
 

 openapi
 

 spec.\n\nIf
 

 the
 

 question
 

 does
 

 not
 

 seem
 

 related
 

 to
 

 the
 

 API,
 

 return
 

 I
 

 don't
 

 know.
 

 Do
 

 not
 

 make
 

 up
 

 an
 

 answer.\nOnly
 

 use
 

 information
 

 provided
 

 by
 

 the
 

 tools
 

 to
 

 construct
 

 your
 

 response.\n\nFirst,
 

 find
 

 the
 

 base
 

 URL
 

 needed
 

 to
 

 make
 

 the
 

 request.\n\nSecond,
 

 find
 

 the
 

 relevant
 

 paths
 

 needed
 

 to
 

 answer
 

 the
 

 question.
 

 Take
 

 note
 

 that,
 

 sometimes,
 

 you
 

 might
 

 need
 

 to
 

 make
 

 more
 

 than
 

 one
 

 request
 

 to
 

 more
 

 than
 

 one
 

 path
 

 to
 

 answer
 

 the
 

 question.\n\nThird,
 

 find
 

 the
 

 required
 

 parameters
 

 needed
 

 to
 

 make
 

 the
 

 request.
 

 For
 

 GET
 

 requests,
 

 these
 

 are
 

 usually
 

 URL
 

 parameters
 

 and
 

 for
 

 POST
 

 requests,
 

 these
 

 are
 

 request
 

 body
 

 parameters.\n\nFourth,
 

 make
 

 the
 

 requests
 

 needed
 

 to
 

 answer
 

 the
 

 question.
 

 Ensure
 

 that
 

 you
 

 are
 

 sending
 

 the
 

 correct
 

 parameters
 

 to
 

 the
 

 request
 

 by
 

 checking
 

 which
 

 parameters
 

 are
 

 required.
 

 For
 

 parameters
 

 with
 

 a
 

 fixed
 

 set
 

 of
 

 values,
 

 please
 

 use
 

 the
 

 spec
 

 to
 

 look
 

 at
 

 which
 

 values
 

 are
 

 allowed.\n\nUse
 

 the
 

 exact
 

 parameter
 

 names
 

 as
 

 listed
 

 in
 

 the
 

 spec,
 

 do
 

 not
 

 make
 

 up
 

 any
 

 names
 

 or
 

 abbreviate
 

 the
 

 names
 

 of
 

 parameters.\nIf
 

 you
 

 get
 

 a
 

 not
 

 found
 

 error,
 

 ensure
 

 that
 

 you
 

 are
 

 using
 

 a
 

 path
 

 that
 

 actually
 

 exists
 

 in
 

 the
 

 spec.\n"*
 ,
 *suffix
 



 :
 





 str
 





 =
 





 'Begin!\n\nQuestion:
 

 {input}\nThought:
 

 I
 

 should
 

 explore
 

 the
 

 spec
 

 to
 

 find
 

 the
 

 base
 

 url
 

 for
 

 the
 

 API.\n{agent_scratchpad}'*
 ,
 *format_instructions
 



 :
 





 str
 





 =
 





 'Use
 

 the
 

 following
 

 format:\n\nQuestion:
 

 the
 

 input
 

 question
 

 you
 

 must
 

 answer\nThought:
 

 you
 

 should
 

 always
 

 think
 

 about
 

 what
 

 to
 

 do\nAction:
 

 the
 

 action
 

 to
 

 take,
 

 should
 

 be
 

 one
 

 of
 

 [{tool_names}]\nAction
 

 Input:
 

 the
 

 input
 

 to
 

 the
 

 action\nObservation:
 

 the
 

 result
 

 of
 

 the
 

 action\n...
 

 (this
 

 Thought/Action/Action
 

 Input/Observation
 

 can
 

 repeat
 

 N
 

 times)\nThought:
 

 I
 

 now
 

 know
 

 the
 

 final
 

 answer\nFinal
 

 Answer:
 

 the
 

 final
 

 answer
 

 to
 

 the
 

 original
 

 input
 

 question'*
 ,
 *input_variables
 



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
 *max_iterations
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 15*
 ,
 *max_execution_time
 



 :
 





 Optional
 


 [
 


 float
 


 ]
 






 =
 





 None*
 ,
 *early_stopping_method
 



 :
 





 str
 





 =
 





 'force'*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *return_intermediate_steps
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.AgentExecutor](agents#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/openapi/base#create_openapi_agent)
[#](#langchain.agents.agent_toolkits.create_openapi_agent "Permalink to this definition") 



 Construct a json agent from an LLM and tools.
 








 langchain.agents.agent_toolkits.
 



 create_pandas_dataframe_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *df
 



 :
 





 Any*
 ,
 *callback_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]
 






 =
 





 None*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 '\nYou
 

 are
 

 working
 

 with
 

 a
 

 pandas
 

 dataframe
 

 in
 

 Python.
 

 The
 

 name
 

 of
 

 the
 

 dataframe
 

 is
 

 `df`.\nYou
 

 should
 

 use
 

 the
 

 tools
 

 below
 

 to
 

 answer
 

 the
 

 question
 

 posed
 

 of
 

 you:'*
 ,
 *suffix
 



 :
 





 str
 





 =
 





 '\nThis
 

 is
 

 the
 

 result
 

 of
 

 `print(df.head())`:\n{df}\n\nBegin!\nQuestion:
 

 {input}\n{agent_scratchpad}'*
 ,
 *input_variables
 



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
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *return_intermediate_steps
 



 :
 





 bool
 





 =
 





 False*
 ,
 *max_iterations
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 15*
 ,
 *max_execution_time
 



 :
 





 Optional
 


 [
 


 float
 


 ]
 






 =
 





 None*
 ,
 *early_stopping_method
 



 :
 





 str
 





 =
 





 'force'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.AgentExecutor](agents#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/pandas/base#create_pandas_dataframe_agent)
[#](#langchain.agents.agent_toolkits.create_pandas_dataframe_agent "Permalink to this definition") 



 Construct a pandas agent from an LLM and dataframe.
 








 langchain.agents.agent_toolkits.
 



 create_pbi_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *toolkit
 



 :
 





 Optional
 


 [
 

[langchain.agents.agent_toolkits.powerbi.toolkit.PowerBIToolkit](#langchain.agents.agent_toolkits.PowerBIToolkit "langchain.agents.agent_toolkits.powerbi.toolkit.PowerBIToolkit")


 ]*
 ,
 *powerbi
 



 :
 





 Optional
 


 [
 

[langchain.utilities.powerbi.PowerBIDataset](utilities#langchain.utilities.PowerBIDataset "langchain.utilities.powerbi.PowerBIDataset")


 ]
 






 =
 





 None*
 ,
 *callback_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]
 






 =
 





 None*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 'You
 

 are
 

 an
 

 agent
 

 designed
 

 to
 

 interact
 

 with
 

 a
 

 Power
 

 BI
 

 Dataset.\nGiven
 

 an
 

 input
 

 question,
 

 create
 

 a
 

 syntactically
 

 correct
 

 DAX
 

 query
 

 to
 

 run,
 

 then
 

 look
 

 at
 

 the
 

 results
 

 of
 

 the
 

 query
 

 and
 

 return
 

 the
 

 answer.\nUnless
 

 the
 

 user
 

 specifies
 

 a
 

 specific
 

 number
 

 of
 

 examples
 

 they
 

 wish
 

 to
 

 obtain,
 

 always
 

 limit
 

 your
 

 query
 

 to
 

 at
 

 most
 

 {top_k}
 

 results.\nYou
 

 can
 

 order
 

 the
 

 results
 

 by
 

 a
 

 relevant
 

 column
 

 to
 

 return
 

 the
 

 most
 

 interesting
 

 examples
 

 in
 

 the
 

 database.\nNever
 

 query
 

 for
 

 all
 

 the
 

 columns
 

 from
 

 a
 

 specific
 

 table,
 

 only
 

 ask
 

 for
 

 a
 

 the
 

 few
 

 relevant
 

 columns
 

 given
 

 the
 

 question.\n\nYou
 

 have
 

 access
 

 to
 

 tools
 

 for
 

 interacting
 

 with
 

 the
 

 Power
 

 BI
 

 Dataset.
 

 Only
 

 use
 

 the
 

 below
 

 tools.
 

 Only
 

 use
 

 the
 

 information
 

 returned
 

 by
 

 the
 

 below
 

 tools
 

 to
 

 construct
 

 your
 

 final
 

 answer.
 

 Usually
 

 I
 

 should
 

 first
 

 ask
 

 which
 

 tables
 

 I
 

 have,
 

 then
 

 how
 

 each
 

 table
 

 is
 

 defined
 

 and
 

 then
 

 ask
 

 the
 

 question
 

 to
 

 query
 

 tool
 

 to
 

 create
 

 a
 

 query
 

 for
 

 me
 

 and
 

 then
 

 I
 

 should
 

 ask
 

 the
 

 query
 

 tool
 

 to
 

 execute
 

 it,
 

 finally
 

 create
 

 a
 

 nice
 

 sentence
 

 that
 

 answers
 

 the
 

 question.
 

 If
 

 you
 

 receive
 

 an
 

 error
 

 back
 

 that
 

 mentions
 

 that
 

 the
 

 query
 

 was
 

 wrong
 

 try
 

 to
 

 phrase
 

 the
 

 question
 

 differently
 

 and
 

 get
 

 a
 

 new
 

 query
 

 from
 

 the
 

 question
 

 to
 

 query
 

 tool.\n\nIf
 

 the
 

 question
 

 does
 

 not
 

 seem
 

 related
 

 to
 

 the
 

 dataset,
 

 just
 

 return
 

 "I
 

 don\'t
 

 know"
 

 as
 

 the
 

 answer.\n'*
 ,
 *suffix
 



 :
 





 str
 





 =
 





 'Begin!\n\nQuestion:
 

 {input}\nThought:
 

 I
 

 should
 

 first
 

 ask
 

 which
 

 tables
 

 I
 

 have,
 

 then
 

 how
 

 each
 

 table
 

 is
 

 defined
 

 and
 

 then
 

 ask
 

 the
 

 question
 

 to
 

 query
 

 tool
 

 to
 

 create
 

 a
 

 query
 

 for
 

 me
 

 and
 

 then
 

 I
 

 should
 

 ask
 

 the
 

 query
 

 tool
 

 to
 

 execute
 

 it,
 

 finally
 

 create
 

 a
 

 nice
 

 sentence
 

 that
 

 answers
 

 the
 

 question.\n{agent_scratchpad}'*
 ,
 *format_instructions
 



 :
 





 str
 





 =
 





 'Use
 

 the
 

 following
 

 format:\n\nQuestion:
 

 the
 

 input
 

 question
 

 you
 

 must
 

 answer\nThought:
 

 you
 

 should
 

 always
 

 think
 

 about
 

 what
 

 to
 

 do\nAction:
 

 the
 

 action
 

 to
 

 take,
 

 should
 

 be
 

 one
 

 of
 

 [{tool_names}]\nAction
 

 Input:
 

 the
 

 input
 

 to
 

 the
 

 action\nObservation:
 

 the
 

 result
 

 of
 

 the
 

 action\n...
 

 (this
 

 Thought/Action/Action
 

 Input/Observation
 

 can
 

 repeat
 

 N
 

 times)\nThought:
 

 I
 

 now
 

 know
 

 the
 

 final
 

 answer\nFinal
 

 Answer:
 

 the
 

 final
 

 answer
 

 to
 

 the
 

 original
 

 input
 

 question'*
 ,
 *examples
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *input_variables
 



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
 *top_k
 



 :
 





 int
 





 =
 





 10*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *agent_kwargs
 



 :
 





 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*

 )
 


 →
 

[langchain.agents.agent.AgentExecutor](agents#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/powerbi/base#create_pbi_agent)
[#](#langchain.agents.agent_toolkits.create_pbi_agent "Permalink to this definition") 



 Construct a pbi agent from an LLM and tools.
 








 langchain.agents.agent_toolkits.
 



 create_pbi_chat_agent
 


 (
 
*llm
 



 :
 





 langchain.chat_models.base.BaseChatModel*
 ,
 *toolkit
 



 :
 





 Optional
 


 [
 

[langchain.agents.agent_toolkits.powerbi.toolkit.PowerBIToolkit](#langchain.agents.agent_toolkits.PowerBIToolkit "langchain.agents.agent_toolkits.powerbi.toolkit.PowerBIToolkit")


 ]*
 ,
 *powerbi
 



 :
 





 Optional
 


 [
 

[langchain.utilities.powerbi.PowerBIDataset](utilities#langchain.utilities.PowerBIDataset "langchain.utilities.powerbi.PowerBIDataset")


 ]
 






 =
 





 None*
 ,
 *callback_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]
 






 =
 





 None*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 'Assistant
 

 is
 

 a
 

 large
 

 language
 

 model
 

 trained
 

 by
 

 OpenAI
 

 built
 

 to
 

 help
 

 users
 

 interact
 

 with
 

 a
 

 PowerBI
 

 Dataset.\n\nAssistant
 

 is
 

 designed
 

 to
 

 be
 

 able
 

 to
 

 assist
 

 with
 

 a
 

 wide
 

 range
 

 of
 

 tasks,
 

 from
 

 answering
 

 simple
 

 questions
 

 to
 

 providing
 

 in-depth
 

 explanations
 

 and
 

 discussions
 

 on
 

 a
 

 wide
 

 range
 

 of
 

 topics.
 

 As
 

 a
 

 language
 

 model,
 

 Assistant
 

 is
 

 able
 

 to
 

 generate
 

 human-like
 

 text
 

 based
 

 on
 

 the
 

 input
 

 it
 

 receives,
 

 allowing
 

 it
 

 to
 

 engage
 

 in
 

 natural-sounding
 

 conversations
 

 and
 

 provide
 

 responses
 

 that
 

 are
 

 coherent
 

 and
 

 relevant
 

 to
 

 the
 

 topic
 

 at
 

 hand.\n\nAssistant
 

 is
 

 constantly
 

 learning
 

 and
 

 improving,
 

 and
 

 its
 

 capabilities
 

 are
 

 constantly
 

 evolving.
 

 It
 

 is
 

 able
 

 to
 

 process
 

 and
 

 understand
 

 large
 

 amounts
 

 of
 

 text,
 

 and
 

 can
 

 use
 

 this
 

 knowledge
 

 to
 

 provide
 

 accurate
 

 and
 

 informative
 

 responses
 

 to
 

 a
 

 wide
 

 range
 

 of
 

 questions.
 

 Additionally,
 

 Assistant
 

 is
 

 able
 

 to
 

 generate
 

 its
 

 own
 

 text
 

 based
 

 on
 

 the
 

 input
 

 it
 

 receives,
 

 allowing
 

 it
 

 to
 

 engage
 

 in
 

 discussions
 

 and
 

 provide
 

 explanations
 

 and
 

 descriptions
 

 on
 

 a
 

 wide
 

 range
 

 of
 

 topics.
 

 \n\nGiven
 

 an
 

 input
 

 question,
 

 create
 

 a
 

 syntactically
 

 correct
 

 DAX
 

 query
 

 to
 

 run,
 

 then
 

 look
 

 at
 

 the
 

 results
 

 of
 

 the
 

 query
 

 and
 

 return
 

 the
 

 answer.
 

 Unless
 

 the
 

 user
 

 specifies
 

 a
 

 specific
 

 number
 

 of
 

 examples
 

 they
 

 wish
 

 to
 

 obtain,
 

 always
 

 limit
 

 your
 

 query
 

 to
 

 at
 

 most
 

 {top_k}
 

 results.
 

 You
 

 can
 

 order
 

 the
 

 results
 

 by
 

 a
 

 relevant
 

 column
 

 to
 

 return
 

 the
 

 most
 

 interesting
 

 examples
 

 in
 

 the
 

 database.\n\nOverall,
 

 Assistant
 

 is
 

 a
 

 powerful
 

 system
 

 that
 

 can
 

 help
 

 with
 

 a
 

 wide
 

 range
 

 of
 

 tasks
 

 and
 

 provide
 

 valuable
 

 insights
 

 and
 

 information
 

 on
 

 a
 

 wide
 

 range
 

 of
 

 topics.
 

 Whether
 

 you
 

 need
 

 help
 

 with
 

 a
 

 specific
 

 question
 

 or
 

 just
 

 want
 

 to
 

 have
 

 a
 

 conversation
 

 about
 

 a
 

 particular
 

 topic,
 

 Assistant
 

 is
 

 here
 

 to
 

 assist.\n\nUsually
 

 I
 

 should
 

 first
 

 ask
 

 which
 

 tables
 

 I
 

 have,
 

 then
 

 how
 

 each
 

 table
 

 is
 

 defined
 

 and
 

 then
 

 ask
 

 the
 

 question
 

 to
 

 query
 

 tool
 

 to
 

 create
 

 a
 

 query
 

 for
 

 me
 

 and
 

 then
 

 I
 

 should
 

 ask
 

 the
 

 query
 

 tool
 

 to
 

 execute
 

 it,
 

 finally
 

 create
 

 a
 

 complete
 

 sentence
 

 that
 

 answers
 

 the
 

 question.
 

 If
 

 you
 

 receive
 

 an
 

 error
 

 back
 

 that
 

 mentions
 

 that
 

 the
 

 query
 

 was
 

 wrong
 

 try
 

 to
 

 phrase
 

 the
 

 question
 

 differently
 

 and
 

 get
 

 a
 

 new
 

 query
 

 from
 

 the
 

 question
 

 to
 

 query
 

 tool.\n'*
 ,
 *suffix
 



 :
 





 str
 





 =
 





 "TOOLS\n------\nAssistant
 

 can
 

 ask
 

 the
 

 user
 

 to
 

 use
 

 tools
 

 to
 

 look
 

 up
 

 information
 

 that
 

 may
 

 be
 

 helpful
 

 in
 

 answering
 

 the
 

 users
 

 original
 

 question.
 

 The
 

 tools
 

 the
 

 human
 

 can
 

 use
 

 are:\n\n{{tools}}\n\n{format_instructions}\n\nUSER'S
 

 INPUT\n--------------------\nHere
 

 is
 

 the
 

 user's
 

 input
 

 (remember
 

 to
 

 respond
 

 with
 

 a
 

 markdown
 

 code
 

 snippet
 

 of
 

 a
 

 json
 

 blob
 

 with
 

 a
 

 single
 

 action,
 

 and
 

 NOTHING
 

 else):\n\n{{{{input}}}}\n"*
 ,
 *examples
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *input_variables
 



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
 *memory
 



 :
 





 Optional
 


 [
 


 langchain.memory.chat_memory.BaseChatMemory
 


 ]
 






 =
 





 None*
 ,
 *top_k
 



 :
 





 int
 





 =
 





 10*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *agent_kwargs
 



 :
 





 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*

 )
 


 →
 

[langchain.agents.agent.AgentExecutor](agents#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/powerbi/chat_base#create_pbi_chat_agent)
[#](#langchain.agents.agent_toolkits.create_pbi_chat_agent "Permalink to this definition") 



 Construct a pbi agent from an Chat LLM and tools.
 



 If you supply only a toolkit and no powerbi dataset, the same LLM is used for both.
 








 langchain.agents.agent_toolkits.
 



 create_python_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *tool
 



 :
 





 langchain.tools.python.tool.PythonREPLTool*
 ,
 *callback_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]
 






 =
 





 None*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 'You
 

 are
 

 an
 

 agent
 

 designed
 

 to
 

 write
 

 and
 

 execute
 

 python
 

 code
 

 to
 

 answer
 

 questions.\nYou
 

 have
 

 access
 

 to
 

 a
 

 python
 

 REPL,
 

 which
 

 you
 

 can
 

 use
 

 to
 

 execute
 

 python
 

 code.\nIf
 

 you
 

 get
 

 an
 

 error,
 

 debug
 

 your
 

 code
 

 and
 

 try
 

 again.\nOnly
 

 use
 

 the
 

 output
 

 of
 

 your
 

 code
 

 to
 

 answer
 

 the
 

 question.
 

 \nYou
 

 might
 

 know
 

 the
 

 answer
 

 without
 

 running
 

 any
 

 code,
 

 but
 

 you
 

 should
 

 still
 

 run
 

 the
 

 code
 

 to
 

 get
 

 the
 

 answer.\nIf
 

 it
 

 does
 

 not
 

 seem
 

 like
 

 you
 

 can
 

 write
 

 code
 

 to
 

 answer
 

 the
 

 question,
 

 just
 

 return
 

 "I
 

 don\'t
 

 know"
 

 as
 

 the
 

 answer.\n'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.AgentExecutor](agents#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/python/base#create_python_agent)
[#](#langchain.agents.agent_toolkits.create_python_agent "Permalink to this definition") 



 Construct a python agent from an LLM and tool.
 








 langchain.agents.agent_toolkits.
 



 create_sql_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *toolkit
 



 :
 




[langchain.agents.agent_toolkits.sql.toolkit.SQLDatabaseToolkit](#langchain.agents.agent_toolkits.SQLDatabaseToolkit "langchain.agents.agent_toolkits.sql.toolkit.SQLDatabaseToolkit")*
 ,
 *callback_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]
 






 =
 





 None*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 'You
 

 are
 

 an
 

 agent
 

 designed
 

 to
 

 interact
 

 with
 

 a
 

 SQL
 

 database.\nGiven
 

 an
 

 input
 

 question,
 

 create
 

 a
 

 syntactically
 

 correct
 

 {dialect}
 

 query
 

 to
 

 run,
 

 then
 

 look
 

 at
 

 the
 

 results
 

 of
 

 the
 

 query
 

 and
 

 return
 

 the
 

 answer.\nUnless
 

 the
 

 user
 

 specifies
 

 a
 

 specific
 

 number
 

 of
 

 examples
 

 they
 

 wish
 

 to
 

 obtain,
 

 always
 

 limit
 

 your
 

 query
 

 to
 

 at
 

 most
 

 {top_k}
 

 results.\nYou
 

 can
 

 order
 

 the
 

 results
 

 by
 

 a
 

 relevant
 

 column
 

 to
 

 return
 

 the
 

 most
 

 interesting
 

 examples
 

 in
 

 the
 

 database.\nNever
 

 query
 

 for
 

 all
 

 the
 

 columns
 

 from
 

 a
 

 specific
 

 table,
 

 only
 

 ask
 

 for
 

 the
 

 relevant
 

 columns
 

 given
 

 the
 

 question.\nYou
 

 have
 

 access
 

 to
 

 tools
 

 for
 

 interacting
 

 with
 

 the
 

 database.\nOnly
 

 use
 

 the
 

 below
 

 tools.
 

 Only
 

 use
 

 the
 

 information
 

 returned
 

 by
 

 the
 

 below
 

 tools
 

 to
 

 construct
 

 your
 

 final
 

 answer.\nYou
 

 MUST
 

 double
 

 check
 

 your
 

 query
 

 before
 

 executing
 

 it.
 

 If
 

 you
 

 get
 

 an
 

 error
 

 while
 

 executing
 

 a
 

 query,
 

 rewrite
 

 the
 

 query
 

 and
 

 try
 

 again.\n\nDO
 

 NOT
 

 make
 

 any
 

 DML
 

 statements
 

 (INSERT,
 

 UPDATE,
 

 DELETE,
 

 DROP
 

 etc.)
 

 to
 

 the
 

 database.\n\nIf
 

 the
 

 question
 

 does
 

 not
 

 seem
 

 related
 

 to
 

 the
 

 database,
 

 just
 

 return
 

 "I
 

 don\'t
 

 know"
 

 as
 

 the
 

 answer.\n'*
 ,
 *suffix
 



 :
 





 str
 





 =
 





 'Begin!\n\nQuestion:
 

 {input}\nThought:
 

 I
 

 should
 

 look
 

 at
 

 the
 

 tables
 

 in
 

 the
 

 database
 

 to
 

 see
 

 what
 

 I
 

 can
 

 query.\n{agent_scratchpad}'*
 ,
 *format_instructions
 



 :
 





 str
 





 =
 





 'Use
 

 the
 

 following
 

 format:\n\nQuestion:
 

 the
 

 input
 

 question
 

 you
 

 must
 

 answer\nThought:
 

 you
 

 should
 

 always
 

 think
 

 about
 

 what
 

 to
 

 do\nAction:
 

 the
 

 action
 

 to
 

 take,
 

 should
 

 be
 

 one
 

 of
 

 [{tool_names}]\nAction
 

 Input:
 

 the
 

 input
 

 to
 

 the
 

 action\nObservation:
 

 the
 

 result
 

 of
 

 the
 

 action\n...
 

 (this
 

 Thought/Action/Action
 

 Input/Observation
 

 can
 

 repeat
 

 N
 

 times)\nThought:
 

 I
 

 now
 

 know
 

 the
 

 final
 

 answer\nFinal
 

 Answer:
 

 the
 

 final
 

 answer
 

 to
 

 the
 

 original
 

 input
 

 question'*
 ,
 *input_variables
 



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
 *top_k
 



 :
 





 int
 





 =
 





 10*
 ,
 *max_iterations
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 15*
 ,
 *max_execution_time
 



 :
 





 Optional
 


 [
 


 float
 


 ]
 






 =
 





 None*
 ,
 *early_stopping_method
 



 :
 





 str
 





 =
 





 'force'*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.AgentExecutor](agents#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/sql/base#create_sql_agent)
[#](#langchain.agents.agent_toolkits.create_sql_agent "Permalink to this definition") 



 Construct a sql agent from an LLM and tools.
 








 langchain.agents.agent_toolkits.
 



 create_vectorstore_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *toolkit
 



 :
 




[langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreToolkit](#langchain.agents.agent_toolkits.VectorStoreToolkit "langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreToolkit")*
 ,
 *callback_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]
 






 =
 





 None*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 'You
 

 are
 

 an
 

 agent
 

 designed
 

 to
 

 answer
 

 questions
 

 about
 

 sets
 

 of
 

 documents.\nYou
 

 have
 

 access
 

 to
 

 tools
 

 for
 

 interacting
 

 with
 

 the
 

 documents,
 

 and
 

 the
 

 inputs
 

 to
 

 the
 

 tools
 

 are
 

 questions.\nSometimes,
 

 you
 

 will
 

 be
 

 asked
 

 to
 

 provide
 

 sources
 

 for
 

 your
 

 questions,
 

 in
 

 which
 

 case
 

 you
 

 should
 

 use
 

 the
 

 appropriate
 

 tool
 

 to
 

 do
 

 so.\nIf
 

 the
 

 question
 

 does
 

 not
 

 seem
 

 relevant
 

 to
 

 any
 

 of
 

 the
 

 tools
 

 provided,
 

 just
 

 return
 

 "I
 

 don\'t
 

 know"
 

 as
 

 the
 

 answer.\n'*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.AgentExecutor](agents#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/vectorstore/base#create_vectorstore_agent)
[#](#langchain.agents.agent_toolkits.create_vectorstore_agent "Permalink to this definition") 



 Construct a vectorstore agent from an LLM and tools.
 








 langchain.agents.agent_toolkits.
 



 create_vectorstore_router_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *toolkit
 



 :
 




[langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreRouterToolkit](#langchain.agents.agent_toolkits.VectorStoreRouterToolkit "langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreRouterToolkit")*
 ,
 *callback_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]
 






 =
 





 None*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 'You
 

 are
 

 an
 

 agent
 

 designed
 

 to
 

 answer
 

 questions.\nYou
 

 have
 

 access
 

 to
 

 tools
 

 for
 

 interacting
 

 with
 

 different
 

 sources,
 

 and
 

 the
 

 inputs
 

 to
 

 the
 

 tools
 

 are
 

 questions.\nYour
 

 main
 

 task
 

 is
 

 to
 

 decide
 

 which
 

 of
 

 the
 

 tools
 

 is
 

 relevant
 

 for
 

 answering
 

 question
 

 at
 

 hand.\nFor
 

 complex
 

 questions,
 

 you
 

 can
 

 break
 

 the
 

 question
 

 down
 

 into
 

 sub
 

 questions
 

 and
 

 use
 

 tools
 

 to
 

 answers
 

 the
 

 sub
 

 questions.\n'*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.AgentExecutor](agents#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/vectorstore/base#create_vectorstore_router_agent)
[#](#langchain.agents.agent_toolkits.create_vectorstore_router_agent "Permalink to this definition") 



 Construct a vectorstore router agent from an LLM and tools.
 






