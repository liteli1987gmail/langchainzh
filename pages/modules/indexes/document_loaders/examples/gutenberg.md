Gutenberg
=========================================================

本文介绍如何将古腾堡电子书的链接加载到我们可以向下使用的文档格式中。

引入`GutenbergLoader`：

```
from langchain.document_loaders import GutenbergLoader
```

指定加载的古腾堡电子书链接：

```
loader = GutenbergLoader('https://www.gutenberg.org/cache/epub/69972/pg69972.txt')
```

加载电子书内容：

```
data = loader.load()
```

输出电子书内容：

```
data
```