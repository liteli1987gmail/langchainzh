

OpenSearch
=============

该页面介绍如何在LangChain中使用OpenSearch生态系统。教程分为两个部分：安装和设置，以及指向特定OpenSearch包装器的参考。

安装和设置
---------------------

* 使用 `pip install opensearch-py` 命令安装Python包。

包装器
---------------------

VectorStore
---------------------

OpenSearch向量数据库的包装器允许您将其用作向量存储库，以便使用lucene、nmslib和faiss引擎提供的近似向量搜索支持的语义搜索，或者使用painless脚本和脚本评分函数进行暴力向量搜索。

使用以下代码导入此向量存储库：

```
from langchain.vectorstores import OpenSearchVectorSearch

```

如果您需要更详细的OpenSearch包装器演示，请参见[此教程](../modules/indexes/vectorstores/examples/opensearch)

