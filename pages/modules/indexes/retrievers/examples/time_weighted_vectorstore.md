

时间加权向量存储检索器[#](#time-weighted-vectorstore-retriever "跳转到此标题的永久链接")
==================================================================

这个检索器使用语义相似性和时间新旧性的组合。

评分算法如下：

```
semantic_similarity + (1.0 - decay_rate) ** hours_passed

```

需要注意的是，hours_passed 指的是自上次访问检索器中的对象以来经过的小时数，而不是自创建以来的小时数。这意味着经常访问的对象保持“新鲜”。

```
import faiss

from datetime import datetime, timedelta
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers import TimeWeightedVectorStoreRetriever
from langchain.schema import Document
from langchain.vectorstores import FAISS

```

低衰减率[#](#low-decay-rate "跳转到此标题的永久链接")
--------------------------------------

低衰减率（在此情况下，我们将其设置为接近0)意味着记忆会被“记住”更长时间。衰减率为0意味着记忆永远不会被遗忘，使得这个检索器等同于向量查找。

```
# Define your embedding model
embeddings_model = OpenAIEmbeddings()
# Initialize the vectorstore as empty
embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})
retriever = TimeWeightedVectorStoreRetriever(vectorstore=vectorstore, decay_rate=.0000000000000000000000001, k=1) 

```

```
yesterday = datetime.now() - timedelta(days=1)
retriever.add_documents([Document(page_content="hello world", metadata={"last_accessed_at": yesterday})])
retriever.add_documents([Document(page_content="hello foo")])

```

```
['5c9f7c06-c9eb-45f2-aea5-efce5fb9f2bd']

```

```
# "Hello World" is returned first because it is most salient, and the decay rate is close to 0., meaning it's still recent enough
retriever.get_relevant_documents("hello world")

```

```
[Document(page_content='hello world', metadata={'last_accessed_at': datetime.datetime(2023, 4, 16, 22, 9, 1, 966261), 'created_at': datetime.datetime(2023, 4, 16, 22, 9, 0, 374683), 'buffer_idx': 0})]

```

高衰减率[#](#high-decay-rate "跳转到此标题的永久链接")
---------------------------------------

当衰减因子很高（例如，几个9)，时间新旧性得分很快降为0！如果将其设置为1，对所有对象来说，时间新旧性都是0，这再次使得这个检索器等同于向量查找。

```
# Define your embedding model
embeddings_model = OpenAIEmbeddings()
# Initialize the vectorstore as empty
embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})
retriever = TimeWeightedVectorStoreRetriever(vectorstore=vectorstore, decay_rate=.999, k=1) 

```

```
yesterday = datetime.now() - timedelta(days=1)
retriever.add_documents([Document(page_content="hello world", metadata={"last_accessed_at": yesterday})])
retriever.add_documents([Document(page_content="hello foo")])

```

```
['40011466-5bbe-4101-bfd1-e22e7f505de2']

```

```
# "Hello Foo" is returned first because "hello world" is mostly forgotten
retriever.get_relevant_documents("hello world")

```

```
[Document(page_content='hello foo', metadata={'last_accessed_at': datetime.datetime(2023, 4, 16, 22, 9, 2, 494798), 'created_at': datetime.datetime(2023, 4, 16, 22, 9, 2, 178722), 'buffer_idx': 1})]

```

