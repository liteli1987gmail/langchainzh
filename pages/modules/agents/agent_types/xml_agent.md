# XML Agent

某些语言模型（如Anthropic的Claude）在处理XML时表现特别出色。本文介绍如何使用XML代理程序进行提示。

:::⚠⚠⚠



* 仅与常规LLM一起使用，不要与聊天模型一起使用。
* 仅与非结构化工具一起使用，即只接受单个字符串输入的工具。
* 有关更多代理类型，请参阅[AgentTypes](/modules/agents/agent_types/)文档。
:::

```python
from langchain import hub
from langchain.agents import AgentExecutor, create_xml_agent
from langchain_anthropic.chat_models import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
```

## 初始化工具

我们将初始化要使用的工具

```python
tools = [TavilySearchResults(max_results=1)]
```

## 创建代理

下面我们将使用LangChain内置的[create_xml_agent](https://api.python.langchain.com/en/latest/agents/langchain.agents.xml.base.create_xml_agent.html)构造函数。

```python
# 获取要使用的提示-您可以修改这个！
prompt = hub.pull("hwchase17/xml-agent-convo")
```

```python
# 选择将驱动代理的LLM
llm = ChatAnthropic(model="claude-2.1")

# 构建XML代理
agent = create_xml_agent(llm, tools, prompt)
```

## 运行代理

```python
# 通过传入代理和工具来创建代理执行器
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

```python
agent_executor.invoke({"input": "LangChain是什么?"})
```

```
[1m> 进入新的AgentExecutor链...[0m
[32;1m[1;3m <tool>tavily_search_results_json</tool><tool_input>LangChain是什么?[0m[36;1m[1;3m[{'url': 'https://aws.amazon.com/what-is/langchain/', 'content': 'What Is LangChain? What is LangChain?  How does LangChain work?  Why is LangChain important?  that LangChain provides to reduce development time.LangChain is an open source framework for building applications based on large language models (LLMs). LLMs are large deep-learning models pre-trained on large amounts of data that can generate responses to user queries—for example, answering questions or creating images from text-based prompts.'}][0m[32;1m[1;3m <final_answer>LangChain是一个基于大型语言模型（LLMs）构建应用程序的开源框架。LLMs是在大量数据上进行预训练的大型深度学习模型，可以生成对用户查询的响应，例如回答问题或根据以文本为基础的提示创建图像。LangChain提供了降低开发时间的功能。</final_answer>[0m

[1m> 链结束。[0m
```

```
{'input': 'LangChain是什么?',
 'output': 'LangChain是一个基于大型语言模型（LLMs）构建应用程序的开源框架。LLMs是在大量数据上进行预训练的大型深度学习模型，可以生成对用户查询的响应，例如回答问题或根据以文本为基础的提示创建图像。LangChain提供了降低开发时间的功能。'}
```

## 在聊天记录中使用

```python
from langchain_core.messages import AIMessage, HumanMessage

agent_executor.invoke(
    {
        "input": "我的名字是什么？只有在需要时使用工具，否则用最终答案回答",
        # 注意，聊天历史是一个字符串，因为这个提示是针对LLMs而不是聊天模型的
        "chat_history": "Human: 嗨！我的名字是Bob\nAI: 你好Bob！很高兴认识你",
    }
)
```

```
[1m> 进入新的AgentExecutor链...[0m
[32;1m[1;3m <final_answer>你的名字是Bob。</final_answer>

由于你已经告诉我你的名字是Bob，我不需要使用任何工具来回答“我的名字是什么？”这个问题。我可以直接提供最终答案，即你的名字是Bob。[0m

[1m> 链结束。[0m
```

```
{'input': '我的名字是什么？只有在需要时使用工具，否则用最终答案回答',
 'chat_history': 'Human: 嗨！我的名字是Bob\nAI: 你好Bob！很高兴认识你',
 'output': '你的名字是Bob。'}
```

# 自定义XML代理

**注意：**为了更高度的可定制性，我们建议查看[LangGraph](/docs/langgraph)。

这里我们提供一个自定义XML代理实现的示例，以便让您了解`create_xml_agent`在幕后所做的工作。

```python
from langchain.agents.output_parsers import XMLAgentOutputParser
```

```python
# 将中间步骤转换为要传递给模型的字符串的逻辑
# 这与提示中的指令相当紧密地耦合在一起
def convert_intermediate_steps(intermediate_steps):
    log = ""
    for action, observation in intermediate_steps:
        log += (
            f"<tool>{action.tool}</tool><tool_input>{action.tool_input}"
            f"</tool_input><observation>{observation}</observation>"
        )
    return log


# 将工具转换为要放入提示中的字符串的逻辑
def convert_tools(tools):
    return "\n".join([f"{tool.name}: {tool.description}" for tool in tools])
```

从可运行的代码构建代理通常涉及以下几点：

1. 中间步骤的数据处理。这些步骤需要以语言模型能够识别的方式表示。这应该与提示中的说明相当紧密地耦合在一起。

2. 提示本身

3. 包含停止令牌的模型（如果需要）

4. 输出解析器-应与提示中指定的格式相匹配。

```python
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: convert_intermediate_steps(
            x["intermediate_steps"]
        ),
    }
    | prompt.partial(tools=convert_tools(tools))
    | llm.bind(stop=["</tool_input>", "</final_answer>"])
    | XMLAgentOutputParser()
)
```

```python
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

```python
agent_executor.invoke({"input": "what is LangChain?"})
```

```
[1m> 进入新的AgentExecutor链...[0m
[32;1m[1;3m<tool>tavily_search_results_json</tool>
<tool_input>what is LangChain[0m[36;1m[1;3m[{'url': 'https://www.techtarget.com/searchEnterpriseAI/definition/LangChain', 'content': "Everything you need to know\nWhat are the features of LangChain?\nLangChain is made up of the following modules that ensure the multiple components needed to make an effective NLP app can run smoothly:\nWhat are the integrations of LangChain?\nLangChain typically builds applications using integrations with LLM providers and external sources where data can be found and stored. What is synthetic data?\nExamples and use cases for LangChain\nThe LLM-based applications LangChain is capable of building can be applied to multiple advanced use cases within various industries and vertical markets, such as the following:\nReaping the benefits of NLP is a key of why LangChain is important. As the airline giant moves more of its data workloads to the cloud, tools from Intel's Granulate are making platforms such as ...\nThe vendor's new platform, now in beta testing, combines its existing lakehouse with AI to better enable users to manage and ...\n The following steps are required to use this:\nIn this scenario, the language model would be expected to take the two input variables -- the adjective and the content -- and produce a fascinating fact about zebras as its output.\n The goal of LangChain is to link powerful LLMs, such as OpenAI's GPT-3.5 and GPT-4, to an array of external data sources to create and reap the benefits of natural language processing (NLP) applications.\n"}][0m[32;1m[1;3m<final_answer>
LangChain是由Anthropic开发的平台，通过将GPT-3.5和GPT-4等大型语言模型与外部数据源进行链接，使用户能够构建NLP应用程序。它提供管理和集成NLP应用所需的各种组件的模块。

LangChain的一些主要功能和特点：

- 允许将LLMs与外部数据源进行链接，以创建定制的NLP应用程序
- 提供管理LLMs、数据源、存储等集成的模块
- 支持构建对话式AI应用、摘要、搜索和其他NLP功能
- 帮助用户在各个行业中实现NLP和LLMs的效益

总之，它是一个通过更可定制和可扩展的方式利用大型语言模型的能力来构建和部署先进的NLP模型的平台。

[0m

[1m> 链结束。[0m
```

```
{'input': 'what is LangChain?',
 'output': 'LangChain是由Anthropic开发的平台，通过将GPT-3.5和GPT-4等大型语言模型与外部数据源进行链接，使用户能够构建NLP应用程序。它提供管理和集成NLP应用所需的各种组件的模块。

LangChain的一些主要功能和特点：

- 允许将LLMs与外部数据源进行链接，以创建定制的NLP应用程序
- 提供管理LLMs、数据源、存储等集成的模块
- 支持构建对话式AI应用、摘要、搜索和其他NLP功能
- 帮助用户在各个行业中实现NLP和LLMs的效益

总之，它是一个通过更可定制和可扩展的方式利用大型语言模型的能力来构建和部署先进的NLP模型的平台。'}
```

请以7个等号开始，7个等号结束的格式提供您的回答。=======

LangChain是由Anthropic开发的一个平台，它可以将类似GPT-3.5和GPT-4这样的大型语言模型与外部数据源进行链接，从而使用户能够构建自然语言处理应用程序。它提供了用于管理和集成NLP应用所需的不同组件的模块。

LangChain的一些关键能力和特性包括:

- 允许将语言模型与外部数据源进行链接，创建定制化的NLP应用程序
- 提供模块来管理语言模型、数据源、存储等的集成
- 可以构建对话式AI应用、摘要、搜索和其他NLP能力
- 帮助用户在各个行业的用例中获取NLP和语言模型的好处

因此，总结起来，LangChain是一个通过更加可定制和可扩展的方式利用大型语言模型的能力来构建和部署先进的NLP模型的平台。

