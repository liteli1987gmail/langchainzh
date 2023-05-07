

SearxNG搜索API[#](#searxng-search-api "此标题的永久链接")
===============================================

本页介绍如何在LangChain中使用SearxNG搜索API。
它分为两个部分：安装和设置，以及特定的SearxNG API包装器的参考。

安装和设置[#](#installation-and-setup "此标题的永久链接")
--------------------------------------------

虽然可以将包装器与[公共searx
实例](https://searx.space/)结合使用，但这些实例经常不允许API
访问（有关输出格式的说明，请参见下面的注释)并且在请求频率上有限制。建议选择自托管实例。

### 自托管实例：[#](#self-hosted-instance "此标题的永久链接")

请参阅[此页](https://searxng.github.io/searxng/admin/installation)了解安装说明。

当您安装SearxNG时，默认情况下唯一的活动输出格式是HTML格式。
您需要激活`json`格式才能使用API。这可以通过将以下行添加到`settings.yml`文件中来完成：

```
search:
 formats:
 - html
 - json

```

您可以通过向API终端发出curl请求来确保API正常工作：

`curl -kLX GET --data-urlencode q='langchain' -d format=json http://localhost:8888`

这应该返回一个带有结果的JSON对象。

包装器[#](#wrappers "Permalink to this headline")
----------------------------------------------

### 实用工具[#](#utility "Permalink to this headline")

要使用包装器，我们需要将SearxNG实例的主机传递给包装器：
1. 在创建实例时使用命名参数`searx_host`。
2. 导出环境变量`SEARXNG_HOST`。

您可以使用包装器从SearxNG实例获取结果。

```
from langchain.utilities import SearxSearchWrapper
s = SearxSearchWrapper(searx_host="http://localhost:8888")
s.run("what is a large language model?")

```

### 工具[#](#tool "Permalink to this headline")

你也可以将此包装器作为工具加载（与代理一起使用)。

你可以通过以下方式实现：

```
from langchain.agents import load_tools
tools = load_tools(["searx-search"],
                    searx_host="http://localhost:8888",
                    engines=["github"])

```

请注意，我们可以选择传递自定义引擎来使用。

如果你想要获取包含元数据的结果作为 json，你可以使用：

```
tools = load_tools(["searx-search-results-json"],
                    searx_host="http://localhost:8888",
                    num_results=5)

```

有关工具的更多信息，请参阅[此页面](../modules/agents/tools/getting_started)

