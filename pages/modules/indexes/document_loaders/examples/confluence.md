

Confluence[#](#confluence "Permalink to this headline")
=======================================================

> 
> [Confluence](https://www.atlassian.com/software/confluence) 是一个 Wiki 协作平台，可保存和组织所有与项目相关的资料。`Confluence` 是一个主要处理内容管理活动的知识库。
> 
> 
> 

用于加载 `Confluence` 页面的加载程序。

目前支持 `username/api_key` 和 `Oauth2 login`。

指定要加载的页面 ID 和/或空间键列表，将相应的页面加载到文档对象中，如果两者都指定，则返回两个集合的并集。

您还可以指定一个布尔值`include_attachments`来包括附件。默认值为False，如果设置为True，则会下载所有附件，并且ConfluenceReader将从附件中提取文本并将其添加到文档对象中。目前支持的附件类型有：`PDF`、`PNG`、`JPEG/JPG`、`SVG`、`Word`和`Excel`。

提示：`space_key`和`page_id`都可以在Confluence页面的URL中找到 - https://yoursite.atlassian.com/wiki/spaces/<space_key>/pages/<page_id>

```
#!pip install atlassian-python-api

```

```
from langchain.document_loaders import ConfluenceLoader

loader = ConfluenceLoader(
    url="https://yoursite.atlassian.com/wiki",
    username="me",
    api_key="12345"
)
documents = loader.load(space_key="SPACE", include_attachments=True, limit=50)

```

