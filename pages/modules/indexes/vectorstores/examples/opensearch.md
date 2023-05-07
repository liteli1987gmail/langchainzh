
OpenSearch
=== 
> 
> [OpenSearch](https://opensearch.org/) 是一个可扩展、灵活和可扩展的开源软件套件，用于搜索、分析和可观测应用，其许可证为 Apache 2.0。`OpenSearch`是一个基于`Apache Lucene`的分布式搜索和分析引擎。
> 
> 
> 

此笔记本演示了如何使用与`OpenSearch`数据库相关的功能。

要运行，您应该启动并运行opensearch实例：[here](https://opensearch.org/docs/latest/install-and-configure/install-opensearch/index/) `similarity_search`默认执行Approximate k-NN搜索，它使用几个算法之一，如Lucene、Nmslib、Faiss，推荐用于大型数据集。要执行暴力搜索，我们有其他搜索方法，称为脚本评分和无痛脚本。请查看[此文档](https://opensearch.org/docs/latest/search-plugins/knn/index/)了解更多详细信息。

```
!pip install opensearch-py

```

我们希望使用OpenAIEmbeddings，因此我们必须获取OpenAI API密钥。

```
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

```

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import OpenSearchVectorSearch
from langchain.document_loaders import TextLoader

```

```
from langchain.document_loaders import TextLoader
loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

```

```
docsearch = OpenSearchVectorSearch.from_documents(docs, embeddings, opensearch_url="http://localhost:9200")

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)

```

```
print(docs[0].page_content)

```

使用自定义参数的近似k-NN搜索相似度[＃](#similarity-search-using-approximate-k-nn-search-with-custom-parameters "此标题的永久链接")
----------------------------------------------------------------------------------------------------------

```
docsearch = OpenSearchVectorSearch.from_documents(docs, embeddings, opensearch_url="http://localhost:9200", engine="faiss", space_type="innerproduct", ef_construction=256, m=48)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)

```

```
print(docs[0].page_content)

```

使用自定义参数的脚本评分相似度搜索[＃](#similarity-search-using-script-scoring-with-custom-parameters "此标题的永久链接")
-----------------------------------------------------------------------------------------------

```
docsearch = OpenSearchVectorSearch.from_documents(docs, embeddings, opensearch_url="http://localhost:9200", is_appx_search=False)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search("What did the president say about Ketanji Brown Jackson", k=1, search_type="script_scoring")

```

```
print(docs[0].page_content)

```

使用自定义参数的Painless脚本搜索相似度[＃](#similarity-search-using-painless-scripting-with-custom-parameters "此标题的永久链接")
---------------------------------------------------------------------------------------------------------

```
docsearch = OpenSearchVectorSearch.from_documents(docs, embeddings, opensearch_url="http://localhost:9200", is_appx_search=False)
filter = {"bool": {"filter": {"term": {"text": "smuggling"}}}}
query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search("What did the president say about Ketanji Brown Jackson", search_type="painless_scripting", space_type="cosineSimilarity", pre_filter=filter)

```

```
print(docs[0].page_content)

```

使用现有的OpenSearch实例[＃](#using-a-preexisting-opensearch-instance "此标题的永久链接")
-------------------------------------------------------------------------

还可以使用已有向量的文档与现有的OpenSearch实例。

```
# this is just an example, you would need to change these values to point to another opensearch instance
docsearch = OpenSearchVectorSearch(index_name="index-*", embedding_function=embeddings, opensearch_url="http://localhost:9200")

# you can specify custom field names to match the fields you're using to store your embedding, document text value, and metadata
docs = docsearch.similarity_search("Who was asking about getting lunch today?", search_type="script_scoring", space_type="cosinesimil", vector_field="message_embedding", text_field="message", metadata_field="message_metadata")

```

