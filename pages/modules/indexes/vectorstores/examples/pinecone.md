

松果[#](#pinecone "此标题的永久链接")
===========================

[松果](https://docs.pinecone.io/docs/overview)是一个功能广泛的向量数据库。

本笔记本展示了如何使用与`松果`向量数据库相关的功能。

要使用松果，您必须拥有API密钥。以下是[安装说明](https://docs.pinecone.io/docs/quickstart)。

```
!pip install pinecone-client

```

```
import os
import getpass

PINECONE_API_KEY = getpass.getpass('Pinecone API Key:')

```

```
PINECONE_ENV = getpass.getpass('Pinecone Environment:')

```

我们想使用`OpenAI Embeddings`，因此我们必须获取OpenAI API密钥。

```
os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

```

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
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
import pinecone 

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENV  # next to api key in console
)

index_name = "langchain-demo"

docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)

# if you already have an index, you can load it like this
# docsearch = Pinecone.from_existing_index(index_name, embeddings)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)

```

```
print(docs[0].page_content)

```

