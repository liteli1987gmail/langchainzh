

Azure Files
===============
> 
>[Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction)是在云中提供的完全托管的文件共享，可通过行业标准的Server Message Block（`SMB`)协议、Network File System (`NFS`)协议和`Azure Files REST API`进行访问。
> 
> 
> 

本文介绍如何从Azure Files中加载文档对象。

```
#!pip install azure-storage-blob

```

```
from langchain.document_loaders import AzureBlobStorageFileLoader

```

```
loader = AzureBlobStorageFileLoader(conn_str='<connection string>', container='<container name>', blob_name='<blob name>')

```

```
loader.load()

```

```
[Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpxvave6wl/fake.docx'}, lookup_index=0)]

```

