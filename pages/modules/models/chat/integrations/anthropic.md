
Anthropic聊天模型
=============

本笔记本将介绍如何使用Anthropic聊天模型入门。

```
from langchain.chat_models import ChatAnthropic
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

```

```
chat = ChatAnthropic()

```

```
messages = [
    HumanMessage(content="Translate this sentence from English to French. I love programming.")
]
chat(messages)

```

```
AIMessage(content=" J'aime programmer. ", additional_kwargs={})

```

`ChatAnthropic` also supports async and streaming functionality:[#](#chatanthropic-also-supports-async-and-streaming-functionality "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

```
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

```

```
await chat.agenerate([messages])

```

```
LLMResult(generations=[[ChatGeneration(text=" J'aime la programmation.", generation_info=None, message=AIMessage(content=" J'aime la programmation.", additional_kwargs={}))]], llm_output={})

```

```
chat = ChatAnthropic(streaming=True, verbose=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
chat(messages)

```

```
 J'adore programmer.

```

```
AIMessage(content=" J'adore programmer.", additional_kwargs={})

```

