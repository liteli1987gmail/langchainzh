




 Memory
 [#](#module-langchain.memory "Permalink to this headline")
====================================================================




*pydantic
 

 model*


 langchain.memory.
 



 ChatMessageHistory
 

[[source]](../../_modules/langchain/memory/chat_message_histories/in_memory#ChatMessageHistory)
[#](#langchain.memory.ChatMessageHistory "Permalink to this definition") 




*field*


 messages
 

*:
 




 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]*
*=
 




 []*
[#](#langchain.memory.ChatMessageHistory.messages "Permalink to this definition") 








 add_ai_message
 


 (
 
*message
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/in_memory#ChatMessageHistory.add_ai_message)
[#](#langchain.memory.ChatMessageHistory.add_ai_message "Permalink to this definition") 



 Add an AI message to the store
 








 add_user_message
 


 (
 
*message
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/in_memory#ChatMessageHistory.add_user_message)
[#](#langchain.memory.ChatMessageHistory.add_user_message "Permalink to this definition") 



 Add a user message to the store
 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/in_memory#ChatMessageHistory.clear)
[#](#langchain.memory.ChatMessageHistory.clear "Permalink to this definition") 



 Remove all messages from the store
 








*pydantic
 

 model*


 langchain.memory.
 



 CombinedMemory
 

[[source]](../../_modules/langchain/memory/combined#CombinedMemory)
[#](#langchain.memory.CombinedMemory "Permalink to this definition") 



 Class for combining multiple memories’ data together.
 




*field*


 memories
 

*:
 




 List
 


 [
 


 langchain.schema.BaseMemory
 


 ]*
*[Required]*
[#](#langchain.memory.CombinedMemory.memories "Permalink to this definition") 



 For tracking all the memories that should be accessed.
 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/combined#CombinedMemory.clear)
[#](#langchain.memory.CombinedMemory.clear "Permalink to this definition") 



 Clear context from this session for every memory.
 








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
 



[[source]](../../_modules/langchain/memory/combined#CombinedMemory.load_memory_variables)
[#](#langchain.memory.CombinedMemory.load_memory_variables "Permalink to this definition") 



 Load all vars from sub-memories.
 








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
 


[[source]](../../_modules/langchain/memory/combined#CombinedMemory.save_context)
[#](#langchain.memory.CombinedMemory.save_context "Permalink to this definition") 



 Save context from this session for every memory.
 






*property*


 memory_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.memory.CombinedMemory.memory_variables "Permalink to this definition") 



 All the memory variables that this instance provides.
 








*pydantic
 

 model*


 langchain.memory.
 



 ConversationBufferMemory
 

[[source]](../../_modules/langchain/memory/buffer#ConversationBufferMemory)
[#](#langchain.memory.ConversationBufferMemory "Permalink to this definition") 



 Buffer for storing conversation memory.
 




*field*


 ai_prefix
 

*:
 




 str*
*=
 




 'AI'*
[#](#langchain.memory.ConversationBufferMemory.ai_prefix "Permalink to this definition") 






*field*


 human_prefix
 

*:
 




 str*
*=
 




 'Human'*
[#](#langchain.memory.ConversationBufferMemory.human_prefix "Permalink to this definition") 








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
 




 Any
 


 ]
 



[[source]](../../_modules/langchain/memory/buffer#ConversationBufferMemory.load_memory_variables)
[#](#langchain.memory.ConversationBufferMemory.load_memory_variables "Permalink to this definition") 



 Return history buffer.
 






*property*


 buffer
 

*:
 




 Any*
[#](#langchain.memory.ConversationBufferMemory.buffer "Permalink to this definition") 



 String buffer of memory.
 








*pydantic
 

 model*


 langchain.memory.
 



 ConversationBufferWindowMemory
 

[[source]](../../_modules/langchain/memory/buffer_window#ConversationBufferWindowMemory)
[#](#langchain.memory.ConversationBufferWindowMemory "Permalink to this definition") 



 Buffer for storing conversation memory.
 




*field*


 ai_prefix
 

*:
 




 str*
*=
 




 'AI'*
[#](#langchain.memory.ConversationBufferWindowMemory.ai_prefix "Permalink to this definition") 






*field*


 human_prefix
 

*:
 




 str*
*=
 




 'Human'*
[#](#langchain.memory.ConversationBufferWindowMemory.human_prefix "Permalink to this definition") 






*field*


 k
 

*:
 




 int*
*=
 




 5*
[#](#langchain.memory.ConversationBufferWindowMemory.k "Permalink to this definition") 








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
 



[[source]](../../_modules/langchain/memory/buffer_window#ConversationBufferWindowMemory.load_memory_variables)
[#](#langchain.memory.ConversationBufferWindowMemory.load_memory_variables "Permalink to this definition") 



 Return history buffer.
 






*property*


 buffer
 

*:
 




 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]*
[#](#langchain.memory.ConversationBufferWindowMemory.buffer "Permalink to this definition") 



 String buffer of memory.
 








*pydantic
 

 model*


 langchain.memory.
 



 ConversationEntityMemory
 

[[source]](../../_modules/langchain/memory/entity#ConversationEntityMemory)
[#](#langchain.memory.ConversationEntityMemory "Permalink to this definition") 



 Entity extractor & summarizer to memory.
 




*field*


 ai_prefix
 

*:
 




 str*
*=
 




 'AI'*
[#](#langchain.memory.ConversationEntityMemory.ai_prefix "Permalink to this definition") 






*field*


 chat_history_key
 

*:
 




 str*
*=
 




 'history'*
[#](#langchain.memory.ConversationEntityMemory.chat_history_key "Permalink to this definition") 






*field*


 entity_cache
 

*:
 




 List
 


 [
 


 str
 


 ]*
*=
 




 []*
[#](#langchain.memory.ConversationEntityMemory.entity_cache "Permalink to this definition") 






*field*


 entity_extraction_prompt
 

*:
 



[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")*
*=
 




 PromptTemplate(input_variables=['history',
 

 'input'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='You
 

 are
 

 an
 

 AI
 

 assistant
 

 reading
 

 the
 

 transcript
 

 of
 

 a
 

 conversation
 

 between
 

 an
 

 AI
 

 and
 

 a
 

 human.
 

 Extract
 

 all
 

 of
 

 the
 

 proper
 

 nouns
 

 from
 

 the
 

 last
 

 line
 

 of
 

 conversation.
 

 As
 

 a
 

 guideline,
 

 a
 

 proper
 

 noun
 

 is
 

 generally
 

 capitalized.
 

 You
 

 should
 

 definitely
 

 extract
 

 all
 

 names
 

 and
 

 places.\n\nThe
 

 conversation
 

 history
 

 is
 

 provided
 

 just
 

 in
 

 case
 

 of
 

 a
 

 coreference
 

 (e.g.
 

 "What
 

 do
 

 you
 

 know
 

 about
 

 him"
 

 where
 

 "him"
 

 is
 

 defined
 

 in
 

 a
 

 previous
 

 line)
 

 --
 

 ignore
 

 items
 

 mentioned
 

 there
 

 that
 

 are
 

 not
 

 in
 

 the
 

 last
 

 line.\n\nReturn
 

 the
 

 output
 

 as
 

 a
 

 single
 

 comma-separated
 

 list,
 

 or
 

 NONE
 

 if
 

 there
 

 is
 

 nothing
 

 of
 

 note
 

 to
 

 return
 

 (e.g.
 

 the
 

 user
 

 is
 

 just
 

 issuing
 

 a
 

 greeting
 

 or
 

 having
 

 a
 

 simple
 

 conversation).\n\nEXAMPLE\nConversation
 

 history:\nPerson
 

 #1:
 

 how\'s
 

 it
 

 going
 

 today?\nAI:
 

 "It\'s
 

 going
 

 great!
 

 How
 

 about
 

 you?"\nPerson
 

 #1:
 

 good!
 

 busy
 

 working
 

 on
 

 Langchain.
 

 lots
 

 to
 

 do.\nAI:
 

 "That
 

 sounds
 

 like
 

 a
 

 lot
 

 of
 

 work!
 

 What
 

 kind
 

 of
 

 things
 

 are
 

 you
 

 doing
 

 to
 

 make
 

 Langchain
 

 better?"\nLast
 

 line:\nPerson
 

 #1:
 

 i\'m
 

 trying
 

 to
 

 improve
 

 Langchain\'s
 

 interfaces,
 

 the
 

 UX,
 

 its
 

 integrations
 

 with
 

 various
 

 products
 

 the
 

 user
 

 might
 

 want
 

 ...
 

 a
 

 lot
 

 of
 

 stuff.\nOutput:
 

 Langchain\nEND
 

 OF
 

 EXAMPLE\n\nEXAMPLE\nConversation
 

 history:\nPerson
 

 #1:
 

 how\'s
 

 it
 

 going
 

 today?\nAI:
 

 "It\'s
 

 going
 

 great!
 

 How
 

 about
 

 you?"\nPerson
 

 #1:
 

 good!
 

 busy
 

 working
 

 on
 

 Langchain.
 

 lots
 

 to
 

 do.\nAI:
 

 "That
 

 sounds
 

 like
 

 a
 

 lot
 

 of
 

 work!
 

 What
 

 kind
 

 of
 

 things
 

 are
 

 you
 

 doing
 

 to
 

 make
 

 Langchain
 

 better?"\nLast
 

 line:\nPerson
 

 #1:
 

 i\'m
 

 trying
 

 to
 

 improve
 

 Langchain\'s
 

 interfaces,
 

 the
 

 UX,
 

 its
 

 integrations
 

 with
 

 various
 

 products
 

 the
 

 user
 

 might
 

 want
 

 ...
 

 a
 

 lot
 

 of
 

 stuff.
 

 I\'m
 

 working
 

 with
 

 Person
 

 #2.\nOutput:
 

 Langchain,
 

 Person
 

 #2\nEND
 

 OF
 

 EXAMPLE\n\nConversation
 

 history
 

 (for
 

 reference
 

 only):\n{history}\nLast
 

 line
 

 of
 

 conversation
 

 (for
 

 extraction):\nHuman:
 

 {input}\n\nOutput:',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.memory.ConversationEntityMemory.entity_extraction_prompt "Permalink to this definition") 






*field*


 entity_store
 

*:
 




 langchain.memory.entity.BaseEntityStore*
*[Optional]*
[#](#langchain.memory.ConversationEntityMemory.entity_store "Permalink to this definition") 






*field*


 entity_summarization_prompt
 

*:
 



[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")*
*=
 




 PromptTemplate(input_variables=['entity',
 

 'summary',
 

 'history',
 

 'input'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='You
 

 are
 

 an
 

 AI
 

 assistant
 

 helping
 

 a
 

 human
 

 keep
 

 track
 

 of
 

 facts
 

 about
 

 relevant
 

 people,
 

 places,
 

 and
 

 concepts
 

 in
 

 their
 

 life.
 

 Update
 

 the
 

 summary
 

 of
 

 the
 

 provided
 

 entity
 

 in
 

 the
 

 "Entity"
 

 section
 

 based
 

 on
 

 the
 

 last
 

 line
 

 of
 

 your
 

 conversation
 

 with
 

 the
 

 human.
 

 If
 

 you
 

 are
 

 writing
 

 the
 

 summary
 

 for
 

 the
 

 first
 

 time,
 

 return
 

 a
 

 single
 

 sentence.\nThe
 

 update
 

 should
 

 only
 

 include
 

 facts
 

 that
 

 are
 

 relayed
 

 in
 

 the
 

 last
 

 line
 

 of
 

 conversation
 

 about
 

 the
 

 provided
 

 entity,
 

 and
 

 should
 

 only
 

 contain
 

 facts
 

 about
 

 the
 

 provided
 

 entity.\n\nIf
 

 there
 

 is
 

 no
 

 new
 

 information
 

 about
 

 the
 

 provided
 

 entity
 

 or
 

 the
 

 information
 

 is
 

 not
 

 worth
 

 noting
 

 (not
 

 an
 

 important
 

 or
 

 relevant
 

 fact
 

 to
 

 remember
 

 long-term),
 

 return
 

 the
 

 existing
 

 summary
 

 unchanged.\n\nFull
 

 conversation
 

 history
 

 (for
 

 context):\n{history}\n\nEntity
 

 to
 

 summarize:\n{entity}\n\nExisting
 

 summary
 

 of
 

 {entity}:\n{summary}\n\nLast
 

 line
 

 of
 

 conversation:\nHuman:
 

 {input}\nUpdated
 

 summary:',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.memory.ConversationEntityMemory.entity_summarization_prompt "Permalink to this definition") 






*field*


 human_prefix
 

*:
 




 str*
*=
 




 'Human'*
[#](#langchain.memory.ConversationEntityMemory.human_prefix "Permalink to this definition") 






*field*


 k
 

*:
 




 int*
*=
 




 3*
[#](#langchain.memory.ConversationEntityMemory.k "Permalink to this definition") 






*field*


 llm
 

*:
 




 langchain.base_language.BaseLanguageModel*
*[Required]*
[#](#langchain.memory.ConversationEntityMemory.llm "Permalink to this definition") 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/entity#ConversationEntityMemory.clear)
[#](#langchain.memory.ConversationEntityMemory.clear "Permalink to this definition") 



 Clear memory contents.
 








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
 




 Any
 


 ]
 



[[source]](../../_modules/langchain/memory/entity#ConversationEntityMemory.load_memory_variables)
[#](#langchain.memory.ConversationEntityMemory.load_memory_variables "Permalink to this definition") 



 Return history buffer.
 








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
 


[[source]](../../_modules/langchain/memory/entity#ConversationEntityMemory.save_context)
[#](#langchain.memory.ConversationEntityMemory.save_context "Permalink to this definition") 



 Save context from this conversation to buffer.
 






*property*


 buffer
 

*:
 




 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]*
[#](#langchain.memory.ConversationEntityMemory.buffer "Permalink to this definition") 








*pydantic
 

 model*


 langchain.memory.
 



 ConversationKGMemory
 

[[source]](../../_modules/langchain/memory/kg#ConversationKGMemory)
[#](#langchain.memory.ConversationKGMemory "Permalink to this definition") 



 Knowledge graph memory for storing conversation memory.
 



 Integrates with external knowledge graph to store and retrieve
information about knowledge triples in the conversation.
 




*field*


 ai_prefix
 

*:
 




 str*
*=
 




 'AI'*
[#](#langchain.memory.ConversationKGMemory.ai_prefix "Permalink to this definition") 






*field*


 entity_extraction_prompt
 

*:
 



[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")*
*=
 




 PromptTemplate(input_variables=['history',
 

 'input'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='You
 

 are
 

 an
 

 AI
 

 assistant
 

 reading
 

 the
 

 transcript
 

 of
 

 a
 

 conversation
 

 between
 

 an
 

 AI
 

 and
 

 a
 

 human.
 

 Extract
 

 all
 

 of
 

 the
 

 proper
 

 nouns
 

 from
 

 the
 

 last
 

 line
 

 of
 

 conversation.
 

 As
 

 a
 

 guideline,
 

 a
 

 proper
 

 noun
 

 is
 

 generally
 

 capitalized.
 

 You
 

 should
 

 definitely
 

 extract
 

 all
 

 names
 

 and
 

 places.\n\nThe
 

 conversation
 

 history
 

 is
 

 provided
 

 just
 

 in
 

 case
 

 of
 

 a
 

 coreference
 

 (e.g.
 

 "What
 

 do
 

 you
 

 know
 

 about
 

 him"
 

 where
 

 "him"
 

 is
 

 defined
 

 in
 

 a
 

 previous
 

 line)
 

 --
 

 ignore
 

 items
 

 mentioned
 

 there
 

 that
 

 are
 

 not
 

 in
 

 the
 

 last
 

 line.\n\nReturn
 

 the
 

 output
 

 as
 

 a
 

 single
 

 comma-separated
 

 list,
 

 or
 

 NONE
 

 if
 

 there
 

 is
 

 nothing
 

 of
 

 note
 

 to
 

 return
 

 (e.g.
 

 the
 

 user
 

 is
 

 just
 

 issuing
 

 a
 

 greeting
 

 or
 

 having
 

 a
 

 simple
 

 conversation).\n\nEXAMPLE\nConversation
 

 history:\nPerson
 

 #1:
 

 how\'s
 

 it
 

 going
 

 today?\nAI:
 

 "It\'s
 

 going
 

 great!
 

 How
 

 about
 

 you?"\nPerson
 

 #1:
 

 good!
 

 busy
 

 working
 

 on
 

 Langchain.
 

 lots
 

 to
 

 do.\nAI:
 

 "That
 

 sounds
 

 like
 

 a
 

 lot
 

 of
 

 work!
 

 What
 

 kind
 

 of
 

 things
 

 are
 

 you
 

 doing
 

 to
 

 make
 

 Langchain
 

 better?"\nLast
 

 line:\nPerson
 

 #1:
 

 i\'m
 

 trying
 

 to
 

 improve
 

 Langchain\'s
 

 interfaces,
 

 the
 

 UX,
 

 its
 

 integrations
 

 with
 

 various
 

 products
 

 the
 

 user
 

 might
 

 want
 

 ...
 

 a
 

 lot
 

 of
 

 stuff.\nOutput:
 

 Langchain\nEND
 

 OF
 

 EXAMPLE\n\nEXAMPLE\nConversation
 

 history:\nPerson
 

 #1:
 

 how\'s
 

 it
 

 going
 

 today?\nAI:
 

 "It\'s
 

 going
 

 great!
 

 How
 

 about
 

 you?"\nPerson
 

 #1:
 

 good!
 

 busy
 

 working
 

 on
 

 Langchain.
 

 lots
 

 to
 

 do.\nAI:
 

 "That
 

 sounds
 

 like
 

 a
 

 lot
 

 of
 

 work!
 

 What
 

 kind
 

 of
 

 things
 

 are
 

 you
 

 doing
 

 to
 

 make
 

 Langchain
 

 better?"\nLast
 

 line:\nPerson
 

 #1:
 

 i\'m
 

 trying
 

 to
 

 improve
 

 Langchain\'s
 

 interfaces,
 

 the
 

 UX,
 

 its
 

 integrations
 

 with
 

 various
 

 products
 

 the
 

 user
 

 might
 

 want
 

 ...
 

 a
 

 lot
 

 of
 

 stuff.
 

 I\'m
 

 working
 

 with
 

 Person
 

 #2.\nOutput:
 

 Langchain,
 

 Person
 

 #2\nEND
 

 OF
 

 EXAMPLE\n\nConversation
 

 history
 

 (for
 

 reference
 

 only):\n{history}\nLast
 

 line
 

 of
 

 conversation
 

 (for
 

 extraction):\nHuman:
 

 {input}\n\nOutput:',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.memory.ConversationKGMemory.entity_extraction_prompt "Permalink to this definition") 






*field*


 human_prefix
 

*:
 




 str*
*=
 




 'Human'*
[#](#langchain.memory.ConversationKGMemory.human_prefix "Permalink to this definition") 






*field*


 k
 

*:
 




 int*
*=
 




 2*
[#](#langchain.memory.ConversationKGMemory.k "Permalink to this definition") 






*field*


 kg
 

*:
 




 langchain.graphs.networkx_graph.NetworkxEntityGraph*
*[Optional]*
[#](#langchain.memory.ConversationKGMemory.kg "Permalink to this definition") 






*field*


 knowledge_extraction_prompt
 

*:
 



[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")*
*=
 




 PromptTemplate(input_variables=['history',
 

 'input'],
 

 output_parser=None,
 

 partial_variables={},
 

 template="You
 

 are
 

 a
 

 networked
 

 intelligence
 

 helping
 

 a
 

 human
 

 track
 

 knowledge
 

 triples
 

 about
 

 all
 

 relevant
 

 people,
 

 things,
 

 concepts,
 

 etc.
 

 and
 

 integrating
 

 them
 

 with
 

 your
 

 knowledge
 

 stored
 

 within
 

 your
 

 weights
 

 as
 

 well
 

 as
 

 that
 

 stored
 

 in
 

 a
 

 knowledge
 

 graph.
 

 Extract
 

 all
 

 of
 

 the
 

 knowledge
 

 triples
 

 from
 

 the
 

 last
 

 line
 

 of
 

 conversation.
 

 A
 

 knowledge
 

 triple
 

 is
 

 a
 

 clause
 

 that
 

 contains
 

 a
 

 subject,
 

 a
 

 predicate,
 

 and
 

 an
 

 object.
 

 The
 

 subject
 

 is
 

 the
 

 entity
 

 being
 

 described,
 

 the
 

 predicate
 

 is
 

 the
 

 property
 

 of
 

 the
 

 subject
 

 that
 

 is
 

 being
 

 described,
 

 and
 

 the
 

 object
 

 is
 

 the
 

 value
 

 of
 

 the
 

 property.\n\nEXAMPLE\nConversation
 

 history:\nPerson
 

 #1:
 

 Did
 

 you
 

 hear
 

 aliens
 

 landed
 

 in
 

 Area
 

 51?\nAI:
 

 No,
 

 I
 

 didn't
 

 hear
 

 that.
 

 What
 

 do
 

 you
 

 know
 

 about
 

 Area
 

 51?\nPerson
 

 #1:
 

 It's
 

 a
 

 secret
 

 military
 

 base
 

 in
 

 Nevada.\nAI:
 

 What
 

 do
 

 you
 

 know
 

 about
 

 Nevada?\nLast
 

 line
 

 of
 

 conversation:\nPerson
 

 #1:
 

 It's
 

 a
 

 state
 

 in
 

 the
 

 US.
 

 It's
 

 also
 

 the
 

 number
 

 1
 

 producer
 

 of
 

 gold
 

 in
 

 the
 

 US.\n\nOutput:
 

 (Nevada,
 

 is
 

 a,
 

 state)<|>(Nevada,
 

 is
 

 in,
 

 US)<|>(Nevada,
 

 is
 

 the
 

 number
 

 1
 

 producer
 

 of,
 

 gold)\nEND
 

 OF
 

 EXAMPLE\n\nEXAMPLE\nConversation
 

 history:\nPerson
 

 #1:
 

 Hello.\nAI:
 

 Hi!
 

 How
 

 are
 

 you?\nPerson
 

 #1:
 

 I'm
 

 good.
 

 How
 

 are
 

 you?\nAI:
 

 I'm
 

 good
 

 too.\nLast
 

 line
 

 of
 

 conversation:\nPerson
 

 #1:
 

 I'm
 

 going
 

 to
 

 the
 

 store.\n\nOutput:
 

 NONE\nEND
 

 OF
 

 EXAMPLE\n\nEXAMPLE\nConversation
 

 history:\nPerson
 

 #1:
 

 What
 

 do
 

 you
 

 know
 

 about
 

 Descartes?\nAI:
 

 Descartes
 

 was
 

 a
 

 French
 

 philosopher,
 

 mathematician,
 

 and
 

 scientist
 

 who
 

 lived
 

 in
 

 the
 

 17th
 

 century.\nPerson
 

 #1:
 

 The
 

 Descartes
 

 I'm
 

 referring
 

 to
 

 is
 

 a
 

 standup
 

 comedian
 

 and
 

 interior
 

 designer
 

 from
 

 Montreal.\nAI:
 

 Oh
 

 yes,
 

 He
 

 is
 

 a
 

 comedian
 

 and
 

 an
 

 interior
 

 designer.
 

 He
 

 has
 

 been
 

 in
 

 the
 

 industry
 

 for
 

 30
 

 years.
 

 His
 

 favorite
 

 food
 

 is
 

 baked
 

 bean
 

 pie.\nLast
 

 line
 

 of
 

 conversation:\nPerson
 

 #1:
 

 Oh
 

 huh.
 

 I
 

 know
 

 Descartes
 

 likes
 

 to
 

 drive
 

 antique
 

 scooters
 

 and
 

 play
 

 the
 

 mandolin.\nOutput:
 

 (Descartes,
 

 likes
 

 to
 

 drive,
 

 antique
 

 scooters)<|>(Descartes,
 

 plays,
 

 mandolin)\nEND
 

 OF
 

 EXAMPLE\n\nConversation
 

 history
 

 (for
 

 reference
 

 only):\n{history}\nLast
 

 line
 

 of
 

 conversation
 

 (for
 

 extraction):\nHuman:
 

 {input}\n\nOutput:",
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.memory.ConversationKGMemory.knowledge_extraction_prompt "Permalink to this definition") 






*field*


 llm
 

*:
 




 langchain.base_language.BaseLanguageModel*
*[Required]*
[#](#langchain.memory.ConversationKGMemory.llm "Permalink to this definition") 






*field*


 summary_message_cls
 

*:
 




 Type
 


 [
 


 langchain.schema.BaseMessage
 


 ]*
*=
 




 <class
 

 'langchain.schema.SystemMessage'>*
[#](#langchain.memory.ConversationKGMemory.summary_message_cls "Permalink to this definition") 



 Number of previous utterances to include in the context.
 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/kg#ConversationKGMemory.clear)
[#](#langchain.memory.ConversationKGMemory.clear "Permalink to this definition") 



 Clear memory contents.
 








 get_current_entities
 


 (
 
*input_string
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/memory/kg#ConversationKGMemory.get_current_entities)
[#](#langchain.memory.ConversationKGMemory.get_current_entities "Permalink to this definition") 








 get_knowledge_triplets
 


 (
 
*input_string
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.graphs.networkx_graph.KnowledgeTriple
 


 ]
 



[[source]](../../_modules/langchain/memory/kg#ConversationKGMemory.get_knowledge_triplets)
[#](#langchain.memory.ConversationKGMemory.get_knowledge_triplets "Permalink to this definition") 








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
 




 Any
 


 ]
 



[[source]](../../_modules/langchain/memory/kg#ConversationKGMemory.load_memory_variables)
[#](#langchain.memory.ConversationKGMemory.load_memory_variables "Permalink to this definition") 



 Return history buffer.
 








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
 


[[source]](../../_modules/langchain/memory/kg#ConversationKGMemory.save_context)
[#](#langchain.memory.ConversationKGMemory.save_context "Permalink to this definition") 



 Save context from this conversation to buffer.
 








*pydantic
 

 model*


 langchain.memory.
 



 ConversationStringBufferMemory
 

[[source]](../../_modules/langchain/memory/buffer#ConversationStringBufferMemory)
[#](#langchain.memory.ConversationStringBufferMemory "Permalink to this definition") 



 Buffer for storing conversation memory.
 




*field*


 ai_prefix
 

*:
 




 str*
*=
 




 'AI'*
[#](#langchain.memory.ConversationStringBufferMemory.ai_prefix "Permalink to this definition") 



 Prefix to use for AI generated responses.
 






*field*


 buffer
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.memory.ConversationStringBufferMemory.buffer "Permalink to this definition") 






*field*


 human_prefix
 

*:
 




 str*
*=
 




 'Human'*
[#](#langchain.memory.ConversationStringBufferMemory.human_prefix "Permalink to this definition") 






*field*


 input_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.memory.ConversationStringBufferMemory.input_key "Permalink to this definition") 






*field*


 output_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.memory.ConversationStringBufferMemory.output_key "Permalink to this definition") 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/buffer#ConversationStringBufferMemory.clear)
[#](#langchain.memory.ConversationStringBufferMemory.clear "Permalink to this definition") 



 Clear memory contents.
 








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
 



[[source]](../../_modules/langchain/memory/buffer#ConversationStringBufferMemory.load_memory_variables)
[#](#langchain.memory.ConversationStringBufferMemory.load_memory_variables "Permalink to this definition") 



 Return history buffer.
 








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
 


[[source]](../../_modules/langchain/memory/buffer#ConversationStringBufferMemory.save_context)
[#](#langchain.memory.ConversationStringBufferMemory.save_context "Permalink to this definition") 



 Save context from this conversation to buffer.
 






*property*


 memory_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.memory.ConversationStringBufferMemory.memory_variables "Permalink to this definition") 



 Will always return list of memory variables.
:meta private:
 








*pydantic
 

 model*


 langchain.memory.
 



 ConversationSummaryBufferMemory
 

[[source]](../../_modules/langchain/memory/summary_buffer#ConversationSummaryBufferMemory)
[#](#langchain.memory.ConversationSummaryBufferMemory "Permalink to this definition") 



 Buffer with summarizer for storing conversation memory.
 




*field*


 max_token_limit
 

*:
 




 int*
*=
 




 2000*
[#](#langchain.memory.ConversationSummaryBufferMemory.max_token_limit "Permalink to this definition") 






*field*


 memory_key
 

*:
 




 str*
*=
 




 'history'*
[#](#langchain.memory.ConversationSummaryBufferMemory.memory_key "Permalink to this definition") 






*field*


 moving_summary_buffer
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.memory.ConversationSummaryBufferMemory.moving_summary_buffer "Permalink to this definition") 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/summary_buffer#ConversationSummaryBufferMemory.clear)
[#](#langchain.memory.ConversationSummaryBufferMemory.clear "Permalink to this definition") 



 Clear memory contents.
 








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
 




 Any
 


 ]
 



[[source]](../../_modules/langchain/memory/summary_buffer#ConversationSummaryBufferMemory.load_memory_variables)
[#](#langchain.memory.ConversationSummaryBufferMemory.load_memory_variables "Permalink to this definition") 



 Return history buffer.
 








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
 


[[source]](../../_modules/langchain/memory/summary_buffer#ConversationSummaryBufferMemory.save_context)
[#](#langchain.memory.ConversationSummaryBufferMemory.save_context "Permalink to this definition") 



 Save context from this conversation to buffer.
 






*property*


 buffer
 

*:
 




 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]*
[#](#langchain.memory.ConversationSummaryBufferMemory.buffer "Permalink to this definition") 








*pydantic
 

 model*


 langchain.memory.
 



 ConversationSummaryMemory
 

[[source]](../../_modules/langchain/memory/summary#ConversationSummaryMemory)
[#](#langchain.memory.ConversationSummaryMemory "Permalink to this definition") 



 Conversation summarizer to memory.
 




*field*


 buffer
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.memory.ConversationSummaryMemory.buffer "Permalink to this definition") 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/summary#ConversationSummaryMemory.clear)
[#](#langchain.memory.ConversationSummaryMemory.clear "Permalink to this definition") 



 Clear memory contents.
 








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
 




 Any
 


 ]
 



[[source]](../../_modules/langchain/memory/summary#ConversationSummaryMemory.load_memory_variables)
[#](#langchain.memory.ConversationSummaryMemory.load_memory_variables "Permalink to this definition") 



 Return history buffer.
 








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
 


[[source]](../../_modules/langchain/memory/summary#ConversationSummaryMemory.save_context)
[#](#langchain.memory.ConversationSummaryMemory.save_context "Permalink to this definition") 



 Save context from this conversation to buffer.
 








*pydantic
 

 model*


 langchain.memory.
 



 ConversationTokenBufferMemory
 

[[source]](../../_modules/langchain/memory/token_buffer#ConversationTokenBufferMemory)
[#](#langchain.memory.ConversationTokenBufferMemory "Permalink to this definition") 



 Buffer for storing conversation memory.
 




*field*


 ai_prefix
 

*:
 




 str*
*=
 




 'AI'*
[#](#langchain.memory.ConversationTokenBufferMemory.ai_prefix "Permalink to this definition") 






*field*


 human_prefix
 

*:
 




 str*
*=
 




 'Human'*
[#](#langchain.memory.ConversationTokenBufferMemory.human_prefix "Permalink to this definition") 






*field*


 llm
 

*:
 




 langchain.base_language.BaseLanguageModel*
*[Required]*
[#](#langchain.memory.ConversationTokenBufferMemory.llm "Permalink to this definition") 






*field*


 max_token_limit
 

*:
 




 int*
*=
 




 2000*
[#](#langchain.memory.ConversationTokenBufferMemory.max_token_limit "Permalink to this definition") 






*field*


 memory_key
 

*:
 




 str*
*=
 




 'history'*
[#](#langchain.memory.ConversationTokenBufferMemory.memory_key "Permalink to this definition") 








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
 




 Any
 


 ]
 



[[source]](../../_modules/langchain/memory/token_buffer#ConversationTokenBufferMemory.load_memory_variables)
[#](#langchain.memory.ConversationTokenBufferMemory.load_memory_variables "Permalink to this definition") 



 Return history buffer.
 








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
 


[[source]](../../_modules/langchain/memory/token_buffer#ConversationTokenBufferMemory.save_context)
[#](#langchain.memory.ConversationTokenBufferMemory.save_context "Permalink to this definition") 



 Save context from this conversation to buffer. Pruned.
 






*property*


 buffer
 

*:
 




 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]*
[#](#langchain.memory.ConversationTokenBufferMemory.buffer "Permalink to this definition") 



 String buffer of memory.
 








*class*


 langchain.memory.
 



 CosmosDBChatMessageHistory
 


 (
 
*cosmos_endpoint
 



 :
 





 str*
 ,
 *cosmos_database
 



 :
 





 str*
 ,
 *cosmos_container
 



 :
 





 str*
 ,
 *credential
 



 :
 





 Any*
 ,
 *session_id
 



 :
 





 str*
 ,
 *user_id
 



 :
 





 str*
 ,
 *ttl
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/memory/chat_message_histories/cosmos_db#CosmosDBChatMessageHistory)
[#](#langchain.memory.CosmosDBChatMessageHistory "Permalink to this definition") 



 Chat history backed by Azure CosmosDB.
 






 add_ai_message
 


 (
 
*message
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/cosmos_db#CosmosDBChatMessageHistory.add_ai_message)
[#](#langchain.memory.CosmosDBChatMessageHistory.add_ai_message "Permalink to this definition") 



 Add a AI message to the memory.
 








 add_user_message
 


 (
 
*message
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/cosmos_db#CosmosDBChatMessageHistory.add_user_message)
[#](#langchain.memory.CosmosDBChatMessageHistory.add_user_message "Permalink to this definition") 



 Add a user message to the memory.
 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/cosmos_db#CosmosDBChatMessageHistory.clear)
[#](#langchain.memory.CosmosDBChatMessageHistory.clear "Permalink to this definition") 



 Clear session memory from this memory and cosmos.
 








 load_messages
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/cosmos_db#CosmosDBChatMessageHistory.load_messages)
[#](#langchain.memory.CosmosDBChatMessageHistory.load_messages "Permalink to this definition") 



 Retrieve the messages from Cosmos
 








 messages
 

*:
 




 List
 


 [
 


 BaseMessage
 


 ]*
[#](#langchain.memory.CosmosDBChatMessageHistory.messages "Permalink to this definition") 








 prepare_cosmos
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/cosmos_db#CosmosDBChatMessageHistory.prepare_cosmos)
[#](#langchain.memory.CosmosDBChatMessageHistory.prepare_cosmos "Permalink to this definition") 



 Prepare the CosmosDB client.
 



 Use this function or the context manager to make sure your database is ready.
 








 upsert_messages
 


 (
 
*new_message
 



 :
 





 Optional
 


 [
 


 langchain.schema.BaseMessage
 


 ]
 






 =
 





 None*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/cosmos_db#CosmosDBChatMessageHistory.upsert_messages)
[#](#langchain.memory.CosmosDBChatMessageHistory.upsert_messages "Permalink to this definition") 



 Update the cosmosdb item.
 








*class*


 langchain.memory.
 



 DynamoDBChatMessageHistory
 


 (
 
*table_name
 



 :
 





 str*
 ,
 *session_id
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/memory/chat_message_histories/dynamodb#DynamoDBChatMessageHistory)
[#](#langchain.memory.DynamoDBChatMessageHistory "Permalink to this definition") 



 Chat message history that stores history in AWS DynamoDB.
This class expects that a DynamoDB table with name
 
 table_name
 
 and a partition Key of
 
 SessionId
 
 is present.
 




 Parameters
 

* **table_name** 
 – name of the DynamoDB table
* **session_id** 
 – arbitrary key that is used to store the messages
of a single chat session.








 add_ai_message
 


 (
 
*message
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/dynamodb#DynamoDBChatMessageHistory.add_ai_message)
[#](#langchain.memory.DynamoDBChatMessageHistory.add_ai_message "Permalink to this definition") 



 Add an AI message to the store
 








 add_user_message
 


 (
 
*message
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/dynamodb#DynamoDBChatMessageHistory.add_user_message)
[#](#langchain.memory.DynamoDBChatMessageHistory.add_user_message "Permalink to this definition") 



 Add a user message to the store
 








 append
 


 (
 
*message
 



 :
 





 langchain.schema.BaseMessage*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/dynamodb#DynamoDBChatMessageHistory.append)
[#](#langchain.memory.DynamoDBChatMessageHistory.append "Permalink to this definition") 



 Append the message to the record in DynamoDB
 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/dynamodb#DynamoDBChatMessageHistory.clear)
[#](#langchain.memory.DynamoDBChatMessageHistory.clear "Permalink to this definition") 



 Clear session memory from DynamoDB
 






*property*


 messages
 

*:
 




 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]*
[#](#langchain.memory.DynamoDBChatMessageHistory.messages "Permalink to this definition") 



 Retrieve the messages from DynamoDB
 








*class*


 langchain.memory.
 



 InMemoryEntityStore
 

[[source]](../../_modules/langchain/memory/entity#InMemoryEntityStore)
[#](#langchain.memory.InMemoryEntityStore "Permalink to this definition") 



 Basic in-memory entity store.
 






 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/entity#InMemoryEntityStore.clear)
[#](#langchain.memory.InMemoryEntityStore.clear "Permalink to this definition") 



 Delete all entities from store.
 








 delete
 


 (
 
*key
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/entity#InMemoryEntityStore.delete)
[#](#langchain.memory.InMemoryEntityStore.delete "Permalink to this definition") 



 Delete entity value from store.
 








 exists
 


 (
 
*key
 



 :
 





 str*

 )
 


 →
 


 bool
 


[[source]](../../_modules/langchain/memory/entity#InMemoryEntityStore.exists)
[#](#langchain.memory.InMemoryEntityStore.exists "Permalink to this definition") 



 Check if entity exists in store.
 








 get
 


 (
 
*key
 



 :
 





 str*
 ,
 *default
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 


 →
 


 Optional
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/memory/entity#InMemoryEntityStore.get)
[#](#langchain.memory.InMemoryEntityStore.get "Permalink to this definition") 



 Get entity value from store.
 








 set
 


 (
 
*key
 



 :
 





 str*
 ,
 *value
 



 :
 





 Optional
 


 [
 


 str
 


 ]*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/entity#InMemoryEntityStore.set)
[#](#langchain.memory.InMemoryEntityStore.set "Permalink to this definition") 



 Set entity value in store.
 








 store
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 Optional
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 {}*
[#](#langchain.memory.InMemoryEntityStore.store "Permalink to this definition") 








*class*


 langchain.memory.
 



 PostgresChatMessageHistory
 


 (
 
*session_id
 



 :
 





 str*
 ,
 *connection_string
 



 :
 





 str
 





 =
 





 'postgresql://postgres:mypassword@localhost/chat_history'*
 ,
 *table_name
 



 :
 





 str
 





 =
 





 'message_store'*

 )
 
[[source]](../../_modules/langchain/memory/chat_message_histories/postgres#PostgresChatMessageHistory)
[#](#langchain.memory.PostgresChatMessageHistory "Permalink to this definition") 






 add_ai_message
 


 (
 
*message
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/postgres#PostgresChatMessageHistory.add_ai_message)
[#](#langchain.memory.PostgresChatMessageHistory.add_ai_message "Permalink to this definition") 



 Add an AI message to the store
 








 add_user_message
 


 (
 
*message
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/postgres#PostgresChatMessageHistory.add_user_message)
[#](#langchain.memory.PostgresChatMessageHistory.add_user_message "Permalink to this definition") 



 Add a user message to the store
 








 append
 


 (
 
*message
 



 :
 





 langchain.schema.BaseMessage*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/postgres#PostgresChatMessageHistory.append)
[#](#langchain.memory.PostgresChatMessageHistory.append "Permalink to this definition") 



 Append the message to the record in PostgreSQL
 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/postgres#PostgresChatMessageHistory.clear)
[#](#langchain.memory.PostgresChatMessageHistory.clear "Permalink to this definition") 



 Clear session memory from PostgreSQL
 






*property*


 messages
 

*:
 




 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]*
[#](#langchain.memory.PostgresChatMessageHistory.messages "Permalink to this definition") 



 Retrieve the messages from PostgreSQL
 








*pydantic
 

 model*


 langchain.memory.
 



 ReadOnlySharedMemory
 

[[source]](../../_modules/langchain/memory/readonly#ReadOnlySharedMemory)
[#](#langchain.memory.ReadOnlySharedMemory "Permalink to this definition") 



 A memory wrapper that is read-only and cannot be changed.
 




*field*


 memory
 

*:
 




 langchain.schema.BaseMemory*
*[Required]*
[#](#langchain.memory.ReadOnlySharedMemory.memory "Permalink to this definition") 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/readonly#ReadOnlySharedMemory.clear)
[#](#langchain.memory.ReadOnlySharedMemory.clear "Permalink to this definition") 



 Nothing to clear, got a memory like a vault.
 








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
 



[[source]](../../_modules/langchain/memory/readonly#ReadOnlySharedMemory.load_memory_variables)
[#](#langchain.memory.ReadOnlySharedMemory.load_memory_variables "Permalink to this definition") 



 Load memory variables from memory.
 








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
 


[[source]](../../_modules/langchain/memory/readonly#ReadOnlySharedMemory.save_context)
[#](#langchain.memory.ReadOnlySharedMemory.save_context "Permalink to this definition") 



 Nothing should be saved or changed
 






*property*


 memory_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.memory.ReadOnlySharedMemory.memory_variables "Permalink to this definition") 



 Return memory variables.
 








*class*


 langchain.memory.
 



 RedisChatMessageHistory
 


 (
 
*session_id
 



 :
 





 str*
 ,
 *url
 



 :
 





 str
 





 =
 





 'redis://localhost:6379/0'*
 ,
 *key_prefix
 



 :
 





 str
 





 =
 





 'message_store:'*
 ,
 *ttl
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/memory/chat_message_histories/redis#RedisChatMessageHistory)
[#](#langchain.memory.RedisChatMessageHistory "Permalink to this definition") 






 add_ai_message
 


 (
 
*message
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/redis#RedisChatMessageHistory.add_ai_message)
[#](#langchain.memory.RedisChatMessageHistory.add_ai_message "Permalink to this definition") 



 Add an AI message to the store
 








 add_user_message
 


 (
 
*message
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/redis#RedisChatMessageHistory.add_user_message)
[#](#langchain.memory.RedisChatMessageHistory.add_user_message "Permalink to this definition") 



 Add a user message to the store
 








 append
 


 (
 
*message
 



 :
 





 langchain.schema.BaseMessage*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/redis#RedisChatMessageHistory.append)
[#](#langchain.memory.RedisChatMessageHistory.append "Permalink to this definition") 



 Append the message to the record in Redis
 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/chat_message_histories/redis#RedisChatMessageHistory.clear)
[#](#langchain.memory.RedisChatMessageHistory.clear "Permalink to this definition") 



 Clear session memory from Redis
 






*property*


 key
 

*:
 




 str*
[#](#langchain.memory.RedisChatMessageHistory.key "Permalink to this definition") 



 Construct the record key to use
 






*property*


 messages
 

*:
 




 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]*
[#](#langchain.memory.RedisChatMessageHistory.messages "Permalink to this definition") 



 Retrieve the messages from Redis
 








*class*


 langchain.memory.
 



 RedisEntityStore
 


 (
 
*session_id
 



 :
 





 str
 





 =
 





 'default'*
 ,
 *url
 



 :
 





 str
 





 =
 





 'redis://localhost:6379/0'*
 ,
 *key_prefix
 



 :
 





 str
 





 =
 





 'memory_store'*
 ,
 *ttl
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 86400*
 ,
 *recall_ttl
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 259200*
 ,
 *\*
 



 args
 



 :
 





 Any*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/memory/entity#RedisEntityStore)
[#](#langchain.memory.RedisEntityStore "Permalink to this definition") 



 Redis-backed Entity store. Entities get a TTL of 1 day by default, and
that TTL is extended by 3 days every time the entity is read back.
 






 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/entity#RedisEntityStore.clear)
[#](#langchain.memory.RedisEntityStore.clear "Permalink to this definition") 



 Delete all entities from store.
 








 delete
 


 (
 
*key
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/entity#RedisEntityStore.delete)
[#](#langchain.memory.RedisEntityStore.delete "Permalink to this definition") 



 Delete entity value from store.
 








 exists
 


 (
 
*key
 



 :
 





 str*

 )
 


 →
 


 bool
 


[[source]](../../_modules/langchain/memory/entity#RedisEntityStore.exists)
[#](#langchain.memory.RedisEntityStore.exists "Permalink to this definition") 



 Check if entity exists in store.
 






*property*


 full_key_prefix
 

*:
 




 str*
[#](#langchain.memory.RedisEntityStore.full_key_prefix "Permalink to this definition") 








 get
 


 (
 
*key
 



 :
 





 str*
 ,
 *default
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 


 →
 


 Optional
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/memory/entity#RedisEntityStore.get)
[#](#langchain.memory.RedisEntityStore.get "Permalink to this definition") 



 Get entity value from store.
 








 key_prefix
 

*:
 




 str*
*=
 




 'memory_store'*
[#](#langchain.memory.RedisEntityStore.key_prefix "Permalink to this definition") 








 recall_ttl
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 259200*
[#](#langchain.memory.RedisEntityStore.recall_ttl "Permalink to this definition") 








 redis_client
 

*:
 




 Any*
[#](#langchain.memory.RedisEntityStore.redis_client "Permalink to this definition") 








 session_id
 

*:
 




 str*
*=
 




 'default'*
[#](#langchain.memory.RedisEntityStore.session_id "Permalink to this definition") 








 set
 


 (
 
*key
 



 :
 





 str*
 ,
 *value
 



 :
 





 Optional
 


 [
 


 str
 


 ]*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/entity#RedisEntityStore.set)
[#](#langchain.memory.RedisEntityStore.set "Permalink to this definition") 



 Set entity value in store.
 








 ttl
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 86400*
[#](#langchain.memory.RedisEntityStore.ttl "Permalink to this definition") 








*pydantic
 

 model*


 langchain.memory.
 



 SimpleMemory
 

[[source]](../../_modules/langchain/memory/simple#SimpleMemory)
[#](#langchain.memory.SimpleMemory "Permalink to this definition") 



 Simple memory for storing context or other bits of information that shouldn’t
ever change between prompts.
 




*field*


 memories
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
*=
 




 {}*
[#](#langchain.memory.SimpleMemory.memories "Permalink to this definition") 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/simple#SimpleMemory.clear)
[#](#langchain.memory.SimpleMemory.clear "Permalink to this definition") 



 Nothing to clear, got a memory like a vault.
 








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
 



[[source]](../../_modules/langchain/memory/simple#SimpleMemory.load_memory_variables)
[#](#langchain.memory.SimpleMemory.load_memory_variables "Permalink to this definition") 



 Return key-value pairs given the text input to the chain.
 



 If None, return all memories
 








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
 


[[source]](../../_modules/langchain/memory/simple#SimpleMemory.save_context)
[#](#langchain.memory.SimpleMemory.save_context "Permalink to this definition") 



 Nothing should be saved or changed, my memory is set in stone.
 






*property*


 memory_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.memory.SimpleMemory.memory_variables "Permalink to this definition") 



 Input keys this memory class will load dynamically.
 








*pydantic
 

 model*


 langchain.memory.
 



 VectorStoreRetrieverMemory
 

[[source]](../../_modules/langchain/memory/vectorstore#VectorStoreRetrieverMemory)
[#](#langchain.memory.VectorStoreRetrieverMemory "Permalink to this definition") 



 Class for a VectorStore-backed memory object.
 




*field*


 input_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.memory.VectorStoreRetrieverMemory.input_key "Permalink to this definition") 



 Key name to index the inputs to load_memory_variables.
 






*field*


 memory_key
 

*:
 




 str*
*=
 




 'history'*
[#](#langchain.memory.VectorStoreRetrieverMemory.memory_key "Permalink to this definition") 



 Key name to locate the memories in the result of load_memory_variables.
 






*field*


 retriever
 

*:
 




 langchain.vectorstores.base.VectorStoreRetriever*
*[Required]*
[#](#langchain.memory.VectorStoreRetrieverMemory.retriever "Permalink to this definition") 



 VectorStoreRetriever object to connect to.
 






*field*


 return_docs
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.memory.VectorStoreRetrieverMemory.return_docs "Permalink to this definition") 



 Whether or not to return the result of querying the database directly.
 








 clear
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/memory/vectorstore#VectorStoreRetrieverMemory.clear)
[#](#langchain.memory.VectorStoreRetrieverMemory.clear "Permalink to this definition") 



 Nothing to clear.
 








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
 




 Union
 


 [
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



 ,
 




 str
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/memory/vectorstore#VectorStoreRetrieverMemory.load_memory_variables)
[#](#langchain.memory.VectorStoreRetrieverMemory.load_memory_variables "Permalink to this definition") 



 Return history buffer.
 








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
 


[[source]](../../_modules/langchain/memory/vectorstore#VectorStoreRetrieverMemory.save_context)
[#](#langchain.memory.VectorStoreRetrieverMemory.save_context "Permalink to this definition") 



 Save context from this conversation to buffer.
 






*property*


 memory_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.memory.VectorStoreRetrieverMemory.memory_variables "Permalink to this definition") 



 The list of keys emitted from the load_memory_variables method.
 








