

SVM检索器[#](#svm-retriever "此标题的永久链接")
====================================

本教程介绍了如何使用一个在底层使用scikit-learn的SVM的检索器。

主要基于 https://github.com/karpathy/randomfun/blob/master/knn_vs_svm.ipynb

```
from langchain.retrievers import SVMRetriever
from langchain.embeddings import OpenAIEmbeddings

```

```
# !pip install scikit-learn

```

使用文本创建新的检索器[#](#create-new-retriever-with-texts "此标题的永久链接")
-----------------------------------------------------------

```
retriever = SVMRetriever.from_texts(["foo", "bar", "world", "hello", "foo bar"], OpenAIEmbeddings())

```

使用检索器[#](#use-retriever "此标题的永久链接")
-----------------------------------

现在我们可以使用检索器了！

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
 Document(page_content='world', metadata={})]

```

