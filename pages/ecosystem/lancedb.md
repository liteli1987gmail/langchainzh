

LanceDB[#](#lancedb "跳转到标题")
============================

本页面介绍如何在LangChain中使用[LanceDB](https://github.com/lancedb/lancedb), 分为两部分: 安装和设置，以及对特定LanceDB包装器的引用。

安装和设置[#](#installation-and-setup "跳转到标题")
-----------------------------------------

* 使用`pip install lancedb`安装Python SDK。

包装器[#](#wrappers "跳转到标题")
-------------------------

### VectorStore[#](#vectorstore "跳转到标题")

已经存在一个LanceDB数据库的包装器，允许您将其用作向量库，无论是用于语义搜索还是示例选择。

导入这个向量库:

```
from langchain.vectorstores import LanceDB

```

有关LanceDB包装器的更详细演练，请参见此教程

