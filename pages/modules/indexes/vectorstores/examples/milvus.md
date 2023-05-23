

Milvus[#](#milvus "Permalink to this headline")
===============================================

> 
> [Milvus](https://milvus.io/docs/overview.md) 是一个存储、索引和管理由深度神经网络和其他机器学习（ML)模型生成的大规模嵌入向量的数据库。
> 
> 
> 

本教程展示了如何使用与 Milvus 向量数据库相关的功能。

要运行，您应该有一个[运行中的 Milvus 实例](https://milvus.io/docs/install_standalone-docker.md)。

```
!pip install pymilvus

```

我们想要使用 OpenAIEmbeddings，所以我们需要获取 OpenAI API 密钥。

```
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

```

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Milvus
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
vector_db = Milvus.from_documents(
    docs,
    embeddings,
    connection_args={"host": "127.0.0.1", "port": "19530"},
)

```

```
docs = vector_db.similarity_search(query)

```

```
docs[0]

```

