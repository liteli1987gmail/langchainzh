

Google搜索包装器[#](#google-search-wrapper "此标题的永久链接")
=================================================

本页面介绍如何在LangChain中使用Google搜索API。它分为两个部分：安装和设置，以及对特定Google搜索包装器的引用。

安装和设置[#](#installation-and-setup "此标题的永久链接")
--------------------------------------------

* 使用`pip install google-api-python-client`安装要求

* 按照[这些说明](https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search)设置自定义搜索引擎

* 从前面的步骤中获取API密钥和自定义搜索引擎ID，并将它们设置为环境变量`GOOGLE_API_KEY`和`GOOGLE_CSE_ID`

包装器[#](#wrappers "此标题的永久链接")
----------------------------

### 实用工具[#](#utility "此标题的永久链接")

存在一个GoogleSearchAPIWrapper实用工具，它包装了这个API。要导入此实用工具：

```
from langchain.utilities import GoogleSearchAPIWrapper

```

有关此包装器的更详细步骤，请参见[此笔记本电脑](../modules/agents/tools/examples/google_search)。

### 工具[#](#tool "此标题的永久链接")

您还可以将此包装器轻松加载为工具（用于与代理一起使用)。
您可以使用以下命令完成此操作：

```
from langchain.agents import load_tools
tools = load_tools(["google-search"])

```

了解更多信息，请查看[此页面](../modules/agents/tools/getting_started)

