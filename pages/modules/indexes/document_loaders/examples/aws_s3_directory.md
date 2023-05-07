

AWS S3目录[#](#aws-s3-directory "此标题的永久链接")
=========================================

> 
> [Amazon Simple Storage Service（Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders)是一项对象存储服务
> 
> 
> 

> 
> [AWS S3目录](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders)
> 
> 
> 

本文介绍如何从`AWS S3 目录`对象中加载文档对象。

```
#!pip install boto3

```

```
from langchain.document_loaders import S3DirectoryLoader

```

```
loader = S3DirectoryLoader("testing-hwc")

```

```
loader.load()

```

指定前缀[#](#specifying-a-prefix "此标题的永久链接")
----------------------------------------

您还可以指定前缀以更精细地控制要加载的文件。

```
loader = S3DirectoryLoader("testing-hwc", prefix="fake")

```

```
loader.load()

```

```
[Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpujbkzf_l/fake.docx'}, lookup_index=0)]

```

