

OpenAI[#](#openai "此标题的永久链接")
===============================================

让我们加载OpenAI嵌入类。

```
from langchain.embeddings import OpenAIEmbeddings

```

```
embeddings = OpenAIEmbeddings()

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

让我们加载带有第一代模型（例如“text-search-ada-doc-001 / text-search-ada-query-001”）的OpenAI嵌入类。注意：这些不是推荐的模型-请参见[此处](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)。

```
from langchain.embeddings.openai import OpenAIEmbeddings

```

```
embeddings = OpenAIEmbeddings()

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

