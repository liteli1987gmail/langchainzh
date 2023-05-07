

DeepInfra[#](#deepinfra "Permalink to this headline")
=====================================================

`DeepInfra` 提供了多种LLM [several LLMs](https://deepinfra.com/models).

本文介绍如何使用Langchain与[DeepInfra](https://deepinfra.com)进行交互。 

Imports[#](#imports "Permalink to this headline")
-------------------------------------------------

```
import os
from langchain.llms import DeepInfra
from langchain import PromptTemplate, LLMChain

```

设置环境变量的API Key[#](#set-the-environment-api-key "Permalink to this headline")
-----------------------------------------------------------------------------------------

请确保从DeepInfra获取API Key。您必须[登录](https://deepinfra.com/login?from=%2Fdash)并获取新令牌。

您将获得1个小时的免费服务器级GPU计算时间，以测试不同的模型（请参见[此处](https://github.com/deepinfra/deepctl#deepctl))。

您可以使用 `deepctl auth token` 命令打印您的令牌。

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

确保先通过`deepctl deploy create -m google/flat-t5-xl`部署模型（参见[此处](https://github.com/deepinfra/deepctl#deepctl))

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

