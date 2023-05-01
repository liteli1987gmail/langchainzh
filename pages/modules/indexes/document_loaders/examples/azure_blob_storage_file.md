


 Azure Blob Storage File
 [#](#azure-blob-storage-file "Permalink to this headline")
=====================================================================================



 This covers how to load document objects from a Azure Blob Storage file.
 







```
from langchain.document_loaders import AzureBlobStorageFileLoader

```










```
#!pip install azure-storage-blob

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







