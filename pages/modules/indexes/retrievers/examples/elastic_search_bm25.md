

ElasticSearch BM25[#](#elasticsearch-bm25 "本标题的永久链接")
=====================================================

本笔记本介绍了如何使用一个检索器，其底层使用ElasticSearcha和BM25。

要了解BM25的详细信息，请参阅[此博客文章](https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables)。

```
from langchain.retrievers import ElasticSearchBM25Retriever

```

创建新的检索器[#](#create-new-retriever "本标题的永久链接")
--------------------------------------------

```
elasticsearch_url="http://localhost:9200"
retriever = ElasticSearchBM25Retriever.create(elasticsearch_url, "langchain-index-4")

```

```
# Alternatively, you can load an existing index
# import elasticsearch
# elasticsearch_url="http://localhost:9200"
# retriever = ElasticSearchBM25Retriever(elasticsearch.Elasticsearch(elasticsearch_url), "langchain-index")

```

添加文本（如果必要)[#](#add-texts-if-necessary "本标题的永久链接")
-------------------------------------------------

我们可以选择向检索器中添加文本（如果它们还没有在其中)

```
retriever.add_texts(["foo", "bar", "world", "hello", "foo bar"])

```

```
['cbd4cb47-8d9f-4f34-b80e-ea871bc49856',
 'f3bd2e24-76d1-4f9b-826b-ec4c0e8c7365',
 '8631bfc8-7c12-48ee-ab56-8ad5f373676e',
 '8be8374c-3253-4d87-928d-d73550a2ecf0',
 'd79f457b-2842-4eab-ae10-77aa420b53d7']

```

使用检索器[#](#use-retriever "本标题的永久链接")
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
 Document(page_content='foo bar', metadata={})]

```

