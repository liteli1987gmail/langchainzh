# YAML解析器

该输出解析器允许用户指定任意模式并查询LLMs，以符合该模式的输出，使用YAML格式化其响应。

请记住，大型语言模型是有缺陷的抽象！您必须使用具有足够容量的LLM来生成格式良好的YAML。在OpenAI系列中，DaVinci可以可靠地执行，但Curie的能力已经急剧下降。

您可以选择使用Pydantic声明数据模型。

```python
from typing import List

from langchain.output_parsers import YamlOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
```

```python
model = ChatOpenAI(temperature=0)
```

# 定义您期望的数据结构。

```python
class Joke(BaseModel):
    setup: str = Field(description="提出一个笑话的问题")
    punchline: str = Field(description="解决笑话的答案")
```

# 以及一个旨在提示语言模型填充数据结构的查询。

```python
joke_query = "告诉我一个笑话。"

# 设置解析器+将指令注入到提示模板中。

parser = YamlOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="回答用户提问。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

chain.invoke({"query": joke_query})


```

