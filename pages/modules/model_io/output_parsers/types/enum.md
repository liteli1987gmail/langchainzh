# 枚举解析器

这个笔记本展示了如何使用枚举输出解析器。

```python
from langchain.output_parsers.enum import EnumOutputParser
```

```python
from enum import Enum

class Colors(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
```

```python
parser = EnumOutputParser(enum=Colors)
```

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

prompt = PromptTemplate.from_template(
    """这个人有什么颜色的眼睛？

> 人物: {person}

说明: {instructions}"""
).partial(instructions=parser.get_format_instructions())
chain = prompt | ChatOpenAI() | parser
```

```python
chain.invoke({"person": "弗兰克·辛纳屈"})
```


```
<Colors.BLUE: 'blue'>
```