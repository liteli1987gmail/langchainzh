# LCEL的优势

:::
我们建议先阅读LCEL的 [入门指南](/expression_language/get_started) 部分。
:::

LCEL旨在简化使用LLM构建有用应用程序并组合相关组件的过程。它通过提供以下功能来实现这一目标：

1. **统一的接口**：每个LCEL对象实现`Runnable`接口，该接口定义了一组常见的调用方法（`invoke`、`batch`、`stream`、`ainvoke`等）。这使得LCEL对象的链条也能够自动支持批处理和中间步骤的流处理等有用操作，因为每个LCEL对象的链条本身也是一个LCEL对象。
2. **组合原语**：LCEL提供了一些原语，可以轻松地组合链条、并行化组件、添加容错机制、动态配置链条内部等等。

要更好地理解LCEL的价值，最好是看到它的实际效果，并思考如果没有它，如何重新创建类似的功能。在本教程中，我们将使用[入门指南](/expression_language/get_started#基本例子)中的[基本例子](/expression_language/get_started#basic_example)进行演示。我们将使用简单的提示+模型链条，该链条在底层已经定义了许多功能，并观察重新创建所有这些功能所需的步骤。


```python
%pip install --upgrade --quiet  langchain-core langchain-openai langchain-anthropic
```

## 调用（Invoke）
在最简单的情况下，我们只想传入一个主题字符串，并获得一个笑话字符串：

```{=mdx}
<ColumnContainer>

<Column>

```

#### 没有使用LCEL



```python
from typing import List

import openai


prompt_template = "告诉我一个关于{topic}的笑话"
client = openai.OpenAI()

def call_chat_model(messages: List[dict]) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=messages,
    )
    return response.choices[0].message.content

def invoke_chain(topic: str) -> str:
    prompt_value = prompt_template.format(topic=topic)
    messages = [{"role": "user", "content": prompt_value}]
    return call_chat_model(messages)

invoke_chain("冰淇淋")
```


```{=mdx}
</Column>

<Column>
```

#### 使用LCEL




```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


prompt = ChatPromptTemplate.from_template(
    "告诉我一个关于{topic}的笑话"
)
output_parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo")
chain = (
    {"topic": RunnablePassthrough()} 
    | prompt
    | model
    | output_parser
)

chain.invoke("冰淇淋")
```


```{=mdx}
</Column>
</ColumnContainer>
```
## 流（Stream）
如果我们想要流式传输结果，我们需要更改函数：

```{=mdx}

<ColumnContainer>
<Column>
```

#### 没有使用LCEL




```python
from typing import Iterator


def stream_chat_model(messages: List[dict]) -> Iterator[str]:
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )
    for response in stream:
        content = response.choices[0].delta.content
        if content is not None:
            yield content

def stream_chain(topic: str) -> Iterator[str]:
    prompt_value = prompt.format(topic=topic)
    return stream_chat_model([{"role": "user", "content": prompt_value}])


for chunk in stream_chain("冰淇淋"):
    print(chunk, end="", flush=True)
```

```{=mdx}
</Column>

<Column>
```
#### 使用LCEL




```python
for chunk in chain.stream("冰淇淋"):
    print(chunk, end="", flush=True)
```

```{=mdx}
</Column>
</ColumnContainer>
```

## 批处理（Batch）

如果我们想要并行运行一批输入，我们同样需要一个新的函数：

```{=mdx}
<ColumnContainer>
<Column>
```

#### 没有使用LCEL




```python
from concurrent.futures import ThreadPoolExecutor


def batch_chain(topics: list) -> list:
    with ThreadPoolExecutor(max_workers=5) as executor:
        return list(executor.map(invoke_chain, topics))

batch_chain(["冰淇淋", "意大利面", "饺子"])
```

```{=mdx}
</Column>

<Column>
```
#### 使用LCEL




```python
chain.batch(["冰淇淋", "意大利面", "饺子"])
```

```{=mdx}
</Column>
</ColumnContainer>
```
------
                你翻译完后对原内容进行替换，将结果返回给我。mdx文档是: Advantages of LCEL## 异步

如果我们需要一个异步版本：

```{=mdx}
<ColumnContainer>
<Column>
```

#### 没有LCEL




```python
async_client = openai.AsyncOpenAI()

async def acall_chat_model(messages: List[dict]) -> str:
    response = await async_client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=messages,
    )
    return response.choices[0].message.content

async def ainvoke_chain(topic: str) -> str:
    prompt_value = prompt_template.format(topic=topic)
    messages = [{"role": "user", "content": prompt_value}]
    return await acall_chat_model(messages)


await ainvoke_chain("冰淇淋")
```

```{=mdx}
</Column>

<Column>
```

#### LCEL




```python
await chain.ainvoke("冰淇淋")
```

```{=mdx}
</Column>
</ColumnContainer>
```
## 异步批处理

```{=mdx}
<ColumnContainer>
<Column>
```

#### 没有LCEL




```python
import asyncio
import openai


async def abatch_chain(topics: list) -> list:
    coros = map(ainvoke_chain, topics)
    return await asyncio.gather(*coros)


await abatch_chain(["冰淇淋", "意大利面", "饺子"])
```

```{=mdx}
</Column>

<Column>
```

#### LCEL




```python
await chain.abatch(["冰淇淋", "意大利面", "饺子"])
```

```{=mdx}
</Column>
</ColumnContainer>
```

## LLM而不是聊天模型

如果我们想要使用完成端点而不是聊天端点：

```{=mdx}
<ColumnContainer>
<Column>
```

#### 没有LCEL




```python
def call_llm(prompt_value: str) -> str:
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt_value,
    )
    return response.choices[0].text

def invoke_llm_chain(topic: str) -> str:
    prompt_value = prompt_template.format(topic=topic)
    return call_llm(prompt_value)

invoke_llm_chain("冰淇淋")
```

```{=mdx}
</Column>

<Column>
```

#### LCEL




```python
from langchain_openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct")
llm_chain = (
    {"topic": RunnablePassthrough()} 
    | prompt
    | llm
    | output_parser
)

llm_chain.invoke("冰淇淋")
```

```{=mdx}
</Column>
</ColumnContainer>
```

## 不同的模型提供者

如果我们想要使用Anthropic而不是OpenAI：

```{=mdx}
<ColumnContainer>
<Column>
```

#### 没有LCEL




```python
import anthropic

anthropic_template = f"Human:\n\n{prompt_template}\n\nAssistant:"
anthropic_client = anthropic.Anthropic()

def call_anthropic(prompt_value: str) -> str:
    response = anthropic_client.completions.create(
        model="claude-2",
        prompt=prompt_value,
        max_tokens_to_sample=256,
    )
    return response.completion    

def invoke_anthropic_chain(topic: str) -> str:
    prompt_value = anthropic_template.format(topic=topic)
    return call_anthropic(prompt_value)

invoke_anthropic_chain("冰淇淋")
```

```{=mdx}
</Column>

<Column>
```

#### LCEL




```python
from langchain_anthropic import ChatAnthropic

anthropic = ChatAnthropic(model="claude-2")
anthropic_chain = (
    {"topic": RunnablePassthrough()} 
    | prompt 
    | anthropic
    | output_parser
)

anthropic_chain.invoke("冰淇淋")
```

```{=mdx}
</Column>
</ColumnContainer>
```

------## 运行时可配置性

如果我们想要在运行时使聊天模型或LLM的选择可配置化：

```{=mdx}
<ColumnContainer>
<Column>
```

#### 没有LCEL




```python
def invoke_configurable_chain(
    topic: str, 
    *, 
    model: str = "chat_openai"
) -> str:
    if model == "chat_openai":
        return invoke_chain(topic)
    elif model == "openai":
        return invoke_llm_chain(topic)
    elif model == "anthropic":
        return invoke_anthropic_chain(topic)
    else:
        raise ValueError(
            f"Received invalid model '{model}'."
            " Expected one of chat_openai, openai, anthropic"
        )

def stream_configurable_chain(
    topic: str, 
    *, 
    model: str = "chat_openai"
) -> Iterator[str]:
    if model == "chat_openai":
        return stream_chain(topic)
    elif model == "openai":
        # 注意我们还没有实现这个功能。
        return stream_llm_chain(topic)
    elif model == "anthropic":
        # 注意我们还没有实现这个功能。
        return stream_anthropic_chain(topic)
    else:
        raise ValueError(
            f"Received invalid model '{model}'."
            " Expected one of chat_openai, openai, anthropic"
        )

def batch_configurable_chain(
    topics: List[str], 
    *, 
    model: str = "chat_openai"
) -> List[str]:
    # 你懂的
    ...

async def abatch_configurable_chain(
    topics: List[str], 
    *, 
    model: str = "chat_openai"
) -> List[str]:
    ...

invoke_configurable_chain("ice cream", model="openai")
stream = stream_configurable_chain(
    "ice_cream", 
    model="anthropic"
)
for chunk in stream:
    print(chunk, end="", flush=True)

# batch_configurable_chain(["ice cream", "spaghetti", "dumplings"])
# await ainvoke_configurable_chain("ice cream")
```

```{=mdx}
</Column>

<Column>
```

#### 有LCEL




```python
from langchain_core.runnables import ConfigurableField


configurable_model = model.configurable_alternatives(
    ConfigurableField(id="model"), 
    default_key="chat_openai", 
    openai=llm,
    anthropic=anthropic,
)
configurable_chain = (
    {"topic": RunnablePassthrough()} 
    | prompt 
    | configurable_model 
    | output_parser
)
```


```python
configurable_chain.invoke(
    "ice cream", 
    config={"model": "openai"}
)
stream = configurable_chain.stream(
    "ice cream", 
    config={"model": "anthropic"}
)
for chunk in stream:
    print(chunk, end="", flush=True)

configurable_chain.batch(["ice cream", "spaghetti", "dumplings"])

# await configurable_chain.ainvoke("ice cream")
```

```{=mdx}
</Column>
</ColumnContainer>
```

## 日志记录

如果我们想要记录我们的中间结果：

```{=mdx}
<ColumnContainer>
<Column>
```

#### 没有LCEL

为了说明的目的，我们将`print`中间结果




```python
def invoke_anthropic_chain_with_logging(topic: str) -> str:
    print(f"输入: {topic}")
    prompt_value = anthropic_template.format(topic=topic)
    print(f"格式化后的提示: {prompt_value}")
    output = call_anthropic(prompt_value)
    print(f"输出: {output}")
    return output

invoke_anthropic_chain_with_logging("ice cream")
```

```{=mdx}
</Column>

<Column>
```

#### 有LCEL
每个组件都内置了与LangSmith的集成。如果我们设置了以下两个环境变量，所有链路追踪都将记录到LangSmith中。



```python
import os

os.environ["LANGCHAIN_API_KEY"] = "..."
os.environ["LANGCHAIN_TRACING_V2"] = "true"

anthropic_chain.invoke("ice cream")
```

这是我们的LangSmith追踪的样子：https://smith.langchain.com/public/e4de52f8-bcd9-4732-b950-deee4b04e313/r

```{=mdx}
</Column>
</ColumnContainer>
```

## 备用选择

如果我们想要添加备用逻辑，以防一个模型API失效：

```{=mdx}
<ColumnContainer>
<Column>
```

#### 没有LCEL





```python
def invoke_chain_with_fallback(topic: str) -> str:
    try:
        return invoke_chain(topic)
    except Exception:
        return invoke_anthropic_chain(topic)

async def ainvoke_chain_with_fallback(topic: str) -> str:
    try:
        return await ainvoke_chain(topic)
    except Exception:
我提供的mdx文档的内容需要翻译，只要翻译md语法中的标题、段落和列表的内容，驼峰和下划线单词不必翻译，请保留md语法标点符号，你翻译完后对原内容进行替换，将结果返回给我。mdx文档是:------
        # 注意：我们实际上还没有实现这个。
        return await ainvoke_anthropic_chain(topic)

async def batch_chain_with_fallback(topics: List[str]) -> str:
    try:
        return batch_chain(topics)
    except Exception:
        # 注意：我们实际上还没有实现这个。
        return batch_anthropic_chain(topics)

invoke_chain_with_fallback("ice cream")
# await ainvoke_chain_with_fallback("ice cream")
batch_chain_with_fallback(["ice cream", "spaghetti", "dumplings"]))
```

```{=mdx}
</Column>

<Column>
```

#### LCEL




```python
fallback_chain = chain.with_fallbacks([anthropic_chain])

fallback_chain.invoke("ice cream")
# await fallback_chain.ainvoke("ice cream")
fallback_chain.batch(["ice cream", "spaghetti", "dumplings"])
```

```{=mdx}
</Column>
</ColumnContainer>
```

## 完整代码比较

即使在这个简单的例子中，我们的LCEL链将很多功能简洁地集成在一起。随着链变得更加复杂，这变得尤为有价值。

```{=mdx}
<ColumnContainer>
<Column>
```

#### 没有LCEL




```python
from concurrent.futures import ThreadPoolExecutor
from typing import Iterator, List, Tuple

import anthropic
import openai


prompt_template = "告诉我一个关于{topic}的笑话"
anthropic_template = f"人类：\n\n{prompt_template}\n\n助手:"
client = openai.OpenAI()
async_client = openai.AsyncOpenAI()
anthropic_client = anthropic.Anthropic()

def call_chat_model(messages: List[dict]) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=messages,
    )
    return response.choices[0].message.content

def invoke_chain(topic: str) -> str:
    print(f"输入: {topic}")
    prompt_value = prompt_template.format(topic=topic)
    print(f"格式化的提示语: {prompt_value}")
    messages = [{"role": "user", "content": prompt_value}]
    output = call_chat_model(messages)
    print(f"输出: {output}")
    return output

def stream_chat_model(messages: List[dict]) -> Iterator[str]:
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )
    for response in stream:
        content = response.choices[0].delta.content
        if content is not None:
            yield content

def stream_chain(topic: str) -> Iterator[str]:
    print(f"输入: {topic}")
    prompt_value = prompt.format(topic=topic)
    print(f"格式化的提示语: {prompt_value}")
    stream = stream_chat_model([{"role": "user", "content": prompt_value}])
    for chunk in stream:
        print(f"标记: {chunk}", end="")
        yield chunk

def batch_chain(topics: list) -> list:
    with ThreadPoolExecutor(max_workers=5) as executor:
        return list(executor.map(invoke_chain, topics))

def call_llm(prompt_value: str) -> str:
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt_value,
    )
    return response.choices[0].text

def invoke_llm_chain(topic: str) -> str:
    print(f"输入: {topic}")
    prompt_value = promtp_template.format(topic=topic)
    print(f"格式化的提示语: {prompt_value}")
    output = call_llm(prompt_value)
    print(f"输出: {output}")
    return output

def call_anthropic(prompt_value: str) -> str:
    response = anthropic_client.completions.create(
        model="claude-2",
        prompt=prompt_value,
        max_tokens_to_sample=256,
    )
    return response.completion   

def invoke_anthropic_chain(topic: str) -> str:
    print(f"输入: {topic}")
    prompt_value = anthropic_template.format(topic=topic)
    print(f"格式化的提示语: {prompt_value}")
    output = call_anthropic(prompt_value)
    print(f"输出: {output}")
    return output

async def ainvoke_anthropic_chain(topic: str) -> str:
    ...

def stream_anthropic_chain(topic: str) -> Iterator[str]:
    ...

def batch_anthropic_chain(topics: List[str]) -> List[str]:
    ...

def invoke_configurable_chain(
    topic: str, 
    *, 
    model: str = "chat_openai"
) -> str:
    if model == "chat_openai":
        return invoke_chain(topic)
    elif model == "openai":
        return invoke_llm_chain(topic)
    elif model == "anthropic":
        return invoke_anthropic_chain(topic)
    else:
        raise ValueError(
            f"接收到无效的模型'{model}'。"
            " 期望chat_openai、openai、anthropic之一。"
        )

def stream_configurable_chain(
    topic: str, 
    *, 
    model: str = "chat_openai"
) -> Iterator[str]:
    if model == "chat_openai":
        return stream_chain(topic)
    elif model == "openai":
        # 注意我们还没有实现这个。
        return stream_llm_chain(topic)
    elif model == "anthropic":
        # 注意我们还没有实现这个
        return stream_anthropic_chain(topic)
    else:
        raise ValueError(
            f"接收到无效的模型'{model}'。"
            " 期望chat_openai、openai、anthropic之一。"
        )

def batch_configurable_chain(
    topics: List[str], 
    *, 
    model: str = "chat_openai"
) -> List[str]:
    ...

async def abatch_configurable_chain(
    topics: List[str], 
    *, 
    model: str = "chat_openai"
) -> List[str]:
    ...

def invoke_chain_with_fallback(topic: str) -> str:
    try:
        return invoke_chain(topic)
    except Exception:
        return invoke_anthropic_chain(topic)

async def ainvoke_chain_with_fallback(topic: str) -> str:
    try:
        return await ainvoke_chain(topic)
    except Exception:
        return await ainvoke_anthropic_chain(topic)

async def batch_chain_with_fallback(topics: List[str]) -> str:
    try:
        return batch_chain(topics)
    except Exception:
        return batch_anthropic_chain(topics)
```

```{=mdx}
</Column>

<Column>
```

------
                你的回答是：                #### LCEL

```python
import os

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, ConfigurableField

os.environ["LANGCHAIN_API_KEY"] = "..."
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_template(
    "告诉我一个关于{topic}的短笑话"
)
chat_openai = ChatOpenAI(model="gpt-3.5-turbo")
openai = OpenAI(model="gpt-3.5-turbo-instruct")
anthropic = ChatAnthropic(model="claude-2")
model = (
    chat_openai
    .with_fallbacks([anthropic])
    .configurable_alternatives(
        ConfigurableField(id="model"),
        default_key="chat_openai",
        openai=openai,
        anthropic=anthropic,
    )
)

chain = (
    {"topic": RunnablePassthrough()} 
    | prompt 
    | model 
    | StrOutputParser()
)
```

```{=mdx}
</Column>
</ColumnContainer>
```

## 下一步骤

要继续学习LCEL，我们建议：
- 阅读完整的LCEL [接口](/expression_language/interface)，这里我们只是部分介绍。
- 探索 [primitives](/expression_language/primitives) 以了解LCEL提供了什么。
------