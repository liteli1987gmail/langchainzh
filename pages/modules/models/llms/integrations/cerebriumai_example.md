

CerebriumAI[#](#cerebriumai "跳转到这个标题的永久链接")
===========================================

`Cerebrium` 是一个 AWS Sagemaker 的替代品。它还提供 API 访问**[多个 LLM 模型](https://docs.cerebrium.ai/cerebrium/prebuilt-models/deployment)**。

本笔记介绍如何使用 Langchain 和**[CerebriumAI](https://docs.cerebrium.ai/introduction)**。

安装 cerebrium[#](#install-cerebrium "跳转到这个标题的永久链接")
--------------------------------------------------

使用 `CerebriumAI` API 需要安装 `cerebrium` 包。使用 `pip3 install cerebrium` 命令安装。

```
# Install the package
!pip3 install cerebrium

```

导入[#](#imports "跳转到这个标题的永久链接")
------------------------------

```
import os
from langchain.llms import CerebriumAI
from langchain import PromptTemplate, LLMChain

```

设置环境 API 密钥[#](#set-the-environment-api-key "跳转到这个标题的永久链接")
-----------------------------------------------------------

确保从CerebriumAI获取您的API密钥。请参见[这里](https://dashboard.cerebrium.ai/login)。您将获得1小时的免费无服务器GPU计算，以测试不同的模型。

```
os.environ["CEREBRIUMAI_API_KEY"] = "YOUR_KEY_HERE"

```

创建CerebriumAI实例[#](#create-the-cerebriumai-instance "跳转到此标题的链接")
----------------------------------------------------------------

您可以指定不同的参数，例如模型终端点URL、最大长度、温度等。您必须提供一个终端点URL。

```
llm = CerebriumAI(endpoint_url="YOUR ENDPOINT URL HERE")

```

创建提示模板[#](#create-a-prompt-template "跳转到此标题的链接")
------------------------------------------------

我们将为问答创建一个提示模板。

```
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

```

启动LLMChain[#](#initiate-the-llmchain "跳转到此标题的链接")
-------------------------------------------------

```
llm_chain = LLMChain(prompt=prompt, llm=llm)

```

运行LLMChain[#](#run-the-llmchain "跳转到此标题的链接")
--------------------------------------------

提供一个问题并运行LLMChain。

```
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)

```

