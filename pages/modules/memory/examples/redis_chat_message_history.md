


 Redis Chat Message History
 [#](#redis-chat-message-history "Permalink to this headline")
===========================================================================================



 This notebook goes over how to use Redis to store chat message history.
 







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







