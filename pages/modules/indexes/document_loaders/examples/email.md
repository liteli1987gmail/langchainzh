

电子邮件[#](#email "跳转到此标题的永久链接")
=============================

本笔记本演示了如何加载电子邮件 (`.eml`) 或者 `Microsoft Outlook` (`.msg`) 文件。

使用非结构化数据[#](#using-unstructured "跳转到此标题的永久链接")
----------------------------------------------

```
#!pip install unstructured

```

```
from langchain.document_loaders import UnstructuredEmailLoader

```

```
loader = UnstructuredEmailLoader('example_data/fake-email.eml')

```

```
data = loader.load()

```

```
data

```

```
[Document(page_content='This is a test email to use for unit tests.  Important points:  Roses are red  Violets are blue', metadata={'source': 'example_data/fake-email.eml'})]

```

### 保留元素[#](#retain-elements "跳转到此标题的永久链接")

在底层，非结构化数据为不同的文本块创建不同的“元素”。默认情况下，我们将它们组合在一起，但您可以通过指定 `mode="elements"` 来轻松保持分离。

```
loader = UnstructuredEmailLoader('example_data/fake-email.eml', mode="elements")

```

```
data = loader.load()

```

```
data[0]

```

```
Document(page_content='This is a test email to use for unit tests.', lookup_str='', metadata={'source': 'example_data/fake-email.eml'}, lookup_index=0)

```

使用OutlookMessageLoader[#](#using-outlookmessageloader "跳转到此标题的永久链接")
--------------------------------------------------------------------

```
#!pip install extract_msg

```

```
from langchain.document_loaders import OutlookMessageLoader

```

```
loader = OutlookMessageLoader('example_data/fake-email.msg')

```

```
data = loader.load()

```

```
data[0]

```

```
Document(page_content='This is a test email to experiment with the MS Outlook MSG Extractor\r\n\r\n\r\n-- \r\n\r\n\r\nKind regards\r\n\r\n\r\n\r\n\r\nBrian Zhou\r\n\r\n', metadata={'subject': 'Test for TIF files', 'sender': 'Brian Zhou <brizhou@gmail.com>', 'date': 'Mon, 18 Nov 2013 16:26:24 +0800'})

```

