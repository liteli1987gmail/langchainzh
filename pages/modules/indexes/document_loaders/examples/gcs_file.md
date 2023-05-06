GCS文件存储
=================================================

这篇文章介绍了如何从Google Cloud Storage (GCS)文件对象中加载文档对象。

```
from langchain.document_loaders import GCSFileLoader
```

安装google-cloud-storage：

```
# !pip install google-cloud-storage
```

指定项目名、存储桶（bucket）和文件名：

```
loader = GCSFileLoader(project_name="aist", bucket="testing-hwc", blob="fake.docx")
```

加载数据：

```
loader.load()
```

可能会收到警告信息，建议使用Service account认证。以下是输出结果：

```
[Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmp3srlf8n8/fake.docx'}, lookup_index=0)]
```