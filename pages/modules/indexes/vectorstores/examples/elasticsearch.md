
Elasticsearch
=====




[Elasticsearch](https://www.elastic.co/elasticsearch/)是一个分布式、RESTful搜索和分析引擎。它提供了一个分布式、多租户能力的全文搜索引擎，具有HTTP网络接口和无模式JSON文档。

此教程演示了如何使用与`Elasticsearch`数据库相关的功能。

安装[#](#installation "此标题的永久链接")
-------------------------------

请查看[Elasticsearch安装说明](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch)。

要连接到不需要登录凭据的Elasticsearch实例，请将Elasticsearch URL和索引名称与嵌入对象一起传递给构造函数。

示例：

```
        from langchain import ElasticVectorSearch
        from langchain.embeddings import OpenAIEmbeddings

        embedding = OpenAIEmbeddings()
        elastic_vector_search = ElasticVectorSearch(
            elasticsearch_url="http://localhost:9200",
            index_name="test_index",
            embedding=embedding
        )

```

To connect to an Elasticsearch instance that requires login credentials,
including Elastic Cloud, use the Elasticsearch URL format
https://username:password@es_host:9243. For example, to connect to Elastic
Cloud, create the Elasticsearch URL with the required authentication details and
pass it to the ElasticVectorSearch constructor as the named parameter
elasticsearch_url.

You can obtain your Elastic Cloud URL and login credentials by logging in to the
Elastic Cloud console at https://cloud.elastic.co, selecting your deployment, and
navigating to the “Deployments” page.

To obtain your Elastic Cloud password for the default “elastic” user:

1. Log in to the Elastic Cloud console at https://cloud.elastic.co
2. Go to “Security” > “Users”
3. Locate the “elastic” user and click “Edit”
4. Click “Reset password”
5. Follow the prompts to reset the password

Format for Elastic Cloud URLs is
https://username:password@cluster_id.region_id.gcp.cloud.es.io:9243.

Example:

```
        from langchain import ElasticVectorSearch
        from langchain.embeddings import OpenAIEmbeddings

        embedding = OpenAIEmbeddings()

        elastic_host = "cluster_id.region_id.gcp.cloud.es.io"
        elasticsearch_url = f"https://username:password@{elastic_host}:9243"
        elastic_vector_search = ElasticVectorSearch(
            elasticsearch_url=elasticsearch_url,
            index_name="test_index",
            embedding=embedding
        )

```

```
!pip install elasticsearch

```

```
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

```

Example[#](#example "Permalink to this headline")
-------------------------------------------------

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch
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
db = ElasticVectorSearch.from_documents(docs, embeddings, elasticsearch_url="http://localhost:9200")

query = "What did the president say about Ketanji Brown Jackson"
docs = db.similarity_search(query)

```

```
print(docs[0].page_content)

```

```
In state after state, new laws have been passed, not only to suppress the vote, but to subvert entire elections. 

We cannot let this happen. 

Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```

