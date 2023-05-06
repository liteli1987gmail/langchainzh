

# 代理类型[#](#agent-types "Permalink to this headline")

代理使用LLM（语言模型）来确定应采取哪些操作以及以何顺序执行这些操作。

动作可能是使用工具并观察其输出，或向用户返回响应。

以下是LangChain中可用的代理：

## 零-shot反应描述[#](#zero-shot-react-description "Permalink to this headline")

此代理使用ReAct框架，仅基于工具的描述来确定要使用的工具。可以提供任意数量的工具。

此代理需要为每个工具提供描述。

`react-docstore`[#](#react-docstore "Permalink to this headline")
-----------------------------------------------------------------

这个代理使用ReAct框架与文档存储进行交互。必须提供两个工具：一个`搜索`工具和一个`查找`工具（它们必须被命名为这样）。`搜索`工具应该搜索文档，而`查找`工具应该查找最近找到的文档中的一个术语。这个代理相当于原始的[ReAct论文](https://arxiv.org/pdf/2210.03629.pdf)，特别是维基百科的例子。

`self-ask-with-search`[#](#self-ask-with-search "标题的永久链接")
----------------------------------------------------------

这个代理使用一个被命名为`Intermediate Answer`的工具。这个工具应该能够查找问题的事实性答案。这个代理相当于原始的[self ask with search paper](https://ofir.io/self-ask.pdf)，其中提供了Google搜索API作为工具。

### `conversational-react-description`[#](#conversational-react-description "Permalink to this headline")

This agent is designed to be used in conversational settings.
The prompt is designed to make the agent helpful and conversational.
It uses the ReAct framework to decide which tool to use, and uses memory to remember the previous conversation interactions.

