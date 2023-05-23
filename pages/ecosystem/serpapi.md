

SerpAPI[#](#serpapi "跳转到此标题的永久链接")
==================================

本页面介绍如何在LangChain中使用SerpAPI搜索API。它分为两个部分：安装和设置，以及对特定SerpAPI包装器的引用。

安装和设置[#](#installation-and-setup "跳转到此标题的永久链接")
-----------------------------------------------

* 使用`pip install google-search-results`安装要求。

* 获取SerpAPI api密钥，将其设置为环境变量（`SERPAPI_API_KEY`)之一。

包装器[#](#wrappers "跳转到此标题的永久链接")
-------------------------------

### 实用工具[#](#utility "跳转到此标题的永久链接")

存在一个SerpAPI实用程序，它包装了这个API。要导入此实用程序：

```
from langchain.utilities import SerpAPIWrapper

```

更详细的教程可以查看[本教程](../modules/agents/tools/examples/serpapi)。

### 工具[#](#tool "Permalink to this headline")

您还可以将此包装器轻松加载为工具(与代理一起使用)。
您可以使用以下命令完成此操作：

```
from langchain.agents import load_tools
tools = load_tools(["serpapi"])

```

有关更多信息，请参见[此页面](../modules/agents/tools/getting_started)

