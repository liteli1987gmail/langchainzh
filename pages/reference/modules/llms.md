




 LLMs
 [#](#module-langchain.llms "Permalink to this headline")
================================================================



 Wrappers on top of large language models APIs.
 




*pydantic
 

 model*


 langchain.llms.
 



 AI21
 

[[source]](../../_modules/langchain/llms/ai21#AI21)
[#](#langchain.llms.AI21 "Permalink to this definition") 



 Wrapper around AI21 large language models.
 



 To use, you should have the environment variable
 `AI21_API_KEY`
 set with your API key.
 



 Example
 





```
from langchain.llms import AI21
ai21 = AI21(model="j2-jumbo-instruct")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 base_url
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.AI21.base_url "Permalink to this definition") 



 Base url to use, if None decides based on model name.
 






*field*


 countPenalty
 

*:
 




 langchain.llms.ai21.AI21PenaltyData*
*=
 




 AI21PenaltyData(scale=0,
 

 applyToWhitespaces=True,
 

 applyToPunctuations=True,
 

 applyToNumbers=True,
 

 applyToStopwords=True,
 

 applyToEmojis=True)*
[#](#langchain.llms.AI21.countPenalty "Permalink to this definition") 



 Penalizes repeated tokens according to count.
 






*field*


 frequencyPenalty
 

*:
 




 langchain.llms.ai21.AI21PenaltyData*
*=
 




 AI21PenaltyData(scale=0,
 

 applyToWhitespaces=True,
 

 applyToPunctuations=True,
 

 applyToNumbers=True,
 

 applyToStopwords=True,
 

 applyToEmojis=True)*
[#](#langchain.llms.AI21.frequencyPenalty "Permalink to this definition") 



 Penalizes repeated tokens according to frequency.
 






*field*


 logitBias
 

*:
 




 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 float
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.llms.AI21.logitBias "Permalink to this definition") 



 Adjust the probability of specific tokens being generated.
 






*field*


 maxTokens
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.AI21.maxTokens "Permalink to this definition") 



 The maximum number of tokens to generate in the completion.
 






*field*


 minTokens
 

*:
 




 int*
*=
 




 0*
[#](#langchain.llms.AI21.minTokens "Permalink to this definition") 



 The minimum number of tokens to generate in the completion.
 






*field*


 model
 

*:
 




 str*
*=
 




 'j2-jumbo-instruct'*
[#](#langchain.llms.AI21.model "Permalink to this definition") 



 Model name to use.
 






*field*


 numResults
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.AI21.numResults "Permalink to this definition") 



 How many completions to generate for each prompt.
 






*field*


 presencePenalty
 

*:
 




 langchain.llms.ai21.AI21PenaltyData*
*=
 




 AI21PenaltyData(scale=0,
 

 applyToWhitespaces=True,
 

 applyToPunctuations=True,
 

 applyToNumbers=True,
 

 applyToStopwords=True,
 

 applyToEmojis=True)*
[#](#langchain.llms.AI21.presencePenalty "Permalink to this definition") 



 Penalizes repeated tokens.
 






*field*


 temperature
 

*:
 




 float*
*=
 




 0.7*
[#](#langchain.llms.AI21.temperature "Permalink to this definition") 



 What sampling temperature to use.
 






*field*


 topP
 

*:
 




 float*
*=
 




 1.0*
[#](#langchain.llms.AI21.topP "Permalink to this definition") 



 Total probability mass of tokens to consider at each step.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.AI21.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AI21.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AI21.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.AI21.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.AI21.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.AI21.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AI21.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AI21.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.AI21.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.AI21.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.AI21.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.AI21.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.AI21.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 AlephAlpha
 

[[source]](../../_modules/langchain/llms/aleph_alpha#AlephAlpha)
[#](#langchain.llms.AlephAlpha "Permalink to this definition") 



 Wrapper around Aleph Alpha large language models.
 



 To use, you should have the
 `aleph_alpha_client`
 python package installed, and the
environment variable
 `ALEPH_ALPHA_API_KEY`
 set with your API key, or pass
it as a named parameter to the constructor.
 



 Parameters are explained more in depth here:
 [Aleph-Alpha/aleph-alpha-client](https://github.com/Aleph-Alpha/aleph-alpha-client/blob/c14b7dd2b4325c7da0d6a119f6e76385800e097b/aleph_alpha_client/completion.py#L10) 




 Example
 





```
from langchain.llms import AlephAlpha
alpeh_alpha = AlephAlpha(aleph_alpha_api_key="my-api-key")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 aleph_alpha_api_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.AlephAlpha.aleph_alpha_api_key "Permalink to this definition") 



 API key for Aleph Alpha API.
 






*field*


 best_of
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.llms.AlephAlpha.best_of "Permalink to this definition") 



 returns the one with the “best of” results
(highest log probability per token)
 






*field*


 completion_bias_exclusion_first_token_only
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.AlephAlpha.completion_bias_exclusion_first_token_only "Permalink to this definition") 



 Only consider the first token for the completion_bias_exclusion.
 






*field*


 contextual_control_threshold
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 None*
[#](#langchain.llms.AlephAlpha.contextual_control_threshold "Permalink to this definition") 



 If set to None, attention control parameters only apply to those tokens that have
explicitly been set in the request.
If set to a non-None value, control parameters are also applied to similar tokens.
 






*field*


 control_log_additive
 

*:
 




 Optional
 


 [
 


 bool
 


 ]*
*=
 




 True*
[#](#langchain.llms.AlephAlpha.control_log_additive "Permalink to this definition") 



 True: apply control by adding the log(control_factor) to attention scores.
False: (attention_scores - - attention_scores.min(-1)) \* control_factor
 






*field*


 echo
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.AlephAlpha.echo "Permalink to this definition") 



 Echo the prompt in the completion.
 






*field*


 frequency_penalty
 

*:
 




 float*
*=
 




 0.0*
[#](#langchain.llms.AlephAlpha.frequency_penalty "Permalink to this definition") 



 Penalizes repeated tokens according to frequency.
 






*field*


 log_probs
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.llms.AlephAlpha.log_probs "Permalink to this definition") 



 Number of top log probabilities to be returned for each generated token.
 






*field*


 logit_bias
 

*:
 




 Optional
 


 [
 


 Dict
 


 [
 


 int
 


 ,
 




 float
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.llms.AlephAlpha.logit_bias "Permalink to this definition") 



 The logit bias allows to influence the likelihood of generating tokens.
 






*field*


 maximum_tokens
 

*:
 




 int*
*=
 




 64*
[#](#langchain.llms.AlephAlpha.maximum_tokens "Permalink to this definition") 



 The maximum number of tokens to be generated.
 






*field*


 minimum_tokens
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 0*
[#](#langchain.llms.AlephAlpha.minimum_tokens "Permalink to this definition") 



 Generate at least this number of tokens.
 






*field*


 model
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 'luminous-base'*
[#](#langchain.llms.AlephAlpha.model "Permalink to this definition") 



 Model name to use.
 






*field*


 n
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.AlephAlpha.n "Permalink to this definition") 



 How many completions to generate for each prompt.
 






*field*


 penalty_bias
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.AlephAlpha.penalty_bias "Permalink to this definition") 



 Penalty bias for the completion.
 






*field*


 penalty_exceptions
 

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
[#](#langchain.llms.AlephAlpha.penalty_exceptions "Permalink to this definition") 



 List of strings that may be generated without penalty,
regardless of other penalty settings
 






*field*


 penalty_exceptions_include_stop_sequences
 

*:
 




 Optional
 


 [
 


 bool
 


 ]*
*=
 




 None*
[#](#langchain.llms.AlephAlpha.penalty_exceptions_include_stop_sequences "Permalink to this definition") 



 Should stop_sequences be included in penalty_exceptions.
 






*field*


 presence_penalty
 

*:
 




 float*
*=
 




 0.0*
[#](#langchain.llms.AlephAlpha.presence_penalty "Permalink to this definition") 



 Penalizes repeated tokens.
 






*field*


 raw_completion
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.AlephAlpha.raw_completion "Permalink to this definition") 



 Force the raw completion of the model to be returned.
 






*field*


 repetition_penalties_include_completion
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.llms.AlephAlpha.repetition_penalties_include_completion "Permalink to this definition") 



 Flag deciding whether presence penalty or frequency penalty
are updated from the completion.
 






*field*


 repetition_penalties_include_prompt
 

*:
 




 Optional
 


 [
 


 bool
 


 ]*
*=
 




 False*
[#](#langchain.llms.AlephAlpha.repetition_penalties_include_prompt "Permalink to this definition") 



 Flag deciding whether presence penalty or frequency penalty are
updated from the prompt.
 






*field*


 stop_sequences
 

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
[#](#langchain.llms.AlephAlpha.stop_sequences "Permalink to this definition") 



 Stop sequences to use.
 






*field*


 temperature
 

*:
 




 float*
*=
 




 0.0*
[#](#langchain.llms.AlephAlpha.temperature "Permalink to this definition") 



 A non-negative float that tunes the degree of randomness in generation.
 






*field*


 tokens
 

*:
 




 Optional
 


 [
 


 bool
 


 ]*
*=
 




 False*
[#](#langchain.llms.AlephAlpha.tokens "Permalink to this definition") 



 return tokens of completion.
 






*field*


 top_k
 

*:
 




 int*
*=
 




 0*
[#](#langchain.llms.AlephAlpha.top_k "Permalink to this definition") 



 Number of most likely tokens to consider at each step.
 






*field*


 top_p
 

*:
 




 float*
*=
 




 0.0*
[#](#langchain.llms.AlephAlpha.top_p "Permalink to this definition") 



 Total probability mass of tokens to consider at each step.
 






*field*


 use_multiplicative_presence_penalty
 

*:
 




 Optional
 


 [
 


 bool
 


 ]*
*=
 




 False*
[#](#langchain.llms.AlephAlpha.use_multiplicative_presence_penalty "Permalink to this definition") 



 Flag deciding whether presence penalty is applied
multiplicatively (True) or additively (False).
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.AlephAlpha.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AlephAlpha.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AlephAlpha.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.AlephAlpha.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.AlephAlpha.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.AlephAlpha.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AlephAlpha.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AlephAlpha.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.AlephAlpha.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.AlephAlpha.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.AlephAlpha.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.AlephAlpha.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.AlephAlpha.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 Anthropic
 

[[source]](../../_modules/langchain/llms/anthropic#Anthropic)
[#](#langchain.llms.Anthropic "Permalink to this definition") 



 Wrapper around Anthropic’s large language models.
 



 To use, you should have the
 `anthropic`
 python package installed, and the
environment variable
 `ANTHROPIC_API_KEY`
 set with your API key, or pass
it as a named parameter to the constructor.
 



 Example
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `raise_warning`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 default_request_timeout
 

*:
 




 Optional
 


 [
 


 Union
 


 [
 


 float
 


 ,
 




 Tuple
 


 [
 


 float
 


 ,
 




 float
 


 ]
 



 ]
 



 ]*
*=
 




 None*
[#](#langchain.llms.Anthropic.default_request_timeout "Permalink to this definition") 



 Timeout for requests to Anthropic Completion API. Default is 600 seconds.
 






*field*


 max_tokens_to_sample
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.Anthropic.max_tokens_to_sample "Permalink to this definition") 



 Denotes the number of tokens to predict per generation.
 






*field*


 model
 

*:
 




 str*
*=
 




 'claude-v1'*
[#](#langchain.llms.Anthropic.model "Permalink to this definition") 



 Model name to use.
 






*field*


 streaming
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.Anthropic.streaming "Permalink to this definition") 



 Whether to stream the results.
 






*field*


 temperature
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 None*
[#](#langchain.llms.Anthropic.temperature "Permalink to this definition") 



 A non-negative float that tunes the degree of randomness in generation.
 






*field*


 top_k
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.llms.Anthropic.top_k "Permalink to this definition") 



 Number of most likely tokens to consider at each step.
 






*field*


 top_p
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 None*
[#](#langchain.llms.Anthropic.top_p "Permalink to this definition") 



 Total probability mass of tokens to consider at each step.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.Anthropic.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Anthropic.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Anthropic.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Anthropic.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Anthropic.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.Anthropic.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Anthropic.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Anthropic.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.Anthropic.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.Anthropic.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.Anthropic.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.Anthropic.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 








 stream
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 Generator
 


[[source]](../../_modules/langchain/llms/anthropic#Anthropic.stream)
[#](#langchain.llms.Anthropic.stream "Permalink to this definition") 



 Call Anthropic completion_stream and return the resulting generator.
 



 BETA: this is a beta feature while we figure out the right abstraction.
Once that happens, this interface could change.
 




 Parameters
 

* **prompt** 
 – The prompt to pass into the model.
* **stop** 
 – Optional list of stop words to use when generating.




 Returns
 


 A generator representing the stream of tokens from Anthropic.
 





 Example
 





```
prompt = "Write a poem about a stream."
prompt = f"\n\nHuman: {prompt}\n\nAssistant:"
generator = anthropic.stream(prompt)
for token in generator:
    yield token

```







*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.Anthropic.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 AzureOpenAI
 

[[source]](../../_modules/langchain/llms/openai#AzureOpenAI)
[#](#langchain.llms.AzureOpenAI "Permalink to this definition") 



 Wrapper around Azure-specific OpenAI large language models.
 



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
from langchain.llms import AzureOpenAI
openai = AzureOpenAI(model_name="text-davinci-003")

```





 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 allowed_special
 

*:
 




 Union
 


 [
 


 Literal
 


 [
 



 'all'
 



 ]
 



 ,
 




 AbstractSet
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 {}*
[#](#langchain.llms.AzureOpenAI.allowed_special "Permalink to this definition") 



 Set of special tokens that are allowed。
 






*field*


 batch_size
 

*:
 




 int*
*=
 




 20*
[#](#langchain.llms.AzureOpenAI.batch_size "Permalink to this definition") 



 Batch size to use when passing multiple documents to generate.
 






*field*


 best_of
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.AzureOpenAI.best_of "Permalink to this definition") 



 Generates best_of completions server-side and returns the “best”.
 






*field*


 deployment_name
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.llms.AzureOpenAI.deployment_name "Permalink to this definition") 



 Deployment name to use.
 






*field*


 disallowed_special
 

*:
 




 Union
 


 [
 


 Literal
 


 [
 



 'all'
 



 ]
 



 ,
 




 Collection
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 'all'*
[#](#langchain.llms.AzureOpenAI.disallowed_special "Permalink to this definition") 



 Set of special tokens that are not allowed。
 






*field*


 frequency_penalty
 

*:
 




 float*
*=
 




 0*
[#](#langchain.llms.AzureOpenAI.frequency_penalty "Permalink to this definition") 



 Penalizes repeated tokens according to frequency.
 






*field*


 logit_bias
 

*:
 




 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 float
 


 ]
 



 ]*
*[Optional]*
[#](#langchain.llms.AzureOpenAI.logit_bias "Permalink to this definition") 



 Adjust the probability of specific tokens being generated.
 






*field*


 max_retries
 

*:
 




 int*
*=
 




 6*
[#](#langchain.llms.AzureOpenAI.max_retries "Permalink to this definition") 



 Maximum number of retries to make when generating.
 






*field*


 max_tokens
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.AzureOpenAI.max_tokens "Permalink to this definition") 



 The maximum number of tokens to generate in the completion.
-1 returns as many tokens as possible given the prompt and
the models maximal context size.
 






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
[#](#langchain.llms.AzureOpenAI.model_kwargs "Permalink to this definition") 



 Holds any model parameters valid for
 
 create
 
 call not explicitly specified.
 






*field*


 model_name
 

*:
 




 str*
*=
 




 'text-davinci-003'*
[#](#langchain.llms.AzureOpenAI.model_name "Permalink to this definition") 



 Model name to use.
 






*field*


 n
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.AzureOpenAI.n "Permalink to this definition") 



 How many completions to generate for each prompt.
 






*field*


 presence_penalty
 

*:
 




 float*
*=
 




 0*
[#](#langchain.llms.AzureOpenAI.presence_penalty "Permalink to this definition") 



 Penalizes repeated tokens.
 






*field*


 request_timeout
 

*:
 




 Optional
 


 [
 


 Union
 


 [
 


 float
 


 ,
 




 Tuple
 


 [
 


 float
 


 ,
 




 float
 


 ]
 



 ]
 



 ]*
*=
 




 None*
[#](#langchain.llms.AzureOpenAI.request_timeout "Permalink to this definition") 



 Timeout for requests to OpenAI completion API. Default is 600 seconds.
 






*field*


 streaming
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.AzureOpenAI.streaming "Permalink to this definition") 



 Whether to stream the results or not.
 






*field*


 temperature
 

*:
 




 float*
*=
 




 0.7*
[#](#langchain.llms.AzureOpenAI.temperature "Permalink to this definition") 



 What sampling temperature to use.
 






*field*


 top_p
 

*:
 




 float*
*=
 




 1*
[#](#langchain.llms.AzureOpenAI.top_p "Permalink to this definition") 



 Total probability mass of tokens to consider at each step.
 






*field*


 verbose
 

*:
 




 bool*
*[Optional]*
[#](#langchain.llms.AzureOpenAI.verbose "Permalink to this definition") 



 Whether to print out response text.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.AzureOpenAI.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AzureOpenAI.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AzureOpenAI.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.AzureOpenAI.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.AzureOpenAI.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 create_llm_result
 


 (
 
*choices
 



 :
 





 Any*
 ,
 *prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *token_usage
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 int
 


 ]*

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AzureOpenAI.create_llm_result "Permalink to this definition") 



 Create the LLMResult from the choices and prompts.
 








 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.AzureOpenAI.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AzureOpenAI.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.AzureOpenAI.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.AzureOpenAI.get_num_tokens "Permalink to this definition") 



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
 


[#](#langchain.llms.AzureOpenAI.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 get_sub_prompts
 


 (
 
*params
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
 ,
 *prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 



[#](#langchain.llms.AzureOpenAI.get_sub_prompts "Permalink to this definition") 



 Get the sub prompts for llm call.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.AzureOpenAI.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 max_tokens_for_prompt
 


 (
 
*prompt
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.AzureOpenAI.max_tokens_for_prompt "Permalink to this definition") 



 Calculate the maximum number of tokens possible to generate for a prompt.
 




 Parameters
 


**prompt** 
 – The prompt to pass into the model.
 




 Returns
 


 The maximum number of tokens to generate for a prompt.
 





 Example
 





```
max_tokens = openai.max_token_for_prompt("Tell me a joke.")

```









 modelname_to_contextsize
 


 (
 
*modelname
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.AzureOpenAI.modelname_to_contextsize "Permalink to this definition") 



 Calculate the maximum number of tokens possible to generate for a model.
 




 Parameters
 


**modelname** 
 – The modelname we want to know the context size for.
 




 Returns
 


 The maximum context size
 





 Example
 





```
max_tokens = openai.modelname_to_contextsize("text-davinci-003")

```









 prep_streaming_params
 


 (
 
*stop
 



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

 )
 


 →
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



[#](#langchain.llms.AzureOpenAI.prep_streaming_params "Permalink to this definition") 



 Prepare the params for streaming.
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.AzureOpenAI.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 








 stream
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 Generator
 


[#](#langchain.llms.AzureOpenAI.stream "Permalink to this definition") 



 Call OpenAI with streaming flag and return the resulting generator.
 



 BETA: this is a beta feature while we figure out the right abstraction.
Once that happens, this interface could change.
 




 Parameters
 

* **prompt** 
 – The prompts to pass into the model.
* **stop** 
 – Optional list of stop words to use when generating.




 Returns
 


 A generator representing the stream of tokens from OpenAI.
 





 Example
 





```
generator = openai.stream("Tell me a joke.")
for token in generator:
    yield token

```







*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.AzureOpenAI.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 Banana
 

[[source]](../../_modules/langchain/llms/bananadev#Banana)
[#](#langchain.llms.Banana "Permalink to this definition") 



 Wrapper around Banana large language models.
 



 To use, you should have the
 `banana-dev`
 python package installed,
and the environment variable
 `BANANA_API_KEY`
 set with your API key.
 



 Any parameters that are valid to be passed to the call can be passed
in, even if not explicitly saved on this class.
 



 Example
 




 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 model_key
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.llms.Banana.model_key "Permalink to this definition") 



 model endpoint to use
 






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
[#](#langchain.llms.Banana.model_kwargs "Permalink to this definition") 



 Holds any model parameters valid for
 
 create
 
 call not
explicitly specified.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.Banana.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Banana.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Banana.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Banana.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Banana.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.Banana.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Banana.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Banana.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.Banana.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.Banana.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.Banana.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.Banana.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.Banana.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 CerebriumAI
 

[[source]](../../_modules/langchain/llms/cerebriumai#CerebriumAI)
[#](#langchain.llms.CerebriumAI "Permalink to this definition") 



 Wrapper around CerebriumAI large language models.
 



 To use, you should have the
 `cerebrium`
 python package installed, and the
environment variable
 `CEREBRIUMAI_API_KEY`
 set with your API key.
 



 Any parameters that are valid to be passed to the call can be passed
in, even if not explicitly saved on this class.
 



 Example
 




 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 endpoint_url
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.llms.CerebriumAI.endpoint_url "Permalink to this definition") 



 model endpoint to use
 






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
[#](#langchain.llms.CerebriumAI.model_kwargs "Permalink to this definition") 



 Holds any model parameters valid for
 
 create
 
 call not
explicitly specified.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.CerebriumAI.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.CerebriumAI.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.CerebriumAI.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.CerebriumAI.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.CerebriumAI.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.CerebriumAI.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.CerebriumAI.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.CerebriumAI.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.CerebriumAI.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.CerebriumAI.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.CerebriumAI.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.CerebriumAI.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.CerebriumAI.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 Cohere
 

[[source]](../../_modules/langchain/llms/cohere#Cohere)
[#](#langchain.llms.Cohere "Permalink to this definition") 



 Wrapper around Cohere large language models.
 



 To use, you should have the
 `cohere`
 python package installed, and the
environment variable
 `COHERE_API_KEY`
 set with your API key, or pass
it as a named parameter to the constructor.
 



 Example
 





```
from langchain.llms import Cohere
cohere = Cohere(model="gptd-instruct-tft", cohere_api_key="my-api-key")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 frequency_penalty
 

*:
 




 float*
*=
 




 0.0*
[#](#langchain.llms.Cohere.frequency_penalty "Permalink to this definition") 



 Penalizes repeated tokens according to frequency. Between 0 and 1.
 






*field*


 k
 

*:
 




 int*
*=
 




 0*
[#](#langchain.llms.Cohere.k "Permalink to this definition") 



 Number of most likely tokens to consider at each step.
 






*field*


 max_tokens
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.Cohere.max_tokens "Permalink to this definition") 



 Denotes the number of tokens to predict per generation.
 






*field*


 model
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.Cohere.model "Permalink to this definition") 



 Model name to use.
 






*field*


 p
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.Cohere.p "Permalink to this definition") 



 Total probability mass of tokens to consider at each step.
 






*field*


 presence_penalty
 

*:
 




 float*
*=
 




 0.0*
[#](#langchain.llms.Cohere.presence_penalty "Permalink to this definition") 



 Penalizes repeated tokens. Between 0 and 1.
 






*field*


 temperature
 

*:
 




 float*
*=
 




 0.75*
[#](#langchain.llms.Cohere.temperature "Permalink to this definition") 



 A non-negative float that tunes the degree of randomness in generation.
 






*field*


 truncate
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.Cohere.truncate "Permalink to this definition") 



 Specify how the client handles inputs longer than the maximum token
length: Truncate from START, END or NONE
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.Cohere.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Cohere.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Cohere.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Cohere.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Cohere.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.Cohere.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Cohere.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Cohere.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.Cohere.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.Cohere.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.Cohere.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.Cohere.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.Cohere.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 DeepInfra
 

[[source]](../../_modules/langchain/llms/deepinfra#DeepInfra)
[#](#langchain.llms.DeepInfra "Permalink to this definition") 



 Wrapper around DeepInfra deployed models.
 



 To use, you should have the
 `requests`
 python package installed, and the
environment variable
 `DEEPINFRA_API_TOKEN`
 set with your API token, or pass
it as a named parameter to the constructor.
 



 Only supports
 
 text-generation
 
 and
 
 text2text-generation
 
 for now.
 



 Example
 





```
from langchain.llms import DeepInfra
di = DeepInfra(model_id="google/flan-t5-xl",
                    deepinfra_api_token="my-api-key")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.DeepInfra.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.DeepInfra.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.DeepInfra.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.DeepInfra.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.DeepInfra.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.DeepInfra.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.DeepInfra.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.DeepInfra.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.DeepInfra.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.DeepInfra.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.DeepInfra.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.DeepInfra.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.DeepInfra.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 ForefrontAI
 

[[source]](../../_modules/langchain/llms/forefrontai#ForefrontAI)
[#](#langchain.llms.ForefrontAI "Permalink to this definition") 



 Wrapper around ForefrontAI large language models.
 



 To use, you should have the environment variable
 `FOREFRONTAI_API_KEY`
 set with your API key.
 



 Example
 





```
from langchain.llms import ForefrontAI
forefrontai = ForefrontAI(endpoint_url="")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 base_url
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.ForefrontAI.base_url "Permalink to this definition") 



 Base url to use, if None decides based on model name.
 






*field*


 endpoint_url
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.llms.ForefrontAI.endpoint_url "Permalink to this definition") 



 Model name to use.
 






*field*


 length
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.ForefrontAI.length "Permalink to this definition") 



 The maximum number of tokens to generate in the completion.
 






*field*


 repetition_penalty
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.ForefrontAI.repetition_penalty "Permalink to this definition") 



 Penalizes repeated tokens according to frequency.
 






*field*


 temperature
 

*:
 




 float*
*=
 




 0.7*
[#](#langchain.llms.ForefrontAI.temperature "Permalink to this definition") 



 What sampling temperature to use.
 






*field*


 top_k
 

*:
 




 int*
*=
 




 40*
[#](#langchain.llms.ForefrontAI.top_k "Permalink to this definition") 



 The number of highest probability vocabulary tokens to
keep for top-k-filtering.
 






*field*


 top_p
 

*:
 




 float*
*=
 




 1.0*
[#](#langchain.llms.ForefrontAI.top_p "Permalink to this definition") 



 Total probability mass of tokens to consider at each step.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.ForefrontAI.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.ForefrontAI.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.ForefrontAI.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.ForefrontAI.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.ForefrontAI.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.ForefrontAI.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.ForefrontAI.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.ForefrontAI.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.ForefrontAI.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.ForefrontAI.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.ForefrontAI.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.ForefrontAI.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.ForefrontAI.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 GPT4All
 

[[source]](../../_modules/langchain/llms/gpt4all#GPT4All)
[#](#langchain.llms.GPT4All "Permalink to this definition") 



 Wrapper around GPT4All language models.
 



 To use, you should have the
 `pyllamacpp`
 python package installed, the
pre-trained model file, and the model’s config information.
 



 Example
 





```
from langchain.llms import GPT4All
model = GPT4All(model="./models/gpt4all-model.bin", n_ctx=512, n_threads=8)

# Simplest invocation
response = model("Once upon a time, ")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 echo
 

*:
 




 Optional
 


 [
 


 bool
 


 ]*
*=
 




 False*
[#](#langchain.llms.GPT4All.echo "Permalink to this definition") 



 Whether to echo the prompt.
 






*field*


 embedding
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.GPT4All.embedding "Permalink to this definition") 



 Use embedding mode only.
 






*field*


 f16_kv
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.GPT4All.f16_kv "Permalink to this definition") 



 Use half-precision for key/value cache.
 






*field*


 logits_all
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.GPT4All.logits_all "Permalink to this definition") 



 Return logits for all tokens, not just the last token.
 






*field*


 model
 

*:
 




 str*
*[Required]*
[#](#langchain.llms.GPT4All.model "Permalink to this definition") 



 Path to the pre-trained GPT4All model file.
 






*field*


 n_batch
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.GPT4All.n_batch "Permalink to this definition") 



 Batch size for prompt processing.
 






*field*


 n_ctx
 

*:
 




 int*
*=
 




 512*
[#](#langchain.llms.GPT4All.n_ctx "Permalink to this definition") 



 Token context window.
 






*field*


 n_parts
 

*:
 




 int*
*=
 




 -1*
[#](#langchain.llms.GPT4All.n_parts "Permalink to this definition") 



 Number of parts to split the model into.
If -1, the number of parts is automatically determined.
 






*field*


 n_predict
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 256*
[#](#langchain.llms.GPT4All.n_predict "Permalink to this definition") 



 The maximum number of tokens to generate.
 






*field*


 n_threads
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 4*
[#](#langchain.llms.GPT4All.n_threads "Permalink to this definition") 



 Number of threads to use.
 






*field*


 repeat_last_n
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 64*
[#](#langchain.llms.GPT4All.repeat_last_n "Permalink to this definition") 



 Last n tokens to penalize
 






*field*


 repeat_penalty
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 1.3*
[#](#langchain.llms.GPT4All.repeat_penalty "Permalink to this definition") 



 The penalty to apply to repeated tokens.
 






*field*


 seed
 

*:
 




 int*
*=
 




 0*
[#](#langchain.llms.GPT4All.seed "Permalink to this definition") 



 Seed. If -1, a random seed is used.
 






*field*


 stop
 

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
[#](#langchain.llms.GPT4All.stop "Permalink to this definition") 



 A list of strings to stop generation when encountered.
 






*field*


 streaming
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.GPT4All.streaming "Permalink to this definition") 



 Whether to stream the results or not.
 






*field*


 temp
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 0.8*
[#](#langchain.llms.GPT4All.temp "Permalink to this definition") 



 The temperature to use for sampling.
 






*field*


 top_k
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 40*
[#](#langchain.llms.GPT4All.top_k "Permalink to this definition") 



 The top-k value to use for sampling.
 






*field*


 top_p
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 0.95*
[#](#langchain.llms.GPT4All.top_p "Permalink to this definition") 



 The top-p value to use for sampling.
 






*field*


 use_mlock
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.GPT4All.use_mlock "Permalink to this definition") 



 Force system to keep model in RAM.
 






*field*


 vocab_only
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.GPT4All.vocab_only "Permalink to this definition") 



 Only load the vocabulary, no weights.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.GPT4All.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.GPT4All.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.GPT4All.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.GPT4All.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.GPT4All.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.GPT4All.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.GPT4All.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.GPT4All.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.GPT4All.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.GPT4All.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.GPT4All.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.GPT4All.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.GPT4All.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 GooseAI
 

[[source]](../../_modules/langchain/llms/gooseai#GooseAI)
[#](#langchain.llms.GooseAI "Permalink to this definition") 



 Wrapper around OpenAI large language models.
 



 To use, you should have the
 `openai`
 python package installed, and the
environment variable
 `GOOSEAI_API_KEY`
 set with your API key.
 



 Any parameters that are valid to be passed to the openai.create call can be passed
in, even if not explicitly saved on this class.
 



 Example
 




 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 frequency_penalty
 

*:
 




 float*
*=
 




 0*
[#](#langchain.llms.GooseAI.frequency_penalty "Permalink to this definition") 



 Penalizes repeated tokens according to frequency.
 






*field*


 logit_bias
 

*:
 




 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 float
 


 ]
 



 ]*
*[Optional]*
[#](#langchain.llms.GooseAI.logit_bias "Permalink to this definition") 



 Adjust the probability of specific tokens being generated.
 






*field*


 max_tokens
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.GooseAI.max_tokens "Permalink to this definition") 



 The maximum number of tokens to generate in the completion.
-1 returns as many tokens as possible given the prompt and
the models maximal context size.
 






*field*


 min_tokens
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.GooseAI.min_tokens "Permalink to this definition") 



 The minimum number of tokens to generate in the completion.
 






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
[#](#langchain.llms.GooseAI.model_kwargs "Permalink to this definition") 



 Holds any model parameters valid for
 
 create
 
 call not explicitly specified.
 






*field*


 model_name
 

*:
 




 str*
*=
 




 'gpt-neo-20b'*
[#](#langchain.llms.GooseAI.model_name "Permalink to this definition") 



 Model name to use
 






*field*


 n
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.GooseAI.n "Permalink to this definition") 



 How many completions to generate for each prompt.
 






*field*


 presence_penalty
 

*:
 




 float*
*=
 




 0*
[#](#langchain.llms.GooseAI.presence_penalty "Permalink to this definition") 



 Penalizes repeated tokens.
 






*field*


 temperature
 

*:
 




 float*
*=
 




 0.7*
[#](#langchain.llms.GooseAI.temperature "Permalink to this definition") 



 What sampling temperature to use
 






*field*


 top_p
 

*:
 




 float*
*=
 




 1*
[#](#langchain.llms.GooseAI.top_p "Permalink to this definition") 



 Total probability mass of tokens to consider at each step.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.GooseAI.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.GooseAI.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.GooseAI.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.GooseAI.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.GooseAI.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.GooseAI.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.GooseAI.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.GooseAI.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.GooseAI.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.GooseAI.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.GooseAI.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.GooseAI.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.GooseAI.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 HuggingFaceEndpoint
 

[[source]](../../_modules/langchain/llms/huggingface_endpoint#HuggingFaceEndpoint)
[#](#langchain.llms.HuggingFaceEndpoint "Permalink to this definition") 



 Wrapper around HuggingFaceHub Inference Endpoints.
 



 To use, you should have the
 `huggingface_hub`
 python package installed, and the
environment variable
 `HUGGINGFACEHUB_API_TOKEN`
 set with your API token, or pass
it as a named parameter to the constructor.
 



 Only supports
 
 text-generation
 
 and
 
 text2text-generation
 
 for now.
 



 Example
 





```
from langchain.llms import HuggingFaceEndpoint
endpoint_url = (
    "https://abcdefghijklmnop.us-east-1.aws.endpoints.huggingface.cloud"
)
hf = HuggingFaceEndpoint(
    endpoint_url=endpoint_url,
    huggingfacehub_api_token="my-api-key"
)

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 endpoint_url
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.llms.HuggingFaceEndpoint.endpoint_url "Permalink to this definition") 



 Endpoint URL to use.
 






*field*


 model_kwargs
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.llms.HuggingFaceEndpoint.model_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model.
 






*field*


 task
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.HuggingFaceEndpoint.task "Permalink to this definition") 



 Task to call the model with. Should be a task that returns
 
 generated_text
 
 .
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.HuggingFaceEndpoint.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFaceEndpoint.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFaceEndpoint.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.HuggingFaceEndpoint.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.HuggingFaceEndpoint.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.HuggingFaceEndpoint.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFaceEndpoint.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFaceEndpoint.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.HuggingFaceEndpoint.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.HuggingFaceEndpoint.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.HuggingFaceEndpoint.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.HuggingFaceEndpoint.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.HuggingFaceEndpoint.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 HuggingFaceHub
 

[[source]](../../_modules/langchain/llms/huggingface_hub#HuggingFaceHub)
[#](#langchain.llms.HuggingFaceHub "Permalink to this definition") 



 Wrapper around HuggingFaceHub models.
 



 To use, you should have the
 `huggingface_hub`
 python package installed, and the
environment variable
 `HUGGINGFACEHUB_API_TOKEN`
 set with your API token, or pass
it as a named parameter to the constructor.
 



 Only supports
 
 text-generation
 
 and
 
 text2text-generation
 
 for now.
 



 Example
 





```
from langchain.llms import HuggingFaceHub
hf = HuggingFaceHub(repo_id="gpt2", huggingfacehub_api_token="my-api-key")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 model_kwargs
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.llms.HuggingFaceHub.model_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model.
 






*field*


 repo_id
 

*:
 




 str*
*=
 




 'gpt2'*
[#](#langchain.llms.HuggingFaceHub.repo_id "Permalink to this definition") 



 Model name to use.
 






*field*


 task
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.HuggingFaceHub.task "Permalink to this definition") 



 Task to call the model with. Should be a task that returns
 
 generated_text
 
 .
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.HuggingFaceHub.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFaceHub.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFaceHub.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.HuggingFaceHub.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.HuggingFaceHub.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.HuggingFaceHub.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFaceHub.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFaceHub.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.HuggingFaceHub.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.HuggingFaceHub.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.HuggingFaceHub.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.HuggingFaceHub.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.HuggingFaceHub.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 HuggingFacePipeline
 

[[source]](../../_modules/langchain/llms/huggingface_pipeline#HuggingFacePipeline)
[#](#langchain.llms.HuggingFacePipeline "Permalink to this definition") 



 Wrapper around HuggingFace Pipeline API.
 



 To use, you should have the
 `transformers`
 python package installed.
 



 Only supports
 
 text-generation
 
 and
 
 text2text-generation
 
 for now.
 




 Example using from_model_id:
 




```
from langchain.llms import HuggingFacePipeline
hf = HuggingFacePipeline.from_model_id(
    model_id="gpt2", task="text-generation"
)

```





 Example passing pipeline in directly:
 




```
from langchain.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
pipe = pipeline(
    "text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10
)
hf = HuggingFacePipeline(pipeline=pipe)

```







 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 model_id
 

*:
 




 str*
*=
 




 'gpt2'*
[#](#langchain.llms.HuggingFacePipeline.model_id "Permalink to this definition") 



 Model name to use.
 






*field*


 model_kwargs
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.llms.HuggingFacePipeline.model_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.HuggingFacePipeline.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFacePipeline.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFacePipeline.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.HuggingFacePipeline.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.HuggingFacePipeline.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.HuggingFacePipeline.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 






*classmethod*


 from_model_id
 


 (
 
*model_id
 



 :
 





 str*
 ,
 *task
 



 :
 





 str*
 ,
 *device
 



 :
 





 int
 





 =
 





 -
 

 1*
 ,
 *model_kwargs
 



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
 


 langchain.llms.base.LLM
 


[[source]](../../_modules/langchain/llms/huggingface_pipeline#HuggingFacePipeline.from_model_id)
[#](#langchain.llms.HuggingFacePipeline.from_model_id "Permalink to this definition") 



 Construct the pipeline object from model_id and task.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFacePipeline.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.HuggingFacePipeline.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.HuggingFacePipeline.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.HuggingFacePipeline.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.HuggingFacePipeline.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.HuggingFacePipeline.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.HuggingFacePipeline.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 LlamaCpp
 

[[source]](../../_modules/langchain/llms/llamacpp#LlamaCpp)
[#](#langchain.llms.LlamaCpp "Permalink to this definition") 



 Wrapper around the llama.cpp model.
 



 To use, you should have the llama-cpp-python library installed, and provide the
path to the Llama model as a named parameter to the constructor.
Check out:
 [abetlen/llama-cpp-python](https://github.com/abetlen/llama-cpp-python) 




 Example
 





```
from langchain.llms import LlamaCppEmbeddings
llm = LlamaCppEmbeddings(model_path="/path/to/llama/model")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 echo
 

*:
 




 Optional
 


 [
 


 bool
 


 ]*
*=
 




 False*
[#](#langchain.llms.LlamaCpp.echo "Permalink to this definition") 



 Whether to echo the prompt.
 






*field*


 f16_kv
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.llms.LlamaCpp.f16_kv "Permalink to this definition") 



 Use half-precision for key/value cache.
 






*field*


 last_n_tokens_size
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 64*
[#](#langchain.llms.LlamaCpp.last_n_tokens_size "Permalink to this definition") 



 The number of tokens to look back when applying the repeat_penalty.
 






*field*


 logits_all
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.LlamaCpp.logits_all "Permalink to this definition") 



 Return logits for all tokens, not just the last token.
 






*field*


 logprobs
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.llms.LlamaCpp.logprobs "Permalink to this definition") 



 The number of logprobs to return. If None, no logprobs are returned.
 






*field*


 lora_base
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.LlamaCpp.lora_base "Permalink to this definition") 



 The path to the Llama LoRA base model.
 






*field*


 lora_path
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.LlamaCpp.lora_path "Permalink to this definition") 



 The path to the Llama LoRA. If None, no LoRa is loaded.
 






*field*


 max_tokens
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 256*
[#](#langchain.llms.LlamaCpp.max_tokens "Permalink to this definition") 



 The maximum number of tokens to generate.
 






*field*


 model_path
 

*:
 




 str*
*[Required]*
[#](#langchain.llms.LlamaCpp.model_path "Permalink to this definition") 



 The path to the Llama model file.
 






*field*


 n_batch
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 8*
[#](#langchain.llms.LlamaCpp.n_batch "Permalink to this definition") 



 Number of tokens to process in parallel.
Should be a number between 1 and n_ctx.
 






*field*


 n_ctx
 

*:
 




 int*
*=
 




 512*
[#](#langchain.llms.LlamaCpp.n_ctx "Permalink to this definition") 



 Token context window.
 






*field*


 n_parts
 

*:
 




 int*
*=
 




 -1*
[#](#langchain.llms.LlamaCpp.n_parts "Permalink to this definition") 



 Number of parts to split the model into.
If -1, the number of parts is automatically determined.
 






*field*


 n_threads
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.llms.LlamaCpp.n_threads "Permalink to this definition") 



 Number of threads to use.
If None, the number of threads is automatically determined.
 






*field*


 repeat_penalty
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 1.1*
[#](#langchain.llms.LlamaCpp.repeat_penalty "Permalink to this definition") 



 The penalty to apply to repeated tokens.
 






*field*


 seed
 

*:
 




 int*
*=
 




 -1*
[#](#langchain.llms.LlamaCpp.seed "Permalink to this definition") 



 Seed. If -1, a random seed is used.
 






*field*


 stop
 

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
[#](#langchain.llms.LlamaCpp.stop "Permalink to this definition") 



 A list of strings to stop generation when encountered.
 






*field*


 streaming
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.llms.LlamaCpp.streaming "Permalink to this definition") 



 Whether to stream the results, token by token.
 






*field*


 suffix
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.LlamaCpp.suffix "Permalink to this definition") 



 A suffix to append to the generated text. If None, no suffix is appended.
 






*field*


 temperature
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 0.8*
[#](#langchain.llms.LlamaCpp.temperature "Permalink to this definition") 



 The temperature to use for sampling.
 






*field*


 top_k
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 40*
[#](#langchain.llms.LlamaCpp.top_k "Permalink to this definition") 



 The top-k value to use for sampling.
 






*field*


 top_p
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 0.95*
[#](#langchain.llms.LlamaCpp.top_p "Permalink to this definition") 



 The top-p value to use for sampling.
 






*field*


 use_mlock
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.LlamaCpp.use_mlock "Permalink to this definition") 



 Force system to keep model in RAM.
 






*field*


 use_mmap
 

*:
 




 Optional
 


 [
 


 bool
 


 ]*
*=
 




 True*
[#](#langchain.llms.LlamaCpp.use_mmap "Permalink to this definition") 



 Whether to keep the model loaded in RAM
 






*field*


 vocab_only
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.LlamaCpp.vocab_only "Permalink to this definition") 



 Only load the vocabulary, no weights.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.LlamaCpp.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.LlamaCpp.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.LlamaCpp.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.LlamaCpp.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.LlamaCpp.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.LlamaCpp.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.LlamaCpp.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.LlamaCpp.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.LlamaCpp.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.LlamaCpp.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.LlamaCpp.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.LlamaCpp.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 








 stream
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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
 *run_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.manager.CallbackManagerForLLMRun
 


 ]
 






 =
 





 None*

 )
 


 →
 


 Generator
 


 [
 


 Dict
 


 ,
 




 None
 


 ,
 




 None
 


 ]
 



[[source]](../../_modules/langchain/llms/llamacpp#LlamaCpp.stream)
[#](#langchain.llms.LlamaCpp.stream "Permalink to this definition") 



 Yields results objects as they are generated in real time.
 



> 
> 
> 
>  BETA: this is a beta feature while we figure out the right abstraction:
> Once that happens, this interface could change.
>  
> 
> 
> 
>  It also calls the callback manager’s on_llm_new_token event with
> similar parameters to the OpenAI LLM class method of the same name.
>  
> 
> 
> 
> 
>  Args:
>  
> 
> 
>  prompt: The prompts to pass into the model.
> stop: Optional list of stop words to use when generating.
>  
> 
> 
> 
> 
>  Returns:
>  
> 
> 
>  A generator representing the stream of tokens being generated.
>  
> 
> 
> 
> 
>  Yields:
>  
> 
> 
>  A dictionary like objects containing a string token and metadata.
> See llama-cpp-python docs and below for more.
>  
> 
> 
> 
> 
>  Example:
>  
> 
> 
> 
> 
> ```
> from langchain.llms import LlamaCpp
> llm = LlamaCpp(
>     model_path="/path/to/local/model.bin",
>     temperature = 0.5
> )
> for chunk in llm.stream("Ask 'Hi, how are you?' like a pirate:'",
>         stop=["'","
> 
> ```
> 
> 
> 
> 
> 
> 
> 




 “]):
 


 result = chunk[“choices”][0]
print(result[“text”], end=’’, flush=True)
 








*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.LlamaCpp.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 Modal
 

[[source]](../../_modules/langchain/llms/modal#Modal)
[#](#langchain.llms.Modal "Permalink to this definition") 



 Wrapper around Modal large language models.
 



 To use, you should have the
 `modal-client`
 python package installed.
 



 Any parameters that are valid to be passed to the call can be passed
in, even if not explicitly saved on this class.
 



 Example
 




 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 endpoint_url
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.llms.Modal.endpoint_url "Permalink to this definition") 



 model endpoint to use
 






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
[#](#langchain.llms.Modal.model_kwargs "Permalink to this definition") 



 Holds any model parameters valid for
 
 create
 
 call not
explicitly specified.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.Modal.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Modal.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Modal.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Modal.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Modal.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.Modal.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Modal.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Modal.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.Modal.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.Modal.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.Modal.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.Modal.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.Modal.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 NLPCloud
 

[[source]](../../_modules/langchain/llms/nlpcloud#NLPCloud)
[#](#langchain.llms.NLPCloud "Permalink to this definition") 



 Wrapper around NLPCloud large language models.
 



 To use, you should have the
 `nlpcloud`
 python package installed, and the
environment variable
 `NLPCLOUD_API_KEY`
 set with your API key.
 



 Example
 





```
from langchain.llms import NLPCloud
nlpcloud = NLPCloud(model="gpt-neox-20b")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 bad_words
 

*:
 




 List
 


 [
 


 str
 


 ]*
*=
 




 []*
[#](#langchain.llms.NLPCloud.bad_words "Permalink to this definition") 



 List of tokens not allowed to be generated.
 






*field*


 do_sample
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.llms.NLPCloud.do_sample "Permalink to this definition") 



 Whether to use sampling (True) or greedy decoding.
 






*field*


 early_stopping
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.NLPCloud.early_stopping "Permalink to this definition") 



 Whether to stop beam search at num_beams sentences.
 






*field*


 length_no_input
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.llms.NLPCloud.length_no_input "Permalink to this definition") 



 Whether min_length and max_length should include the length of the input.
 






*field*


 length_penalty
 

*:
 




 float*
*=
 




 1.0*
[#](#langchain.llms.NLPCloud.length_penalty "Permalink to this definition") 



 Exponential penalty to the length.
 






*field*


 max_length
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.NLPCloud.max_length "Permalink to this definition") 



 The maximum number of tokens to generate in the completion.
 






*field*


 min_length
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.NLPCloud.min_length "Permalink to this definition") 



 The minimum number of tokens to generate in the completion.
 






*field*


 model_name
 

*:
 




 str*
*=
 




 'finetuned-gpt-neox-20b'*
[#](#langchain.llms.NLPCloud.model_name "Permalink to this definition") 



 Model name to use.
 






*field*


 num_beams
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.NLPCloud.num_beams "Permalink to this definition") 



 Number of beams for beam search.
 






*field*


 num_return_sequences
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.NLPCloud.num_return_sequences "Permalink to this definition") 



 How many completions to generate for each prompt.
 






*field*


 remove_end_sequence
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.llms.NLPCloud.remove_end_sequence "Permalink to this definition") 



 Whether or not to remove the end sequence token.
 






*field*


 remove_input
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.llms.NLPCloud.remove_input "Permalink to this definition") 



 Remove input text from API response
 






*field*


 repetition_penalty
 

*:
 




 float*
*=
 




 1.0*
[#](#langchain.llms.NLPCloud.repetition_penalty "Permalink to this definition") 



 Penalizes repeated tokens. 1.0 means no penalty.
 






*field*


 temperature
 

*:
 




 float*
*=
 




 0.7*
[#](#langchain.llms.NLPCloud.temperature "Permalink to this definition") 



 What sampling temperature to use.
 






*field*


 top_k
 

*:
 




 int*
*=
 




 50*
[#](#langchain.llms.NLPCloud.top_k "Permalink to this definition") 



 The number of highest probability tokens to keep for top-k filtering.
 






*field*


 top_p
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.NLPCloud.top_p "Permalink to this definition") 



 Total probability mass of tokens to consider at each step.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.NLPCloud.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.NLPCloud.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.NLPCloud.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.NLPCloud.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.NLPCloud.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.NLPCloud.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.NLPCloud.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.NLPCloud.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.NLPCloud.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.NLPCloud.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.NLPCloud.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.NLPCloud.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.NLPCloud.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 OpenAI
 

[[source]](../../_modules/langchain/llms/openai#OpenAI)
[#](#langchain.llms.OpenAI "Permalink to this definition") 



 Wrapper around OpenAI large language models.
 



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
from langchain.llms import OpenAI
openai = OpenAI(model_name="text-davinci-003")

```





 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 verbose
 

*:
 




 bool*
*[Optional]*
[#](#langchain.llms.OpenAI.verbose "Permalink to this definition") 



 Whether to print out response text.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.OpenAI.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.OpenAI.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.OpenAI.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.OpenAI.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.OpenAI.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 create_llm_result
 


 (
 
*choices
 



 :
 





 Any*
 ,
 *prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *token_usage
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 int
 


 ]*

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.OpenAI.create_llm_result "Permalink to this definition") 



 Create the LLMResult from the choices and prompts.
 








 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.OpenAI.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.OpenAI.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.OpenAI.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.OpenAI.get_num_tokens "Permalink to this definition") 



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
 


[#](#langchain.llms.OpenAI.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 get_sub_prompts
 


 (
 
*params
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
 ,
 *prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 



[#](#langchain.llms.OpenAI.get_sub_prompts "Permalink to this definition") 



 Get the sub prompts for llm call.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.OpenAI.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 max_tokens_for_prompt
 


 (
 
*prompt
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.OpenAI.max_tokens_for_prompt "Permalink to this definition") 



 Calculate the maximum number of tokens possible to generate for a prompt.
 




 Parameters
 


**prompt** 
 – The prompt to pass into the model.
 




 Returns
 


 The maximum number of tokens to generate for a prompt.
 





 Example
 





```
max_tokens = openai.max_token_for_prompt("Tell me a joke.")

```









 modelname_to_contextsize
 


 (
 
*modelname
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.OpenAI.modelname_to_contextsize "Permalink to this definition") 



 Calculate the maximum number of tokens possible to generate for a model.
 




 Parameters
 


**modelname** 
 – The modelname we want to know the context size for.
 




 Returns
 


 The maximum context size
 





 Example
 





```
max_tokens = openai.modelname_to_contextsize("text-davinci-003")

```









 prep_streaming_params
 


 (
 
*stop
 



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

 )
 


 →
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



[#](#langchain.llms.OpenAI.prep_streaming_params "Permalink to this definition") 



 Prepare the params for streaming.
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.OpenAI.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 








 stream
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 Generator
 


[#](#langchain.llms.OpenAI.stream "Permalink to this definition") 



 Call OpenAI with streaming flag and return the resulting generator.
 



 BETA: this is a beta feature while we figure out the right abstraction.
Once that happens, this interface could change.
 




 Parameters
 

* **prompt** 
 – The prompts to pass into the model.
* **stop** 
 – Optional list of stop words to use when generating.




 Returns
 


 A generator representing the stream of tokens from OpenAI.
 





 Example
 





```
generator = openai.stream("Tell me a joke.")
for token in generator:
    yield token

```







*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.OpenAI.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 OpenAIChat
 

[[source]](../../_modules/langchain/llms/openai#OpenAIChat)
[#](#langchain.llms.OpenAIChat "Permalink to this definition") 



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
from langchain.llms import OpenAIChat
openaichat = OpenAIChat(model_name="gpt-3.5-turbo")

```





 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 allowed_special
 

*:
 




 Union
 


 [
 


 Literal
 


 [
 



 'all'
 



 ]
 



 ,
 




 AbstractSet
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 {}*
[#](#langchain.llms.OpenAIChat.allowed_special "Permalink to this definition") 



 Set of special tokens that are allowed。
 






*field*


 disallowed_special
 

*:
 




 Union
 


 [
 


 Literal
 


 [
 



 'all'
 



 ]
 



 ,
 




 Collection
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 'all'*
[#](#langchain.llms.OpenAIChat.disallowed_special "Permalink to this definition") 



 Set of special tokens that are not allowed。
 






*field*


 max_retries
 

*:
 




 int*
*=
 




 6*
[#](#langchain.llms.OpenAIChat.max_retries "Permalink to this definition") 



 Maximum number of retries to make when generating.
 






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
[#](#langchain.llms.OpenAIChat.model_kwargs "Permalink to this definition") 



 Holds any model parameters valid for
 
 create
 
 call not explicitly specified.
 






*field*


 model_name
 

*:
 




 str*
*=
 




 'gpt-3.5-turbo'*
[#](#langchain.llms.OpenAIChat.model_name "Permalink to this definition") 



 Model name to use.
 






*field*


 prefix_messages
 

*:
 




 List*
*[Optional]*
[#](#langchain.llms.OpenAIChat.prefix_messages "Permalink to this definition") 



 Series of messages for Chat input.
 






*field*


 streaming
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.OpenAIChat.streaming "Permalink to this definition") 



 Whether to stream the results or not.
 






*field*


 verbose
 

*:
 




 bool*
*[Optional]*
[#](#langchain.llms.OpenAIChat.verbose "Permalink to this definition") 



 Whether to print out response text.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.OpenAIChat.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.OpenAIChat.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.OpenAIChat.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.OpenAIChat.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.OpenAIChat.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.OpenAIChat.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.OpenAIChat.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.OpenAIChat.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[[source]](../../_modules/langchain/llms/openai#OpenAIChat.get_num_tokens)
[#](#langchain.llms.OpenAIChat.get_num_tokens "Permalink to this definition") 



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
 


[#](#langchain.llms.OpenAIChat.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.OpenAIChat.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.OpenAIChat.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.OpenAIChat.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 Petals
 

[[source]](../../_modules/langchain/llms/petals#Petals)
[#](#langchain.llms.Petals "Permalink to this definition") 



 Wrapper around Petals Bloom models.
 



 To use, you should have the
 `petals`
 python package installed, and the
environment variable
 `HUGGINGFACE_API_KEY`
 set with your API key.
 



 Any parameters that are valid to be passed to the call can be passed
in, even if not explicitly saved on this class.
 



 Example
 




 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 client
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.llms.Petals.client "Permalink to this definition") 



 The client to use for the API calls.
 






*field*


 do_sample
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.llms.Petals.do_sample "Permalink to this definition") 



 Whether or not to use sampling; use greedy decoding otherwise.
 






*field*


 max_length
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.llms.Petals.max_length "Permalink to this definition") 



 The maximum length of the sequence to be generated.
 






*field*


 max_new_tokens
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.Petals.max_new_tokens "Permalink to this definition") 



 The maximum number of new tokens to generate in the completion.
 






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
[#](#langchain.llms.Petals.model_kwargs "Permalink to this definition") 



 Holds any model parameters valid for
 
 create
 
 call
not explicitly specified.
 






*field*


 model_name
 

*:
 




 str*
*=
 




 'bigscience/bloom-petals'*
[#](#langchain.llms.Petals.model_name "Permalink to this definition") 



 The model to use.
 






*field*


 temperature
 

*:
 




 float*
*=
 




 0.7*
[#](#langchain.llms.Petals.temperature "Permalink to this definition") 



 What sampling temperature to use
 






*field*


 tokenizer
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.llms.Petals.tokenizer "Permalink to this definition") 



 The tokenizer to use for the API calls.
 






*field*


 top_k
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.llms.Petals.top_k "Permalink to this definition") 



 The number of highest probability vocabulary tokens
to keep for top-k-filtering.
 






*field*


 top_p
 

*:
 




 float*
*=
 




 0.9*
[#](#langchain.llms.Petals.top_p "Permalink to this definition") 



 The cumulative probability for top-p sampling.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.Petals.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Petals.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Petals.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Petals.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Petals.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.Petals.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Petals.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Petals.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.Petals.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.Petals.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.Petals.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.Petals.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.Petals.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 PipelineAI
 

[[source]](../../_modules/langchain/llms/pipelineai#PipelineAI)
[#](#langchain.llms.PipelineAI "Permalink to this definition") 



 Wrapper around PipelineAI large language models.
 



 To use, you should have the
 `pipeline-ai`
 python package installed,
and the environment variable
 `PIPELINE_API_KEY`
 set with your API key.
 



 Any parameters that are valid to be passed to the call can be passed
in, even if not explicitly saved on this class.
 



 Example
 




 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 pipeline_key
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.llms.PipelineAI.pipeline_key "Permalink to this definition") 



 The id or tag of the target pipeline
 






*field*


 pipeline_kwargs
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
*[Optional]*
[#](#langchain.llms.PipelineAI.pipeline_kwargs "Permalink to this definition") 



 Holds any pipeline parameters valid for
 
 create
 
 call not
explicitly specified.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.PipelineAI.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PipelineAI.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PipelineAI.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.PipelineAI.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.PipelineAI.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.PipelineAI.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PipelineAI.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PipelineAI.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.PipelineAI.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.PipelineAI.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.PipelineAI.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.PipelineAI.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.PipelineAI.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 PredictionGuard
 

[[source]](../../_modules/langchain/llms/predictionguard#PredictionGuard)
[#](#langchain.llms.PredictionGuard "Permalink to this definition") 



 Wrapper around Prediction Guard large language models.
To use, you should have the
 `predictionguard`
 python package installed, and the
environment variable
 `PREDICTIONGUARD_TOKEN`
 set with your access token, or pass
it as a named parameter to the constructor.
.. rubric:: Example
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 max_tokens
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.PredictionGuard.max_tokens "Permalink to this definition") 



 Denotes the number of tokens to predict per generation.
 






*field*


 name
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 'default-text-gen'*
[#](#langchain.llms.PredictionGuard.name "Permalink to this definition") 



 Proxy name to use.
 






*field*


 temperature
 

*:
 




 float*
*=
 




 0.75*
[#](#langchain.llms.PredictionGuard.temperature "Permalink to this definition") 



 A non-negative float that tunes the degree of randomness in generation.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.PredictionGuard.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PredictionGuard.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PredictionGuard.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.PredictionGuard.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.PredictionGuard.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.PredictionGuard.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PredictionGuard.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PredictionGuard.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.PredictionGuard.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.PredictionGuard.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.PredictionGuard.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.PredictionGuard.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.PredictionGuard.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 PromptLayerOpenAI
 

[[source]](../../_modules/langchain/llms/promptlayer_openai#PromptLayerOpenAI)
[#](#langchain.llms.PromptLayerOpenAI "Permalink to this definition") 



 Wrapper around OpenAI large language models.
 



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
be passed here. The PromptLayerOpenAI LLM adds two optional
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
from langchain.llms import PromptLayerOpenAI
openai = PromptLayerOpenAI(model_name="text-davinci-003")

```





 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.PromptLayerOpenAI.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PromptLayerOpenAI.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PromptLayerOpenAI.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.PromptLayerOpenAI.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.PromptLayerOpenAI.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 create_llm_result
 


 (
 
*choices
 



 :
 





 Any*
 ,
 *prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *token_usage
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 int
 


 ]*

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PromptLayerOpenAI.create_llm_result "Permalink to this definition") 



 Create the LLMResult from the choices and prompts.
 








 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.PromptLayerOpenAI.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PromptLayerOpenAI.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PromptLayerOpenAI.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.PromptLayerOpenAI.get_num_tokens "Permalink to this definition") 



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
 


[#](#langchain.llms.PromptLayerOpenAI.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 get_sub_prompts
 


 (
 
*params
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
 ,
 *prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 



[#](#langchain.llms.PromptLayerOpenAI.get_sub_prompts "Permalink to this definition") 



 Get the sub prompts for llm call.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.PromptLayerOpenAI.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 max_tokens_for_prompt
 


 (
 
*prompt
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.PromptLayerOpenAI.max_tokens_for_prompt "Permalink to this definition") 



 Calculate the maximum number of tokens possible to generate for a prompt.
 




 Parameters
 


**prompt** 
 – The prompt to pass into the model.
 




 Returns
 


 The maximum number of tokens to generate for a prompt.
 





 Example
 





```
max_tokens = openai.max_token_for_prompt("Tell me a joke.")

```









 modelname_to_contextsize
 


 (
 
*modelname
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.PromptLayerOpenAI.modelname_to_contextsize "Permalink to this definition") 



 Calculate the maximum number of tokens possible to generate for a model.
 




 Parameters
 


**modelname** 
 – The modelname we want to know the context size for.
 




 Returns
 


 The maximum context size
 





 Example
 





```
max_tokens = openai.modelname_to_contextsize("text-davinci-003")

```









 prep_streaming_params
 


 (
 
*stop
 



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

 )
 


 →
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



[#](#langchain.llms.PromptLayerOpenAI.prep_streaming_params "Permalink to this definition") 



 Prepare the params for streaming.
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.PromptLayerOpenAI.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 








 stream
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 Generator
 


[#](#langchain.llms.PromptLayerOpenAI.stream "Permalink to this definition") 



 Call OpenAI with streaming flag and return the resulting generator.
 



 BETA: this is a beta feature while we figure out the right abstraction.
Once that happens, this interface could change.
 




 Parameters
 

* **prompt** 
 – The prompts to pass into the model.
* **stop** 
 – Optional list of stop words to use when generating.




 Returns
 


 A generator representing the stream of tokens from OpenAI.
 





 Example
 





```
generator = openai.stream("Tell me a joke.")
for token in generator:
    yield token

```







*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.PromptLayerOpenAI.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 PromptLayerOpenAIChat
 

[[source]](../../_modules/langchain/llms/promptlayer_openai#PromptLayerOpenAIChat)
[#](#langchain.llms.PromptLayerOpenAIChat "Permalink to this definition") 



 Wrapper around OpenAI large language models.
 



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
 



 All parameters that can be passed to the OpenAIChat LLM can also
be passed here. The PromptLayerOpenAIChat adds two optional
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
from langchain.llms import PromptLayerOpenAIChat
openaichat = PromptLayerOpenAIChat(model_name="gpt-3.5-turbo")

```





 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 allowed_special
 

*:
 




 Union
 


 [
 


 Literal
 


 [
 



 'all'
 



 ]
 



 ,
 




 AbstractSet
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 {}*
[#](#langchain.llms.PromptLayerOpenAIChat.allowed_special "Permalink to this definition") 



 Set of special tokens that are allowed。
 






*field*


 disallowed_special
 

*:
 




 Union
 


 [
 


 Literal
 


 [
 



 'all'
 



 ]
 



 ,
 




 Collection
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 'all'*
[#](#langchain.llms.PromptLayerOpenAIChat.disallowed_special "Permalink to this definition") 



 Set of special tokens that are not allowed。
 






*field*


 max_retries
 

*:
 




 int*
*=
 




 6*
[#](#langchain.llms.PromptLayerOpenAIChat.max_retries "Permalink to this definition") 



 Maximum number of retries to make when generating.
 






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
[#](#langchain.llms.PromptLayerOpenAIChat.model_kwargs "Permalink to this definition") 



 Holds any model parameters valid for
 
 create
 
 call not explicitly specified.
 






*field*


 model_name
 

*:
 




 str*
*=
 




 'gpt-3.5-turbo'*
[#](#langchain.llms.PromptLayerOpenAIChat.model_name "Permalink to this definition") 



 Model name to use.
 






*field*


 prefix_messages
 

*:
 




 List*
*[Optional]*
[#](#langchain.llms.PromptLayerOpenAIChat.prefix_messages "Permalink to this definition") 



 Series of messages for Chat input.
 






*field*


 streaming
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.PromptLayerOpenAIChat.streaming "Permalink to this definition") 



 Whether to stream the results or not.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.PromptLayerOpenAIChat.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PromptLayerOpenAIChat.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PromptLayerOpenAIChat.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.PromptLayerOpenAIChat.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.PromptLayerOpenAIChat.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.PromptLayerOpenAIChat.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PromptLayerOpenAIChat.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.PromptLayerOpenAIChat.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.PromptLayerOpenAIChat.get_num_tokens "Permalink to this definition") 



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
 


[#](#langchain.llms.PromptLayerOpenAIChat.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.PromptLayerOpenAIChat.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.PromptLayerOpenAIChat.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.PromptLayerOpenAIChat.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 RWKV
 

[[source]](../../_modules/langchain/llms/rwkv#RWKV)
[#](#langchain.llms.RWKV "Permalink to this definition") 



 Wrapper around RWKV language models.
 



 To use, you should have the
 `rwkv`
 python package installed, the
pre-trained model file, and the model’s config information.
 



 Example
 





```
from langchain.llms import RWKV
model = RWKV(model="./models/rwkv-3b-fp16.bin", strategy="cpu fp32")

# Simplest invocation
response = model("Once upon a time, ")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 CHUNK_LEN
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.RWKV.CHUNK_LEN "Permalink to this definition") 



 Batch size for prompt processing.
 






*field*


 max_tokens_per_generation
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.RWKV.max_tokens_per_generation "Permalink to this definition") 



 Maximum number of tokens to generate.
 






*field*


 model
 

*:
 




 str*
*[Required]*
[#](#langchain.llms.RWKV.model "Permalink to this definition") 



 Path to the pre-trained RWKV model file.
 






*field*


 penalty_alpha_frequency
 

*:
 




 float*
*=
 




 0.4*
[#](#langchain.llms.RWKV.penalty_alpha_frequency "Permalink to this definition") 



 Positive values penalize new tokens based on their existing frequency
in the text so far, decreasing the model’s likelihood to repeat the same
line verbatim..
 






*field*


 penalty_alpha_presence
 

*:
 




 float*
*=
 




 0.4*
[#](#langchain.llms.RWKV.penalty_alpha_presence "Permalink to this definition") 



 Positive values penalize new tokens based on whether they appear
in the text so far, increasing the model’s likelihood to talk about
new topics..
 






*field*


 rwkv_verbose
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.llms.RWKV.rwkv_verbose "Permalink to this definition") 



 Print debug information.
 






*field*


 strategy
 

*:
 




 str*
*=
 




 'cpu
 

 fp32'*
[#](#langchain.llms.RWKV.strategy "Permalink to this definition") 



 Token context window.
 






*field*


 temperature
 

*:
 




 float*
*=
 




 1.0*
[#](#langchain.llms.RWKV.temperature "Permalink to this definition") 



 The temperature to use for sampling.
 






*field*


 tokens_path
 

*:
 




 str*
*[Required]*
[#](#langchain.llms.RWKV.tokens_path "Permalink to this definition") 



 Path to the RWKV tokens file.
 






*field*


 top_p
 

*:
 




 float*
*=
 




 0.5*
[#](#langchain.llms.RWKV.top_p "Permalink to this definition") 



 The top-p value to use for sampling.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.RWKV.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.RWKV.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.RWKV.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.RWKV.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.RWKV.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.RWKV.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.RWKV.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.RWKV.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.RWKV.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.RWKV.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.RWKV.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.RWKV.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.RWKV.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 Replicate
 

[[source]](../../_modules/langchain/llms/replicate#Replicate)
[#](#langchain.llms.Replicate "Permalink to this definition") 



 Wrapper around Replicate models.
 



 To use, you should have the
 `replicate`
 python package installed,
and the environment variable
 `REPLICATE_API_TOKEN`
 set with your API token.
You can find your token here:
 <https://replicate.com/account>




 The model param is required, but any other model parameters can also
be passed in with the format input={model_param: value, …}
 



 Example
 




 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.Replicate.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Replicate.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Replicate.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Replicate.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Replicate.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.Replicate.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Replicate.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Replicate.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.Replicate.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.Replicate.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.Replicate.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.Replicate.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.Replicate.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 SagemakerEndpoint
 

[[source]](../../_modules/langchain/llms/sagemaker_endpoint#SagemakerEndpoint)
[#](#langchain.llms.SagemakerEndpoint "Permalink to this definition") 



 Wrapper around custom Sagemaker Inference Endpoints.
 



 To use, you must supply the endpoint name from your deployed
Sagemaker model & the region where it is deployed.
 



 To authenticate, the AWS client uses the following methods to
automatically load credentials:
 <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials>




 If a specific credential profile should be used, you must pass
the name of the profile from the ~/.aws/credentials file that is to be used.
 



 Make sure the credentials / roles used have the required policies to
access the Sagemaker endpoint.
See:
 <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies>





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 content_handler
 

*:
 




 langchain.llms.sagemaker_endpoint.LLMContentHandler*
*[Required]*
[#](#langchain.llms.SagemakerEndpoint.content_handler "Permalink to this definition") 



 The content handler class that provides an input and
output transform functions to handle formats between LLM
and the endpoint.
 






*field*


 credentials_profile_name
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.SagemakerEndpoint.credentials_profile_name "Permalink to this definition") 



 The name of the profile in the ~/.aws/credentials or ~/.aws/config files, which
has either access keys or role information specified.
If not specified, the default credential profile or, if on an EC2 instance,
credentials from IMDS will be used.
See:
 <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials>







*field*


 endpoint_kwargs
 

*:
 




 Optional
 


 [
 


 Dict
 


 ]*
*=
 




 None*
[#](#langchain.llms.SagemakerEndpoint.endpoint_kwargs "Permalink to this definition") 



 Optional attributes passed to the invoke_endpoint
function. See
 [`boto3`_](#id1)
 . docs for more info.
.. _boto3: <
 <https://boto3.amazonaws.com/v1/documentation/api/latest/index>
 >
 






*field*


 endpoint_name
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.llms.SagemakerEndpoint.endpoint_name "Permalink to this definition") 



 The name of the endpoint from the deployed Sagemaker model.
Must be unique within an AWS Region.
 






*field*


 model_kwargs
 

*:
 




 Optional
 


 [
 


 Dict
 


 ]*
*=
 




 None*
[#](#langchain.llms.SagemakerEndpoint.model_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model.
 






*field*


 region_name
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.llms.SagemakerEndpoint.region_name "Permalink to this definition") 



 The aws region where the Sagemaker model is deployed, eg.
 
 us-west-2
 
 .
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.SagemakerEndpoint.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SagemakerEndpoint.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SagemakerEndpoint.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.SagemakerEndpoint.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.SagemakerEndpoint.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.SagemakerEndpoint.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SagemakerEndpoint.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SagemakerEndpoint.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.SagemakerEndpoint.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.SagemakerEndpoint.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.SagemakerEndpoint.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.SagemakerEndpoint.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.SagemakerEndpoint.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 SelfHostedHuggingFaceLLM
 

[[source]](../../_modules/langchain/llms/self_hosted_hugging_face#SelfHostedHuggingFaceLLM)
[#](#langchain.llms.SelfHostedHuggingFaceLLM "Permalink to this definition") 



 Wrapper around HuggingFace Pipeline API to run on self-hosted remote hardware.
 



 Supported hardware includes auto-launched instances on AWS, GCP, Azure,
and Lambda, as well as servers specified
by IP address and SSH credentials (such as on-prem, or another cloud
like Paperspace, Coreweave, etc.).
 



 To use, you should have the
 `runhouse`
 python package installed.
 



 Only supports
 
 text-generation
 
 and
 
 text2text-generation
 
 for now.
 




 Example using from_model_id:
 




```
from langchain.llms import SelfHostedHuggingFaceLLM
import runhouse as rh
gpu = rh.cluster(name="rh-a10x", instance_type="A100:1")
hf = SelfHostedHuggingFaceLLM(
    model_id="google/flan-t5-large", task="text2text-generation",
    hardware=gpu
)

```





 Example passing fn that generates a pipeline (bc the pipeline is not serializable):
 




```
from langchain.llms import SelfHostedHuggingFaceLLM
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import runhouse as rh

def get_pipeline():
    model_id = "gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    pipe = pipeline(
        "text-generation", model=model, tokenizer=tokenizer
    )
    return pipe
hf = SelfHostedHuggingFaceLLM(
    model_load_fn=get_pipeline, model_id="gpt2", hardware=gpu)

```







 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 device
 

*:
 




 int*
*=
 




 0*
[#](#langchain.llms.SelfHostedHuggingFaceLLM.device "Permalink to this definition") 



 Device to use for inference. -1 for CPU, 0 for GPU, 1 for second GPU, etc.
 






*field*


 hardware
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.llms.SelfHostedHuggingFaceLLM.hardware "Permalink to this definition") 



 Remote hardware to send the inference function to.
 






*field*


 inference_fn
 

*:
 




 Callable*
*=
 




 <function
 

 _generate_text>*
[#](#langchain.llms.SelfHostedHuggingFaceLLM.inference_fn "Permalink to this definition") 



 Inference function to send to the remote hardware.
 






*field*


 load_fn_kwargs
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.llms.SelfHostedHuggingFaceLLM.load_fn_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model load function.
 






*field*


 model_id
 

*:
 




 str*
*=
 




 'gpt2'*
[#](#langchain.llms.SelfHostedHuggingFaceLLM.model_id "Permalink to this definition") 



 Hugging Face model_id to load the model.
 






*field*


 model_kwargs
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.llms.SelfHostedHuggingFaceLLM.model_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model.
 






*field*


 model_load_fn
 

*:
 




 Callable*
*=
 




 <function
 

 _load_transformer>*
[#](#langchain.llms.SelfHostedHuggingFaceLLM.model_load_fn "Permalink to this definition") 



 Function to load the model remotely on the server.
 






*field*


 model_reqs
 

*:
 




 List
 


 [
 


 str
 


 ]*
*=
 




 ['./',
 

 'transformers',
 

 'torch']*
[#](#langchain.llms.SelfHostedHuggingFaceLLM.model_reqs "Permalink to this definition") 



 Requirements to install on hardware to inference the model.
 






*field*


 task
 

*:
 




 str*
*=
 




 'text-generation'*
[#](#langchain.llms.SelfHostedHuggingFaceLLM.task "Permalink to this definition") 



 Hugging Face task (either “text-generation” or “text2text-generation”).
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 






*classmethod*


 from_pipeline
 


 (
 
*pipeline
 



 :
 





 Any*
 ,
 *hardware
 



 :
 





 Any*
 ,
 *model_reqs
 



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
 *device
 



 :
 





 int
 





 =
 





 0*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.llms.base.LLM
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.from_pipeline "Permalink to this definition") 



 Init the SelfHostedPipeline from a pipeline object or string.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.SelfHostedHuggingFaceLLM.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 SelfHostedPipeline
 

[[source]](../../_modules/langchain/llms/self_hosted#SelfHostedPipeline)
[#](#langchain.llms.SelfHostedPipeline "Permalink to this definition") 



 Run model inference on self-hosted remote hardware.
 



 Supported hardware includes auto-launched instances on AWS, GCP, Azure,
and Lambda, as well as servers specified
by IP address and SSH credentials (such as on-prem, or another
cloud like Paperspace, Coreweave, etc.).
 



 To use, you should have the
 `runhouse`
 python package installed.
 




 Example for custom pipeline and inference functions:
 




```
from langchain.llms import SelfHostedPipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import runhouse as rh

def load_pipeline():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    return pipeline(
        "text-generation", model=model, tokenizer=tokenizer,
        max_new_tokens=10
    )
def inference_fn(pipeline, prompt, stop = None):
    return pipeline(prompt)[0]["generated_text"]

gpu = rh.cluster(name="rh-a10x", instance_type="A100:1")
llm = SelfHostedPipeline(
    model_load_fn=load_pipeline,
    hardware=gpu,
    model_reqs=model_reqs, inference_fn=inference_fn
)

```





 Example for <2GB model (can be serialized and sent directly to the server):
 




```
from langchain.llms import SelfHostedPipeline
import runhouse as rh
gpu = rh.cluster(name="rh-a10x", instance_type="A100:1")
my_model = ...
llm = SelfHostedPipeline.from_pipeline(
    pipeline=my_model,
    hardware=gpu,
    model_reqs=["./", "torch", "transformers"],
)

```





 Example passing model path for larger models:
 




```
from langchain.llms import SelfHostedPipeline
import runhouse as rh
import pickle
from transformers import pipeline

generator = pipeline(model="gpt2")
rh.blob(pickle.dumps(generator), path="models/pipeline.pkl"
    ).save().to(gpu, path="models")
llm = SelfHostedPipeline.from_pipeline(
    pipeline="models/pipeline.pkl",
    hardware=gpu,
    model_reqs=["./", "torch", "transformers"],
)

```







 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 hardware
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.llms.SelfHostedPipeline.hardware "Permalink to this definition") 



 Remote hardware to send the inference function to.
 






*field*


 inference_fn
 

*:
 




 Callable*
*=
 




 <function
 

 _generate_text>*
[#](#langchain.llms.SelfHostedPipeline.inference_fn "Permalink to this definition") 



 Inference function to send to the remote hardware.
 






*field*


 load_fn_kwargs
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.llms.SelfHostedPipeline.load_fn_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model load function.
 






*field*


 model_load_fn
 

*:
 




 Callable*
*[Required]*
[#](#langchain.llms.SelfHostedPipeline.model_load_fn "Permalink to this definition") 



 Function to load the model remotely on the server.
 






*field*


 model_reqs
 

*:
 




 List
 


 [
 


 str
 


 ]*
*=
 




 ['./',
 

 'torch']*
[#](#langchain.llms.SelfHostedPipeline.model_reqs "Permalink to this definition") 



 Requirements to install on hardware to inference the model.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.SelfHostedPipeline.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SelfHostedPipeline.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SelfHostedPipeline.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.SelfHostedPipeline.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.SelfHostedPipeline.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.SelfHostedPipeline.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 






*classmethod*


 from_pipeline
 


 (
 
*pipeline
 



 :
 





 Any*
 ,
 *hardware
 



 :
 





 Any*
 ,
 *model_reqs
 



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
 *device
 



 :
 





 int
 





 =
 





 0*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.llms.base.LLM
 


[[source]](../../_modules/langchain/llms/self_hosted#SelfHostedPipeline.from_pipeline)
[#](#langchain.llms.SelfHostedPipeline.from_pipeline "Permalink to this definition") 



 Init the SelfHostedPipeline from a pipeline object or string.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SelfHostedPipeline.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.SelfHostedPipeline.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.SelfHostedPipeline.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.SelfHostedPipeline.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.SelfHostedPipeline.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.SelfHostedPipeline.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.SelfHostedPipeline.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 StochasticAI
 

[[source]](../../_modules/langchain/llms/stochasticai#StochasticAI)
[#](#langchain.llms.StochasticAI "Permalink to this definition") 



 Wrapper around StochasticAI large language models.
 



 To use, you should have the environment variable
 `STOCHASTICAI_API_KEY`
 set with your API key.
 



 Example
 





```
from langchain.llms import StochasticAI
stochasticai = StochasticAI(api_url="")

```





 Validators
 

* `build_extra`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 api_url
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.llms.StochasticAI.api_url "Permalink to this definition") 



 Model name to use.
 






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
[#](#langchain.llms.StochasticAI.model_kwargs "Permalink to this definition") 



 Holds any model parameters valid for
 
 create
 
 call not
explicitly specified.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.StochasticAI.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.StochasticAI.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.StochasticAI.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.StochasticAI.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.StochasticAI.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.StochasticAI.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.StochasticAI.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.StochasticAI.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.StochasticAI.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.StochasticAI.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.StochasticAI.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.StochasticAI.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.StochasticAI.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








*pydantic
 

 model*


 langchain.llms.
 



 Writer
 

[[source]](../../_modules/langchain/llms/writer#Writer)
[#](#langchain.llms.Writer "Permalink to this definition") 



 Wrapper around Writer large language models.
 



 To use, you should have the environment variable
 `WRITER_API_KEY`
 set with your API key.
 



 Example
 





```
from langchain import Writer
writer = Writer(model_id="palmyra-base")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 base_url
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.llms.Writer.base_url "Permalink to this definition") 



 Base url to use, if None decides based on model name.
 






*field*


 beam_search_diversity_rate
 

*:
 




 float*
*=
 




 1.0*
[#](#langchain.llms.Writer.beam_search_diversity_rate "Permalink to this definition") 



 Only applies to beam search, i.e. when the beam width is >1.
A higher value encourages beam search to return a more diverse
set of candidates
 






*field*


 beam_width
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.llms.Writer.beam_width "Permalink to this definition") 



 The number of concurrent candidates to keep track of during
beam search
 






*field*


 length
 

*:
 




 int*
*=
 




 256*
[#](#langchain.llms.Writer.length "Permalink to this definition") 



 The maximum number of tokens to generate in the completion.
 






*field*


 length_pentaly
 

*:
 




 float*
*=
 




 1.0*
[#](#langchain.llms.Writer.length_pentaly "Permalink to this definition") 



 Only applies to beam search, i.e. when the beam width is >1.
Larger values penalize long candidates more heavily, thus preferring
shorter candidates
 






*field*


 logprobs
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.llms.Writer.logprobs "Permalink to this definition") 



 Whether to return log probabilities.
 






*field*


 model_id
 

*:
 




 str*
*=
 




 'palmyra-base'*
[#](#langchain.llms.Writer.model_id "Permalink to this definition") 



 Model name to use.
 






*field*


 random_seed
 

*:
 




 int*
*=
 




 0*
[#](#langchain.llms.Writer.random_seed "Permalink to this definition") 



 The model generates random results.
Changing the random seed alone will produce a different response
with similar characteristics. It is possible to reproduce results
by fixing the random seed (assuming all other hyperparameters
are also fixed)
 






*field*


 repetition_penalty
 

*:
 




 float*
*=
 




 1.0*
[#](#langchain.llms.Writer.repetition_penalty "Permalink to this definition") 



 Penalizes repeated tokens according to frequency.
 






*field*


 stop
 

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
[#](#langchain.llms.Writer.stop "Permalink to this definition") 



 Sequences when completion generation will stop
 






*field*


 temperature
 

*:
 




 float*
*=
 




 1.0*
[#](#langchain.llms.Writer.temperature "Permalink to this definition") 



 What sampling temperature to use.
 






*field*


 tokens_to_generate
 

*:
 




 int*
*=
 




 24*
[#](#langchain.llms.Writer.tokens_to_generate "Permalink to this definition") 



 Max number of tokens to generate.
 






*field*


 top_k
 

*:
 




 int*
*=
 




 1*
[#](#langchain.llms.Writer.top_k "Permalink to this definition") 



 The number of highest probability vocabulary tokens to
keep for top-k-filtering.
 






*field*


 top_p
 

*:
 




 float*
*=
 




 1.0*
[#](#langchain.llms.Writer.top_p "Permalink to this definition") 



 Total probability mass of tokens to consider at each step.
 








 __call__
 


 (
 
*prompt
 



 :
 





 str*
 ,
 *stop
 



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

 )
 


 →
 


 str
 


[#](#langchain.llms.Writer.__call__ "Permalink to this definition") 



 Check Cache and run the LLM on the given prompt and input.
 






*async*


 agenerate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Writer.agenerate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 






*async*


 agenerate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Writer.agenerate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 






*classmethod*


 construct
 


 (
 
*_fields_set
 



 :
 





 Optional
 


 [
 


 SetStr
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 values
 



 :
 





 Any*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Writer.construct "Permalink to this definition") 



 Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if
 
 Config.extra = ‘allow’
 
 was set since it adds all passed values
 








 copy
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *update
 



 :
 





 Optional
 


 [
 


 DictStrAny
 


 ]
 






 =
 





 None*
 ,
 *deep
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 Model
 


[#](#langchain.llms.Writer.copy "Permalink to this definition") 



 Duplicate a model, optionally choose which fields to include, exclude and change.
 




 Parameters
 

* **include** 
 – fields to include in new model
* **exclude** 
 – fields to exclude from new model, as with values this takes precedence over include
* **update** 
 – values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data
* **deep** 
 – set to
 
 True
 
 to make a deep copy of the model




 Returns
 


 new model instance
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[#](#langchain.llms.Writer.dict "Permalink to this definition") 



 Return a dictionary of the LLM.
 








 generate
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Writer.generate "Permalink to this definition") 



 Run the LLM on the given prompt and input.
 








 generate_prompt
 


 (
 
*prompts
 



 :
 





 List
 


 [
 


 langchain.schema.PromptValue
 


 ]*
 ,
 *stop
 



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

 )
 


 →
 


 langchain.schema.LLMResult
 


[#](#langchain.llms.Writer.generate_prompt "Permalink to this definition") 



 Take in a list of prompt values and return an LLMResult.
 








 get_num_tokens
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 int
 


[#](#langchain.llms.Writer.get_num_tokens "Permalink to this definition") 



 Get the number of tokens present in the text.
 








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
 


[#](#langchain.llms.Writer.get_num_tokens_from_messages "Permalink to this definition") 



 Get the number of tokens in the message.
 








 json
 


 (
 
*\**
 ,
 *include
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *exclude
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 AbstractSetIntStr
 


 ,
 




 MappingIntStrAny
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *by_alias
 



 :
 





 bool
 





 =
 





 False*
 ,
 *skip_defaults
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *exclude_unset
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_defaults
 



 :
 





 bool
 





 =
 





 False*
 ,
 *exclude_none
 



 :
 





 bool
 





 =
 





 False*
 ,
 *encoder
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 Any
 


 ]
 



 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *models_as_dict
 



 :
 





 bool
 





 =
 





 True*
 ,
 *\*\*
 



 dumps_kwargs
 



 :
 





 Any*

 )
 


 →
 


 unicode
 


[#](#langchain.llms.Writer.json "Permalink to this definition") 



 Generate a JSON representation of the model,
 
 include
 
 and
 
 exclude
 
 arguments as per
 
 dict()
 
 .
 




 encoder
 
 is an optional function to supply as
 
 default
 
 to json.dumps(), other arguments as per
 
 json.dumps()
 
 .
 








 save
 


 (
 
*file_path
 



 :
 





 Union
 


 [
 


 pathlib.Path
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[#](#langchain.llms.Writer.save "Permalink to this definition") 



 Save the LLM.
 




 Parameters
 


**file_path** 
 – Path to file to save the LLM to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  llm.save(file_path=”path/llm.yaml”)
>  
> 
> 
> 
> 






*classmethod*


 update_forward_refs
 


 (
 
*\*\*
 



 localns
 



 :
 





 Any*

 )
 


 →
 


 None
 


[#](#langchain.llms.Writer.update_forward_refs "Permalink to this definition") 



 Try to update ForwardRefs on fields based on this Model, globalns and localns.
 








