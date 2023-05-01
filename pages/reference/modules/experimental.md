


 Experimental Modules
 [#](#experimental-modules "Permalink to this headline")
===============================================================================



 This module contains experimental modules and reproductions of existing work using LangChain primitives.
 




 Autonomous Agents
 [#](#autonomous-agents "Permalink to this headline")
-------------------------------------------------------------------------



 Here, we document the BabyAGI and AutoGPT classes from the langchain.experimental module.
 




*class*


 langchain.experimental.
 



 BabyAGI
 


 (
 
*\**
 ,
 *memory
 



 :
 





 Optional
 


 [
 


 langchain.schema.BaseMemory
 


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
 





 None*
 ,
 *task_list
 



 :
 





 collections.deque
 





 =
 





 None*
 ,
 *task_creation_chain
 



 :
 





 langchain.chains.base.Chain*
 ,
 *task_prioritization_chain
 



 :
 





 langchain.chains.base.Chain*
 ,
 *execution_chain
 



 :
 





 langchain.chains.base.Chain*
 ,
 *task_id_counter
 



 :
 





 int
 





 =
 





 1*
 ,
 *vectorstore
 



 :
 




[langchain.vectorstores.base.VectorStore](vectorstores#langchain.vectorstores.VectorStore "langchain.vectorstores.base.VectorStore")*
 ,
 *max_iterations
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/experimental/autonomous_agents/baby_agi/baby_agi#BabyAGI)
[#](#langchain.experimental.BabyAGI "Permalink to this definition") 



 Controller model for the BabyAGI agent.
 




*model*


 Config
 

[[source]](../../_modules/langchain/experimental/autonomous_agents/baby_agi/baby_agi#BabyAGI.Config)
[#](#langchain.experimental.BabyAGI.Config "Permalink to this definition") 



 Configuration for this pydantic object.
 






 arbitrary_types_allowed
 

*=
 




 True*
[#](#langchain.experimental.BabyAGI.Config.arbitrary_types_allowed "Permalink to this definition") 










 execute_task
 


 (
 
*objective
 



 :
 





 str*
 ,
 *task
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 5*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/experimental/autonomous_agents/baby_agi/baby_agi#BabyAGI.execute_task)
[#](#langchain.experimental.BabyAGI.execute_task "Permalink to this definition") 



 Execute a task.
 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *vectorstore
 



 :
 




[langchain.vectorstores.base.VectorStore](vectorstores#langchain.vectorstores.VectorStore "langchain.vectorstores.base.VectorStore")*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *task_execution_chain
 



 :
 





 Optional
 


 [
 


 langchain.chains.base.Chain
 


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
 

[langchain.experimental.autonomous_agents.baby_agi.baby_agi.BabyAGI](#langchain.experimental.BabyAGI "langchain.experimental.autonomous_agents.baby_agi.baby_agi.BabyAGI")


[[source]](../../_modules/langchain/experimental/autonomous_agents/baby_agi/baby_agi#BabyAGI.from_llm)
[#](#langchain.experimental.BabyAGI.from_llm "Permalink to this definition") 



 Initialize the BabyAGI Controller.
 








 get_next_task
 


 (
 
*result
 



 :
 





 str*
 ,
 *task_description
 



 :
 





 str*
 ,
 *objective
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 Dict
 


 ]
 



[[source]](../../_modules/langchain/experimental/autonomous_agents/baby_agi/baby_agi#BabyAGI.get_next_task)
[#](#langchain.experimental.BabyAGI.get_next_task "Permalink to this definition") 



 Get the next task.
 






*property*


 input_keys
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.experimental.BabyAGI.input_keys "Permalink to this definition") 



 Input keys this chain expects.
 






*property*


 output_keys
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.experimental.BabyAGI.output_keys "Permalink to this definition") 



 Output keys this chain expects.
 








 prioritize_tasks
 


 (
 
*this_task_id
 



 :
 





 int*
 ,
 *objective
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 Dict
 


 ]
 



[[source]](../../_modules/langchain/experimental/autonomous_agents/baby_agi/baby_agi#BabyAGI.prioritize_tasks)
[#](#langchain.experimental.BabyAGI.prioritize_tasks "Permalink to this definition") 



 Prioritize tasks.
 








*class*


 langchain.experimental.
 



 AutoGPT
 


 (
 
*ai_name
 



 :
 





 str*
 ,
 *memory
 



 :
 





 langchain.vectorstores.base.VectorStoreRetriever*
 ,
 *chain
 



 :
 




[langchain.chains.llm.LLMChain](chains#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
 ,
 *output_parser
 



 :
 





 langchain.experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser*
 ,
 *tools
 



 :
 





 List
 


 [
 

[langchain.tools.base.BaseTool](tools#langchain.tools.BaseTool "langchain.tools.base.BaseTool")


 ]*
 ,
 *feedback_tool
 



 :
 





 Optional
 


 [
 

[langchain.tools.human.tool.HumanInputRun](tools#langchain.tools.HumanInputRun "langchain.tools.human.tool.HumanInputRun")


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/experimental/autonomous_agents/autogpt/agent#AutoGPT)
[#](#langchain.experimental.AutoGPT "Permalink to this definition") 



 Agent class for interacting with Auto-GPT.
 







 Generative Agents
 [#](#generative-agents "Permalink to this headline")
-------------------------------------------------------------------------



 Here, we document the GenerativeAgent and GenerativeAgentMemory classes from the langchain.experimental module.
 




*class*


 langchain.experimental.
 



 GenerativeAgent
 


 (
 
*\**
 ,
 *name
 



 :
 





 str*
 ,
 *age
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 None*
 ,
 *traits
 



 :
 





 str
 





 =
 





 'N/A'*
 ,
 *status
 



 :
 





 str*
 ,
 *memory
 



 :
 




[langchain.experimental.generative_agents.memory.GenerativeAgentMemory](#langchain.experimental.GenerativeAgentMemory "langchain.experimental.generative_agents.memory.GenerativeAgentMemory")*
 ,
 *llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *summary
 



 :
 





 str
 





 =
 





 ''*
 ,
 *summary_refresh_seconds
 



 :
 





 int
 





 =
 





 3600*
 ,
 *last_refreshed
 



 :
 





 datetime.datetime
 





 =
 





 None*
 ,
 *daily_summaries
 



 :
 





 List
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/experimental/generative_agents/generative_agent#GenerativeAgent)
[#](#langchain.experimental.GenerativeAgent "Permalink to this definition") 



 A character with memory and innate characteristics.
 




*model*


 Config
 

[[source]](../../_modules/langchain/experimental/generative_agents/generative_agent#GenerativeAgent.Config)
[#](#langchain.experimental.GenerativeAgent.Config "Permalink to this definition") 



 Configuration for this pydantic object.
 






 arbitrary_types_allowed
 

*=
 




 True*
[#](#langchain.experimental.GenerativeAgent.Config.arbitrary_types_allowed "Permalink to this definition") 








*field*


 age
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.experimental.GenerativeAgent.age "Permalink to this definition") 



 The optional age of the character.
 






*field*


 daily_summaries
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Optional]*
[#](#langchain.experimental.GenerativeAgent.daily_summaries "Permalink to this definition") 



 Summary of the events in the plan that the agent took.
 








 generate_dialogue_response
 


 (
 
*observation
 



 :
 





 str*

 )
 


 →
 


 Tuple
 


 [
 


 bool
 


 ,
 




 str
 


 ]
 



[[source]](../../_modules/langchain/experimental/generative_agents/generative_agent#GenerativeAgent.generate_dialogue_response)
[#](#langchain.experimental.GenerativeAgent.generate_dialogue_response "Permalink to this definition") 



 React to a given observation.
 








 generate_reaction
 


 (
 
*observation
 



 :
 





 str*

 )
 


 →
 


 Tuple
 


 [
 


 bool
 


 ,
 




 str
 


 ]
 



[[source]](../../_modules/langchain/experimental/generative_agents/generative_agent#GenerativeAgent.generate_reaction)
[#](#langchain.experimental.GenerativeAgent.generate_reaction "Permalink to this definition") 



 React to a given observation.
 








 get_full_header
 


 (
 
*force_refresh
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/experimental/generative_agents/generative_agent#GenerativeAgent.get_full_header)
[#](#langchain.experimental.GenerativeAgent.get_full_header "Permalink to this definition") 



 Return a full header of the agent’s status, summary, and current time.
 








 get_summary
 


 (
 
*force_refresh
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/experimental/generative_agents/generative_agent#GenerativeAgent.get_summary)
[#](#langchain.experimental.GenerativeAgent.get_summary "Permalink to this definition") 



 Return a descriptive summary of the agent.
 






*field*


 last_refreshed
 

*:
 




 datetime.datetime*
*[Optional]*
[#](#langchain.experimental.GenerativeAgent.last_refreshed "Permalink to this definition") 



 The last time the character’s summary was regenerated.
 






*field*


 llm
 

*:
 




 langchain.base_language.BaseLanguageModel*
*[Required]*
[#](#langchain.experimental.GenerativeAgent.llm "Permalink to this definition") 



 The underlying language model.
 






*field*


 memory
 

*:
 



[langchain.experimental.generative_agents.memory.GenerativeAgentMemory](#langchain.experimental.GenerativeAgentMemory "langchain.experimental.generative_agents.memory.GenerativeAgentMemory")*
*[Required]*
[#](#langchain.experimental.GenerativeAgent.memory "Permalink to this definition") 



 The memory object that combines relevance, recency, and ‘importance’.
 






*field*


 name
 

*:
 




 str*
*[Required]*
[#](#langchain.experimental.GenerativeAgent.name "Permalink to this definition") 



 The character’s name.
 






*field*


 status
 

*:
 




 str*
*[Required]*
[#](#langchain.experimental.GenerativeAgent.status "Permalink to this definition") 



 The traits of the character you wish not to change.
 








 summarize_related_memories
 


 (
 
*observation
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/experimental/generative_agents/generative_agent#GenerativeAgent.summarize_related_memories)
[#](#langchain.experimental.GenerativeAgent.summarize_related_memories "Permalink to this definition") 



 Summarize memories that are most relevant to an observation.
 






*field*


 summary
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.experimental.GenerativeAgent.summary "Permalink to this definition") 



 Stateful self-summary generated via reflection on the character’s memory.
 






*field*


 summary_refresh_seconds
 

*:
 




 int*
*=
 




 3600*
[#](#langchain.experimental.GenerativeAgent.summary_refresh_seconds "Permalink to this definition") 



 How frequently to re-generate the summary.
 






*field*


 traits
 

*:
 




 str*
*=
 




 'N/A'*
[#](#langchain.experimental.GenerativeAgent.traits "Permalink to this definition") 



 Permanent traits to ascribe to the character.
 








*class*


 langchain.experimental.
 



 GenerativeAgentMemory
 


 (
 
*\**
 ,
 *llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *memory_retriever
 



 :
 




[langchain.retrievers.time_weighted_retriever.TimeWeightedVectorStoreRetriever](retrievers#langchain.retrievers.TimeWeightedVectorStoreRetriever "langchain.retrievers.time_weighted_retriever.TimeWeightedVectorStoreRetriever")*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *reflection_threshold
 



 :
 





 Optional
 


 [
 


 float
 


 ]
 






 =
 





 None*
 ,
 *current_plan
 



 :
 





 List
 


 [
 


 str
 


 ]
 






 =
 





 []*
 ,
 *importance_weight
 



 :
 





 float
 





 =
 





 0.15*
 ,
 *aggregate_importance
 



 :
 





 float
 





 =
 





 0.0*
 ,
 *max_tokens_limit
 



 :
 





 int
 





 =
 





 1200*
 ,
 *queries_key
 



 :
 





 str
 





 =
 





 'queries'*
 ,
 *most_recent_memories_token_key
 



 :
 





 str
 





 =
 





 'recent_memories_token'*
 ,
 *add_memory_key
 



 :
 





 str
 





 =
 





 'add_memory'*
 ,
 *relevant_memories_key
 



 :
 





 str
 





 =
 





 'relevant_memories'*
 ,
 *relevant_memories_simple_key
 



 :
 





 str
 





 =
 





 'relevant_memories_simple'*
 ,
 *most_recent_memories_key
 



 :
 





 str
 





 =
 





 'most_recent_memories'*

 )
 
[[source]](../../_modules/langchain/experimental/generative_agents/memory#GenerativeAgentMemory)
[#](#langchain.experimental.GenerativeAgentMemory "Permalink to this definition") 






 add_memory
 


 (
 
*memory_content
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/experimental/generative_agents/memory#GenerativeAgentMemory.add_memory)
[#](#langchain.experimental.GenerativeAgentMemory.add_memory "Permalink to this definition") 



 Add an observation or memory to the agent’s memory.
 






*field*


 aggregate_importance
 

*:
 




 float*
*=
 




 0.0*
[#](#langchain.experimental.GenerativeAgentMemory.aggregate_importance "Permalink to this definition") 



 Track the sum of the ‘importance’ of recent memories.
 



 Triggers reflection when it reaches reflection_threshold.
 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/experimental/generative_agents/memory#GenerativeAgentMemory.clear)
[#](#langchain.experimental.GenerativeAgentMemory.clear "Permalink to this definition") 



 Clear memory contents.
 






*field*


 current_plan
 

*:
 




 List
 


 [
 


 str
 


 ]*
*=
 




 []*
[#](#langchain.experimental.GenerativeAgentMemory.current_plan "Permalink to this definition") 



 The current plan of the agent.
 








 fetch_memories
 


 (
 
*observation
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/experimental/generative_agents/memory#GenerativeAgentMemory.fetch_memories)
[#](#langchain.experimental.GenerativeAgentMemory.fetch_memories "Permalink to this definition") 



 Fetch related memories.
 






*field*


 importance_weight
 

*:
 




 float*
*=
 




 0.15*
[#](#langchain.experimental.GenerativeAgentMemory.importance_weight "Permalink to this definition") 



 How much weight to assign the memory importance.
 






*field*


 llm
 

*:
 




 langchain.base_language.BaseLanguageModel*
*[Required]*
[#](#langchain.experimental.GenerativeAgentMemory.llm "Permalink to this definition") 



 The core language model.
 








 load_memory_variables
 


 (
 
*inputs
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*

 )
 


 →
 


 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



[[source]](../../_modules/langchain/experimental/generative_agents/memory#GenerativeAgentMemory.load_memory_variables)
[#](#langchain.experimental.GenerativeAgentMemory.load_memory_variables "Permalink to this definition") 



 Return key-value pairs given the text input to the chain.
 






*field*


 memory_retriever
 

*:
 



[langchain.retrievers.time_weighted_retriever.TimeWeightedVectorStoreRetriever](retrievers#langchain.retrievers.TimeWeightedVectorStoreRetriever "langchain.retrievers.time_weighted_retriever.TimeWeightedVectorStoreRetriever")*
*[Required]*
[#](#langchain.experimental.GenerativeAgentMemory.memory_retriever "Permalink to this definition") 



 The retriever to fetch related memories.
 






*property*


 memory_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.experimental.GenerativeAgentMemory.memory_variables "Permalink to this definition") 



 Input keys this memory class will load dynamically.
 








 pause_to_reflect
 


 (
 

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/experimental/generative_agents/memory#GenerativeAgentMemory.pause_to_reflect)
[#](#langchain.experimental.GenerativeAgentMemory.pause_to_reflect "Permalink to this definition") 



 Reflect on recent observations and generate ‘insights’.
 






*field*


 reflection_threshold
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 None*
[#](#langchain.experimental.GenerativeAgentMemory.reflection_threshold "Permalink to this definition") 



 When aggregate_importance exceeds reflection_threshold, stop to reflect.
 








 save_context
 


 (
 
*inputs
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
 ,
 *outputs
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/experimental/generative_agents/memory#GenerativeAgentMemory.save_context)
[#](#langchain.experimental.GenerativeAgentMemory.save_context "Permalink to this definition") 



 Save the context of this model run to memory.
 









