Notion
===================================================

本文介绍如何从Notion数据库转储中加载文档。

要获取这个Notion转储，请按照以下说明操作：

🧑 自定义数据集的说明

从Notion导出数据集，您可以通过点击右上角的三个点然后点击 “导出” 来完成。

在导出时，请确保选择“Markdown和CSV”格式选项。

这将在您的下载文件夹中生成一个.zip文件。将.zip文件移动到该存储库中。

运行以下命令解压缩zip文件（根据需要替换“Export…”为您自己的文件名)。

```
unzip Export-d3adfe0f-3131-4bf3-8987-a52017fc1bae.zip -d Notion_DB

```

运行以下命令摄取数据。

```
from langchain.document_loaders import NotionDirectoryLoader
loader = NotionDirectoryLoader("Notion_DB")
docs = loader.load()
```