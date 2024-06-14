# 存储在LLMChain中的记忆

这本笔记本介绍如何在`LLMChain`中使用Memory类。

我们将添加[ConversationBufferMemory](https://api.python.langchain.com/en/latest/memory/langchain.memory.buffer.ConversationBufferMemory.html#langchain.memory.buffer.ConversationBufferMemory)类，尽管它可以是任何记忆类。

```python
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
```

最重要的步骤是正确设置提示。在下面的提示中，我们有两个输入键：一个用于实际输入，另一个用于Memory类中的输入。重要的是，确保在`PromptTemplate`和`ConversationBufferMemory`中的键匹配(`chat_history`)。

```python
template = """您是一个与人类对话的聊天机器人。

{chat_history}
人类: {human_input}
聊天机器人:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")
```

```python
llm = OpenAI()
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory,
)
```

```python
llm_chain.predict(human_input="嗨，朋友")
```

```
> 进入新的LLMChain链...
进入格式后的提示:
您是一个与人类对话的聊天机器人。

人类: 嗨，朋友
聊天机器人:

> 完成链。
```

'嗨，你好! 今天我能为你做点什么吗?'

```python
llm_chain.predict(human_input="还不错- 你好吗？")
```

```
> 进入新的LLMChain链...
进入格式后的提示:
您是一个与人类对话的聊天机器人。

人类: 嗨，朋友
AI: 嗨，你好! 今天我能为你做点什么吗?
人类: 还不错- 你好吗？
聊天机器人:

> 完成链。
```

'我很棒，谢谢你的关心！你自己怎么样？'

## 将Memory添加到基于聊天模型的`LLMChain`

上面的内容适用于完成式`LLM`，但是如果您使用聊天模型，可能会在使用结构化聊天消息时获得更好的表现。以下是一个例子。

```python
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
```

我们将使用[ChatPromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html?highlight=chatprompttemplate)类设置聊天提示。

[from_messages](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate.from_messages)方法从消息列表(例如`SystemMessage`、`HumanMessage`、`AIMessage`、`ChatMessage`等)或消息模板(如下面的[MessagesPlaceholder](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder))中创建`ChatPromptTemplate`。

下面的配置确保将Memory注入到聊天提示的中间，在`chat_history`键中，并将用户的输入以人类/用户消息的形式添加到聊天提示的末尾。

```python
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="您是一个与人类对话的聊天机器人。"
        ),  # 持续系统提示
        MessagesPlaceholder(
            variable_name="chat_history"
        ),  # 存储Memory的位置
        HumanMessagePromptTemplate.from_template(
            "{human_input}"
        ),  # 将人类输入注入的位置
    ]
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
```

```python
llm = ChatOpenAI()

chat_llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory,
)
```

```python
chat_llm_chain.predict(human_input="嗨，朋友")
```

```
> 进入新的LLMChain链...
进入格式后的提示:
System: 您是一个与人类对话的聊天机器人。
人类: 嗨，朋友

> 完成链。
```

'你好！我能帮你做什么呢，朋友？'

```python
chat_llm_chain.predict(human_input="还不错- 你好吗？")
```

```
> 进入新的LLMChain链...
进入格式后的提示:
System: 您是一个与人类对话的聊天机器人。
人类: 嗨，朋友
AI: 你好！我能帮你做什么呢，朋友？
人类: 还不错- 你好吗？

> 完成链。
```

'我是一个AI聊天机器人，所以我没有感情，但我在这里帮助和与您聊天！您想详细谈论什么或有什么问题需要帮助吗？'