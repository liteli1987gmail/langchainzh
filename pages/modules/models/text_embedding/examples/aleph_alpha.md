

阿勒夫·阿尔法[#](#aleph-alpha "到这个标题的永久链接")
=====================================

使用阿勒夫·阿尔法的语义嵌入有两种可能的方法。如果您有结构不同的文本（例如文档和查询)，则应使用不对称嵌入。相反，对于结构可比较的文本，建议使用对称嵌入。

不对称[#](#asymmetric "到这个标题的永久链接")
--------------------------------

```
from langchain.embeddings import AlephAlphaAsymmetricSemanticEmbedding

```

```
document = "This is a content of the document"
query = "What is the contnt of the document?"

```

```
embeddings = AlephAlphaAsymmetricSemanticEmbedding()

```

```
doc_result = embeddings.embed_documents([document])

```

```
query_result = embeddings.embed_query(query)

```

对称[#](#symmetric "到这个标题的永久链接")
------------------------------

```
from langchain.embeddings import AlephAlphaSymmetricSemanticEmbedding

```

```
text = "This is a test text"

```

```
embeddings = AlephAlphaSymmetricSemanticEmbedding()

```

```
doc_result = embeddings.embed_documents([text])

```

```
query_result = embeddings.embed_query(text)

```

