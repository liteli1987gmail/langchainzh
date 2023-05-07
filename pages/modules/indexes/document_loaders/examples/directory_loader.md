目录加载器
 [#](#directory-loader "Permalink to this headline")
=======================================================================



本文介绍如何使用DirectoryLoader来加载目录中的所有文档。在默认情况下，它使用 `UnstructuredLoader` 进行操作。
 
```
from langchain.document_loaders import DirectoryLoader

```

我们可以使用 `glob` 参数来控制加载哪些文件。请注意，这里不加载 `.rst` 文件或 `.ipynb` 文件。
 
```
loader = DirectoryLoader('../', glob="**/*.md")

```

```
docs = loader.load()

```

```
len(docs)

```

显示进度条
 [#](#show-a-progress-bar "Permalink to this headline")
-----------------------------------------------------------------------------

默认情况下，不会显示进度条。要显示进度条，请安装 `tqdm` 库（例如 `pip install tqdm`)，并将 `show_progress` 参数设置为 `True` 。

```
%pip install tqdm
loader = DirectoryLoader('../', glob="**/*.md", show_progress=True)
docs = loader.load()

```

更改加载器类
 [#](#change-loader-class "Permalink to this headline")
-----------------------------------------------------------------------------

默认情况下，它使用 `UnstructuredLoader` 类。但是，你可以相当容易地改变加载器的类型。

```
from langchain.document_loaders import TextLoader

```

```
loader = DirectoryLoader('../', glob="**/*.md", loader_cls=TextLoader)

```

```
docs = loader.load()

```

```
len(docs)

```

如果您需要加载Python源代码文件，请使用 `PythonLoader`。

```
from langchain.document_loaders import PythonLoader

```

```
loader = DirectoryLoader('../../../../../', glob="**/*.py", loader_cls=PythonLoader)

```

```
docs = loader.load()

```

```
len(docs)

```