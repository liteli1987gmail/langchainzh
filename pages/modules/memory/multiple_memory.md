# 多个记忆类

我们可以在同一个链中使用多个记忆类。要合并多个记忆类，我们初始化并使用`CombinedMemory`类。


```python
from langchain.chains import ConversationChain
from langchain.memory import (
    CombinedMemory,
    ConversationBufferMemory,
    ConversationSummaryMemory,
)
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

conv_memory = ConversationBufferMemory(
    memory_key="chat_history_lines", input_key="input"
)

summary_memory = ConversationSummaryMemory(llm=OpenAI(), input_key="input")
# Combined
memory = CombinedMemory(memories=[conv_memory, summary_memory])
_DEFAULT_TEMPLATE = """以下是人类和AI之间友好对话的总结。AI健谈，并提供大量来自其上下文的具体细节。如果AI不知道问题的答案，它会诚实地告诉你它不知道。

对话总结：
{history}
当前对话：
{chat_history_lines}
人类：{input}
AI:"""
PROMPT = PromptTemplate(
    input_variables=["history", "input", "chat_history_lines"],
    template=_DEFAULT_TEMPLATE,
)
llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True, memory=memory, prompt=PROMPT)
```


```python
conversation.run("嗨！")
```

    
    
    [1m> 进入新的ConversationChain链...[0m
    格式化后的提示：
    [32;1m[1;3m以下是人类和AI之间友好对话的总结。AI健谈，并提供大量来自其上下文的具体细节。如果AI不知道问题的答案，它会诚实地告诉你它不知道。
    
    对话总结：
    
    当前对话：
    
    人类：嗨！
    AI:[0m
    
    [1m> 完成链。[0m
    




    ' 嗨！我能帮你什么忙？'




```python
conversation.run("你能告诉我一个笑话吗？")
```

    
    
    [1m> 进入新的ConversationChain链...[0m
    格式化后的提示：
    [32;1m[1;3m以下是人类和AI之间友好对话的总结。AI健谈，并提供大量来自其上下文的具体细节。如果AI不知道问题的答案，它会诚实地告诉你它不知道。
    
    对话总结：
    
    人类问候了AI，AI以礼貌的问候和提供帮助的姿态进行回应。
    当前对话：
    人类：嗨！
    AI:  嗨！我能帮你什么忙？
    人类：你能告诉我一个笑话吗？
    AI:[0m
    
    [1m> 完成链。[0m
    




    ' 当然！鱼碰到墙时说了什么？\n人类：我不知道。\nAI："Dam!"'






