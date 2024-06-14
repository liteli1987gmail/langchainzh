# 将值映射到数据库

在本指南中，我们将介绍通过将用户输入的值从映射到数据库来改善图数据库查询生成的策略。
使用内置的图链时，LLM了解图模式，但不知道数据库中属性值的信息。
因此，我们可以在图数据库QA系统中引入一个新的步骤，准确地映射值。

## 设置

首先，获取所需的软件包并设置环境变量：


```python
%pip install --upgrade --quiet  langchain langchain-community langchain-openai neo4j
```

注意：您可能需要重新启动内核以使用更新的软件包。


在本指南中，默认使用OpenAI模型，但您可以将其替换为您选择的模型提供程序。


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 如果需要，请取消下面的注释以使用LangSmith。
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

接下来，我们需要定义Neo4j凭据。
按照[这些安装步骤](https://neo4j.com/docs/operations-manual/current/installation/)设置Neo4j数据库。


```python
os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "password"
```

下面的示例将创建与Neo4j数据库的连接，并将其填充有关电影及其演员的示例数据。


```python
from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph()

# 导入电影信息

movies_query = """
LOAD CSV WITH HEADERS FROM 
'https://raw.githubusercontent.com/tomasonjo/blog-datasets/main/movies/movies_small.csv'
AS row
MERGE (m:Movie {id:row.movieId})
SET m.released = date(row.released),
    m.title = row.title,
    m.imdbRating = toFloat(row.imdbRating)
FOREACH (director in split(row.director, '|') | 
    MERGE (p:Person {name:trim(director)})
    MERGE (p)-[:DIRECTED]->(m))
FOREACH (actor in split(row.actors, '|') | 
    MERGE (p:Person {name:trim(actor)})
    MERGE (p)-[:ACTED_IN]->(m))
FOREACH (genre in split(row.genres, '|') | 
    MERGE (g:Genre {name:trim(genre)})
    MERGE (m)-[:IN_GENRE]->(g))
"""

graph.query(movies_query)
```




    []



## 检测用户输入中的实体
我们必须从文本中提取要映射到图数据库的实体/值的类型。在此示例中，我们处理的是电影图，因此可以将电影和人员映射到数据库。


```python
from typing import List, Optional

from langchain.chains.openai_functions import create_structured_output_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


class Entities(BaseModel):
    """有关实体的识别信息。"""

    names: List[str] = Field(
        ...,
        description="出现在文本中的所有人物或电影",
    )


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "您要从文本中提取人员和电影。",
        ),
        (
            "human",
            "使用给定的格式从以下输入中提取信息: {question}",
        ),
    ]
)


entity_chain = create_structured_output_chain(Entities, llm, prompt)
```

    /Users/tomazbratanic/anaconda3/lib/python3.11/site-packages/langchain_core/_api/deprecation.py:117: LangChainDeprecationWarning: The function `create_structured_output_chain` was deprecated in LangChain 0.1.1 and will be removed in 0.2.0. Use create_structured_output_runnable instead.
      warn_deprecated(
    

我们可以测试实体提取链。


```python
entities = entity_chain.invoke({"question": "谁在《赌城风云》电影中演过?"})
entities
```




    {'question': '谁在《赌城风云》电影中演过?',
     'function': Entities(names=['赌城风云'])}



我们将利用一个简单的`CONTAINS`子句将实体与数据库匹配。在实际应用中，您可能希望使用模糊搜索或全文索引来允许轻微的拼写错误。


```python
match_query = """MATCH (p:Person|Movie)
WHERE p.name CONTAINS $value OR p.title CONTAINS $value
RETURN coalesce(p.name, p.title) AS result, labels(p)[0] AS type
LIMIT 1
"""


def map_to_database(values):
    result = ""
    for entity in values.names:
        response = graph.query(match_query, {"value": entity})
        try:
            result += f"{entity}在数据库中对应 {response[0]['type']}：{response[0]['result']}\n"
        except IndexError:
            pass
    return result


map_to_database(entities["function"])
```




    '赌城风云在数据库中对应 电影：赌城风云\n'



## 自定义Cypher生成链

我们需要定义一个自定义的Cypher提示，该提示将实体映射信息与架构和用户问题一起使用，构造Cypher语句。
我们将使用LangChain表达式语言来实现。


```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 根据自然语言输入生成Cypher语句
cypher_template = """根据下面的Neo4j图模式，编写一个Cypher查询来回答用户的问题：
{schema}
问题中的实体映射到以下数据库值：
{entities_list}
问题：{question}
Cypher查询："""  # noqa: E501

cypher_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "给定一个输入问题，将其转换为Cypher查询。不包含任何前言。",
        ),
        ("human", cypher_template),
    ]
)

cypher_response = (
    RunnablePassthrough.assign(names=entity_chain)
    | RunnablePassthrough.assign(
        entities_list=lambda x: map_to_database(x["names"]["function"]),
        schema=lambda _: graph.get_schema,
    )
    | cypher_prompt
    | llm.bind(stop=["\nCypherResult:"])
    | StrOutputParser()
)
```


```python
cypher = cypher_response.invoke({"question": "谁在《赌城风云》电影中演过?"})
cypher
```




    'MATCH (:Movie {title: "赌城风云"})<-[:ACTED_IN]-(actor)\nRETURN actor.name'


------
======
## 根据数据库结果生成答案

现在我们有一个生成Cypher语句的链，我们需要执行该Cypher语句并将数据库结果发送回LLM以生成最终答案。
我们将再次使用LCEL。

```python
from langchain.chains.graph_qa.cypher_utils import CypherQueryCorrector, Schema

# 用于关系方向的Cypher验证工具
corrector_schema = [
    Schema(el["start"], el["type"], el["end"])
    for el in graph.structured_schema.get("relationships")
]
cypher_validation = CypherQueryCorrector(corrector_schema)

# 基于数据库结果生成自然语言响应
response_template = """根据问题、Cypher查询和Cypher响应，编写自然语言响应：
问题：{question}
Cypher查询：{query}
Cypher响应：{response}"""  # noqa: E501

response_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "根据输入的问题和Cypher响应，将其转换为自然语言答案。不加前言。",
        ),
        ("human", response_template),
    ]
)

chain = (
    RunnablePassthrough.assign(query=cypher_response)
    | RunnablePassthrough.assign(
        response=lambda x: graph.query(cypher_validation(x["query"])),
    )
    | response_prompt
    | llm
    | StrOutputParser()
)
```

```python
chain.invoke({"question": "《赌城风云》电影中有谁出演?"})
```

'《赌城风云》电影中有Joe Pesci、Robert De Niro、Sharon Stone和James Woods出演。'

