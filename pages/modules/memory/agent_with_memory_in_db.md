# 数据库中带记忆的代理（AgentWithMemoryInDb）

这篇笔记介绍了向代理添加内存的过程，其中内存使用外部消息存储。在阅读本笔记之前，请先学习以下几篇笔记，因为这将建立在它们的基础之上：

- [LLMChain中的Memory](/modules/memory/adding_memory)
- [自定义代理](/modules/agents/how_to/custom_agent)
- [代理中的Memory](/modules/memory/agent_with_memory)

要将带有外部消息存储的内存添加到代理中，我们将执行以下步骤：

1. 我们将创建一个`RedisChatMessageHistory`来连接外部数据库以存储消息。
2. 我们将使用该聊天历史创建一个`LLMChain`作为内存。
3. 我们将使用该`LLMChain`创建自定义代理。

为了完成这个练习，我们将创建一个简单的自定义代理，该代理可以访问搜索工具并利用`ConversationBufferMemory`类。

```python
from langchain.agents import AgentExecutor, Tool, ZeroShotAgent
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_openai import OpenAI
```

```python
search = GoogleSearchAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
    )
]
```

注意`PromptTemplate`中`chat_history`变量的使用，该变量与`ConversationBufferMemory`中的动态键名匹配。

```python
prefix = """Have a conversation with a human, answering the following questions as best you can. You have access to the following tools:"""
suffix = """Begin!"

{chat_history}
Question: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
    tools,
    prefix=prefix,
    suffix=suffix,
    input_variables=["input", "chat_history", "agent_scratchpad"],
)
```

现在我们可以创建由数据库支持的`RedisChatMessageHistory`。

```python
message_history = RedisChatMessageHistory(
    url="redis://localhost:6379/0", ttl=600, session_id="my-session"
)

memory = ConversationBufferMemory(
    memory_key="chat_history", chat_memory=message_history
)
```

现在我们可以构建`LLMChain`，使用Memory对象，然后创建代理。

```python
llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
agent_chain = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True, memory=memory
)
```

```python
agent_chain.run(input="How many people live in Canada?")
```

'加拿大目前的人口为38,566,192，截至2022年12月31日星期六，基于最新的联合国数据的Worldometer解释。'

要测试这个代理的记忆，我们可以问一个后续问题，该问题依赖于前一个交流中的信息才能被正确回答。

```python
agent_chain.run(input="他们的国歌叫什么？")
```

'加拿大的国歌名为"O Canada"。'

我们可以看到，代理记住了前一个问题是关于加拿大，正确询问了Google搜索加拿大国歌的名称。

现在，让我们将其与没有内存的代理进行比较。

```python
prefix = """Have a conversation with a human, answering the following questions as best you can. You have access to the following tools:"""
suffix = """Begin!"

Question: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
    tools, prefix=prefix, suffix=suffix, input_variables=["input", "agent_scratchpad"]
)
llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
agent_without_memory = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True
)
```

```python
agent_without_memory.run("How many people live in Canada?")
```

'加拿大目前的人口为38,566,192，截至2022年12月31日星期六，基于最新的联合国数据的Worldometer解释。'

```python
agent_without_memory.run("他们的国歌叫什么？")
```

'国家的国歌名为国歌名。'

