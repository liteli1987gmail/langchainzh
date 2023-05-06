

BiliBiliLoader
=======

这个加载器使用 [bilibili-api](https://github.com/MoyuScript/bilibili-api) 来从 `B站` 获取文本转录。

使用这个 BiliBiliLoader，用户可以轻松地获取平台上他们所需的视频内容的文字转录。
```
#!pip install bilibili-api

```

```
from langchain.document_loaders.bilibili import BiliBiliLoader

```

```
loader = BiliBiliLoader(
    ["https://www.bilibili.com/video/BV1xt411o7Xu/"]
)

```

```
loader.load()

```

