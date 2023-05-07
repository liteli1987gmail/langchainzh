

AWS S3 文件[#](#aws-s3-file "标题永久链接")
===================================

> 
> [Amazon 简单存储服务（Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders) 是一种对象存储服务。
> 
> 
> 

> 
> [AWS S3 存储桶](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket)
> 
> 
> 

这涵盖了如何从 `AWS S3 文件` 对象中加载文档对象的内容。

```
from langchain.document_loaders import S3FileLoader

```

```
#!pip install boto3

```

```
loader = S3FileLoader("testing-hwc", "fake.docx")

```

```
loader.load()

```

```
[Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpxvave6wl/fake.docx'}, lookup_index=0)]

```

