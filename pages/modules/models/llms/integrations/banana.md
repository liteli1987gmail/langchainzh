

香蕉[#](#banana "Permalink to this headline")
===========================================

[香蕉](https://www.banana.dev/about-us)致力于构建机器学习基础设施。

这个例子介绍了如何使用LangChain与香蕉模型进行交互

```
# Install the package https://docs.banana.dev/banana-docs/core-concepts/sdks/python
!pip install banana-dev

```

```
# get new tokens: https://app.banana.dev/
# We need two tokens, not just an `api_key`: `BANANA_API_KEY` and `YOUR_MODEL_KEY`

import os
from getpass import getpass

os.environ["BANANA_API_KEY"] = "YOUR_API_KEY"
# OR
# BANANA_API_KEY = getpass()

```

```
from langchain.llms import Banana
from langchain import PromptTemplate, LLMChain

```

```
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

```

```
llm = Banana(model_key="YOUR_MODEL_KEY")

```

```
llm_chain = LLMChain(prompt=prompt, llm=llm)

```

```
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)

```

