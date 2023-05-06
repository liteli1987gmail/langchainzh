Git
=============================================

这篇文章展示了如何从Git仓库中加载文本文件。

从磁盘加载仓库：

```
from git import Repo

repo = Repo.clone_from(
    "https://github.com/hwchase17/langchain", to_path="./example_data/test_repo1"
)

# 获取当前分支
branch = repo.head.reference
```

使用GitLoader加载：

```
from langchain.document_loaders import GitLoader

loader = GitLoader(repo_path="./example_data/test_repo1/", branch=branch)

data = loader.load()
```

输出个别文件的内容：

```
print(data[0])
```

从远程地址克隆仓库：

```
loader = GitLoader(
    clone_url="https://github.com/hwchase17/langchain",
    repo_path="./example_data/test_repo2/",
    branch="master",
)

data = loader.load()
```

使用过滤器加载指定类型的文件：

```
from langchain.document_loaders import GitLoader

# 比如只加载python文件
loader = GitLoader(repo_path="./example_data/test_repo1/", file_filter=lambda file_path: file_path.endswith(".py"))
```