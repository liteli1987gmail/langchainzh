# ReAct

本次演示展示了如何使用一个agent来实现[ReAct](https://react-lm.github.io/)的逻辑。

```python
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import OpenAI
```

## 初始化工具

让我们加载一些要使用的工具。

```python
tools = [TavilySearchResults(max_results=1)]
```

## 创建Agent

```python
# 获取要使用的提示 - 您可以修改这个！
prompt = hub.pull("hwchase17/react")
```

```python
# 选择要使用的LLM
llm = OpenAI()

# 构建ReAct agent
agent = create_react_agent(llm, tools, prompt)
```

## 运行Agent

```python
# 通过传入agent和tools来创建一个agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

```python
agent_executor.invoke({"input": "LangChain是什么?"})
```

    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m 我应该研究一下LangChain以了解更多信息。
    动作: tavily_search_results_json
    动作输入: "LangChain"[0m[36;1m[1;3m[{'url': 'https://www.ibm.com/topics/langchain', 'content': 'LangChain主要是Python和Javascript的抽象库，用于表示常见的步骤和概念  LangChain是一个用于开发使用大型语言模型的应用程序的开源编排框架  其他LangChain功能，如同名的链条。  LangChain提供了超过25种不同的嵌入方法的集成，以及超过50种不同的向量存储方式LangChain是一种使用大型语言模型（LLM）构建应用程序的工具，如聊天机器人和虚拟代理。它简化了编程和与外部数据源和软件工作流程的集成过程。它支持Python和Javascript语言，并支持各种LLM提供商，包括OpenAI、Google和IBM。'}][0m[32;1m[1;3m 我应该阅读摘要并查看LangChain的不同功能和集成。
    动作: tavily_search_results_json
    动作输入: "LangChain的功能和集成"[0m[36;1m[1;3m[{'url': 'https://www.ibm.com/topics/langchain', 'content': "LangChain提供了超过25种不同的嵌入方法的集成，以及超过50种不同的向量存储方式  LangChain是一个用于开发使用大型语言模型的应用程序的开源编排框架  其他LangChain功能，如同名的链条。  LangChain主要是Python和Javascript的抽象库，用于表示常见的步骤和概念由Harrison Chase于2022年10月推出，《LangChain》在2023年6月成为Github上增长最快的开源项目。   在接下来的一个月，随着OpenAI的ChatGPT的重大推出，LangChain在促进生成AI的普及方面发挥了重要作用。"}][0m[32;1m[1;3m 我应该注意LangChain的发布日期和受欢迎程度。
    动作: tavily_search_results_json
    动作输入: "LangChain的发布日期和受欢迎程度"[0m[36;1m[1;3m[{'url': 'https://www.ibm.com/topics/langchain', 'content': "LangChain是一个用于开发使用大型语言模型的应用程序的开源编排框架  其他LangChain功能，如同名的链条。  LangChain提供了超过25种不同的嵌入方法的集成，以及超过50种不同的向量存储方式  LangChain主要是Python和Javascript的抽象库，用于表示常见的步骤和概念由Harrison Chase于2022年10月推出，《LangChain》在2023年6月成为Github上增长最快的开源项目。   在接下来的一个月，随着OpenAI的ChatGPT的重大推出，LangChain在促进生成AI的普及方面发挥了重要作用。"}][0m[32;1m[1;3m 我现在知道最终的答案了。
    最终答案: LangChain是一个使用大型语言模型（LLMs）构建应用程序的开源编排框架，例如聊天机器人和虚拟代理。它是由Harrison Chase于2022年10月推出的，2023年6月，在Github上是增长最快的开源项目。[0m
    
    [1m> 完成链。[0m
    




    {'input': 'LangChain是什么?',
     'output': 'LangChain是一个使用大型语言模型（LLMs）构建应用程序的开源编排框架，例如聊天机器人和虚拟代理。它是由Harrison Chase于2022年10月推出的，2023年6月，在Github上是增长最快的开源项目。'}

## 使用聊天历史

在使用聊天历史时，我们需要一个能考虑到这一点的提示。

```python
# 获取要使用的提示 - 您可以修改这个！
prompt = hub.pull("hwchase17/react-chat")
```

```python
# 构建ReAct agent
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

```python
from langchain_core.messages import AIMessage, HumanMessage

agent_executor.invoke(
    {
        "input": "我的名字是什么？如果需要，请使用工具，否则用最终答案作出回应",
        # 注意，聊天历史是一个字符串，因为这个提示是针对LLMs而不是聊天模型的
        "chat_history": "Human: 你好！我的名字是Bob\nAI: 你好Bob！很高兴认识你",
    }
)
```

    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m思考: 我是否需要使用工具？不需要
    最终答案: 你的名字是Bob。[0m
    
    [1m> 完成链。[0m
    



```
    {'input': '我的名字是什么？如果需要，请使用工具，否则用最终答案作出回应',
     'chat_history': 'Human: 你好！我的名字是Bob\nAI: 你好Bob！很高兴认识你',
     'output': '你的名字是Bob。'}
>>>>>>> main
```