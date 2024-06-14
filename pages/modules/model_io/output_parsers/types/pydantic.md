# Pydantic解析器
该解析器允许用户指定任意Pydantic模型，并查询与该模型匹配的输出。

请记住，大型语言模型是有泄漏的抽象！您必须使用容量足够的语言模型来生成格式良好的JSON。在OpenAI系列中，DaVinci可以可靠地实现这一点，但[Curie](https://wiprotechblogs.medium.com/davinci-vs-curie-a-comparison-between-gpt-3-engines-for-extractive-summarization-b568d4633b3b)的能力已经显著下降。

使用Pydantic声明数据模型。Pydantic的BaseModel类似于Python中的dataclass，但具有实际的类型检查和强制转换。

```python
from typing import List

from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain_openai import ChatOpenAI
```

```python
model = ChatOpenAI(temperature=0)
```

```python
# 定义您所需的数据结构。
class Joke(BaseModel):
    setup: str = Field(description="用以引出笑话的问题")
    punchline: str = Field(description="解答笑话的答案")

    # 您可以使用Pydantic轻松添加自定义验证逻辑。
    @validator("setup")
    def question_ends_with_question_mark(cls, field):
        if field[-1] != "?":
            raise ValueError("问题形式不正确！")
        return field


# 还有一个查询意图，用于提示语言模型填充数据结构。
joke_query = "告诉我一个笑话。"

# 设置解析器并将指令注入到提示模板中。
parser = PydanticOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

chain.invoke({"query": joke_query})
```

```python
# 这里是另一个示例，但使用复合类型的字段。
class Actor(BaseModel):
    name: str = Field(description="演员姓名")
    film_names: List[str] = Field(description="他们主演的电影名称列表")


actor_query = "生成随机演员的电影作品列表。"

parser = PydanticOutputParser(pydantic_object=Actor)

prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

chain.invoke({"query": actor_query})
```







