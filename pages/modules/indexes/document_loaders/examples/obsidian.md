Obsidian
=======================================================

本文介绍如何从Obsidian数据库中加载文档。

由于Obsidian只作为Markdown文件夹存储在磁盘上，因此加载器只需要取一个指向此目录的路径。

Obsidian文件有时还包含元数据，即文件顶部的YAML块。这些值将添加到文档的元数据中。（`ObsidianLoader`还可以传递`collect_metadata = False`参数以禁用此行为。)

用法：

```
from langchain.document_loaders import ObsidianLoader
loader = ObsidianLoader("<path-to-obsidian>")
docs = loader.load()
```