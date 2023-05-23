# Zilliz Cloud

[Zilliz Cloud](https://zilliz.com/doc/quick_start)是一个完全托管在云端的向量数据库和`LF AI Milvus®`服务。

本教程展示了如何使用与Zilliz Cloud向量数据库相关的功能。

要运行，您应该有一个正在运行的"Zilliz Cloud"实例。这里是[安装指南](https://zilliz.com/cloud)。

```python
!pip install pymilvus
```

我们想使用`OpenAIEmbeddings`，因此必须获取OpenAI API密钥。

```python
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API密钥：')
```

需要将以下内容替换为Zilliz Cloud连接信息：

```python
ZILLIZ_CLOUD_URI = "" # 例如："https://in01-17f69c292d4a5sa.aws-us-west-2.vectordb.zillizcloud.com:19536"
ZILLIZ_CLOUD_USERNAME = ""  # 例如："username"
ZILLIZ_CLOUD_PASSWORD = ""  # 例如："*********"
```

```python
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Milvus
from langchain.document_loaders import TextLoader

loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

vector_db = Milvus.from_documents(
    docs,
    embeddings,
    connection_args={
        "uri": ZILLIZ_CLOUD_URI,
        "username": ZILLIZ_CLOUD_USERNAME,
        "password": ZILLIZ_CLOUD_PASSWORD,
        "secure": True
    }
)

docs = vector_db.similarity_search(query)

docs[0]
```