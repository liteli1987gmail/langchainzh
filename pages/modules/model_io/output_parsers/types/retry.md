# 重试解析器

在某些情况下，只通过查看输出可以修复任何解析错误，但在其他情况下则不行。一个例子是当输出不仅格式错误，而且部分不完整时。考虑下面的例子。

```python
from langchain.output_parsers import (
    OutputFixingParser,
    PydanticOutputParser,
)
from langchain.prompts import (
    PromptTemplate,
)
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI, OpenAI
```

```python
template = """基于用户提问，为应该采取的步骤提供一个动作和动作输入。
{format_instructions}
问题: {query}
回答:"""

class Action(BaseModel):
    action: str = Field(description="要采取的动作")
    action_input: str = Field(description="动作的输入")

parser = PydanticOutputParser(pydantic_object=Action)
```

```python
prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
```

```python
prompt_value = prompt.format_prompt(query="谁是李奥纳多的女友?")
```
```python
bad_response = '{"action": "搜索"}'
```

如果我们试图直接解析这个响应，会出现错误：

```python
    parser.parse(bad_response)
```

    ---------------------------------------------------------------------------

    ValidationError                           Traceback (most recent call last)

    File ~/workplace/langchain/libs/langchain/langchain/output_parsers/pydantic.py:30, in PydanticOutputParser.parse(self, text)
         29     json_object = json.loads(json_str, strict=False)
    ---> 30     return self.pydantic_object.parse_obj(json_object)
         32 except (json.JSONDecodeError, ValidationError) as e:

    File ~/.pyenv/versions/3.10.1/envs/langchain/lib/python3.10/site-packages/pydantic/main.py:526, in pydantic.main.BaseModel.parse_obj()

    File ~/.pyenv/versions/3.10.1/envs/langchain/lib/python3.10/site-packages/pydantic/main.py:341, in pydantic.main.BaseModel.__init__()

    ValidationError: 1 validation error for Action
    action_input
      field required (type=value_error.missing)

    During handling of the above exception, another exception occurred:

    OutputParserException                     Traceback (most recent call last)

    Cell In[6], line 1
    ----> 1 parser.parse(bad_response)

    File ~/workplace/langchain/libs/langchain/langchain/output_parsers/pydantic.py:35, in PydanticOutputParser.parse(self, text)
         33 name = self.pydantic_object.__name__
         34 msg = f"Failed to parse {name} from completion {text}. Got: {e}"
    ---> 35 raise OutputParserException(msg, llm_output=text)

    OutputParserException: Failed to parse Action from completion {"action": "搜索"}. Got: 1 validation error for Action
    action_input
      field required (type=value_error.missing)

如果我们尝试使用`OutputFixingParser`来修复此错误，它会变得困惑-也就是说，它不知道实际上应该为动作输入放入什么内容。

```python
fix_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())
```

```python
fix_parser.parse(bad_response)
```

    Action(action='搜索', action_input='输入')

相反，我们可以使用RetryOutputParser，在第二次尝试时将提示（以及原始输出）传递给它，以获得更好的响应。

```python
from langchain.output_parsers import RetryOutputParser
```

```python
retry_parser = RetryOutputParser.from_llm(parser=parser, llm=OpenAI(temperature=0))
```

```python
retry_parser.parse_with_prompt(bad_response, prompt_value)
```

    Action(action='搜索', action_input='李奥纳多的女友')

我们还可以很容易地将RetryOutputParser与自定义链结合，将原始的LLM/ChatModel输出转换为更可操作的格式。

```python
from langchain_core.runnables import RunnableLambda, RunnableParallel

completion_chain = prompt | OpenAI(temperature=0)

main_chain = RunnableParallel(
    completion=completion_chain, prompt_value=prompt
) | RunnableLambda(lambda x: retry_parser.parse_with_prompt(**x))

main_chain.invoke({"query": "谁是李奥纳多的女友?"})
```

    Action(action='搜索', action_input='李奥纳多的女友')

