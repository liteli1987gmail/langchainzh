

外星人吃了。。。

[Writer](https://writer.com/) is a platform to generate different language content.

This example goes over how to use LangChain to interact with `Writer` [models](https://dev.writer.com/docs/models).

You have to get the WRITER_API_KEY [here](https://dev.writer.com/docs).

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

