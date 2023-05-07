

对话缓存窗口内存[#](#conversationbufferwindowmemory "此标题的永久链接")
=======================================================

`ConversationBufferWindowMemory`保留了对话随时间推移的交互列表。它仅使用最后K个交互。这可以用于保持最近交互的滑动窗口，以便缓冲区不会过大。

让我们先探索这种类型内存的基本功能。

```
from langchain.memory import ConversationBufferWindowMemory

```

```
memory = ConversationBufferWindowMemory( k=1)
memory.save_context({"input": "hi"}, {"ouput": "whats up"})
memory.save_context({"input": "not much you"}, {"ouput": "not much"})

```

```
memory.load_memory_variables({})

```

```
{'history': 'Human: not much you\nAI: not much'}

```

我们也可以将历史记录作为消息列表获取（如果您正在使用聊天模型，则这非常有用）。

```
memory = ConversationBufferWindowMemory( k=1, return_messages=True)
memory.save_context({"input": "hi"}, {"ouput": "whats up"})
memory.save_context({"input": "not much you"}, {"ouput": "not much"})

```

```
memory.load_memory_variables({})

```

```
{'history': [HumanMessage(content='not much you', additional_kwargs={}),
  AIMessage(content='not much', additional_kwargs={})]}

```

在链中使用[#](#using-in-a-chain "此标题的永久链接")
--------------------------------------

让我们通过一个例子来演示，再次设置`verbose=True`，以便我们可以看到提示。

```
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
conversation_with_summary = ConversationChain(
    llm=OpenAI(temperature=0), 
    # We set a low k=2, to only keep the last 2 interactions in memory
    memory=ConversationBufferWindowMemory(k=2), 
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
" Hi there! I'm doing great. I'm currently helping a customer with a technical issue. How about you?"

```

```
conversation_with_summary.predict(input="What's their issues?")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: Hi, what's up?
AI: Hi there! I'm doing great. I'm currently helping a customer with a technical issue. How about you?
Human: What's their issues?
AI:

> Finished chain.

```

```
" The customer is having trouble connecting to their Wi-Fi network. I'm helping them troubleshoot the issue and get them connected."

```

```
conversation_with_summary.predict(input="Is it going well?")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: Hi, what's up?
AI: Hi there! I'm doing great. I'm currently helping a customer with a technical issue. How about you?
Human: What's their issues?
AI: The customer is having trouble connecting to their Wi-Fi network. I'm helping them troubleshoot the issue and get them connected.
Human: Is it going well?
AI:

> Finished chain.

```

```
" Yes, it's going well so far. We've already identified the problem and are now working on a solution."

```

```
# Notice here that the first interaction does not appear.
conversation_with_summary.predict(input="What's the solution?")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: What's their issues?
AI: The customer is having trouble connecting to their Wi-Fi network. I'm helping them troubleshoot the issue and get them connected.
Human: Is it going well?
AI: Yes, it's going well so far. We've already identified the problem and are now working on a solution.
Human: What's the solution?
AI:

> Finished chain.

```

```
" The solution is to reset the router and reconfigure the settings. We're currently in the process of doing that."

```

