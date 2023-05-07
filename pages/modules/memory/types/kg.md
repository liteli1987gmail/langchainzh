

对话知识图谱记忆[#](#conversation-knowledge-graph-memory "本标题的永久链接")
============================================================

这种类型的记忆使用知识图谱来重建记忆。

让我们先来了解如何使用这些工具。

```
from langchain.memory import ConversationKGMemory
from langchain.llms import OpenAI

```

```
llm = OpenAI(temperature=0)
memory = ConversationKGMemory(llm=llm)
memory.save_context({"input": "say hi to sam"}, {"ouput": "who is sam"})
memory.save_context({"input": "sam is a friend"}, {"ouput": "okay"})

```

```
memory.load_memory_variables({"input": 'who is sam'})

```

```
{'history': 'On Sam: Sam is friend.'}

```

我们还可以将历史记录作为消息列表获取（如果您正在使用聊天模型，则这非常有用）。

```
memory = ConversationKGMemory(llm=llm, return_messages=True)
memory.save_context({"input": "say hi to sam"}, {"ouput": "who is sam"})
memory.save_context({"input": "sam is a friend"}, {"ouput": "okay"})

```

```
memory.load_memory_variables({"input": 'who is sam'})

```

```
{'history': [SystemMessage(content='On Sam: Sam is friend.', additional_kwargs={})]}

```

我们还可以更模块化地从新消息中获取当前实体（将先前的消息用作上下文）。

```
memory.get_current_entities("what's Sams favorite color?")

```

```
['Sam']

```

我们还可以更模块化地从新消息中获取知识三元组（将先前的消息用作上下文）。

```
memory.get_knowledge_triplets("her favorite color is red")

```

```
[KnowledgeTriple(subject='Sam', predicate='favorite color', object_='red')]

```

在链式使用中[#](#using-in-a-chain "本标题的永久链接")
---------------------------------------

现在让我们在链式使用中使用它！

```
llm = OpenAI(temperature=0)
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationChain

template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. 
If the AI does not know the answer to a question, it truthfully says it does not know. The AI ONLY uses information contained in the "Relevant Information" section and does not hallucinate.

Relevant Information:

{history}

Conversation:
Human: {input}
AI:"""
prompt = PromptTemplate(
    input_variables=["history", "input"], template=template
)
conversation_with_kg = ConversationChain(
    llm=llm, 
    verbose=True, 
    prompt=prompt,
    memory=ConversationKGMemory(llm=llm)
)

```

```
conversation_with_kg.predict(input="Hi, what's up?")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. 
If the AI does not know the answer to a question, it truthfully says it does not know. The AI ONLY uses information contained in the "Relevant Information" section and does not hallucinate.

Relevant Information:

Conversation:
Human: Hi, what's up?
AI:

> Finished chain.

```

```
" Hi there! I'm doing great. I'm currently in the process of learning about the world around me. I'm learning about different cultures, languages, and customs. It's really fascinating! How about you?"

```

```
conversation_with_kg.predict(input="My name is James and I'm helping Will. He's an engineer.")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. 
If the AI does not know the answer to a question, it truthfully says it does not know. The AI ONLY uses information contained in the "Relevant Information" section and does not hallucinate.

Relevant Information:

Conversation:
Human: My name is James and I'm helping Will. He's an engineer.
AI:

> Finished chain.

```

```
" Hi James, it's nice to meet you. I'm an AI and I understand you're helping Will, the engineer. What kind of engineering does he do?"

```

```
conversation_with_kg.predict(input="What do you know about Will?")

```

```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. 
If the AI does not know the answer to a question, it truthfully says it does not know. The AI ONLY uses information contained in the "Relevant Information" section and does not hallucinate.

Relevant Information:

On Will: Will is an engineer.

Conversation:
Human: What do you know about Will?
AI:

> Finished chain.

```

```
' Will is an engineer.'

```

