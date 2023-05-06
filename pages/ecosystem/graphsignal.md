

Graphsignal[#](#graphsignal "Permalink to this headline")
=========================================================

本页介绍如何使用[Graphsignal](https://app.graphsignal.com)跟踪和监控LangChain。Graphsignal可以完全可视化您的应用程序。它提供了链和工具的延迟细分，带有完整上下文的异常，数据监控，计算/GPU利用率，OpenAI成本分析等。

安装和设置[#](#installation-and-setup "Permalink to this headline")
--------------------------------------------------------------

* 使用`pip install graphsignal`安装Python库

* 在[此处](https://graphsignal.com)创建免费的Graphsignal账户

* 获取API密钥并将其设置为环境变量(`GRAPHSIGNAL_API_KEY`)

追踪和监控[#](#tracing-and-monitoring "Permalink to this headline")
--------------------------------------------------------------

Graphsignal会自动进行仪器化和启动追踪和监控链。 然后，可在您的[Graphsignal仪表板](https://app.graphsignal.com)中使用跟踪和指标。

通过提供部署名称来初始化跟踪器：

```
import graphsignal

graphsignal.configure(deployment='my-langchain-app-prod')

```

要额外跟踪任何函数或代码，可以使用装饰器或上下文管理器：

```
@graphsignal.trace_function
def handle_request():    
    chain.run("some initial text")

```

```
with graphsignal.start_trace('my-chain'):
    chain.run("some initial text")

```

可选择启用分析，以记录每个跟踪的函数级统计信息。

```
with graphsignal.start_trace(
        'my-chain', options=graphsignal.TraceOptions(enable_profiling=True)):
    chain.run("some initial text")

```

请参阅[快速入门](https://graphsignal.com/docs/guides/quick-start/)指南，了解完整的设置说明。

