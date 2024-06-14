# 定义自定义工具

在构建您自己的代理时，您需要为其提供一个可使用的工具列表。除了调用的实际函数外，工具包括几个组件：

- `name`（str），是必需的，必须在提供给代理的工具集中是唯一的
- `description`（str），是可选的但建议的，因为代理用它来确定工具的使用
- `args_schema`（Pydantic BaseModel），是可选的但建议的，可用于提供更多信息（例如，few-shot examples）或验证预期参数。

有多种方法可以定义工具。在本指南中，我们将介绍两个函数的定义方式：

1. 一个虚构的搜索功能，它始终返回字符串"LangChain"
2. 一个乘法器功能，将两个数字相乘

这里最大的区别是第一个函数只需要一个输入，而第二个函数需要多个。许多代理只能使用需要单个输入的函数，因此了解如何处理这些函数很重要。在大多数情况下，定义这些自定义工具是相同的，但也有一些不同之处。

```python
# 导入通用需要的内容
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
```

## @tool 装饰器

这个`@tool`装饰器是定义自定义工具的最简单方式。该装饰器默认使用函数名作为工具名，但可以通过传递字符串作为第一个参数来覆盖。此外，装饰器将使用函数的文档字符串作为工具的描述 - 因此必须提供文档字符串。

```python
@tool
def search(query: str) -> str:
    """在线查找内容。"""
    return "LangChain"
```

```python
print(search.name)
print(search.description)
print(search.args)
```

    search
    search(query: str) -> str - 在线查找内容。
    {'query': {'title': 'Query', 'type': 'string'}}
    
```python
@tool
def multiply(a: int, b: int) -> int:
    """乘以两个数字。"""
    return a * b
```

```python
print(multiply.name)
print(multiply.description)
print(multiply.args)
```

    multiply
    multiply(a: int, b: int) -> int - 乘以两个数字。
    {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
    
您还可以通过将它们传递给工具装饰器来自定义工具名称和JSON args。

```python
class SearchInput(BaseModel):
    query: str = Field(description="应该是搜索查询")


@tool("search-tool", args_schema=SearchInput, return_direct=True)
def search(query: str) -> str:
    """在线查找内容。"""
    return "LangChain"
```

```python
print(search.name)
print(search.description)
print(search.args)
print(search.return_direct)
```

    search-tool
    search-tool(query: str) -> str - 在线查找内容。
    {'query': {'title': 'Query', 'description': '应该是搜索查询', 'type': 'string'}}
    True

## 继承 BaseTool 类

您还可以通过将自定义工具子类化为BaseTool类来明确定义自定义工具。这提供了对工具定义的最大控制，但需要更多的工作。

```python
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

class SearchInput(BaseModel):
    query: str = Field(description="应该是一个搜索查询")

class CalculatorInput(BaseModel):
    a: int = Field(description="第一个数字")
    b: int = Field(description="第二个数字")

class CustomSearchTool(BaseTool):
    name = "custom_search"
    description = "在需要回答有关当前事件的问题时有用"
    args_schema: Type[BaseModel] = SearchInput

    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """使用该工具。"""
        return "LangChain"

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """异步使用该工具。"""
        raise NotImplementedError("custom_search不支持异步")

class CustomCalculatorTool(BaseTool):
    name = "Calculator"
    description = "在需要回答有关数学问题时有用"
    args_schema: Type[BaseModel] = CalculatorInput
    return_direct: bool = True

    def _run(
        self, a: int, b: int, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """使用该工具。"""
        return a * b

    async def _arun(
        self, a: int, b: int, run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """异步使用该工具。"""
        raise NotImplementedError("Calculator不支持异步")
````

```python
search = CustomSearchTool()
print(search.name)
print(search.description)
print(search.args)
```

    custom_search
    在需要回答有关当前事件的问题时有用
    {'query': {'title': 'Query', 'description': '应该是一个搜索查询', 'type': 'string'}}

```python
multiply = CustomCalculatorTool()
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.return_direct)
```

    Calculator
    在需要回答有关数学问题时有用
    {'a': {'title': 'A', 'description': '第一个数字', 'type': 'integer'}, 'b': {'title': 'B', 'description': '第二个数字', 'type': 'integer'}}
    True
## StructuredTool 数据类

您还可以使用`StructuredTool`数据类。这种方法是前两种方法的混合。它比从BaseTool类继承更方便，但提供的功能比仅使用装饰器更多。

```python
def search_function(query: str):
    return "LangChain"

search = StructuredTool.from_function(
    func=search_function,
    name="Search",
    description="在需要回答有关当前事件的问题时很有用",
    # coroutine= ... <- 如果需要，您也可以指定一个异步方法
)
```
```python
print(search.name)
print(search.description)
print(search.args)
```

    搜索
    Search(query: str) - 当您需要回答有关当前事件的问题时非常有用
    {'query': {'title': '查询', 'type': 'string'}}

您还可以定义自定义的 `args_schema` 来提供有关输入的更多信息。

```python
class CalculatorInput(BaseModel):
    a: int = Field(description="第一个数字")
    b: int = Field(description="第二个数字")


def multiply(a: int, b: int) -> int:
    """乘以两个数字。"""
    return a * b


calculator = StructuredTool.from_function(
    func=multiply,
    name="Calculator",
    description="乘以数字",
    args_schema=CalculatorInput,
    return_direct=True,
    # coroutine= ... <- 如果需要，您也可以指定一个异步方法
)
```

```python
print(calculator.name)
print(calculator.description)
print(calculator.args)
```

    计算器
    Calculator(a: int, b: int) -> int - 乘以数字
    {'a': {'title': 'A', 'description': '第一个数字', 'type': 'integer'}, 'b': {'title': 'B', 'description': '第二个数字', 'type': 'integer'}}

## 处理工具错误
当工具遇到错误并且异常没有被捕获时，代理将停止执行。如果您希望代理继续执行，您可以引发一个 `ToolException` 并相应地设置 `handle_tool_error`。

当抛出 `ToolException` 时，代理不会停止工作，但会根据工具的 `handle_tool_error` 变量处理异常，处理结果将作为观察结果返回给代理，并以红色打印。

您可以将 `handle_tool_error` 设置为 `True`，设置为一个统一的字符串值，或者设置为一个函数。如果它被设置为一个函数，该函数应该以 `ToolException` 作为参数并返回一个 `str` 值。

请注意，仅引发一个 `ToolException` 是不会有效的。您需要首先设置工具的 `handle_tool_error`，因为它的默认值是 `False`。

```python
from langchain_core.tools import ToolException


def search_tool1(s: str):
    raise ToolException("搜索工具1不可用。")
```

首先，让我们看看如果我们不设置 `handle_tool_error` 会发生什么 - 它会出现错误。

```python
search = StructuredTool.from_function(
    func=search_tool1,
    name="Search_tool1",
    description="一个坏工具",
)

search.run("test")
```

    --------------------------------------------------------------------------------
    ToolException                             Traceback (most recent call last)

    Cell In[58], line 7
          1 search = StructuredTool.from_function(
          2     func=search_tool1,
          3     name="Search_tool1",
          4     description=description,
          5 )
    ----> 7 search.run("test")

    File ~/workplace/langchain/libs/core/langchain_core/tools.py:344, in BaseTool.run(self, tool_input, verbose, start_color, color, callbacks, tags, metadata, run_name, **kwargs)
        342 if not self.handle_tool_error:
        343     run_manager.on_tool_error(e)
    --> 344     raise e
        345 elif isinstance(self.handle_tool_error, bool):

    File ~/workplace/langchain/libs/core/langchain_core/tools.py:337, in BaseTool.run(self, tool_input, verbose, start_color, color, callbacks, tags, metadata, run_name, **kwargs)
        334 try:
        335     tool_args, tool_kwargs = self._to_args_and_kwargs(parsed_input)
        336     observation = (
    --> 337         self._run(*tool_args, run_manager=run_manager, **tool_kwargs)
        338         if new_arg_supported
        339         else self._run(*tool_args, **tool_kwargs)
        340     )
        341 except ToolException as e:
        342     if not self.handle_tool_error:

    File ~/workplace/langchain/libs/core/langchain_core/tools.py:631, in StructuredTool._run(self, run_manager, *args, **kwargs)
        622 if self.func:
        623     new_argument_supported = signature(self.func).parameters.get("callbacks")
        624     return (
        625         self.func(
        626             *args,
        627             callbacks=run_manager.get_child() if run_manager else None,
        628             **kwargs,
        629         )
        630         if new_argument_supported
    --> 631         else self.func(*args, **kwargs)
        632     )
        633 raise NotImplementedError("Tool does not support sync")

    Cell In[55], line 5, in search_tool1(s)
          4 def search_tool1(s: str):
    ----> 5     raise ToolException("The search tool1 is not available.")

    ToolException: 搜索工具1不可用。

现在，让我们将 `handle_tool_error` 设置为 True

```python
search = StructuredTool.from_function(
    func=search_tool1,
    name="Search_tool1",
    description="一个坏工具",
    handle_tool_error=True,
)

search.run("test")
```

    '搜索工具1不可用.'

我们还可以使用自定义的方式来处理工具错误

```python
def _handle_error(error: ToolException) -> str:
    return (
        "在工具执行期间发生了以下错误："
        + error.args[0]
        + "请尝试使用另一个工具。"
    )


search = StructuredTool.from_function(
    func=search_tool1,
    name="Search_tool1",
    description="一个坏工具",
    handle_tool_error=_handle_error,
)

search.run("test")
```

    '在工具执行期间发生了以下错误：搜索工具1不可用。请尝试使用另一个工具。'

