# JSON 聊天代理

有些语言模型特别擅长编写JSON。这个代理使用JSON来格式化其输出，旨在支持聊天模型。

```python
from langchain import hub
from langchain.agents import AgentExecutor, create_json_chat_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
```

## 初始化工具

我们将初始化我们想要使用的工具

```python
tools = [TavilySearchResults(max_results=1)]
```

## 创建代理

```python
# 获取要使用的提示 - 您可以修改这个！
prompt = hub.pull("hwchase17/react-chat-json")
```

```python
# 选择驱动代理的LLM
llm = ChatOpenAI()

# 构建JSON代理
agent = create_json_chat_agent(llm, tools, prompt)
```

## 运行代理

```python
# 通过传入代理和工具来创建一个代理执行程序
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)
```

```python
agent_executor.invoke({"input": "什么是LangChain?"})
```

```python
{'input': 'what is LangChain?',
 'output': 'LangChain是用于使用大型语言模型开发应用程序的开源编排框架。它简化了编程和与外部数据源以及软件工作流集成的过程。它支持Python和Javascript语言，并支持包括OpenAI、Google和IBM在内的各种LLM提供商。'}
```

## 使用聊天历史

```python
from langchain_core.messages import AIMessage, HumanMessage

agent_executor.invoke(
    {
        "input": "我的名字是什么？",
        "chat_history": [
            HumanMessage(content="嗨！我叫鲍勃"),
            AIMessage(content="你好，鲍勃！我今天可以如何帮助您？"),
        ],
    }
)
```

```python
{'input': "what's my name?",
 'chat_history': [HumanMessage(content='hi! my name is bob'),
  AIMessage(content='Hello Bob! How can I assist you today?')],
 'output': '您的名字是鲍勃。'}
```

```python

```

