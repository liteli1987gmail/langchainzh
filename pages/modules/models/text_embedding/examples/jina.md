

Jina Embedding
======

让我们加载`Jina Embedding`类.

```
from langchain.embeddings import JinaEmbeddings

```

```
embeddings = JinaEmbeddings(jina_auth_token=jina_auth_token, model_name="ViT-B-32::openai")

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

In the above example, `ViT-B-32::openai`, OpenAI’s pretrained `ViT-B-32` model is used. For a full list of models, see [here](https://cloud.jina.ai/user/inference/model/63dca9df5a0da83009d519cd).

