

入门指南[#](#getting-started "Permalink to this headline")
======================================================

该笔记本展示了与向量存储相关的基本功能。处理向量存储的关键部分是创建要放入其中的向量，这通常是通过嵌入来创建的。因此，在深入研究此功能之前，建议您熟悉嵌入笔记本。

这涵盖了与所有向量存储相关的通用高级功能。

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

```

```
with open('../../state_of_the_union.txt') as f:
    state_of_the_union = f.read()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(state_of_the_union)

embeddings = OpenAIEmbeddings()

```

```
docsearch = Chroma.from_texts(texts, embeddings)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)

```

```
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.

```

```
print(docs[0].page_content)

```

```
In state after state, new laws have been passed, not only to suppress the vote, but to subvert entire elections. 

We cannot let this happen. 

Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```

添加文本[#](#add-texts "Permalink to this headline")
------------------------------------------------

您可以使用`add_texts`方法轻松地将文本添加到向量存储中。它将返回文档ID的列表（以防您需要在下游使用它们)。

```
docsearch.add_texts(["Ankush went to Princeton"])

```

```
['a05e3d0c-ab40-11ed-a853-e65801318981']

```

```
query = "Where did Ankush go to college?"
docs = docsearch.similarity_search(query)

```

```
docs[0]

```

```
Document(page_content='Ankush went to Princeton', lookup_str='', metadata={}, lookup_index=0)

```

来自文档[#](#from-documents "Permalink to this headline")
-----------------------------------------------------

我们也可以直接从文档初始化向量存储。当我们使用文本拆分器方法直接获取文档时，这非常有用（当原始文档有相关元数据时很方便)。

```
documents = text_splitter.create_documents([state_of_the_union], metadatas=[{"source": "State of the Union"}])

```

```
docsearch = Chroma.from_documents(documents, embeddings)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)

```

```
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.

```

```
print(docs[0].page_content)

```

```
In state after state, new laws have been passed, not only to suppress the vote, but to subvert entire elections. 

We cannot let this happen. 

Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```

