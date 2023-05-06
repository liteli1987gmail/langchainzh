

Apify数据集[#](#apify-dataset "此标题的永久链接")
======================================

> 
> [Apify数据集](https://docs.apify.com/platform/storage/dataset)是一种可扩展的、仅可添加的存储器，具有顺序访问功能，用于存储结构化的网络爬取结果，例如产品列表或Google SERP，然后将它们导出为各种格式，如JSON、CSV或Excel。数据集主要用于保存[Apify Actors](https://apify.com/store)的结果——用于各种网络爬取、抓取和数据提取方案的无服务器云程序。
> 
> 
> 

本笔记本演示了如何将Apify数据集加载到LangChain中。

前提条件[#](#prerequisites "此标题的永久链接")
----------------------------------

您需要在Apify平台上拥有现有的数据集。如果您没有，请先查看[此笔记本](../../../agents/tools/examples/apify），了解如何使用Apify从文档、知识库、帮助中心或博客中提取内容。

```
#!pip install apify-client

```

首先，将`ApifyDatasetLoader`导入您的源代码中:

```
from langchain.document_loaders import ApifyDatasetLoader
from langchain.document_loaders.base import Document

```

然后提供一个将Apify数据集记录字段映射到LangChain `Document`格式的函数。

例如，如果你的数据集项结构如下：

```
{
 "url": "https://apify.com",
 "text": "Apify is the best web scraping and automation platform."
}

```

下面代码中的映射函数将把它们转换为LangChain `Document`格式，以便您可以将其进一步与任何LLM模型一起使用（例如用于问答）。

```
loader = ApifyDatasetLoader(
    dataset_id="your-dataset-id",
    dataset_mapping_function=lambda dataset_item: Document(
        page_content=dataset_item["text"], metadata={"source": dataset_item["url"]}
    ),
)

```

```
data = loader.load()

```

问答示例[#](#an-example-with-question-answering "Permalink to this headline")
-------------------------------------------------------------------------

在此示例中，我们使用数据集中的数据回答一个问题。

```
from langchain.docstore.document import Document
from langchain.document_loaders import ApifyDatasetLoader
from langchain.indexes import VectorstoreIndexCreator

```

```
loader = ApifyDatasetLoader(
    dataset_id="your-dataset-id",
    dataset_mapping_function=lambda item: Document(
        page_content=item["text"] or "", metadata={"source": item["url"]}
    ),
)

```

```
index = VectorstoreIndexCreator().from_loaders([loader])

```

```
query = "What is Apify?"
result = index.query_with_sources(query)

```

```
print(result["answer"])
print(result["sources"])

```

```
 Apify is a platform for developing, running, and sharing serverless cloud programs. It enables users to create web scraping and automation tools and publish them on the Apify platform.

https://docs.apify.com/platform/actors, https://docs.apify.com/platform/actors/running/actors-in-store, https://docs.apify.com/platform/security, https://docs.apify.com/platform/actors/examples

```

