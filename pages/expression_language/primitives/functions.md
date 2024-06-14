# 运行自定义函数

您可以在流水线中使用任意的函数。

请注意，这些函数的所有输入都需要是一个参数。如果您有一个接受多个参数的函数，您应该编写一个接受单个输入并将其拆分成多个参数的包装器函数。
%pip install --upgrade --quiet langchain langchain-openai

```python
from operator import itemgetter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI


def length_function(text):
    return len(text)


def _multiple_length_function(text1, text2):
    return len(text1) * len(text2)


def multiple_length_function(_dict):
    return _multiple_length_function(_dict["text1"], _dict["text2"])


prompt = ChatPromptTemplate.from_template("what is {a} + {b}")
model = ChatOpenAI()

chain1 = prompt | model

chain = (
    {
        "a": itemgetter("foo") | RunnableLambda(length_function),
        "b": {"text1": itemgetter("foo"), "text2": itemgetter("bar")}
        | RunnableLambda(multiple_length_function),
    }
    | prompt
    | model
)
```


```python
chain.invoke({"foo": "bar", "bar": "gah"})
```




    AIMessage(content='3 + 9 = 12', response_metadata={'token_usage': {'completion_tokens': 7, 'prompt_tokens': 14, 'total_tokens': 21}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': 'fp_b28b39ffa8', 'finish_reason': 'stop', 'logprobs': None}, id='run-bd204541-81fd-429a-ad92-dd1913af9b1c-0')



## 接受 Runnable 配置

Runnable lambdas 可以选择性地接受一个 [RunnableConfig](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig)，它们可以使用它来传递回调函数、标签和其他配置信息给嵌套的运行。

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableConfig
```


```python
import json


def parse_or_fix(text: str, config: RunnableConfig):
    fixing_chain = (
        ChatPromptTemplate.from_template(
            "Fix the following text:\n\n```text\n{input}\n```\nError: {error}"
            " Don't narrate, just respond with the fixed data."
        )
        | ChatOpenAI()
        | StrOutputParser()
    )
    for _ in range(3):
        try:
            return json.loads(text)
        except Exception as e:
            text = fixing_chain.invoke({"input": text, "error": e}, config)
    return "Failed to parse"
```


```python
from langchain_community.callbacks import get_openai_callback

with get_openai_callback() as cb:
    output = RunnableLambda(parse_or_fix).invoke(
        "{foo: bar}", {"tags": ["my-tag"], "callbacks": [cb]}
    )
    print(output)
    print(cb)
```

    {'foo': 'bar'}
    Tokens Used: 62
    	Prompt Tokens: 56
    	Completion Tokens: 6
    Successful Requests: 1
    Total Cost (USD): $9.6e-05
    

# 流式传输

您可以在 LCEL 流水线中使用生成器函数（即使用 `yield` 关键词的函数，并且行为类似于迭代器）。

这些生成器的签名应为 `Iterator[Input] -> Iterator[Output]`。或者对于异步生成器：`AsyncIterator[Input] -> AsyncIterator[Output]`。

这些对于以下情况非常有用：
- 实现自定义的输出解析器
- 修改先前步骤的输出，同时保持流式传输能力

这是一个用于逗号分隔列表的自定义输出解析器的示例：


```python
from typing import Iterator, List

prompt = ChatPromptTemplate.from_template(
    "Write a comma-separated list of 5 animals similar to: {animal}. Do not include numbers"
)
model = ChatOpenAI(temperature=0.0)

str_chain = prompt | model | StrOutputParser()
```


```python
for chunk in str_chain.stream({"animal": "bear"}):
    print(chunk, end="", flush=True)
```

    lion, tiger, wolf, gorilla, panda


```python
str_chain.invoke({"animal": "bear"})
```




    'lion, tiger, wolf, gorilla, panda'




```python
# This is a custom parser that splits an iterator of llm tokens
# into a list of strings separated by commas
def split_into_list(input: Iterator[str]) -> Iterator[List[str]]:
    # hold partial input until we get a comma
    buffer = ""
    for chunk in input:
        # add current chunk to buffer
        buffer += chunk
        # while there are commas in the buffer
        while "," in buffer:
            # split buffer on comma
            comma_index = buffer.index(",")
            # yield everything before the comma
            yield [buffer[:comma_index].strip()]
            # save the rest for the next iteration
            buffer = buffer[comma_index + 1 :]
    # yield the last chunk
    yield [buffer.strip()]
```


```python
list_chain = str_chain | split_into_list
```


```python
for chunk in list_chain.stream({"animal": "bear"}):
    print(chunk, flush=True)
```

    ['lion']
    ['tiger']
    ['wolf']
    ['gorilla']
    ['panda']
    


```python
list_chain.invoke({"animal": "bear"})
```




    ['lion', 'tiger', 'wolf', 'gorilla', 'elephant']



------## 异步版本


```python
from typing import AsyncIterator


async def asplit_into_list(
    input: AsyncIterator[str],
) -> AsyncIterator[List[str]]:  # 异步函数
    buffer = ""
    async for (
        chunk
    ) in input:  # `input` 是一个 `async_generator` 对象，所以使用 `async for`
        buffer += chunk
        while "," in buffer:
            comma_index = buffer.index(",")
            yield [buffer[:comma_index].strip()]
            buffer = buffer[comma_index + 1 :]
    yield [buffer.strip()]


list_chain = str_chain | asplit_into_list
```


```python
async for chunk in list_chain.astream({"animal": "bear"}):
    print(chunk, flush=True)
```

    ['狮子']
    ['老虎']
    ['狼']
    ['大猩猩']
    ['熊猫']
    


```python
await list_chain.ainvoke({"animal": "bear"})
```




    ['狮子', '老虎', '狼', '大猩猩', '熊猫']


------