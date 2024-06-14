# 添加消息历史记录（内存）

`RunnableWithMessageHistory`允许我们为特定类型的链添加消息历史记录。它包装另一个Runnable，并管理聊天消息历史记录。

具体来说，它可用于以下任何一种输入为

* `BaseMessage`序列
* 具有以`BaseMessage`序列为输入的键的字典
* 具有将最新消息（字符串或`BaseMessage`序列）和历史消息作为键的字典

并将以下任一输出作为输出

* 可当作`AIMessage`内容处理的字符串
* `BaseMessage`序列
* 包含`BaseMessage`序列的键的字典

让我们通过一些示例来看看它是如何工作的。首先，我们构建一个Runnable（在这里接受一个字典作为输入，并返回一个消息作为输出）：

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai.chat_models import ChatOpenAI

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You're an assistant who's good at {ability}. Respond in 20 words or fewer",
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)
runnable = prompt | model
```

为了管理消息历史记录，我们将需要：
1. 此Runnable；
2. 一个可调用对象，返回`BaseChatMessageHistory`的实例。

请查看[内存集成](https://integrations.langchain.com/memory)页面，了解使用Redis和其他供应商实现聊天消息历史记录的方法。这里，我们演示如何使用内存中的`ChatMessageHistory`以及使用`RedisChatMessageHistory`进行更持久化的存储。

## 内存中

下面我们展示一个简单的示例，其中聊天历史记录保存在内存中，这里通过一个全局Python字典实现。

我们构建了一个可调用的`get_session_history`，它引用此字典以返回`ChatMessageHistory`的实例。可以通过在运行时将配置传递给`RunnableWithMessageHistory`来指定可调用对象的参数。默认情况下，将使用字符串`session_id`作为配置参数。可以通过`history_factory_config`关键字参数来调整。

使用单参数默认值：

```python
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


with_message_history = RunnableWithMessageHistory(
    runnable,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)
```

注意，我们指定了`input_messages_key`（要作为最新输入消息处理的键）和`history_messages_key`（要添加历史消息的键）。

在调用此新Runnable时，我们通过配置参数指定相应的聊天历史记录：

```python
with_message_history.invoke(
    {"ability": "math", "input": "What does cosine mean?"},
    config={"configurable": {"session_id": "abc123"}},
)
```




    AIMessage(content='Cosine is a trigonometric function that calculates the ratio of the adjacent side to the hypotenuse of a right triangle.')




```python
# 记住
with_message_history.invoke(
    {"ability": "math", "input": "What?"},
    config={"configurable": {"session_id": "abc123"}},
)
```




    AIMessage(content='Cosine is a mathematical function used to calculate the length of a side in a right triangle.')




```python
# 新的session_id --> 不会记住。
with_message_history.invoke(
    {"ability": "math", "input": "What?"},
    config={"configurable": {"session_id": "def234"}},
)
```




    AIMessage(content='I can help with math problems. What do you need assistance with?')



我们可以通过将`ConfigurableFieldSpec`对象的列表传递给`history_factory_config`参数来自定义跟踪消息历史记录的配置参数。下面，我们使用了两个参数：`user_id`和`conversation_id`。

```python
from langchain_core.runnables import ConfigurableFieldSpec

store = {}


def get_session_history(user_id: str, conversation_id: str) -> BaseChatMessageHistory:
    if (user_id, conversation_id) not in store:
        store[(user_id, conversation_id)] = ChatMessageHistory()
    return store[(user_id, conversation_id)]


with_message_history = RunnableWithMessageHistory(
    runnable,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
    history_factory_config=[
        ConfigurableFieldSpec(
            id="user_id",
            annotation=str,
            name="User ID",
            description="Unique identifier for the user.",
            default="",
            is_shared=True,
        ),
        ConfigurableFieldSpec(
            id="conversation_id",
            annotation=str,
            name="Conversation ID",
            description="Unique identifier for the conversation.",
            default="",
            is_shared=True,
        ),
    ],
)
```


```python
with_message_history.invoke(
    {"ability": "math", "input": "Hello"},
    config={"configurable": {"user_id": "123", "conversation_id": "1"}},
)
```

### 使用不同签名的Runnable的示例

上面的Runnable接受一个字典作为输入，并返回一个BaseMessage。下面我们展示一些其他选项。

#### 输入为消息，输出为字典

```python
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableParallel

chain = RunnableParallel({"output_message": ChatOpenAI()})


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    output_messages_key="output_message",
)

with_message_history.invoke(
    [HumanMessage(content="What did Simone de Beauvoir believe about free will")],
    config={"configurable": {"session_id": "baz"}},
)
```




    {'output_message': AIMessage(content="Simone de Beauvoir believed in the existence of free will. She argued that individuals have the ability to make choices and determine their own actions, even in the face of social and cultural constraints. She rejected the idea that individuals are purely products of their environment or predetermined by biology or destiny. Instead, she emphasized the importance of personal responsibility and the need for individuals to actively engage in creating their own lives and defining their own existence. De Beauvoir believed that freedom and agency come from recognizing one's own freedom and actively exercising it in the pursuit of personal and collective liberation.")}




```python
with_message_history.invoke(
    [HumanMessage(content="How did this compare to Sartre")],
    config={"configurable": {"session_id": "baz"}},
)
```




    {'output_message': AIMessage(content='Simone de Beauvoir\'s views on free will were closely aligned with those of her contemporary and partner Jean-Paul Sartre. Both de Beauvoir and Sartre were existentialist philosophers who emphasized the importance of individual freedom and the rejection of determinism. They believed that human beings have the capacity to transcend their circumstances and create their own meaning and values.\n\nSartre, in his famous work "Being and Nothingness," argued that human beings are condemned to be free, meaning that we are burdened with the responsibility of making choices and defining ourselves in a world that lacks inherent meaning. Like de Beauvoir, Sartre believed that individuals have the ability to exercise their freedom and make choices in the face of external and internal constraints.\n\nWhile there may be some nuanced differences in their philosophical writings, overall, de Beauvoir and Sartre shared a similar belief in the existence of free will and the importance of individual agency in shaping one\'s own life.')}



#### Messages input, messages output


```python
RunnableWithMessageHistory(
    ChatOpenAI(),
    get_session_history,
)
```

#### Dict with single key for all messages input, messages output


```python
from operator import itemgetter

RunnableWithMessageHistory(
    itemgetter("input_messages") | ChatOpenAI(),
    get_session_history,
    input_messages_key="input_messages",
)
```

## 持久性存储

在许多情况下，持久化对话历史记录是可取的。`RunnableWithMessageHistory` 不关心 `get_session_history` 可调用函数如何检索聊天消息历史记录。在 [此处](https://github.com/langchain-ai/langserve/blob/main/examples/chat_with_persistence_and_user/server.py) 查看使用本地文件系统的示例。下面我们演示如何使用 Redis。请查看 [memory integrations](https://integrations.langchain.com/memory) 页面了解使用其他服务提供商的聊天消息历史记录实现。

### 设置

如果尚未安装 Redis，则需要安装 Redis：


```python
%pip install --upgrade --quiet redis
```

如果没有现有的 Redis 部署用于连接，则启动本地 Redis Stack 服务器：
```bash
docker run -d -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```


```python
REDIS_URL = "redis://localhost:6379/0"
```

### [LangSmith](/langsmith)

对于消息历史记录注入等情况，LangSmith 尤其有用，否则很难理解链中各个部分的输入是什么。

注意，LangSmith 不是必需的，但它很有帮助。
如果您希望使用 LangSmith，在上面的链接上注册后，请确保取消下面的注释并设置环境变量以开始记录 traces：


```python
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

只需定义一个新的可调用函数来更新消息历史记录的实现，这次返回 `RedisChatMessageHistory` 的实例：


```python
from langchain_community.chat_message_histories import RedisChatMessageHistory


def get_message_history(session_id: str) -> RedisChatMessageHistory:
    return RedisChatMessageHistory(session_id, url=REDIS_URL)


with_message_history = RunnableWithMessageHistory(
    runnable,
    get_message_history,
    input_messages_key="input",
    history_messages_key="history",
)
```

可以像以前一样调用：


```python
with_message_history.invoke(
    {"ability": "math", "input": "What does cosine mean?"},
    config={"configurable": {"session_id": "foobar"}},
)
```




    AIMessage(content='Cosine is a trigonometric function that represents the ratio of the adjacent side to the hypotenuse in a right triangle.')




```python
with_message_history.invoke(
    {"ability": "math", "input": "What's its inverse"},
    config={"configurable": {"session_id": "foobar"}},
)
```




    AIMessage(content='The inverse of cosine is the arccosine function, denoted as acos or cos^-1, which gives the angle corresponding to a given cosine value.')



- [Langsmith trace](https://smith.langchain.com/public/bd73e122-6ec1-48b2-82df-e6483dc9cb63/r)


查看第二次调用的 Langsmith 追踪，我们可以看到在构建提示时注入了一个名为 "history" 的变量，它是一个包含两条消息（我们的第一个输入和第一个输出）的列表。