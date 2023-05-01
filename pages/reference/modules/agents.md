




 Agents
 [#](#module-langchain.agents "Permalink to this headline")
====================================================================



 Interface for agents.
 




*pydantic
 

 model*


 langchain.agents.
 



 Agent
 

[[source]](../../_modules/langchain/agents/agent#Agent)
[#](#langchain.agents.Agent "Permalink to this definition") 



 Class responsible for calling the language model and deciding the action.
 



 This is driven by an LLMChain. The prompt in the LLMChain MUST include
a variable called “agent_scratchpad” where the agent can put its
intermediary work.
 




*field*


 allowed_tools
 

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
[#](#langchain.agents.Agent.allowed_tools "Permalink to this definition") 






*field*


 llm_chain
 

*:
 



[langchain.chains.llm.LLMChain](chains#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
*[Required]*
[#](#langchain.agents.Agent.llm_chain "Permalink to this definition") 






*field*


 output_parser
 

*:
 



[langchain.agents.agent.AgentOutputParser](#langchain.agents.AgentOutputParser "langchain.agents.agent.AgentOutputParser")*
*[Required]*
[#](#langchain.agents.Agent.output_parser "Permalink to this definition") 






*async*


 aplan
 


 (
 
*intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
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
 


 Union
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 langchain.schema.AgentFinish
 


 ]
 



[[source]](../../_modules/langchain/agents/agent#Agent.aplan)
[#](#langchain.agents.Agent.aplan "Permalink to this definition") 



 Given input, decided what to do.
 




 Parameters
 

* **intermediate_steps** 
 – Steps the LLM has taken to date,
along with observations
* **callbacks** 
 – Callbacks to run.
* **\*\*kwargs** 
 – User inputs.




 Returns
 


 Action specifying what tool to use.
 








*abstract
 



 classmethod*


 create_prompt
 


 (
 
*tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*

 )
 


 →
 

[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")


[[source]](../../_modules/langchain/agents/agent#Agent.create_prompt)
[#](#langchain.agents.Agent.create_prompt "Permalink to this definition") 



 Create a prompt for this class.
 






*classmethod*


 from_llm_and_tools
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
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
 *output_parser
 



 :
 





 Optional
 


 [
 

[langchain.agents.agent.AgentOutputParser](#langchain.agents.AgentOutputParser "langchain.agents.agent.AgentOutputParser")


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
 

[langchain.agents.agent.Agent](#langchain.agents.Agent "langchain.agents.agent.Agent")


[[source]](../../_modules/langchain/agents/agent#Agent.from_llm_and_tools)
[#](#langchain.agents.Agent.from_llm_and_tools "Permalink to this definition") 



 Construct an agent from an LLM and tools.
 








 get_allowed_tools
 


 (
 

 )
 


 →
 


 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/agents/agent#Agent.get_allowed_tools)
[#](#langchain.agents.Agent.get_allowed_tools "Permalink to this definition") 








 get_full_inputs
 


 (
 
*intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



[[source]](../../_modules/langchain/agents/agent#Agent.get_full_inputs)
[#](#langchain.agents.Agent.get_full_inputs "Permalink to this definition") 



 Create the full inputs for the LLMChain from intermediate steps.
 








 plan
 


 (
 
*intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
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
 


 Union
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 langchain.schema.AgentFinish
 


 ]
 



[[source]](../../_modules/langchain/agents/agent#Agent.plan)
[#](#langchain.agents.Agent.plan "Permalink to this definition") 



 Given input, decided what to do.
 




 Parameters
 

* **intermediate_steps** 
 – Steps the LLM has taken to date,
along with observations
* **callbacks** 
 – Callbacks to run.
* **\*\*kwargs** 
 – User inputs.




 Returns
 


 Action specifying what tool to use.
 










 return_stopped_response
 


 (
 
*early_stopping_method
 



 :
 





 str*
 ,
 *intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.schema.AgentFinish
 


[[source]](../../_modules/langchain/agents/agent#Agent.return_stopped_response)
[#](#langchain.agents.Agent.return_stopped_response "Permalink to this definition") 



 Return response when agent has been stopped due to max iterations.
 








 tool_run_logging_kwargs
 


 (
 

 )
 


 →
 


 Dict
 


[[source]](../../_modules/langchain/agents/agent#Agent.tool_run_logging_kwargs)
[#](#langchain.agents.Agent.tool_run_logging_kwargs "Permalink to this definition") 






*abstract
 



 property*


 llm_prefix
 

*:
 




 str*
[#](#langchain.agents.Agent.llm_prefix "Permalink to this definition") 



 Prefix to append the LLM call with.
 






*abstract
 



 property*


 observation_prefix
 

*:
 




 str*
[#](#langchain.agents.Agent.observation_prefix "Permalink to this definition") 



 Prefix to append the observation with.
 






*property*


 return_values
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.agents.Agent.return_values "Permalink to this definition") 



 Return values of the agent.
 








*pydantic
 

 model*


 langchain.agents.
 



 AgentExecutor
 

[[source]](../../_modules/langchain/agents/agent#AgentExecutor)
[#](#langchain.agents.AgentExecutor "Permalink to this definition") 



 Consists of an agent using tools.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_return_direct_tool`
 »
 `all
 

 fields`
* `validate_tools`
 »
 `all
 

 fields`






*field*


 agent
 

*:
 




 Union
 


 [
 

[BaseSingleActionAgent](#langchain.agents.BaseSingleActionAgent "langchain.agents.BaseSingleActionAgent")


 ,
 



[BaseMultiActionAgent](#langchain.agents.BaseMultiActionAgent "langchain.agents.BaseMultiActionAgent")


 ]*
*[Required]*
[#](#langchain.agents.AgentExecutor.agent "Permalink to this definition") 






*field*


 early_stopping_method
 

*:
 




 str*
*=
 




 'force'*
[#](#langchain.agents.AgentExecutor.early_stopping_method "Permalink to this definition") 






*field*


 max_execution_time
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 None*
[#](#langchain.agents.AgentExecutor.max_execution_time "Permalink to this definition") 






*field*


 max_iterations
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 15*
[#](#langchain.agents.AgentExecutor.max_iterations "Permalink to this definition") 






*field*


 return_intermediate_steps
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.agents.AgentExecutor.return_intermediate_steps "Permalink to this definition") 






*field*


 tools
 

*:
 




 Sequence
 


 [
 

[BaseTool](tools#langchain.tools.BaseTool "langchain.tools.BaseTool")


 ]*
*[Required]*
[#](#langchain.agents.AgentExecutor.tools "Permalink to this definition") 






*classmethod*


 from_agent_and_tools
 


 (
 
*agent
 



 :
 





 Union
 


 [
 

[langchain.agents.agent.BaseSingleActionAgent](#langchain.agents.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent")


 ,
 



[langchain.agents.agent.BaseMultiActionAgent](#langchain.agents.BaseMultiActionAgent "langchain.agents.agent.BaseMultiActionAgent")


 ]*
 ,
 *tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
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
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent#AgentExecutor.from_agent_and_tools)
[#](#langchain.agents.AgentExecutor.from_agent_and_tools "Permalink to this definition") 



 Create from agent and tools.
 








 lookup_tool
 


 (
 
*name
 



 :
 





 str*

 )
 


 →
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


[[source]](../../_modules/langchain/agents/agent#AgentExecutor.lookup_tool)
[#](#langchain.agents.AgentExecutor.lookup_tool "Permalink to this definition") 



 Lookup tool by name.
 








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
 


[[source]](../../_modules/langchain/agents/agent#AgentExecutor.save)
[#](#langchain.agents.AgentExecutor.save "Permalink to this definition") 



 Raise error - saving not supported for Agent Executors.
 








 save_agent
 


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
 


[[source]](../../_modules/langchain/agents/agent#AgentExecutor.save_agent)
[#](#langchain.agents.AgentExecutor.save_agent "Permalink to this definition") 



 Save the underlying agent.
 








*pydantic
 

 model*


 langchain.agents.
 



 AgentOutputParser
 

[[source]](../../_modules/langchain/agents/agent#AgentOutputParser)
[#](#langchain.agents.AgentOutputParser "Permalink to this definition") 




*abstract*


 parse
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 Union
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 langchain.schema.AgentFinish
 


 ]
 



[[source]](../../_modules/langchain/agents/agent#AgentOutputParser.parse)
[#](#langchain.agents.AgentOutputParser.parse "Permalink to this definition") 



 Parse text into agent action/finish.
 








*class*


 langchain.agents.
 



 AgentType
 


 (
 
*value*

 )
 
[[source]](../../_modules/langchain/agents/agent_types#AgentType)
[#](#langchain.agents.AgentType "Permalink to this definition") 



 An enumeration.
 






 CHAT_CONVERSATIONAL_REACT_DESCRIPTION
 

*=
 




 'chat-conversational-react-description'*
[#](#langchain.agents.AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION "Permalink to this definition") 








 CHAT_ZERO_SHOT_REACT_DESCRIPTION
 

*=
 




 'chat-zero-shot-react-description'*
[#](#langchain.agents.AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION "Permalink to this definition") 








 CONVERSATIONAL_REACT_DESCRIPTION
 

*=
 




 'conversational-react-description'*
[#](#langchain.agents.AgentType.CONVERSATIONAL_REACT_DESCRIPTION "Permalink to this definition") 








 REACT_DOCSTORE
 

*=
 




 'react-docstore'*
[#](#langchain.agents.AgentType.REACT_DOCSTORE "Permalink to this definition") 








 SELF_ASK_WITH_SEARCH
 

*=
 




 'self-ask-with-search'*
[#](#langchain.agents.AgentType.SELF_ASK_WITH_SEARCH "Permalink to this definition") 








 ZERO_SHOT_REACT_DESCRIPTION
 

*=
 




 'zero-shot-react-description'*
[#](#langchain.agents.AgentType.ZERO_SHOT_REACT_DESCRIPTION "Permalink to this definition") 








*pydantic
 

 model*


 langchain.agents.
 



 BaseMultiActionAgent
 

[[source]](../../_modules/langchain/agents/agent#BaseMultiActionAgent)
[#](#langchain.agents.BaseMultiActionAgent "Permalink to this definition") 



 Base Agent class.
 




*abstract
 



 async*


 aplan
 


 (
 
*intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
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
 


 Union
 


 [
 


 List
 


 [
 


 langchain.schema.AgentAction
 


 ]
 



 ,
 




 langchain.schema.AgentFinish
 


 ]
 



[[source]](../../_modules/langchain/agents/agent#BaseMultiActionAgent.aplan)
[#](#langchain.agents.BaseMultiActionAgent.aplan "Permalink to this definition") 



 Given input, decided what to do.
 




 Parameters
 

* **intermediate_steps** 
 – Steps the LLM has taken to date,
along with observations
* **callbacks** 
 – Callbacks to run.
* **\*\*kwargs** 
 – User inputs.




 Returns
 


 Actions specifying what tool to use.
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[[source]](../../_modules/langchain/agents/agent#BaseMultiActionAgent.dict)
[#](#langchain.agents.BaseMultiActionAgent.dict "Permalink to this definition") 



 Return dictionary representation of agent.
 








 get_allowed_tools
 


 (
 

 )
 


 →
 


 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/agents/agent#BaseMultiActionAgent.get_allowed_tools)
[#](#langchain.agents.BaseMultiActionAgent.get_allowed_tools "Permalink to this definition") 






*abstract*


 plan
 


 (
 
*intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
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
 


 Union
 


 [
 


 List
 


 [
 


 langchain.schema.AgentAction
 


 ]
 



 ,
 




 langchain.schema.AgentFinish
 


 ]
 



[[source]](../../_modules/langchain/agents/agent#BaseMultiActionAgent.plan)
[#](#langchain.agents.BaseMultiActionAgent.plan "Permalink to this definition") 



 Given input, decided what to do.
 




 Parameters
 

* **intermediate_steps** 
 – Steps the LLM has taken to date,
along with observations
* **callbacks** 
 – Callbacks to run.
* **\*\*kwargs** 
 – User inputs.




 Returns
 


 Actions specifying what tool to use.
 










 return_stopped_response
 


 (
 
*early_stopping_method
 



 :
 





 str*
 ,
 *intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.schema.AgentFinish
 


[[source]](../../_modules/langchain/agents/agent#BaseMultiActionAgent.return_stopped_response)
[#](#langchain.agents.BaseMultiActionAgent.return_stopped_response "Permalink to this definition") 



 Return response when agent has been stopped due to max iterations.
 








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
 


[[source]](../../_modules/langchain/agents/agent#BaseMultiActionAgent.save)
[#](#langchain.agents.BaseMultiActionAgent.save "Permalink to this definition") 



 Save the agent.
 




 Parameters
 


**file_path** 
 – Path to file to save the agent to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  # If working with agent executor
> agent.agent.save(file_path=”path/agent.yaml”)
>  
> 
> 
> 
> 








 tool_run_logging_kwargs
 


 (
 

 )
 


 →
 


 Dict
 


[[source]](../../_modules/langchain/agents/agent#BaseMultiActionAgent.tool_run_logging_kwargs)
[#](#langchain.agents.BaseMultiActionAgent.tool_run_logging_kwargs "Permalink to this definition") 






*property*


 return_values
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.agents.BaseMultiActionAgent.return_values "Permalink to this definition") 



 Return values of the agent.
 








*pydantic
 

 model*


 langchain.agents.
 



 BaseSingleActionAgent
 

[[source]](../../_modules/langchain/agents/agent#BaseSingleActionAgent)
[#](#langchain.agents.BaseSingleActionAgent "Permalink to this definition") 



 Base Agent class.
 




*abstract
 



 async*


 aplan
 


 (
 
*intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
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
 


 Union
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 langchain.schema.AgentFinish
 


 ]
 



[[source]](../../_modules/langchain/agents/agent#BaseSingleActionAgent.aplan)
[#](#langchain.agents.BaseSingleActionAgent.aplan "Permalink to this definition") 



 Given input, decided what to do.
 




 Parameters
 

* **intermediate_steps** 
 – Steps the LLM has taken to date,
along with observations
* **callbacks** 
 – Callbacks to run.
* **\*\*kwargs** 
 – User inputs.




 Returns
 


 Action specifying what tool to use.
 










 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[[source]](../../_modules/langchain/agents/agent#BaseSingleActionAgent.dict)
[#](#langchain.agents.BaseSingleActionAgent.dict "Permalink to this definition") 



 Return dictionary representation of agent.
 






*classmethod*


 from_llm_and_tools
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
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
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.BaseSingleActionAgent](#langchain.agents.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent")


[[source]](../../_modules/langchain/agents/agent#BaseSingleActionAgent.from_llm_and_tools)
[#](#langchain.agents.BaseSingleActionAgent.from_llm_and_tools "Permalink to this definition") 








 get_allowed_tools
 


 (
 

 )
 


 →
 


 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/agents/agent#BaseSingleActionAgent.get_allowed_tools)
[#](#langchain.agents.BaseSingleActionAgent.get_allowed_tools "Permalink to this definition") 






*abstract*


 plan
 


 (
 
*intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
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
 


 Union
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 langchain.schema.AgentFinish
 


 ]
 



[[source]](../../_modules/langchain/agents/agent#BaseSingleActionAgent.plan)
[#](#langchain.agents.BaseSingleActionAgent.plan "Permalink to this definition") 



 Given input, decided what to do.
 




 Parameters
 

* **intermediate_steps** 
 – Steps the LLM has taken to date,
along with observations
* **callbacks** 
 – Callbacks to run.
* **\*\*kwargs** 
 – User inputs.




 Returns
 


 Action specifying what tool to use.
 










 return_stopped_response
 


 (
 
*early_stopping_method
 



 :
 





 str*
 ,
 *intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.schema.AgentFinish
 


[[source]](../../_modules/langchain/agents/agent#BaseSingleActionAgent.return_stopped_response)
[#](#langchain.agents.BaseSingleActionAgent.return_stopped_response "Permalink to this definition") 



 Return response when agent has been stopped due to max iterations.
 








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
 


[[source]](../../_modules/langchain/agents/agent#BaseSingleActionAgent.save)
[#](#langchain.agents.BaseSingleActionAgent.save "Permalink to this definition") 



 Save the agent.
 




 Parameters
 


**file_path** 
 – Path to file to save the agent to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  # If working with agent executor
> agent.agent.save(file_path=”path/agent.yaml”)
>  
> 
> 
> 
> 








 tool_run_logging_kwargs
 


 (
 

 )
 


 →
 


 Dict
 


[[source]](../../_modules/langchain/agents/agent#BaseSingleActionAgent.tool_run_logging_kwargs)
[#](#langchain.agents.BaseSingleActionAgent.tool_run_logging_kwargs "Permalink to this definition") 






*property*


 return_values
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.agents.BaseSingleActionAgent.return_values "Permalink to this definition") 



 Return values of the agent.
 








*pydantic
 

 model*


 langchain.agents.
 



 ConversationalAgent
 

[[source]](../../_modules/langchain/agents/conversational/base#ConversationalAgent)
[#](#langchain.agents.ConversationalAgent "Permalink to this definition") 



 An agent designed to hold a conversation in addition to using tools.
 




*field*


 ai_prefix
 

*:
 




 str*
*=
 




 'AI'*
[#](#langchain.agents.ConversationalAgent.ai_prefix "Permalink to this definition") 






*field*


 output_parser
 

*:
 



[langchain.agents.agent.AgentOutputParser](#langchain.agents.AgentOutputParser "langchain.agents.agent.AgentOutputParser")*
*[Optional]*
[#](#langchain.agents.ConversationalAgent.output_parser "Permalink to this definition") 






*classmethod*


 create_prompt
 


 (
 
*tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
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
 

 OpenAI.\n\nAssistant
 

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
 

 topics.\n\nOverall,
 

 Assistant
 

 is
 

 a
 

 powerful
 

 tool
 

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
 

 assist.\n\nTOOLS:\n------\n\nAssistant
 

 has
 

 access
 

 to
 

 the
 

 following
 

 tools:'*
 ,
 *suffix
 



 :
 





 str
 





 =
 





 'Begin!\n\nPrevious
 

 conversation
 

 history:\n{chat_history}\n\nNew
 

 input:
 

 {input}\n{agent_scratchpad}'*
 ,
 *format_instructions
 



 :
 





 str
 





 =
 





 'To
 

 use
 

 a
 

 tool,
 

 please
 

 use
 

 the
 

 following
 

 format:\n\n```\nThought:
 

 Do
 

 I
 

 need
 

 to
 

 use
 

 a
 

 tool?
 

 Yes\nAction:
 

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
 

 action\n```\n\nWhen
 

 you
 

 have
 

 a
 

 response
 

 to
 

 say
 

 to
 

 the
 

 Human,
 

 or
 

 if
 

 you
 

 do
 

 not
 

 need
 

 to
 

 use
 

 a
 

 tool,
 

 you
 

 MUST
 

 use
 

 the
 

 format:\n\n```\nThought:
 

 Do
 

 I
 

 need
 

 to
 

 use
 

 a
 

 tool?
 

 No\n{ai_prefix}:
 

 [your
 

 response
 

 here]\n```'*
 ,
 *ai_prefix
 



 :
 





 str
 





 =
 





 'AI'*
 ,
 *human_prefix
 



 :
 





 str
 





 =
 





 'Human'*
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

 )
 


 →
 

[langchain.prompts.prompt.PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")


[[source]](../../_modules/langchain/agents/conversational/base#ConversationalAgent.create_prompt)
[#](#langchain.agents.ConversationalAgent.create_prompt "Permalink to this definition") 



 Create prompt in the style of the zero shot agent.
 




 Parameters
 

* **tools** 
 – List of tools the agent will have access to, used to format the
prompt.
* **prefix** 
 – String to put before the list of tools.
* **suffix** 
 – String to put after the list of tools.
* **ai_prefix** 
 – String to use before AI output.
* **human_prefix** 
 – String to use before human output.
* **input_variables** 
 – List of input variables the final prompt will expect.




 Returns
 


 A PromptTemplate with the template assembled from the pieces here.
 








*classmethod*


 from_llm_and_tools
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
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
 *output_parser
 



 :
 





 Optional
 


 [
 

[langchain.agents.agent.AgentOutputParser](#langchain.agents.AgentOutputParser "langchain.agents.agent.AgentOutputParser")


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
 

 OpenAI.\n\nAssistant
 

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
 

 topics.\n\nOverall,
 

 Assistant
 

 is
 

 a
 

 powerful
 

 tool
 

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
 

 assist.\n\nTOOLS:\n------\n\nAssistant
 

 has
 

 access
 

 to
 

 the
 

 following
 

 tools:'*
 ,
 *suffix
 



 :
 





 str
 





 =
 





 'Begin!\n\nPrevious
 

 conversation
 

 history:\n{chat_history}\n\nNew
 

 input:
 

 {input}\n{agent_scratchpad}'*
 ,
 *format_instructions
 



 :
 





 str
 





 =
 





 'To
 

 use
 

 a
 

 tool,
 

 please
 

 use
 

 the
 

 following
 

 format:\n\n```\nThought:
 

 Do
 

 I
 

 need
 

 to
 

 use
 

 a
 

 tool?
 

 Yes\nAction:
 

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
 

 action\n```\n\nWhen
 

 you
 

 have
 

 a
 

 response
 

 to
 

 say
 

 to
 

 the
 

 Human,
 

 or
 

 if
 

 you
 

 do
 

 not
 

 need
 

 to
 

 use
 

 a
 

 tool,
 

 you
 

 MUST
 

 use
 

 the
 

 format:\n\n```\nThought:
 

 Do
 

 I
 

 need
 

 to
 

 use
 

 a
 

 tool?
 

 No\n{ai_prefix}:
 

 [your
 

 response
 

 here]\n```'*
 ,
 *ai_prefix
 



 :
 





 str
 





 =
 





 'AI'*
 ,
 *human_prefix
 



 :
 





 str
 





 =
 





 'Human'*
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
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.Agent](#langchain.agents.Agent "langchain.agents.agent.Agent")


[[source]](../../_modules/langchain/agents/conversational/base#ConversationalAgent.from_llm_and_tools)
[#](#langchain.agents.ConversationalAgent.from_llm_and_tools "Permalink to this definition") 



 Construct an agent from an LLM and tools.
 






*property*


 llm_prefix
 

*:
 




 str*
[#](#langchain.agents.ConversationalAgent.llm_prefix "Permalink to this definition") 



 Prefix to append the llm call with.
 






*property*


 observation_prefix
 

*:
 




 str*
[#](#langchain.agents.ConversationalAgent.observation_prefix "Permalink to this definition") 



 Prefix to append the observation with.
 








*pydantic
 

 model*


 langchain.agents.
 



 ConversationalChatAgent
 

[[source]](../../_modules/langchain/agents/conversational_chat/base#ConversationalChatAgent)
[#](#langchain.agents.ConversationalChatAgent "Permalink to this definition") 



 An agent designed to hold a conversation in addition to using tools.
 




*field*


 output_parser
 

*:
 



[langchain.agents.agent.AgentOutputParser](#langchain.agents.AgentOutputParser "langchain.agents.agent.AgentOutputParser")*
*[Optional]*
[#](#langchain.agents.ConversationalChatAgent.output_parser "Permalink to this definition") 






*classmethod*


 create_prompt
 


 (
 
*tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
 ,
 *system_message
 



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
 

 OpenAI.\n\nAssistant
 

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
 

 topics.\n\nOverall,
 

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
 

 assist.'*
 ,
 *human_message
 



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
 

 else):\n\n{{{{input}}}}"*
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
 *output_parser
 



 :
 





 Optional
 


 [
 


 langchain.schema.BaseOutputParser
 


 ]
 






 =
 





 None*

 )
 


 →
 

[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")


[[source]](../../_modules/langchain/agents/conversational_chat/base#ConversationalChatAgent.create_prompt)
[#](#langchain.agents.ConversationalChatAgent.create_prompt "Permalink to this definition") 



 Create a prompt for this class.
 






*classmethod*


 from_llm_and_tools
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
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
 *output_parser
 



 :
 





 Optional
 


 [
 

[langchain.agents.agent.AgentOutputParser](#langchain.agents.AgentOutputParser "langchain.agents.agent.AgentOutputParser")


 ]
 






 =
 





 None*
 ,
 *system_message
 



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
 

 OpenAI.\n\nAssistant
 

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
 

 topics.\n\nOverall,
 

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
 

 assist.'*
 ,
 *human_message
 



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
 

 else):\n\n{{{{input}}}}"*
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
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.Agent](#langchain.agents.Agent "langchain.agents.agent.Agent")


[[source]](../../_modules/langchain/agents/conversational_chat/base#ConversationalChatAgent.from_llm_and_tools)
[#](#langchain.agents.ConversationalChatAgent.from_llm_and_tools "Permalink to this definition") 



 Construct an agent from an LLM and tools.
 






*property*


 llm_prefix
 

*:
 




 str*
[#](#langchain.agents.ConversationalChatAgent.llm_prefix "Permalink to this definition") 



 Prefix to append the llm call with.
 






*property*


 observation_prefix
 

*:
 




 str*
[#](#langchain.agents.ConversationalChatAgent.observation_prefix "Permalink to this definition") 



 Prefix to append the observation with.
 








*pydantic
 

 model*


 langchain.agents.
 



 LLMSingleActionAgent
 

[[source]](../../_modules/langchain/agents/agent#LLMSingleActionAgent)
[#](#langchain.agents.LLMSingleActionAgent "Permalink to this definition") 




*field*


 llm_chain
 

*:
 



[langchain.chains.llm.LLMChain](chains#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
*[Required]*
[#](#langchain.agents.LLMSingleActionAgent.llm_chain "Permalink to this definition") 






*field*


 output_parser
 

*:
 



[langchain.agents.agent.AgentOutputParser](#langchain.agents.AgentOutputParser "langchain.agents.agent.AgentOutputParser")*
*[Required]*
[#](#langchain.agents.LLMSingleActionAgent.output_parser "Permalink to this definition") 






*field*


 stop
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Required]*
[#](#langchain.agents.LLMSingleActionAgent.stop "Permalink to this definition") 






*async*


 aplan
 


 (
 
*intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
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
 


 Union
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 langchain.schema.AgentFinish
 


 ]
 



[[source]](../../_modules/langchain/agents/agent#LLMSingleActionAgent.aplan)
[#](#langchain.agents.LLMSingleActionAgent.aplan "Permalink to this definition") 



 Given input, decided what to do.
 




 Parameters
 

* **intermediate_steps** 
 – Steps the LLM has taken to date,
along with observations
* **callbacks** 
 – Callbacks to run.
* **\*\*kwargs** 
 – User inputs.




 Returns
 


 Action specifying what tool to use.
 










 plan
 


 (
 
*intermediate_steps
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 str
 


 ]
 



 ]*
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
 


 Union
 


 [
 


 langchain.schema.AgentAction
 


 ,
 




 langchain.schema.AgentFinish
 


 ]
 



[[source]](../../_modules/langchain/agents/agent#LLMSingleActionAgent.plan)
[#](#langchain.agents.LLMSingleActionAgent.plan "Permalink to this definition") 



 Given input, decided what to do.
 




 Parameters
 

* **intermediate_steps** 
 – Steps the LLM has taken to date,
along with observations
* **callbacks** 
 – Callbacks to run.
* **\*\*kwargs** 
 – User inputs.




 Returns
 


 Action specifying what tool to use.
 










 tool_run_logging_kwargs
 


 (
 

 )
 


 →
 


 Dict
 


[[source]](../../_modules/langchain/agents/agent#LLMSingleActionAgent.tool_run_logging_kwargs)
[#](#langchain.agents.LLMSingleActionAgent.tool_run_logging_kwargs "Permalink to this definition") 








*pydantic
 

 model*


 langchain.agents.
 



 MRKLChain
 

[[source]](../../_modules/langchain/agents/mrkl/base#MRKLChain)
[#](#langchain.agents.MRKLChain "Permalink to this definition") 



 Chain that implements the MRKL system.
 



 Example
 





```
from langchain import OpenAI, MRKLChain
from langchain.chains.mrkl.base import ChainConfig
llm = OpenAI(temperature=0)
prompt = PromptTemplate(...)
chains = [...]
mrkl = MRKLChain.from_chains(llm=llm, prompt=prompt)

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_return_direct_tool`
 »
 `all
 

 fields`
* `validate_tools`
 »
 `all
 

 fields`






*field*


 agent
 

*:
 




 Union
 


 [
 

[BaseSingleActionAgent](#langchain.agents.BaseSingleActionAgent "langchain.agents.BaseSingleActionAgent")


 ,
 



[BaseMultiActionAgent](#langchain.agents.BaseMultiActionAgent "langchain.agents.BaseMultiActionAgent")


 ]*
*[Required]*
[#](#langchain.agents.MRKLChain.agent "Permalink to this definition") 






*field*


 callback_manager
 

*:
 




 Optional
 


 [
 


 BaseCallbackManager
 


 ]*
*=
 




 None*
[#](#langchain.agents.MRKLChain.callback_manager "Permalink to this definition") 






*field*


 callbacks
 

*:
 




 Callbacks*
*=
 




 None*
[#](#langchain.agents.MRKLChain.callbacks "Permalink to this definition") 






*field*


 early_stopping_method
 

*:
 




 str*
*=
 




 'force'*
[#](#langchain.agents.MRKLChain.early_stopping_method "Permalink to this definition") 






*field*


 max_execution_time
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 None*
[#](#langchain.agents.MRKLChain.max_execution_time "Permalink to this definition") 






*field*


 max_iterations
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 15*
[#](#langchain.agents.MRKLChain.max_iterations "Permalink to this definition") 






*field*


 memory
 

*:
 




 Optional
 


 [
 


 BaseMemory
 


 ]*
*=
 




 None*
[#](#langchain.agents.MRKLChain.memory "Permalink to this definition") 






*field*


 return_intermediate_steps
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.agents.MRKLChain.return_intermediate_steps "Permalink to this definition") 






*field*


 tools
 

*:
 




 Sequence
 


 [
 

[BaseTool](tools#langchain.tools.BaseTool "langchain.tools.BaseTool")


 ]*
*[Required]*
[#](#langchain.agents.MRKLChain.tools "Permalink to this definition") 






*field*


 verbose
 

*:
 




 bool*
*[Optional]*
[#](#langchain.agents.MRKLChain.verbose "Permalink to this definition") 






*classmethod*


 from_chains
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *chains
 



 :
 





 List
 


 [
 


 langchain.agents.mrkl.base.ChainConfig
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/mrkl/base#MRKLChain.from_chains)
[#](#langchain.agents.MRKLChain.from_chains "Permalink to this definition") 



 User friendly way to initialize the MRKL chain.
 



 This is intended to be an easy way to get up and running with the
MRKL chain.
 




 Parameters
 

* **llm** 
 – The LLM to use as the agent LLM.
* **chains** 
 – The chains the MRKL system has access to.
* **\*\*kwargs** 
 – parameters to be passed to initialization.




 Returns
 


 An initialized MRKL chain.
 





 Example
 





```
from langchain import LLMMathChain, OpenAI, SerpAPIWrapper, MRKLChain
from langchain.chains.mrkl.base import ChainConfig
llm = OpenAI(temperature=0)
search = SerpAPIWrapper()
llm_math_chain = LLMMathChain(llm=llm)
chains = [
    ChainConfig(
        action_name = "Search",
        action=search.search,
        action_description="useful for searching"
    ),
    ChainConfig(
        action_name="Calculator",
        action=llm_math_chain.run,
        action_description="useful for doing math"
    )
]
mrkl = MRKLChain.from_chains(llm, chains)

```









*pydantic
 

 model*


 langchain.agents.
 



 ReActChain
 

[[source]](../../_modules/langchain/agents/react/base#ReActChain)
[#](#langchain.agents.ReActChain "Permalink to this definition") 



 Chain that implements the ReAct paper.
 



 Example
 





```
from langchain import ReActChain, OpenAI
react = ReAct(llm=OpenAI())

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_return_direct_tool`
 »
 `all
 

 fields`
* `validate_tools`
 »
 `all
 

 fields`






*field*


 agent
 

*:
 




 Union
 


 [
 

[BaseSingleActionAgent](#langchain.agents.BaseSingleActionAgent "langchain.agents.BaseSingleActionAgent")


 ,
 



[BaseMultiActionAgent](#langchain.agents.BaseMultiActionAgent "langchain.agents.BaseMultiActionAgent")


 ]*
*[Required]*
[#](#langchain.agents.ReActChain.agent "Permalink to this definition") 






*field*


 callback_manager
 

*:
 




 Optional
 


 [
 


 BaseCallbackManager
 


 ]*
*=
 




 None*
[#](#langchain.agents.ReActChain.callback_manager "Permalink to this definition") 






*field*


 callbacks
 

*:
 




 Callbacks*
*=
 




 None*
[#](#langchain.agents.ReActChain.callbacks "Permalink to this definition") 






*field*


 early_stopping_method
 

*:
 




 str*
*=
 




 'force'*
[#](#langchain.agents.ReActChain.early_stopping_method "Permalink to this definition") 






*field*


 max_execution_time
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 None*
[#](#langchain.agents.ReActChain.max_execution_time "Permalink to this definition") 






*field*


 max_iterations
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 15*
[#](#langchain.agents.ReActChain.max_iterations "Permalink to this definition") 






*field*


 memory
 

*:
 




 Optional
 


 [
 


 BaseMemory
 


 ]*
*=
 




 None*
[#](#langchain.agents.ReActChain.memory "Permalink to this definition") 






*field*


 return_intermediate_steps
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.agents.ReActChain.return_intermediate_steps "Permalink to this definition") 






*field*


 tools
 

*:
 




 Sequence
 


 [
 

[BaseTool](tools#langchain.tools.BaseTool "langchain.tools.BaseTool")


 ]*
*[Required]*
[#](#langchain.agents.ReActChain.tools "Permalink to this definition") 






*field*


 verbose
 

*:
 




 bool*
*[Optional]*
[#](#langchain.agents.ReActChain.verbose "Permalink to this definition") 








*pydantic
 

 model*


 langchain.agents.
 



 ReActTextWorldAgent
 

[[source]](../../_modules/langchain/agents/react/base#ReActTextWorldAgent)
[#](#langchain.agents.ReActTextWorldAgent "Permalink to this definition") 



 Agent for the ReAct TextWorld chain.
 




*field*


 output_parser
 

*:
 



[langchain.agents.agent.AgentOutputParser](#langchain.agents.AgentOutputParser "langchain.agents.agent.AgentOutputParser")*
*[Optional]*
[#](#langchain.agents.ReActTextWorldAgent.output_parser "Permalink to this definition") 






*classmethod*


 create_prompt
 


 (
 
*tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*

 )
 


 →
 

[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")


[[source]](../../_modules/langchain/agents/react/base#ReActTextWorldAgent.create_prompt)
[#](#langchain.agents.ReActTextWorldAgent.create_prompt "Permalink to this definition") 



 Return default prompt.
 








*pydantic
 

 model*


 langchain.agents.
 



 SelfAskWithSearchChain
 

[[source]](../../_modules/langchain/agents/self_ask_with_search/base#SelfAskWithSearchChain)
[#](#langchain.agents.SelfAskWithSearchChain "Permalink to this definition") 



 Chain that does self ask with search.
 



 Example
 





```
from langchain import SelfAskWithSearchChain, OpenAI, GoogleSerperAPIWrapper
search_chain = GoogleSerperAPIWrapper()
self_ask = SelfAskWithSearchChain(llm=OpenAI(), search_chain=search_chain)

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_return_direct_tool`
 »
 `all
 

 fields`
* `validate_tools`
 »
 `all
 

 fields`






*field*


 agent
 

*:
 




 Union
 


 [
 

[BaseSingleActionAgent](#langchain.agents.BaseSingleActionAgent "langchain.agents.BaseSingleActionAgent")


 ,
 



[BaseMultiActionAgent](#langchain.agents.BaseMultiActionAgent "langchain.agents.BaseMultiActionAgent")


 ]*
*[Required]*
[#](#langchain.agents.SelfAskWithSearchChain.agent "Permalink to this definition") 






*field*


 callback_manager
 

*:
 




 Optional
 


 [
 


 BaseCallbackManager
 


 ]*
*=
 




 None*
[#](#langchain.agents.SelfAskWithSearchChain.callback_manager "Permalink to this definition") 






*field*


 callbacks
 

*:
 




 Callbacks*
*=
 




 None*
[#](#langchain.agents.SelfAskWithSearchChain.callbacks "Permalink to this definition") 






*field*


 early_stopping_method
 

*:
 




 str*
*=
 




 'force'*
[#](#langchain.agents.SelfAskWithSearchChain.early_stopping_method "Permalink to this definition") 






*field*


 max_execution_time
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 None*
[#](#langchain.agents.SelfAskWithSearchChain.max_execution_time "Permalink to this definition") 






*field*


 max_iterations
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 15*
[#](#langchain.agents.SelfAskWithSearchChain.max_iterations "Permalink to this definition") 






*field*


 memory
 

*:
 




 Optional
 


 [
 


 BaseMemory
 


 ]*
*=
 




 None*
[#](#langchain.agents.SelfAskWithSearchChain.memory "Permalink to this definition") 






*field*


 return_intermediate_steps
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.agents.SelfAskWithSearchChain.return_intermediate_steps "Permalink to this definition") 






*field*


 tools
 

*:
 




 Sequence
 


 [
 

[BaseTool](tools#langchain.tools.BaseTool "langchain.tools.BaseTool")


 ]*
*[Required]*
[#](#langchain.agents.SelfAskWithSearchChain.tools "Permalink to this definition") 






*field*


 verbose
 

*:
 




 bool*
*[Optional]*
[#](#langchain.agents.SelfAskWithSearchChain.verbose "Permalink to this definition") 








*pydantic
 

 model*


 langchain.agents.
 



 Tool
 

[[source]](../../_modules/langchain/agents/tools#Tool)
[#](#langchain.agents.Tool "Permalink to this definition") 



 Tool that takes in function or coroutine directly.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `validate_func_not_partial`
 »
 `func`






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
 


 str
 


 ]
 



 ]
 



 ]*
*=
 




 None*
[#](#langchain.agents.Tool.coroutine "Permalink to this definition") 



 The asynchronous version of the function.
 






*field*


 description
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.agents.Tool.description "Permalink to this definition") 



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
 




 str
 


 ]*
*[Required]*
[#](#langchain.agents.Tool.func "Permalink to this definition") 



 The function to run when the tool is called.
 






*property*


 args
 

*:
 




 dict*
[#](#langchain.agents.Tool.args "Permalink to this definition") 



 The tool’s input arguments.
 








*pydantic
 

 model*


 langchain.agents.
 



 ZeroShotAgent
 

[[source]](../../_modules/langchain/agents/mrkl/base#ZeroShotAgent)
[#](#langchain.agents.ZeroShotAgent "Permalink to this definition") 



 Agent for the MRKL chain.
 




*field*


 output_parser
 

*:
 



[langchain.agents.agent.AgentOutputParser](#langchain.agents.AgentOutputParser "langchain.agents.agent.AgentOutputParser")*
*[Optional]*
[#](#langchain.agents.ZeroShotAgent.output_parser "Permalink to this definition") 






*classmethod*


 create_prompt
 


 (
 
*tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 'Answer
 

 the
 

 following
 

 questions
 

 as
 

 best
 

 you
 

 can.
 

 You
 

 have
 

 access
 

 to
 

 the
 

 following
 

 tools:'*
 ,
 *suffix
 



 :
 





 str
 





 =
 





 'Begin!\n\nQuestion:
 

 {input}\nThought:{agent_scratchpad}'*
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

 )
 


 →
 

[langchain.prompts.prompt.PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")


[[source]](../../_modules/langchain/agents/mrkl/base#ZeroShotAgent.create_prompt)
[#](#langchain.agents.ZeroShotAgent.create_prompt "Permalink to this definition") 



 Create prompt in the style of the zero shot agent.
 




 Parameters
 

* **tools** 
 – List of tools the agent will have access to, used to format the
prompt.
* **prefix** 
 – String to put before the list of tools.
* **suffix** 
 – String to put after the list of tools.
* **input_variables** 
 – List of input variables the final prompt will expect.




 Returns
 


 A PromptTemplate with the template assembled from the pieces here.
 








*classmethod*


 from_llm_and_tools
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
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
 *output_parser
 



 :
 





 Optional
 


 [
 

[langchain.agents.agent.AgentOutputParser](#langchain.agents.AgentOutputParser "langchain.agents.agent.AgentOutputParser")


 ]
 






 =
 





 None*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 'Answer
 

 the
 

 following
 

 questions
 

 as
 

 best
 

 you
 

 can.
 

 You
 

 have
 

 access
 

 to
 

 the
 

 following
 

 tools:'*
 ,
 *suffix
 



 :
 





 str
 





 =
 





 'Begin!\n\nQuestion:
 

 {input}\nThought:{agent_scratchpad}'*
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
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.Agent](#langchain.agents.Agent "langchain.agents.agent.Agent")


[[source]](../../_modules/langchain/agents/mrkl/base#ZeroShotAgent.from_llm_and_tools)
[#](#langchain.agents.ZeroShotAgent.from_llm_and_tools "Permalink to this definition") 



 Construct an agent from an LLM and tools.
 






*property*


 llm_prefix
 

*:
 




 str*
[#](#langchain.agents.ZeroShotAgent.llm_prefix "Permalink to this definition") 



 Prefix to append the llm call with.
 






*property*


 observation_prefix
 

*:
 




 str*
[#](#langchain.agents.ZeroShotAgent.observation_prefix "Permalink to this definition") 



 Prefix to append the observation with.
 










 langchain.agents.
 



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
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/csv/base#create_csv_agent)
[#](#langchain.agents.create_csv_agent "Permalink to this definition") 



 Create csv agent by loading to a dataframe and using pandas agent.
 








 langchain.agents.
 



 create_json_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *toolkit
 



 :
 




[langchain.agents.agent_toolkits.json.toolkit.JsonToolkit](agent_toolkits#langchain.agents.agent_toolkits.JsonToolkit "langchain.agents.agent_toolkits.json.toolkit.JsonToolkit")*
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
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/json/base#create_json_agent)
[#](#langchain.agents.create_json_agent "Permalink to this definition") 



 Construct a json agent from an LLM and tools.
 








 langchain.agents.
 



 create_openapi_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *toolkit
 



 :
 




[langchain.agents.agent_toolkits.openapi.toolkit.OpenAPIToolkit](agent_toolkits#langchain.agents.agent_toolkits.OpenAPIToolkit "langchain.agents.agent_toolkits.openapi.toolkit.OpenAPIToolkit")*
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
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/openapi/base#create_openapi_agent)
[#](#langchain.agents.create_openapi_agent "Permalink to this definition") 



 Construct a json agent from an LLM and tools.
 








 langchain.agents.
 



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
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/pandas/base#create_pandas_dataframe_agent)
[#](#langchain.agents.create_pandas_dataframe_agent "Permalink to this definition") 



 Construct a pandas agent from an LLM and dataframe.
 








 langchain.agents.
 



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
 

[langchain.agents.agent_toolkits.powerbi.toolkit.PowerBIToolkit](agent_toolkits#langchain.agents.agent_toolkits.PowerBIToolkit "langchain.agents.agent_toolkits.powerbi.toolkit.PowerBIToolkit")


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
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/powerbi/base#create_pbi_agent)
[#](#langchain.agents.create_pbi_agent "Permalink to this definition") 



 Construct a pbi agent from an LLM and tools.
 








 langchain.agents.
 



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
 

[langchain.agents.agent_toolkits.powerbi.toolkit.PowerBIToolkit](agent_toolkits#langchain.agents.agent_toolkits.PowerBIToolkit "langchain.agents.agent_toolkits.powerbi.toolkit.PowerBIToolkit")


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
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/powerbi/chat_base#create_pbi_chat_agent)
[#](#langchain.agents.create_pbi_chat_agent "Permalink to this definition") 



 Construct a pbi agent from an Chat LLM and tools.
 



 If you supply only a toolkit and no powerbi dataset, the same LLM is used for both.
 








 langchain.agents.
 



 create_sql_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *toolkit
 



 :
 




[langchain.agents.agent_toolkits.sql.toolkit.SQLDatabaseToolkit](agent_toolkits#langchain.agents.agent_toolkits.SQLDatabaseToolkit "langchain.agents.agent_toolkits.sql.toolkit.SQLDatabaseToolkit")*
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
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/sql/base#create_sql_agent)
[#](#langchain.agents.create_sql_agent "Permalink to this definition") 



 Construct a sql agent from an LLM and tools.
 








 langchain.agents.
 



 create_vectorstore_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *toolkit
 



 :
 




[langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreToolkit](agent_toolkits#langchain.agents.agent_toolkits.VectorStoreToolkit "langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreToolkit")*
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
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/vectorstore/base#create_vectorstore_agent)
[#](#langchain.agents.create_vectorstore_agent "Permalink to this definition") 



 Construct a vectorstore agent from an LLM and tools.
 








 langchain.agents.
 



 create_vectorstore_router_agent
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *toolkit
 



 :
 




[langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreRouterToolkit](agent_toolkits#langchain.agents.agent_toolkits.VectorStoreRouterToolkit "langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreRouterToolkit")*
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
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/agent_toolkits/vectorstore/base#create_vectorstore_router_agent)
[#](#langchain.agents.create_vectorstore_router_agent "Permalink to this definition") 



 Construct a vectorstore router agent from an LLM and tools.
 








 langchain.agents.
 



 get_all_tool_names
 


 (
 

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/agents/load_tools#get_all_tool_names)
[#](#langchain.agents.get_all_tool_names "Permalink to this definition") 



 Get a list of all possible tool names.
 








 langchain.agents.
 



 initialize_agent
 


 (
 
*tools
 



 :
 





 Sequence
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
 ,
 *llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *agent
 



 :
 





 Optional
 


 [
 

[langchain.agents.agent_types.AgentType](#langchain.agents.AgentType "langchain.agents.agent_types.AgentType")


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
 *agent_path
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *agent_kwargs
 



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
 

[langchain.agents.agent.AgentExecutor](#langchain.agents.AgentExecutor "langchain.agents.agent.AgentExecutor")


[[source]](../../_modules/langchain/agents/initialize#initialize_agent)
[#](#langchain.agents.initialize_agent "Permalink to this definition") 



 Load an agent executor given tools and LLM.
 




 Parameters
 

* **tools** 
 – List of tools this agent has access to.
* **llm** 
 – Language model to use as the agent.
* **agent** 
 – Agent type to use. If None and agent_path is also None, will default to
AgentType.ZERO_SHOT_REACT_DESCRIPTION.
* **callback_manager** 
 – CallbackManager to use. Global callback manager is used if
not provided. Defaults to None.
* **agent_path** 
 – Path to serialized agent to use.
* **agent_kwargs** 
 – Additional key word arguments to pass to the underlying agent
* **\*\*kwargs** 
 – Additional key word arguments passed to the agent executor




 Returns
 


 An agent executor
 










 langchain.agents.
 



 load_agent
 


 (
 
*path
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 pathlib.Path
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.agents.agent.BaseSingleActionAgent](#langchain.agents.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent")


[[source]](../../_modules/langchain/agents/loading#load_agent)
[#](#langchain.agents.load_agent "Permalink to this definition") 



 Unified method for loading a agent from LangChainHub or local fs.
 








 langchain.agents.
 



 load_tools
 


 (
 
*tool_names
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *llm
 



 :
 





 Optional
 


 [
 


 langchain.llms.base.BaseLLM
 


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
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]
 



[[source]](../../_modules/langchain/agents/load_tools#load_tools)
[#](#langchain.agents.load_tools "Permalink to this definition") 



 Load tools based on their name.
 




 Parameters
 

* **tool_names** 
 – name of tools to load.
* **llm** 
 – Optional language model, may be needed to initialize certain tools.
* **callback_manager** 
 – Optional callback manager. If not provided, default global callback manager will be used.




 Returns
 


 List of tools.
 










 langchain.agents.
 



 tool
 


 (
 
*\*
 



 args
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 Callable
 


 ]*
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

 )
 


 →
 


 Callable
 


[[source]](../../_modules/langchain/agents/tools#tool)
[#](#langchain.agents.tool "Permalink to this definition") 



 Make tools out of functions, can be used with or without arguments.
 




 Parameters
 

* **\*args** 
 – The arguments to the tool.
* **return_direct** 
 – Whether to return directly from the tool rather
than continuing the agent loop.
* **args_schema** 
 – optional argument schema for user to specify
* **infer_schema** 
 – Whether to infer the schema of the arguments from
the function’s signature. This also makes the resultant tool
accept a dictionary input to its
 
 run()
 
 function.






 Requires:
 

* Function must be of type (str) -> str
* Function must have a docstring





 Examples
 





```
@tool
def search_api(query: str) -> str:
    # Searches the API for the query.
    return

@tool("search", return_direct=True)
def search_api(query: str) -> str:
    # Searches the API for the query.
    return

```







