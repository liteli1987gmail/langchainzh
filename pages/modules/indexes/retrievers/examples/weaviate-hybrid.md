

Weaviate混合搜索[#](#weaviate-hybrid-search "Permalink to this headline")
=====================================================================

本笔记本演示了如何使用[Weaviate混合搜索](https://weaviate.io/blog/hybrid-search-explained)作为LangChain检索器。

```
import weaviate
import os

WEAVIATE_URL = "..."
client = weaviate.Client(
    url=WEAVIATE_URL,
)

```

```
from langchain.retrievers.weaviate_hybrid_search import WeaviateHybridSearchRetriever
from langchain.schema import Document

```

```
retriever = WeaviateHybridSearchRetriever(client, index_name="LangChain", text_key="text")

```

```
docs = [Document(page_content="foo")]

```

```
retriever.add_documents(docs)

```

```
['3f79d151-fb84-44cf-85e0-8682bfe145e0']

```

```
retriever.get_relevant_documents("foo")

```

```
[Document(page_content='foo', metadata={})]

```

