

TF-IDF检索器[＃](#tf-idf-retriever "永久链接到此标题")
==========================================

本教程概述了如何使用使用scikit-learn的TF-IDF的检索器。

有关TF-IDF详细信息，请参见[此博客文章](https://medium.com/data-science-bootcamp/tf-idf-basics-of-information-retrieval-48de122b2a4c)。

```
from langchain.retrievers import TFIDFRetriever

```

```
# !pip install scikit-learn

```

使用文本创建新的检索器[＃](#create-new-retriever-with-texts "永久链接到此标题")
-----------------------------------------------------------

```
retriever = TFIDFRetriever.from_texts(["foo", "bar", "world", "hello", "foo bar"])

```

使用检索器[＃](#use-retriever "永久链接到此标题")
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

