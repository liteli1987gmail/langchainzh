TensorflowHub
=====

让我们加载TensorflowHub嵌入类。

```
from langchain.embeddings import TensorflowHubEmbeddings

```

```
embeddings = TensorflowHubEmbeddings()

```

```
2023-01-30 23:53:01.652176: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-01-30 23:53:34.362802: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

```

```
text = "This is a test document."

```

```
query_result = embeddings.embed_query(text)

```

```
doc_results = embeddings.embed_documents(["foo"])

```

```
doc_results

```

