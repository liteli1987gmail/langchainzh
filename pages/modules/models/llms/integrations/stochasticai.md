

随机AI[#](#stochasticai "此标题的永久链接")
=================================

> 
> [随机加速平台](https://docs.stochastic.ai/docs/introduction/)旨在简化深度学习模型的生命周期。从上传和版本控制模型，到训练、压缩和加速，最终投入生产。
> 
> 
> 

本示例介绍如何使用LangChain与`StochasticAI`模型进行交互。

您需要在[这里](https://app.stochastic.ai/workspace/profile/settings?tab=profile)获取API_KEY和API_URL。

```
from getpass import getpass

STOCHASTICAI_API_KEY = getpass()

```

```
import os

os.environ["STOCHASTICAI_API_KEY"] = STOCHASTICAI_API_KEY

```

```
YOUR_API_URL = getpass()

```

```
from langchain.llms import StochasticAI
from langchain import PromptTemplate, LLMChain

```

```
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

```

```
llm = StochasticAI(api_url=YOUR_API_URL)

```

```
llm_chain = LLMChain(prompt=prompt, llm=llm)

```

```
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)

```

```
"  Step 1: In 1999, the St. Louis Rams won the Super Bowl.  Step 2: In 1999, Beiber was born.  Step 3: The Rams were in Los Angeles at the time.  Step 4: So they didn't play in the Super Bowl that year.\n"

```

