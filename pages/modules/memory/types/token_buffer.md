# 会话令牌缓冲区

`ConversationTokenBufferMemory` 将最近的交互保留在内存中，并使用令牌长度而不是交互次数来确定何时刷新交互。

首先让我们了解如何使用这些实用工具。

## 使用LLM和内存


```python
from langchain.memory import ConversationTokenBufferMemory
from langchain_openai import OpenAI

llm = OpenAI()
```


```python
memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=10)
memory.save_context({"input": "你好"}, {"output": "最近怎么样"})
memory.save_context({"input": "没什么，你呢"}, {"output": "一般般"})
```


```python
memory.load_memory_variables({})
```




    {'history': '人类: 没什么，你呢\nAI: 一般般'}



我们还可以获取消息列表的历史记录（如果您正在与聊天模型一起使用，这非常有用）。

```python
memory = ConversationTokenBufferMemory(
    llm=llm, max_token_limit=10, return_messages=True
)
memory.save_context({"input": "你好"}, {"output": "最近怎么样"})
memory.save_context({"input": "没什么，你呢"}, {"output": "一般般"})
```

## 在链中使用
让我们通过一个示例来说明，再次将 `verbose=True` 进行设置，以便我们可以看到提示。

```python
from langchain.chains import ConversationChain

conversation_with_summary = ConversationChain(
    llm=llm,
    # 为了测试目的，我们设置了一个非常低的 max_token_limit。
    memory=ConversationTokenBufferMemory(llm=OpenAI(), max_token_limit=60),
    verbose=True,
)
conversation_with_summary.predict(input="你好，近来怎么样？")
```

    
    
    [1m> 进入新的 ConversationChain 链...[0m
    格式化后的提示：
    [32;1m[1;3m下面是一个友好对话的片段，其中涉及人工智能和人类的对话。人工智能非常健谈，从其上下文中提供了大量具体的细节。如果人工智能无法回答问题，它会如实回答自己不知道。
    
    当前对话：
    
    人类: 你好，近来怎么样？
    AI:[0m
    
    [1m> 完成链。[0m
    




    " 你好！我过得很好，正在享受这一天。你呢？"




```python
conversation_with_summary.predict(input="我正在写一些文档！")
```

    
    
    [1m> 进入新的 ConversationChain 链...[0m
    格式化后的提示：
    [32;1m[1;3m下面是一个友好对话的片段，其中涉及人工智能和人类的对话。人工智能非常健谈，从其上下文中提供了大量具体的细节。如果人工智能无法回答问题，它会如实回答自己不知道。
    
    当前对话：
    人类: 你好，近来怎么样？
    AI:  你好！我过得很好，正在享受这一天。你呢？
    人类: 我正在写一些文档！
    AI:[0m
    
    [1m> 完成链。[0m
    




    " 听起来是一个充实的一天！你在写哪方面的文档呢？"




```python
conversation_with_summary.predict(input="是关于LangChain的！你听说过吗？")
```

    
    
    [1m> 进入新的 ConversationChain 链...[0m
    格式化后的提示：
    [32;1m[1;3m下面是一个友好对话的片段，其中涉及人工智能和人类的对话。人工智能非常健谈，从其上下文中提供了大量具体的细节。如果人工智能无法回答问题，它会如实回答自己不知道。
    
    当前对话：
    人类: 你好，近来怎么样？
    AI:  你好！我过得很好，正在享受这一天。你呢？
    人类: 我正在写一些文档！
    AI:  听起来是一个充实的一天！你在写哪方面的文档呢？
    人类: 是关于LangChain的！你听说过吗？
    AI:[0m
    
    [1m> 完成链。[0m
    




    " 是的，我听说过LangChain！它是一个分布式的语言学习平台，可以实时连接母语人士和学习者。你写的就是这个文档吗？"




```python
# 我们可以看到缓冲区已经更新了
conversation_with_summary.predict(
    input="哈哈，不是，虽然很多人把它弄混了"
)
```

    
    
    [1m> 进入新的 ConversationChain 链...[0m
    格式化后的提示：
    [32;1m[1;3m下面是一个友好对话的片段，其中涉及人工智能和人类的对话。人工智能非常健谈，从其上下文中提供了大量具体的细节。如果人工智能无法回答问题，它会如实回答自己不知道。
    
    当前对话：
    人类: 是关于LangChain的！你听说过吗？
    AI:  是的，我听说过LangChain！它是一个分布式的语言学习平台，可以实时连接母语人士和学习者。你写的就是这个文档吗？
    人类: 哈哈，不是，虽然很多人把它弄混了
    AI:[0m
    
    [1m> 完成链。[0m
    




    " 哦，我明白了。你是在指其他的语言学习平台吗？"






