

ForefrontAI[#](#forefrontai "跳转到此标题的永久链接")
==========================================

`Forefront` 平台可让您微调和使用[开源大型语言模型](https://docs.forefront.ai/forefront/master/models)。

本教程将介绍如何使用 Langchain 和[ForefrontAI](https://www.forefront.ai/)。

导入[#](#imports "跳转到此标题的永久链接")
-----------------------------

```
import os
from langchain.llms import ForefrontAI
from langchain import PromptTemplate, LLMChain

```

设置环境 API 密钥[#](#set-the-environment-api-key "跳转到此标题的永久链接")
----------------------------------------------------------

确保从 ForefrontAI 获取您的 API 密钥。您将获得 5 天免费试用，以测试不同的模型。

```
# get a new token: https://docs.forefront.ai/forefront/api-reference/authentication

from getpass import getpass

FOREFRONTAI_API_KEY = getpass()

```

```
os.environ["FOREFRONTAI_API_KEY"] = FOREFRONTAI_API_KEY

```

创建 ForefrontAI 实例[#](#create-the-forefrontai-instance "跳转到此标题的永久链接")
--------------------------------------------------------------------

您可以指定不同的参数，如模型端点 URL、长度、温度（temperature）等。您必须提供端点 URL。

```
llm = ForefrontAI(endpoint_url="YOUR ENDPOINT URL HERE")

```

创建提示模板[#](#create-a-prompt-template "此标题的永久链接")
-----------------------------------------------

我们将为问题和答案创建提示模板。

```
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

```

启动LLMChain[#](#initiate-the-llmchain "此标题的永久链接")
------------------------------------------------

```
llm_chain = LLMChain(prompt=prompt, llm=llm)

```

运行LLMChain[#](#run-the-llmchain "此标题的永久链接")
-------------------------------------------

提供一个问题并运行LLMChain。

```
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)

```

