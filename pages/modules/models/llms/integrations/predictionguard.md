


如何使用 PredictionGuard wrapper
=================================================

```
! pip install predictionguard langchain

```

```
import predictionguard as pg
from langchain.llms import PredictionGuard

```

基本的LLM用法[#](#basic-llm-usage "Permalink to this headline")
-----------------------------------------------------------------

```
pgllm = PredictionGuard(name="default-text-gen", token="<your access token>")

```

```
pgllm("Tell me a joke")

```

链[#](#chaining "Permalink to this headline")
---------------------------------------------------

```
from langchain import PromptTemplate, LLMChain

```

```
template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=pgllm, verbose=True)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.predict(question=question)

```

```
template = """Write a {adjective} poem about {subject}."""
prompt = PromptTemplate(template=template, input_variables=["adjective", "subject"])
llm_chain = LLMChain(prompt=prompt, llm=pgllm, verbose=True)

llm_chain.predict(adjective="sad", subject="ducks")

```

