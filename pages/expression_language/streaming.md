# 使用 LangChain 进行流式处理

流式处理对于让基于LLMs的应用程序对最终用户产生响应至关重要。

重要的LangChain原语，如LLMs、解析器、提示器、检索器和代理，实现了LangChain [Runnable Interface](/expression_language/interface)。

该接口提供了两种一般的流内容方法：

1. sync `stream` 和 async `astream`：一种**默认实现**，从链中流式传输**最终输出**。
2. async `astream_events` 和 async `astream_log`：这些方法提供了一种从链中流式传输**中间步骤**和**最终输出**的方式。

让我们来看看这两种方法，并尝试理解如何使用它们。🥷

## 使用 Stream

所有的 `Runnable` 对象都实现了一个名为 `stream` 的同步方法和一个名为 `astream` 的异步变体。

这些方法的设计目的是将最终输出以块的形式进行流式传输，尽快返回每个块。

只有当程序中的所有步骤都知道如何处理一个**输入流**时，才能进行流式传输；也就是说，逐个处理输入块，并产生相应的输出块。

这种处理的复杂程度可以有所不同，从简单的任务，比如发射LLM产生的令牌，到更具挑战性的任务，比如在整个JSON完成之前流式传输JSON结果的部分。

开始探索流式处理的最佳方式是从LLMs应用中最重要的组件开始——LLMs本身！

### LLMs 和 Chat 模型

大型语言模型及其聊天变体是基于LLM的应用程序的主要瓶颈。🙊

大型语言模型可能需要**几秒钟**来生成对查询的完整响应。这比应用程序对最终用户的响应时间**约为200-300毫秒**的阈值要慢得多。

使应用程序更具响应性的关键策略是显示中间进度；也就是说，逐个令牌地从模型流式传输输出。

我们将展示使用 [Anthropic](/integrations/platforms/anthropic) 中的聊天模型来进行流式处理的示例。要使用该模型，您需要安装 `langchain-anthropic` 包。您可以使用以下命令来完成安装：

```python
pip install -qU langchain-anthropic
```

```python
# 显示了使用 Anthropic 的示例，但您可以使用您喜欢的聊天模型！
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic()

chunks = []
async for chunk in model.astream("你好，请告诉我一些关于你自己的东西"):
    chunks.append(chunk)
    print(chunk.content, end="|", flush=True)
```

    你好|!| 我的| 名字| 是| Claude|.| 我是|由|Anthropic|创建的|AI|助手，力求|友好|、|无害|和|诚实|。||

让我们检查其中一块的内容

```python
chunks[0]
```

输出结果如下：

```python
AIMessageChunk(content=' 你好')
```

我们得到了一个叫做 `AIMessageChunk` 的内容块。该块表示 `AIMessage` 的一部分。

设计上，消息块是可累加的——只需将它们加在一起，就可以得到到目前为止的响应状态！

```python
chunks[0] + chunks[1] + chunks[2] + chunks[3] + chunks[4]
```

输出结果如下：

```python
AIMessageChunk(content=' 你好！我的名字是')
```

### Chains

实际上，几乎所有的LLM应用程序都涉及多个步骤，而不仅仅是调用一个语言模型。

让我们构建一个简单的链，使用 `LangChain Expression Language` (`LCEL`) 来组合一个提示器、模型和解析器，并验证流式处理的工作方式。

我们将使用 `StrOutputParser` 来解析模型的输出。这是一个简单的解析器，从 `AIMessageChunk` 中提取 `content` 字段，给出了模型返回的令牌。

:::{.callout-tip}
LCEL 是一种*声明性*的方法，通过将不同的 LangChain 原语链接在一起来指定一个 "程序"。使用 LCEL 创建的链可以自动实现 `stream` 和 `astream`，实现最终输出的流式传输。事实上，使用 LCEL 创建的链实现了整个标准的可运行接口。
:::

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("告诉我一个关于 {topic} 的笑话")
parser = StrOutputParser()
chain = prompt | model | parser

async for chunk in chain.astream({"topic": "鹦鹉"}):
    print(chunk, end="|", flush=True)
```

输出结果如下：

```python
这里有一个关于鹦鹉的傻笑话：|
    
什么样的老师给出很好的建议？正确答案是：一位专业的老师！||
```

您可能会注意到上面的 `parser` 实际上没有阻塞模型的流式输出，而是逐个处理每个块。许多 [LCEL元语](/expression_language/primitives) 也支持这种转换式的流式传递，这在构建应用程序时非常方便。

某些可运行对象，例如[prompt模板](/modules/model_io/prompts)和[chat模型](/modules/model_io/chat)，无法处理单个块，而是将所有先前的步骤聚合起来。这将中断流式传输过程。可以[设计函数返回生成器](/expression_language/primitives/functions#streaming)，

:::{.callout-note}
如果上述功能与您构建的内容无关，您不需要使用 `LangChain 表达式语言` 来使用 LangChain，而可以依靠**命令式**编程方法，对每个组件逐个调用 `invoke`、`batch` 或 `stream`，将结果分配给变量，然后根据需要在下游使用它们。

如果这符合您的需求，那么我们就没问题👌！
:::

### 使用输入流进行工作

如果您希望在产生输出的同时流式传输 JSON，该怎么办呢？

如果您依赖于 `json.loads` 来解析部分 JSON，那么解析会失败，因为部分 JSON 不是有效的 JSON。

您可能会完全不知所措，并声称无法流式传输JSON。

实际上，有一种方法可以做到——解析器需要在**输入流**上操作，并尝试将部分 JSON "自动完成" 为有效状态。

让我们看看这样的解析器是如何工作的。

```python
from langchain_core.output_parsers import JsonOutputParser

chain = (
    model | JsonOutputParser()
)  # 由于较旧版本的 Langchain 中存在的 bug，JsonOutputParser 未从某些模型中流式传输结果
async for text in chain.astream(
    '以 JSON 格式输出一个包含法国、西班牙和日本以及它们的人口的国家列表。使用一个 key 为 "countries"、包含一个国家列表的字典。每个国家应该具有 "name" 和 "population" key'
):
    print(text, flush=True)
```

输出结果如下：

```python
{}
{'countries': []}
{'countries': [{}]}
{'countries': [{'name': ''}]}
{'countries': [{'name': '法国'}]}
{'countries': [{'name': '法国', 'population': 67}]}
{'countries': [{'name': '法国', 'population': 6739}]}
{'countries': [{'name': '法国', 'population': 673915}]}
{'countries': [{'name': '法国', 'population': 67391582}]}
{'countries': [{'name': '法国', 'population': 67391582}, {}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': ''}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西'}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙'}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙', 'population': 46}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙', 'population': 4675}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙', 'population': 467547}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙', 'population': 46754778}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙', 'population': 46754778}, {}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙', 'population': 46754778}, {'name': ''}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙', 'population': 46754778}, {'name': '日本'}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙', 'population': 46754778}, {'name': '日本', 'population': 12}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙', 'population': 46754778}, {'name': '日本', 'population': 12647}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙', 'population': 46754778}, {'name': '日本', 'population': 1264764}]}
{'countries': [{'name': '法国', 'population': 67391582}, {'name': '西班牙', 'population': 46754778}, {'name': '日本', 'population': 126476461}]}
```

现在，让我们**中断**流式传输。我们将使用之前的示例，并在最后附加一个提取函数，该函数会从最终的 JSON 中提取国家名称。

:::{.callout-warning}
链中的任何步骤，如果只处理**最终输入**而不是**输入流**，都有可能中断 `stream` 或 `astream` 的流式处理功能。
:::

:::{.callout-tip}
稍后，我们将讨论 `astream_events` API，该 API 可以从中间步骤流式传输结果。即使链中包含仅处理**最终输入**的步骤，该API也会流式传输中间步骤的结果。
:::

```python
from langchain_core.output_parsers import (
    JsonOutputParser,
)


# 一个只处理最终输入而不处理输入流的函数
def _extract_country_names(inputs):
    """A function that does not operates on input streams and breaks streaming."""
    if not isinstance(inputs, dict):
        return ""

    if "countries" not in inputs:
        return ""

    countries = inputs["countries"]

    if not isinstance(countries, list):
        return ""

    country_names = [
        country.get("name") for country in countries if isinstance(country, dict)
    ]
    return country_names


chain = model | JsonOutputParser() | _extract_country_names

async for text in chain.astream(
    '以 JSON 格式输出一个包含法国、西班牙和日本以及它们的人口的国家列表。使用一个 key 为 "countries"、包含一个国家列表的字典。每个国家应该具有 "name" 和 "population" key'
):
    print(text, end="|", flush=True)
```

输出结果如下：

```python
['法国', '西班牙', '日本']|
```

【完】#### 生成器函数

使用一个可以在**输入流**上操作的生成器函数来修复流式处理。

:::{.callout-tip}
生成器函数（使用`yield`的函数）允许编写操作**输入流**的代码。
:::


```python
from langchain_core.output_parsers import JsonOutputParser


async def _extract_country_names_streaming(input_stream):
    """在输入流上操作的函数。"""
    country_names_so_far = set()

    async for input in input_stream:
        if not isinstance(input, dict):
            continue

        if "countries" not in input:
            continue

        countries = input["countries"]

        if not isinstance(countries, list):
            continue

        for country in countries:
            name = country.get("name")
            if not name:
                continue
            if name not in country_names_so_far:
                yield name
                country_names_so_far.add(name)


chain = model | JsonOutputParser() | _extract_country_names_streaming

async for text in chain.astream(
    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`'
):
    print(text, end="|", flush=True)
```

    France|Sp|Spain|Japan|

:::{.callout-note}
由于上面的代码依赖于JSON自动完成，您可能会看到部分国家名称（例如`Sp`和`Spain`），这不是我们希望得到的提取结果！

我们关注的是流式处理的概念，而不一定是链的结果。
:::

### 非流式组件

一些内置组件（如Retrievers）不提供任何`streaming`。如果我们尝试对它们进行`streaming`会发生什么？ 🤨


```python
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

vectorstore = FAISS.from_texts(
    ["harrison worked at kensho", "harrison likes spicy food"],
    embedding=OpenAIEmbeddings(),
)
retriever = vectorstore.as_retriever()

chunks = [chunk for chunk in retriever.stream("where did harrison work?")]
chunks
```




    [[Document(page_content='harrison worked at kensho'),
      Document(page_content='harrison likes spicy food')]]



流仅产生了该组件的最终结果。

这很好 🥹！并非所有组件都必须实现流式处理 - 在某些情况下，流式处理要么是不必要的，要么很困难，要么根本没有意义。

:::{.callout-tip}
使用非流式组件构建的LCEL链，在很多情况下仍然能够流式处理，流式处理部分输出从链中的最后一个非流式步骤后开始。
:::


```python
retrieval_chain = (
    {
        "context": retriever.with_config(run_name="Docs"),
        "question": RunnablePassthrough(),
    }
    | prompt
    | model
    | StrOutputParser()
)
```


```python
for chunk in retrieval_chain.stream(
    "Where did harrison work? " "Write 3 made up sentences about this place."
):
    print(chunk, end="|", flush=True)
```

     Based| on| the| given| context|,| the| only| information| provided| about| where| Harrison| worked| is| that| he| worked| at| Ken|sh|o|.| Since| there| are| no| other| details| provided| about| Ken|sh|o|,| I| do| not| have| enough| information| to| write| 3| additional| made| up| sentences| about| this| place|.| I| can| only| state| that| Harrison| worked| at| Ken|sh|o|.||

现在我们已经了解了`stream`和`astream`的工作原理，让我们进入流事件的世界。🏞️

## 使用流事件

事件流是一个**beta**API。该API可能根据反馈意见进行一些更改。

:::{.callout-note}
在langchain-core **0.1.14**中引入。
:::


```python
import langchain_core

langchain_core.__version__
```




    '0.1.18'



为了使`astream_events` API正常工作：

* 尽可能地在代码中使用`async`（例如，async工具等）
* 如果定义自定义函数/可运行对象，请传播回调函数
* 每当在LLM上使用不带LCEL的可运行对象时，请确保在LLM上调用`.astream()`而不是`.ainvoke`来强制LLM流式处理标记。
* 如果有任何不符合预期的情况，请告诉我们！ :)

### 事件参考

下面是显示各种可运行对象可能产生的一些事件的参考表格。

:::{.callout-note}
当流式处理正确实现时，对可运行对象的输入在完全消耗输入流之前将不会为人所知。这意味着`inputs`通常只会包括`end`事件而不是`start`事件。
:::


| 事件               | 名称              | 块                             | 输入                                           | 输出                                          |
|--------------------|-------------------|---------------------------------|-----------------------------------------------|-------------------------------------------------|
| on_chat_model_start  | [model name]     |                                 | {"messages": [[SystemMessage, HumanMessage]]} |                                                 |
| on_chat_model_stream | [model name]     | AIMessageChunk(content="hello") |                                               |                                                 |
| on_chat_model_end    | [model name]     |                                 | {"messages": [[SystemMessage, HumanMessage]]} | {"generations": [...], "llm_output": None, ...} |
| on_llm_start         | [model name]     |                                 | {'input': 'hello'}                            |                                                 |
| on_llm_stream        | [model name]     | 'Hello'                         |                                               |                                                 |
| on_llm_end           | [model name]     |                                 | 'Hello human!'                                |
| on_chain_start       | format_docs      |                                 |                                               |                                                 |
| on_chain_stream      | format_docs      | "hello world!, goodbye world!"  |                                               |                                                 |
| on_chain_end         | format_docs      |                                 | [Document(...)]                               | "hello world!, goodbye world!"                  |
| on_tool_start        | some_tool        |                                 | {"x": 1, "y": "2"}                            |                                                 |
| on_tool_stream       | some_tool        | {"x": 1, "y": "2"}              |                                               |                                                 |
| on_tool_end          | some_tool        |                                 |                                               | {"x": 1, "y": "2"}                              |
| on_retriever_start   | [retriever name] |                                 | {"query": "hello"}                            |                                                 |
| on_retriever_chunk   | [retriever name] | {documents: [...]}              |                                               |                                                 |
| on_retriever_end     | [retriever name] |                                 | {"query": "hello"}                            | {documents: [...]}                              |
| on_prompt_start      | [template_name]  |                                 | {"question": "hello"}                         |                                                 |
| on_prompt_end        | [template_name]  |                                 | {"question": "hello"}                         | ChatPromptValue(messages: [SystemMessage, ...]) |

### Chat Model

让我们首先查看聊天模型生成的事件。


```python
events = []
async for event in model.astream_events("hello", version="v1"):
    events.append(event)
```

    /home/eugene/src/langchain/libs/core/langchain_core/_api/beta_decorator.py:86: LangChainBetaWarning: This API is in beta and may change in the future.
      warn_beta(
    

:::{.callout-note}

嘿，API中的那个有趣的version="v1"参数是什么？！ 😾

这是一个**beta API**，我们几乎肯定会对其进行一些更改。

这个version参数将使我们最小化对您的代码进行的此类重大更改。

简而言之，我们现在在让您烦恼，以免以后再烦恼。
:::

让我们看看一些开始事件和一些结束事件。


```python
events[:3]
```




    [{'event': 'on_chat_model_start',
      'run_id': '555843ed-3d24-4774-af25-fbf030d5e8c4',
      'name': 'ChatAnthropic',
      'tags': [],
      'metadata': {},
      'data': {'input': 'hello'}},
     {'event': 'on_chat_model_stream',
      'run_id': '555843ed-3d24-4774-af25-fbf030d5e8c4',
      'tags': [],
      'metadata': {},
      'name': 'ChatAnthropic',
      'data': {'chunk': AIMessageChunk(content=' Hello')}},
     {'event': 'on_chat_model_stream',
      'run_id': '555843ed-3d24-4774-af25-fbf030d5e8c4',
      'tags': [],
      'metadata': {},
      'name': 'ChatAnthropic',
      'data': {'chunk': AIMessageChunk(content='!')}}]




```python
events[-2:]
```




    [{'event': 'on_chat_model_stream',
      'run_id': '555843ed-3d24-4774-af25-fbf030d5e8c4',
      'tags': [],
      'metadata': {},
      'name': 'ChatAnthropic',
      'data': {'chunk': AIMessageChunk(content='')}},
     {'event': 'on_chat_model_end',
      'name': 'ChatAnthropic',
      'run_id': '555843ed-3d24-4774-af25-fbf030d5e8c4',
      'tags': [],
      'metadata': {},
      'data': {'output': AIMessageChunk(content=' Hello!')}}]



### Chain

让我们重新审视一下解析流式JSON的示例链以探索流式事件API。


```python
chain = (
    model | JsonOutputParser()
)  # 由于旧版本的Langchain中存在错误，JsonOutputParser无法从某些模型中流式传输结果

events = [
    event
    async for event in chain.astream_events(
        'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`',
        version="v1",
    )
]
```

如果您检查前几个事件，您会注意到有**3**个不同的启动事件，而不是**2**个启动事件。

这三个启动事件对应于：

1. 链（模型 + 解析器）
2. 模型
3. 解析器


```python
events[:3]
```




    [{'event': 'on_chain_start',
      'run_id': 'b1074bff-2a17-458b-9e7b-625211710df4',
      'name': 'RunnableSequence',
      'tags': [],
      'metadata': {},
      'data': {'input': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`'}},
     {'event': 'on_chat_model_start',
      'name': 'ChatAnthropic',
      'run_id': '6072be59-1f43-4f1c-9470-3b92e8406a99',
      'tags': ['seq:step:1'],
      'metadata': {},
      'data': {'input': {'messages': [[HumanMessage(content='output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`')]]}}},
     {'event': 'on_parser_start',
      'name': 'JsonOutputParser',
      'run_id': 'bf978194-0eda-4494-ad15-3a5bfe69cd59',
      'tags': ['seq:step:2'],
      'metadata': {},
      'data': {}}]



如果您查看最后3个事件，您认为会看到什么？中间的事件呢？

让我们使用此API从模型和解析器中获取流式事件。我们忽略链的启动事件、结束事件和事件。


```python
num_events = 0

async for event in chain.astream_events(
    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`',
    version="v1",
):
    kind = event["event"]
    if kind == "on_chat_model_stream":
        print(
            f"Chat model chunk: {repr(event['data']['chunk'].content)}",
            flush=True,
        )
    if kind == "on_parser_stream":
        print(f"Parser chunk: {event['data']['chunk']}", flush=True)
    num_events += 1
    if num_events > 30:
        # 截断输出
        print("...")
        break
```

    Chat model chunk: ' Here'
    Chat model chunk: ' is'
    Chat model chunk: ' the'
    Chat model chunk: ' JSON'
    Chat model chunk: ' with'
    Chat model chunk: ' the'
    Chat model chunk: ' requested'
    Chat model chunk: ' countries'
    Chat model chunk: ' and'
    Chat model chunk: ' their'
    Chat model chunk: ' populations'
    Chat model chunk: ':'
    Chat model chunk: '\n\n```'
    Chat model chunk: 'json'
    Parser chunk: {}
    Chat model chunk: '\n{'
    Chat model chunk: '\n '
    Chat model chunk: ' "'
    Chat model chunk: 'countries'
    Chat model chunk: '":'
    Parser chunk: {'countries': []}
    Chat model chunk: ' ['
    Chat model chunk: '\n   '
    Parser chunk: {'countries': [{}]}
    Chat model chunk: ' {'
    ...
    

由于模型和解析器都支持流式传输，我们实时看到了来自这两个组件的流式事件！挺酷的，不是吗？🦜

### 过滤事件

由于此API产生的事件非常多，因此能够对事件进行过滤非常有用。

您可以按组件`name`、组件`tags`或组件`type`进行过滤。

#### 按名称


```python
chain = model.with_config({"run_name": "model"}) | JsonOutputParser().with_config(
    {"run_name": "my_parser"}
)

max_events = 0
async for event in chain.astream_events(
    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`',
    version="v1",
    include_names=["my_parser"],
):
    print(event)
    max_events += 1
    if max_events > 10:
        # 截断输出
        print("...")
        break
```

    {'event': 'on_parser_start', 'name': 'my_parser', 'run_id': 'f2ac1d1c-e14a-45fc-8990-e5c24e707299', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {}}
    {'event': 'on_parser_stream', 'name': 'my_parser', 'run_id': 'f2ac1d1c-e14a-45fc-8990-e5c24e707299', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {}}}
    {'event': 'on_parser_stream', 'name': 'my_parser', 'run_id': 'f2ac1d1c-e14a-45fc-8990-e5c24e707299', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': []}}}
    {'event': 'on_parser_stream', 'name': 'my_parser', 'run_id': 'f2ac1d1c-e14a-45fc-8990-e5c24e707299', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{}]}}}
    {'event': 'on_parser_stream', 'name': 'my_parser', 'run_id': 'f2ac1d1c-e14a-45fc-8990-e5c24e707299', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': ''}]}}}
    {'event': 'on_parser_stream', 'name': 'my_parser', 'run_id': 'f2ac1d1c-e14a-45fc-8990-e5c24e707299', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France'}]}}}
    {'event': 'on_parser_stream', 'name': 'my_parser', 'run_id': 'f2ac1d1c-e14a-45fc-8990-e5c24e707299', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France', 'population': 67}]}}}
    {'event': 'on_parser_stream', 'name': 'my_parser', 'run_id': 'f2ac1d1c-e14a-45fc-8990-e5c24e707299', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France', 'population': 6739}]}}}
    {'event': 'on_parser_stream', 'name': 'my_parser', 'run_id': 'f2ac1d1c-e14a-45fc-8990-e5c24e707299', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France', 'population': 673915}]}}}
    {'event': 'on_parser_stream', 'name': 'my_parser', 'run_id': 'f2ac1d1c-e14a-45fc-8990-e5c24e707299', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France', 'population': 67391582}]}}}
    {'event': 'on_parser_stream', 'name': 'my_parser', 'run_id': 'f2ac1d1c-e14a-45fc-8990-e5c24e707299', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'France', 'population': 67391582}, {}]}}}
    ...
    

#### 按类型


```python
chain = model.with_config({"run_name": "model"}) | JsonOutputParser().with_config(
    {"run_name": "my_parser"}
)

max_events = 0
async for event in chain.astream_events(
    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`',
    version="v1",
    include_types=["chat_model"],
):
    print(event)
    max_events += 1
    if max_events > 10:
        # 截断输出
        print("...")
        break
```

    {'event': 'on_chat_model_start', 'name': 'model', 'run_id': '98a6e192-8159-460c-ba73-6dfc921e3777', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'input': {'messages': [[HumanMessage(content='output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`')]]}}}
    {'event': 'on_chat_model_stream', 'name': 'model', 'run_id': '98a6e192-8159-460c-ba73-6dfc921e3777', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' Here')}}
    {'event': 'on_chat_model_stream', 'name': 'model', 'run_id': '98a6e192-8159-460c-ba73-6dfc921e3777', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' is')}}
    {'event': 'on_chat_model_stream', 'name': 'model', 'run_id': '98a6e192-8159-460c-ba73-6dfc921e3777', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' the')}}
    {'event': 'on_chat_model_stream', 'name': 'model', 'run_id': '98a6e192-8159-460c-ba73-6dfc921e3777', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' JSON')}}
    {'event': 'on_chat_model_stream', 'name': 'model', 'run_id': '98a6e192-8159-460c-ba73-6dfc921e3777', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' with')}}
    {'event': 'on_chat_model_stream', 'name': 'model', 'run_id': '98a6e192-8159-460c-ba73-6dfc921e3777', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' the')}}
    {'event': 'on_chat_model_stream', 'name': 'model', 'run_id': '98a6e192-8159-460c-ba73-6dfc921e3777', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' requested')}}
    {'event': 'on_chat_model_stream', 'name': 'model', 'run_id': '98a6e192-8159-460c-ba73-6dfc921e3777', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' countries')}}
    {'event': 'on_chat_model_stream', 'name': 'model', 'run_id': '98a6e192-8159-460c-ba73-6dfc921e3777', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' and')}}
    {'event': 'on_chat_model_stream', 'name': 'model', 'run_id': '98a6e192-8159-460c-ba73-6dfc921e3777', 'tags': ['seq:step:1'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' their')}}
    ...
    

#### 按标签

:::{.callout-caution}

标签会被给定可运行组件的子组件继承。

如果您使用标签进行过滤，请确保这正是您想要的。
:::


```python
chain = (model | JsonOutputParser()).with_config({"tags": ["my_chain"]})

max_events = 0
async for event in chain.astream_events(
    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`',
    version="v1",
    include_tags=["my_chain"],
):
    print(event)
    max_events += 1
    if max_events > 10:
------
                你的答案是:# Truncate output
print("...")
break


```
```
{'event': 'on_chain_start', 'run_id': '190875f3-3fb7-49ad-9b6e-f49da22f3e49', 'name': 'RunnableSequence', 'tags': ['my_chain'], 'metadata': {}, 'data': {'input': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`'}}
{'event': 'on_chat_model_start', 'name': 'ChatAnthropic', 'run_id': 'ff58f732-b494-4ff9-852a-783d42f4455d', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {}, 'data': {'input': {'messages': [[HumanMessage(content='output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of "countries" which contains a list of countries. Each country should have the key `name` and `population`')]]}}}
{'event': 'on_parser_start', 'name': 'JsonOutputParser', 'run_id': '3b5e4ca1-40fe-4a02-9a19-ba2a43a6115c', 'tags': ['seq:step:2', 'my_chain'], 'metadata': {}, 'data': {}}
{'event': 'on_chat_model_stream', 'name': 'ChatAnthropic', 'run_id': 'ff58f732-b494-4ff9-852a-783d42f4455d', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' Here')}}
{'event': 'on_chat_model_stream', 'name': 'ChatAnthropic', 'run_id': 'ff58f732-b494-4ff9-852a-783d42f4455d', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' is')}}
{'event': 'on_chat_model_stream', 'name': 'ChatAnthropic', 'run_id': 'ff58f732-b494-4ff9-852a-783d42f4455d', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' the')}}
{'event': 'on_chat_model_stream', 'name': 'ChatAnthropic', 'run_id': 'ff58f732-b494-4ff9-852a-783d42f4455d', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' JSON')}}
{'event': 'on_chat_model_stream', 'name': 'ChatAnthropic', 'run_id': 'ff58f732-b494-4ff9-852a-783d42f4455d', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' with')}}
{'event': 'on_chat_model_stream', 'name': 'ChatAnthropic', 'run_id': 'ff58f732-b494-4ff9-852a-783d42f4455d', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' the')}}
{'event': 'on_chat_model_stream', 'name': 'ChatAnthropic', 'run_id': 'ff58f732-b494-4ff9-852a-783d42f4455d', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' requested')}}
{'event': 'on_chat_model_stream', 'name': 'ChatAnthropic', 'run_id': 'ff58f732-b494-4ff9-852a-783d42f4455d', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {}, 'data': {'chunk': AIMessageChunk(content=' countries')}}
...# 我提供的mdx文档的内容需要翻译，只要翻译md语法中的标题、段落和列表的内容，驼峰和下划线单词不必翻译，请保留md语法标点符号，你翻译完后对原内容进行替换，将结果返回给我。mdx文档是:------

{'event': 'on_chain_start', 'run_id': '4fe56c7b-6982-4999-a42d-79ba56151176', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'data': {'input': '1234'}}
{'event': 'on_chain_start', 'name': 'reverse_word', 'run_id': '335fe781-8944-4464-8d2e-81f61d1f85f5', 'tags': [], 'metadata': {}, 'data': {'input': '1234'}}
{'event': 'on_chain_end', 'name': 'reverse_word', 'run_id': '335fe781-8944-4464-8d2e-81f61d1f85f5', 'tags': [], 'metadata': {}, 'data': {'input': '1234', 'output': '4321'}}
{'event': 'on_chain_stream', 'run_id': '4fe56c7b-6982-4999-a42d-79ba56151176', 'tags': [], 'metadata': {}, 'name': 'reverse_and_double', 'data': {'chunk': '43214321'}}
{'event': 'on_chain_end', 'name': 'reverse_and_double', 'run_id': '4fe56c7b-6982-4999-a42d-79ba56151176', 'tags': [], 'metadata': {}, 'data': {'output': '43214321'}}


And with the @chain decorator:
```

```python
from langchain_core.runnables import chain


@chain
async def reverse_and_double(word: str):
    return await reverse_word.ainvoke(word) * 2


await reverse_and_double.ainvoke("1234")

async for event in reverse_and_double.astream_events("1234", version="v1"):
    print(event)
```
```
{'event': 'on_chain_start', 'run_id': '7485eedb-1854-429c-a2f8-03d01452daef', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'data': {'input': '1234'}}
{'event': 'on_chain_start', 'name': 'reverse_word', 'run_id': 'e7cddab2-9b95-4e80-abaf-4b2429117835', 'tags': [], 'metadata': {}, 'data': {'input': '1234'}}
{'event': 'on_chain_end', 'name': 'reverse_word', 'run_id': 'e7cddab2-9b95-4e80-abaf-4b2429117835', 'tags': [], 'metadata': {}, 'data': {'input': '1234', 'output': '4321'}}
{'event': 'on_chain_stream', 'run_id': '7485eedb-1854-429c-a2f8-03d01452daef', 'tags': [], 'metadata': {}, 'name': 'reverse_and_double', 'data': {'chunk': '43214321'}}
{'event': 'on_chain_end', 'name': 'reverse_and_double', 'run_id': '7485eedb-1854-429c-a2f8-03d01452daef', 'tags': [], 'metadata': {}, 'data': {'output': '43214321'}}
```
