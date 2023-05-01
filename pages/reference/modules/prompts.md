




 PromptTemplates
 [#](#module-langchain.prompts "Permalink to this headline")
==============================================================================



 Prompt template classes.
 




*pydantic
 

 model*


 langchain.prompts.
 



 BaseChatPromptTemplate
 

[[source]](../../_modules/langchain/prompts/chat#BaseChatPromptTemplate)
[#](#langchain.prompts.BaseChatPromptTemplate "Permalink to this definition") 






 format
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/prompts/chat#BaseChatPromptTemplate.format)
[#](#langchain.prompts.BaseChatPromptTemplate.format "Permalink to this definition") 



 Format the prompt with the inputs.
 




 Parameters
 


**kwargs** 
 – Any arguments to be passed to the prompt template.
 




 Returns
 


 A formatted string.
 





 Example:
 





```
prompt.format(variable1="foo")

```







*abstract*


 format_messages
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]
 



[[source]](../../_modules/langchain/prompts/chat#BaseChatPromptTemplate.format_messages)
[#](#langchain.prompts.BaseChatPromptTemplate.format_messages "Permalink to this definition") 



 Format kwargs into a list of messages.
 








 format_prompt
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.schema.PromptValue
 


[[source]](../../_modules/langchain/prompts/chat#BaseChatPromptTemplate.format_prompt)
[#](#langchain.prompts.BaseChatPromptTemplate.format_prompt "Permalink to this definition") 



 Create Chat Messages.
 








*pydantic
 

 model*


 langchain.prompts.
 



 BasePromptTemplate
 

[[source]](../../_modules/langchain/prompts/base#BasePromptTemplate)
[#](#langchain.prompts.BasePromptTemplate "Permalink to this definition") 



 Base class for all prompt templates, returning a prompt.
 




*field*


 input_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Required]*
[#](#langchain.prompts.BasePromptTemplate.input_variables "Permalink to this definition") 



 A list of the names of the variables the prompt template expects.
 






*field*


 output_parser
 

*:
 




 Optional
 


 [
 


 langchain.schema.BaseOutputParser
 


 ]*
*=
 




 None*
[#](#langchain.prompts.BasePromptTemplate.output_parser "Permalink to this definition") 



 How to parse the output of calling an LLM on this formatted prompt.
 








 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[[source]](../../_modules/langchain/prompts/base#BasePromptTemplate.dict)
[#](#langchain.prompts.BasePromptTemplate.dict "Permalink to this definition") 



 Return dictionary representation of prompt.
 






*abstract*


 format
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/prompts/base#BasePromptTemplate.format)
[#](#langchain.prompts.BasePromptTemplate.format "Permalink to this definition") 



 Format the prompt with the inputs.
 




 Parameters
 


**kwargs** 
 – Any arguments to be passed to the prompt template.
 




 Returns
 


 A formatted string.
 





 Example:
 





```
prompt.format(variable1="foo")

```







*abstract*


 format_prompt
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.schema.PromptValue
 


[[source]](../../_modules/langchain/prompts/base#BasePromptTemplate.format_prompt)
[#](#langchain.prompts.BasePromptTemplate.format_prompt "Permalink to this definition") 



 Create Chat Messages.
 








 partial
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 Callable
 


 [
 



 [
 



 ]
 



 ,
 




 str
 


 ]
 



 ]*

 )
 


 →
 

[langchain.prompts.base.BasePromptTemplate](#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")


[[source]](../../_modules/langchain/prompts/base#BasePromptTemplate.partial)
[#](#langchain.prompts.BasePromptTemplate.partial "Permalink to this definition") 



 Return a partial of the prompt template.
 








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
 


[[source]](../../_modules/langchain/prompts/base#BasePromptTemplate.save)
[#](#langchain.prompts.BasePromptTemplate.save "Permalink to this definition") 



 Save the prompt.
 




 Parameters
 


**file_path** 
 – Path to directory to save prompt to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  prompt.save(file_path=”path/prompt.yaml”)
>  
> 
> 
> 
> 








*pydantic
 

 model*


 langchain.prompts.
 



 ChatPromptTemplate
 

[[source]](../../_modules/langchain/prompts/chat#ChatPromptTemplate)
[#](#langchain.prompts.ChatPromptTemplate "Permalink to this definition") 






 format
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/prompts/chat#ChatPromptTemplate.format)
[#](#langchain.prompts.ChatPromptTemplate.format "Permalink to this definition") 



 Format the prompt with the inputs.
 




 Parameters
 


**kwargs** 
 – Any arguments to be passed to the prompt template.
 




 Returns
 


 A formatted string.
 





 Example:
 





```
prompt.format(variable1="foo")

```









 format_messages
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]
 



[[source]](../../_modules/langchain/prompts/chat#ChatPromptTemplate.format_messages)
[#](#langchain.prompts.ChatPromptTemplate.format_messages "Permalink to this definition") 



 Format kwargs into a list of messages.
 








 partial
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 Callable
 


 [
 



 [
 



 ]
 



 ,
 




 str
 


 ]
 



 ]*

 )
 


 →
 

[langchain.prompts.base.BasePromptTemplate](#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")


[[source]](../../_modules/langchain/prompts/chat#ChatPromptTemplate.partial)
[#](#langchain.prompts.ChatPromptTemplate.partial "Permalink to this definition") 



 Return a partial of the prompt template.
 








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
 


[[source]](../../_modules/langchain/prompts/chat#ChatPromptTemplate.save)
[#](#langchain.prompts.ChatPromptTemplate.save "Permalink to this definition") 



 Save the prompt.
 




 Parameters
 


**file_path** 
 – Path to directory to save prompt to.
 





 Example:
.. code-block:: python
 



> 
> 
> 
>  prompt.save(file_path=”path/prompt.yaml”)
>  
> 
> 
> 
> 








*pydantic
 

 model*


 langchain.prompts.
 



 FewShotPromptTemplate
 

[[source]](../../_modules/langchain/prompts/few_shot#FewShotPromptTemplate)
[#](#langchain.prompts.FewShotPromptTemplate "Permalink to this definition") 



 Prompt template that contains few shot examples.
 




*field*


 example_prompt
 

*:
 



[langchain.prompts.prompt.PromptTemplate](#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")*
*[Required]*
[#](#langchain.prompts.FewShotPromptTemplate.example_prompt "Permalink to this definition") 



 PromptTemplate used to format an individual example.
 






*field*


 example_selector
 

*:
 




 Optional
 


 [
 


 langchain.prompts.example_selector.base.BaseExampleSelector
 


 ]*
*=
 




 None*
[#](#langchain.prompts.FewShotPromptTemplate.example_selector "Permalink to this definition") 



 ExampleSelector to choose the examples to format into the prompt.
Either this or examples should be provided.
 






*field*


 example_separator
 

*:
 




 str*
*=
 




 '\n\n'*
[#](#langchain.prompts.FewShotPromptTemplate.example_separator "Permalink to this definition") 



 String separator used to join the prefix, the examples, and suffix.
 






*field*


 examples
 

*:
 




 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.prompts.FewShotPromptTemplate.examples "Permalink to this definition") 



 Examples to format into the prompt.
Either this or example_selector should be provided.
 






*field*


 input_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Required]*
[#](#langchain.prompts.FewShotPromptTemplate.input_variables "Permalink to this definition") 



 A list of the names of the variables the prompt template expects.
 






*field*


 prefix
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.prompts.FewShotPromptTemplate.prefix "Permalink to this definition") 



 A prompt template string to put before the examples.
 






*field*


 suffix
 

*:
 




 str*
*[Required]*
[#](#langchain.prompts.FewShotPromptTemplate.suffix "Permalink to this definition") 



 A prompt template string to put after the examples.
 






*field*


 template_format
 

*:
 




 str*
*=
 




 'f-string'*
[#](#langchain.prompts.FewShotPromptTemplate.template_format "Permalink to this definition") 



 The format of the prompt template. Options are: ‘f-string’, ‘jinja2’.
 






*field*


 validate_template
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.prompts.FewShotPromptTemplate.validate_template "Permalink to this definition") 



 Whether or not to try validating the template.
 








 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[[source]](../../_modules/langchain/prompts/few_shot#FewShotPromptTemplate.dict)
[#](#langchain.prompts.FewShotPromptTemplate.dict "Permalink to this definition") 



 Return a dictionary of the prompt.
 








 format
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/prompts/few_shot#FewShotPromptTemplate.format)
[#](#langchain.prompts.FewShotPromptTemplate.format "Permalink to this definition") 



 Format the prompt with the inputs.
 




 Parameters
 


**kwargs** 
 – Any arguments to be passed to the prompt template.
 




 Returns
 


 A formatted string.
 





 Example:
 





```
prompt.format(variable1="foo")

```









*pydantic
 

 model*


 langchain.prompts.
 



 FewShotPromptWithTemplates
 

[[source]](../../_modules/langchain/prompts/few_shot_with_templates#FewShotPromptWithTemplates)
[#](#langchain.prompts.FewShotPromptWithTemplates "Permalink to this definition") 



 Prompt template that contains few shot examples.
 




*field*


 example_prompt
 

*:
 



[langchain.prompts.prompt.PromptTemplate](#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")*
*[Required]*
[#](#langchain.prompts.FewShotPromptWithTemplates.example_prompt "Permalink to this definition") 



 PromptTemplate used to format an individual example.
 






*field*


 example_selector
 

*:
 




 Optional
 


 [
 


 langchain.prompts.example_selector.base.BaseExampleSelector
 


 ]*
*=
 




 None*
[#](#langchain.prompts.FewShotPromptWithTemplates.example_selector "Permalink to this definition") 



 ExampleSelector to choose the examples to format into the prompt.
Either this or examples should be provided.
 






*field*


 example_separator
 

*:
 




 str*
*=
 




 '\n\n'*
[#](#langchain.prompts.FewShotPromptWithTemplates.example_separator "Permalink to this definition") 



 String separator used to join the prefix, the examples, and suffix.
 






*field*


 examples
 

*:
 




 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.prompts.FewShotPromptWithTemplates.examples "Permalink to this definition") 



 Examples to format into the prompt.
Either this or example_selector should be provided.
 






*field*


 input_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Required]*
[#](#langchain.prompts.FewShotPromptWithTemplates.input_variables "Permalink to this definition") 



 A list of the names of the variables the prompt template expects.
 






*field*


 prefix
 

*:
 




 Optional
 


 [
 

[langchain.prompts.base.StringPromptTemplate](#langchain.prompts.StringPromptTemplate "langchain.prompts.base.StringPromptTemplate")


 ]*
*=
 




 None*
[#](#langchain.prompts.FewShotPromptWithTemplates.prefix "Permalink to this definition") 



 A PromptTemplate to put before the examples.
 






*field*


 suffix
 

*:
 



[langchain.prompts.base.StringPromptTemplate](#langchain.prompts.StringPromptTemplate "langchain.prompts.base.StringPromptTemplate")*
*[Required]*
[#](#langchain.prompts.FewShotPromptWithTemplates.suffix "Permalink to this definition") 



 A PromptTemplate to put after the examples.
 






*field*


 template_format
 

*:
 




 str*
*=
 




 'f-string'*
[#](#langchain.prompts.FewShotPromptWithTemplates.template_format "Permalink to this definition") 



 The format of the prompt template. Options are: ‘f-string’, ‘jinja2’.
 






*field*


 validate_template
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.prompts.FewShotPromptWithTemplates.validate_template "Permalink to this definition") 



 Whether or not to try validating the template.
 








 dict
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Dict
 


[[source]](../../_modules/langchain/prompts/few_shot_with_templates#FewShotPromptWithTemplates.dict)
[#](#langchain.prompts.FewShotPromptWithTemplates.dict "Permalink to this definition") 



 Return a dictionary of the prompt.
 








 format
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/prompts/few_shot_with_templates#FewShotPromptWithTemplates.format)
[#](#langchain.prompts.FewShotPromptWithTemplates.format "Permalink to this definition") 



 Format the prompt with the inputs.
 




 Parameters
 


**kwargs** 
 – Any arguments to be passed to the prompt template.
 




 Returns
 


 A formatted string.
 





 Example:
 





```
prompt.format(variable1="foo")

```









*pydantic
 

 model*


 langchain.prompts.
 



 MessagesPlaceholder
 

[[source]](../../_modules/langchain/prompts/chat#MessagesPlaceholder)
[#](#langchain.prompts.MessagesPlaceholder "Permalink to this definition") 



 Prompt template that assumes variable is already list of messages.
 






 format_messages
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.BaseMessage
 


 ]
 



[[source]](../../_modules/langchain/prompts/chat#MessagesPlaceholder.format_messages)
[#](#langchain.prompts.MessagesPlaceholder.format_messages "Permalink to this definition") 



 To a BaseMessage.
 






*property*


 input_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.prompts.MessagesPlaceholder.input_variables "Permalink to this definition") 



 Input variables for this prompt template.
 










 langchain.prompts.
 



 Prompt
 

[#](#langchain.prompts.Prompt "Permalink to this definition") 



 alias of
 [`langchain.prompts.prompt.PromptTemplate`](#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")







*pydantic
 

 model*


 langchain.prompts.
 



 PromptTemplate
 

[[source]](../../_modules/langchain/prompts/prompt#PromptTemplate)
[#](#langchain.prompts.PromptTemplate "Permalink to this definition") 



 Schema to represent a prompt for an LLM.
 



 Example
 





```
from langchain import PromptTemplate
prompt = PromptTemplate(input_variables=["foo"], template="Say {foo}")

```





*field*


 input_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Required]*
[#](#langchain.prompts.PromptTemplate.input_variables "Permalink to this definition") 



 A list of the names of the variables the prompt template expects.
 






*field*


 template
 

*:
 




 str*
*[Required]*
[#](#langchain.prompts.PromptTemplate.template "Permalink to this definition") 



 The prompt template.
 






*field*


 template_format
 

*:
 




 str*
*=
 




 'f-string'*
[#](#langchain.prompts.PromptTemplate.template_format "Permalink to this definition") 



 The format of the prompt template. Options are: ‘f-string’, ‘jinja2’.
 






*field*


 validate_template
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.prompts.PromptTemplate.validate_template "Permalink to this definition") 



 Whether or not to try validating the template.
 








 format
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/prompts/prompt#PromptTemplate.format)
[#](#langchain.prompts.PromptTemplate.format "Permalink to this definition") 



 Format the prompt with the inputs.
 




 Parameters
 


**kwargs** 
 – Any arguments to be passed to the prompt template.
 




 Returns
 


 A formatted string.
 





 Example:
 





```
prompt.format(variable1="foo")

```







*classmethod*


 from_examples
 


 (
 
*examples
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *suffix
 



 :
 





 str*
 ,
 *input_variables
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *example_separator
 



 :
 





 str
 





 =
 





 '\n\n'*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 ''*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.prompts.prompt.PromptTemplate](#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")


[[source]](../../_modules/langchain/prompts/prompt#PromptTemplate.from_examples)
[#](#langchain.prompts.PromptTemplate.from_examples "Permalink to this definition") 



 Take examples in list format with prefix and suffix to create a prompt.
 



 Intended to be used as a way to dynamically create a prompt from examples.
 




 Parameters
 

* **examples** 
 – List of examples to use in the prompt.
* **suffix** 
 – String to go after the list of examples. Should generally
set up the user’s input.
* **input_variables** 
 – A list of variable names the final prompt template
will expect.
* **example_separator** 
 – The separator to use in between examples. Defaults
to two new line characters.
* **prefix** 
 – String that should go before any examples. Generally includes
examples. Default to an empty string.




 Returns
 


 The final prompt generated.
 








*classmethod*


 from_file
 


 (
 
*template_file
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 pathlib.Path
 


 ]*
 ,
 *input_variables
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.prompts.prompt.PromptTemplate](#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")


[[source]](../../_modules/langchain/prompts/prompt#PromptTemplate.from_file)
[#](#langchain.prompts.PromptTemplate.from_file "Permalink to this definition") 



 Load a prompt from a file.
 




 Parameters
 

* **template_file** 
 – The path to the file containing the prompt template.
* **input_variables** 
 – A list of variable names the final prompt template
will expect.




 Returns
 


 The prompt loaded from the file.
 








*classmethod*


 from_template
 


 (
 
*template
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.prompts.prompt.PromptTemplate](#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")


[[source]](../../_modules/langchain/prompts/prompt#PromptTemplate.from_template)
[#](#langchain.prompts.PromptTemplate.from_template "Permalink to this definition") 



 Load a prompt template from a template.
 








*pydantic
 

 model*


 langchain.prompts.
 



 StringPromptTemplate
 

[[source]](../../_modules/langchain/prompts/base#StringPromptTemplate)
[#](#langchain.prompts.StringPromptTemplate "Permalink to this definition") 



 String prompt should expose the format method, returning a prompt.
 






 format_prompt
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.schema.PromptValue
 


[[source]](../../_modules/langchain/prompts/base#StringPromptTemplate.format_prompt)
[#](#langchain.prompts.StringPromptTemplate.format_prompt "Permalink to this definition") 



 Create Chat Messages.
 










 langchain.prompts.
 



 load_prompt
 


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
 

[langchain.prompts.base.BasePromptTemplate](#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")


[[source]](../../_modules/langchain/prompts/loading#load_prompt)
[#](#langchain.prompts.load_prompt "Permalink to this definition") 



 Unified method for loading a prompt from LangChainHub or local fs.
 





