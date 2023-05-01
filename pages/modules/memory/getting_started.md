

开始
=====================================================================


这个笔记本详细介绍了 LangChain 对记忆的看法。

内存涉及在用户与语言模型的交互过程中始终保持状态的概念。用户与语言模型的交互被捕获在聊天消息的概念中，所以这归结为从一系列聊天消息中摄取、捕获、转换和提取知识。有许多不同的方法可以实现这一点，每种方法都作为自己的内存类型存在。

一般来说，对于每种类型的记忆，有两种方法来理解使用记忆。这些是从消息序列中提取信息的独立函数，还有一种方法可以在链中使用这种类型的内存。

内存可以返回多条信息(例如，最近的 N 条消息和所有以前消息的摘要)。返回的信息可以是字符串，也可以是消息列表。

在这个笔记本中，我们将介绍最简单的内存形式: “缓冲”内存，它仅仅涉及保持所有以前的消息的缓冲区。我们将在这里展示如何使用模块化实用函数，然后展示如何在链中使用它(既返回字符串，也返回消息列表)。


 




聊天记录
---------------------------------------------------------------------------



支撑大多数(如果不是全部)内存模块的核心实用工具类之一是 ChatMessageHistory 类。这是一个超轻量级的包装器，它提供了一些方便的方法来保存人类消息、人工智能消息，然后获取它们。

如果要管理链外部的内存，可能需要直接使用此类。
 



 







```
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()

history.add_user_message("hi!")

history.add_ai_message("whats up?")

```










```
history.messages

```








```
[HumanMessage(content='hi!', additional_kwargs={}),
 AIMessage(content='whats up?', additional_kwargs={})]

```








缓冲记忆
---------------------------------------------------------------------------------------

现在我们展示如何在链中使用这个简单的概念。我们首先展示 ConversationBufferMemory，它只是 ChatMessageHistory 的一个包装器，用于提取变量中的消息。

我们可以首先提取它作为一个字符串。
 







```
from langchain.memory import ConversationBufferMemory

```










```
memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("hi!")
memory.chat_memory.add_ai_message("whats up?")

```










```
memory.load_memory_variables({})

```








```
{'history': 'Human: hi!\nAI: whats up?'}

```






我们还可以获取作为消息列表的历史记录
 







```
memory = ConversationBufferMemory(return_messages=True)
memory.chat_memory.add_user_message("hi!")
memory.chat_memory.add_ai_message("whats up?")

```










```
memory.load_memory_variables({})

```








```
{'history': [HumanMessage(content='hi!', additional_kwargs={}),
  AIMessage(content='whats up?', additional_kwargs={})]}

```








连锁使用
-----------------------------------------------------------------------



最后，让我们看看如何在链中使用它(设置 verose = True，这样我们就可以看到提示符)。
 







```
from langchain.llms import OpenAI
from langchain.chains import ConversationChain


llm = OpenAI(temperature=0)
conversation = ConversationChain(
    llm=llm, 
    verbose=True, 
    memory=ConversationBufferMemory()
)

```










```
conversation.predict(input="Hi there!")

```








```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

Human: Hi there!
AI:

> Finished chain.

```






```
" Hi there! It's nice to meet you. How can I help you today?"

```










```
conversation.predict(input="I'm doing well! Just having a conversation with an AI.")

```








```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: Hi there!
AI: Hi there! It's nice to meet you. How can I help you today?
Human: I'm doing well! Just having a conversation with an AI.
AI:

> Finished chain.

```






```
" That's great! It's always nice to have a conversation with someone new. What would you like to talk about?"

```










```
conversation.predict(input="Tell me about yourself.")

```








```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: Hi there!
AI: Hi there! It's nice to meet you. How can I help you today?
Human: I'm doing well! Just having a conversation with an AI.
AI: That's great! It's always nice to have a conversation with someone new. What would you like to talk about?
Human: Tell me about yourself.
AI:

> Finished chain.

```






```
" Sure! I'm an AI created to help people with their everyday tasks. I'm programmed to understand natural language and provide helpful information. I'm also constantly learning and updating my knowledge base so I can provide more accurate and helpful answers."

```








保存邮件历史记录
-----------------------------------------------------------------------------------



您可能经常需要保存消息，然后加载它们再次使用。通过首先将消息转换为普通的 python 字典，保存它们(作为 json 或其他形式) ，然后加载它们，可以很容易地做到这一点。这里有一个这样做的例子。
 







```
import json

from langchain.memory import ChatMessageHistory
from langchain.schema import messages_from_dict, messages_to_dict

history = ChatMessageHistory()

history.add_user_message("hi!")

history.add_ai_message("whats up?")

```










```
dicts = messages_to_dict(history.messages)

```










```
dicts

```








```
[{'type': 'human', 'data': {'content': 'hi!', 'additional_kwargs': {}}},
 {'type': 'ai', 'data': {'content': 'whats up?', 'additional_kwargs': {}}}]

```










```
new_messages = messages_from_dict(dicts)

```










```
new_messages

```








```
[HumanMessage(content='hi!', additional_kwargs={}),
 AIMessage(content='whats up?', additional_kwargs={})]

```






这就是开始！有很多不同类型的内存，看看我们的例子来看看他们。
 





