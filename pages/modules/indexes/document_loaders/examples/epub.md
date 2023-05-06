

EPub[#](#epub "跳转到本标题的永久链接")
============================

> 
> [EPUB](https://zh.wikipedia.org/wiki/EPUB) 是一种使用“.epub”文件扩展名的电子书文件格式。该术语是电子出版物的缩写，有时以 ePub 的样式呈现。`EPUB` 受许多电子阅读器支持，大多数智能手机、平板电脑和计算机都有兼容软件。
> 
> 
> 

本文介绍了如何将`.epub`文档加载到可以向下使用的文档格式中。您需要安装 [`pandocs`](https://pandoc.org/installing） 包才能使此加载程序正常工作。

```
#!pip install pandocs

```

```
from langchain.document_loaders import UnstructuredEPubLoader

```

```
loader = UnstructuredEPubLoader("winter-sports.epub")

```

```
data = loader.load()

```

保留元素[#](#retain-elements "跳转到本标题的永久链接")
---------------------------------------

在幕后，Unstructured 为不同的文本块创建不同的“元素”。默认情况下，我们将它们合并在一起，但您可以通过指定 `mode="elements"` 来轻松保留该分离。

```
loader = UnstructuredEPubLoader("winter-sports.epub", mode="elements")

```

```
data = loader.load()

```

```
data[0]

```

```
Document(page_content='The Project Gutenberg eBook of Winter Sports in\nSwitzerland, by E. F. Benson', lookup_str='', metadata={'source': 'winter-sports.epub', 'page_number': 1, 'category': 'Title'}, lookup_index=0)

```

