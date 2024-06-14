# 使用工具

这节内容将介绍如何创建对话代理：能够使用工具与其他系统和API进行交互的聊天机器人。

在阅读本指南之前，我们建议您先阅读本节中的[聊天机器人快速入门](/use_cases/chatbots/quickstart)，并熟悉[代理文档](/modules/agents/)。

## 设置

在本指南中，我们将使用一个包含单个用于搜索网络的工具的[OpenAI工具代理](/modules/agents/agent_types/openai_tools)。默认情况下，将使用[Tavily](/docs/integrations/tools/tavily_search)提供的功能，但您可以将其替换为任何类似的工具。本节其他内容将假定您正在使用Tavily。

您需要在Tavily网站上[注册账户](https://tavily.com/)，并安装以下软件包：

```python
%pip install --upgrade --quiet langchain-openai tavily-python

# 设置环境变量 OPENAI_API_KEY 或从 .env 文件中加载：
import dotenv

dotenv.load_dotenv()
```

    [33m警告: 您正在使用 pip 版本 22.0.4；但是版本 23.3.2 可用。
    您应考虑使用以下命令升级：
    /Users/jacoblee/.pyenv/versions/3.10.5/bin/python -m pip install --upgrade pip[0m[33m
注意：您可能需要重新启动内核以使用更新的软件包。
    




    True



您还需要设置您的OpenAI密钥为 `OPENAI_API_KEY`，并将您的Tavily API密钥设置为 `TAVILY_API_KEY`。

## 创建一个代理

我们的最终目标是创建一个代理，能够根据需要在查找信息时以对话的形式回答用户的问题。

首先，让我们初始化Tavily和一个可以调用工具的OpenAI聊天模型：

```python
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI

tools = [TavilySearchResults(max_results=1)]

# 选择将驱动代理的LLM
# 只有某些模型支持这个
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
```

为了使我们的代理具有对话功能，我们还必须选择一个包含聊天记录占位符的提示。以下是一个示例：

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 适用于 https://smith.langchain.com/hub/hwchase17/openai-tools-agent 示例的修改版
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个有帮助的助手。并非每个查询都需要使用工具——用户可能只是想聊天！",
        ),
        MessagesPlaceholder(variable_name="messages"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
```

好了！现在让我们组装我们的代理：

```python
from langchain.agents import AgentExecutor, create_openai_tools_agent

agent = create_openai_tools_agent(chat, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

## 运行代理

既然我们已经设置好了代理，让我们尝试与它交互！它可以处理不需要查找的简单查询：

```python
from langchain_core.messages import HumanMessage

agent_executor.invoke({"messages": [HumanMessage(content="我是Nemo！")]})
```

    
    
    [1m> 进入新的 AgentExecutor 链...[0m
    [32;1m[1;3m你好 Nemo！很高兴见到你。你有什么问题需要我的帮助吗？[0m
    
    [1m> 链结束。[0m
    




    {'messages': [HumanMessage(content='我是Nemo！')],
     'output': '你好 Nemo！很高兴见到你。你有什么问题需要我的帮助吗？'}



或者，如果需要的话，它可以使用传递的搜索工具获取最新信息：

```python
agent_executor.invoke(
    {
        "messages": [
            HumanMessage(
                content="大堡礁当前的保育状况如何？"
            )
        ],
    }
)
```

    
    
    [1m> 进入新的 AgentExecutor 链...[0m
    [32;1m[1;3m
    调用：`tavily_search_results_json`，参数为`{'query': '大堡礁当前的保育状况'}`
    
    
    [0m[36;1m[1;3m[{'url': 'https://www.barrierreef.org/news/blog/this-is-the-critical-decade-for-coral-reef-survival', 'content': '大堡礁全球珊瑚礁保育。©2024 Great Barrier Reef Foundation. 网站由bigfish.tv提供的支持 #相关新闻·2024年1月29日 2.9亿个新珊瑚宝宝助力恢复和保护大堡礁 大堡礁基金会执行董事Anna Marsden表示，如果我们现在采取行动，就还来得及。《2020年世界珊瑚礁状况报告》是有史以来规模最大的全球珊瑚礁健康分析。报告发现，自2009年以来，全球14%的珊瑚礁已经消失。然而，报告还指出，这些珊瑚中的一些在2019年之前的10年内得到了恢复。}][0m[32;1m[1;3m大堡礁当前的保育状况是一个紧急关切的问题。根据大堡礁基金会的《2020年世界珊瑚礁状况报告》，自2009年以来，全球14%的珊瑚礁已经消失。然而，该报告还指出，这些珊瑚中的一些在2019年之前的10年内得到了恢复。有关更多信息，请访问以下链接：[Great Barrier Reef Foundation - 保育状况](https://www.barrierreef.org/news/blog/this-is-the-critical-decade-for-coral-reef-survival)[0m
    
    [1m> 链结束。[0m
    




    {'messages': [HumanMessage(content='大堡礁当前的保育状况如何？')],
     'output': '大堡礁当前的保育状况是一个紧急关切的问题。根据大堡礁基金会的《2020年世界珊瑚礁状况报告》，自2009年以来，全球14%的珊瑚礁已经消失。然而，该报告还指出，这些珊瑚中的一些在2019年之前的10年内得到了恢复。有关更多信息，请访问以下链接：[Great Barrier Reef Foundation - 保育状况](https://www.barrierreef.org/news/blog/this-is-the-critical-decade-for-coral-reef-survival)'}



## 对话回复

因为我们的提示包含了一个用于聊天历史记录的占位符，我们的代理还可以考虑以往的交互，并像标准聊天机器人一样进行对话回复：

```python
from langchain_core.messages import AIMessage, HumanMessage

agent_executor.invoke(
    {
        "messages": [
            HumanMessage(content="我是Nemo！"),
            AIMessage(content="你好 Nemo！你有什么问题需要我的帮助吗？"),
            HumanMessage(content="我的名字是什么？"),
        ],
    }
)
```

    
    
    [1m> 进入新的 AgentExecutor 链...[0m
    [32;1m[1;3m你的名字是 Nemo！[0m
    
    [1m> 链结束。[0m
    




    {'messages': [HumanMessage(content='我是Nemo！'),
      AIMessage(content='你好 Nemo！你有什么问题需要我的帮助吗？'),
      HumanMessage(content='我的名字是什么？')],
     'output': '你的名字是 Nemo！'}



如果需要，您还可以将代理执行器包装在一个`RunnableWithMessageHistory`类中以在内部管理历史消息。首先，我们需要略微修改提示，以接受单独的输入变量，以便包装器可以解析要存储为历史记录的输入值：

```python
# 适用于 https://smith.langchain.com/hub/hwchase17/openai-tools-agent 示例的修改版
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个有帮助的助手。并非每个查询都需要使用工具——用户可能只是想聊天！",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent = create_openai_tools_agent(chat, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

然后，由于我们的代理执行器具有多个输出，我们还必须在初始化包装器时设置 `output_messages_key` 属性：

```python
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

demo_ephemeral_chat_history_for_chain = ChatMessageHistory()

conversational_agent_executor = RunnableWithMessageHistory(
    agent_executor,
    lambda session_id: demo_ephemeral_chat_history_for_chain,
    input_messages_key="input",
    output_messages_key="output",
    history_messages_key="chat_history",
)
```


```python
conversational_agent_executor.invoke(
    {
        "input": "我是Nemo！",
    },
    {"configurable": {"session_id": "unused"}},
)
```

    
    
    [1m> 进入新的 AgentExecutor 链...[0m
    [32;1m[1;3m嗨 Nemo！很高兴见到你。你有什么问题需要我的帮助吗？[0m
    
    [1m> 链结束。[0m
    




    {'input': '我是Nemo！',
     'chat_history': [],
     'output': '嗨 Nemo！很高兴见到你。你有什么问题需要我的帮助吗？'}



```python
conversational_agent_executor.invoke(
    {
        "input": "我的名字是什么？",
    },
    {"configurable": {"session_id": "unused"}},
)
```

    
    
    [1m> 进入新的 AgentExecutor 链...[0m
    [32;1m[1;3m你的名字是 Nemo！你有什么问题需要我的帮助吗，Nemo？[0m
    
    [1m> 链结束。[0m
    




    {'input': '我的名字是什么？',
     'chat_history': [HumanMessage(content='我是Nemo！'),
      AIMessage(content='嗨 Nemo！很高兴见到你。你有什么问题需要我的帮助吗？')],
     'output': '你的名字是 Nemo！你有什么问题需要我的帮助吗，Nemo？'}


------

## 进一步阅读

其他类型的代理也可以支持对话式回应——想要了解更多，请查看[代理人部分](/modules/agents)。

关于工具使用的更多信息，您还可以查看[此用例部分](/use_cases/tool_use/)。
