# 缓存

嵌入可以被存储或临时缓存，以避免需要重新计算它们。

可以使用 `CacheBackedEmbeddings` 来缓存嵌入。缓存支持的嵌入器是一个包装器，它会将嵌入存储在键值存储中。文本被散列，散列用作缓存中的键。

主要支持初始化 `CacheBackedEmbeddings` 的方式是 `from_bytes_store`。它需要以下参数:

- underlying_embedder: 用于嵌入的嵌入器。
- document_embedding_cache: 用于缓存文档嵌入的任何 [`ByteStore`](/docs/integrations/stores/)。
- batch_size: (可选，默认为 `None`) 在存储更新之间要嵌入的文档数。
- namespace: (可选，默认为 `""`) 用于文档缓存的命名空间。此命名空间用于避免与其他缓存发生冲突。例如，将其设置为所使用的嵌入模型的名称。

**注意**:

- 确保设置 `namespace` 参数以避免使用不同嵌入模型嵌入的相同文本的冲突。
- 目前 `CacheBackedEmbeddings` 不缓存使用 `embed_query()` 和 `aembed_query()` 方法创建的嵌入。

```python
from langchain.embeddings import CacheBackedEmbeddings
```

## 使用向量存储

首先，让我们看一个示例，该示例使用本地文件系统存储嵌入，并使用 FAISS 向量存储进行检索。

```python
%pip install --upgrade --quiet langchain-openai faiss-cpu
```

```python
from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

underlying_embeddings = OpenAIEmbeddings()

store = LocalFileStore("./cache/")

cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings, store, namespace=underlying_embeddings.model
)
```

在嵌入之前，缓存是空的：

```python
list(store.yield_keys())
```

加载文档，将其拆分为块，嵌入每个块并将其加载到向量存储中。

```python
raw_documents = TextLoader("../../state_of_the_union.txt").load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
```

创建向量存储：

```python
%%time
db = FAISS.from_documents(documents, cached_embedder)
```

如果尝试重新创建向量存储，速度会更快，因为不需要重新计算任何嵌入。

```python
%%time
db2 = FAISS.from_documents(documents, cached_embedder)
```

以下是一些已创建的嵌入：

```python
list(store.yield_keys())[:5]
```

# 切换 `ByteStore`

为了使用不同的 `ByteStore`，只需在创建 `CacheBackedEmbeddings` 时使用它。下面，我们创建一个等效的缓存嵌入对象，但使用非持久的 `InMemoryByteStore`：

```python
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import InMemoryByteStore

store = InMemoryByteStore()

cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings, store, namespace=underlying_embeddings.model
)
```