

如何（以及为什么）使用虚假LLM[#](#how-and-why-to-use-the-fake-llm "Permalink to this headline")
==================================================================================

我们提供了一个用于测试的虚假LLM类。这使您可以模拟对LLM的调用，并模拟LLM以特定方式响应时会发生什么。

在这个笔记本中，我们将介绍如何使用它。

我们从在代理中使用FakeLLM开始。

```
from langchain.llms.fake import FakeListLLM

```

```
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

```

```
tools = load_tools(["python_repl"])

```

```
responses=[
    "Action: Python REPL\nAction Input: print(2 + 2)",
    "Final Answer: 4"
]
llm = FakeListLLM(responses=responses)

```

```
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

```

```
agent.run("whats 2 + 2")

```

```
> Entering new AgentExecutor chain...
Action: Python REPL
Action Input: print(2 + 2)
Observation: 4

Thought:Final Answer: 4

> Finished chain.

```

```
'4'

```

