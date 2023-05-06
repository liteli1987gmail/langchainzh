GitBook
=====================================================

本文介绍如何从任何GitBook中获取页面数据。

引入GitbookLoader：

```
from langchain.document_loaders import GitbookLoader
```

指定加载的GitBook网址：

```
loader = GitbookLoader("https://docs.gitbook.com")
```

加载单个页面：

```
page_data = loader.load()
```

输出第一个页面的内容：

```
print(page_data[0])
```

加载GitBook上所有页面的内容：

```
loader = GitbookLoader("https://docs.gitbook.com", load_all_paths=True)

all_pages_data = loader.load()
```

输出加载的文档数量：

```
print(f"fetched {len(all_pages_data)} documents.")
```

输出第三个页面的内容：

```
all_pages_data[2]
```