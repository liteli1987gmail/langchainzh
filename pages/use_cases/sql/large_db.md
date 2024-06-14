# 大型数据库

为了对数据库编写有效的查询，我们需要为模型提供表名、表结构和要查询的特征值。当存在许多表、列和/或高基数列时，我们无法在每个提示中转储有关数据库的完整信息。相反，我们必须找到方法，在提示中动态插入最相关的信息。让我们来看看如何实现这些技术。

## 设置

首先，获取所需的包并设置环境变量：

```python
%pip install --upgrade --quiet langchain langchain-community langchain-openai
```

    请注意：您可能需要重新启动内核才能使用更新后的包。

在本指南中，我们默认使用OpenAI模型，但您可以根据自己的选择切换到其他模型供应商。

```python
import getpass
import os

# os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 取消下面一行的注释以使用LangSmith。不是必需的。
os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

    ········

下面的示例将使用一个带有Chinook数据库的SQLite连接。按照[这些安装步骤](https://database.guide/2-sample-databases-sqlite/)在与此笔记本相同的目录中创建`Chinook.db`：

* 将[此文件](https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql)保存为`Chinook_Sqlite.sql`
* 运行`sqlite3 Chinook.db`
* 运行`.read Chinook_Sqlite.sql`
* 测试`SELECT * FROM Artist LIMIT 10;`

现在，`Chinhook.db`位于我们的目录中，我们可以使用基于SQLAlchemy的[SQLDatabase](https://api.python.langchain.com/en/latest/utilities/langchain_community.utilities.sql_database.SQLDatabase.html)类进行接口操作：

```python
from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")
```

    sqlite
    ['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track']
    




    "[(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith'), (4, 'Alanis Morissette'), (5, 'Alice In Chains'), (6, 'Antônio Carlos Jobim'), (7, 'Apocalyptica'), (8, 'Audioslave'), (9, 'BackBeat'), (10, 'Billy Cobham')]"



## 多个表

在我们的提示中包含的主要信息之一是相关表的结构。当我们有很多表时，无法在单个提示中展示所有的结构。在这种情况下，我们可以先提取与用户输入相关的表名，然后只包含它们的结构。

一种简单而可靠的方法是使用OpenAI的函数调用和Pydantic模型。LangChain提供了一个内置的[create_extraction_chain_pydantic](https://api.python.langchain.com/en/latest/chains/langchain.chains.openai_tools.extraction.create_extraction_chain_pydantic.html)链，让我们可以做到这一点：

```python
from langchain.chains.openai_tools import create_extraction_chain_pydantic
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)


class Table(BaseModel):
    """SQL数据库中的表。"""

    name: str = Field(description="SQL数据库中的表名。")


table_names = "\n".join(db.get_usable_table_names())
system = f"""返回与用户问题可能相关的**所有SQL表的名称**。
这些表包括：

{table_names}

请记住，**包括所有可能相关的表**，即使您不确定它们是否需要。"""
table_chain = create_extraction_chain_pydantic(Table, llm, system_message=system)
table_chain.invoke({"input": "Alanis Morisette歌曲的全部类型是什么"})
```

这很有效！除了在下面将要看到的，实际上我们还需要一些其他的表。基于仅根据用户问题，模型可能难以知道这一点。在这种情况下，我们可以通过将表分组来简化模型的工作。我们只需要让模型在"音乐"和"业务"之间进行选择，并从中选择所有相关的表：

```python
system = """返回与用户问题相关的SQL表的名称。
这些表包括：

音乐
业务"""
category_chain = create_extraction_chain_pydantic(Table, llm, system_message=system)
category_chain.invoke({"input": "Alanis Morisette的全部类型是什么"})
```

运行结果如下：

```
[Table(name='音乐')]
```

```python
from typing import List


def get_tables(categories: List[Table]) -> List[str]:
    tables = []
    for category in categories:
        if category.name == "音乐":
            tables.extend(
                [
                    "Album",
                    "Artist",
                    "Genre",
                    "MediaType",
                    "Playlist",
                    "PlaylistTrack",
                    "Track",
                ]
            )
        elif category.name == "业务":
            tables.extend(["Customer", "Employee", "Invoice", "InvoiceLine"])
    return tables


table_chain = category_chain | get_tables  # noqa
table_chain.invoke({"input": "Alanis Morisette的全部类型是什么"})
```

运行结果如下：

```
['Album', 'Artist', 'Genre', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track']
```

现在，我们已经获得了可以为任何查询输出相关表的链。我们可以将其与我们的[create_sql_query_chain](https://api.python.langchain.com/en/latest/chains/langchain.chains.sql_database.query.create_sql_query_chain.html)结合使用，该链可以接受一个`table_names_to_use`列表来确定在提示中包含哪些表结构：

```python
from operator import itemgetter

from langchain.chains import create_sql_query_chain
from langchain_core.runnables import RunnablePassthrough

query_chain = create_sql_query_chain(llm, db)
# 将"question"键转换为当前table_chain所需的"input"键。
table_chain = {"input": itemgetter("question")} | table_chain
# 使用table_chain设置table_names_to_use。
full_chain = RunnablePassthrough.assign(table_names_to_use=table_chain) | query_chain
```

```python
query = full_chain.invoke(
    {"question": "Alanis Morisette的全部类型是什么"}
)
print(query)
```

运行结果如下：

```
SELECT "Genre"."Name"
FROM "Genre"
JOIN "Track" ON "Genre"."GenreId" = "Track"."GenreId"
JOIN "Album" ON "Track"."AlbumId" = "Album"."AlbumId"
JOIN "Artist" ON "Album"."ArtistId" = "Artist"."ArtistId"
WHERE "Artist"."Name" = 'Alanis Morissette'
```

```python
db.run(query)
```

运行结果如下：

```
[('Rock',), ('Rock',), ('Rock',), ('Rock',), ('Rock',), ('Rock',), ('Rock',), ('Rock',), ('Rock',), ('Rock',), ('Rock',), ('Rock',), ('Rock',)]
```

我们可以稍微改写我们的问题，消除回答中的冗余内容：

```python
query = full_chain.invoke(
    {"question": "Alanis Morisette的所有歌曲的唯一类型是什么"}
)
print(query)
```

运行结果如下：

```
SELECT DISTINCT g.Name
FROM Genre g
JOIN Track t ON g.GenreId = t.GenreId
JOIN Album a ON t.AlbumId = a.AlbumId
JOIN Artist ar ON a.ArtistId = ar.ArtistId
WHERE ar.Name = 'Alanis Morissette'
```

```python
db.run(query)
```

运行结果如下：

```
[('Rock',)]
```

我们可以在此处查看此次运行的[LangSmith跟踪](https://smith.langchain.com/public/20b8ef90-1dac-4754-90f0-6bc11203c50a/r)。

我们已经了解了如何在链中动态包含一小部分表结构的提示。解决此问题的另一种可能的方法是通过为代理提供一个工具，让代理自行决定何时查找表。您可以在[SQL：代理](/use_cases/sql/agents)指南中看到此类示例。=======

## 高基数列

为了过滤包含专有名词（例如地址、歌曲名称或艺术家名称）的列，我们首先需要仔细检查拼写，以便正确过滤数据。

一个简单的策略是创建一个向量存储，包含数据库中存在的所有不同的专有名词。然后，我们可以对每个用户输入查询该向量存储，并将最相关的专有名词插入到提示中。

首先，我们需要每个实体的唯一值，为此我们定义了一个函数，将结果解析为一个元素列表：

```python
import ast
import re

def query_as_list(db, query):
    res = db.run(query)
    res = [el for sub in ast.literal_eval(res) for el in sub if el]
    res = [re.sub(r"\b\d+\b", "", string).strip() for string in res]
    return res

proper_nouns = query_as_list(db, "SELECT Name FROM Artist")
proper_nouns += query_as_list(db, "SELECT Title FROM Album")
proper_nouns += query_as_list(db, "SELECT Name FROM Genre")
len(proper_nouns)
proper_nouns[:5]
```
现在，我们可以将所有值嵌入和存储在向量数据库中：
```python
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

vector_db = FAISS.from_texts(proper_nouns, OpenAIEmbeddings())
retriever = vector_db.as_retriever(search_kwargs={"k": 15})
```
然后，我们可以创建一个查询构造链，首先从数据库检索值，并将其插入到提示中：
```python
from operator import itemgetter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

system = """You are a SQLite expert. Given an input question, create a syntactically \
correct SQLite query to run. Unless otherwise specificed, do not return more than \
{top_k} rows.\n\nHere is the relevant table info: {table_info}\n\nHere is a non-exhaustive \
list of possible feature values. If filtering on a feature value make sure to check its spelling \
against this list first:\n\n{proper_nouns}"""

prompt = ChatPromptTemplate.from_messages([("system", system), ("human", "{input}")])

query_chain = create_sql_query_chain(llm, db, prompt=prompt)
retriever_chain = (
    itemgetter("question")
    | retriever
    | (lambda docs: "\n".join(doc.page_content for doc in docs))
)
chain = RunnablePassthrough.assign(proper_nouns=retriever_chain) | query_chain
```
让我们试验一下链条，看看在不使用检索和使用检索的情况下，当我们尝试过滤掉"elenis moriset"（Alanis Morissette的拼写错误）时会发生什么：
```python
# Without retrieval
query = query_chain.invoke(
    {"question": "What are all the genres of elenis moriset songs", "proper_nouns": ""}
)
print(query)
db.run(query)
```
```
SELECT DISTINCT Genre.Name
FROM Genre
JOIN Track ON Genre.GenreId = Track.GenreId
JOIN Album ON Track.AlbumId = Album.AlbumId
JOIN Artist ON Album.ArtistId = Artist.ArtistId
WHERE Artist.Name = 'Elenis Moriset'
```
```python
# With retrieval
query = chain.invoke({"question": "What are all the genres of elenis moriset songs"})
print(query)
db.run(query)
```
```
SELECT DISTINCT Genre.Name
FROM Genre
JOIN Track ON Genre.GenreId = Track.GenreId
JOIN Album ON Track.AlbumId = Album.AlbumId
JOIN Artist ON Album.ArtistId = Artist.ArtistId
WHERE Artist.Name = 'Alanis Morissette'
```
我们可以发现，通过检索，我们能够更正拼写并获得有效的结果。

解决这个问题的另一种可能方法是让一个Agent自行决定何时查找专有名词。你可以在 [SQL: Agents](/use_cases/sql/agents) 指南中看到这个问题的一个例子。
