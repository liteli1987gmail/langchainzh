


 LLM Chain
 [#](#llm-chain "Permalink to this headline")
=========================================================



`LLMChain`
 is perhaps one of the most popular ways of querying an LLM object. It formats the prompt template using the input key values provided (and also memory key values, if available), passes the formatted string to LLM and returns the LLM output. Below we show additional functionalities of
 `LLMChain`
 class.
 







```
from langchain import PromptTemplate, OpenAI, LLMChain

prompt_template = "What is a good name for a company that makes {product}?"

llm = OpenAI(temperature=0)
llm_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)
llm_chain("colorful socks")

```








```
{'product': 'colorful socks', 'text': '\n\nSocktastic!'}

```








 Additional ways of running LLM Chain
 [#](#additional-ways-of-running-llm-chain "Permalink to this headline")
===============================================================================================================



 Aside from
 `__call__`
 and
 `run`
 methods shared by all
 `Chain`
 object (see
 [Getting Started](../getting_started)
 to learn more),
 `LLMChain`
 offers a few more ways of calling the chain logic:
 


* `apply`
 allows you run the chain against a list of inputs:







```
input_list = [
    {"product": "socks"},
    {"product": "computer"},
    {"product": "shoes"}
]

llm_chain.apply(input_list)

```








```
[{'text': '\n\nSocktastic!'},
 {'text': '\n\nTechCore Solutions.'},
 {'text': '\n\nFootwear Factory.'}]

```





* `generate`
 is similar to
 `apply`
 , except it return an
 `LLMResult`
 instead of string.
 `LLMResult`
 often contains useful generation such as token usages and finish reason.







```
llm_chain.generate(input_list)

```








```
LLMResult(generations=[[Generation(text='\n\nSocktastic!', generation_info={'finish_reason': 'stop', 'logprobs': None})], [Generation(text='\n\nTechCore Solutions.', generation_info={'finish_reason': 'stop', 'logprobs': None})], [Generation(text='\n\nFootwear Factory.', generation_info={'finish_reason': 'stop', 'logprobs': None})]], llm_output={'token_usage': {'prompt_tokens': 36, 'total_tokens': 55, 'completion_tokens': 19}, 'model_name': 'text-davinci-003'})

```





* `predict`
 is similar to
 `run`
 method except in 2 ways:
 


	+ Input key is specified as keyword argument instead of a Python dict
	+ It supports multiple input keys.







```
# Single input example
llm_chain.predict(product="colorful socks")

```








```
'\n\nSocktastic!'

```










```
# Multiple inputs example

template = """Tell me a {adjective} joke about {subject}."""
prompt = PromptTemplate(template=template, input_variables=["adjective", "subject"])
llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0))

llm_chain.predict(adjective="sad", subject="ducks")

```








```
'\n\nQ: What did the duck say when his friend died?\nA: Quack, quack, goodbye.'

```








 Parsing the outputs
 [#](#parsing-the-outputs "Permalink to this headline")
=============================================================================



 By default,
 `LLMChain`
 does not parse the output even if the underlying
 `prompt`
 object has an output parser. If you would like to apply that output parser on the LLM output, use
 `predict_and_parse`
 instead of
 `predict`
 and
 `apply_and_parse`
 instead of
 `apply`
 .
 



 With
 `predict`
 :
 







```
from langchain.output_parsers import CommaSeparatedListOutputParser

output_parser = CommaSeparatedListOutputParser()
template = """List all the colors in a rainbow"""
prompt = PromptTemplate(template=template, input_variables=[], output_parser=output_parser)
llm_chain = LLMChain(prompt=prompt, llm=llm)

llm_chain.predict()

```








```
'\n\nRed, orange, yellow, green, blue, indigo, violet'

```






 With
 `predict_and_parser`
 :
 







```
llm_chain.predict_and_parse()

```








```
['Red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

```








 Initialize from string
 [#](#initialize-from-string "Permalink to this headline")
===================================================================================



 You can also construct an LLMChain from a string template directly.
 







```
template = """Tell me a {adjective} joke about {subject}."""
llm_chain = LLMChain.from_string(llm=llm, template=template)

```










```
llm_chain.predict(adjective="sad", subject="ducks")

```








```
'\n\nQ: What did the duck say when his friend died?\nA: Quack, quack, goodbye.'

```







