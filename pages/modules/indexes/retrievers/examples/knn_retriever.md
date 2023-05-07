

This notebook goes over how to use a retriever that under the hood uses an kNN.

Largely based on https://github.com/karpathy/randomfun/blob/master/knn_vs_svm.ipynb

```
from langchain.retrievers import KNNRetriever
from langchain.embeddings import OpenAIEmbeddings

```

Create New Retriever with Texts[#](#create-new-retriever-with-texts "Permalink to this headline")
-------------------------------------------------------------------------------------------------

```
retriever = KNNRetriever.from_texts(["foo", "bar", "world", "hello", "foo bar"], OpenAIEmbeddings())

```

Use Retriever[#](#use-retriever "Permalink to this headline")
-------------------------------------------------------------

We can now use the retriever!

```
result = retriever.get_relevant_documents("foo")

```

```
result

```

```
[Document(page_content='foo', metadata={}),
 Document(page_content='foo bar', metadata={}),
 Document(page_content='hello', metadata={}),
 Document(page_content='bar', metadata={})]

```

