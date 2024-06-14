# 索引化

这里，我们将使用LangChain索引API来查看基本的索引化工作流程。

索引API允许您从任何来源加载并将文档与向量存储保持同步。具体来说，它有助于：

* 避免将重复内容写入向量存储
* 避免重复写入未更改的内容
* 避免对未更改的内容重新计算嵌入

所有这些都应该帮助您节省时间和金钱，同时提高向量搜索结果。

关键是，索引API甚至适用于已经经历多个转换步骤（例如，通过文本分块）的文档，与原始来源文档相关。

## 工作原理

LangChain索引化利用了一个记录管理器（`RecordManager`），用于跟踪文档写入向量存储。

在索引化内容时，对每个文档计算哈希，并将以下信息存储在记录管理器中：

- 文档哈希（页面内容和元数据的哈希）
- 写入时间
- 源ID -- 每个文档的元数据应包含信息，以便我们确定此文档的最终来源

## 删除模式

将文档索引到向量存储时，可能需要删除一些现有文档。在某些情况下，您可能希望删除与正在索引的新文档来自相同来源的任何现有文档。在其他情况下，您可能希望完全删除所有现有文档。索引API的删除模式可以让您选择所需的行为：

| 清理模式 | 重复内容去重 | 可并行化 | 清除已删除的源文档 | 清理源文档和/或派生文档的变异 | 清理定时 |
|-----------|----------------|-------------|------------------------|-------------------------------------|---------------|
| 无         | ✅             | ✅         | ❌                     | ❌                                | -             |
| 增量     | ✅             | ✅          | ❌                     | ✅                                | 连续的      |
| 完整     | ✅             | ❌         | ✅                     | ✅                                | 索引结束时 |

`无`不进行任何自动清理，允许用户手动清理旧内容。

`增量`和`完整`提供以下自动清理功能：

* 如果源文档或派生文档的内容**发生更改**，无论是`增量`还是`完整`模式都将清除（删除）以前版本的内容。
* 如果源文档已被**删除**（意味着它不包括在当前正在索引的文档中），`完整`清理模式将正确地从向量存储中删除它，但`增量`模式不会。

当内容发生变异（例如，源PDF文件已被修订）时，在索引期间会出现一段时间，新版本和旧版本可能会返回给用户。这发生在新内容写入之后，但旧版本被删除之前。

* `增量`索引化最大程度地减少了这段时间，因为它能够不断进行清理，随即写入。
* `完整`模式在所有批次写入后执行清理。

## 要求

1. 不要与已独立于索引API预先填充内容的存储一起使用，因为记录管理器将不知道以前插入记录。
2. 仅适用于支持LangChain `vectorstore`的向量存储：
   * 按ID添加文档（使用`ids`参数的`add_documents`方法）
   * 按ID删除（使用`ids`参数的`delete`方法）

兼容的向量存储：`AnalyticDB`、`AstraDB`、`AwaDB`、`Bagel`、`Cassandra`、`Chroma`、`CouchbaseVectorStore`、`DashVector`、`DatabricksVectorSearch`、`DeepLake`、`Dingo`、`ElasticVectorSearch`、`ElasticsearchStore`、`FAISS`、`HanaDB`、`Milvus`、`MyScale`、`OpenSearchVectorSearch`、`PGVector`、`Pinecone`、`Qdrant`、`Redis`、`Rockset`、`ScaNN`、`SupabaseVectorStore`、`SurrealDBStore`、`TimescaleVector`、`Vald`、`VDMS`、`Vearch`、`VespaStore`、`Weaviate`、`ZepVectorStore`、`TencentVectorDB`、`OpenSearchVectorSearch`。
  
## 注意

记录管理器依赖基于时间的机制来确定可以清理的内容（当使用`完整`或`增量`清理模式时）。

如果两个任务连续运行，第一个任务在时间更改之前完成，那么第二个任务可能无法清理内容。

在实际设置中，这不太可能成为问题，原因如下：

1. RecordManager使用更高分辨率的时间戳。
2. 数据需要在第一个任务和第二个任务运行之间更改，如果任务之间的时间间隔很短，则这种情况变得不太可能。
3. 索引任务通常需要超过几毫秒。

## 快速入门


```python
from langchain.indexes import SQLRecordManager, index
from langchain_core.documents import Document
from langchain_elasticsearch import ElasticsearchStore
from langchain_openai import OpenAIEmbeddings
```

初始化一个向量存储并设置嵌入：


```python
collection_name = "test_index"

embedding = OpenAIEmbeddings()

vectorstore = ElasticsearchStore(
    es_url="http://localhost:9200", index_name="test_index", embedding=embedding
)
```

使用适当的命名空间初始化记录管理器。

**建议：** 使用一个考虑到向量存储和向量存储中的集合名称的命名空间；例如，'redis/my_docs'、'chromadb/my_docs'或'postgres/my_docs'。


```python
namespace = f"elasticsearch/{collection_name}"
record_manager = SQLRecordManager(
    namespace, db_url="sqlite:///record_manager_cache.sql"
)
```

在使用记录管理器之前创建架构。


```python
record_manager.create_schema()
```

让我们索引一些测试文档：


```python
doc1 = Document(page_content="kitty", metadata={"source": "kitty.txt"})
doc2 = Document(page_content="doggy", metadata={"source": "doggy.txt"})
```

将文档索引为空的向量存储：


```python
def _clear():
    """Hacky helper method to clear content. See the `full` mode section to to understand why it works."""
    index([], record_manager, vectorstore, cleanup="full", source_id_key="source")
```

### ``无`` 删除模式

这种模式不会自动清除旧版本的内容；但是，它仍会处理内容去重。


```python
_clear()
```


```python
index(
    [doc1, doc1, doc1, doc1, doc1],
    record_manager,
    vectorstore,
    cleanup=None,
    source_id_key="source",
)
```



```
    {'num_added': 1, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}
```



```python
_clear()
```


```python
index([doc1, doc2], record_manager, vectorstore, cleanup=None, source_id_key="source")
```



```
    {'num_added': 2, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}
```


第二次处理时，所有内容都将被跳过：


```python
index([doc1, doc2], record_manager, vectorstore, cleanup=None, source_id_key="source")
```


```

    {'num_added': 0, 'num_updated': 0, 'num_skipped': 2, 'num_deleted': 0}
```


### ``"增量"`` 删除模式


```python
_clear()
```


```python
index(
    [doc1, doc2],
    record_manager,
    vectorstore,
    cleanup="incremental",
    source_id_key="source",
)
```



```
    {'num_added': 2, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}

```

再次索引应导致两个文档都被**跳过** -- 同时跳过嵌入操作！


```python
index(
    [doc1, doc2],
    record_manager,
    vectorstore,
    cleanup="incremental",
    source_id_key="source",
)
```



```
    {'num_added': 0, 'num_updated': 0, 'num_skipped': 2, 'num_deleted': 0}

```

如果在增量索引模式下不提供任何文档，则不会发生任何改变。


```python
index([], record_manager, vectorstore, cleanup="incremental", source_id_key="source")
```



```
    {'num_added': 0, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}
```


如果我们突变文档，新版本将被写入，所有共享相同来源的旧版本将被删除。


```python
changed_doc_2 = Document(page_content="puppy", metadata={"source": "doggy.txt"})
```


```python
index(
    [changed_doc_2],
    record_manager,
    vectorstore,
    cleanup="incremental",
    source_id_key="source",
)
```



```
    {'num_added': 1, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 1}
```



### ``"full"`` deletion mode

在 `full` 模式下，用户应该将应该被索引的 `full` 内容传递给索引函数。

任何未传递到索引函数中但存在于向量存储中的文档都将被删除！

这种行为对处理源文档的删除很有用。

```python
_clear()
```

```python
all_docs = [doc1, doc2]
```

```python
index(all_docs, record_manager, vectorstore, cleanup="full", source_id_key="source")
```

{'num_added': 2, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}

假设有人删除了第一个文档：

```python
del all_docs[0]
```

```python
all_docs
```

[Document(page_content='doggy', metadata={'source': 'doggy.txt'})]

使用full模式将清除已删除的内容。

```python
index(all_docs, record_manager, vectorstore, cleanup="full", source_id_key="source")
```

{'num_added': 0, 'num_updated': 0, 'num_skipped': 1, 'num_deleted': 1}

## Source

metadata属性包含一个名为 `source` 的字段。这个源应该指向与给定文档相关联的最终来源。

例如，如果这些文档代表某个父文档的各个部分，那么这两个文档的 `source` 应该相同，并引用父文档。

一般来说，总是应该指定 `source`。只有在你 **绝对不** 打算使用 `incremental` 模式，并且由于某种原因无法正确设置 `source` 字段时才使用 `None`。

```python
from langchain_text_splitters import CharacterTextSplitter
```

```python
doc1 = Document(
    page_content="kitty kitty kitty kitty kitty", metadata={"source": "kitty.txt"}
)
doc2 = Document(page_content="doggy doggy the doggy", metadata={"source": "doggy.txt"})
```

```python
new_docs = CharacterTextSplitter(
    separator="t", keep_separator=True, chunk_size=12, chunk_overlap=2
).split_documents([doc1, doc2])
new_docs
```
```
[Document(page_content='kitty kit', metadata={'source': 'kitty.txt'}),
 Document(page_content='tty kitty ki', metadata={'source': 'kitty.txt'}),
 Document(page_content='tty kitty', metadata={'source': 'kitty.txt'}),
 Document(page_content='doggy doggy', metadata={'source': 'doggy.txt'}),
 Document(page_content='the doggy', metadata={'source': 'doggy.txt'})]
```
```python
_clear()
```

```python
index(
    new_docs,
    record_manager,
    vectorstore,
    cleanup="incremental",
    source_id_key="source",
)
```

{'num_added': 5, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}

```python
changed_doggy_docs = [
    Document(page_content="woof woof", metadata={"source": "doggy.txt"}),
    Document(page_content="woof woof woof", metadata={"source": "doggy.txt"}),
]
```

这将删除与 `doggy.txt` 源关联的旧版本文档，并用新版本替换它们。

```python
index(
    changed_doggy_docs,
    record_manager,
    vectorstore,
    cleanup="incremental",
    source_id_key="source",
)
```
```
{'num_added': 2, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 2}
```
```python
vectorstore.similarity_search("dog", k=30)
```
```
[Document(page_content='woof woof', metadata={'source': 'doggy.txt'}),
 Document(page_content='woof woof woof', metadata={'source': 'doggy.txt'}),
 Document(page_content='tty kitty', metadata={'source': 'kitty.txt'}),
 Document(page_content='tty kitty ki', metadata={'source': 'kitty.txt'}),
 Document(page_content='kitty kit', metadata={'source': 'kitty.txt'})]
```
## 使用加载器

索引可以接受文档的可迭代对象或任何加载器。

**注意：** 加载器 **必须** 正确设置源键。

```python
from langchain_community.document_loaders.base import BaseLoader

class MyCustomLoader(BaseLoader):
    def lazy_load(self):
        text_splitter = CharacterTextSplitter(
            separator="t", keep_separator=True, chunk_size=12, chunk_overlap=2
        )
        docs = [
            Document(page_content="woof woof", metadata={"source": "doggy.txt"}),
            Document(page_content="woof woof woof", metadata={"source": "doggy.txt"}),
        ]
        yield from text_splitter.split_documents(docs)
    
    def load(self):
        return list(self.lazy_load())
```

```python
_clear()
```=======

```python
loader = MyCustomLoader()
```


```python
loader.load()
```




    [Document(page_content='woof woof', metadata={'source': 'doggy.txt'}),
     Document(page_content='woof woof woof', metadata={'source': 'doggy.txt'})]




```python
index(loader, record_manager, vectorstore, cleanup="full", source_id_key="source")
```




    {'num_added': 2, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}




```python
vectorstore.similarity_search("dog", k=30)
```




    [Document(page_content='woof woof', metadata={'source': 'doggy.txt'}),
     Document(page_content='woof woof woof', metadata={'source': 'doggy.txt'})]
