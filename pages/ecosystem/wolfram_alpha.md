

Wolfram Alpha Wrapper[#](#wolfram-alpha-wrapper "Permalink to this headline")
=============================================================================

本页面介绍如何在LangChain中使用Wolfram Alpha API。它分为两部分：安装和设置，以及特定的Wolfram Alpha包装器的参考。

安装和设置[#](#installation-and-setup "Permalink to this headline")
--------------------------------------------------------------

* 使用`pip install wolframalpha`安装所需的依赖项

* 在wolfram alpha注册开发者帐户[此处](https://developer.wolframalpha.com/)

* 创建应用程序并获取您的APP ID

* 将您的APP ID设置为环境变量`WOLFRAM_ALPHA_APPID`

包装器
----------------------

Utility

有一个WolframAlphaAPIWrapper实用程序，用于包装此API。导入此实用程序：

```
from langchain.utilities.wolfram_alpha import WolframAlphaAPIWrapper

```

有关此包装器的更详细说明，请参见[此教程](../modules/agents/tools/examples/wolfram_alpha)。

工具
----------------------

您还可以将此包装器作为工具轻松地加载到代理中使用。可以使用以下代码完成此操作：

```
from langchain.agents import load_tools
tools = load_tools(["wolfram-alpha"])

```

有关此的更多信息，请参见[此页面](../modules/agents/tools/getting_started)。

