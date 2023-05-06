PowerPoint
===========================================================

本文介绍如何将PowerPoint文档加载到我们可以在下游使用的文档格式中。

用法：

```
from langchain.document_loaders import UnstructuredPowerPointLoader
loader = UnstructuredPowerPointLoader("example_data/fake-power-point.pptx")
data = loader.load()
```

返回结果是一个Document对象列表，其中包含每个幻灯片的内容，元数据和索引。

保留元素

在内部，Unstructured为不同的文本块创建不同的“元素”。默认情况下，我们将其组合在一起，但是您可以通过指定`mode="elements"`来轻松保持该分离。