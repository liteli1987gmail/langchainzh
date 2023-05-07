
Vespa.ai作为LangChain检索器
===


本笔记展示了如何使用Vespa.ai作为LangChain检索器。
Vespa.ai是一个高效的结构化文本和向量搜索平台。
更多信息请参见[Vespa.ai](https://vespa.ai)。

为了创建一个检索器，我们使用[pyvespa](https://pyvespa.readthedocs.io/en/latest/index)来
创建到Vespa服务的连接。

```
from vespa.application import Vespa

vespa_app = Vespa(url="https://doc-search.vespa.oath.cloud")

```

这将创建一个连接到Vespa服务的连接，这里是Vespa文档搜索服务。
使用pyvespa，您还可以连接到
[Vespa Cloud实例](https://pyvespa.readthedocs.io/en/latest/deploy-vespa-cloud)
或者本地
[Docker实例](https://pyvespa.readthedocs.io/en/latest/deploy-docker)。

连接到服务后，您可以设置检索器：

```
from langchain.retrievers.vespa_retriever import VespaRetriever

vespa_query_body = {
    "yql": "select content from paragraph where userQuery()",
    "hits": 5,
    "ranking": "documentation",
    "locale": "en-us"
}
vespa_content_field = "content"
retriever = VespaRetriever(vespa_app, vespa_query_body, vespa_content_field)

```

This sets up a LangChain retriever that fetches documents from the Vespa application.
Here, up to 5 results are retrieved from the `content` field in the `paragraph` document type,
using `doumentation` as the ranking method. The `userQuery()` is replaced with the actual query
passed from LangChain.

Please refer to the [pyvespa documentation](https://pyvespa.readthedocs.io/en/latest/getting-started-pyvespa#Query)
for more information.

Now you can return the results and continue using the results in LangChain.

```
retriever.get_relevant_documents("what is vespa?")

```

