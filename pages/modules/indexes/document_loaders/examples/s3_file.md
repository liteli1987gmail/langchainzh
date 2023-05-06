s3 File
==========================================================

本文介绍如何从s3文件对象加载文档对象。
示例代码：

```
from langchain.document_loaders import S3FileLoader
```

需要安装`boto3`包：

```
!pip install boto3
```

初始化载入器：

```
loader = S3FileLoader("testing-hwc", "fake.docx")
```

加载并返回文档对象：

```
loader.load()
```

返回结果是一个Document对象列表，其中每个对象包含文档内容和元数据。