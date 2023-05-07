

入门[#](#getting-started "到这个标题的永久链接")
====================================

代理使用LLM来确定采取哪些行动以及顺序。
一个动作可以是使用工具并观察其输出，或返回给用户。

当代理被正确使用时，它们可以非常强大。这个笔记本的目的是向您展示如何通过最简单、最高级别的API轻松使用代理。

为了加载代理，您应该了解以下概念：

* 工具：执行特定职责的函数。这可以是诸如：Google搜索、数据库查找、Python REPL、其他链等。工具的接口目前是期望有一个字符串作为输入，一个字符串作为输出的函数。

* LLM：为代理提供动力的语言模型。

* 代理：要使用的代理。这应该是一个引用支持代理类的字符串。因为这个笔记本专注于最简单、最高级别的API，所以只涵盖使用标准支持的代理。如果您想实现自定义代理，请参阅自定义代理的文档（即将推出)。

**代理人**：支持的代理人清单及其规格，请参见[此处](agents)。

**工具**：预定义工具及其规格的清单，请参见[此处](tools)。

```
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

```

首先，让我们加载我们要使用的语言模型来控制代理人。

```
llm = OpenAI(temperature=0)

```

接下来，让我们加载一些要使用的工具。请注意，`llm-math`工具使用LLM，因此我们需要传递它。

```
tools = load_tools(["serpapi", "llm-math"], llm=llm)

```

最后，让我们使用工具、语言模型和我们想要使用的代理人类型初始化一个代理人。

```
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

```

现在让我们来测试一下吧！

```
agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

```

```
> Entering new AgentExecutor chain...
 I need to find out who Leo DiCaprio's girlfriend is and then calculate her age raised to the 0.43 power.
Action: Search
Action Input: "Leo DiCaprio girlfriend"
Observation: Camila Morrone
Thought: I need to find out Camila Morrone's age
Action: Search
Action Input: "Camila Morrone age"
Observation: 25 years
Thought: I need to calculate 25 raised to the 0.43 power
Action: Calculator
Action Input: 25^0.43
Observation: Answer: 3.991298452658078

Thought: I now know the final answer
Final Answer: Camila Morrone is Leo DiCaprio's girlfriend and her current age raised to the 0.43 power is 3.991298452658078.

> Finished chain.

```

```
"Camila Morrone is Leo DiCaprio's girlfriend and her current age raised to the 0.43 power is 3.991298452658078."

```

