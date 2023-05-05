
`Petals`以BitTorrent方式在家中运行超过100B的语言模型。

本笔记本介绍如何使用Langchain和[Petals](https://github.com/bigscience-workshop/petals)。

安装Petals[#](#install-petals "此标题的永久链接")
---------------------------------------

要使用Petals API，需要安装`petals`包。使用`pip3 install petals`进行安装。

```
!pip3 install petals

```

导入[#](#imports "此标题的永久链接")
--------------------------

```
import os
from langchain.llms import Petals
from langchain import PromptTemplate, LLMChain

```

设置环境API密钥[#](#set-the-environment-api-key "此标题的永久链接")
-----------------------------------------------------

请确保从Huggingface获取[API密钥](https://huggingface.co/docs/api-inference/quicktour#get-your-api-token)。

```
from getpass import getpass

HUGGINGFACE_API_KEY = getpass()

```

```
os.environ["HUGGINGFACE_API_KEY"] = HUGGINGFACE_API_KEY

```

Create the Petals instance[#](#create-the-petals-instance "Permalink to this headline")
---------------------------------------------------------------------------------------

You can specify different parameters such as the model name, max new tokens, temperature, etc.

```
# this can take several minutes to download big files!

llm = Petals(model_name="bigscience/bloom-petals")

```

```
Downloading:   1%|▏                        | 40.8M/7.19G [00:24<15:44, 7.57MB/s]

```

Create a Prompt Template[#](#create-a-prompt-template "Permalink to this headline")
-----------------------------------------------------------------------------------

We will create a prompt template for Question and Answer.

```
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

```

Initiate the LLMChain[#](#initiate-the-llmchain "Permalink to this headline")
-----------------------------------------------------------------------------

```
llm_chain = LLMChain(prompt=prompt, llm=llm)

```

Run the LLMChain[#](#run-the-llmchain "Permalink to this headline")
-------------------------------------------------------------------

Provide a question and run the LLMChain.

```
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)

```

