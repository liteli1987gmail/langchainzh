GCS目录
=================================================

这篇文章介绍了如何从Google Cloud Storage (GCS)目录中加载文档对象。

```
from langchain.document_loaders import GCSDirectoryLoader
```

安装google-cloud-storage：

```
# !pip install google-cloud-storage
```

指定项目名，存储桶（bucket）：

```
loader = GCSDirectoryLoader(project_name="aist", bucket="testing-hwc")
```

加载数据：

```
loader.load()
```

如果使用End user credentials认证，可能会收到警告信息，建议使用Service account认证。以下是输出结果：

```
[Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpz37njh7u/fake.docx'}, lookup_index=0)]
```

指定前缀，更精细化地控制加载的文件：

```
loader = GCSDirectoryLoader(project_name="aist", bucket="testing-hwc", prefix="fake")
```

重新加载数据：

```
loader.load()
```

以下是输出结果：

```
[Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpylg6291i/fake.docx'}, lookup_index=0)]
```