Llama-cpp嵌入
=============

本教程将介绍如何在LangChain中使用Llama-cpp嵌入。

```
!pip install llama-cpp-python

```

```
from langchain.embeddings import LlamaCppEmbeddings

```

```
llama = LlamaCppEmbeddings(model_path="/path/to/model/ggml-model-q4_0.bin")

```

```
text = "This is a test document."

```

```
query_result = llama.embed_query(text)

```

```
doc_result = llama.embed_documents([text])

```

