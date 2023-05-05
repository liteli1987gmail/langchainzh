

Aleph Alpha[#](#aleph-alpha "Permalink to this headline")
=========================================================

[The Luminous series](https://docs.aleph-alpha.com/docs/introduction/luminous/) is a family of large language models.

This example goes over how to use LangChain to interact with Aleph Alpha models

```
# Install the package
!pip install aleph-alpha-client

```

```
# create a new token: https://docs.aleph-alpha.com/docs/account/#create-a-new-token

from getpass import getpass

ALEPH_ALPHA_API_KEY = getpass()

```

```
from langchain.llms import AlephAlpha
from langchain import PromptTemplate, LLMChain

```

```
template = """Q: {question}

A:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

```

```
llm = AlephAlpha(model="luminous-extended", maximum_tokens=20, stop_sequences=["Q:"], aleph_alpha_api_key=ALEPH_ALPHA_API_KEY)

```

```
llm_chain = LLMChain(prompt=prompt, llm=llm)

```

```
question = "What is AI?"

llm_chain.run(question)

```

```
' Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems.\n'

```

