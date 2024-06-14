# 选择多个工具

在我们的[快速入门](/use_cases/tool_use/quickstart)中，我们介绍了如何构建一个调用单个`multiply`工具的链。现在让我们来看看如何扩展这个链，使其能够从多个工具中选择调用。我们将重点介绍链条，因为默认情况下[代理](/use_cases/tool_use/agents)可以在多个工具之间路由。

## 设置

我们需要为本指南安装以下软件包:


```python
%pip install --upgrade --quiet langchain langchain-openai
```

并设置以下环境变量:


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 如果您想使用LangSmith，请取消下面的注释
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 工具

回顾一下，我们已经有了一个`multiply`工具:


```python
from langchain_core.tools import tool


@tool
def multiply(first_int: int, second_int: int) -> int:
    """将两个整数相乘。"""
    return first_int * second_int
```

现在我们可以在它基础上添加一个`exponentiate`和一个`add`工具:


```python
@tool
def add(first_int: int, second_int: int) -> int:
    "将两个整数相加。"
    return first_int + second_int


@tool
def exponentiate(base: int, exponent: int) -> int:
    "将基数的指数幂。"
    return base**exponent
```

使用一个工具和使用多个工具之间的主要区别在于，对于多个工具，我们无法确定模型将调用哪个工具。因此，我们不能像在[快速入门](/use_cases/tool_use/quickstart)中那样硬编码将特定工具放入我们的链条中。相反，我们将添加一个`call_tool_list`，即一个`RunnableLambda`，它接受`JsonOutputToolsParser`的输出并根据它实际构建链条的末尾，这意味着在运行时附加到链条末尾被调用的工具。我们可以这样做，因为LCEL有一个很酷的特性，即在任何可运行序列（LCEL的核心构建块）中，如果一个组件返回更多的可运行项，则这些项作为链条的一部分运行。


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

model = ChatOpenAI(model="gpt-3.5-turbo")
tools = [multiply, exponentiate, add]
model_with_tools = model.bind_tools(tools)
tool_map = {tool.name: tool for tool in tools}


def call_tool(tool_invocation: dict) -> Union[str, Runnable]:
    """根据模型选择的工具动态构建链条末尾的函数。"""
    tool = tool_map[tool_invocation["type"]]
    return RunnablePassthrough.assign(output=itemgetter("args") | tool)


# .map()允许我们将函数应用于输入列表。
call_tool_list = RunnableLambda(call_tool).map()
chain = model_with_tools | JsonOutputToolsParser() | call_tool_list
```


```python
chain.invoke("23乘以7是多少")
```




    [{'type': 'multiply',
      'args': {'first_int': 23, 'second_int': 7},
      'output': 161}]




```python
chain.invoke("一百万加上十亿是多少")
```




    [{'type': 'add',
      'args': {'first_int': 1000000, 'second_int': 1000000000},
      'output': 1001000000}]




```python
chain.invoke("立方37")
```




    [{'type': 'exponentiate',
      'args': {'base': 37, 'exponent': 3},
      'output': 50653}]