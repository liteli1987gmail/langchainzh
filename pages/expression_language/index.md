# LangChain 表达语言(LCEL)

LangChain 表达语言(LCEL) 是一种声明式方法，可以轻松组合链条。
LCEL 从第一天设计时就目的在于**支持将原型置于生产中，无需更改代码**，无论是最简单的“提示+LLM”链还是最复杂的链(我们见过成功在生产中运行带有数百步骤的LCEL链)。以下是你可能想使用LCEL的几个原因的亮点：

[**一流的流处理支持**](/expression_language/streaming)
当你使用LCEL构建链时，你可以获得尽可能短的首个令牌时间(直到输出的第一个块出来的时间)。对于一些链来说，这意味着我们可以从LLM直接将令牌流式传输到流式输出解析器，您将以与LLM提供程序输出原始令牌的速率相同的速率获得解析的增量输出块。

[**异步支持**](/expression_language/interface)
使用LCEL构建的任何链既可以使用同步API(例如在原型设计时的Jupyter笔记本中)调用，也可以使用异步API(例如在[LangServe](/langsmith)服务器上)调用。这使得您可以在原型和生产环境中使用相同的代码，具有良好的性能，并能够在同一个服务器上处理许多并发请求。

[**优化的并行执行**](/expression_language/primitives/parallel)
只要您的LCEL链有可以并行执行的步骤(例如，如果您从多个提取器中获取文档)，我们会自动执行它，无论是同步接口还是异步接口，以获得最小的延迟。

[**重试和回退**](/docs/guides/productionization/fallbacks)
为LCEL链的任何部分配置重试和回退。这是使您的链在大规模环境中更加可靠的好方法。我们目前正在添加重试/回退的流处理支持，这样您就可以在不牺牲延迟的情况下获得更高的可靠性。

[**访问中间结果**](/expression_language/interface#async-stream-events-beta)
对于更复杂的链，访问中间步骤的结果通常非常有用，即使在最终输出产生之前。这可以用于让最终用户知道发生了什么，甚至只是用于调试链。您可以流式传输中间结果，在每个[LangServe](/docs/langserve)服务器上都可以使用。

[**输入和输出模式**](/expression_language/interface#input-schema)
输入和输出模式根据链的结构推断出每个LCEL链的Pydantic和JSONSchema模式。这可以用于验证输入和输出，并且是LangServe的一个重要组成部分。

[**无缝的LangSmith跟踪**](/langsmith)
随着链条变得越来越复杂，了解每个步骤发生的具体情况变得越来越重要。
在LCEL中，**所有**步骤都自动记录到[LangSmith](/langsmith/)，以实现最大的可观察性和可调试性。

[**无缝的LangServe部署**](https://python.langchain.com/v0.2/docs//langserve/)
使用LCEL创建的任何链都可以轻松部署使用[LangServe](https://python.langchain.com/v0.2/docs//langserve/)。# 基本元素

除了可与LCEL一起使用的各种组件之外，LangChain还包括各种基本元素，这些元素有助于传递和格式化数据、绑定参数、调用自定义逻辑等等。



