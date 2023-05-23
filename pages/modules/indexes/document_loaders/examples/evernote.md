EverNote [#](#evernote "Permalink to this headline")
===================================================

> 
> [EverNote](https://evernote.com/)旨在用于归档和创建笔记，其中可以嵌入照片、音频和保存的Web内容。笔记存储在虚拟的“教程”中，可以标记、注释、编辑、搜索和导出。
> 
> 
> 

本文介绍如何从磁盘加载 `EverNote` 文件。

```
#!pip install pypandoc
import pypandoc

pypandoc.download_pandoc()

```

```
from langchain.document_loaders import EverNoteLoader

loader = EverNoteLoader("example_data/testing.enex")
loader.load()

```

```
[Document(page_content='testing this  what happens?  to the world?\n', metadata={'source': 'example_data/testing.enex'})]

```