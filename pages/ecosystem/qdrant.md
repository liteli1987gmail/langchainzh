

Qdrant[#](#qdrant "跳转到标题：Qdrant")
=================================

本页介绍如何在LangChain中使用Qdrant生态系统。它分为两个部分：安装和设置，以及特定Qdrant包装器的参考。

安装和设置[#](#installation-and-setup "跳转到标题：安装和设置")
-----------------------------------------------

* 使用`pip install qdrant-client`安装Python SDK

包装器[#](#wrappers "跳转到标题：包装器")
-----------------------------

### VectorStore[#](#vectorstore "跳转到标题：VectorStore")

存在一个Qdrant索引的包装器，允许您将其用作向量存储，无论是用于语义搜索还是示例选择。

导入此向量存储的方法如下：

```
from langchain.vectorstores import Qdrant

```

有关Qdrant包装器的更详细说明，请参见[此教程](../modules/indexes/vectorstores/examples/qdrant)

