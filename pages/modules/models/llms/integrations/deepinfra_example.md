

DeepInfra[#](#deepinfra "Permalink to this headline")
=====================================================

`DeepInfra` provides [several LLMs](https://deepinfra.com/models).

This notebook goes over how to use Langchain with [DeepInfra](https://deepinfra.com).

Imports[#](#imports "Permalink to this headline")
-------------------------------------------------

```
import os
from langchain.llms import DeepInfra
from langchain import PromptTemplate, LLMChain

```

Set the Environment API Key[#](#set-the-environment-api-key "Permalink to this headline")
-----------------------------------------------------------------------------------------

Make sure to get your API key from DeepInfra. You have to [Login](https://deepinfra.com/login?from=%2Fdash) and get a new token.

You are given a 1 hour free of serverless GPU compute to test different models. (see [here](https://github.com/deepinfra/deepctl#deepctl))
You can print your token with `deepctl auth token`

```
# get a new token: https://deepinfra.com/login?from=%2Fdash

from getpass import getpass

DEEPINFRA_API_TOKEN = getpass()

```

```
os.environ["DEEPINFRA_API_TOKEN"] = DEEPINFRA_API_TOKEN

```

创建DeepInfra实例[#](#create-the-deepinfra-instance "本标题的永久链接")
-----------------------------------------------------------

确保先通过`deepctl deploy create -m google/flat-t5-xl`部署模型（参见[此处](https://github.com/deepinfra/deepctl#deepctl)）

```
llm = DeepInfra(model_id="DEPLOYED MODEL ID")

```

创建提示模板[#](#create-a-prompt-template "本标题的永久链接")
-----------------------------------------------

我们将为问题和答案创建提示模板。

```
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

```

启动LLMChain[#](#initiate-the-llmchain "本标题的永久链接")
------------------------------------------------

```
llm_chain = LLMChain(prompt=prompt, llm=llm)

```

运行LLMChain[#](#run-the-llmchain "本标题的永久链接")
-------------------------------------------

提供一个问题并运行LLMChain。

```
question = "What NFL team won the Super Bowl in 2015?"

llm_chain.run(question)

```

