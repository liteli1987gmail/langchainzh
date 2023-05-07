MyScale
===

> 
> [MyScale](https://docs.myscale.com/zh/overview/) 是一种云端数据库，专门为 AI 应用和解决方案进行优化，构建在开源的 [ClickHouse](https://github.com/ClickHouse/ClickHouse) 上。
> 
> 
> 

这个笔记本展示了如何使用与 `MyScale` 向量数据库相关的功能。

设置环境[#](#setting-up-envrionments "跳转到这个标题的链接")
----------------------------------------------

```
!pip install clickhouse-connect

```

我们想要使用 OpenAIEmbeddings，因此需要获得 OpenAI API 密钥。

```
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

```

有两种设置 myscale 索引参数的方式。

- 环境变量

在运行应用之前，请使用 `export` 设置环境变量：
`export MYSCALE_URL='<your-endpoints-url>' MYSCALE_PORT=<your-endpoints-port> MYSCALE_USERNAME=<your-username> MYSCALE_PASSWORD=<your-password> ...`

您可以在我们的SaaS上轻松找到您的帐户、密码和其他信息。有关详细信息，请参见[此文档](https://docs.myscale.com/en/cluster-management/)

`MyScaleSettings`下的每个属性都可以使用前缀`MYSCALE_`设置，并且不区分大小写。
2. Create `MyScaleSettings` object with parameters

```
from langchain.vectorstores import MyScale, MyScaleSettings
config = MyScaleSetting(host="<your-backend-url>", port=8443, ...)
index = MyScale(embedding_function, config)
index.add_documents(...)

```

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import MyScale
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
for d in docs:
    d.metadata = {'some': 'metadata'}
docsearch = MyScale.from_documents(docs, embeddings)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)

```

```
Inserting data...: 100%|██████████| 42/42 [00:18<00:00,  2.21it/s]

```

```
print(docs[0].page_content)

```

```
As Frances Haugen, who is here with us tonight, has shown, we must hold social media platforms accountable for the national experiment they’re conducting on our children for profit. 

It’s time to strengthen privacy protections, ban targeted advertising to children, demand tech companies stop collecting personal data on our children. 

And let’s get all Americans the mental health services they need. More people they can turn to for help, and full parity between physical and mental health care. 

Third, support our veterans. 

Veterans are the best of us. 

I’ve always believed that we have a sacred obligation to equip all those we send to war and care for them and their families when they come home. 

My administration is providing assistance with job training and housing, and now helping lower-income veterans get VA care debt-free.  

Our troops in Iraq and Afghanistan faced many dangers.

```

Get connection info and data schema[#](#get-connection-info-and-data-schema "Permalink to this headline")
---------------------------------------------------------------------------------------------------------

```
print(str(docsearch))

```

Filtering[#](#filtering "Permalink to this headline")
-----------------------------------------------------

You can have direct access to myscale SQL where statement. You can write `WHERE` clause following standard SQL.

**NOTE**: Please be aware of SQL injection, this interface must not be directly called by end-user.

If you custimized your `column_map` under your setting, you search with filter like this:

```
from langchain.vectorstores import MyScale, MyScaleSettings
from langchain.document_loaders import TextLoader

loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

for i, d in enumerate(docs):
    d.metadata = {'doc_id': i}

docsearch = MyScale.from_documents(docs, embeddings)

```

```
Inserting data...: 100%|██████████| 42/42 [00:15<00:00,  2.69it/s]

```

```
meta = docsearch.metadata_column
output = docsearch.similarity_search_with_relevance_scores('What did the president say about Ketanji Brown Jackson?', 
                                                           k=4, where_str=f"{meta}.doc_id<10")
for d, dist in output:
    print(dist, d.metadata, d.page_content[:20] + '...')

```

```
0.252379834651947 {'doc_id': 6, 'some': ''} And I’m taking robus...
0.25022566318511963 {'doc_id': 1, 'some': ''} Groups of citizens b...
0.2469480037689209 {'doc_id': 8, 'some': ''} And so many families...
0.2428302764892578 {'doc_id': 0, 'some': 'metadata'} As Frances Haugen, w...

```

Deleting your data[#](#deleting-your-data "Permalink to this headline")
-----------------------------------------------------------------------

```
docsearch.drop()

```

