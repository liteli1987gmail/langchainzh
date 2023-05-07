Roam
==========================================================

本文介绍如何从Roam数据库中加载文档。本文以此示例[repo](https://github.com/JimmyLv/roam-qa)为灵感。

使用方法：

1. 从Roam Research中导出数据集。可以通过单击右上角的三个点，然后单击`导出`进行操作。

2. 在导出时，确保选择`Markdown和CSV`格式选项。

3. 这将在下载文件夹中生成一个`.zip`文件。将`.zip`文件移动到此存储库中。

4. 运行以下命令解压缩zip文件（根据需要将`Export...`替换为您自己的文件名)。

```
unzip Roam-Export-1675782732639.zip -d Roam_DB
```

示例代码： 

```
from langchain.document_loaders import RoamLoader
loader = RoamLoader("Roam_DB")
docs = loader.load()
``` 

返回结果是一个Document对象列表，其中每个对象包含文档内容和元数据。