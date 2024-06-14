# 基于时间加权向量存储检索器

这个检索器使用语义相似性和时间衰减的结合。

计算它们的算法是:

```
semantic_similarity + (1.0 - decay_rate) ^ hours_passed
```

值得注意的是，`hours_passed`指的是自检索器中的对象**上次被访问**以来经过的小时数，并不是自创建以来的时间。这意味着频繁访问的对象将保持“新鲜”状态。



```python
from datetime import datetime, timedelta

import faiss
from langchain.retrievers import TimeWeightedVectorStoreRetriever
from langchain_community.docstore import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
```

## 低衰减率

低`decay rate`（在这个例子中，我们将它设定得非常低，接近于0）意味着记忆将被持久记住。衰减率为0表示记忆永远不会被遗忘，使得这个检索器等同于向量查找。



```python
# 定义你的嵌入模型
embeddings_model = OpenAIEmbeddings()
# 初始化为空的向量存储
embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore = FAISS(embeddings_model, index, InMemoryDocstore({}), {})
retriever = TimeWeightedVectorStoreRetriever(
    vectorstore=vectorstore, decay_rate=0.0000000000000000000000001, k=1
)
```


```python
yesterday = datetime.now() - timedelta(days=1)
retriever.add_documents(
    [Document(page_content="hello world", metadata={"last_accessed_at": yesterday})]
)
retriever.add_documents([Document(page_content="hello foo")])
```




    ['c3dcf671-3c0a-4273-9334-c4a913076bfa']




```python
# "Hello World" 被首先返回，因为它最突出，且衰减率接近于0，意味着仍然足够新鲜
retriever.get_relevant_documents("hello world")
```




    [Document(page_content='hello world', metadata={'last_accessed_at': datetime.datetime(2023, 12, 27, 15, 30, 18, 457125), 'created_at': datetime.datetime(2023, 12, 27, 15, 30, 8, 442662), 'buffer_idx': 0})]



## 高衰减率

当`decay rate`较高（例如，多个9），`recency score`迅速降为0! 如果将衰减率设置为1，那么所有对象的`recency`都为0，再次使得这等同于向量查找。



```python
# 定义你的嵌入模型
embeddings_model = OpenAIEmbeddings()
# 初始化为空的向量存储
embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore = FAISS(embeddings_model, index, InMemoryDocstore({}), {})
retriever = TimeWeightedVectorStoreRetriever(
    vectorstore=vectorstore, decay_rate=0.999, k=1
)
```


```python
yesterday = datetime.now() - timedelta(days=1)
retriever.add_documents(
    [Document(page_content="hello world", metadata={"last_accessed_at": yesterday})]
)
retriever.add_documents([Document(page_content="hello foo")])
```




    ['eb1c4c86-01a8-40e3-8393-9a927295a950']




```python
# "Hello Foo" 被首先返回，因为"hello world"已经大部分被遗忘
retriever.get_relevant_documents("hello world")
```




    [Document(page_content='hello foo', metadata={'last_accessed_at': datetime.datetime(2023, 12, 27, 15, 30, 50, 57185), 'created_at': datetime.datetime(2023, 12, 27, 15, 30, 44, 720490), 'buffer_idx': 1})]



## 虚拟时间

使用LangChain中的一些工具，你可以模拟时间组件。



```python
import datetime

from langchain.utils import mock_now
```


```python
# 注意上次访问时间是这个日期时间
with mock_now(datetime.datetime(2024, 2, 3, 10, 11)):
    print(retriever.get_relevant_documents("hello world"))
```

    [Document(page_content='hello world', metadata={'last_accessed_at': MockDateTime(2024, 2, 3, 10, 11), 'created_at': datetime.datetime(2023, 12, 27, 15, 30, 44, 532941), 'buffer_idx': 0})]
    


```python

```