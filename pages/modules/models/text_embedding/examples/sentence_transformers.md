SentenceTransformers
======

[SentenceTransformers](https://www.sbert.net/)嵌入是使用`HuggingFaceEmbeddings`集成调用的。 我们还为那些更熟悉直接使用该包的用户添加了`SentenceTransformerEmbeddings`的别名。

SentenceTransformers是一个Python软件包，它可以生成文本和图像嵌入，源自于[Sentence-BERT](https://arxiv.org/abs/1908.10084)。

```
!pip install sentence_transformers > /dev/null

```

```
[notice] A new release of pip is available: 23.0.1 -> 23.1.1
[notice] To update, run: pip install --upgrade pip

```

```
from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings 

```

```
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# Equivalent to SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

```

```
text = "This is a test document."

```

```
query_result = embeddings.embed_query(text)

```

```
doc_result = embeddings.embed_documents([text, "This is not a test document."])

```

