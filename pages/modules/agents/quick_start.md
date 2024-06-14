# 快速入门

要最好地理解代理框架，让我们构建一个代理，其中包含两个工具：一个用于在线查找信息，另一个用于查找我们加载到索引中的特定数据。

这将假定您已了解 [LLMs](/modules/model_io/) 和 [检索](/modules/data_connection/)，因此如果您还没有探索这些部分，建议您这样做。

## 设置：LangSmith

根据定义，代理在返回给用户的输出之前会执行一系列自我确定的、依赖输入的步骤。这使得调试这些系统特别棘手，而可观察性尤为重要。[LangSmith](/langsmith) 在这种情况下特别有用。

建立使用LangChain时，所有步骤都将自动在LangSmith中跟踪。
要设置LangSmith，我们只需要设置以下环境变量：

```bash
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY="<your-api-key>"
```

## 定义工具

我们首先需要创建我们想要使用的工具。我们将使用两个工具：[Tavily](/docs/integrations/tools/tavily_search)（用于在线搜索），然后是在我们创建的本地索引上的检索器

### [Tavily](/docs/integrations/tools/tavily_search)

LangChain 中有一个内置工具，可方便地使用 Tavily 搜索引擎作为工具。
请注意，这需要一个 API 密钥 - 他们有一个免费的套餐，但如果您没有或不想创建一个，您可以忽略这一步。

创建您的 API 密钥后，您需要将其导出为：

```bash
export TAVILY_API_KEY="..."
```

```python
from langchain_community.tools.tavily_search import TavilySearchResults
```

```python
search = TavilySearchResults()
```

```python
search.invoke("what is the weather in SF")
```

### 检索器

我们还将在我们自己的一些数据上创建一个检索器。有关此处每个步骤的更深入解释，请查看 [本节](/modules/data_connection/)。

```python
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()
documents = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200
).split_documents(docs)
vector = FAISS.from_documents(documents, OpenAIEmbeddings())
retriever = vector.as_retriever()
```

```python
retriever.get_relevant_documents("how to upload a dataset")[0]
```

现在我们已经填充了我们将要进行检索的索引，我们可以轻松地将其转换为一个工具（代理正确使用它所需的格式）

```python
from langchain.tools.retriever import create_retriever_tool
```

```python
retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
)
```

### 工具

现在我们已经创建了这两个工具，我们可以创建一个我们将在下游使用的工具列表。

```python
tools = [search, retriever_tool]
```

## 创建代理

现在我们已经定义了工具，我们可以创建代理。我们将使用一个 OpenAI Functions 代理 - 有关此类代理的更多信息，以及其他选项，请参阅 [本指南](/modules/agents/agent_types/)。

首先，我们选择要引导代理的 LLM。

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
```

接下来，我们选择要使用的提示来引导代理。

如果您想查看此提示的内容并访问 LangSmith，请前往：

https://smith.langchain.com/hub/hwchase17/openai-functions-agent

```python
from langchain import hub

# 获取要使用的提示 - 您可以修改这个！
prompt = hub.pull("hwchase17/openai-functions-agent")
prompt.messages
```

现在，我们可以使用 LLM、提示和工具初始化代理。代理负责接受输入并决定采取什么行动。至关重要的是，代理不执行这些操作 - 这是由 AgentExecutor（下一步）执行的。有关如何考虑这些组件的更多信息，请参阅我们的 [概念指南](/modules/agents/concepts/)。

```python
from langchain.agents import create_tool_calling_agent

agent = create_tool_calling_agent(llm, tools, prompt)
```

最后，我们将代理（大脑）与工具结合在 AgentExecutor 中（该 Executor 将重复调用代理并执行工具）。

```python
from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

## 运行代理

现在我们可以在几个查询上运行代理！请注意，目前这些都是**无状态**查询（它不会记住先前的交互）。

```python
agent_executor.invoke({"input": "hi!"})
```

```python
agent_executor.invoke({"input": "how can langsmith help with testing?"})
```

```python
agent_executor.invoke({"input": "whats the weather in sf?"})
``` 

## 添加在内存中

正如之前提到的，这个代理是无状态的。这意味着它不会记住先前的交互。要给它添加记忆，我们需要传入先前的`chat_history`。注意：它需要被称为`chat_history`，因为我们正在使用的提示。如果我们使用不同的提示，我们可以更改变量名


```python
# 在这里，我们传入一个空的消息列表给chat_history，因为这是对话中的第一条消息
agent_executor.invoke({"input": "hi! my name is bob", "chat_history": []})
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m你好 Bob！我今天可以如何帮助你？[0m
    
    [1m> 链处理完成。[0m
    




    {'input': 'hi! my name is bob',
     'chat_history': [],
     'output': '你好 Bob！我今天可以如何帮助你？'}




```python
from langchain_core.messages import AIMessage, HumanMessage
```


```python
agent_executor.invoke(
    {
        "chat_history": [
            HumanMessage(content="hi! my name is bob"),
            AIMessage(content="Hello Bob! How can I assist you today?"),
        ],
        "input": "what's my name?",
    }
)
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m你的名字是 Bob。我可以如何帮助你，Bob？[0m
    
    [1m> 链处理完成。[0m
    




    {'chat_history': [HumanMessage(content='hi! my name is bob'),
      AIMessage(content='Hello Bob! How can I assist you today?')],
     'input': "what's my name?",
     'output': '你的名字是 Bob。我可以如何帮助你，Bob？'}



如果我们想自动跟踪这些消息，我们可以将其包装在一个RunnableWithMessageHistory中。有关如何使用此功能的更多信息，请参阅[此指南](/expression_language/how_to/message_history/)。


```python
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
```


```python
message_history = ChatMessageHistory()
```


```python
agent_with_chat_history = RunnableWithMessageHistory(
    agent_executor,
    # 这是必需的，因为在大多数实际情况下，需要一个会话 id
    # 这里并没有真正使用，因为我们使用的是一个简单的内存中的 ChatMessageHistory
    lambda session_id: message_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)
```


```python
agent_with_chat_history.invoke(
    {"input": "hi! I'm bob"},
    # 这是必需的，因为在大多数实际情况下，需要一个会话 id
    # 这里并没有真正使用，因为我们使用的是一个简单的内存中的 ChatMessageHistory
    config={"configurable": {"session_id": "<foo>"}},
)
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m你好 Bob！我今天可以如何帮助你？[0m
    
    [1m> 链处理完成。[0m
    




    {'input': "hi! I'm bob",
     'chat_history': [],
     'output': '你好 Bob！我今天可以如何帮助你？'}




```python
agent_with_chat_history.invoke(
    {"input": "what's my name?"},
    # 这是必需的，因为在大多数实际情况下，需要一个会话 id
    # 这里并没有真正使用，因为我们使用的是一个简单的内存中的 ChatMessageHistory
    config={"configurable": {"session_id": "<foo>"}},
)
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m你的名字是 Bob！我可以如何帮助你，Bob？[0m
    
    [1m> 链处理完成。[0m
    




    {'input': "what's my name?",
     'chat_history': [HumanMessage(content="hi! I'm bob"),
      AIMessage(content='Hello Bob! How can I assist you today?')],
     'output': '你的名字是 Bob！我可以如何帮助你，Bob？'}



## 结论

到这里就结束了！在这个快速入门中，我们介绍了如何创建一个简单的代理。代理是一个复杂的主题，有很多内容需要学习！请返回[主代理页面](/modules/agents/)，查找更多关于概念指南、不同类型的代理、如何创建自定义工具等的资源！

---



# 快速入门

Chat models是语言模型的一种变体。
虽然Chat models在内部使用语言模型，但它们使用的界面略有不同。
它们使用的不是“输入文本，输出文本”API，而是使用一种以“聊天消息”为输入和输出的界面。

## 设置


```{=mdx}
import ChatModelTabs from "@theme/ChatModelTabs";

<ChatModelTabs customVarName="chat" />
```

如果您不想设置环境变量，可以在初始化聊天模型类时通过api key参数参数直接传入密钥:

```{=mdx}
<ChatModelTabs
  anthropicParams={`model="claude-3-sonnet-20240229", api_key="..."`}
  openaiParams={`model="gpt-3.5-turbo-0125", api_key="..."`}
  mistralParams={`model="mistral-large-latest", api_key="..."`}
  fireworksParams={`model="accounts/fireworks/models/mixtral-8x7b-instruct", api_key="..."`}
  googleParams={`model="gemini-pro", google_api_key="..."`}
  togetherParams={`, together_api_key="..."`}
  customVarName="chat"
/>
```

## 消息

Chat模型的界面是基于消息而不是原始文本。
LangChain当前支持的消息类型有 `AIMessage`, `HumanMessage`, `SystemMessage`, `FunctionMessage` 和 `ChatMessage` -- `ChatMessage` 接受一个任意的角色参数。大部分情况下，您只需处理 `HumanMessage`, `AIMessage`, 和 `SystemMessage`

## LCEL

Chat模型实现了 [Runnable接口](/expression_language/interface)，这是 [LangChain Expression Language (LCEL)](/expression_language/) 的基本构建块。这意味着它们支持 `invoke`, `ainvoke`, `stream`, `astream`, `batch`, `abatch`, `astream_log` 调用。

Chat模型接受 `List[BaseMessage]` 或可转换为消息的对象作为输入，包括 `str` (转换为 `HumanMessage`) 和 `PromptValue`。


```python
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="你是一个乐于助人的助手"),
    HumanMessage(content="模型正则化的目的是什么？"),
]
```


```python
# | output: false
# | echo: false

from langchain_openai import ChatOpenAI

chat = ChatOpenAI()
```


```python
chat.invoke(messages)
```




    AIMessage(content="模型正则化的目的是防止机器学习模型过度拟合训练数据。当模型变得过于复杂并开始拟合训练数据中的噪声时，就会出现过拟合现象。过拟合会导致模型在未见数据上的泛化能力较差。正则化技术会对模型的目标函数引入额外的约束或惩罚项，以避免模型过于复杂，并促使模型更简单、更具泛化能力。正则化有助于在完全拟合训练数据和防止过拟合之间取得平衡，从而提高模型在新的、未见数据上的性能。")




```python
for chunk in chat.stream(messages):
    print(chunk.content, end="", flush=True)
```

    模型正则化的目的是防止过拟合并提高机器学习模型的泛化能力。当模型过于复杂并学习训练数据中的噪声或随机变化时，就会导致模型在新的、未见数据上的性能较差。正则化技术通过在模型的学习过程中引入额外的约束或惩罚项来降低模型复杂度。这有助于提高模型的泛化能力，减少过拟合的风险，并使模型能够在未见数据上做出准确的预测。


```python
chat.batch([messages])
```




    [AIMessage(content="模型正则化的目的是防止机器学习模型在训练数据上过拟合。过拟合发生在模型变得过于复杂并开始学习训练数据中的噪声或随机波动，而不是基本模式或关系。正则化技术向模型的目标函数添加惩罚项，阻止模型变得过于复杂，并帮助其更好地拟合新的、未见过的数据。通过减小方差并提高模型整体性能，正则化有助于提高模型在新数据上的准确性。")]

## [LangSmith](/langsmith)

所有的`ChatModel`都带有内建的LangSmith跟踪功能。只需设置以下环境变量：
```bash
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY=<你的API密钥>
```

任何`ChatModel`的调用（无论是在链中还是不在链中）都将自动被跟踪。跟踪将包括输入、输出、延迟、令牌使用情况、调用参数、环境参数等等。请参阅此处的示例：https://smith.langchain.com/public/a54192ae-dd5c-4f7a-88d1-daa1eaba1af7/r。

然后，在LangSmith中，您可以对任何跟踪提供反馈，编译带注释的数据集进行评估，在 playground 中调试性能等等。

## [Legacy] `__call__`
#### 输入消息 -> 输出消息

为了方便，您还可以将聊天模型视为可调用对象。您可以通过将一个或多个消息传递给聊天模型来获得聊天的完成情况。响应将是一条消息。


```python
from langchain_core.messages import HumanMessage, SystemMessage

chat(
    [
        HumanMessage(
            content="将这句话从英语翻译成法语：我爱编程。"
        )
    ]
)
```




    AIMessage(content="J'adore la programmation.")



OpenAI的聊天模型支持多条消息作为输入。有关更多信息，请参阅[这里](https://platform.openai.com/docs/guides/chat/chat-vs-completions)。以下是向聊天模型发送系统消息和用户消息的示例：


```python
messages = [
    SystemMessage(
        content="您是一个有帮助的助手，负责将英语翻译成法语。"
    ),
    HumanMessage(content="我爱编程。"),
]
chat(messages)
```




    AIMessage(content="J'adore la programmation.")



## [Legacy] `generate`
#### 批量调用、更丰富的输出

您还可以更进一步，使用`generate`为多组消息生成完成结果。这将返回一个带有额外`message`参数的`LLMResult`。该参数将包括有关每次生成的更多信息，超出返回的消息（例如，完成原因）以及有关完整API调用的其他信息（例如，使用的总令牌数）。

```python
batch_messages = [
    [
        SystemMessage(
            content="您是一个有帮助的助手，负责将英语翻译成法语。"
        ),
        HumanMessage(content="我爱编程。"),
    ],
    [
        SystemMessage(
            content="您是一个有帮助的助手，负责将英语翻译成法语。"
        ),
        HumanMessage(content="我爱人工智能。"),
    ],
]
result = chat.generate(batch_messages)
result
```




    LLMResult(generations=[[ChatGeneration(text="J'adore programmer.", generation_info={'finish_reason': 'stop'}, message=AIMessage(content="J'adore programmer."))], [ChatGeneration(text="J'adore l'intelligence artificielle.", generation_info={'finish_reason': 'stop'}, message=AIMessage(content="J'adore l'intelligence artificielle."))]], llm_output={'token_usage': {'prompt_tokens': 53, 'completion_tokens': 18, 'total_tokens': 71}, 'model_name': 'gpt-3.5-turbo'}, run=[RunInfo(run_id=UUID('077917a9-026c-47c4-b308-77b37c3a3bfa')), RunInfo(run_id=UUID('0a70a0bf-c599-4f51-932a-c7d42202c984'))])



您可以从此LLMResult中获取诸如令牌使用情况之类的信息：


```python
result.llm_output
```




    {'token_usage': {'prompt_tokens': 53,
      'completion_tokens': 18,
      'total_tokens': 71},
     'model_name': 'gpt-3.5-turbo'}




---

# 快速入门

大型语言模型（LLMs）是LangChain的核心组件。
LangChain本身不提供LLMs，而是提供一个与多个不同LLMs进行交互的标准接口。

有许多LLM提供商（OpenAI，Cohere，Hugging Face等）-`LLM`类旨在为它们提供一个标准接口。

在这个演示中，我们将使用OpenAI的LLM包装器，尽管突出显示的功能对于所有LLM类型都是通用的。

### 设置

为了这个例子，我们需要安装OpenAI Python包：

```bash
pip install openai
```

访问API需要一个API密钥，您可以通过创建一个帐户并在此处获取API密钥来获得。一旦我们有了密钥，我们希望在启动时将其设置为环境变量：

```bash
export OPENAI_API_KEY="..."
```

如果您不想设置环境变量，可以在初始化OpenAI LLM类时直接通过`api_key`命名参数传递密钥：

```python
from langchain_openai import OpenAI

llm = OpenAI(api_key="...")
```

否则，您可以不带任何参数初始化：

```python
from langchain_openai import OpenAI

llm = OpenAI()
```

## LCEL

LLMs实现了[Runnable interface](/expression_language/interface)，这是[LangChain Expression Language (LCEL)](/expression_language/)的基本构建块。这意味着它们支持`invoke`、`ainvoke`、`stream`、`astream`、`batch`、`abatch`、`astream_log`调用。

LLMs接受**字符串**作为输入，或者可以被强制转换为字符串提示的对象，包括`List[BaseMessage]`和`PromptValue`。

```python
llm.invoke("失业和通货膨胀之间的关系有哪些理论？")
```


'\n\n1. 菲利普斯曲线理论：该理论认为失业和通货膨胀之间存在一种相反的关系，也就是失业率低时，通货膨胀率就高，反之亦然。\n\n2.货币主义理论：该理论指出失业和通货膨胀之间的关系较弱，货币供应的变化在决定通货膨胀方面更为重要。\n\n3.资源利用理论：这表明当失业率低时，企业可以提高工资和价格以利用增加的产品和服务需求。这导致通货膨胀率升高。'


```python
for chunk in llm.stream("失业和通货膨胀之间的关系有哪些理论？"):
    print(chunk, end="", flush=True)
```

    
    
    1. 菲利普斯曲线理论：该理论认为失业和通货膨胀之间存在一种相反的关系，也就是失业率低时，通货膨胀率就会上升，反之亦然。
    
    2. 成本推动通货膨胀理论：该理论认为失业率的增加导致总需求减少，从而由于供应减少导致物价上涨。
    
    3. 工资推动通货膨胀理论：该理论认为当失业率较低时，由于竞争争夺劳动力，工资会上涨，从而导致物价上涨。
    
    4. 货币主义理论：该理论认为失业和通货膨胀之间没有直接关系，但货币供应的增加会导致通货膨胀，而失业率的增加可能导致货币供应的增加。


```python
llm.batch(["失业和通货膨胀之间的关系有哪些理论？"])
```


['\n\n1. 菲利普斯曲线理论：该理论认为失业和通货膨胀之间存在一种相反的关系，也就是失业率下降，通货膨胀上升，而失业率上升，通货膨胀下降。该理论的基本观点是，当经济状况良好时，对商品和服务的需求增加，导致价格上涨。\n\n2. 成本推动理论：该理论认为，当生产成本增加时，会导致价格上涨和产量下降。这可能导致失业率升高，最终导致通货膨胀率上升。\n\n3. 需求拉动理论：该理论认为，当商品和服务的需求增加时，会导致价格上涨，最终导致通货膨胀上升。此时，由于企业无法满足需求的增加，失业率可能上升。\n\n4. 结构性失业理论：该理论认为，当失业者的技能与就业市场所需的技能不匹配时，会导致失业率上升，最终导致通货膨胀上升。']


```python
await llm.ainvoke("失业和通货膨胀之间的关系有哪些理论？")
```


'\n\n1. 菲利普斯曲线理论：该理论认为失业和通货膨胀之间存在一种相反的关系，也就是失业率下降，通货膨胀率上升，反之亦然。\n\n2. 成本推动理论：该理论认为失业率的增加导致总需求下降，从而导致供应减少和价格上涨。\n\n3. 需求拉动理论：该理论认为当商品和服务的需求增加时，会导致价格上涨和通货膨胀。此时，由于企业无法满足需求，失业率可能增加。\n\n4. 货币理论：该理论认为货币供应量和通货膨胀与失业之间存在关系。当货币供应量增加时，价格上涨，进而导致通货膨胀增加。如果失业率较高，则货币供应量增加，导致通货膨胀增加。'


```python
async for chunk in llm.astream("失业和通货膨胀之间的关系有哪些理论？"):
    print(chunk, end="", flush=True)
```

    
    
    1. 菲利普斯曲线理论：该理论认为失业和通货膨胀之间存在一种相反的关系，也就是失业率低时，通货膨胀率上升，反之亦然。
    
    2. 成本推动理论：该理论认为失业率和成本推动通货膨胀之间存在一种关系。成本推动通货膨胀理论认为，当生产成本上升时，会导致价格上升和产量下降。这可能导致失业率上升，最终导致通货膨胀率上升。
    
    3. 需求拉动理论：该理论认为需求拉动通货膨胀理论认为，当商品和服务的需求增加时，会导致价格上升和通货膨胀上升。这可能导致失业率上升，因为企业无法满足需求的增加。
    
    4. 货币理论：该理论认为货币供应量和通货膨胀与失业之间存在关系。当货币供应量增加时，导致通货膨胀增加。如果失业率较高，货币供应量也会增加，从而导致通货膨胀增加。


```python
await llm.abatch(["失业和通货膨胀之间的关系有哪些理论？"])
```


['\n\n1. 菲利普斯曲线理论：该理论认为失业和通货膨胀之间存在一种相反的关系，也就是失业率下降，导致通货膨胀上升，而失业率上升，导致通货膨胀下降。该理论认为，当经济状况良好时，存在更多对商品和服务的需求，导致物价上升。\n\n2. 成本推动理论：该理论认为，当生产成本增加时，会导致价格上升和产量下降。这可能导致失业率上升，并最终导致通货膨胀上升。\n\n3. 需求拉动理论：该理论认为，当商品和服务的需求增加时，会导致价格上升，并最终导致通货膨胀上升。这可能导致失业率上升，因为企业无法满足需求的增加。\n\n4. 结构性失业理论：该理论认为，当失业者的技能与就业市场所需的技能不匹配时，会导致失业率上升，并最终导致通货膨胀上升。']


```python
async for chunk in llm.astream_log("失业和通货膨胀之间的关系有哪些理论？"):
    print(chunk)
```

    RunLogPatch({'op': 'replace',
      'path': '',
      'value': {'final_output': None,
                'id': 'baf410ad-618e-44db-93c8-809da4e3ed44',
                'logs': {},
                'streamed_output': []}})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '\n'})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '\n'})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '1'})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '.'})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': ' 菲利普斯曲线理论：'})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '该理论认为失业和通货膨胀之间存在一种相反的关系，也就是失业率下降，通货膨胀率上升，反之亦然。\n'})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '2. 成本推动理论：'})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '该理论认为失业率的增加导致总需求下降，从而导致供应减少和价格上涨。\n'})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '3. 需求拉动理论：'})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '该理论认为当商品和服务的需求增加时，会导致价格上涨和通货膨胀。此时，由于企业无法满足需求的增加，失业率可能增加。\n'})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '4. 货币理论：'})
    RunLogPatch({'op': 'add',
      'path': '/streamed_output/-',
      'value': '该理论认为货币供应量和通货膨胀与失业之间存在关系。当货币供应量增加时，导致通货膨胀增加。如果失业率较高，货币供应量也会增加，导致通货膨胀增加。\n'})
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '\n'})



                


## [LangSmith](/langsmith)

所有`LLM`都配备了内置的LangSmith跟踪功能。只需设置以下环境变量：
```bash
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY=<your-api-key>
```

任何`LLM`调用（不管是嵌套在链中还是独立的）都将自动被跟踪。跟踪将包括输入、输出、延迟、令牌使用、调用参数、环境参数等内容。在这里查看一个示例：https://smith.langchain.com/public/7924621a-ff58-4b1c-a2a2-035a354ef434/r。

在LangSmith中，您可以为任何跟踪提供反馈，编译带注释的数据集进行评估，在playground中调试性能等等。

聊天模型可以输出文本。但是很多时候，你可能希望获得比普通文本更结构化的信息。这就是输出解析器发挥作用的地方。

输出解析器是帮助结构化语言模型响应的类。一个输出解析器必须实现两种主要方法:

- "获取格式说明": 一个返回包含语言模型输出应如何格式化的指令字符串的方法。
- "解析": 一个接受一个字符串（假定为语言模型的响应）并将其解析为某种结构的方法。

还有一个可选项：

- "带提示解析": 一个接受一个字符串（假定为语言模型的响应）和一个提示（假定为生成此响应的提示）并将其解析为某种结构的方法。在这种情况下，提示主要用于输出解析器想要重试或修复输出并需要提示中的信息来执行此操作。

## 入门

下面我们将介绍主要类型的输出解析器，即 `PydanticOutputParser`。


```python
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain_openai import OpenAI

model = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.0)


# 定义您期望的数据结构。
class Joke(BaseModel):
    setup: str = Field(description="用来设置笑话的问题")
    punchline: str = Field(description="用来解答笑话的答案")

    # 您可以使用 Pydantic 轻松添加自定义验证逻辑。
    @validator("setup")
    def question_ends_with_question_mark(cls, field):
        if field[-1] != "?":
            raise ValueError("Badly formed question!")
        return field


# 设置一个解析器 + 将指令注入到提示模板中。
parser = PydanticOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="回答用户的查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# 还有一个用来提示语言模型填充数据结构的查询。
prompt_and_model = prompt | model
output = prompt_and_model.invoke({"query": "Tell me a joke."})
parser.invoke(output)
```




    Joke(setup='鸡为什么要过马路？', punchline='为了到达另一边！')



## LCEL

输出解析器实现[可运行接口](/expression_language/interface)，这是[LangChain 表达式语言 (LCEL)](/expression_language/)的基本构建块。这意味着它们支持 `invoke`、`ainvoke`、`stream`、`astream`、`batch`、`abatch`、`astream_log` 调用。

输出解析器接受字符串或 `BaseMessage` 输入，并可以返回任意类型。


```python
parser.invoke(output)
```




    Joke(setup='鸡为什么要过马路？', punchline='为了到达另一边！')



我们也可以将解析器添加到我们的 `Runnable` 序列中，而不是手动调用解析器：


```python
chain = prompt | model | parser
chain.invoke({"query": "Tell me a joke."})
```




    Joke(setup='鸡为什么要过马路？', punchline='为了到达另一边！')



虽然所有解析器都支持流接口，但只有一些解析器可以流式传递部分解析对象，因为这在很大程度上取决于输出类型。不能构造部分对象的解析器将简单地生成完全解析的输出。

例如，`SimpleJsonOutputParser` 可以流式传递部分输出：


```python
from langchain.output_parsers.json import SimpleJsonOutputParser

json_prompt = PromptTemplate.from_template(
    "返回一个带有 `answer` 键的 JSON 对象，以回答以下问题：{question}"
)
json_parser = SimpleJsonOutputParser()
json_chain = json_prompt | model | json_parser
```


```python
list(json_chain.stream({"question": "Who invented the microscope?"}))
```




    [{},
     {'answer': ''},
     {'answer': 'Ant'},
     {'answer': 'Anton'},
     {'answer': 'Antonie'},
     {'answer': 'Antonie van'},
     {'answer': 'Antonie van Lee'},
     {'answer': 'Antonie van Leeu'},
     {'answer': 'Antonie van Leeuwen'},
     {'answer': 'Antonie van Leeuwenho'},
     {'answer': 'Antonie van Leeuwenhoek'}]



而 `PydanticOutputParser` 则不能：


```python
list(chain.stream({"query": "Tell me a joke."}))
```




    [Joke(setup='鸡为什么要过马路？', punchline='为了到达另一边！')]




请检查修改后的文档，看是否满足您的要求。如果需要进一步调整，请随时告诉我。# 快速参考

提示模板是为生成语言模型提示的预定义配方。

模板可能包括说明、少量示例以及特定上下文和问题，适用于特定任务。

LangChain 提供了创建和使用提示模板的工具。

LangChain 努力创建与模型无关的模板，以便轻松地在不同的语言模型之间重用现有模板。

通常，语言模型期望提示要么是一个字符串，要么是一组聊天消息。

## `PromptTemplate`

使用 `PromptTemplate` 创建一个字符串提示的模板。

默认情况下，`PromptTemplate` 使用[Python 的 str.format](https://docs.python.org/3/library/stdtypes.html#str.format) 语法进行模板化。


```python
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "告诉我一个关于 {content} 的 {adjective} 笑话。"
)
prompt_template.format(adjective="有趣", content="小鸡")
```




    '告诉我一个有趣的笑话关于小鸡。'



该模板支持任意数量的变量，包括没有变量的情况:


```python
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("告诉我一个笑话")
prompt_template.format()
```




    '告诉我一个笑话'



您可以创建自定义提示模板，以任何您想要的方式格式化提示。有关更多信息，请参阅[Prompt 模板组合](/modules/model_io/prompts/composition/)。

## `ChatPromptTemplate`

用于[聊天模型](/modules/model_io/chat)/ 的提示是一个[聊天消息](/modules/model_io/chat/message_types/)的列表。

每条聊天消息都与内容关联，并附有一个名为 `role` 的额外参数。
例如，在 OpenAI 的 [Chat Completions API](https://platform.openai.com/docs/guides/chat/introduction) 中，聊天消息可以与 AI 助手、人类或系统角色相关联。

创建一个聊天提示模板，如下所示:


```python
from langchain_core.prompts import ChatPromptTemplate

聊天模板 = ChatPromptTemplate.from_messages(
    [
        ("system", "您是一个乐于助人的 AI 机器人。您的名字是 {name}。"),
        ("human", "你好，你好吗？"),
        ("ai", "我做得很好，谢谢！"),
        ("human", "{user_input}"),
    ]
)

消息 = chat_template.format_messages(name="鲍勃", user_input="你叫什么名字？")
```

将这些格式化的消息传递给 LangChain 的 `ChatOpenAI` 聊天模型类，大致相当于直接使用 OpenAI 客户端执行以下操作:


```python
%pip 安装 openai
```


```python
from openai import OpenAI

客户端 = OpenAI()

响应 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "您是一个乐于助人的 AI 机器人。您的名字是 Bob。"},
        {"role": "user", "content": "你好，你好吗？"},
        {"role": "assistant", "content": "我做得很好，谢谢！"},
        {"role": "user", "content": "你叫什么名字？"},
    ],
)
```

`ChatPromptTemplate.from_messages` 静态方法接受多种消息表示形式，并是一种方便的方式，格式化输入为聊天模型所需的确切消息。

例如，除了使用 (type, content) 的 2-元组表示法之外，您还可以传入 `MessagePromptTemplate` 或 `BaseMessage` 的实例。


```python
from langchain.prompts import HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "您是一个乐于助人的助手，重新编写用户的文本，使其听起来更乐观。"
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)
messages = chat_template.format_messages(text="我不喜欢吃美味的东西")
print(messages)
```

    [SystemMessage(content="您是一个乐于助人的助手，重新编写用户的文本，使其听起来更乐观。"), HumanMessage(content="我不喜欢吃美味的东西")]
    

这为您构造聊天提示提供了很大的灵活性。

## 消息提示

LangChain 提供了不同类型的 `MessagePromptTemplate`。其中最常用的是 `AIMessagePromptTemplate`、`SystemMessagePromptTemplate` 和 `HumanMessagePromptTemplate`，分别用于创建 AI 消息、系统消息和用户消息。您可以在[这里](/modules/model_io/chat/message_types)阅读更多关于不同类型消息的信息。

在聊天模型支持使用任意角色的聊天消息的情况下，您可以使用 `ChatMessagePromptTemplate`，该模板允许用户指定角色名称。


```python
from langchain.prompts import ChatMessagePromptTemplate

提示 = "愿 {subject} 与你同在"

chat_message_prompt = ChatMessagePromptTemplate.from_template(
    role="绝地武士", template=prompt
)
chat_message_prompt.format(subject="原力")
```




    ChatMessage(content='愿原力与你同在', role='绝地武士')



## `MessagesPlaceholder`

LangChain 还提供 `MessagesPlaceholder`，它可以完全控制在格式化期间呈现的消息。当您不确定应该为消息提示模板使用哪种角色，或者希望在格式化期间插入一系列消息时，这可能非常有用。


```python
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

human_prompt = "用 {word_count} 个单词总结我们迄今为止的对话。"
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)

chat_prompt = ChatPromptTemplate.from_messages(
    [MessagesPlaceholder(variable_name="conversation"), human_message_template]
)
```


```python
from langchain_core.messages import AIMessage, HumanMessage

human_message = HumanMessage(content="最好的学习编程的方法是什么？")
ai_message = AIMessage(
    content="""\
1. 选择一种编程语言：决定您想要学习的编程语言。

2. 从基础知识开始：熟悉基本的编程概念，如变量、数据类型和控制结构。

3. 实践，实践，再实践：学习编程的最佳方式是通过动手实践。\
"""
)

chat_prompt.format_prompt(
    conversation=[human_message, ai_message], word_count="10"
).to_messages()
```




    [HumanMessage(content='最好的学习编程的方法是什么？'),
     AIMessage(content='1. 选择一种编程语言：决定您想要学习的编程语言。\n\n2. 从基础知识开始：熟悉基本的编程概念，如变量、数据类型和控制结构。\n\n3. 实践，实践，再实践：学习编程的最佳方式是通过动手实践'),
     HumanMessage(content='用 10 个单词总结我们迄今为止的对话。')]



消息提示模板类型的完整列表包括:

* [AIMessagePromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.AIMessagePromptTemplate.html)，用于 AI 助手消息;
* [SystemMessagePromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.SystemMessagePromptTemplate.html)，用于系统消息;
* [HumanMessagePromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.HumanMessagePromptTemplate.html)，用于用户消息;
* [ChatMessagePromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatMessagePromptTemplate.html)，用于具有任意角色的消息;
* [MessagesPlaceholder](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html)，用于容纳消息列表。



##  LCEL

`PromptTemplate` 和 `ChatPromptTemplate` 实现了[Runnable interface](/expression_language/interface)，是[LangChain Expression Language (LCEL)](/expression_language/)的基本构建块。这意味着它们支持 `invoke`, `ainvoke`, `stream`, `astream`, `batch`, `abatch`, `astream_log` 调用。

`PromptTemplate` 接受一个字典（包含提示变量）并返回一个 `StringPromptValue`。`ChatPromptTemplate` 接受一个字典并返回一个 `ChatPromptValue`。


```python
prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)

prompt_val = prompt_template.invoke({"adjective": "funny", "content": "chickens"})
prompt_val
```




    StringPromptValue(text='Tell me a funny joke about chickens.')




```python
prompt_val.to_string()
```




    'Tell me a funny joke about chickens.'




```python
prompt_val.to_messages()
```




    [HumanMessage(content='Tell me a funny joke about chickens.')]




```python
chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are a helpful assistant that re-writes the user's text to "
                "sound more upbeat."
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)

chat_val = chat_template.invoke({"text": "i dont like eating tasty things."})
```


```python
chat_val.to_messages()
```




    [SystemMessage(content="You are a helpful assistant that re-writes the user's text to sound more upbeat."),
     HumanMessage(content='i dont like eating tasty things.')]




```python
chat_val.to_string()
```




    "System: You are a helpful assistant that re-writes the user's text to sound more upbeat.\nHuman: i dont like eating tasty things."






# 快速入门

快速入门将介绍如何与语言模型进行基本操作。它将介绍两种不同类型的模型 - LLM和ChatModels。然后将介绍如何使用PromptTemplates格式化这些模型的输入，以及如何使用输出解析器处理输出。

## 模型
对于这个入门指南，我们将提供几个选项：使用类似Anthropic或OpenAI的API，或者使用通过Ollama本地开源模型。





首先，我们需要安装他们的合作伙伴软件包：

```shell
pip install langchain-openai
```

访问API需要一个API密钥，你可以通过创建账户并转到[这里](https://platform.openai.com/account/api-keys)获得密钥。一旦我们有了密钥，我们希望通过运行以下方式将其设置为环境变量：

```shell
export OPENAI_API_KEY="..."
```

然后我们可以初始化模型：

```python
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI

llm = OpenAI()
chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125")
```

如果你不想设置环境变量，也可以在初始化OpenAI LLM类时通过`api_key`命名参数直接传递密钥：

```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(api_key="...")
```



[Ollama](https://ollama.ai/)允许你在本地运行开源的大型语言模型，如Llama 2。

首先，按照[这些说明](https://github.com/jmorganca/ollama)设置和运行本地Ollama实例：

* [下载](https://ollama.ai/download)
* 通过`ollama pull llama2`获取模型

然后，确保Ollama服务器正在运行。之后，你可以执行：
```python
from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama

llm = Ollama(model="llama2")
chat_model = ChatOllama()
```
首先，我们需要导入LangChain x Anthropic软件包。

```shell
pip install langchain-anthropic
```

访问API需要一个API密钥，你可以通过在[这里](https://claude.ai/login)创建账户获得密钥。一旦我们有了密钥，我们希望通过运行以下方式将其设置为环境变量：

```shell
export ANTHROPIC_API_KEY="..."
```

然后我们可以初始化模型：

```python
from langchain_anthropic import ChatAnthropic

chat_model = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.2, max_tokens=1024)
```

如果你不想设置环境变量，也可以在初始化Anthropic Chat Model类时通过`api_key`命名参数直接传递密钥：

```python
chat_model = ChatAnthropic(api_key="...")
```



首先，我们需要安装他们的合作伙伴软件包：

```shell
pip install langchain-cohere
```

访问API需要一个API密钥，你可以通过创建账户并前往[这里](https://dashboard.cohere.com/api-keys)获得密钥。一旦我们有了密钥，我们希望通过运行以下方式将其设置为环境变量：

```shell
export COHERE_API_KEY="..."
```

然后我们可以初始化模型：

```python
from langchain_cohere import ChatCohere

chat_model = ChatCohere()
```

如果你不想设置环境变量，也可以在初始化Cohere LLM类时通过`cohere_api_key`命名参数直接传递密钥：

```python
from langchain_cohere import ChatCohere

chat_model = ChatCohere(cohere_api_key="...")
```

  /TabItem>
/Tabs>

`llm`和`chat_model`都是代表特定模型配置的对象。
你可以使用参数像`temperature`等来初始化它们，然后传递它们给其他组件。
它们之间的主要区别是它们的输入和输出模式。
LLM对象将字符串作为输入，并输出字符串。
ChatModel对象将消息列表作为输入，并输出一条消息。

当我们调用它们时，我们可以看到LLM和ChatModel之间的区别。

```python
from langchain_core.messages import HumanMessage

text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]

llm.invoke(text)
# >> Feetful of Fun

chat_model.invoke(messages)
# >> AIMessage(content="Socks O'Color")
```

LLM返回一个字符串，而ChatModel返回一条消息。

## Prompt模板

大多数LLM应用程序不会直接将用户输入传递到LLM中。通常，它们会将用户输入添加到更大的文本中，称为提示模板，该模板提供有关正在处理的特定任务的额外上下文信息。

在前面的示例中，我们传递给模型的文本包含指示生成公司名称的说明。对于我们的应用程序，如果用户只需要提供有关公司/产品描述，而不必考虑向模型提供说明，那将是很方便的。

PromptTemplates正是帮助实现这一目标的工具！
它们将所有将用户输入转换为完全格式化提示的逻辑捆绑在一起。
这可以非常简单开始 - 例如，用于生成上述字符串的提示只是：

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
prompt.format(product="colorful socks")
```

```python
What is a good name for a company that makes colorful socks?
```

然而，使用这些的优势不止一点。
你可以“局部”处理变量 - 例如，你可以一次只格式化一些变量。
你可以将它们组合在一起，轻松地将不同模板组合成单个提示。
有关这些功能的更多解释，请查看有关提示的部分以获取更多细节。

`PromptTemplate`还可用于生成消息列表。
在这种情况下，提示不仅包含有关内容的信息，还包括每条消息（其作用，其在列表中的位置等）。
通常出现的情况是`ChatPromptTemplate`是`ChatMessageTemplates`列表。
每个`ChatMessageTemplate`包含有关如何格式化该`ChatMessage`的说明 - 其作用，以及其内容。
让我们在下面看一下这个：

```python
from langchain.prompts.chat import ChatPromptTemplate

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")
```

```pycon
[
    SystemMessage(content="You are a helpful assistant that translates English to French.", additional_kwargs={}),
    HumanMessage(content="I love programming.")
]
```


ChatPrompt模板也可以以其他方式构建 - 有关更多详细信息，请查看有关提示的部分。

## 输出解析器

`OutputParser`将语言模型的原始输出转换为可在下游使用的格式。
`OutputParser`的主要类型包括：

- 将从`LLM`中的文本转换为结构化信息（例如JSON）
- 将`ChatMessage`转换为字符串
- 将除消息之外的返回信息（例如OpenAI函数调用）转换为字符串。

有关完整信息，请查看有关输出解析器的部分。

在这个入门指南中，我们使用简单的解析器来解析逗号分隔的值列表。

```python
from langchain.output_parsers import CommaSeparatedListOutputParser

output_parser = CommaSeparatedListOutputParser()
output_parser.parse("hi, bye")
# >> ['hi', 'bye']
```

## 与LCEL合成

现在我们可以将所有这些组合成一个链条。
该链将获取输入变量，将其传递给提示模板以创建提示，将提示传递给语言模型，然后通过一个（可选的）输出解析器来处理输出。
这是将一组模块化逻辑捆绑在一起的便捷方法。
让我们看看它是如何工作的！

```python
template = "Generate a list of 5 {text}.\n\n{format_instructions}"

chat_prompt = ChatPromptTemplate.from_template(template)
chat_prompt = chat_prompt.partial(format_instructions=output_parser.get_format_instructions())
chain = chat_prompt | chat_model | output_parser
chain.invoke({"text": "colors"})
# >> ['red', 'blue', 'green', 'yellow', 'orange']
```

请注意，我们使用`|`语法将这些组件连接在一起。
这种`|`语法由LangChain表达式语言（LCEL）提供支持，并依赖于所有这些对象实现的通用`Runnable`接口。
要了解有关LCEL的更多信息，请阅读此处的文档。

## 结论

这就是关于如何开始使用提示，模型和输出解析器的全部内容！这只是表面，还有更多内容等着你去了解。欲了解更多信息，请查看：

- [提示部分](/modules/model_io/prompts/)以获取有关如何使用提示模板的信息
- [LLM部分](/modules/model_io/llms/)以获取有关LLM接口的更多信息
- [ChatModel部分](/modules/model_io/chat/)以获取有关ChatModel接口的更多信息
- [输出解析器部分](/modules/model_io/output_parsers/)以了解有关不同类型输出解析器的信息。