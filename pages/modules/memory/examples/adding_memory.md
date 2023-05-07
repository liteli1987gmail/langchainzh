

如何向LLMChain添加内存[#](#how-to-add-memory-to-an-llmchain "永久链接到此标题")
================================================================

本笔记本将介绍如何使用Memory类与LLMChain。在本次演示中，我们将添加`ConversationBufferMemory`类，但这可以是任何内存类。

```
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate

```

最重要的步骤是正确设置提示。在下面的提示中，我们有两个输入键：一个用于实际输入，另一个用于来自Memory类的输入。重要的是，确保PromptTemplate和ConversationBufferMemory中的键匹配(`chat_history`)。

```
template = """You are a chatbot having a conversation with a human.

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], 
    template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

```

```
llm_chain = LLMChain(
    llm=OpenAI(), 
    prompt=prompt, 
    verbose=True, 
    memory=memory,
)

```

```
llm_chain.predict(human_input="Hi there my friend")

```

```
> Entering new LLMChain chain...
Prompt after formatting:
You are a chatbot having a conversation with a human.

Human: Hi there my friend
Chatbot:

> Finished LLMChain chain.

```

```
' Hi there, how are you doing today?'

```

```
llm_chain.predict(human_input="Not too bad - how are you?")

```

```
> Entering new LLMChain chain...
Prompt after formatting:
You are a chatbot having a conversation with a human.

Human: Hi there my friend
AI: Hi there, how are you doing today?
Human: Not to bad - how are you?
Chatbot:

> Finished LLMChain chain.

```

```
" I'm doing great, thank you for asking!"

```

