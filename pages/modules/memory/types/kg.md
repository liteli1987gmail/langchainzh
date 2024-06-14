# 对话知识图谱

这种类型的记忆使用知识图谱来重现记忆。


## 使用LLM记忆


```python
from langchain.memory import ConversationKGMemory
from langchain_openai import OpenAI
```


```python
llm = OpenAI(temperature=0)
memory = ConversationKGMemory(llm=llm)
memory.save_context({"input": "对Sam打招呼"}, {"output": "Sam是谁"})
memory.save_context({"input": "Sam是朋友"}, {"output": "好的"})
```


```python
memory.load_memory_variables({"input": "Sam是谁"})
```




    {'history': '关于Sam: Sam是朋友。'}



我们也可以将历史记录作为消息列表获取（如果您与聊天模型一起使用，则此功能很有用）。


```python
memory = ConversationKGMemory(llm=llm, return_messages=True)
memory.save_context({"input": "对Sam打招呼"}, {"output": "Sam是谁"})
memory.save_context({"input": "Sam是朋友"}, {"output": "好的"})
```


```python
memory.load_memory_variables({"input": "Sam是谁"})
```




    {'history': [SystemMessage(content='关于Sam: Sam是朋友。', additional_kwargs={})]}



我们还可以更模块化地从新消息中获取当前实体（将使用先前的消息作为上下文）。


```python
memory.get_current_entities("Sam最喜欢的颜色是什么？")
```




    ['Sam']



我们还可以更模块化地从新消息中获取知识三元组（将使用先前的消息作为上下文）。


```python
memory.get_knowledge_triplets("她最喜欢的颜色是红色")
```




    [KnowledgeTriple(subject='Sam', predicate='最喜欢的颜色', object_='红色')]



## 在链条中使用

现在让我们在链条中使用它！


```python
llm = OpenAI(temperature=0)
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate

template = """下面是一个友好的人工智能和人类之间的对话。人工智能健谈并提供了大量来自其上下文的详细信息。
如果人工智能对一个问题不知道答案，它会真实地说它不知道。人工智能仅使用包含在“相关信息”部分中的信息，不会产生幻觉。

相关信息：

{history}

对话：
人类：{input}
人工智能："""
prompt = PromptTemplate(input_variables=["history", "input"], template=template)
conversation_with_kg = ConversationChain(
    llm=llm, verbose=True, prompt=prompt, memory=ConversationKGMemory(llm=llm)
)
```


```python
conversation_with_kg.predict(input="嗨，最近怎么样？")
```

    
    
    [1m> 进入新的ConversationChain链条...[0m
    格式化后的提示：
    [32;1m[1;3m下面是一个友好的人工智能和人类之间的对话。人工智能健谈并提供了大量来自其上下文的详细信息。
    如果人工智能对一个问题不知道答案，它会真实地说它不知道。人工智能仅使用包含在“相关信息”部分中的信息，不会产生幻觉。
    
    相关信息：
    
    
    
    对话：
    人类：嗨，最近怎么样？
    人工智能：[0m
    
    [1m> 完成链条。[0m
    




    " 嗨！我过得很好。我正在学习我们周围的世界。我正在了解不同的文化，语言和风俗习惯。真是很有意思！你呢？"




```python
conversation_with_kg.predict(
    input="我叫James，我在帮助Will。他是一名工程师。"
)
```

    
    
    [1m> 进入新的ConversationChain链条...[0m
    格式化后的提示：
    [32;1m[1;3m下面是一个友好的人工智能和人类之间的对话。人工智能健谈并提供了大量来自其上下文的详细信息。
    如果人工智能对一个问题不知道答案，它会真实地说它不知道。人工智能仅使用包含在“相关信息”部分中的信息，不会产生幻觉。
    
    相关信息：
    
    
    
    对话：
    人类：我叫James，我在帮助Will。他是一名工程师。
    人工智能：[0m
    
    [1m> 完成链条。[0m
    




    " 嗨James，很高兴见到你。我是一个AI，我知道你正在帮助工程师Will。他从事什么类型的工程工作？"




```python
conversation_with_kg.predict(input="你知道关于Will的什么信息？")
```

    
    
    [1m> 进入新的ConversationChain链条...[0m
    格式化后的提示：
    [32;1m[1;3m下面是一个友好的人工智能和人类之间的对话。人工智能健谈并提供了大量来自其上下文的详细信息。
    如果人工智能对一个问题不知道答案，它会真实地说它不知道。人工智能仅使用包含在“相关信息”部分中的信息，不会产生幻觉。
    
    相关信息：
    
    关于Will: Will是一名工程师。
    
    对话：
    人类：你知道关于Will的什么信息？
    人工智能：[0m
    
    [1m> 完成链条。[0m
    




    ' Will是一名工程师。'




