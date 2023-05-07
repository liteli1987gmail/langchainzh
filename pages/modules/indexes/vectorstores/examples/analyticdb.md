

分析型数据库[#](#analyticdb "本标题的永久链接")
=================================

> 
> [分析型数据库（AnalyticDB)](https://www.alibabacloud.com/help/zh/doc-detail/188196.htm)是一种大规模并行处理（MPP)数据仓库服务，旨在在线分析大量数据。
> 
> 
> 

> 
> `AnalyticDB for PostgreSQL`基于开源的`Greenplum Database`项目开发，并由`阿里云`进行深度扩展。分析型数据库（AnalyticDB)支持ANSI SQL 2003语法以及PostgreSQL和Oracle数据库生态系统。分析型数据库还支持行存储和列存储。分析型数据库处理PB级别的数据时具有高性能，并支持高并发在线查询。
> 
> 
> 

本笔记本演示了如何使用与`AnalyticDB`向量数据库相关的功能。
要运行，您需要拥有一个正在运行的[分析型数据库](https://www.alibabacloud.com/help/zh/doc-detail/188196.htm)实例：

* 使用[AnalyticDB云向量数据库](https://www.alibabacloud.com/product/hybriddb-postgresql)。 点击此处快速部署。

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import AnalyticDB

```

通过调用OpenAI API拆分文档并获取嵌入

```
from langchain.document_loaders import TextLoader
loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

```

通过设置相关环境连接到AnalyticDB

```
export PG_HOST={your_analyticdb_hostname}
export PG_PORT={your_analyticdb_port} # Optional, default is 5432
export PG_DATABASE={your_database} # Optional, default is postgres
export PG_USER={database_username}
export PG_PASSWORD={database_password}

```

然后将您的嵌入和文档存储到AnalyticDB中

```
import os

connection_string = AnalyticDB.connection_string_from_db_params(
    driver=os.environ.get("PG_DRIVER", "psycopg2cffi"),
    host=os.environ.get("PG_HOST", "localhost"),
    port=int(os.environ.get("PG_PORT", "5432")),
    database=os.environ.get("PG_DATABASE", "postgres"),
    user=os.environ.get("PG_USER", "postgres"),
    password=os.environ.get("PG_PASSWORD", "postgres"),
)

vector_db = AnalyticDB.from_documents(
    docs,
    embeddings,
    connection_string= connection_string,
)

```

查询和检索数据

```
query = "What did the president say about Ketanji Brown Jackson"
docs = vector_db.similarity_search(query)

```

```
print(docs[0].page_content)

```

```
Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```

