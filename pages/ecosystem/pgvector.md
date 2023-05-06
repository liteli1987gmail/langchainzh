

PGVector[#](#pgvector "跳转至此标题的链接")
==================================

本页介绍如何在LangChain内使用Postgres[PGVector](https://github.com/pgvector/pgvector)生态系统。它分为两个部分：安装和设置，以及对特定PGVector包装器的引用。

安装[#](#installation "跳转至此标题的链接")
--------------------------------

* 使用`pip install pgvector`安装Python包。

设置[#](#setup "跳转至此标题的链接")
-------------------------

- 第一步是创建一个已安装`pgvector`扩展的数据库。

遵循[PGVector安装步骤](https://github.com/pgvector/pgvector#installation)中的步骤来安装数据库和扩展。Docker镜像是最简单的入门方式。

包装器[#](#wrappers "此标题的永久链接")
----------------------------

### VectorStore[#](#vectorstore "此标题的永久链接")

存在一个 Postgres 向量数据库的包装器，使您可以将其用作向量存储，无论是用于语义搜索还是示例选择。

要导入此向量存储：

```
from langchain.vectorstores.pgvector import PGVector

```

### 用法[#](#usage "此标题的永久链接")

有关 PGVector 包装器的更详细演练，请参见 [此笔记本](../modules/indexes/vectorstores/examples/pgvector)

