

伪嵌入[#](#fake-embeddings "此标题的永久链接")
===================================

LangChain还提供了一个伪嵌入类。您可以使用它来测试您的pipeline。

```
from langchain.embeddings import FakeEmbeddings

```

```
embeddings = FakeEmbeddings(size=1352)

```

```
query_result = embeddings.embed_query("foo")

```

```
doc_results = embeddings.embed_documents(["foo"])

```

