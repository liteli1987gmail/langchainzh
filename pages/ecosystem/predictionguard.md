

预测保护[#](#prediction-guard "跳转到本标题的永久链接")
========================================

本页面介绍如何在LangChain中使用预测保护生态系统。它分为两个部分：安装和设置，然后是对特定预测保护包装器的引用。

安装和设置[#](#installation-and-setup "跳转到本标题的永久链接")
-----------------------------------------------

* 使用 `pip install predictionguard` 安装Python SDK。

* 获取预测保护访问令牌（如此处所述[here](https://docs.predictionguard.com/)），并将其设置为环境变量（`PREDICTIONGUARD_TOKEN`）

LLM包装器[#](#llm-wrapper "跳转到本标题的永久链接")
-------------------------------------

现在存在一个Prediction Guard LLM包装器，您可以使用它来访问

```
from langchain.llms import PredictionGuard

```

在初始化LLM时，您可以提供您的Prediction Guard“代理”的名称作为参数：

```
pgllm = PredictionGuard(name="your-text-gen-proxy")

```

或者，您可以使用Prediction Guard的默认代理来进行SOTA LLM：

```
pgllm = PredictionGuard(name="default-text-gen")

```

您还可以直接提供访问令牌作为参数：

```
pgllm = PredictionGuard(name="default-text-gen", token="<your access token>")

```

示例用法[#](#example-usage "Permalink to this headline")
----------------------------------------------------

LLM包装器的基本用法：

```
from langchain.llms import PredictionGuard

pgllm = PredictionGuard(name="default-text-gen")
pgllm("Tell me a joke")

```

使用Prediction Guard包装器进行基本LLM链接：

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

