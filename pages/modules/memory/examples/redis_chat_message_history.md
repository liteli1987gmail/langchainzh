

Redis聊天消息历史记录[#](#redis-chat-message-history "Permalink to this headline")
==========================================================================

本教程介绍如何使用Redis存储聊天消息历史记录。

```
from langchain.memory import RedisChatMessageHistory

history = RedisChatMessageHistory("foo")

history.add_user_message("hi!")

history.add_ai_message("whats up?")

```

```
history.messages

```

```
[AIMessage(content='whats up?', additional_kwargs={}),
 HumanMessage(content='hi!', additional_kwargs={})]

```

