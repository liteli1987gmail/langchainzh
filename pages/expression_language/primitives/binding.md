# Binding: 附加运行时参数

有时候我们希望在一个Runnable序列中调用一个Runnable，并传递一些常量参数，这些参数不是前一个Runnable的输出的一部分，也不是用户输入的一部分。我们可以使用`Runnable.bind()`来传递这些参数。

假设我们有一个简单的提示+模型序列:

```python
%pip install --upgrade --quiet  langchain langchain-openai
```

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
```

```python
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "用代数符号写出下列方程并求解。使用以下格式\n\nEQUATION:...\nSOLUTION:...\n\n",
        ),
        ("human", "{equation_statement}"),
    ]
)
model = ChatOpenAI(temperature=0)
runnable = (
    {"equation_statement": RunnablePassthrough()} | prompt | model | StrOutputParser()
)

print(runnable.invoke("x的三次方加上七等于12"))
```

    EQUATION: x^3 + 7 = 12
    
    SOLUTION:
    将方程两边都减去7，我们得到：
    x^3 = 12 - 7
    x^3 = 5
    
    将方程两边都开三次方，我们得到：
    x = ∛5
    
    因此，方程x^3 + 7 = 12的解为x = ∛5.


现在我们想要使用特定的`stop`词调用模型:


```python
runnable = (
    {"equation_statement": RunnablePassthrough()}
    | prompt
    | model.bind(stop="SOLUTION")
    | StrOutputParser()
)
print(runnable.invoke("x的三次方加上七等于12"))
```

    EQUATION: x^3 + 7 = 12
    
    
    

## 附加OpenAI函数

绑定的一个特别有用的应用是将OpenAI函数附加到兼容的OpenAI模型上:

```python
function = {
    "name": "solver",
    "description": "Formulates and solves an equation",
    "parameters": {
        "type": "object",
        "properties": {
            "equation": {
                "type": "string",
                "description": "The algebraic expression of the equation",
            },
            "solution": {
                "type": "string",
                "description": "The solution to the equation",
            },
        },
        "required": ["equation", "solution"],
    },
}
```

```python
# 需要gpt-4才能正确解决这个问题
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "用代数符号写出下列方程并求解。",
        ),
        ("human", "{equation_statement}"),
    ]
)
model = ChatOpenAI(model="gpt-4", temperature=0).bind(
    function_call={"name": "solver"}, functions=[function]
)
runnable = {"equation_statement": RunnablePassthrough()} | prompt | model
runnable.invoke("x的三次方加上七等于12")
```

    AIMessage(content='', additional_kwargs={'function_call': {'name': 'solver', 'arguments': '{\n"equation": "x^3 + 7 = 12",\n"solution": "x = ∛5"\n}'}}, example=False)


## 附加OpenAI工具

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "获取给定位置的当前天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市和州，例如：旧金山，加利福尼亚",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    }
]
```

```python
model = ChatOpenAI(model="gpt-3.5-turbo-1106").bind(tools=tools)
model.invoke("旧金山、纽约市和洛杉矶的天气如何？")
```

    AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_zHN0ZHwrxM7nZDdqTp6dkPko', 'function': {'arguments': '{"location": "旧金山，加利福尼亚", "unit": "celsius"}', 'name': 'get_current_weather'}, 'type': 'function'}, {'id': 'call_aqdMm9HBSlFW9c9rqxTa7eQv', 'function': {'arguments': '{"location": "纽约市，纽约", "unit": "celsius"}', 'name': 'get_current_weather'}, 'type': 'function'}, {'id': 'call_cx8E567zcLzYV2WSWVgO63f1', 'function': {'arguments': '{"location": "洛杉矶，加利福尼亚", "unit": "celsius"}', 'name': 'get_current_weather'}, 'type': 'function'}]})

------
