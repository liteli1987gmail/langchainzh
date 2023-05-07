

Qdrant[#](#qdrant "跳转到标题锚点")
============================

> 
> [Qdrant](https://qdrant.tech/documentation/)（读作：quadrant)是一个向量相似性搜索引擎。它提供了一个生产就绪的服务，带有一个方便的API来存储、搜索和管理点——带有额外的负载的向量。 `Qdrant`被定制为支持扩展过滤。它使得它对所有类型的神经网络或基于语义的匹配、分面搜索和其他应用程序都有用。
> 
> 
> 

这个笔记本展示了如何使用与`Qdrant`向量数据库相关的功能。

有各种各样的运行`Qdrant`的方式，根据所选择的方式，会有一些微妙的差异。选项包括：

* 本地模式，不需要服务器

* 本地服务器部署

* Qdrant云

请参阅[安装说明](https://qdrant.tech/documentation/install/)。

```
!pip install qdrant-client

```

我们想使用`OpenAIEmbeddings`，所以我们必须获取OpenAI API密钥。

```
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

```

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Qdrant
from langchain.document_loaders import TextLoader

```

```
loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

```

从LangChain连接到Qdrant[#](#从langchain连接到qdrant "标题的永久链接")
------------------------------------------------------

### 本地模式[#](#本地模式 "标题的永久链接")

Python客户端允许您在本地模式下运行相同的代码，而无需运行Qdrant服务器。这对于测试和调试或者如果您计划仅存储少量向量非常有用。嵌入可能完全在内存中保留或在磁盘上持久化。

#### 内存中[#](#内存中 "标题的永久链接")

对于一些测试场景和快速实验，您可能更喜欢仅将所有数据保存在内存中，这样当客户端被销毁时，数据就会丢失 - 通常在脚本/笔记本的末尾。

```
qdrant = Qdrant.from_documents(
    docs, embeddings, 
    location=":memory:",  # Local mode with in-memory storage only
    collection_name="my_documents",
)

```

#### 磁盘存储[#](#磁盘存储 "标题的永久链接")

在不使用Qdrant服务器的本地模式下，可能还会将向量存储在磁盘上，以便在运行之间持久化它们。

```
qdrant = Qdrant.from_documents(
    docs, embeddings, 
    path="/tmp/local_qdrant",
    collection_name="my_documents",
)

```

### 本地服务器部署[#](#本地服务器部署 "标题的永久链接")

无论您选择使用[Docker容器](https://qdrant.tech/documentation/install/)在本地启动Qdrant，还是选择使用[官方Helm图表](https://github.com/qdrant/qdrant-helm)进行Kubernetes部署，连接到此实例的方式都是相同的。您需要提供指向服务的URL。

```
url = "<---qdrant url here --->"
qdrant = Qdrant.from_documents(
    docs, embeddings, 
    url, prefer_grpc=True, 
    collection_name="my_documents",
)

```

### Qdrant Cloud[#](#qdrant-cloud "本标题的永久链接")

如果您不想忙于管理基础架构，可以选择在[Qdrant Cloud](https://cloud.qdrant.io/)上设置完全托管的Qdrant群集。其中包括一个永久免费的1GB群集，可供试用。使用Qdrant的托管版本的主要区别在于，您需要提供API密钥以保护您的部署不被公开访问。

```
url = "<---qdrant cloud cluster url here --->"
api_key = "<---api key here--->"
qdrant = Qdrant.from_documents(
    docs, embeddings, 
    url, prefer_grpc=True, api_key=api_key, 
    collection_name="my_documents",
)

```

重用同一集合[#](#reusing-the-same-collection "本标题的永久链接")
--------------------------------------------------

假设你现在是一名优秀的文档撰写者，而且你精通英文和中文。请将以下字符串json里的英语翻译为中文，键名不变,值是html标签，标签的属性不用翻译，只要翻译标签的text。

```
del qdrant

```

```
import qdrant_client

client = qdrant_client.QdrantClient(
    path="/tmp/local_qdrant", prefer_grpc=True
)
qdrant = Qdrant(
    client=client, collection_name="my_documents", 
    embedding_function=embeddings.embed_query
)

```

相似度搜索[#](#similarity-search "此标题的永久链接")
---------------------------------------

使用Qdrant向量存储最简单的场景是执行相似度搜索。在底层，我们的查询将使用`嵌入函数`进行编码，并用于在Qdrant集合中查找相似的文档。

```
query = "What did the president say about Ketanji Brown Jackson"
found_docs = qdrant.similarity_search(query)

```

```
print(found_docs[0].page_content)

```

```
Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```

带有分数的相似性搜索[#](#similarity-search-with-score "此标题的永久链接")
-------------------------------------------------------

有时我们可能想执行搜索，但也要获得相关性得分，以了解特定结果的好坏程度。

```
query = "What did the president say about Ketanji Brown Jackson"
found_docs = qdrant.similarity_search_with_score(query)

```

```
document, score = found_docs[0]
print(document.page_content)
print(f"\nScore: {score}")

```

```
Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

Score: 0.8153784913324512

```

最大边际相关性搜索（MMR)[#](#maximum-marginal-relevance-search-mmr "此标题的永久链接")
--------------------------------------------------------------------

如果您想查找一些类似的文档，但又希望获得多样化的结果，那么MMR是您应该考虑的方法。最大边际相关性优化了查询相似度和所选文档之间的多样性。

```
query = "What did the president say about Ketanji Brown Jackson"
found_docs = qdrant.max_marginal_relevance_search(query, k=2, fetch_k=10)

```

```
for i, doc in enumerate(found_docs):
    print(f"{i + 1}.", doc.page_content, "\n")

```

```
1. Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence. 

2. We can’t change how divided we’ve been. But we can change how we move forward—on COVID-19 and other issues we must face together. 

I recently visited the New York City Police Department days after the funerals of Officer Wilbert Mora and his partner, Officer Jason Rivera. 

They were responding to a 9-1-1 call when a man shot and killed them with a stolen gun. 

Officer Mora was 27 years old. 

Officer Rivera was 22. 

Both Dominican Americans who’d grown up on the same streets they later chose to patrol as police officers. 

I spoke with their families and told them that we are forever in debt for their sacrifice, and we will carry on their mission to restore the trust and safety every community deserves. 

I’ve worked on these issues a long time. 

I know what works: Investing in crime preventionand community police officers who’ll walk the beat, who’ll know the neighborhood, and who can restore trust and safety. 

```

Qdrant作为检索器[#](#qdrant-as-a-retriever "本标题的永久链接")
-------------------------------------------------

Qdrant，与所有其他向量存储一样，通过使用余弦相似度作为LangChain检索器。

```
retriever = qdrant.as_retriever()
retriever

```

```
VectorStoreRetriever(vectorstore=<langchain.vectorstores.qdrant.Qdrant object at 0x7fc4e5720a00>, search_type='similarity', search_kwargs={})

```

也可以指定使用MMR作为搜索策略，而不是相似度。

```
retriever = qdrant.as_retriever(search_type="mmr")
retriever

```

```
VectorStoreRetriever(vectorstore=<langchain.vectorstores.qdrant.Qdrant object at 0x7fc4e5720a00>, search_type='mmr', search_kwargs={})

```

```
query = "What did the president say about Ketanji Brown Jackson"
retriever.get_relevant_documents(query)[0]

```

```
Document(page_content='Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', metadata={'source': '../../../state_of_the_union.txt'})

```

自定义Qdrant[#](#customizing-qdrant "本标题的永久链接")
--------------------------------------------

Qdrant将您的向量嵌入与可选的类似JSON的有效载荷一起存储。有效载荷是可选的，但由于LangChain假定嵌入是从文档生成的，因此我们保留上下文数据，因此您也可以提取原始文本。

默认情况下，您的文档将存储在以下有效载荷结构中：

```
{
 "page_content": "Lorem ipsum dolor sit amet",
 "metadata": {
 "foo": "bar"
 }
}

```

但是，您可以决定使用不同的键来存储页面内容和元数据。如果您已经有一个要重用的集合，那很有用。您始终可以更改

```
Qdrant.from_documents(
    docs, embeddings, 
    location=":memory:",
    collection_name="my_documents_2",
    content_payload_key="my_page_content_key",
    metadata_payload_key="my_meta",
)

```

```
<langchain.vectorstores.qdrant.Qdrant at 0x7fc4e2baa230>

```

