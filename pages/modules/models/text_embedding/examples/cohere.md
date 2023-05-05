

连贯性[#](#cohere "Permalink to this headline")
============================================

让我们加载Cohere嵌入类。

```
from langchain.embeddings import CohereEmbeddings

```

```
embeddings = CohereEmbeddings(cohere_api_key=cohere_api_key)

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

