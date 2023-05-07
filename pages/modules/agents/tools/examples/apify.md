

Apify[#](#apify "Permalink to this headline")
=============================================

本笔记本演示了如何使用[Apify集成](../../../../ecosystem/apify)进行LangChain。

[Apify](https://apify.com) 是一个用于网络抓取和数据提取的云平台，提供了一个由一千多个现成的应用程序组成的[生态系统](https://apify.com/store)，这些应用程序称为各种网络抓取、爬行和数据提取用例的*演员*。例如，您可以使用它来提取Google搜索结果、Instagram和Facebook配置文件、来自Amazon或Shopify的产品、Google Maps评论等等。

在本例中，我们将使用[网站内容爬虫](https://apify.com/apify/website-content-crawler)演员，它可以深度爬行文档、知识库、帮助中心或博客等网站，并从网页中提取文本内容。然后我们将这些文档提供给向量索引，并从中回答问题。

```
#!pip install apify-client

```

首先，将`ApifyWrapper`导入到您的源代码中：

```
from langchain.document_loaders.base import Document
from langchain.indexes import VectorstoreIndexCreator
from langchain.utilities import ApifyWrapper

```

使用您的[Apify API令牌](https://console.apify.com/account/integrations)进行初始化，并且为本示例使用您的OpenAI API密钥：

```
import os
os.environ["OPENAI_API_KEY"] = "Your OpenAI API key"
os.environ["APIFY_API_TOKEN"] = "Your Apify API token"

apify = ApifyWrapper()

```

然后运行Actor，等待其完成，并从Apify数据集中获取其结果到LangChain文档加载器。

请注意，如果您已经在Apify数据集中有一些结果，则可以直接使用`ApifyDatasetLoader`加载它们，如[此笔记本](../../../indexes/document_loaders/examples/apify_dataset)所示。在那个笔记本中，您还会找到`dataset_mapping_function`的说明，它用于将Apify数据集记录中的字段映射到LangChain`Document`字段。

```
loader = apify.call_actor(
    actor_id="apify/website-content-crawler",
    run_input={"startUrls": [{"url": "https://python.langchain.com/en/latest/"}]},
    dataset_mapping_function=lambda item: Document(
        page_content=item["text"] or "", metadata={"source": item["url"]}
    ),
)

```

从爬取的文档初始化向量索引：

```
index = VectorstoreIndexCreator().from_loaders([loader])

```

最后，查询向量索引：

```
query = "What is LangChain?"
result = index.query_with_sources(query)

```

```
print(result["answer"])
print(result["sources"])

```

```
 LangChain is a standard interface through which you can interact with a variety of large language models (LLMs). It provides modules that can be used to build language model applications, and it also provides chains and agents with memory capabilities.

https://python.langchain.com/en/latest/modules/models/llms, https://python.langchain.com/en/latest/getting_started/getting_started

```

