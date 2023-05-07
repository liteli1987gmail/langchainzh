

对话摘要缓存内存[#](#conversationsummarybuffermemory "标题的永久链接")
=======================================================

`ConversationSummaryBufferMemory`结合了前两个想法。它将最近的交互记录缓存在内存中，但不仅仅是完全清除旧的交互，而是将它们编译成一份摘要并同时使用。不过，与之前的实现不同，它使用令牌长度而不是交互数量来确定何时清除交互。

首先让我们了解如何使用这些工具

```
from langchain.memory import ConversationSummaryBufferMemory
from langchain.llms import OpenAI
llm = OpenAI()

```

```
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=10)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})

```

```
memory.load_memory_variables({})

```

```
{'history': 'System: \nThe human says "hi", and the AI responds with "whats up".\nHuman: not much you\nAI: not much'}

```

我们还可以将历史记录作为消息列表获取（如果您正在使用聊天模型，则此功能很有用）。

```
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=10, return_messages=True)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})

```

我们还可以直接利用`predict_new_summary`方法。

```
messages = memory.chat_memory.messages
previous_summary = ""
memory.predict_new_summary(messages, previous_summary)

```

```
'\nThe human and AI state that they are not doing much.'

```

在链式中使用[#](#using-in-a-chain "标题的永久链接")
--------------------------------------

让我们通过一个例子来了解，再次设置`verbose=True`，以便我们可以看到提示。

```
from langchain.chains import ConversationChain
conversation_with_summary = ConversationChain(
    llm=llm, 
    # We set a very low max_token_limit for the purposes of testing.
    memory=ConversationSummaryBufferMemory(llm=OpenAI(), max_token_limit=40),
    verbose=True
)
conversation_with_summary.predict(input="Hi, what's up?")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

Human: Hi, what's up?
AI:

> Finished chain.

```

```
" Hi there! I'm doing great. I'm learning about the latest advances in artificial intelligence. What about you?"

```

```
conversation_with_summary.predict(input="Just working on writing some documentation!")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: Hi, what's up?
AI: Hi there! I'm doing great. I'm spending some time learning about the latest developments in AI technology. How about you?
Human: Just working on writing some documentation!
AI:

> Finished chain.

```

```
' That sounds like a great use of your time. Do you have experience with writing documentation?'

```

```
# We can see here that there is a summary of the conversation and then some previous interactions
conversation_with_summary.predict(input="For LangChain! Have you heard of it?")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
System: 
The human asked the AI what it was up to and the AI responded that it was learning about the latest developments in AI technology.
Human: Just working on writing some documentation!
AI: That sounds like a great use of your time. Do you have experience with writing documentation?
Human: For LangChain! Have you heard of it?
AI:

> Finished chain.

```

```
" No, I haven't heard of LangChain. Can you tell me more about it?"

```

```
# We can see here that the summary and the buffer are updated
conversation_with_summary.predict(input="Haha nope, although a lot of people confuse it for that")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
System: 
The human asked the AI what it was up to and the AI responded that it was learning about the latest developments in AI technology. The human then mentioned they were writing documentation, to which the AI responded that it sounded like a great use of their time and asked if they had experience with writing documentation.
Human: For LangChain! Have you heard of it?
AI: No, I haven't heard of LangChain. Can you tell me more about it?
Human: Haha nope, although a lot of people confuse it for that
AI:

> Finished chain.

```

```
' Oh, okay. What is LangChain?'

```

