# 并行工具使用

在[带有多个工具的链条](/use_cases/tool_use/multiple_tools)指南中，我们看到了如何构建函数调用链，这些链可以在多个工具之间进行选择。一些模型，比如2023年秋季发布的OpenAI模型，还支持并行函数调用，这使得你可以在单个模型调用中调用多个函数（或多次调用同一个函数）。我们在多个工具指南中的先前链条实际上已经支持了这一点，我们只需要使用一个支持并行函数调用的OpenAI模型即可。

## 设置

为了完成本指南，我们需要安装以下包：


```python
%pip install --upgrade --quiet langchain langchain-openai
```

并设置以下环境变量：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 如果你想使用LangSmith，请取消下面的注释
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 工具


```python
from langchain_core.tools import tool


@tool
def multiply(first_int: int, second_int: int) -> int:
    """Multiply two integers together."""
    return first_int * second_int


@tool
def add(first_int: int, second_int: int) -> int:
    "Add two integers."
    return first_int + second_int


@tool
def exponentiate(base: int, exponent: int) -> int:
    "Exponentiate the base to the exponent power."
    return base**exponent
```

# 链条

请注意，我们使用了一个`-1106`型号的模型，截至本文撰写时，这是唯一支持并行函数调用的类型：


```python
from operator import itemgetter
from typing import Union

from langchain.output_parsers import JsonOutputToolsParser
from langchain_core.runnables import (
    Runnable,
    RunnableLambda,
    RunnableMap,
    RunnablePassthrough,
)
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo-1106")
tools = [multiply, exponentiate, add]
model_with_tools = model.bind_tools(tools)
tool_map = {tool.name: tool for tool in tools}


def call_tool(tool_invocation: dict) -> Union[str, Runnable]:
    """Function for dynamically constructing the end of the chain based on the model-selected tool."""
    tool = tool_map[tool_invocation["type"]]
    return RunnablePassthrough.assign(output=itemgetter("args") | tool)


# .map() allows us to apply a function to a list of inputs.
call_tool_list = RunnableLambda(call_tool).map()
chain = model_with_tools | JsonOutputToolsParser() | call_tool_list
```


```python
chain.invoke(
    "What's 23 times 7, and what's five times 18 and add a million plus a billion and cube thirty-seven"
)
```




    [{'type': 'multiply',
      'args': {'first_int': 23, 'second_int': 7},
      'output': 161},
     {'type': 'add', 'args': {'first_int': 5, 'second_int': 18}, 'output': 23},
     {'type': 'add',
      'args': {'first_int': 1000000, 'second_int': 1000000000},
      'output': 1001000000},
     {'type': 'exponentiate',
      'args': {'base': 37, 'exponent': 3},
      'output': 50653}]

------



