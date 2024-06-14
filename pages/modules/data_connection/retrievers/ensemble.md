# 集成检索器

`EnsembleRetriever` 接受一个检索器的列表作为输入，将它们的 `get_relevant_documents()` 方法的结果进行集成，并根据 [Reciprocal Rank Fusion](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) 算法重新排序结果。

通过充分利用不同算法的优势，`EnsembleRetriever` 可以实现比任何单一算法更好的性能。

最常见的模式是将稀疏检索器（如BM25）与稠密检索器（如嵌入相似度）结合起来，因为它们的优势互补。这也被称为"混合搜索"。稀疏检索器根据关键词能够有效地找到相关文档，而稠密检索器则能够根据语义相似性找到相关文档。

```python
%pip install --upgrade --quiet  rank_bm25 > /dev/null
```

```python
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
```

```python
doc_list_1 = [
    "I like apples",
    "I like oranges",
    "Apples and oranges are fruits",
]

# 初始化BM25检索器和FAISS检索器
bm25_retriever = BM25Retriever.from_texts(
    doc_list_1, metadatas=[{"source": 1}] * len(doc_list_1)
)
bm25_retriever.k = 2

doc_list_2 = [
    "You like apples",
    "You like oranges",
]

embedding = OpenAIEmbeddings()
faiss_vectorstore = FAISS.from_texts(
    doc_list_2, embedding, metadatas=[{"source": 2}] * len(doc_list_2)
)
faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": 2})

# 初始化集成检索器
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, faiss_retriever], weights=[0.5, 0.5]
)
```

```python
docs = ensemble_retriever.invoke("apples")
docs
```

## 运行时配置

我们也可以在运行时配置检索器。为了做到这一点，我们需要将字段标记为可配置的。

```python
from langchain_core.runnables import ConfigurableField
```

```python
faiss_retriever = faiss_vectorstore.as_retriever(
    search_kwargs={"k": 2}
).configurable_fields(
    search_kwargs=ConfigurableField(
        id="search_kwargs_faiss",
        name="Search Kwargs",
        description="The search kwargs to use",
    )
)
```

```python
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, faiss_retriever], weights=[0.5, 0.5]
)
```

```python
config = {"configurable": {"search_kwargs_faiss": {"k": 1}}}
docs = ensemble_retriever.invoke("apples", config=config)
docs
```

注意，这里只返回了 FAISS 检索器中的一个来源，因为我们在运行时传入了相应的配置。



