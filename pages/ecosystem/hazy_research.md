

朦胧研究[#](#hazy-research "此标题的永久链接")
==================================

本页面介绍如何在LangChain中使用朦胧研究生态系统。分为两部分：安装和设置，以及对特定朦胧研究包的引用。

安装和设置[#](#installation-and-setup "此标题的永久链接")
--------------------------------------------

* 使用`清单`，请使用`pip install manifest-ml`安装。

包装器[#](#wrappers "此标题的永久链接")
----------------------------

### LLM[#](#llm "此标题的永久链接")

在Hazy Research的`manifest`库周围存在一个LLM包装器。
`manifest`是一个Python库，它本身是许多模型提供商的包装器，并添加了缓存、历史记录等功能。

使用该包装器的方法：

```
from langchain.llms.manifest import ManifestWrapper

```

