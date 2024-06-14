# 代码编写

使用LCEL编写Python代码的示例。

```python
%pip install --upgrade --quiet langchain-core langchain-experimental langchain-openai
```


```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
)
from langchain_experimental.utilities import PythonREPL
from langchain_openai import ChatOpenAI
```


```python
template = """编写一些用于解决用户问题的Python代码。 

只返回Markdown格式的Python代码，例如：

```python
....
```"""
prompt = ChatPromptTemplate.from_messages([("system", template), ("human", "{input}")])

model = ChatOpenAI()
```


```python
def _sanitize_output(text: str):
    _, after = text.split("```python")
    return after.split("```")[0]
```


```python
chain = prompt | model | StrOutputParser() | _sanitize_output | PythonREPL().run
```


```python
chain.invoke({"input": "2加2等于多少"})
```

    Python REPL可以执行任意代码。请谨慎使用。
    




    '4\n'