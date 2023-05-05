

OpenAI[#](#openai "Permalink to this headline")
===============================================

本笔记涵盖了如何开始使用OpenAI聊天模型。

```
from langchain.chat_models import ChatOpenAI
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
chat = ChatOpenAI(temperature=0)

```

```
messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Translate this sentence from English to French. I love programming.")
]
chat(messages)

```

```
AIMessage(content="J'aime programmer.", additional_kwargs={}, example=False)

```

您可以使用模板，通过使用 `MessagePromptTemplate` 来实现。您可以从一个或多个 `MessagePromptTemplates` 构建一个 `ChatPromptTemplate`。您可以使用 `ChatPromptTemplate` 的 `format_prompt` 方法 - 这将返回一个 `PromptValue`，您可以将其转换为字符串或消息对象，具体取决于您希望将格式化值用作llm或聊天模型的输入还是消息对象。

为了方便起见，在模板上公开了一个 `from_template` 方法。如果您要使用此模板，它将如下所示：

```
template="You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

```

```
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# get a chat completion from the formatted messages
chat(chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages())

```

```
AIMessage(content="J'adore la programmation.", additional_kwargs={})

```

