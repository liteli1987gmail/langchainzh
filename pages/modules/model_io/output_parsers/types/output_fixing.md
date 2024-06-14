# 输出修复解析器

这个输出解析器包装另一个输出解析器，在第一个失败时调用另一个LLM来修复任何错误。

但我们不仅可以抛出错误。具体来说，我们可以将格式不正确的输出与格式化指令一起传递给模型，并要求它进行修复。

对于这个示例，我们将使用上面的Pydantic输出解析器。如果我们向它传递不符合模式的结果会发生什么:


```python
from typing import List

from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
```


```python
class Actor(BaseModel):
    name: str = Field(description="name of an actor")
    film_names: List[str] = Field(description="list of names of films they starred in")


actor_query = "Generate the filmography for a random actor."

parser = PydanticOutputParser(pydantic_object=Actor)
```


```python
misformatted = "{'name': 'Tom Hanks', 'film_names': ['Forrest Gump']}"
```


```python
parser.parse(misformatted)
```


    ---------------------------------------------------------------------------

    JSONDecodeError                           Traceback (most recent call last)

    File ~/workplace/langchain/libs/langchain/langchain/output_parsers/pydantic.py:29, in PydanticOutputParser.parse(self, text)
         28     json_str = match.group()
    ---> 29 json_object = json.loads(json_str, strict=False)
         30 return self.pydantic_object.parse_obj(json_object)
    

    File ~/.pyenv/versions/3.10.1/lib/python3.10/json/__init__.py:359, in loads(s, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)
        358     kw['parse_constant'] = parse_constant
    --> 359 return cls(**kw).decode(s)
    

    File ~/.pyenv/versions/3.10.1/lib/python3.10/json/decoder.py:337, in JSONDecoder.decode(self, s, _w)
        333 """Return the Python representation of ``s`` (a ``str`` instance
        334 containing a JSON document).
        335 
        336 """
    --> 337 obj, end = self.raw_decode(s, idx=_w(s, 0).end())
        338 end = _w(s, end).end()
    

    File ~/.pyenv/versions/3.10.1/lib/python3.10/json/decoder.py:353, in JSONDecoder.raw_decode(self, s, idx)
        352 try:
    --> 353     obj, end = self.scan_once(s, idx)
        354 except StopIteration as err:
    

    JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

    
    During handling of the above exception, another exception occurred:
    

    OutputParserException                     Traceback (most recent call last)

    Cell In[4], line 1
    ----> 1 parser.parse(misformatted)
    

    File ~/workplace/langchain/libs/langchain/langchain/output_parsers/pydantic.py:35, in PydanticOutputParser.parse(self, text)
         33 name = self.pydantic_object.__name__
         34 msg = f"Failed to parse {name} from completion {text}. Got: {e}"
    ---> 35 raise OutputParserException(msg, llm_output=text)
    

    OutputParserException: Failed to parse Actor from completion {'name': 'Tom Hanks', 'film_names': ['Forrest Gump']}. Got: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)


现在我们可以构建和使用 `OutputFixingParser`。这个输出解析器接受另一个输出解析器作为参数，同时也接受一个LLM，用来尝试纠正任何格式错误。


```python
from langchain.output_parsers import OutputFixingParser

new_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())
```


```python
new_parser.parse(misformatted)
```




    Actor(name='Tom Hanks', film_names=['Forrest Gump'])




```python

```