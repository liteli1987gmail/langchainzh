s3 Directory
==========================================================

本文介绍如何从s3目录对象加载文档对象。

示例代码：

```
from langchain.document_loaders import S3DirectoryLoader
```

需要安装`boto3`包：

```
!pip install boto3
```

初始化载入器：

```
loader = S3DirectoryLoader("testing-hwc")
```

加载并返回文档对象列表：

```
loader.load()
```

返回结果是一个Document对象列表，其中每个对象包含文档内容和元数据。

指定前缀：

您还可以指定前缀以更精细地控制要加载的文件。

示例代码：

```
loader = S3DirectoryLoader("testing-hwc", prefix="fake")
loader.load()
```

返回结果是以前缀开头的Document对象列表，其中每个对象包含文档内容和元数据。