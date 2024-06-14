# 内存管理

聊天机器人的一个关键特性是能够使用之前对话轮次的内容作为上下文。这种状态管理可以采用多种形式，包括：

- 将之前的消息简单地添加到聊天模型的提示中。
- 上述方式，但剪裁旧消息以减少模型处理的干扰信息量。
- 更复杂的修改，如为长时间运行的对话合成摘要。

下面我们将详细介绍一些技术！

## 设置

您需要安装一些包，并将您的OpenAI API密钥设置为名为`OPENAI_API_KEY`的环境变量：

```python
%pip install --upgrade --quiet langchain langchain-openai

# 设置环境变量OPENAI_API_KEY，或从.env文件加载：
import dotenv

dotenv.load_dotenv()
```

    [33m警告: 您正在使用pip版本22.0.4；然而，版本23.3.2可用。
    您应该通过'/Users/jacoblee/.pyenv/versions/3.10.5/bin/python -m pip install --upgrade pip'命令考虑升级。[0m
    [33m
    [0m注意：您可能需要重新启动内核才能使用更新的程序包。
    




    True

我们还需要设置一个聊天模型，供下面的示例使用。

```python
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model="gpt-3.5-turbo-1106")
```

## 消息传递

最简单的记忆形式就是将聊天历史消息传递给一个链条。以下是一个示例：

```python
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "您是一个有用的助手。尽力回答所有问题。",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | chat

chain.invoke(
    {
        "messages": [
            HumanMessage(
                content="将这个句子从英语翻译成法语：我喜欢编程。"
            ),
            AIMessage(content="J'adore la programmation."),
            HumanMessage(content="你刚才说什么？"),
        ],
    }
)
```

可以看到，通过将之前的对话传递给一个链条，它可以使用它作为上下文来回答问题。这是聊天机器人记忆的基本概念-本指南的其余部分将演示传递或重新格式化消息的便捷技术。

## 聊天历史

将消息直接存储和传递为数组是完全可以的，但我们也可以使用LangChain内置的[消息历史记录类](/modules/memory/chat_messages/)来存储和加载消息。这个类的实例负责从持久存储中存储和加载聊天消息。LangChain集成了许多提供程序-您可以在这里查看[集成列表](/docs/integrations/memory)-但是为了本演示，我们将使用一个临时演示类。

以下是API的示例：

```python
from langchain.memory import ChatMessageHistory

demo_ephemeral_chat_history = ChatMessageHistory()

demo_ephemeral_chat_history.add_user_message(
    "将这个句子从英语翻译成法语：我喜欢编程。"
)

demo_ephemeral_chat_history.add_ai_message("J'adore la programmation.")

demo_ephemeral_chat_history.messages
```

我们可以直接使用它来存储我们链条的对话轮次：

```python
demo_ephemeral_chat_history = ChatMessageHistory()

input1 = "将这个句子从英语翻译成法语：我喜欢编程。"

demo_ephemeral_chat_history.add_user_message(input1)

response = chain.invoke(
    {
        "messages": demo_ephemeral_chat_history.messages,
    }
)

demo_ephemeral_chat_history.add_ai_message(response)

input2 = "我刚才问了你什么？"

demo_ephemeral_chat_history.add_user_message(input2)

chain.invoke(
    {
        "messages": demo_ephemeral_chat_history.messages,
    }
)
```

## 自动历史管理

前面的示例将消息显式传递给链条。这是一种完全可接受的方法，但它需要外部管理新消息。LangChain还包括一个对LCEL链进行包装的能够自动处理此过程的包装器，称为`RunnableWithMessageHistory`。

为了展示它的工作原理，让我们稍微修改上面的提示，以接受一个最终的`input`变量，在聊天历史之后填充一个`HumanMessage`模板。这意味着我们将期望一个包含当前消息之前所有消息的`chat_history`参数，而不是所有消息：

```python
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "您是一个有用的助手。尽力回答所有问题。",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

chain = prompt | chat
```

我们将最新的输入传递给这里的对话，让`RunnableWithMessageHistory`类包装我们的链条，并执行将`input`变量附加到聊天历史的工作。
 
接下来，让我们声明我们的包装链：

```python
from langchain_core.runnables.history import RunnableWithMessageHistory

demo_ephemeral_chat_history_for_chain = ChatMessageHistory()

chain_with_message_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: demo_ephemeral_chat_history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history",
)
```

除了我们要包装的链条之外，此类还接受几个参数：

- 一个工厂函数，根据给定的会话ID返回消息历史记录。这允许您的链条同时处理多个用户，通过加载不同的对话以返回相应的聊天历史记录。
- 一个`input_messages_key`，指定要跟踪和存储在聊天历史中的输入的哪个部分。在本示例中，我们要跟踪作为`input`传递的字符串。
- 一个`history_messages_key`，指定应将先前的消息注入到提示中。我们的提示有一个名为`chat_history`的`MessagesPlaceholder`，所以我们指定此属性以匹配。
- （对于具有多个输出的链条）一个`output_messages_key`，指定要存储为历史记录的输出。这与`input_messages_key`相反。

我们可以像往常一样调用这个新链条，还可以添加一个额外的`configurable`字段，用于指定要传递给工厂函数的特定`session_id`。这在演示中未使用，但在真实的链条中，您将希望返回与传递的会话对应的聊天历史记录：

```python
chain_with_message_history.invoke(
    {"input": "将这个句子从英语翻译成法语：我喜欢编程。"},
    {"configurable": {"session_id": "unused"}},
)
```

```python
chain_with_message_history.invoke(
    {"input": "我刚才问了你什么？"}, 
    {"configurable": {"session_id": "unused"}}
)
```


## 修改聊天记录

修改存储的聊天消息可以帮助您的聊天机器人应对各种情况。以下是一些示例：

### 删减消息

LLMs 和聊天模型具有有限的上下文窗口，即使您没有直接达到限制，您可能也希望限制模型处理的干扰量。一种解决方案是仅加载和存储最近的 `n` 条消息。让我们使用一个带有一些预加载消息的示例历史记录：

```python
demo_ephemeral_chat_history = ChatMessageHistory()

demo_ephemeral_chat_history.add_user_message("嗨！我是尼莫。")
demo_ephemeral_chat_history.add_ai_message("你好！")
demo_ephemeral_chat_history.add_user_message("你今天好吗？")
demo_ephemeral_chat_history.add_ai_message("很好，谢谢！")

demo_ephemeral_chat_history.messages
```

我们将使用上述消息历史记录和我们在上面声明的 `RunnableWithMessageHistory` 链：

```python
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

chain = prompt | chat

chain_with_message_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: demo_ephemeral_chat_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

chain_with_message_history.invoke(
    {"input": "我的名字是什么？"},
    {"configurable": {"session_id": "unused"}},
)
```

我们可以看到链式结构记住了预加载的名称。

但是假设我们的上下文窗口非常小，我们希望将传递给链式结构的消息数量仅限制为最近的 2 条消息。我们可以使用 `clear` 方法删除消息并将其重新添加到历史记录中。虽然我们可以不这样做，但是让我们将此方法放在链式结构的开头，以确保始终调用它：

```python
from langchain_core.runnables import RunnablePassthrough


def trim_messages(chain_input):
    stored_messages = demo_ephemeral_chat_history.messages
    if len(stored_messages) <= 2:
        return False

    demo_ephemeral_chat_history.clear()

    for message in stored_messages[-2:]:
        demo_ephemeral_chat_history.add_message(message)

    return True


chain_with_trimming = (
    RunnablePassthrough.assign(messages_trimmed=trim_messages)
    | chain_with_message_history
)
```

让我们调用这个新的链式结构并检查之后的消息：

```python
chain_with_trimming.invoke(
    {"input": "P. Sherman 住在哪里？"},
    {"configurable": {"session_id": "unused"}},
)
```

我们可以看到我们的历史记录已经删除了最旧的两条消息，并在结尾处添加了最近的对话。下次调用链式结构时，`trim_messages` 将再次被调用，只有最近的两条消息将传递给模型。在这种情况下，这意味着下次调用时模型将忘记我们给它的名字：

```python
chain_with_trimming.invoke(
    {"input": "我的名字是什么？"},
    {"configurable": {"session_id": "unused"}},
)
```
chain = prompt | chat

chain_with_message_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: demo_ephemeral_chat_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)
```

现在，让我们创建一个将之前的交互信息精简为摘要的函数。我们也可以将其添加到链的最前面：

```python
def summarize_messages(chain_input):
    stored_messages = demo_ephemeral_chat_history.messages
    if len(stored_messages) == 0:
        return False
    summarization_prompt = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder(variable_name="chat_history"),
            (
                "user",
                "将以上聊天消息精简成一条摘要消息。请尽可能包含具体细节。",
            ),
        ]
    )
    summarization_chain = summarization_prompt | chat

    summary_message = summarization_chain.invoke({"chat_history": stored_messages})

    demo_ephemeral_chat_history.clear()

    demo_ephemeral_chat_history.add_message(summary_message)

    return True


chain_with_summarization = (
    RunnablePassthrough.assign(messages_summarized=summarize_messages)
    | chain_with_message_history
)
```

让我们看看它是否记住我们给它的名字：

```python
chain_with_summarization.invoke(
    {"input": "我说过我的名字是什么吗？"},
    {"configurable": {"session_id": "unused"}},
)
```

结果应该返回："您自称为Nemo。我可以帮您什么忙呢，Nemo？"

```python
demo_ephemeral_chat_history.messages
```

结果应该返回以下内容：
```
[
    "对话是在Nemo和AI之间进行的。 Nemo先介绍了自己，AI用问候回应。 Nemo接着问AI近况如何，AI回答它很好。",
    "我说过我的名字是什么吗？",
    "您自称为Nemo。我可以帮您什么忙呢，Nemo？"
]
```

请注意，再次调用该链将生成从初始摘要到新消息等的另一个摘要。您也可以设计一种混合方法，在其中一定数量的消息保留在聊天历史记录中，而其他消息被摘要。
