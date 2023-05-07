

从LangChainHub加载[＃](#loading-from-langchainhub "此标题的永久链接")
=========================================================

本笔记涵盖了如何从[LangChainHub](https://github.com/hwchase17/langchain-hub)加载链。

```
from langchain.chains import load_chain

chain = load_chain("lc://chains/llm-math/chain.json")

```

```
chain.run("whats 2 raised to .12")

```

```
> Entering new LLMMathChain chain...
whats 2 raised to .12
Answer: 1.0791812460476249
> Finished chain.

```

```
'Answer: 1.0791812460476249'

```

有时，链会需要额外的参数，这些参数没有与链一起序列化。例如，对于在向量数据库上进行问题回答的链，将需要一个向量数据库。

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA

```

```
from langchain.document_loaders import TextLoader
loader = TextLoader('../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(texts, embeddings)

```

```
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.

```

```
chain = load_chain("lc://chains/vector-db-qa/stuff/chain.json", vectorstore=vectorstore)

```

```
query = "What did the president say about Ketanji Brown Jackson"
chain.run(query)

```

```
" The president said that Ketanji Brown Jackson is a Circuit Court of Appeals Judge, one of the nation's top legal minds, a former top litigator in private practice, a former federal public defender, has received a broad range of support from the Fraternal Order of Police to former judges appointed by Democrats and Republicans, and will continue Justice Breyer's legacy of excellence."

```

