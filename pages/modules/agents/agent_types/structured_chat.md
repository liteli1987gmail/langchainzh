# 结构化聊天

结构化聊天代理能够使用多输入工具。

```python
from langchain import hub
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
```

## 初始化工具

我们将使用 Tavily Search 工具来测试代理

```python
tools = [TavilySearchResults(max_results=1)]
```

## 创建代理

```python
# 获取要使用的提示 - 您可以修改这个！
prompt = hub.pull("hwchase17/structured-chat-agent")
```

```python
# 选择驱动代理的 LLM
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-1106")

# 构建 JSON 代理
agent = create_structured_chat_agent(llm, tools, prompt)
```

## 运行代理

```python
# 通过传入代理和工具来创建代理执行器
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)
```

```python
agent_executor.invoke({"input": "什么是 LangChain?"})
```

```python
{'input': 'what is LangChain?',
 'output': 'LangChain is an open source orchestration framework for the development of applications using large language models. It simplifies the process of programming and integration with external data sources and software workflows. LangChain provides integrations for over 25 different embedding methods and supports various large language model providers such as OpenAI, Google, and IBM. It supports Python and Javascript languages.'}
```

## 与聊天历史一起使用

```python
from langchain_core.messages import AIMessage, HumanMessage

agent_executor.invoke(
    {
        "input": "我的名字是什么? 除非必须，否则不使用工具",
        "chat_history": [
            HumanMessage(content="hi! my name is bob"),
            AIMessage(content="Hello Bob! How can I assist you today?"),
        ],
    }
)
```

```python
{'input': "what's my name? Do not use tools unless you have to",
 'chat_history': [HumanMessage(content='hi! my name is bob'),
  AIMessage(content='Hello Bob! How can I assist you today?')],
 'output': 'Your name is Bob.'}
```