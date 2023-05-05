


[Writer](https://writer.com/) 是一个生成不同语言内容的平台。

本示例将介绍如何使用LangChain与`Writer` [models](https://dev.writer.com/docs/models)进行交互。

您需要从[此处](https://dev.writer.com/docs)获取`WRITER_API_KEY`。

```
from getpass import getpass

WRITER_API_KEY = getpass()

```

```
import os

os.environ["WRITER_API_KEY"] = WRITER_API_KEY

```

```
from langchain.llms import Writer
from langchain import PromptTemplate, LLMChain

```

```
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

```

```
# If you get an error, probably, you need to set up the "base_url" parameter that can be taken from the error log.

llm = Writer()

```

```
llm_chain = LLMChain(prompt=prompt, llm=llm)

```

```
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)

```

