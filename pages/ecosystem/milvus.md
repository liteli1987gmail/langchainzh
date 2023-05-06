

Milvus[#](#milvus "Permalink to this headline")
===============================================

本页介绍如何在LangChain中使用Milvus生态系统。

它分为两部分：安装和设置，以及对特定Milvus包装器的引用。

安装和设置[#](#installation-and-setup "Permalink to this headline")
--------------------------------------------------------------

* 使用`pip install pymilvus`安装Python SDK。

包装器[#](#wrappers "Permalink to this headline")
----------------------------------------------

### VectorStore[#](#vectorstore "Permalink to this headline")

存在一个Milvus索引的包装器，允许您将其用作向量存储，无论是用于语义搜索还是示例选择。

要导入此向量存储：

```
from langchain.vectorstores import Milvus

```

有关Miluvs包装器的更详细的演练，请参见[此笔记本](../modules/indexes/vectorstores/examples/milvus)

