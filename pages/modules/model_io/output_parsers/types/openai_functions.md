# OpenAI功能

这些输出解析器使用OpenAI函数调用来结构化其输出。这意味着它们只能用于支持函数调用的模型。有几种不同的变体:

- [JsonOutputFunctionsParser](https://api.python.langchain.com/en/latest/output_parsers/langchain_core.output_parsers.openai_functions.JsonOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.JsonOutputFunctionsParser)：将函数调用的参数作为JSON返回
- [PydanticOutputFunctionsParser](https://api.python.langchain.com/en/latest/output_parsers/langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticOutputFunctionsParser)：将函数调用的参数作为Pydantic模型返回
- [JsonKeyOutputFunctionsParser](https://api.python.langchain.com/en/latest/output_parsers/langchain_core.output_parsers.openai_functions.JsonKeyOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.JsonKeyOutputFunctionsParser)：将函数调用中特定键的值作为JSON返回
- [PydanticAttrOutputFunctionsParser](https://api.python.langchain.com/en/latest/output_parsers/langchain_core.output_parsers.openai_functions.PydanticAttrOutputFunctionsParser.html#langchain_core.output_parsers.openai_functions.PydanticAttrOutputFunctionsParser)：将函数调用中特定键的值作为Pydantic模型返回



```python
from langchain_community.utils.openai_functions import (
    convert_pydantic_to_openai_function,
)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain_openai import ChatOpenAI
```


```python
class Joke(BaseModel):
    """要告诉用户的笑话。"""

    setup: str = Field(description="用于设定笑话的问题")
    punchline: str = Field(description="解决笑话的答案")


openai_functions = [convert_pydantic_to_openai_function(Joke)]
```


```python
model = ChatOpenAI(temperature=0)
```


```python
prompt = ChatPromptTemplate.from_messages(
    [("system", "您是一个乐于助人的助手"), ("user", "{input}")]
)
```

## JsonOutputFunctionsParser


```python
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
```


```python
parser = JsonOutputFunctionsParser()
```


```python
chain = prompt | model.bind(functions=openai_functions) | parser
```


```python
chain.invoke({"input": "给我讲个笑话"})
```




    {'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}




```python
for s in chain.stream({"input": "给我讲个笑话"}):
    print(s)
```

    {}
    {'setup': ''}
    {'setup': '为什么'}
    {'setup': '为什么科'}
    {'setup': '为什么科学'}
    {'setup': '为什么科学家'}
    {'setup': '为什么科学家不'}
    {'setup': '为什么科学家不相'}
    {'setup': '为什么科学家不相信'}
    {'setup': '为什么科学家不相信原子'}
    {'setup': '为什么科学家不相信原子？', 'punchline': ''}
    {'setup': '为什么科学家不相信原子？', 'punchline': '因为'}
    {'setup': '为什么科学家不相信原子？', 'punchline': '因为它们'}
    {'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构'}
    {'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成'}
    {'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了'}
    {'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切'}
    {'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}
    

## JsonKeyOutputFunctionsParser

这只是从返回的响应中提取一个键。当您想返回一系列事物时，这将非常有用。


```python
from typing import List

from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser
```


```python
class Jokes(BaseModel):
    """要告诉用户的笑话。"""

    joke: List[Joke]
    funniness_level: int
```


```python
parser = JsonKeyOutputFunctionsParser(key_name="joke")
```


```python
openai_functions = [convert_pydantic_to_openai_function(Jokes)]
chain = prompt | model.bind(functions=openai_functions) | parser
```


```python
chain.invoke({"input": "给我讲两个笑话"})
```




    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什么拯救地球？', 'punchline': '扶贫帮困！'}]




```python
for s in chain.stream({"input": "给我讲两个笑话"}):
    print(s)
```

    []
    [{}]
    [{'setup': ''}]
    [{'setup': '为什么'}]
    [{'setup': '为什么科'}]
    [{'setup': '为什么科学'}]
    [{'setup': '为什么科学家'}]
    [{'setup': '为什么科学家不'}]
    [{'setup': '为什么科学家不相'}]
    [{'setup': '为什么科学家不相信'}]
    [{'setup': '为什么科学家不相信原'}]
    [{'setup': '为什么科学家不相信原子'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': ''}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': ''}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什么'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什么拯'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什么拯救'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什么拯救地'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什么拯救地球'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什么拯救地球？', 'punchline': ''}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什么拯救地球？', 'punchline': '扶'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什么拯救地球？', 'punchline': '扶贫'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什么拯救地球？', 'punchline': '扶贫帮'}]
    [{'setup': '为什么科学家不相信原子？', 'punchline': '因为它们构成了一切！'}, {'setup': '拿什么拯救地球？', 'punchline': '扶贫帮困'}]
    

## PydanticOutputFunctionsParser

这在`JsonOutputFunctionsParser`的基础上构建，但将结果传递给了Pydantic模型。这允许进一步的验证，如果您选择的话。


```python
from langchain.output_parsers.openai_functions import PydanticOutputFunctionsParser
```


```python
class Joke(BaseModel):
    """要告诉用户的笑话。"""

    setup: str = Field(description="用于设定笑话的问题")
    punchline: str = Field(description="解决笑话的答案")


# 你可以使用Pydantic轻松添加自定义验证逻辑。

@validator("setup")
def question_ends_with_question_mark(cls, field):
    if field[-1] != "?":
        raise ValueError("问题形式错误！")
    return field


parser = PydanticOutputFunctionsParser(pydantic_schema=Joke)
```


```python
openai_functions = [convert_pydantic_to_openai_function(Joke)]
chain = prompt | model.bind(functions=openai_functions) | parser
```


```python
chain.invoke({"input": "告诉我一个笑话"})
```




    Joke(setup="为什么科学家不相信原子？", punchline='因为它们组成了一切！')






