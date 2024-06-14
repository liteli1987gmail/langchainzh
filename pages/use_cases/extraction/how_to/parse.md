# 解析

能够很好地遵循提示指令的大型语言模型（LLMs）可以被指派以给定的格式输出信息。

这种方法依赖于设计好的提示，然后解析LLMs的输出，使它们能够很好地提取信息。

在这里，我们将使用Claude，它非常擅长遵循指令！请参阅[Anthropic模型](https://www.anthropic.com/api)。

```python
from langchain_anthropic.chat_models import ChatAnthropic

model = ChatAnthropic(model_name="claude-3-sonnet-20240229", temperature=0)
```

:::⚠⚠⚠

所有相同的提取质量考虑因素也适用于解析方法。请查阅[提取质量指南](/use_cases/extraction/guidelines)。

本教程旨在保持简单，但通常确实应该包括参考示例以提高性能！

:::

## 使用 PydanticOutputParser
以下示例使用内置的`PydanticOutputParser`来解析聊天模型的输出。

```python
from typing import List, Optional

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator

class Person(BaseModel):
    """Information about a person."""

    name: str = Field(..., description="The name of the person")
    height_in_meters: float = Field(
        ..., description="The height of the person expressed in meters."
    )

class People(BaseModel):
    """Identifying information about all people in a text."""

    people: List[Person]

# Set up a parser
parser = PydanticOutputParser(pydantic_object=People)

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the user query. Wrap the output in `json` tags\n{format_instructions}",
        ),
        ("human", "{query}"),
    ]
).partial(format_instructions=parser.get_format_instructions())
```

Let's take a look at what information is sent to the model

```python
query = "Anna is 23 years old and she is 6 feet tall"
```

```python
print(prompt.format_prompt(query=query).to_string())
```

    System: Answer the user query. Wrap the output in `json` tags
    The output should be formatted as a JSON instance that conforms to the JSON schema below.
    
    As an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}
    the object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.
    
    Here is the output schema:
    ```
    {"description": "Identifying information about all people in a text.", "properties": {"people": {"title": "People", "type": "array", "items": {"$ref": "#/definitions/Person"}}}, "required": ["people"], "definitions": {"Person": {"title": "Person", "description": "Information about a person.", "type": "object", "properties": {"name": {"title": "Name", "description": "The name of the person", "type": "string"}, "height_in_meters": {"title": "Height In Meters", "description": "The height of the person expressed in meters.", "type": "number"}}, "required": ["name", "height_in_meters"]}}}
    ```
    Human: Anna is 23 years old and she is 6 feet tall
    
```python
chain = prompt | model | parser
chain.invoke({"query": query})
```

    People(people=[Person(name='Anna', height_in_meters=1.83)])

## 自定义解析

使用 `LangChain` 和 `LCEL`，可以轻松创建自定义提示和解析器。

您可以使用一个简单的函数来解析模型的输出！

```python
import json
import re
from typing import List, Optional

from langchain_anthropic.chat_models import ChatAnthropic
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator

class Person(BaseModel):
    """Information about a person."""

    name: str = Field(..., description="The name of the person")
    height_in_meters: float = Field(
        ..., description="The height of the person expressed in meters."
    )

class People(BaseModel):
    """Identifying information about all people in a text."""

    people: List[Person]

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the user query. Output your answer as JSON that  "
            "matches the given schema: ```json\n{schema}\n```. "
            "Make sure to wrap the answer in ```json and ``` tags",
        ),
        ("human", "{query}"),
    ]
).partial(schema=People.schema())

# Custom parser
def extract_json(message: AIMessage) -> List[dict]:
    """Extracts JSON content from a string where JSON is embedded between ```json and ``` tags.

    Parameters:
        text (str): The text containing the JSON content.

    Returns:
        list: A list of extracted JSON strings.
    """
    text = message.content
    # Define the regular expression pattern to match JSON blocks
    pattern = r"```json(.*?)```"

    # Find all non-overlapping matches of the pattern in the string
    matches = re.findall(pattern, text, re.DOTALL)

    # Return the list of matched JSON strings, stripping any leading or trailing whitespace
    try:
        return [json.loads(match.strip()) for match in matches]
    except Exception:
        raise ValueError(f"Failed to parse: {message}")
```

```python
query = "Anna is 23 years old and she is 6 feet tall"
print(prompt.format_prompt(query=query).to_string())
```

    System: Answer the user query. Output your answer as JSON that  matches the given schema: ```json
    {'title': 'People', 'description': 'Identifying information about all people in a text.', 'type': 'object', 'properties': {'people': {'title': 'People', 'type': 'array', 'items': {'$ref': '#/definitions/Person'}}}, 'required': ['people'], 'definitions': {'Person': {'title': 'Person', 'description': 'Information about a person.', 'type': 'object', 'properties': {'name': {'title': 'Name', 'description': 'The name of the person', 'type': 'string'}, 'height_in_meters': {'title': 'Height In Meters', 'description': 'The height of the person expressed in meters.', 'type': 'number'}}, 'required': ['name', 'height_in_meters']}}}
    ```. Make sure to wrap the answer in ```json and ``` tags
    Human: Anna is 23 years old and she is 6 feet tall
    
```python
chain = prompt | model | extract_json
chain.invoke({"query": query})
```

    [{'people': [{'name': 'Anna', 'height_in_meters': 1.83}]}]## 其他库

如果你希望使用解析方法进行提取，请查看 [Kor](https://eyurtsev.github.io/kor/) 库。它由 `LangChain` 的维护人员之一编写，可以帮助设计一个考虑到示例的提示，并且可以控制格式（如JSON或CSV），并在TypeScript中表达模式。它似乎工作得非常好！