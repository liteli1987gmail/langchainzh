


 Prediction Guard
 [#](#prediction-guard "Permalink to this headline")
=======================================================================



 This page covers how to use the Prediction Guard ecosystem within LangChain.
It is broken into two parts: installation and setup, and then references to specific Prediction Guard wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Python SDK with
 `pip
 

 install
 

 predictionguard`
* Get an Prediction Guard access token (as described
 [here](https://docs.predictionguard.com/) 
 ) and set it as an environment variable (
 `PREDICTIONGUARD_TOKEN`
 )





 LLM Wrapper
 [#](#llm-wrapper "Permalink to this headline")
-------------------------------------------------------------



 There exists a Prediction Guard LLM wrapper, which you can access with
 





```
from langchain.llms import PredictionGuard

```




 You can provide the name of your Prediction Guard “proxy” as an argument when initializing the LLM:
 





```
pgllm = PredictionGuard(name="your-text-gen-proxy")

```




 Alternatively, you can use Prediction Guard’s default proxy for SOTA LLMs:
 





```
pgllm = PredictionGuard(name="default-text-gen")

```




 You can also provide your access token directly as an argument:
 





```
pgllm = PredictionGuard(name="default-text-gen", token="<your access token>")

```






 Example usage
 [#](#example-usage "Permalink to this headline")
-----------------------------------------------------------------



 Basic usage of the LLM wrapper:
 





```
from langchain.llms import PredictionGuard

pgllm = PredictionGuard(name="default-text-gen")
pgllm("Tell me a joke")

```




 Basic LLM Chaining with the Prediction Guard wrapper:
 





```
from langchain import PromptTemplate, LLMChain
from langchain.llms import PredictionGuard

template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=PredictionGuard(name="default-text-gen"), verbose=True)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.predict(question=question)

```






