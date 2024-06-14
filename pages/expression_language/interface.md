# 接口（Interface）

为了尽可能简化创建自定义链的过程，我们实现了一个 ["Runnable"](https://api.python.langchain.com/en/stable/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable) 协议。许多 LangChain 组件都实现了 `Runnable` 协议，包括聊天模型、LLMs、输出解析器、检索器、提示模板等。此外，还有几个有用的原语用于处理 Runnable，您可以在 [这个部分](/expression_language/primitives) 中详细了解它们。

这是一个标准接口，使得定义自定义链以及以标准方式调用它们变得容易。
标准接口包括：

- [`stream`](#stream)：以流的方式返回响应的块
- [`invoke`](#invoke)：对输入调用链
- [`batch`](#batch)：对输入列表调用链

这些方法还有对应的异步方法，应使用 [asyncio](https://docs.python.org/3/library/asyncio.html) 的 `await` 语法进行并发操作：

- [`astream`](#async-stream)：以异步流的方式返回响应的块
- [`ainvoke`](#async-invoke)：异步调用链对输入
- [`abatch`](#async-batch)：异步调用链对输入列表
- [`astream_log`](#async-stream-intermediate-steps)：以异步流的方式返回中间步骤的响应，以及最终响应
- [`astream_events`](#async-stream-events)：**beta** 在链中事件发生时流式传输事件（`langchain-core` 0.1.14中引入）

**输入类型**和**输出类型**因组件而异：

| 组件 | 输入类型 | 输出类型 |
| --- | --- | --- |
| Prompt | 字典 | PromptValue |
| ChatModel | 单个字符串、聊天消息列表或 PromptValue | ChatMessage |
| LLM | 单个字符串、聊天消息列表或 PromptValue | 字符串 |
| OutputParser | LLM或ChatModel的输出 | 取决于解析器 |
| Retriever | 单个字符串 | 文档列表 |
| Tool | 单个字符串或字典，取决于工具 | 取决于工具 |

所有 Runnable 都公开了输入和输出的 **模式** 以检查输入和输出：
- [`input_schema`](#input-schema)：从 Runnable 结构动态生成的输入 Pydantic 模型
- [`output_schema`](#output-schema)：从 Runnable 结构动态生成的输出 Pydantic 模型

让我们来看看这些方法。为此，我们将创建一个超级简单的 PromptTemplate + ChatModel 链。

```python
%pip install --upgrade --quiet  langchain-core langchain-community langchain-openai
```

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
chain = prompt | model
```

## 输入模式

一个 Runnable 接受的输入的描述。
这是从任何 Runnable 结构动态生成的 Pydantic 模型。
您可以在其上调用 `.schema()` 来获取 JSONSchema 表示。


```python
# The input schema of the chain is the input schema of its first part, the prompt.
chain.input_schema.schema()
```




    {'title': 'PromptInput',
     'type': 'object',
     'properties': {'topic': {'title': 'Topic', 'type': 'string'}}}




```python
prompt.input_schema.schema()
```




    {'title': 'PromptInput',
     'type': 'object',
     'properties': {'topic': {'title': 'Topic', 'type': 'string'}}}




```python
model.input_schema.schema()
```




    {'title': 'ChatOpenAIInput',
     'anyOf': [{'type': 'string'},
      {'$ref': '#/definitions/StringPromptValue'},
      {'$ref': '#/definitions/ChatPromptValueConcrete'},
      {'type': 'array',
       'items': {'anyOf': [{'$ref': '#/definitions/AIMessage'},
         {'$ref': '#/definitions/HumanMessage'},
         {'$ref': '#/definitions/ChatMessage'},
         {'$ref': '#/definitions/SystemMessage'},
         {'$ref': '#/definitions/FunctionMessage'},
         {'$ref': '#/definitions/ToolMessage'}]}}],
     'definitions': {'StringPromptValue': {'title': 'StringPromptValue',
       'description': 'String prompt value.',
       'type': 'object',
       'properties': {'text': {'title': 'Text', 'type': 'string'},
        'type': {'title': 'Type',
         'default': 'StringPromptValue',
         'enum': ['StringPromptValue'],
         'type': 'string'}},
       'required': ['text']},
      'AIMessage': {'title': 'AIMessage',
       'description': 'A Message from an AI.',
       'type': 'object',
       'properties': {'content': {'title': 'Content',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': 'Additional Kwargs', 'type': 'object'},
        'type': {'title': 'Type',
         'default': 'ai',
         'enum': ['ai'],
         'type': 'string'},
        'example': {'title': 'Example', 'default': False, 'type': 'boolean'}},
       'required': ['content']},
      'HumanMessage': {'title': 'HumanMessage',
       'description': 'A Message from a human.',
       'type': 'object',
       'properties': {'content': {'title': 'Content',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': 'Additional Kwargs', 'type': 'object'},
        'type': {'title': 'Type',
         'default': 'human',
         'enum': ['human'],
         'type': 'string'},
        'example': {'title': 'Example', 'default': False, 'type': 'boolean'}},
       'required': ['content']},
      'ChatMessage': {'title': 'ChatMessage',
       'description': 'A Message that can be assigned an arbitrary speaker (i.e. role).',
       'type': 'object',
       'properties': {'content': {'title': 'Content',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': 'Additional Kwargs', 'type': 'object'},
        'type': {'title': 'Type',
         'default': 'chat',
         'enum': ['chat'],
         'type': 'string'},
        'role': {'title': 'Role', 'type': 'string'}},
       'required': ['content', 'role']},
      'SystemMessage': {'title': 'SystemMessage',
       'description': 'A Message for priming AI behavior, usually passed in as the first of a sequence\nof input messages.',
       'type': 'object',
       'properties': {'content': {'title': 'Content',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': 'Additional Kwargs', 'type': 'object'},
        'type': {'title': 'Type',
         'default': 'system',
         'enum': ['system'],
         'type': 'string'}},
       'required': ['content']},
      'FunctionMessage': {'title': 'FunctionMessage',
       'description': 'A Message for passing the result of executing a function back to a model.',
       'type': 'object',
       'properties': {'content': {'title': 'Content',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': 'Additional Kwargs', 'type': 'object'},
        'type': {'title': 'Type',
         'default': 'function',
         'enum': ['function'],
         'type': 'string'},
        'name': {'title': 'Name', 'type': 'string'}},
       'required': ['content', 'name']},
      'ToolMessage': {'title': 'ToolMessage',
       'description': 'A Message for passing the result of executing a tool back to a model.',
       'type': 'object',
       'properties': {'content': {'title': 'Content',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': 'Additional Kwargs', 'type': 'object'},
        'type': {'title': 'Type',
         'default': 'tool',
         'enum': ['tool'],
         'type': 'string'},
        'tool_call_id': {'title': 'Tool Call Id', 'type': 'string'}},
       'required': ['content', 'tool_call_id']},
      'ChatPromptValueConcrete': {'title': 'ChatPromptValueConcrete',
       'description': 'Chat prompt value which explicitly lists out the message types it accepts.\nFor use in external schemas.',
       'type': 'object',
       'properties': {'messages': {'title': 'Messages',
         'type': 'array',
         'items': {'anyOf': [{'$ref': '#/definitions/AIMessage'},
           {'$ref': '#/definitions/HumanMessage'},
           {'$ref': '#/definitions/ChatMessage'},
           {'$ref': '#/definitions/SystemMessage'},
           {'$ref': '#/definitions/FunctionMessage'},
           {'$ref': '#/definitions/ToolMessage'}]}},
        'type': {'title': 'Type',
         'default': 'ChatPromptValueConcrete',
         'enum': ['ChatPromptValueConcrete'],
         'type': 'string'}},
       'required': ['messages']}}}## 输出模式

对Runnable生成的输出的描述。
这是从任何Runnable的结构动态生成的Pydantic模型。
您可以调用`.schema()`以获取JSONSchema表示形式。


```python
# 链的输出模式是其最后部分的输出模式，在本例中是ChatModel，它输出一个ChatMessage
chain.output_schema.schema()
```




    {'title': 'ChatOpenAIOutput',
     'anyOf': [{'$ref': '#/definitions/AIMessage'},
      {'$ref': '#/definitions/HumanMessage'},
      {'$ref': '#/definitions/ChatMessage'},
      {'$ref': '#/definitions/SystemMessage'},
      {'$ref': '#/definitions/FunctionMessage'},
      {'$ref': '#/definitions/ToolMessage'}],
     'definitions': {'AIMessage': {'title': 'AIMessage',
       'description': '来自AI的消息。',
       'type': 'object',
       'properties': {'content': {'title': '内容',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': '附加参数', 'type': 'object'},
        'type': {'title': '类型',
         'default': 'ai',
         'enum': ['ai'],
         'type': 'string'},
        'example': {'title': '示例', 'default': False, 'type': 'boolean'}},
       'required': ['content']},
      'HumanMessage': {'title': 'HumanMessage',
       'description': '来自人类的消息。',
       'type': 'object',
       'properties': {'content': {'title': '内容',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': '附加参数', 'type': 'object'},
        'type': {'title': '类型',
         'default': 'human',
         'enum': ['human'],
         'type': 'string'},
        'example': {'title': '示例', 'default': False, 'type': 'boolean'}},
       'required': ['content']},
      'ChatMessage': {'title': 'ChatMessage',
       'description': '可以分配任意发言者（即角色）的消息。',
       'type': 'object',
       'properties': {'content': {'title': '内容',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': '附加参数', 'type': 'object'},
        'type': {'title': '类型',
         'default': 'chat',
         'enum': ['chat'],
         'type': 'string'},
        'role': {'title': '角色', 'type': 'string'}},
       'required': ['content', 'role']},
      'SystemMessage': {'title': 'SystemMessage',
       'description': '用于初始化AI行为的消息，通常作为一系列输入消息中的第一个消息。',
       'type': 'object',
       'properties': {'content': {'title': '内容',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': '附加参数', 'type': 'object'},
        'type': {'title': '类型',
         'default': 'system',
         'enum': ['system'],
         'type': 'string'}},
       'required': ['content']},
      'FunctionMessage': {'title': 'FunctionMessage',
       'description': '用于将执行函数的结果传回模型的消息。',
       'type': 'object',
       'properties': {'content': {'title': '内容',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': '附加参数', 'type': 'object'},
        'type': {'title': '类型',
         'default': 'function',
         'enum': ['function'],
         'type': 'string'},
        'name': {'title': '名称', 'type': 'string'}},
       'required': ['content', 'name']},
      'ToolMessage': {'title': 'ToolMessage',
       'description': '用于将执行工具的结果传回模型的消息。',
       'type': 'object',
       'properties': {'content': {'title': '内容',
         'anyOf': [{'type': 'string'},
          {'type': 'array',
           'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}]},
        'additional_kwargs': {'title': '附加参数', 'type': 'object'},
        'type': {'title': '类型',
         'default': 'tool',
         'enum': ['tool'],
         'type': 'string'},
        'tool_call_id': {'title': '工具调用标识', 'type': 'string'}},
       'required': ['content', 'tool_call_id']}}}



## 流


```python
for s in chain.stream({"topic": "bears"}):
    print(s.content, end="", flush=True)
```

    当然，这是一个关于熊的笑话：

    为什么熊不穿鞋？

    因为它们已经有熊脚了！

## 调用


```python
chain.invoke({"topic": "bears"})
```




    AIMessage(content="为什么熊不穿鞋？\n\n因为它们有熊脚！")



## 批处理


```python
chain.batch([{"topic": "bears"}, {"topic": "cats"}])
```




    [AIMessage(content="当然，这是一个关于熊的笑话：\n\n为什么熊不穿鞋？\n\n因为它们已经有熊脚！"),
     AIMessage(content="为什么野生的猫不玩扑克牌？\n\n因为有太多的猎豹！")]



您可以使用`max_concurrency`参数设置并发请求的数量


```python
chain.batch([{"topic": "bears"}, {"topic": "cats"}], config={"max_concurrency": 5})
```




    [AIMessage(content="为什么熊不穿鞋？\n\n因为它们有熊脚！"),
     AIMessage(content="为什么野生的猫不玩扑克牌？太多的猎豹！")]



## 异步流


```python
async for s in chain.astream({"topic": "bears"}):
    print(s.content, end="", flush=True)
```

    为什么熊不穿鞋？

    因为它们有熊脚！

## 异步调用


```python
await chain.ainvoke({"topic": "bears"})
```




    AIMessage(content="为什么熊不穿鞋？\n\n因为它们已经有熊脚！")



## 异步批处理


```python
await chain.abatch([{"topic": "bears"}])
```




   [AIMessage(content="为什么熊不穿鞋？\n\n因为它们有熊脚！")]## 异步流事件（测试版）

事件流是一个**测试版**的API，可能会根据反馈进行一些更改。

注意：在langchain-core 0.2.0中引入。

目前，当使用astream_events API时，请确保以下操作才能正常工作：

* 在代码中始终使用`async`（包括async工具等）
* 如果定义自定义函数/可运行项，请传播回调。
* 在不使用LCEL的情况下使用可运行项时，请确保在LLMs上调用`.astream()`而不是`.ainvoke`以强制LLM流式传输令牌。

### 事件参考


下面是一个参考表格，显示各种Runnable对象可能发出的一些事件。表格之后包含了一些Runnable的定义。

⚠️流式传输输入，在输入流完全消耗之前将不可用。这意味着输入将在对应的`end`钩子而不是`start`事件中可用。

| 事件                  | 名称             | 代码块                           | 输入                                         | 输出                                          |
|----------------------|------------------|---------------------------------|-----------------------------------------------|-------------------------------------------------|
| on_chat_model_start  | [模型名称]         |                                 | {"messages": [[SystemMessage, HumanMessage]]} |                                                 |
| on_chat_model_stream | [模型名称]         | AIMessageChunk(content="hello") |                                               |                                                 |
| on_chat_model_end    | [模型名称]         |                                 | {"messages": [[SystemMessage, HumanMessage]]} | {"generations": [...], "llm_output": None, ...} |
| on_llm_start         | [模型名称]         |                                 | {'input': 'hello'}                            |                                                 |
| on_llm_stream        | [模型名称]         | 'Hello'                         |                                               |                                                 |
| on_llm_end           | [模型名称]         |                                 | 'Hello human!'                                |
| on_chain_start       | format_docs      |                                 |                                               |                                                 |
| on_chain_stream      | format_docs      | "hello world!, goodbye world!"  |                                               |                                                 |
| on_chain_end         | format_docs      |                                 | [Document(...)]                               | "hello world!, goodbye world!"                  |
| on_tool_start        | some_tool        |                                 | {"x": 1, "y": "2"}                            |                                                 |
| on_tool_stream       | some_tool        | {"x": 1, "y": "2"}              |                                               |                                                 |
| on_tool_end          | some_tool        |                                 |                                               | {"x": 1, "y": "2"}                              |
| on_retriever_start   | [检索器名称]         |                                 | {"query": "hello"}                            |                                                 |
| on_retriever_chunk   | [检索器名称]         | {documents: [...]}              |                                               |                                                 |
| on_retriever_end     | [检索器名称]         |                                 | {"query": "hello"}                            | {documents: [...]}                              |
| on_prompt_start      | [模板名称]         |                                 | {"question": "hello"}                         |                                                 |
| on_prompt_end        | [模板名称]         |                                 | {"question": "hello"}                         | ChatPromptValue(messages: [SystemMessage, ...]) |


以下是与上述事件显示相关的声明：

`format_docs`:

```python
def format_docs(docs: List[Document]) -> str:
    '''格式化docs。'''
    return ", ".join([doc.page_content for doc in docs])

format_docs = RunnableLambda(format_docs)
```

`some_tool`:

```python
@工具
def some_tool(x: int, y: str) -> dict:
    '''some_tool。'''
    return {"x": x, "y": y}
```

`prompt`:

```python
template = ChatPromptTemplate.from_messages(
    [("system", "You are Cat Agent 007"), ("human", "{question}")]
).with_config({"run_name": "my_template", "tags": ["my_template"]})
```



让我们定义一个新的chain，以使`astream_events`接口（和稍后的`astream_log`接口）更有趣。


```python
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings

template = """仅根据以下内容回答问题：
{context}

问题：{question}
"""
prompt = ChatPromptTemplate.from_template(template)

vectorstore = FAISS.from_texts(
    ["harrison worked at kensho"], embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

retrieval_chain = (
    {
        "context": retriever.with_config(run_name="Docs"),
        "question": RunnablePassthrough(),
    }
    | prompt
    | model.with_config(run_name="my_llm")
    | StrOutputParser()
)
```

现在让我们使用`astream_events`从检索器和LLM中获取事件。


```python
async for event in retrieval_chain.astream_events(
    "where did harrison work?", version="v1", include_names=["Docs", "my_llm"]
):
    kind = event["event"]
    if kind == "on_chat_model_stream":
        print(event["data"]["chunk"].content, end="|")
    elif kind in {"on_chat_model_start"}:
        print()
        print("Streaming LLM:")
    elif kind in {"on_chat_model_end"}:
        print()
        print("Done streaming LLM.")
    elif kind == "on_retriever_end":
        print("--")
        print("Retrieved the following documents:")
        print(event["data"]["output"]["documents"])
    elif kind == "on_tool_end":
        print(f"Ended tool: {event['name']}")
    else:
        pass
```

    /home/eugene/src/langchain/libs/core/langchain_core/_api/beta_decorator.py:86: LangChainBetaWarning: This API is in beta and may change in the future.
      warn_beta(
    

    --
    Retrieved the following documents:
    [Document(page_content='harrison worked at kensho')]
    
    Streaming LLM:
    |H|arrison| worked| at| Kens|ho|.||
    Done streaming LLM.
    

## 异步流中间步骤

所有可运行项也都有一个`.astream_log()`方法，用于（如发生的）流式传输链/序列的所有或部分中间步骤。

这对于向用户显示进度、使用中间结果或调试链条非常有用。

您可以流式传输所有步骤（默认）或根据名称、标签或元数据包含/排除步骤。

该方法生成[JSONPatch](https://jsonpatch.com) ops，当按照接收到的顺序应用这些ops时，可以构建出RunState。

```python
class LogEntry(TypedDict):
    id: str
    """子运行的ID。"""
    name: str
    """正在运行的对象的名称。"""
    type: str
    """正在运行的对象的类型，例如prompt，chain，llm等。"""
    tags: List[str]
    """运行标签列表。"""
    metadata: Dict[str, Any]
    """运行的元数据键值对。"""
    start_time: str
    """运行开始的ISO-8601时间戳。"""

    streamed_output_str: List[str]
    """由此运行流式传输的LLM令牌列表，如果适用。"""
    final_output: Optional[Any]
    """此运行的最终输出。
    仅在运行成功完成后可获得。"""
    end_time: Optional[str]
    """运行结束的ISO-8601时间戳。
    仅在运行成功结束后可获得。"""


class RunState(TypedDict):
    id: str
    """运行的ID。"""
    streamed_output: List[Any]
    """Runnable.stream()流式传输的输出块列表。"""
    final_output: Optional[Any]
    """运行的最终输出，通常是聚合（`+`）streamed_output的结果。
    仅在运行成功完成后可获得。"""

    logs: Dict[str, LogEntry]
    """运行名称到子运行的映射。
    如果提供了过滤器，则此列表将只包含与过滤器匹配的运行。"""
```

### 流式传输JSONPatch块

这对于例如在HTTP服务器中流式传输`JSONPatch`很有用，然后在客户端应用ops以在那里重建运行状态。有关使任何Runnable构建Web服务器变得更容易的工具，请参见[LangServe](https://github.com/langchain-ai/langserve)。


```python
async for chunk in retrieval_chain.astream_log(
    "where did harrison work?", include_names=["Docs"]
):
    print("-" * 40)
    print(chunk)
```

    ----------------------------------------
    RunLogPatch({'op': 'replace',
      'path': '',
      'value': {'final_output': None,
                'id': '82e9b4b1-3dd6-4732-8db9-90e79c4da48c',
                'logs': {},
                'name': 'RunnableSequence',
                'streamed_output': [],
                'type': 'chain'}})
    ----------------------------------------
    RunLogPatch({'op': 'add',
      'path': '/logs/Docs',
      'value': {'end_time': None,
                'final_output': None,
                'id': '9206e94a-57bd-48ee-8c5e-fdd1c52a6da2',
                'metadata': {},
                'name': 'Docs',
                'start_time': '2024-01-19T22:33:55.902+00:00',
                'streamed_output': [],
                'streamed_output_str': [],
                'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                'type': 'retriever'}})
    ----------------------------------------
    RunLogPatch({'op': 'add',
      'path': '/logs/Docs/final_output',
      'value': {'documents': [Document(page_content='harrison worked at kensho')]}},
     {'op': 'add',
      'path': '/logs/Docs/end_time',
      'value': '2024-01-19T22:33:56.064+00:00'})
    ----------------------------------------
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': ''},
     {'op': 'replace', 'path': '/final_output', 'value': ''})
    ----------------------------------------
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': 'H'},
     {'op': 'replace', 'path': '/final_output', 'value': 'H'})
    ----------------------------------------
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': 'arrison'},
     {'op': 'replace', 'path': '/final_output', 'value': 'Harrison'})
    ----------------------------------------
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': ' worked'},
     {'op': 'replace', 'path': '/final_output', 'value': 'Harrison worked'})
    ----------------------------------------
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': ' at'},
     {'op': 'replace', 'path': '/final_output', 'value': 'Harrison worked at'})
    ----------------------------------------
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': ' Kens'},
     {'op': 'replace', 'path': '/final_output', 'value': 'Harrison worked at Kens'})
    ----------------------------------------
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': 'ho'},
     {'op': 'replace',
      'path': '/final_output',
      'value': 'Harrison worked at Kensho'})
    ----------------------------------------
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': '.'},
     {'op': 'replace',
      'path': '/final_output',
      'value': 'Harrison worked at Kensho.'})
    ----------------------------------------
    RunLogPatch({'op': 'add', 'path': '/streamed_output/-', 'value': ''})
    

------### 流式增量运行状态

您可以简单地传递`diff=False`以获得`RunState`的增量值。
通过更多重复部分，您可以获得更多详细的输出。

```python
async for chunk in retrieval_chain.astream_log(
    "where did harrison work?", include_names=["Docs"], diff=False
):
    print("-" * 70)
    print(chunk)
```

    ----------------------------------------------------------------------
    RunLog({'final_output': None,
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {},
     'name': 'RunnableSequence',
     'streamed_output': [],
     'type': 'chain'})
    ----------------------------------------------------------------------
    RunLog({'final_output': None,
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {'Docs': {'end_time': None,
                       'final_output': None,
                       'id': '8de10b49-d6af-4cb7-a4e7-fbadf6efa01e',
                       'metadata': {},
                       'name': 'Docs',
                       'start_time': '2024-01-19T22:33:56.939+00:00',
                       'streamed_output': [],
                       'streamed_output_str': [],
                       'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                       'type': 'retriever'}},
     'name': 'RunnableSequence',
     'streamed_output': [],
     'type': 'chain'})
    ----------------------------------------------------------------------
    RunLog({'final_output': None,
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {'Docs': {'end_time': '2024-01-19T22:33:57.120+00:00',
                       'final_output': {'documents': [Document(page_content='harrison worked at kensho')]},
                       'id': '8de10b49-d6af-4cb7-a4e7-fbadf6efa01e',
                       'metadata': {},
                       'name': 'Docs',
                       'start_time': '2024-01-19T22:33:56.939+00:00',
                       'streamed_output': [],
                       'streamed_output_str': [],
                       'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                       'type': 'retriever'}},
     'name': 'RunnableSequence',
     'streamed_output': [],
     'type': 'chain'})
    ----------------------------------------------------------------------
    RunLog({'final_output': '',
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {'Docs': {'end_time': '2024-01-19T22:33:57.120+00:00',
                       'final_output': {'documents': [Document(page_content='harrison worked at kensho')]},
                       'id': '8de10b49-d6af-4cb7-a4e7-fbadf6efa01e',
                       'metadata': {},
                       'name': 'Docs',
                       'start_time': '2024-01-19T22:33:56.939+00:00',
                       'streamed_output': [],
                       'streamed_output_str': [],
                       'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                       'type': 'retriever'}},
     'name': 'RunnableSequence',
     'streamed_output': [''],
     'type': 'chain'})
    ----------------------------------------------------------------------
    RunLog({'final_output': 'H',
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {'Docs': {'end_time': '2024-01-19T22:33:57.120+00:00',
                       'final_output': {'documents': [Document(page_content='harrison worked at kensho')]},
                       'id': '8de10b49-d6af-4cb7-a4e7-fbadf6efa01e',
                       'metadata': {},
                       'name': 'Docs',
                       'start_time': '2024-01-19T22:33:56.939+00:00',
                       'streamed_output': [],
                       'streamed_output_str': [],
                       'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                       'type': 'retriever'}},
     'name': 'RunnableSequence',
     'streamed_output': ['', 'H'],
     'type': 'chain'})
    ----------------------------------------------------------------------
    RunLog({'final_output': 'Harrison',
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {'Docs': {'end_time': '2024-01-19T22:33:57.120+00:00',
                       'final_output': {'documents': [Document(page_content='harrison worked at kensho')]},
                       'id': '8de10b49-d6af-4cb7-a4e7-fbadf6efa01e',
                       'metadata': {},
                       'name': 'Docs',
                       'start_time': '2024-01-19T22:33:56.939+00:00',
                       'streamed_output': [],
                       'streamed_output_str': [],
                       'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                       'type': 'retriever'}},
     'name': 'RunnableSequence',
     'streamed_output': ['', 'H', 'arrison'],
     'type': 'chain'})
    ----------------------------------------------------------------------
    RunLog({'final_output': 'Harrison worked',
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {'Docs': {'end_time': '2024-01-19T22:33:57.120+00:00',
                       'final_output': {'documents': [Document(page_content='harrison worked at kensho')]},
                       'id': '8de10b49-d6af-4cb7-a4e7-fbadf6efa01e',
                       'metadata': {},
                       'name': 'Docs',
                       'start_time': '2024-01-19T22:33:56.939+00:00',
                       'streamed_output': [],
                       'streamed_output_str': [],
                       'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                       'type': 'retriever'}},
     'name': 'RunnableSequence',
     'streamed_output': ['', 'H', 'arrison', ' worked'],
     'type': 'chain'})
    ----------------------------------------------------------------------
    RunLog({'final_output': 'Harrison worked at',
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {'Docs': {'end_time': '2024-01-19T22:33:57.120+00:00',
                       'final_output': {'documents': [Document(page_content='harrison worked at kensho')]},
                       'id': '8de10b49-d6af-4cb7-a4e7-fbadf6efa01e',
                       'metadata': {},
                       'name': 'Docs',
                       'start_time': '2024-01-19T22:33:56.939+00:00',
                       'streamed_output': [],
                       'streamed_output_str': [],
                       'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                       'type': 'retriever'}},
     'name': 'RunnableSequence',
     'streamed_output': ['', 'H', 'arrison', ' worked', ' at'],
     'type': 'chain'})
    ----------------------------------------------------------------------
    RunLog({'final_output': 'Harrison worked at Kens',
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {'Docs': {'end_time': '2024-01-19T22:33:57.120+00:00',
                       'final_output': {'documents': [Document(page_content='harrison worked at kensho')]},
                       'id': '8de10b49-d6af-4cb7-a4e7-fbadf6efa01e',
                       'metadata': {},
                       'name': 'Docs',
                       'start_time': '2024-01-19T22:33:56.939+00:00',
                       'streamed_output': [],
                       'streamed_output_str': [],
                       'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                       'type': 'retriever'}},
     'name': 'RunnableSequence',
     'streamed_output': ['', 'H', 'arrison', ' worked', ' at', ' Kens'],
     'type': 'chain'})
    ----------------------------------------------------------------------
    RunLog({'final_output': 'Harrison worked at Kensho',
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {'Docs': {'end_time': '2024-01-19T22:33:57.120+00:00',
                       'final_output': {'documents': [Document(page_content='harrison worked at kensho')]},
                       'id': '8de10b49-d6af-4cb7-a4e7-fbadf6efa01e',
                       'metadata': {},
                       'name': 'Docs',
                       'start_time': '2024-01-19T22:33:56.939+00:00',
                       'streamed_output': [],
                       'streamed_output_str': [],
                       'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                       'type': 'retriever'}},
     'name': 'RunnableSequence',
     'streamed_output': ['', 'H', 'arrison', ' worked', ' at', ' Kens', 'ho'],
     'type': 'chain'})
    ----------------------------------------------------------------------
    RunLog({'final_output': 'Harrison worked at Kensho.',
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {'Docs': {'end_time': '2024-01-19T22:33:57.120+00:00',
                       'final_output': {'documents': [Document(page_content='harrison worked at kensho')]},
                       'id': '8de10b49-d6af-4cb7-a4e7-fbadf6efa01e',
                       'metadata': {},
                       'name': 'Docs',
                       'start_time': '2024-01-19T22:33:56.939+00:00',
                       'streamed_output': [],
                       'streamed_output_str': [],
                       'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                       'type': 'retriever'}},
     'name': 'RunnableSequence',
     'streamed_output': ['', 'H', 'arrison', ' worked', ' at', ' Kens', 'ho', '.'],
     'type': 'chain'})
    ----------------------------------------------------------------------
    RunLog({'final_output': 'Harrison worked at Kensho.',
     'id': '431d1c55-7c50-48ac-b3a2-2f5ba5f35172',
     'logs': {'Docs': {'end_time': '2024-01-19T22:33:57.120+00:00',
                       'final_output': {'documents': [Document(page_content='harrison worked at kensho')]},
                       'id': '8de10b49-d6af-4cb7-a4e7-fbadf6efa01e',
                       'metadata': {},
                       'name': 'Docs',
                       'start_time': '2024-01-19T22:33:56.939+00:00',
                       'streamed_output': [],
                       'streamed_output_str': [],
                       'tags': ['map:key:context', 'FAISS', 'OpenAIEmbeddings'],
                       'type': 'retriever'}},
     'name': 'RunnableSequence',
     'streamed_output': ['',
                         'H',
                         'arrison',
                         ' worked',
                         ' at',
                         ' Kens',
                         'ho',
                         '.',
                         ''],
     'type': 'chain'})
    

## 并行处理

让我们来看一下LangChain表达语言如何支持并行请求。
例如，当使用`RunnableParallel`（通常写作字典）时，它会并行执行每个元素。


```python
from langchain_core.runnables import RunnableParallel

chain1 = ChatPromptTemplate.from_template("给我讲个关于{topic}的笑话") | model
chain2 = (
    ChatPromptTemplate.from_template("写一个关于{topic}的短诗（两行）")
    | model
)
combined = RunnableParallel(joke=chain1, poem=chain2)
```


```python
%%time
chain1.invoke({"topic": "熊"})
```

    CPU 时间：用户 18 毫秒，系统：1.27 毫秒，总共：19.3 毫秒
    实际请求数：692 毫秒




    AIMessage(content="为什么熊不穿鞋？\n\n因为它们已经有熊脚！")



```python
%%time
chain2.invoke({"topic": "熊"})
```

    CPU 时间：用户 10.5 毫秒，系统：166 微秒，总共：10.7 毫秒
    实际请求数：579 毫秒




    AIMessage(content="在森林的拥抱中，\n伟大的熊步行。")



```python
%%time
combined.invoke({"topic": "熊"})
```

    CPU 时间：用户 32 毫秒，系统：2.59 毫秒，总共：34.6 毫秒
    实际请求数：816 毫秒




    {'joke': AIMessage(content="好的，给你一个关于熊的笑话：\n\n熊为什么带一把梯子去酒吧？\n\n因为它听说酒是免费的！"),
     'poem': AIMessage(content="它们在荒野徘徊，\n伟大的力量，自然的王座。")}



### 批处理中的并行处理

并行处理可以与其他可执行文件结合使用。
让我们尝试在批处理中使用并行处理。


```python
%%time
chain1.batch([{"topic": "熊"}, {"topic": "猫"}])
```

    CPU 时间：用户 17.3 毫秒，系统：4.84 毫秒，总共：22.2 毫秒
    实际请求数：628 毫秒




    [AIMessage(content="为什么熊不穿鞋？\n\n因为它们有熊脚！"),
     AIMessage(content="为什么猫不在野外打扑克？\n\n太多的猎豹！")]



```python
%%time
chain2.batch([{"topic": "熊"}, {"topic": "猫"}])
```

    CPU 时间：用户 15.8 毫秒，系统：3.83 毫秒，总共：19.7 毫秒
    实际请求数：718 毫秒




    [AIMessage(content='在野外，熊在漫游，\n古老家园的守护者。'),
     AIMessage(content='胡须优雅，眼睛闪烁，\n猫儿在月光中翩翩起舞。')]



```python
%%time
combined.batch([{"topic": "熊"}, {"topic": "猫"}])
```

    CPU 时间：用户 44.8 毫秒，系统：3.17 毫秒，总共：48 毫秒
    实际请求数：721 毫秒




    [{'joke': AIMessage(content="好的，给你一个关于熊的笑话：\n\n为什么熊不穿鞋？\n\n因为它们有熊脚！"),
      'poem': AIMessage(content="伟大的熊漫游，\n自然力量，美丽展现。")},
     {'joke': AIMessage(content="为什么猫不在野外打扑克？\n\n太多的猎豹！"),
      'poem': AIMessage(content="胡须起舞，眼睛闪耀，\n猫儿拥抱夜晚温柔的流动。")}]


------