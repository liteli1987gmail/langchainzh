




 Output Parsers
 [#](#module-langchain.output_parsers "Permalink to this headline")
====================================================================================




*pydantic
 

 model*


 langchain.output_parsers.
 



 CommaSeparatedListOutputParser
 

[[source]](../../_modules/langchain/output_parsers/list#CommaSeparatedListOutputParser)
[#](#langchain.output_parsers.CommaSeparatedListOutputParser "Permalink to this definition") 



 Parse out comma separated lists.
 






 get_format_instructions
 


 (
 

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/output_parsers/list#CommaSeparatedListOutputParser.get_format_instructions)
[#](#langchain.output_parsers.CommaSeparatedListOutputParser.get_format_instructions "Permalink to this definition") 



 Instructions on how the LLM output should be formatted.
 








 parse
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/output_parsers/list#CommaSeparatedListOutputParser.parse)
[#](#langchain.output_parsers.CommaSeparatedListOutputParser.parse "Permalink to this definition") 



 Parse the output of an LLM call.
 








*pydantic
 

 model*


 langchain.output_parsers.
 



 GuardrailsOutputParser
 

[[source]](../../_modules/langchain/output_parsers/rail_parser#GuardrailsOutputParser)
[#](#langchain.output_parsers.GuardrailsOutputParser "Permalink to this definition") 




*field*


 guard
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.output_parsers.GuardrailsOutputParser.guard "Permalink to this definition") 






*classmethod*


 from_rail
 


 (
 
*rail_file
 



 :
 





 str*
 ,
 *num_reasks
 



 :
 





 int
 





 =
 





 1*

 )
 


 →
 

[langchain.output_parsers.rail_parser.GuardrailsOutputParser](#langchain.output_parsers.GuardrailsOutputParser "langchain.output_parsers.rail_parser.GuardrailsOutputParser")


[[source]](../../_modules/langchain/output_parsers/rail_parser#GuardrailsOutputParser.from_rail)
[#](#langchain.output_parsers.GuardrailsOutputParser.from_rail "Permalink to this definition") 






*classmethod*


 from_rail_string
 


 (
 
*rail_str
 



 :
 





 str*
 ,
 *num_reasks
 



 :
 





 int
 





 =
 





 1*

 )
 


 →
 

[langchain.output_parsers.rail_parser.GuardrailsOutputParser](#langchain.output_parsers.GuardrailsOutputParser "langchain.output_parsers.rail_parser.GuardrailsOutputParser")


[[source]](../../_modules/langchain/output_parsers/rail_parser#GuardrailsOutputParser.from_rail_string)
[#](#langchain.output_parsers.GuardrailsOutputParser.from_rail_string "Permalink to this definition") 








 get_format_instructions
 


 (
 

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/output_parsers/rail_parser#GuardrailsOutputParser.get_format_instructions)
[#](#langchain.output_parsers.GuardrailsOutputParser.get_format_instructions "Permalink to this definition") 



 Instructions on how the LLM output should be formatted.
 








 parse
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 Dict
 


[[source]](../../_modules/langchain/output_parsers/rail_parser#GuardrailsOutputParser.parse)
[#](#langchain.output_parsers.GuardrailsOutputParser.parse "Permalink to this definition") 



 Parse the output of an LLM call.
 



 A method which takes in a string (assumed output of language model )
and parses it into some structure.
 




 Parameters
 


**text** 
 – output of language model
 




 Returns
 


 structured output
 










*pydantic
 

 model*


 langchain.output_parsers.
 



 ListOutputParser
 

[[source]](../../_modules/langchain/output_parsers/list#ListOutputParser)
[#](#langchain.output_parsers.ListOutputParser "Permalink to this definition") 



 Class to parse the output of an LLM call to a list.
 




*abstract*


 parse
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/output_parsers/list#ListOutputParser.parse)
[#](#langchain.output_parsers.ListOutputParser.parse "Permalink to this definition") 



 Parse the output of an LLM call.
 








*pydantic
 

 model*


 langchain.output_parsers.
 



 OutputFixingParser
 

[[source]](../../_modules/langchain/output_parsers/fix#OutputFixingParser)
[#](#langchain.output_parsers.OutputFixingParser "Permalink to this definition") 



 Wraps a parser and tries to fix parsing errors.
 




*field*


 parser
 

*:
 




 langchain.schema.BaseOutputParser
 


 [
 


 langchain.output_parsers.fix.T
 


 ]*
*[Required]*
[#](#langchain.output_parsers.OutputFixingParser.parser "Permalink to this definition") 






*field*


 retry_chain
 

*:
 



[langchain.chains.llm.LLMChain](chains#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
*[Required]*
[#](#langchain.output_parsers.OutputFixingParser.retry_chain "Permalink to this definition") 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *parser
 



 :
 





 langchain.schema.BaseOutputParser
 


 [
 


 langchain.output_parsers.fix.T
 


 ]*
 ,
 *prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['completion',
 

 'error',
 

 'instructions'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Instructions:\n--------------\n{instructions}\n--------------\nCompletion:\n--------------\n{completion}\n--------------\n\nAbove,
 

 the
 

 Completion
 

 did
 

 not
 

 satisfy
 

 the
 

 constraints
 

 given
 

 in
 

 the
 

 Instructions.\nError:\n--------------\n{error}\n--------------\n\nPlease
 

 try
 

 again.
 

 Please
 

 only
 

 respond
 

 with
 

 an
 

 answer
 

 that
 

 satisfies
 

 the
 

 constraints
 

 laid
 

 out
 

 in
 

 the
 

 Instructions:',
 

 template_format='f-string',
 

 validate_template=True)*

 )
 


 →
 

[langchain.output_parsers.fix.OutputFixingParser](#langchain.output_parsers.OutputFixingParser "langchain.output_parsers.fix.OutputFixingParser")


 [
 


 langchain.output_parsers.fix.T
 


 ]
 



[[source]](../../_modules/langchain/output_parsers/fix#OutputFixingParser.from_llm)
[#](#langchain.output_parsers.OutputFixingParser.from_llm "Permalink to this definition") 








 get_format_instructions
 


 (
 

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/output_parsers/fix#OutputFixingParser.get_format_instructions)
[#](#langchain.output_parsers.OutputFixingParser.get_format_instructions "Permalink to this definition") 



 Instructions on how the LLM output should be formatted.
 








 parse
 


 (
 
*completion
 



 :
 





 str*

 )
 


 →
 


 langchain.output_parsers.fix.T
 


[[source]](../../_modules/langchain/output_parsers/fix#OutputFixingParser.parse)
[#](#langchain.output_parsers.OutputFixingParser.parse "Permalink to this definition") 



 Parse the output of an LLM call.
 



 A method which takes in a string (assumed output of language model )
and parses it into some structure.
 




 Parameters
 


**text** 
 – output of language model
 




 Returns
 


 structured output
 










*pydantic
 

 model*


 langchain.output_parsers.
 



 PydanticOutputParser
 

[[source]](../../_modules/langchain/output_parsers/pydantic#PydanticOutputParser)
[#](#langchain.output_parsers.PydanticOutputParser "Permalink to this definition") 




*field*


 pydantic_object
 

*:
 




 Type
 


 [
 


 langchain.output_parsers.pydantic.T
 


 ]*
*[Required]*
[#](#langchain.output_parsers.PydanticOutputParser.pydantic_object "Permalink to this definition") 








 get_format_instructions
 


 (
 

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/output_parsers/pydantic#PydanticOutputParser.get_format_instructions)
[#](#langchain.output_parsers.PydanticOutputParser.get_format_instructions "Permalink to this definition") 



 Instructions on how the LLM output should be formatted.
 








 parse
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 langchain.output_parsers.pydantic.T
 


[[source]](../../_modules/langchain/output_parsers/pydantic#PydanticOutputParser.parse)
[#](#langchain.output_parsers.PydanticOutputParser.parse "Permalink to this definition") 



 Parse the output of an LLM call.
 



 A method which takes in a string (assumed output of language model )
and parses it into some structure.
 




 Parameters
 


**text** 
 – output of language model
 




 Returns
 


 structured output
 










*pydantic
 

 model*


 langchain.output_parsers.
 



 RegexDictParser
 

[[source]](../../_modules/langchain/output_parsers/regex_dict#RegexDictParser)
[#](#langchain.output_parsers.RegexDictParser "Permalink to this definition") 



 Class to parse the output into a dictionary.
 




*field*


 no_update_value
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.output_parsers.RegexDictParser.no_update_value "Permalink to this definition") 






*field*


 output_key_to_format
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]*
*[Required]*
[#](#langchain.output_parsers.RegexDictParser.output_key_to_format "Permalink to this definition") 






*field*


 regex_pattern
 

*:
 




 str*
*=
 




 "{}:\\s?([^.'\\n']\*)\\.?"*
[#](#langchain.output_parsers.RegexDictParser.regex_pattern "Permalink to this definition") 








 parse
 


 (
 
*text
 



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
 



[[source]](../../_modules/langchain/output_parsers/regex_dict#RegexDictParser.parse)
[#](#langchain.output_parsers.RegexDictParser.parse "Permalink to this definition") 



 Parse the output of an LLM call.
 








*pydantic
 

 model*


 langchain.output_parsers.
 



 RegexParser
 

[[source]](../../_modules/langchain/output_parsers/regex#RegexParser)
[#](#langchain.output_parsers.RegexParser "Permalink to this definition") 



 Class to parse the output into a dictionary.
 




*field*


 default_output_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.output_parsers.RegexParser.default_output_key "Permalink to this definition") 






*field*


 output_keys
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Required]*
[#](#langchain.output_parsers.RegexParser.output_keys "Permalink to this definition") 






*field*


 regex
 

*:
 




 str*
*[Required]*
[#](#langchain.output_parsers.RegexParser.regex "Permalink to this definition") 








 parse
 


 (
 
*text
 



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
 



[[source]](../../_modules/langchain/output_parsers/regex#RegexParser.parse)
[#](#langchain.output_parsers.RegexParser.parse "Permalink to this definition") 



 Parse the output of an LLM call.
 








*pydantic
 

 model*


 langchain.output_parsers.
 



 ResponseSchema
 

[[source]](../../_modules/langchain/output_parsers/structured#ResponseSchema)
[#](#langchain.output_parsers.ResponseSchema "Permalink to this definition") 




*field*


 description
 

*:
 




 str*
*[Required]*
[#](#langchain.output_parsers.ResponseSchema.description "Permalink to this definition") 






*field*


 name
 

*:
 




 str*
*[Required]*
[#](#langchain.output_parsers.ResponseSchema.name "Permalink to this definition") 








*pydantic
 

 model*


 langchain.output_parsers.
 



 RetryOutputParser
 

[[source]](../../_modules/langchain/output_parsers/retry#RetryOutputParser)
[#](#langchain.output_parsers.RetryOutputParser "Permalink to this definition") 



 Wraps a parser and tries to fix parsing errors.
 



 Does this by passing the original prompt and the completion to another
LLM, and telling it the completion did not satisfy criteria in the prompt.
 




*field*


 parser
 

*:
 




 langchain.schema.BaseOutputParser
 


 [
 


 langchain.output_parsers.retry.T
 


 ]*
*[Required]*
[#](#langchain.output_parsers.RetryOutputParser.parser "Permalink to this definition") 






*field*


 retry_chain
 

*:
 



[langchain.chains.llm.LLMChain](chains#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
*[Required]*
[#](#langchain.output_parsers.RetryOutputParser.retry_chain "Permalink to this definition") 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *parser
 



 :
 





 langchain.schema.BaseOutputParser
 


 [
 


 langchain.output_parsers.retry.T
 


 ]*
 ,
 *prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['completion',
 

 'prompt'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Prompt:\n{prompt}\nCompletion:\n{completion}\n\nAbove,
 

 the
 

 Completion
 

 did
 

 not
 

 satisfy
 

 the
 

 constraints
 

 given
 

 in
 

 the
 

 Prompt.\nPlease
 

 try
 

 again:',
 

 template_format='f-string',
 

 validate_template=True)*

 )
 


 →
 

[langchain.output_parsers.retry.RetryOutputParser](#langchain.output_parsers.RetryOutputParser "langchain.output_parsers.retry.RetryOutputParser")


 [
 


 langchain.output_parsers.retry.T
 


 ]
 



[[source]](../../_modules/langchain/output_parsers/retry#RetryOutputParser.from_llm)
[#](#langchain.output_parsers.RetryOutputParser.from_llm "Permalink to this definition") 








 get_format_instructions
 


 (
 

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/output_parsers/retry#RetryOutputParser.get_format_instructions)
[#](#langchain.output_parsers.RetryOutputParser.get_format_instructions "Permalink to this definition") 



 Instructions on how the LLM output should be formatted.
 








 parse
 


 (
 
*completion
 



 :
 





 str*

 )
 


 →
 


 langchain.output_parsers.retry.T
 


[[source]](../../_modules/langchain/output_parsers/retry#RetryOutputParser.parse)
[#](#langchain.output_parsers.RetryOutputParser.parse "Permalink to this definition") 



 Parse the output of an LLM call.
 



 A method which takes in a string (assumed output of language model )
and parses it into some structure.
 




 Parameters
 


**text** 
 – output of language model
 




 Returns
 


 structured output
 










 parse_with_prompt
 


 (
 
*completion
 



 :
 





 str*
 ,
 *prompt_value
 



 :
 





 langchain.schema.PromptValue*

 )
 


 →
 


 langchain.output_parsers.retry.T
 


[[source]](../../_modules/langchain/output_parsers/retry#RetryOutputParser.parse_with_prompt)
[#](#langchain.output_parsers.RetryOutputParser.parse_with_prompt "Permalink to this definition") 



 Optional method to parse the output of an LLM call with a prompt.
 



 The prompt is largely provided in the event the OutputParser wants
to retry or fix the output in some way, and needs information from
the prompt to do so.
 




 Parameters
 

* **completion** 
 – output of language model
* **prompt** 
 – prompt value




 Returns
 


 structured output
 










*pydantic
 

 model*


 langchain.output_parsers.
 



 RetryWithErrorOutputParser
 

[[source]](../../_modules/langchain/output_parsers/retry#RetryWithErrorOutputParser)
[#](#langchain.output_parsers.RetryWithErrorOutputParser "Permalink to this definition") 



 Wraps a parser and tries to fix parsing errors.
 



 Does this by passing the original prompt, the completion, AND the error
that was raised to another language and telling it that the completion
did not work, and raised the given error. Differs from RetryOutputParser
in that this implementation provides the error that was raised back to the
LLM, which in theory should give it more information on how to fix it.
 




*field*


 parser
 

*:
 




 langchain.schema.BaseOutputParser
 


 [
 


 langchain.output_parsers.retry.T
 


 ]*
*[Required]*
[#](#langchain.output_parsers.RetryWithErrorOutputParser.parser "Permalink to this definition") 






*field*


 retry_chain
 

*:
 



[langchain.chains.llm.LLMChain](chains#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
*[Required]*
[#](#langchain.output_parsers.RetryWithErrorOutputParser.retry_chain "Permalink to this definition") 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *parser
 



 :
 





 langchain.schema.BaseOutputParser
 


 [
 


 langchain.output_parsers.retry.T
 


 ]*
 ,
 *prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['completion',
 

 'error',
 

 'prompt'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Prompt:\n{prompt}\nCompletion:\n{completion}\n\nAbove,
 

 the
 

 Completion
 

 did
 

 not
 

 satisfy
 

 the
 

 constraints
 

 given
 

 in
 

 the
 

 Prompt.\nDetails:
 

 {error}\nPlease
 

 try
 

 again:',
 

 template_format='f-string',
 

 validate_template=True)*

 )
 


 →
 

[langchain.output_parsers.retry.RetryWithErrorOutputParser](#langchain.output_parsers.RetryWithErrorOutputParser "langchain.output_parsers.retry.RetryWithErrorOutputParser")


 [
 


 langchain.output_parsers.retry.T
 


 ]
 



[[source]](../../_modules/langchain/output_parsers/retry#RetryWithErrorOutputParser.from_llm)
[#](#langchain.output_parsers.RetryWithErrorOutputParser.from_llm "Permalink to this definition") 








 get_format_instructions
 


 (
 

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/output_parsers/retry#RetryWithErrorOutputParser.get_format_instructions)
[#](#langchain.output_parsers.RetryWithErrorOutputParser.get_format_instructions "Permalink to this definition") 



 Instructions on how the LLM output should be formatted.
 








 parse
 


 (
 
*completion
 



 :
 





 str*

 )
 


 →
 


 langchain.output_parsers.retry.T
 


[[source]](../../_modules/langchain/output_parsers/retry#RetryWithErrorOutputParser.parse)
[#](#langchain.output_parsers.RetryWithErrorOutputParser.parse "Permalink to this definition") 



 Parse the output of an LLM call.
 



 A method which takes in a string (assumed output of language model )
and parses it into some structure.
 




 Parameters
 


**text** 
 – output of language model
 




 Returns
 


 structured output
 










 parse_with_prompt
 


 (
 
*completion
 



 :
 





 str*
 ,
 *prompt_value
 



 :
 





 langchain.schema.PromptValue*

 )
 


 →
 


 langchain.output_parsers.retry.T
 


[[source]](../../_modules/langchain/output_parsers/retry#RetryWithErrorOutputParser.parse_with_prompt)
[#](#langchain.output_parsers.RetryWithErrorOutputParser.parse_with_prompt "Permalink to this definition") 



 Optional method to parse the output of an LLM call with a prompt.
 



 The prompt is largely provided in the event the OutputParser wants
to retry or fix the output in some way, and needs information from
the prompt to do so.
 




 Parameters
 

* **completion** 
 – output of language model
* **prompt** 
 – prompt value




 Returns
 


 structured output
 










*pydantic
 

 model*


 langchain.output_parsers.
 



 StructuredOutputParser
 

[[source]](../../_modules/langchain/output_parsers/structured#StructuredOutputParser)
[#](#langchain.output_parsers.StructuredOutputParser "Permalink to this definition") 




*field*


 response_schemas
 

*:
 




 List
 


 [
 

[langchain.output_parsers.structured.ResponseSchema](#langchain.output_parsers.ResponseSchema "langchain.output_parsers.structured.ResponseSchema")


 ]*
*[Required]*
[#](#langchain.output_parsers.StructuredOutputParser.response_schemas "Permalink to this definition") 






*classmethod*


 from_response_schemas
 


 (
 
*response_schemas
 



 :
 





 List
 


 [
 

[langchain.output_parsers.structured.ResponseSchema](#langchain.output_parsers.ResponseSchema "langchain.output_parsers.structured.ResponseSchema")


 ]*

 )
 


 →
 

[langchain.output_parsers.structured.StructuredOutputParser](#langchain.output_parsers.StructuredOutputParser "langchain.output_parsers.structured.StructuredOutputParser")


[[source]](../../_modules/langchain/output_parsers/structured#StructuredOutputParser.from_response_schemas)
[#](#langchain.output_parsers.StructuredOutputParser.from_response_schemas "Permalink to this definition") 








 get_format_instructions
 


 (
 

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/output_parsers/structured#StructuredOutputParser.get_format_instructions)
[#](#langchain.output_parsers.StructuredOutputParser.get_format_instructions "Permalink to this definition") 



 Instructions on how the LLM output should be formatted.
 








 parse
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 Any
 


[[source]](../../_modules/langchain/output_parsers/structured#StructuredOutputParser.parse)
[#](#langchain.output_parsers.StructuredOutputParser.parse "Permalink to this definition") 



 Parse the output of an LLM call.
 



 A method which takes in a string (assumed output of language model )
and parses it into some structure.
 




 Parameters
 


**text** 
 – output of language model
 




 Returns
 


 structured output
 










