

摩托头存储器[#](#motorhead-memory "此标题的永久链接")
=======================================

[摩托头](https://github.com/getmetal/motorhead) 是一个用 Rust 实现的内存服务器。它会自动处理后台的增量摘要，并允许无状态应用程序。

设置[#](#setup "此标题的永久链接")
------------------------

请参阅[摩托头](https://github.com/getmetal/motorhead)的说明以在本地运行服务器。

```
from langchain.memory.motorhead_memory import MotorheadMemory
from langchain import OpenAI, LLMChain, PromptTemplate

template = """You are a chatbot having a conversation with a human.

{chat_history}
Human: {human_input}
AI:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], 
    template=template
)
memory = MotorheadMemory(
    session_id="testing-1",
    url="http://localhost:8080",
    memory_key="chat_history"
)

await memory.init();  # loads previous state from Motörhead 🤘

llm_chain = LLMChain(
    llm=OpenAI(), 
    prompt=prompt, 
    verbose=True, 
    memory=memory,
)

```

```
llm_chain.run("hi im bob")

```

```
> Entering new LLMChain chain...
Prompt after formatting:
You are a chatbot having a conversation with a human.

Human: hi im bob
AI:

> Finished chain.

```

```
' Hi Bob, nice to meet you! How are you doing today?'

```

```
llm_chain.run("whats my name?")

```

```
> Entering new LLMChain chain...
Prompt after formatting:
You are a chatbot having a conversation with a human.

Human: hi im bob
AI: Hi Bob, nice to meet you! How are you doing today?
Human: whats my name?
AI:

> Finished chain.

```

```
' You said your name is Bob. Is that correct?'

```

```
llm_chain.run("whats for dinner?")

```

```
> Entering new LLMChain chain...
Prompt after formatting:
You are a chatbot having a conversation with a human.

Human: hi im bob
AI: Hi Bob, nice to meet you! How are you doing today?
Human: whats my name?
AI: You said your name is Bob. Is that correct?
Human: whats for dinner?
AI:

> Finished chain.

```

```
"  I'm sorry, I'm not sure what you're asking. Could you please rephrase your question?"

```

