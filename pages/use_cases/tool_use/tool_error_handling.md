# 工具错误处理

使用模型调用工具存在一些明显的潜在故障模式。首先，模型需要返回一个可解析的输出。其次，模型需要返回有效的工具参数。

我们可以在我们的链中构建错误处理来减轻这些故障模式。

## 设置

我们需要安装以下软件包：

```python
%pip install --upgrade --quiet langchain langchain-openai
```

并设置这些环境变量：

```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 如果您想使用LangSmith，请取消下面的注释：
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 链

假设我们有以下（虚拟的）工具和工具调用链。我们将故意让工具复杂以尝试使模型出错。

```python
# 定义工具
from langchain_core.tools import tool


@tool
def complex_tool(int_arg: int, float_arg: float, dict_arg: dict) -> int:
    """使用复杂的工具做一些复杂的事情。"""
    return int_arg * float_arg
```

```python
# 定义模型并绑定工具
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
model_with_tools = model.bind_tools(
    [complex_tool],
    tool_choice="complex_tool",
)
```

```python
# 定义链式调用
from operator import itemgetter

from langchain.output_parsers import JsonOutputKeyToolsParser
from langchain_core.runnables import Runnable, RunnableLambda, RunnablePassthrough

chain = (
    model_with_tools
    | JsonOutputKeyToolsParser(key_name="complex_tool", first_tool_only=True)
    | complex_tool
)
```

我们可以看到，即使我们尝试使用一个相当明确的输入调用此链，模型也无法正确调用工具（它忘记了`dict_arg`参数）。

```python
chain.invoke(
    "使用复杂的工具。参数为5、2.1、空字典。不要忘记dict_arg"
)
```

```
ValidationError: 调用工具时出错。以下是引发的错误:

<class 'pydantic.v1.error_wrappers.ValidationError'>: 1个验证错误 for complex_toolSchemaSchema
dict_arg
  field required (type=value_error.missing)
```

## 使用try/except调用工具

更优雅地处理错误的最简单方法是在调用工具的步骤中使用try/except，并在发生错误时返回一条有用的消息。

```python
from typing import Any

from langchain_core.runnables import RunnableConfig


def try_except_tool(tool_args: dict, config: RunnableConfig) -> Runnable:
    try:
        complex_tool.invoke(tool_args, config=config)
    except Exception as e:
        return f"使用以下参数调用工具：\n\n{tool_args}\n\n引发以下错误：\n\n{type(e)}: {e}"


chain = (
    model_with_tools
    | JsonOutputKeyToolsParser(key_name="complex_tool", first_tool_only=True)
    | try_except_tool
)
```

```python
print(
    chain.invoke(
        "使用复杂的工具。参数为5、2.1、空字典。不要忘记dict_arg"
    )
)
```

```
使用以下参数调用工具：

{'int_arg': 5, 'float_arg': 2.1}

引发以下错误：

<class 'pydantic.v1.error_wrappers.ValidationError'>: 1个验证错误 for complex_toolSchemaSchema
dict_arg
  field required (type=value_error.missing)
```
------


## 回退

在工具调用错误的情况下，我们还可以尝试回退到更好的模型。在这种情况下，我们将回退到一个使用 `gpt-4-1106-preview` 而不是 `gpt-3.5-turbo` 的相同链。

```python
chain = (
    model_with_tools
    | JsonOutputKeyToolsParser(key_name="complex_tool", first_tool_only=True)
    | complex_tool
)
better_model = ChatOpenAI(model="gpt-4-1106-preview", temperature=0).bind_tools(
    [complex_tool], tool_choice="complex_tool"
)
better_chain = (
    better_model
    | JsonOutputKeyToolsParser(key_name="complex_tool", first_tool_only=True)
    | complex_tool
)

chain_with_fallback = chain.with_fallbacks([better_chain])
chain_with_fallback.invoke(
    "使用复杂工具。参数为 5, 2.1, 空字典。不要忘记 dict_arg。"
)
```

观察这次链式运行的 [Langsmith trace](https://smith.langchain.com/public/241e1266-8555-4d49-99dc-b8df46109c39/r)，我们可以看到第一个链式调用失败了，而回退成功了。

## 异常重试

为了进一步，我们可以尝试自动重新运行带有传入异常的链式调用，以便模型可以纠正其行为。

```python
import json
from typing import Any

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough


class CustomToolException(Exception):
    """自定义 LangChain 工具异常。"""

    def __init__(self, tool_call: dict, exception: Exception) -> None:
        super().__init__()
        self.tool_call = tool_call
        self.exception = exception


def tool_custom_exception(tool_call: dict, config: RunnableConfig) -> Runnable:
    try:
        return complex_tool.invoke(tool_call["args"], config=config)
    except Exception as e:
        raise CustomToolException(tool_call, e)


def exception_to_messages(inputs: dict) -> dict:
    exception = inputs.pop("exception")
    tool_call = {
        "type": "function",
        "function": {
            "name": "complex_tool",
            "arguments": json.dumps(exception.tool_call["args"]),
        },
        "id": exception.tool_call["id"],
    }

    # 将历史消息添加到原始输入中，以便模型知道它在最后一次工具调用中犯了一个错误。
    messages = [
        AIMessage(content="", additional_kwargs={"tool_calls": [tool_call]}),
        ToolMessage(tool_call_id=tool_call["id"], content=str(exception.exception)),
        HumanMessage(
            content="上次工具调用引发了异常。请尝试使用更正的参数再次调用工具。"
        ),
    ]
    inputs["last_output"] = messages
    return inputs


# 在提示中添加一个 last_output MessagesPlaceholder，如果不传递它，它不会对提示产生任何影响，但是我们可以选择插入一个任意的消息列表到提示中，如果需要的话。我们将在重试时使用此功能插入错误消息。
prompt = ChatPromptTemplate.from_messages(
    [("human", "{input}"), MessagesPlaceholder("last_output", optional=True)]
)
chain = (
    prompt
    | model_with_tools
    | JsonOutputKeyToolsParser(
        key_name="complex_tool", return_id=True, first_tool_only=True
    )
    | tool_custom_exception
)

# 如果初始的链式调用失败，我们将使用传入的异常作为消息重新运行它。
self_correcting_chain = chain.with_fallbacks(
    [exception_to_messages | chain], exception_key="exception"
)
```

```python
self_correcting_chain.invoke(
    {
        "input": "使用复杂工具。参数为 5, 2.1, 空字典。不要忘记 dict_arg"
    }
)
```

我们的链式调用成功了！观察这次链式运行的 [LangSmith trace](https://smith.langchain.com/public/b780b740-daf5-43aa-a217-6d4600aba41b/r)，我们可以看到我们的初始链式调用仍然失败了，只有在重试时链式调用才成功。

