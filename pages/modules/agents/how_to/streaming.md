# 流式输出

流式输出是LLM应用的重要用户体验考虑因素，代理也不例外。与代理一起流媒体会更加复杂，因为你不仅想要流式传输最终答案的令牌，还可能希望流式传输代理所采取的中间步骤。

在这个笔记本中，我们将介绍用于流式传输的`stream/astream`和`astream_events`。

我们的代理将使用工具API进行工具调用：

1. `where_cat_is_hiding`: 返回猫藏在哪里的位置
2. `get_items`: 列出可以在特定地方找到的物品

这些工具将允许我们在一个更有趣的情况下探索流式传输，代理将不得不使用两者来回答一些问题（例如，回答问题`猫藏在哪里的物品？`）。

准备好了吗？🏎️


```python
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.prompts import ChatPromptTemplate
from langchain.tools import tool
from langchain_core.callbacks import Callbacks
from langchain_openai import ChatOpenAI
```

## 创建模型

**注意** 我们在LLM上设置了`streaming=True`。这将允许我们使用`astream_events` API从代理中流式传输令牌。这对于LangChain的旧版本是必需的。


```python
model = ChatOpenAI(temperature=0, streaming=True)
```

## 工具

我们定义了两个依赖于聊天模型生成输出的工具！


```python
import random


@tool
async def where_cat_is_hiding() -> str:
    """猫现在躲在哪里？"""
    return random.choice(["床下", "架子上"])


@tool
async def get_items(place: str) -> str:
    """使用此工具查找给定地方有哪些物品。"""
    if "床" in place:  # 对于床下
        return "袜子、鞋子和灰尘兔"
    if "架子" in place:  # 对于'架子'
        return "书、铅笔和图片"
    else:  # 如果代理决定询问不同的地方
        return "猫零食"
```


```python
await where_cat_is_hiding.ainvoke({})
```




    '架子上'




```python
await get_items.ainvoke({"place": "架子"})
```




    '书、铅笔和图片'



## 初始化代理

这里，我们将初始化一个OpenAI工具代理。

**注意** 请注意，我们使用`"run_name"="Agent"`将名称`Agent`与我们的代理关联起来。我们稍后将在`astream_events` API中使用这一事实。


```python
# 获取要使用的提示 - 您可以修改这个！
prompt = hub.pull("hwchase17/openai-tools-agent")
# 打印(prompt.messages) -- 查看提示
tools = [get_items, where_cat_is_hiding]
agent = create_openai_tools_agent(
    model.with_config({"tags": ["agent_llm"]}), tools, prompt
)
agent_executor = AgentExecutor(agent=agent, tools=tools).with_config(
    {"run_name": "Agent"}
)
```

## 流传中间步骤

我们将使用AgentExecutor的`.stream`方法来流式传输代理的中间步骤。

`.stream`的输出在操作和观察对之间交替，最终以代理是否达到目标为结束。

它看起来像这样：

1. 操作输出
2. 观察输出
3. 操作输出
4. 观察输出

**...（继续直到达到目标）...**

然后，如果达到最终目标，代理将输出**最终答案**。


这些输出的内容摘要如下：

| 输出              | 内容                                                                                       |
|----------------------|--------------------------------------------------------------------------------------|
| **操作**     | `actions` `AgentAction`或子类，与操作调用对应的聊天消息                                                                         |
| **观察**     | `steps`到目前为止代理的历史记录，包括当前操作及其观察，`messages`具有函数调用结果的聊天消息（即观察） |
| **最终答案**  | `output` `AgentFinish`，具有最终输出的聊天消息|


```python
# 注意：我们使用`pprint`仅打印到深度1，这样可以更容易地看到高层次的输出，然后再进行挖掘。
import pprint

chunks = []

async for chunk in agent_executor.astream(
    {"input": "猫躲在哪里有哪些物品？"}
):
    chunks.append(chunk)
    print("------")
    pprint.pprint(chunk, depth=1)
```

    ------
    {'actions': [...], 'messages': [...]}
    ------
    {'messages': [...], 'steps': [...]}
    ------
    {'actions': [...], 'messages': [...]}
    ------
    {'messages': [...], 'steps': [...]}
    ------
    {'messages': [...],
     'output': '猫藏在架子上的物品是书、铅笔和图片。'}
    

### 使用消息

您可以访问输出中的基础`消息`。在处理聊天应用程序时，使用消息可能会很好，因为一切都是消息！


```python
chunks[0]["actions"]
```




    [OpenAIToolAgentAction(tool='where_cat_is_hiding', tool_input={}, log='\n正在调用：使用`{}`查找猫的藏身之处\n\n\n', message_log=[AIMessageChunk(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_pKy4OLcBx6pR6k3GHBOlH68r', 'function': {'arguments': '{}', 'name': 'where_cat_is_hiding'}, 'type': 'function'}]})], tool_call_id='call_pKy4OLcBx6pR6k3GHBOlH68r')]




```python
for chunk in chunks:
    print(chunk["messages"])
```

    [AIMessageChunk(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_pKy4OLcBx6pR6k3GHBOlH68r', 'function': {'arguments': '{}', 'name': 'where_cat_is_hiding'}, 'type': 'function'}]})]
    [FunctionMessage(content='架子上', name='where_cat_is_hiding')]
    [AIMessageChunk(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_qZTz1mRfCCXT18SUy0E07eS4', 'function': {'arguments': '{\n  "place": "架子"\n}', 'name': 'get_items'}, 'type': 'function'}]})]
    [FunctionMessage(content='书、铅笔和图片', name='get_items')]
    [AIMessage(content='猫藏在架子上的物品是书、铅笔和图片。')]
    

此外，它们包含完整的日志信息（`actions`和`steps`），可能更容易在渲染目的中处理。

### 使用AgentAction/Observation

输出还包含更丰富结构化信息，位于`actions`和`steps`内部，这在某些情况下可能很有用，但也可能更难解析。

**注意** `AgentFinish`不作为`streaming`方法的一部分提供。如果您希望添加这个功能，请在github上发起讨论并解释为什么需要它。


```python
async for chunk in agent_executor.astream(
    {"input": "猫躲在哪里有哪些物品？"}
):
# 代理执行

如果`chunk`中包含"actions"字段:
对于`chunk["actions"]`中的每一个action:
输出`Calling Tool: `{action.tool}` with input `{action.tool_input}``

如果`chunk`中包含"steps"字段:
对于`chunk["steps"]`中的每一个step:
输出`Tool Result: `{step.observation}``

如果`chunk`中包含"output"字段:
输出`Final Output: {chunk["output"]}`
否则:
抛出数值错误

输出"---"分割线
```

```python
Calling Tool: `where_cat_is_hiding` with input `{}`
---
Tool Result: `on the shelf`
---
Calling Tool: `get_items` with input `{'place': 'shelf'}`
---
Tool Result: `books, pencils and pictures`
---
Final Output: The items located where the cat is hiding on the shelf are books, pencils, and pictures.
---
```

## 使用自定义事件进行流式处理

如果默认的*stream*行为不适用于你的应用程序(例如，如果你需要从代理或工具内部发生的步骤中流式处理每个标记)，请使用`astream_events` API。

⚠️ 这是一个**beta**API，这意味着一些细节可能会根据使用情况稍微改变。
⚠️ 为了确保所有回调正确工作，请始终使用`async`代码。尽量避免混合同步版本的代码(例如，同步版本的工具)。

我们使用这个API来流式处理以下事件:

1. 带输入的代理开始
2. 带输入的工具开始
3. 带输出的工具结束
4. 逐个标记流式处理代理最终答案
5. 带输出的代理结束


```python
async for event in agent_executor.astream_events(
    {"input": "where is the cat hiding? what items are in that location?"},
    version="v1",
):
    kind = event["event"]
    if kind == "on_chain_start":
        if (
            event["name"] == "Agent"
        ):
            print(
                f"Starting agent: {event['name']} with input: {event['data'].get('input')}"
            )
    elif kind == "on_chain_end":
        if (
            event["name"] == "Agent"
        ):
            print()
            print("--")
            print(
                f"Done agent: {event['name']} with output: {event['data'].get('output')['output']}"
            )
    if kind == "on_chat_model_stream":
        content = event["data"]["chunk"].content
        if content:
            # 在OpenAI上下文中“空内容”表示模型正在请求调用工具。
            # 所以我们只打印非空内容
            print(content, end="|")
    elif kind == "on_tool_start":
        print("--")
        print(
            f"Starting tool: {event['name']} with inputs: {event['data'].get('input')}"
        )
    elif kind == "on_tool_end":
        print(f"Done tool: {event['name']}")
        print(f"Tool output was: {event['data'].get('output')}")
        print("--")
```

```
    开始代理: Agent with input: {'input': 'where is the cat hiding? what items are in that location?'}
    --
    开始工具: where_cat_is_hiding with inputs: {}
    完成工具: where_cat_is_hiding
    工具输出为: on the shelf
    --
    --
    开始工具: get_items with inputs: {'place': 'shelf'}
    完成工具: get_items
    工具输出为: books, pencils and pictures
    The| cat| is| currently| hiding| on| the| shelf|.| In| that| location|,| you| can| find| books|,| pencils|,| and| pictures|.|
    --
    完成代理: Agent with output: The cat is currently hiding on the shelf. In that location, you can find books, pencils, and pictures.
```   

### 从工具内部流式处理事件

如果你的工具利用LangChain可运行对象(例如LCEL链、LLMs、检索器等)，
并且你想要从这些对象中流式处理事件，你需要确保回调正确传播。

查看如何传递回调，让我们重新实现`get_items`工具，使其使用LLM并将回调传递给LLM。随时根据自己的情况进行调整。


```python
@tool
async def get_items(place: str, callbacks: Callbacks) -> str:
    """使用此工具查找给定地点中的物品。"""
    template = ChatPromptTemplate.from_messages(
        [
            (
                "human",
                "Can you tell me what kind of items i might find in the following place: '{place}'. "
                "List at least 3 such items separating them by a comma. And include a brief description of each item..",
            )
        ]
    )
    chain = template | model.with_config(
        {
            "run_name": "Get Items LLM",
            "tags": ["tool_llm"],
            "callbacks": callbacks,
        }
    )
    chunks = [chunk async for chunk in chain.astream({"place": place})]
    return "".join(chunk.content for chunk in chunks)
```

^看看工具如何传播回调。

接下来，让我们初始化我们的代理，并查看新的输出。


```python
prompt = hub.pull("hwchase17/openai-tools-agent")
tools = [get_items, where_cat_is_hiding]
agent = create_openai_tools_agent(
    model.with_config({"tags": ["agent_llm"]}), tools, prompt
)
agent_executor = AgentExecutor(agent=agent, tools=tools).with_config(
    {"run_name": "Agent"}
)

async for event in agent_executor.astream_events(
    {"input": "where is the cat hiding? what items are in that location?"},
    version="v1",
):
    kind = event["event"]
    if kind == "on_chain_start":
        if (
            event["name"] == "Agent"
        ):
            print(
                f"Starting agent: {event['name']} with input: {event['data'].get('input')}"
            )
    elif kind == "on_chain_end":
        if (
            event["name"] == "Agent"
        ):
            print()
            print("--")
            print(
                f"Done agent: {event['name']} with output: {event['data'].get('output')['output']}"
            )
    if kind == "on_chat_model_stream":
        content = event["data"]["chunk"].content
        if content:
            # 在OpenAI上下文中“空内容”表示模型正在请求调用工具。
            # 所以我们只打印非空内容
            print(content, end="|")
    elif kind == "on_tool_start":
        print("--")
        print(
            f"Starting tool: {event['name']} with inputs: {event['data'].get('input')}"
        )
    elif kind == "on_tool_end":
        print(f"Done tool: {event['name']}")
        print(f"Tool output was: {event['data'].get('output')}")
        print("--")
```

    开始代理: Agent with input: {'input': 'where is the cat hiding? what items are in that location?'}
    --
    开始工具: where_cat_is_hiding with inputs: {}
    完成工具: where_cat_is_hiding
    工具输出为: on the shelf
    --
    --
    开始工具: get_items with inputs: {'place': 'shelf'}
    在|一个|架子|上|,| 你|可能|会|找到|:
    
    |1|.| 图书|:| 架子|通常|用来|存放|书籍|。| 它|可以|包含|各种|流派|的|小说|、|教科书|或|参考书|。| 图书|提供|知识|、|娱乐|，|并通过|讲故事|将|你|带到|不同|的|世界|。
    
    |2|.| 装饰物品|:| 架子|经常|展示|装饰物品|，|如|小雕像|、|花瓶|或|照片框|。| 这些|物品|给|空间|增添|个人|风格|，|可以|反映|所有者|的|兴趣|或|回忆|。
    
    |3|.| 储物盒|:| 架子|还|可以|放置|储物盒|或|篮子|。| 这些|容器|帮助|组织|和|清理|空间|，|存放|文档|、|配件|或|小|家居用品|等|杂物|。| 它们|使|架子|看起来|整洁|和|有序|。|
    完成工具: get_items
    工具输出为: 在一个架子上, 你可能会找到:

    1. 图书: 架子通常用来存放书籍。它可以包含各种流派的小说、教科书或参考书。图书提供知识、娱乐，并通过讲故事将你带到不同的世界。

    2. 装饰物品: 架子经常展示装饰物品，如小雕像、花瓶或照片框。这些物品给空间增添个人风格，可以反映所有者的兴趣或回忆。

    3. 储物盒: 架子还可以放置储物盒或篮子。这些容器帮助组织和清理空间，存放文档、配件或小家居用品等杂物。它们使架子看起来整洁和有序。
    --
    猫|正在|架子|上|躲藏|。| 在|那|个|位置|,| 你|可能|会|找到|书籍、装饰物品和|储物盒|。|
    --
    完成代理: Agent with output: 猫正在架子上躲藏。在那个位置, 你可能会找到书籍、装饰物品和储物盒。
    



### 其他方法

#### 使用 astream_log

**注意** 您也可以使用 [astream_log](/expression_language/interface#async-stream-intermediate-steps) API。该API会在执行过程中产生所有事件的详细日志。日志格式基于 [JSONPatch](https://jsonpatch.com/) 标准。它是具有细粒度的日志，但需要解析。出于这个原因，我们创建了代替`astream_events` API。

```python
i = 0
async for chunk in agent_executor.astream_log(
    {"input": "猫躲在哪里？那个位置有什么物品？"},
):
    print(chunk)
    i += 1
    if i > 10:
        break
```

    RunLogPatch({'op': 'replace',
      'path': '',
      'value': {'final_output': None,
                'id': 'c261bc30-60d1-4420-9c66-c6c0797f2c2d',
                'logs': {},
                'name': 'Agent',
                'streamed_output': [],
                'type': 'chain'}})
    RunLogPatch({'op': 'add',
      'path': '/logs/RunnableSequence',
      'value': {'end_time': None,
                'final_output': None,
                'id': '183cb6f8-ed29-4967-b1ea-024050ce66c7',
                'metadata': {},
                'name': 'RunnableSequence',
                'start_time': '2024-01-22T20:38:43.650+00:00',
                'streamed_output': [],
                'streamed_output_str': [],
                'tags': [],
                'type': 'chain'}})
    RunLogPatch({'op': 'add',
      'path': '/logs/RunnableAssign<agent_scratchpad>',
      'value': {'end_time': None,
                'final_output': None,
                'id': '7fe1bb27-3daf-492e-bc7e-28602398f008',
                'metadata': {},
                'name': 'RunnableAssign<agent_scratchpad>',
                'start_time': '2024-01-22T20:38:43.652+00:00',
                'streamed_output': [],
                'streamed_output_str': [],
                'tags': ['seq:step:1'],
                'type': 'chain'}})
    RunLogPatch({'op': 'add',
      'path': '/logs/RunnableAssign<agent_scratchpad>/streamed_output/-',
      'value': {'input': '猫在哪里躲藏？那个位置有什么物品？',
                'intermediate_steps': []}})
    RunLogPatch({'op': 'add',
      'path': '/logs/RunnableParallel<agent_scratchpad>',
      'value': {'end_time': None,
                'final_output': None,
                'id': 'b034e867-e6bb-4296-bfe6-752c44fba6ce',
                'metadata': {},
                'name': 'RunnableParallel<agent_scratchpad>',
                'start_time': '2024-01-22T20:38:43.652+00:00',
                'streamed_output': [],
                'streamed_output_str': [],
                'tags': [],
                'type': 'chain'}})
    RunLogPatch({'op': 'add',
      'path': '/logs/RunnableLambda',
      'value': {'end_time': None,
                'final_output': None,
                'id': '65ceef3e-7a80-4015-8b5b-d949326872e9',
                'metadata': {},
                'name': 'RunnableLambda',
                'start_time': '2024-01-22T20:38:43.653+00:00',
                'streamed_output': [],
                'streamed_output_str': [],
                'tags': ['map:key:agent_scratchpad'],
                'type': 'chain'}})
    RunLogPatch({'op': 'add', 'path': '/logs/RunnableLambda/streamed_output/-', 'value': []})
    RunLogPatch({'op': 'add',
      'path': '/logs/RunnableParallel<agent_scratchpad>/streamed_output/-',
      'value': {'agent_scratchpad': []}})
    RunLogPatch({'op': 'add',
      'path': '/logs/RunnableAssign<agent_scratchpad>/streamed_output/-',
      'value': {'agent_scratchpad': []}})
    RunLogPatch({'op': 'add',
      'path': '/logs/RunnableLambda/final_output',
      'value': {'output': []}},
     {'op': 'add',
      'path': '/logs/RunnableLambda/end_time',
      'value': '2024-01-22T20:38:43.654+00:00'})
    RunLogPatch({'op': 'add',
      'path': '/logs/RunnableParallel<agent_scratchpad>/final_output',
      'value': {'agent_scratchpad': []}},
     {'op': 'add',
      'path': '/logs/RunnableParallel<agent_scratchpad>/end_time',
      'value': '2024-01-22T20:38:43.655+00:00'})
    

这可能需要一些逻辑才能以可操作的格式获得

```python
i = 0
path_status = {}
async for chunk in agent_executor.astream_log(
    {"input": "猫躲在哪里？那个位置有什么物品？"},
):
    for op in chunk.ops:
        if op["op"] == "add":
            if op["path"] not in path_status:
                path_status[op["path"]] = op["value"]
            else:
                path_status[op["path"]] += op["value"]
    print(op["path"])
    print(path_status.get(op["path"]))
    print("----")
    i += 1
    if i > 30:
        break
```

    
    None
    ----
    /logs/RunnableSequence
    {'id': '22bbd5db-9578-4e3f-a6ec-9b61f08cb8a9', 'name': 'RunnableSequence', 'type': 'chain', 'tags': [], 'metadata': {}, 'start_time': '2024-01-22T20:38:43.668+00:00', 'streamed_output': [], 'streamed_output_str': [], 'final_output': None, 'end_time': None}
    ----
    /logs/RunnableAssign<agent_scratchpad>
    {'id': 'e0c00ae2-aaa2-4a09-bc93-cb34bf3f6554', 'name': 'RunnableAssign<agent_scratchpad>', 'type': 'chain', 'tags': ['seq:step:1'], 'metadata': {}, 'start_time': '2024-01-22T20:38:43.672+00:00', 'streamed_output': [], 'streamed_output_str': [], 'final_output': None, 'end_time': None}
    ----
    /logs/RunnableAssign<agent_scratchpad>/streamed_output/-
    {'input': '猫在哪里躲藏？那个位置有什么物品？', 'intermediate_steps': []}
    ----
    /logs/RunnableParallel<agent_scratchpad>
    {'id': '26ff576d-ff9d-4dea-98b2-943312a37f4d', 'name': 'RunnableParallel<agent_scratchpad>', 'type': 'chain', 'tags': [], 'metadata': {}, 'start_time': '2024-01-22T20:38:43.674+00:00', 'streamed_output': [], 'streamed_output_str': [], 'final_output': None, 'end_time': None}
    ----
    /logs/RunnableLambda
    {'id': '9f343c6a-23f7-4a28-832f-d4fe3e95d1dc', 'name': 'RunnableLambda', 'type': 'chain', 'tags': ['map:key:agent_scratchpad'], 'metadata': {}, 'start_time': '2024-01-22T20:38:43.685+00:00', 'streamed_output': [], 'streamed_output_str': [], 'final_output': None, 'end_time': None}
    ----
    /logs/RunnableLambda/streamed_output/-
    []
    ----
    /logs/RunnableParallel<agent_scratchpad>/streamed_output/-
    {'agent_scratchpad': []}
    ----
    /logs/RunnableAssign<agent_scratchpad>/streamed_output/-
    {'input': '猫躲在哪里？那个位置有什么物品？', 'intermediate_steps': [], 'agent_scratchpad': []}
    ----
    /logs/RunnableLambda/end_time
    2024-01-22T20:38:43.687+00:00
    ----
    /logs/RunnableParallel<agent_scratchpad>/end_time
    2024-01-22T20:38:43.688+00:00
    ----
    /logs/RunnableAssign<agent_scratchpad>/end_time
    2024-01-22T20:38:43.688+00:00
    ----
    /logs/ChatPromptTemplate
    {'id': '7e3a84d5-46b8-4782-8eed-d1fe92be6a30', 'name': 'ChatPromptTemplate', 'type': 'prompt', 'tags': ['seq:step:2'], 'metadata': {}, 'start_time': '2024-01-22T20:38:43.689+00:00', 'streamed_output': [], 'streamed_output_str': [], 'final_output': None, 'end_time': None}
    ----
    /logs/ChatPromptTemplate/end_time
    2024-01-22T20:38:43.689+00:00
    ----
    /logs/ChatOpenAI
    {'id': '6446f7ec-b3e4-4637-89d8-b4b34b46ea14', 'name': 'ChatOpenAI', 'type': 'llm', 'tags': ['seq:step:3', 'agent_llm'], 'metadata': {}, 'start_time': '2024-01-22T20:38:43.690+00:00', 'streamed_output': [], 'streamed_output_str': [], 'final_output': None, 'end_time': None}
    ----
    /logs/ChatOpenAI/streamed_output/-
    content='' additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_gKFg6FX8ZQ88wFUs94yx86PF', 'function': {'arguments': '', 'name': 'where_cat_is_hiding'}, 'type': 'function'}]}
    ----
    /logs/ChatOpenAI/streamed_output/-
    content='' additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_gKFg6FX8ZQ88wFUs94yx86PF', 'function': {'arguments': '{}', 'name': 'where_cat_is_hiding'}, 'type': 'function'}]}
    ----
    /logs/ChatOpenAI/streamed_output/-
    content='' additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_gKFg6FX8ZQ88wFUs94yx86PF', 'function': {'arguments': '{}', 'name': 'where_cat_is_hiding'}, 'type': 'function'}]}
    ----
    /logs/ChatOpenAI/end_time
    2024-01-22T20:38:44.203+00:00
    ----
    /logs/OpenAIToolsAgentOutputParser
    {'id': '65912835-8dcd-4be2-ad05-9f239a7ef704', 'name': 'OpenAIToolsAgentOutputParser', 'type': 'parser', 'tags': ['seq:step:4'], 'metadata': {}, 'start_time': '2024-01-22T20:38:44.204+00:00', 'streamed_output': [], 'streamed_output_str': [], 'final_output': None, 'end_time': None}
    ----
    /logs/OpenAIToolsAgentOutputParser/end_time
    2024-01-22T20:38:44.205+00:00
    ----
    /logs/RunnableSequence/streamed_output/-
    [OpenAIToolAgentAction(tool='where_cat_is_hiding', tool_input={}, log='\nInvoking: `where_cat_is_hiding` with `{}`\n\n\n', message_log=[AIMessageChunk(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_gKFg6FX8ZQ88wFUs94yx86PF', 'function': {'arguments': '{}', 'name': 'where_cat_is_hiding'}, 'type': 'function'}]})], tool_call_id='call_gKFg6FX8ZQ88wFUs94yx86PF')]
    ----
    /logs/RunnableSequence/end_time
    2024-01-22T20:38:44.206+00:00
    ----
    /final_output
    None
    ----
    /logs/where_cat_is_hiding
    {'id': '21fde139-0dfa-42bb-ad90-b5b1e984aaba', 'name': 'where_cat_is_hiding', 'type': 'tool', 'tags': [], 'metadata': {}, 'start_time': '2024-01-22T20:38:44.208+00:00', 'streamed_output': [], 'streamed_output_str': [], 'final_output': None, 'end_time': None}
    ----
    /logs/where_cat_is_hiding/end_time
    2024-01-22T20:38:44.208+00:00
    ----
    /final_output/messages/1
    content='under the bed' name='where_cat_is_hiding'
    ----
    /logs/RunnableSequence:2
    {'id': '37d52845-b689-4c18-9c10-ffdd0c4054b0', 'name': 'RunnableSequence', 'type': 'chain', 'tags': [], 'metadata': {}, 'start_time': '2024-01-22T20:38:44.210+00:00', 'streamed_output': [], 'streamed_output_str': [], 'final_output': None, 'end_time': None}
    ----
    /logs/RunnableAssign<agent_scratchpad>:2
    {'id': '30024dea-064f-4b04-b130-671f47ac59bc', 'name': 'RunnableAssign<agent_scratchpad>', 'type': 'chain', 'tags': ['seq:step:1'], 'metadata': {}, 'start_time': '2024-01-22T20:38:44.213+00:00', 'streamed_output': [], 'streamed_output_str': [], 'final_output': None, 'end_time': None}
    ----
    /logs/RunnableAssign<agent_scratchpad>:2/streamed_output/-
    {'input': '猫躲在哪里？那个位置有什么物品？', 'intermediate_steps': [(OpenAIToolAgentAction(tool='where_cat_is_hiding', tool_input={}, log='\nInvoking: `where_cat_is_hiding` with `{}`\n\n\n', message_log=[AIMessageChunk(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_gKFg6FX8ZQ88wFUs94yx86PF', 'function': {'arguments': '{}', 'name': 'where_cat_is_hiding'}, 'type': 'function'}]})], tool_call_id='call_gKFg6FX8ZQ88wFUs94yx86PF'), 'under the bed')]}
    ----
    /logs/RunnableParallel<agent_scratchpad>:2
    {'id': '98906cd7-93c2-47e8-a7d7-2e8d4ab09ed0', 'name': 'RunnableParallel<agent_scratchpad>', 'type': 'chain', 'tags': [], 'metadata': {}, 'start_time': '2024-01-22T20:38:44.215+00:00', 'streamed_output': [], 'streamed_output_str': [], 'final_output': None, 'end_time': None}
    ----
    



#### 使用回调函数（已弃用）

流处理的另一种方法是使用回调函数。如果您仍在运行较旧版本的LangChain并且无法升级，则可能会有所帮助。

一般来说，这并**不**是一个推荐的方法，因为：

1. 对于大多数应用程序，您需要创建两个工作者，将回调写入队列，并且还需要另一个工作者从队列中读取（即，隐藏了使其正常工作所需的复杂性）。
2. **end** 事件可能会缺少一些元数据（例如，像运行名称这样的信息）。因此，如果您需要附加元数据，您应该继承自 `BaseTracer` 而不是 `AsyncCallbackHandler`，以从运行（即跟踪）中提取相关信息，或者根据 `run_id` 自己实现聚合逻辑。
3. 回调函数的行为不一致（例如，输入和输出的编码方式），具体取决于您需要解决的回调类型。

为了说明问题，我们在下面实现了一个回调函数，显示了如何进行 *基于标记的* 逐个令牌传递。根据您的应用程序需求，可以随意实现其他回调函数。

但是 `astream_events` 已经在幕后处理了所有这些，因此您不需要！

```python
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Sequence, TypeVar, Union
from uuid import UUID

from langchain_core.callbacks.base import AsyncCallbackHandler
from langchain_core.messages import BaseMessage
from langchain_core.outputs import ChatGenerationChunk, GenerationChunk, LLMResult

# 这是一个自定义处理程序，将令牌打印到标准输出。您也可以将数据发送到其他地方，例如流式 API 响应


class TokenByTokenHandler(AsyncCallbackHandler):
    def __init__(self, tags_of_interest: List[str]) -> None:
        """自定义回调处理程序。

        Args:
            tags_of_interest: 只会打印来自具有这些标签的模型的 LLM 令牌。
        """
        self.tags_of_interest = tags_of_interest

    async def on_chain_start(
        self,
        serialized: Dict[str, Any],
        inputs: Dict[str, Any],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        """链开始运行时运行。"""
        print("链开始：")
        print(inputs)

    async def on_chain_end(
        self,
        outputs: Dict[str, Any],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        """链结束运行时运行。"""
        print("链结束")
        print(outputs)

    async def on_chat_model_start(
        self,
        serialized: Dict[str, Any],
        messages: List[List[BaseMessage]],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        """聊天模型开始运行时运行。"""
        overlap_tags = self.get_overlap_tags(tags)

        if overlap_tags:
            print(",".join(overlap_tags), end=": ", flush=True)

    def on_tool_start(
        self,
        serialized: Dict[str, Any],
        input_str: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        inputs: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        """工具开始运行时运行。"""
        print("工具开始")
        print(serialized)

    def on_tool_end(
        self,
        output: Any,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        """工具结束运行时运行。"""
        print("工具结束")
        print(str(output))

    async def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        """LLM 结束运行时运行。"""
        overlap_tags = self.get_overlap_tags(tags)

        if overlap_tags:
            # 谁会对美丽表示怀疑？
            print()
            print()

    def get_overlap_tags(self, tags: Optional[List[str]]) -> List[str]:
        """检查与筛选标记的重叠部分。"""
        if not tags:
            return []
        return sorted(set(tags or []) & set(self.tags_of_interest or []))

    async def on_llm_new_token(
        self,
        token: str,
        *,
        chunk: Optional[Union[GenerationChunk, ChatGenerationChunk]] = None,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        """运行新的 LLM 令牌。仅在启用流式传输时可用。"""
        overlap_tags = self.get_overlap_tags(tags)

        if token and overlap_tags:
            print(token, end="|", flush=True)


handler = TokenByTokenHandler(tags_of_interest=["tool_llm", "agent_llm"])

result = await agent_executor.ainvoke(
    {"input": "where is the cat hiding and what items can be found there?"},
    {"callbacks": [handler]},
)
```

```
on chain start: 
{'input': 'where is the cat hiding and what items can be found there?'}
on chain start: 
{'input': ''}
on chain start: 
{'input': ''}
on chain start: 
{'input': ''}
on chain start: 
{'input': ''}
On chain end
[]
On chain end
{'agent_scratchpad': []}
On chain end
{'input': 'where is the cat hiding and what items can be found there?', 'intermediate_steps': [], 'agent_scratchpad': []}
on chain start: 
{'input': 'where is the cat hiding and what items can be found there?', 'intermediate_steps': [], 'agent_scratchpad': []}
On chain end
{'lc': 1, 'type': 'constructor', 'id': ['langchain', 'prompts', 'chat', 'ChatPromptValue'], 'kwargs': {'messages': [{'lc': 1, 'type': 'constructor', 'id': ['langchain', 'schema', 'messages', 'SystemMessage'], 'kwargs': {'content': 'You are a helpful assistant', 'additional_kwargs': {}}}, {'lc': 1, 'type': 'constructor', 'id': ['langchain', 'schema', 'messages', 'HumanMessage'], 'kwargs': {'content': 'where is the cat hiding and what items can be found there?', 'additional_kwargs': {}}}]}}
agent_llm: 

on chain start: 
content='' additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_pboyZTT0587rJtujUluO2OOc', 'function': {'arguments': '{}', 'name': 'where_cat_is_hiding'}, 'type': 'function'}]}
On chain end
...
On chain end
return_values={'output': 'The cat is hiding on the shelf. In the shelf, you might find books, decorative items, and storage boxes.'} log='The cat is hiding on the shelf. In the shelf, you might find books, decorative items, and storage boxes.'
On chain end
{'output': 'The cat is hiding on the shelf. In the shelf, you might find books, decorative items, and storage boxes.'}
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
```


# 数据流


所有ChatModels都实现了Runnable接口，其中包含所有方法的默认实现，例如invoke、batch、abatch、stream、astream。这为所有ChatModels提供了基本的数据流支持。

数据流支持默认返回一个迭代器（或者在异步数据流中返回一个AsyncIterator），其中包含底层ChatModel提供程序返回的最终结果。这显然不能提供逐个标记的数据流，这需要ChatModel提供程序的原生支持，但确保您的代码可用于我们ChatModel集成的任何迭代器标记。

查看[支持逐个标记数据流的集成情况](/docs/integrations/chat/)。

```python
from langchain_community.chat_models import ChatAnthropic
```

```python
chat = ChatAnthropic(model="claude-2")
for chunk in chat.stream("给我写一首关于月球上金鱼的歌"):
    print(chunk.content, end="", flush=True)
```

这是我刚创作的一首关于月球上金鱼的歌：

漂浮在太空中，寻找一个地方
叫做他们的家，孤独一人
穿过星星游泳，这些来自火星的金鱼
抛弃了他们的鱼缸，寻找新的生活
在月球上，在那些坑洞里
寻找食物，也许一些月球食物
深不可测，接近死亡
他们多么希望，只有一条小鱼
加入他们在这里，在他们的未来犹豫不决
在月球上，在地球的背后
憧憬着家，充满泡沫
他们的身体适应，继续持续
在月球上，在那里他们学会了惊叹
对宇航员戏弄的奶酪
当他们凝视着地球时，这个诞生之地
这些离开水中的金鱼，继续游啊游
月球上的先驱者，征服他们的恐惧
在月球上，在那里他们快乐地歌唱




```