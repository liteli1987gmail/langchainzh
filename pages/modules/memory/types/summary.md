

对话摘要记忆[#](#conversationsummarymemory "此标题的永久链接")
================================================

现在让我们来看一下使用稍微复杂的记忆类型 - `对话摘要记忆`。这种记忆类型可以创建关于对话的摘要，有助于从对话中概括信息。

首先，让我们探索该类型记忆的基本功能。

```
from langchain.memory import ConversationSummaryMemory
from langchain.llms import OpenAI

```

```
memory = ConversationSummaryMemory(llm=OpenAI(temperature=0))
memory.save_context({"input": "hi"}, {"ouput": "whats up"})

```

```
memory.load_memory_variables({})

```

```
{'history': '\nThe human greets the AI, to which the AI responds.'}

```

我们还可以将历史记录作为消息列表获取（如果您正在与聊天模型一起使用，则此功能非常有用)。

```
memory = ConversationSummaryMemory(llm=OpenAI(temperature=0), return_messages=True)
memory.save_context({"input": "hi"}, {"ouput": "whats up"})

```

```
memory.load_memory_variables({})

```

```
{'history': [SystemMessage(content='\nThe human greets the AI, to which the AI responds.', additional_kwargs={})]}

```

我们还可以直接使用`predict_new_summary`方法。

```
messages = memory.chat_memory.messages
previous_summary = ""
memory.predict_new_summary(messages, previous_summary)

```

```
'\nThe human greets the AI, to which the AI responds.'

```

在链式操作中使用[#](#using-in-a-chain "此标题的永久链接")
-----------------------------------------

让我们通过一个示例来演示如何在链式操作中使用它，再次设置`verbose=True`以便查看提示。

```
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
llm = OpenAI(temperature=0)
conversation_with_summary = ConversationChain(
    llm=llm, 
    memory=ConversationSummaryMemory(llm=OpenAI()),
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
conversation_with_summary.predict(input="Tell me more about it!")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

The human greeted the AI and asked how it was doing. The AI replied that it was doing great and was currently helping a customer with a technical issue.
Human: Tell me more about it!
AI:

> Finished chain.

```

```
" Sure! The customer is having trouble with their computer not connecting to the internet. I'm helping them troubleshoot the issue and figure out what the problem is. So far, we've tried resetting the router and checking the network settings, but the issue still persists. We're currently looking into other possible solutions."

```

```
conversation_with_summary.predict(input="Very cool -- what is the scope of the project?")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

The human greeted the AI and asked how it was doing. The AI replied that it was doing great and was currently helping a customer with a technical issue where their computer was not connecting to the internet. The AI was troubleshooting the issue and had already tried resetting the router and checking the network settings, but the issue still persisted and they were looking into other possible solutions.
Human: Very cool -- what is the scope of the project?
AI:

> Finished chain.

```

```
" The scope of the project is to troubleshoot the customer's computer issue and find a solution that will allow them to connect to the internet. We are currently exploring different possibilities and have already tried resetting the router and checking the network settings, but the issue still persists."

```

