


[OpenAI](https://platform.openai.com/docs/introduction)提供了不同级别的模型，适用于不同的任务。

此示例介绍了如何使用LangChain与`OpenAI` [models](https://platform.openai.com/docs/models) 进行交互。

```
# get a token: https://platform.openai.com/account/api-keys

from getpass import getpass

OPENAI_API_KEY = getpass()

```

```
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

```

```
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

```

```
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

```

```
llm = OpenAI()

```

```
llm_chain = LLMChain(prompt=prompt, llm=llm)

```

```
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)

```

```
' Justin Bieber was born in 1994, so we are looking for the Super Bowl winner from that year. The Super Bowl in 1994 was Super Bowl XXVIII, and the winner was the Dallas Cowboys.'

```

