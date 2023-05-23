
向量存储 Vectorstore Agent
======


这篇教程展示了一个代理，旨在获取一个或多个向量存储中的信息，可以带有或不带源。

创建向量存储 Create the Vectorstores
---------------------------------------------------------------


```   python
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
llm = OpenAI(temperature=0)

```



```   python
from langchain.document_loaders import TextLoader
loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
state_of_union_store = Chroma.from_documents(texts, embeddings, collection_name="state-of-union")

```



```   python
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.

```



```   python
from langchain.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://beta.ruff.rs/docs/faq/")
docs = loader.load()
ruff_texts = text_splitter.split_documents(docs)
ruff_store = Chroma.from_documents(ruff_texts, embeddings, collection_name="ruff")

```



```   python
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.

```


初始化工具包和代理[#](#initialize-toolkit-and-agent "Permalink to this headline")
-------------------------------------------------------------------------------------------

First, we’ll create an agent with a single vectorstore.


```   python
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo,
)
vectorstore_info = VectorStoreInfo(
    name="state_of_union_address",
    description="the most recent state of the Union adress",
    vectorstore=state_of_union_store
)
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

```


示例 Examples[#](#examples "Permalink to this headline")
---------------------------------------------------


```   python
agent_executor.run("What did biden say about ketanji brown jackson is the state of the union address?")

```



```   python
> Entering new AgentExecutor chain...
 I need to find the answer in the state of the union address
Action: state_of_union_address
Action Input: What did biden say about ketanji brown jackson
Observation:  Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence.
Thought: I now know the final answer
Final Answer: Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence.

> Finished chain.

```



```   python
"Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence."

```



```   python
agent_executor.run("What did biden say about ketanji brown jackson is the state of the union address? List the source.")

```



```   python
> Entering new AgentExecutor chain...
 I need to use the state_of_union_address_with_sources tool to answer this question.
Action: state_of_union_address_with_sources
Action Input: What did biden say about ketanji brown jackson
Observation: {"answer": " Biden said that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson to the United States Supreme Court, and that she is one of the nation's top legal minds who will continue Justice Breyer's legacy of excellence.\n", "sources": "../../state_of_the_union.txt"}
Thought: I now know the final answer
Final Answer: Biden said that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson to the United States Supreme Court, and that she is one of the nation's top legal minds who will continue Justice Breyer's legacy of excellence. Sources: ../../state_of_the_union.txt

> Finished chain.

```



```   python
"Biden said that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson to the United States Supreme Court, and that she is one of the nation's top legal minds who will continue Justice Breyer's legacy of excellence. Sources: ../../state_of_the_union.txt"

```


多个矢量存储Multiple Vectorstores[#](#multiple-vectorstores "Permalink to this headline")
-----------------------------------------------------------------------------

我们也可以很容易地使用这个初始化一个带有多个vectorstore的代理，并使用代理在它们之间路由。做这个。此代理针对路由进行了优化，因此它是一个不同的工具包和初始化器。


```   python
from langchain.agents.agent_toolkits import (
    create_vectorstore_router_agent,
    VectorStoreRouterToolkit,
    VectorStoreInfo,
)

```



```   python
ruff_vectorstore_info = VectorStoreInfo(
    name="ruff",
    description="Information about the Ruff python linting library",
    vectorstore=ruff_store
)
router_toolkit = VectorStoreRouterToolkit(
    vectorstores=[vectorstore_info, ruff_vectorstore_info],
    llm=llm
)
agent_executor = create_vectorstore_router_agent(
    llm=llm,
    toolkit=router_toolkit,
    verbose=True
)

```


示例 Examples[#](#id1 "Permalink to this headline")
----------------------------------------------


```   python
agent_executor.run("What did biden say about ketanji brown jackson is the state of the union address?")

```



```   python
> Entering new AgentExecutor chain...
 I need to use the state_of_union_address tool to answer this question.
Action: state_of_union_address
Action Input: What did biden say about ketanji brown jackson
Observation:  Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence.
Thought: I now know the final answer
Final Answer: Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence.

> Finished chain.

```



```   python
"Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence."

```



```   python
agent_executor.run("What tool does ruff use to run over Jupyter Notebooks?")

```



```   python
> Entering new AgentExecutor chain...
 I need to find out what tool ruff uses to run over Jupyter Notebooks
Action: ruff
Action Input: What tool does ruff use to run over Jupyter Notebooks?
Observation:  Ruff is integrated into nbQA, a tool for running linters and code formatters over Jupyter Notebooks. After installing ruff and nbqa, you can run Ruff over a notebook like so: > nbqa ruff Untitled.ipynb
Thought: I now know the final answer
Final Answer: Ruff is integrated into nbQA, a tool for running linters and code formatters over Jupyter Notebooks. After installing ruff and nbqa, you can run Ruff over a notebook like so: > nbqa ruff Untitled.ipynb

> Finished chain.

```



```   python
'Ruff is integrated into nbQA, a tool for running linters and code formatters over Jupyter Notebooks. After installing ruff and nbqa, you can run Ruff over a notebook like so: > nbqa ruff Untitled.ipynb'

```



```   python
agent_executor.run("What tool does ruff use to run over Jupyter Notebooks? Did the president mention that tool in the state of the union?")

```



```   python
> Entering new AgentExecutor chain...
 I need to find out what tool ruff uses and if the president mentioned it in the state of the union.
Action: ruff
Action Input: What tool does ruff use to run over Jupyter Notebooks?
Observation:  Ruff is integrated into nbQA, a tool for running linters and code formatters over Jupyter Notebooks. After installing ruff and nbqa, you can run Ruff over a notebook like so: > nbqa ruff Untitled.ipynb
Thought: I need to find out if the president mentioned nbQA in the state of the union.
Action: state_of_union_address
Action Input: Did the president mention nbQA in the state of the union?
Observation:  No, the president did not mention nbQA in the state of the union.
Thought: I now know the final answer.
Final Answer: No, the president did not mention nbQA in the state of the union.

> Finished chain.

```



```   python
'No, the president did not mention nbQA in the state of the union.'

```


