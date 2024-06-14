# 部分提示模板

与其他方法一样，"部分化"提示模板是有意义的 - 例如，传递所需值的子集，以创建一个新的提示模板，该模板仅期望其余子集的值。

LangChain以两种方式支持此功能：
1. 使用字符串值进行部分格式化。
2. 使用返回字符串值的函数进行部分格式化。

这两种不同的方式支持不同的用例。在下面的示例中，我们将讨论两种用例的动机以及如何在LangChain中实现。

## 使用字符串进行部分化

希望部分化提示模板的一个常见用例是，如果您先获取一些变量，然后再获取其他变量。例如，假设您有一个需要两个变量`foo`和`baz`的提示模板。如果您在链的早期获取了`foo`值，但稍后才获取`baz`值，那么等到两个变量在同一个地方时再传递它们给提示模板可能很麻烦。相反，您可以使用`foo`值部分化提示模板，然后传递部分化的提示模板，并只使用那个。以下是一个示例：



```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("{foo}{bar}")
partial_prompt = prompt.partial(foo="foo")
print(partial_prompt.format(bar="baz"))
```

    foobaz
    

您还可以使用部分化的变量初始化提示。



```python
prompt = PromptTemplate(
    template="{foo}{bar}", input_variables=["bar"], partial_variables={"foo": "foo"}
)
print(prompt.format(bar="baz"))
```

    foobaz
    

## 使用函数进行部分化

另一个常见用例是使用函数进行部分化。这种情况下的用例是，当您知道您希望以常见方式获取变量时。这种情况的一个典型示例是日期或时间。想象一下，您有一个提示，您始终希望包含当前日期。您不能在提示中硬编码它，并将其与其他输入变量一起传递有点麻烦。在这种情况下，能够使用始终返回当前日期的函数部分化提示非常方便。



```python
from datetime import datetime


def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")
```


```python
prompt = PromptTemplate(
    template="Tell me a {adjective} joke about the day {date}",
    input_variables=["adjective", "date"],
)
partial_prompt = prompt.partial(date=_get_datetime)
print(partial_prompt.format(adjective="funny"))
```

    Tell me a funny joke about the day 12/27/2023, 10:45:22
    

您还可以使用部分化的变量初始化提示，这在这种工作流程中通常更有意义。



```python
prompt = PromptTemplate(
    template="Tell me a {adjective} joke about the day {date}",
    input_variables=["adjective"],
    partial_variables={"date": _get_datetime},
)
print(prompt.format(adjective="funny"))
```

    Tell me a funny joke about the day 12/27/2023, 10:45:36
    


```python

```