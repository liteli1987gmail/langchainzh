# JSON

>[JSON (JavaScript Object Notation)](https://en.wikipedia.org/wiki/JSON) 是一种使用人类可读文本来存储和传输数据对象的开放标准文件格式和数据交换格式，包含属性-值对和数组（或其他可序列化值）。

>[JSON Lines](https://jsonlines.org/) 是一个文件格式，其中每一行都是一个有效的JSON值。

>`JSONLoader` 使用指定的 [jq schema](https://en.wikipedia.org/wiki/Jq_(programming_language)) 来解析JSON文件。它使用 `jq` python包。请查看这个 [手册](https://stedolan.github.io/jq/manual/#Basicfilters)，详细了解 `jq` 语法的文档。

```python
#!pip install jq
```

```python
from langchain_community.document_loaders import JSONLoader
```

```python
import json
from pathlib import Path
from pprint import pprint

file_path='./example_data/facebook_chat.json'
data = json.loads(Path(file_path).read_text())
```

```python
pprint(data)
```

## 使用 `JSONLoader`

假设我们有兴趣提取JSON数据中`messages`键下的`content`字段的值。这可以通过下面的 `JSONLoader` 轻松实现。

### JSON文件

```python
loader = JSONLoader(
    file_path='./example_data/facebook_chat.json',
    jq_schema='.messages[].content',
    text_content=False)

data = loader.load()
```

```python
pprint(data)
```

### JSON Lines文件

如果您想从一个JSON Lines文件加载文档，您需要传递 `json_lines=True` 并指定从单个JSON对象中提取 `page_content` 的 `jq_schema`。

```python
file_path = './example_data/facebook_chat_messages.jsonl'
pprint(Path(file_path).read_text())
```

```python
loader = JSONLoader(
    file_path='./example_data/facebook_chat_messages.jsonl',
    jq_schema='.content',
    text_content=False,
    json_lines=True)

data = loader.load()
```

```python
pprint(data)
```

另一个选择是设置 `jq_schema='.'` 并提供 `content_key`：

```python
loader = JSONLoader(
    file_path='./example_data/facebook_chat_messages.jsonl',
    jq_schema='.',
    content_key='sender_name',
    json_lines=True)

data = loader.load()
```

```python
pprint(data)
```

### 具有jq模式`content_key`的JSON文件

要使用 jq 模式内的 content_key 从 JSON 文件加载文档，请设置 is_content_key_jq_parsable=True。确保 content_key 兼容并可以使用 jq 模式解析。

```python
file_path = './sample.json'
pprint(Path(file_path).read_text())
```

```python
loader = JSONLoader(
    file_path=file_path,
    jq_schema=".data[]",
    content_key=".attributes.message",
    is_content_key_jq_parsable=True,
)

data = loader.load()
```

```python
pprint(data)
```

## 提取元数据

通常，我们希望将JSON文件中的元数据包括到从内容中创建的文档中。

以下演示了如何使用 `JSONLoader` 提取元数据。

需要注意的关键变化是。在之前我们没有收集元数据的示例中，我们可以直接在模式中指定 `page_content` 的值应该从哪里提取。

```
.messages[].content
```

在当前示例中，我们需要告诉加载器在 `messages` 字段中迭代记录。然后， jq_schema 必须是：

```
.messages[]
```

这允许我们将记录（字典）传递到必须实现的 `metadata_func` 中。`metadata_func` 负责识别记录中的哪些信息应包含在最终的 `Document` 对象中存储的元数据中。

此外，现在我们必须明确在加载器中通过 `content_key` 参数指定从记录的哪个键中提取 `page_content` 的值。


```python
# 定义元数据提取函数。
def metadata_func(record: dict, metadata: dict) -> dict:

    metadata["sender_name"] = record.get("sender_name")
    metadata["timestamp_ms"] = record.get("timestamp_ms")

    return metadata


loader = JSONLoader(
    file_path='./example_data/facebook_chat.json',
    jq_schema='.messages[]',
    content_key="content",
    metadata_func=metadata_func
)

data = loader.load()
```

```python
pprint(data)
```

## `metadata_func`

如上所示，`metadata_func` 接受 `JSONLoader` 生成的默认元数据。这使用户完全控制元数据的格式。

例如，默认元数据包含 `source` 和 `seq_num` 键。但是，可能 JSON 数据中也包含这些键。用户可以利用 `metadata_func` 从 JSON 数据中重命名默认键并使用它们。

下面的示例显示了如何修改 `source` 以仅包含文件源相对于 `langchain` 目录的信息。

```python
# 定义元数据提取函数。
def metadata_func(record: dict, metadata: dict) -> dict:

    metadata["sender_name"] = record.get("sender_name")
    metadata["timestamp_ms"] = record.get("timestamp_ms")

    if "source" in metadata:
        source = metadata["source"].split("/")
        source = source[source.index("langchain"):]
        metadata["source"] = "/".join(source)

    return metadata


loader = JSONLoader(
    file_path='./example_data/facebook_chat.json',
    jq_schema='.messages[]',
    content_key="content",
    metadata_func=metadata_func
)

data = loader.load()
```

```python
pprint(data)
```

## 带有jq模式的常见JSON结构

下面的列表提供了一个参考，用户可以根据结构从JSON数据中提取内容的可能的 `jq_schema`。

```
JSON        -> [{"text": ...}, {"text": ...}, {"text": ...}]
jq_schema   -> ".[].text"

JSON        -> {"key": [{"text": ...}, {"text": ...}, {"text": ...}]}
jq_schema   -> ".key[].text"

JSON        -> ["...", "...", "..."]
jq_schema   -> ".[]"

```
------
# JSON解析器

这个输出解析器允许用户指定任意的JSON模式，并查询符合该模式的LLMs的输出。

请记住，大型语言模型是有漏洞的抽象！您必须使用足够容量的LLM来生成格式良好的JSON。在OpenAI系列中，DaVinci可以可靠地完成此任务，但Curie的能力已经显著降低。

您可以选择使用Pydantic来声明您的数据模型。

```python
from typing import List

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
```

```python
model = ChatOpenAI(temperature=0)
```

# 定义您所需的数据结构。

class Joke(BaseModel):
    setup: str = Field(description="问题设置一个笑话")
    punchline: str = Field(description="用于解决笑话的答案")
```

# 并且一个查询用于提示语言模型填充数据结构。
joke_query = "告诉我一个笑话。"

# 设置解析器+将说明注入到提示模板中。
parser = JsonOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

chain.invoke({"query": joke_query})
```
返回结果：
{'setup': "为什么科学家不相信原子？", 'punchline': '因为他们组成了一切！'}

## 流式传输

此输出解析器支持流式传输。

```python
for s in chain.stream({"query": joke_query}):
    print(s)
```
```
结果：
{'setup': ''}
{'setup': '为什么'}
{'setup': '为什么不'}
{'setup': '为什么不相'}
{'setup': '为什么不相信'}
{'setup': '为什么不相信科'}
{'setup': '为什么不相信科学家'}
{'setup': '为什么不相信科学家？', 'punchline': ''}
{'setup': '为什么不相信科学家？', 'punchline': '因为'}
{'setup': '为什么不相信科学家？', 'punchline': '因为他们'}
{'setup': '为什么不相信科学家？', 'punchline': '因为他们构'}
{'setup': '为什么不相信科学家？', 'punchline': '因为他们构成'}
{'setup': '为什么不相信科学家？', 'punchline': '因为他们构成一切'}
{'setup': '为什么不相信科学家？', 'punchline': '因为他们构成一切！'}
```

## 不需要Pydantic

您也可以在不使用Pydantic的情况下使用此功能。这将提示它返回JSON，但不提供有关模式应该是什么的详细信息。

```python
joke_query = "告诉我一个笑话。"

parser = JsonOutputParser()

prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

chain.invoke({"query": joke_query})
```

返回结果：
{'joke': "为什么科学家不相信原子？因为他们组成了一切！"}