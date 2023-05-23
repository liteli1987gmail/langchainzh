

Postgres聊天消息历史记录[#](#postgres-chat-message-history "此标题的永久链接")
==============================================================

本教程介绍如何使用Postgres存储聊天消息历史记录。

```
from langchain.memory import PostgresChatMessageHistory

history = PostgresChatMessageHistory(connection_string="postgresql://postgres:mypassword@localhost/chat_history", session_id="foo")

history.add_user_message("hi!")

history.add_ai_message("whats up?")

```

```
history.messages

```

