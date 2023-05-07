

Chroma[#](#chroma "Permalink to this headline")
===============================================

> 
> [Chroma](https://docs.trychroma.com/getting-started)是用于构建具有嵌入的人工智能应用程序的数据库。
> 
> 
> 

这个笔记本展示了与 `Chroma` 向量数据库相关的功能如何使用。

```
!pip install chromadb

```

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
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader

```

```
from langchain.document_loaders import TextLoader
loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

```

```
db = Chroma.from_documents(docs, embeddings)

query = "What did the president say about Ketanji Brown Jackson"
docs = db.similarity_search(query)

```

```
Using embedded DuckDB without persistence: data will be transient

```

```
print(docs[0].page_content)

```

```
Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```

带有分数的相似度搜索[#](#similarity-search-with-score "Permalink to this headline")
-------------------------------------------------------------------------

```
docs = db.similarity_search_with_score(query)

```

```
docs[0]

```

```
(Document(page_content='Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', metadata={'source': '../../../state_of_the_union.txt'}),
 0.3949805498123169)

```

持久化[#](#persistance "Permalink to this headline")
-------------------------------------------------

以下步骤介绍了如何持久化 ChromaDB 实例。

### 初始化 PeristedChromaDB[#](#initialize-peristedchromadb "Permalink to this headline")

为每个块创建嵌入并将其插入 Chroma 向量数据库。persist_directory 参数告诉 ChromaDB 在持久化时将数据库存储在何处。

```
# Embed and store the texts
# Supplying a persist_directory will store the embeddings on disk
persist_directory = 'db'

embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory=persist_directory)

```

```
Running Chroma using direct local API.
No existing DB found in db, skipping load
No existing DB found in db, skipping load

```

### 持久化数据库[#](#persist-the-database "Permalink to this headline")

我们应该调用 persist() 确保嵌入被写入磁盘。

```
vectordb.persist()
vectordb = None

```

```
Persisting DB to disk, putting it in the save folder db
PersistentDuckDB del, about to run persist
Persisting DB to disk, putting it in the save folder db

```

### 从磁盘加载数据库并创建链[#](#load-the-database-from-disk-and-create-the-chain "本标题的永久链接")

确保传递与实例化数据库时相同的persist_directory和embedding_function。初始化我们将用于问题回答的链。

```
# Now we can load the persisted database from disk, and use it as normal. 
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

```

```
Running Chroma using direct local API.
loaded in 4 embeddings
loaded in 1 collections

```

Retriever选项[#](#retriever-options "本标题的永久链接")
---------------------------------------------

本节介绍使用Chroma作为检索器的不同选项。

### MMR[#](#mmr "本标题的永久链接")

除了在检索器对象中使用相似性搜索之外，您还可以使用`mmr`。

```
retriever = db.as_retriever(search_type="mmr")

```

```
retriever.get_relevant_documents(query)[0]

```

```
Document(page_content='Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', metadata={'source': '../../../state_of_the_union.txt'})

```

