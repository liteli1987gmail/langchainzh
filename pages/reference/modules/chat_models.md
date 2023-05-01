




 Chat Models
 [#](#module-langchain.chat_models "Permalink to this headline")
==============================================================================




*pydantic
 

 model*


 langchain.chat_models.
 



 AzureChatOpenAI
 

[[source]](../../_modules/langchain/chat_models/azure_openai#AzureChatOpenAI)
[#](#langchain.chat_models.AzureChatOpenAI "Permalink to this definition") 



 Wrapper around Azure OpenAI Chat Completion API. To use this class you
must have a deployed model on Azure OpenAI. Use
 
 deployment_name
 
 in the
constructor to refer to the “Model deployment name” in the Azure portal.
 



 In addition, you should have the
 `openai`
 python package installed, and the
following environment variables set or passed in constructor in lower case:
-
 `OPENAI_API_TYPE`
 (default:
 `azure`
 )
-
 `OPENAI_API_KEY`
 -
 `OPENAI_API_BASE`
 -
 `OPENAI_API_VERSION`




 For exmaple, if you have
 
 gpt-35-turbo
 
 deployed, with the deployment name
 
 35-turbo-dev
 
 , the constructor should look like:
 



 Be aware the API version may change.
 



 Any parameters that are valid to be passed to the openai.create call can be passed
in, even if not explicitly saved on this class.
 




*field*


 deployment_name
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.chat_models.AzureChatOpenAI.deployment_name "Permalink to this definition") 






*field*


 openai_api_base
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.chat_models.AzureChatOpenAI.openai_api_base "Permalink to this definition") 






*field*


 openai_api_key
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.chat_models.AzureChatOpenAI.openai_api_key "Permalink to this definition") 






*field*


 openai_api_type
 

*:
 




 str*
*=
 




 'azure'*
[#](#langchain.chat_models.AzureChatOpenAI.openai_api_type "Permalink to this definition") 






*field*


 openai_api_version
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.chat_models.AzureChatOpenAI.openai_api_version "Permalink to this definition") 






*field*


 openai_organization
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.chat_models.AzureChatOpenAI.openai_organization "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chat_models.
 



 ChatAnthropic
 

[[source]](../../_modules/langchain/chat_models/anthropic#ChatAnthropic)
[#](#langchain.chat_models.ChatAnthropic "Permalink to this definition") 



 Wrapper around Anthropic’s large language model.
 



 To use, you should have the
 `anthropic`
 python package installed, and the
environment variable
 `ANTHROPIC_API_KEY`
 set with your API key, or pass
it as a named parameter to the constructor.
 



 Example
 




*field*


 callback_manager
 

*:
 




 Optional
 


 [
 


 langchain.callbacks.base.BaseCallbackManager
 


 ]*
*=
 




 None*
[#](#langchain.chat_models.ChatAnthropic.callback_manager "Permalink to this definition") 






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
[#](#langchain.chat_models.ChatAnthropic.callbacks "Permalink to this definition") 






*field*


 verbose
 

*:
 




 bool*
*[Optional]*
[#](#langchain.chat_models.ChatAnthropic.verbose "Permalink to this definition") 



 Whether to print out response text.
 








*pydantic
 

 model*


 langchain.chat_models.
 



 ChatOpenAI
 

[[source]](../../_modules/langchain/chat_models/openai#ChatOpenAI)
[#](#langchain.chat_models.ChatOpenAI "Permalink to this definition") 



 Wrapper around OpenAI Chat large language models.
 



 To use, you should have the
 `openai`
 python package installed, and the
environment variable
 `OPENAI_API_KEY`
 set with your API key.
 



 Any parameters that are valid to be passed to the openai.create call can be passed
in, even if not explicitly saved on this class.
 



 Example
 





```
from langchain.chat_models import ChatOpenAI
openai = ChatOpenAI(model_name="gpt-3.5-turbo")

```





*field*


 max_retries
 

*:
 




 int*
*=
 




 6*
[#](#langchain.chat_models.ChatOpenAI.max_retries "Permalink to this definition") 



 Maximum number of retries to make when generating.
 






*field*


 max_tokens
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.chat_models.ChatOpenAI.max_tokens "Permalink to this definition") 



 Maximum number of tokens to generate.
 






*field*


 model_kwargs
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
*[Optional]*
[#](#langchain.chat_models.ChatOpenAI.model_kwargs "Permalink to this definition") 



 Holds any model parameters valid for
 
 create
 
 call not explicitly specified.
 






*field*


 model_name
 

*:
 




 str*
*=
 




 'gpt-3.5-turbo'*
[#](#langchain.chat_models.ChatOpenAI.model_name "Permalink to this definition") 



 Model name to use.
 






*field*


 n
 

*:
 




 int*
*=
 




 1*
[#](#langchain.chat_models.ChatOpenAI.n "Permalink to this definition") 



 Number of chat completions to generate for each prompt.
 






*field*


 openai_api_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.chat_models.ChatOpenAI.openai_api_key "Permalink to this definition") 






*field*


 openai_organization
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.chat_models.ChatOpenAI.openai_organization "Permalink to this definition") 






*field*


 request_timeout
 

*:
 




 int*
*=
 




 60*
[#](#langchain.chat_models.ChatOpenAI.request_timeout "Permalink to this definition") 



 Timeout in seconds for the OpenAPI request.
 






*field*


 streaming
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.chat_models.ChatOpenAI.streaming "Permalink to this definition") 



 Whether to stream the results or not.
 






*field*


 temperature
 

*:
 




 float*
*=
 




 0.7*
[#](#langchain.chat_models.ChatOpenAI.temperature "Permalink to this definition") 



 What sampling temperature to use.
 








 completion_with_retry
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Any
 


[[source]](../../_modules/langchain/chat_models/openai#ChatOpenAI.completion_with_retry)
[#](#langchain.chat_models.ChatOpenAI.completion_with_retry "Permalink to this definition") 



 Use tenacity to retry the completion call.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[[source]](../../_modules/langchain/chat_models/openai#ChatOpenAI.get_num_tokens)
[#](#langchain.chat_models.ChatOpenAI.get_num_tokens "Permalink to this definition") 



 Calculate num tokens with tiktoken package.
 








 get_num_tokens_from_messages
 


 (
 
*messages
 



 :
 





 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]*

 )
 


 →
 


 int
 


[[source]](../../_modules/langchain/chat_models/openai#ChatOpenAI.get_num_tokens_from_messages)
[#](#langchain.chat_models.ChatOpenAI.get_num_tokens_from_messages "Permalink to this definition") 



 Calculate num tokens for gpt-3.5-turbo and gpt-4 with tiktoken package.
 



 Official documentation:
 [openai/openai-cookbook](https://github.com/openai/openai-cookbook/blob/) 
 main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb
 








*pydantic
 

 model*


 langchain.chat_models.
 



 PromptLayerChatOpenAI
 

[[source]](../../_modules/langchain/chat_models/promptlayer_openai#PromptLayerChatOpenAI)
[#](#langchain.chat_models.PromptLayerChatOpenAI "Permalink to this definition") 



 Wrapper around OpenAI Chat large language models and PromptLayer.
 



 To use, you should have the
 `openai`
 and
 `promptlayer`
 python
package installed, and the environment variable
 `OPENAI_API_KEY`
 and
 `PROMPTLAYER_API_KEY`
 set with your openAI API key and
promptlayer key respectively.
 



 All parameters that can be passed to the OpenAI LLM can also
be passed here. The PromptLayerChatOpenAI adds to optional
:param
 `pl_tags`
 : List of strings to tag the request with.
:param
 `return_pl_id`
 : If True, the PromptLayer request ID will be
 



> 
> 
> 
>  returned in the
>  `generation_info`
>  field of the
>  `Generation`
>  object.
>  
> 
> 
> 
> 



 Example
 





```
from langchain.chat_models import PromptLayerChatOpenAI
openai = PromptLayerChatOpenAI(model_name="gpt-3.5-turbo")

```





*field*


 pl_tags
 

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
[#](#langchain.chat_models.PromptLayerChatOpenAI.pl_tags "Permalink to this definition") 






*field*


 return_pl_id
 

*:
 




 Optional
 


 [
 


 bool
 


 ]*
*=
 




 False*
[#](#langchain.chat_models.PromptLayerChatOpenAI.return_pl_id "Permalink to this definition") 








