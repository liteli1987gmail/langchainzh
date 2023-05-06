# Azure Blob Storage

> [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction) 是Microsoft为云端提供的对象存储解决方案。Blob Storage针对存储海量非结构化数据进行了优化。非结构化数据是不符合特定数据模型或定义的数据，如文本或二进制数据。

Azure Blob Storage的设计用途包括：

* 直接向浏览器提供图像或文档。
* 存储文件以进行分布式访问。
* 流式传输视频和音频。
* 写入日志文件。
* 存储用于备份和还原、灾难恢复和归档的数据。
* 存储可由本地或Azure托管服务分析的数据。

本笔记介绍如何从 `Azure Blob Storage` 上的容器中加载文档对象。

```
#!pip install azure-storage-blob

```

```
from langchain.document_loaders import AzureBlobStorageContainerLoader

```

```
loader = AzureBlobStorageContainerLoader(conn_str="<conn_str>", container="<container>")

```

```
loader.load()

```

```
[Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpaa9xl6ch/fake.docx'}, lookup_index=0)]

```

指定前缀[#](#specifying-a-prefix "Permalink to this headline")
----------------------------------------------------------

您还可以指定前缀以更精细地控制要加载的文件。

```
loader = AzureBlobStorageContainerLoader(conn_str="<conn_str>", container="<container>", prefix="<prefix>")

```

```
loader.load()

```

```
[Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpujbkzf_l/fake.docx'}, lookup_index=0)]

```

