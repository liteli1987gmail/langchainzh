

FAISS[#](#faiss "到此标题的永久链接")
============================

> 
> [Facebook AI 相似度搜索（Faiss)](https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/)是一种用于稠密向量的高效相似度搜索和聚类的库。它包含了能够搜索任意大小的向量集合的算法，甚至包括可能不适合内存的向量集合。它还包含用于评估和参数调整的支持代码。
> 
> 
> 

[Faiss 文档](https://faiss.ai/)。

这个笔记本展示了如何使用与 `FAISS` 向量数据库相关的功能。

```
#!pip install faiss
# OR
!pip install faiss-cpu

```

我们想使用 OpenAIEmbeddings，所以我们必须获取 OpenAI API 密钥。

```
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

```

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
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
db = FAISS.from_documents(docs, embeddings)

query = "What did the president say about Ketanji Brown Jackson"
docs = db.similarity_search(query)

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

带有分数的相似度搜索[#](#similarity-search-with-score "到此标题的永久链接")
--------------------------------------------------------

有一些特定于 FAISS 的方法。其中之一是 `similarity_search_with_score`，它允许您返回查询与文档之间的相似度分数。

```
docs_and_scores = db.similarity_search_with_score(query)

```

```
docs_and_scores[0]

```

```
(Document(page_content='In state after state, new laws have been passed, not only to suppress the vote, but to subvert entire elections.   We cannot let this happen.   Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', lookup_str='', metadata={'source': '../../state_of_the_union.txt'}, lookup_index=0),
 0.3914415)

```

使用`similarity_search_by_vector`可以搜索与给定嵌入向量类似的文档，该函数接受嵌入向量作为参数而不是字符串。

```
embedding_vector = embeddings.embed_query(query)
docs_and_scores = db.similarity_search_by_vector(embedding_vector)

```

保存和加载[#](#saving-and-loading "本节标题的永久链接")
-----------------------------------------

您还可以保存和加载FAISS索引。这很有用，这样您就不必每次使用时都重新创建它。

```
db.save_local("faiss_index")

```

```
new_db = FAISS.load_local("faiss_index", embeddings)

```

```
docs = new_db.similarity_search(query)

```

```
docs[0]

```

```
Document(page_content='In state after state, new laws have been passed, not only to suppress the vote, but to subvert entire elections.   We cannot let this happen.   Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', lookup_str='', metadata={'source': '../../state_of_the_union.txt'}, lookup_index=0)

```

合并[#](#merging "本节标题的永久链接")
---------------------------

您还可以合并两个FAISS向量存储

```
db1 = FAISS.from_texts(["foo"], embeddings)
db2 = FAISS.from_texts(["bar"], embeddings)

```

```
db1.docstore._dict

```

```
{'e0b74348-6c93-4893-8764-943139ec1d17': Document(page_content='foo', lookup_str='', metadata={}, lookup_index=0)}

```

```
db2.docstore._dict

```

```
{'bdc50ae3-a1bb-4678-9260-1b0979578f40': Document(page_content='bar', lookup_str='', metadata={}, lookup_index=0)}

```

```
db1.merge_from(db2)

```

```
db1.docstore._dict

```

```
{'e0b74348-6c93-4893-8764-943139ec1d17': Document(page_content='foo', lookup_str='', metadata={}, lookup_index=0),
 'd5211050-c777-493d-8825-4800e74cfdb6': Document(page_content='bar', lookup_str='', metadata={}, lookup_index=0)}

```

