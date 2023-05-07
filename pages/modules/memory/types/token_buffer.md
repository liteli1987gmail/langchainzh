

ConversationTokenBufferMemory[#](#conversationtokenbuffermemory "Permalink to this headline")
=============================================================================================

`ConversationTokenBufferMemory` 会在内存中保留最近的对话内容，并使用token长度而不是对话数量来决定何时刷新对话。

首先让我们了解如何使用这些工具

```
from langchain.memory import ConversationTokenBufferMemory
from langchain.llms import OpenAI
llm = OpenAI()

```

```
memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=10)
memory.save_context({"input": "hi"}, {"ouput": "whats up"})
memory.save_context({"input": "not much you"}, {"ouput": "not much"})

```

```
memory.load_memory_variables({})

```

```
{'history': 'Human: not much you\nAI: not much'}

```

我们也可以将历史记录作为消息列表获取（如果您正在使用聊天模型，则这很有用）。

```
memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=10, return_messages=True)
memory.save_context({"input": "hi"}, {"ouput": "whats up"})
memory.save_context({"input": "not much you"}, {"ouput": "not much"})

```

在链式使用中[#](#using-in-a-chain "Permalink to this headline")
---------------------------------------------------------

让我们通过一个例子来了解如何使用，再次设置`verbose=True`，以便我们可以看到提示。

```
from langchain.chains import ConversationChain
conversation_with_summary = ConversationChain(
    llm=llm, 
    # We set a very low max_token_limit for the purposes of testing.
    memory=ConversationTokenBufferMemory(llm=OpenAI(), max_token_limit=60),
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
" Hi there! I'm doing great, just enjoying the day. How about you?"

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
AI: Hi there! I'm doing great, just enjoying the day. How about you?
Human: Just working on writing some documentation!
AI:

> Finished chain.

```

```
' Sounds like a productive day! What kind of documentation are you writing?'

```

```
conversation_with_summary.predict(input="For LangChain! Have you heard of it?")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: Hi, what's up?
AI: Hi there! I'm doing great, just enjoying the day. How about you?
Human: Just working on writing some documentation!
AI: Sounds like a productive day! What kind of documentation are you writing?
Human: For LangChain! Have you heard of it?
AI:

> Finished chain.

```

```
" Yes, I have heard of LangChain! It is a decentralized language-learning platform that connects native speakers and learners in real time. Is that the documentation you're writing about?"

```

```
# We can see here that the buffer is updated
conversation_with_summary.predict(input="Haha nope, although a lot of people confuse it for that")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: For LangChain! Have you heard of it?
AI: Yes, I have heard of LangChain! It is a decentralized language-learning platform that connects native speakers and learners in real time. Is that the documentation you're writing about?
Human: Haha nope, although a lot of people confuse it for that
AI:

> Finished chain.

```

```
" Oh, I see. Is there another language learning platform you're referring to?"

```

