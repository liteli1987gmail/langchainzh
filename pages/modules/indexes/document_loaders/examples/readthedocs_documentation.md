ReadTheDocs文档
==========================================================

本文介绍如何加载作为Read-The-Docs构建的一部分生成的html中的内容。

用法：

```
from langchain.document_loaders import ReadTheDocsLoader
loader = ReadTheDocsLoader("rtdocs", features='html.parser')
docs = loader.load()
```

前提是html已经被抓取到文件夹中。这可以通过取消注释并运行以下命令来完成： 

```
#!wget -r -A -P rtdocs https://langchain.readthedocs.io/en/latest/
```

示例可以从[这里](https://github.com/hwchase17/chat-langchain)查看。