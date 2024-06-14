# 语义层中实现Cypher模板

你可以使用数据库查询从图数据库（如Neo4j）中检索信息。
一种选择是使用LLMs来生成Cypher语句。
虽然这种选项提供了出色的灵活性，但解决方案可能脆弱，并且无法始终生成精确的Cypher语句。
我们可以在语义层中实现Cypher模板作为LLM代理可以与之交互的工具。

![graph_semantic.png](/img/graph_semantic.png)

## 配置

首先，获取所需的软件包并设置环境变量：

```python
%pip install --upgrade --quiet  langchain langchain-community langchain-openai neo4j
```

    注意：您可能需要重新启动内核以使用更新的软件包。
    
在本指南中，我们默认使用OpenAI模型，但您可以将其替换为您选择的模型提供程序。

```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 取消下面的注释以使用LangSmith。非必需。
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

接下来，我们需要定义Neo4j凭据。
按照[这些安装步骤](https://neo4j.com/docs/operations-manual/current/installation/)来设置Neo4j数据库。

```python
os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "password"
```

下面的示例将创建与Neo4j数据库的连接，并将其填充示例数据，其中包含有关电影及其演员的信息。

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
FOREACH (director IN split(row.director, '|') | 
    MERGE (p:Person {name:trim(director)})
    MERGE (p)-[:DIRECTED]->(m))
FOREACH (actor IN split(row.actors, '|') | 
    MERGE (p:Person {name:trim(actor)})
    MERGE (p)-[:ACTED_IN]->(m))
FOREACH (genre IN split(row.genres, '|') | 
    MERGE (g:Genre {name:trim(genre)})
    MERGE (m)-[:IN_GENRE]->(g))
"""

graph.query(movies_query)
```

## 使用Cypher模板创建自定义工具

语义层由各种工具组成，LLM可以使用这些工具与知识图形进行交互。
它们可以具有各种复杂性。您可以将语义层中的每个工具视为一个函数。

我们要实现的函数是用于检索有关电影或演员的信息。

```python
from typing import Optional, Type

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

# 导入通用所需的内容
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool

description_query = """
MATCH (m:Movie|Person)
WHERE m.title CONTAINS $candidate OR m.name CONTAINS $candidate
MATCH (m)-[r:ACTED_IN|HAS_GENRE]-(t)
WITH m, type(r) AS type, collect(COALESCE(t.name, t.title)) AS names
WITH m, type + ": " + REDUCE(s = "", n IN names | s + n + ", ") AS types
WITH m, COLLECT(types) AS contexts
WITH m, "type:" + LABELS(m)[0] + "\ntitle: " + COALESCE(m.title, m.name) 
       + "\nyear: " + COALESCE(m.released, "") + "\n" +
       REDUCE(s = "", c IN contexts | s + SUBSTRING(c, 0, SIZE(c) - 2) + "\n") AS context
RETURN context LIMIT 1
"""

def get_information(entity: str) -> str:
    try:
        data = graph.query(description_query, params={"candidate": entity})
        return data[0]["context"]
    except IndexError:
        return "未找到相关信息"
```

您可以观察到我们已经定义了用于检索信息的Cypher语句。
因此，我们可以避免生成Cypher语句，并使用LLM代理仅填充输入参数来使用工具。
为了向LLM代理提供有关何时使用工具及其输入参数的附加信息，我们将该函数包装为一个工具。

```python
from typing import Optional, Type

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool


class InformationInput(BaseModel):
    entity: str = Field(description="在问题中提到的电影或人物")


class InformationTool(BaseTool):
    name = "Information"
    description = (
        "当您需要回答有关各种演员或电影的问题时很有用"
    )
    args_schema: Type[BaseModel] = InformationInput

    def _run(
        self,
        entity: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """使用该工具。"""
        return get_information(entity)

    async def _arun(
        self,
        entity: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """异步使用该工具。"""
        return get_information(entity)
```

## OpenAI Agent

LangChain表达语言非常方便地定义与语义层上的图数据库进行交互的代理。

```python
from typing import List, Tuple

from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = [InformationTool()]

llm_with_tools = llm.bind(functions=[convert_to_openai_function(t) for t in tools])

prompt = ChatPromptTemplate.from_messages(
```=======

我提供的mdx文档的内容需要翻译，只要翻译md语法中的标题、段落和列表的内容，驼峰和下划线单词不必翻译，请保留md语法标点符号，你翻译完后对原内容进行替换，将结果返回给我。mdx文档是:=======

\[
\begin{align*}
\text{(标题)}&: \text{我提供的mdx文档的内容需要翻译，只要翻译md语法中的标题、段落和列表的内容，驼峰和下划线单词不必翻译，请保留md语法标点符号，你翻译完后对原内容进行替换，将结果返回给我。mdx文档是:} \text{} \\
\text{(段落)}&: \text{我提供的mdx文档的内容需要翻译，只要翻译md语法中的标题、段落和列表的内容，驼峰和下划线单词不必翻译，请保留md语法标点符号，你翻译完后对原内容进行替换，将结果返回给我。} \\
\text{(列表)}&: \text{驼峰和下划线单词不必翻译，} \\
&\text{请保留md语法标点符号，} \\
&\text{你翻译完后对原内容进行替换，将结果返回给我。}
\end{align*}
\]

```python
agent_executor.invoke({"input": "Who played in Casino?"})
```
