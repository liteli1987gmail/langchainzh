Hugging Face嵌入类
===================

让我们加载Hugging Face嵌入类。

```
from langchain.embeddings import HuggingFaceEmbeddings

```

```
embeddings = HuggingFaceEmbeddings()

```

```
text = "This is a test document."

```

```
query_result = embeddings.embed_query(text)

```

```
doc_result = embeddings.embed_documents([text])

```

