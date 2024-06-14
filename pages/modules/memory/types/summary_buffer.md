# 交流摘要缓冲区

`ConversationSummaryBufferMemory` 将这两种思想结合在一起。它在内存中保留最近交互的缓冲区，但不仅仅是完全刷新旧的交互，而是将它们编译成摘要并同时使用。
它使用 token 长度而不是交互次数来确定何时刷新交互。

让我们首先来看看如何使用这些实用工具。

## 使用内存和LLM


```python
from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import OpenAI

llm = OpenAI()
```


```python
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=10)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})
```


```python
memory.load_memory_variables({})
```




    {'history': 'System: \nThe human says "hi", and the AI responds with "whats up".\nHuman: not much you\nAI: not much'}



我们还可以将历史记录作为消息列表获取（如果您将其与聊天模型一起使用，则这将非常有用）。


```python
memory = ConversationSummaryBufferMemory(
    llm=llm, max_token_limit=10, return_messages=True
)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})
```

我们还可以直接利用 `predict_new_summary` 方法。


```python
messages = memory.chat_memory.messages
previous_summary = ""
memory.predict_new_summary(messages, previous_summary)
```




    '\nThe human and AI state that they are not doing much.'



## 在链中使用
让我们通过一个例子走一遍，再次设置 `verbose=True` 以便查看提示。


```python
from langchain.chains import ConversationChain

conversation_with_summary = ConversationChain(
    llm=llm,
    # 我们为了测试目的设置了一个非常低的 max_token_limit。
    memory=ConversationSummaryBufferMemory(llm=OpenAI(), max_token_limit=40),
    verbose=True,
)
conversation_with_summary.predict(input="Hi, what's up?")
```

    
    
    [1m> 进入新 ConversationChain 链...[0m
    格式化后的提示:
    [32;1m[1;3m以下是人类和AI之间友好交流的对话。AI 健谈且提供了大量特定上下文的细节。如果AI不知道问题的答案，它会真诚地说不知道。
    
    当前对话:
    
    Human: Hi, what's up?
    AI:[0m
    
    [1m> 链结束。[0m
    




    " 嗨！我过得很好。我正在了解人工智能的最新进展。你呢？"




```python
conversation_with_summary.predict(input="Just working on writing some documentation!")
```

    
    
    [1m> 进入新 ConversationChain 链...[0m
    格式化后的提示:
    [32;1m[1;3m以下是人类和AI之间友好交流的对话。AI 健谈且提供了大量特定上下文的细节。如果AI不知道问题的答案，它会真诚地说不知道。
    
    当前对话:
    Human: Hi, what's up?
    AI:  嗨！我过得很好。我正在了解人工智能技术的最新发展。你呢？
    Human: Just working on writing some documentation!
    AI:[0m
    
    [1m> 链结束。[0m
    




    ' 听起来是很好的时间安排。你写文档的经验怎么样？'




```python
# 在这里可以看到对话摘要以及之前的互动
conversation_with_summary.predict(input="For LangChain! Have you heard of it?")
```

    
    
    [1m> 进入新 ConversationChain 链...[0m
    格式化后的提示:
    [32;1m[1;3m以下是人类和AI之间友好交流的对话。AI 健谈且提供了大量特定上下文的细节。如果AI不知道问题的答案，它会真诚地说不知道。
    
    当前对话:
    System: 
	  人类问AI正在做什么，AI回答正在了解人工智能技术的最新发展。
    Human: Just working on writing some documentation!
    AI: 听起来是很好的时间安排。你写文档的经验怎么样？
    Human: For LangChain! Have you heard of it?
    AI:[0m
    
    [1m> 链结束。[0m
    




    " 没有，我没有听说过 LangChain。你能告诉我更多吗？"




```python
# 在这里可以看到对话摘要和缓冲区被更新
conversation_with_summary.predict(
    input="Haha nope, although a lot of people confuse it for that"
)
```

    
    
    [1m> 进入新 ConversationChain 链...[0m
    格式化后的提示:
    [32;1m[1;3m以下是人类和AI之间友好交流的对话。AI 健谈且提供了大量特定上下文的细节。如果AI不知道问题的答案，它会真诚地说不知道。
    
    当前对话:
    System: 
	  人类问AI正在做什么，AI回答正在了解人工智能技术的最新发展。
	  人类提到正在编写文档，AI回应似乎是一个很好的时间安排并询问对文档编写是否有经验。
    Human: For LangChain! Have you heard of it?
    AI: 没有，我没有听说过 LangChain。你能告诉我更多吗？
    Human: Haha nope, although a lot of people confuse it for that
    AI:[0m
    
    [1m> 链结束。[0m
    




    ' 哦，好吧。LangChain 是什么？'




```python

```