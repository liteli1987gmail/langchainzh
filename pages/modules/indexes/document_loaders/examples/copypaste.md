

复制粘贴[#](#copy-paste "永久链接至此标题")
===============================

本教程介绍了如何从想要复制和粘贴的内容中加载文档对象。在这种情况下，您甚至不需要使用DocumentLoader，而是可以直接构造文档。

```
from langchain.docstore.document import Document

```

```
text = "..... put the text you copy pasted here......"

```

```
doc = Document(page_content=text)

```

元数据[#](#metadata "永久链接至此标题")
----------------------------

如果您想添加关于获取此文本片段的位置的元数据，可以轻松完成，只需使用元数据键即可。

```
metadata = {"source": "internet", "date": "Friday"}

```

```
doc = Document(page_content=text, metadata=metadata)

```

