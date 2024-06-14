# 提示策略

在本指南中，我们将介绍提升图数据库查询生成的提示策略。我们主要关注的是获取与数据库相关的信息的方法。

## 设置

首先，获取所需的软件包并设置环境变量：


```python
%pip install --upgrade --quiet  langchain langchain-community langchain-openai neo4j
```

    注意：您可能需要重新启动内核才能使用更新的软件包。
    

在本指南中，默认使用OpenAI模型，但您可以将其替换为您选择的模型提供商。


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 若要使用LangSmith，请取消下面的注释。非必需。
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

     ········
    

接下来，我们需要定义Neo4j凭据。
按照[这些安装步骤](https://neo4j.com/docs/operations-manual/current/installation/)设置Neo4j数据库。


```python
os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "password"
```

下面的示例将创建与Neo4j数据库的连接，并使用示例数据填充它，其中包含电影及其演员的信息。


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



# 过滤图模式

有时，在生成Cypher语句时，您可能需要专注于图模式的特定子集。
假设我们正在处理以下图模式：


```python
graph.refresh_schema()
print(graph.schema)
```

    节点属性如下：
    Movie {imdbRating: FLOAT, id: STRING, released: DATE, title: STRING},Person {name: STRING},Genre {name: STRING}
    关系属性如下：

    关系如下：
    (:Movie)-[:IN_GENRE]->(:Genre),(:Person)-[:DIRECTED]->(:Movie),(:Person)-[:ACTED_IN]->(:Movie)
    

假设我们希望从传递给LLM的图模式表示中排除“Genre”节点。
我们可以使用GraphCypherQAChain链的“排除”参数来实现这一目标。


```python
from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = GraphCypherQAChain.from_llm(
    graph=graph, llm=llm, exclude_types=["Genre"], verbose=True
)
```


```python
print(chain.graph_schema)
```

    节点属性如下：
    Movie {imdbRating: FLOAT, id: STRING, released: DATE, title: STRING},Person {name: STRING}
    关系属性如下：

    关系如下：
    (:Person)-[:DIRECTED]->(:Movie),(:Person)-[:ACTED_IN]->(:Movie)
    

## Few-shot示例

包含自然语言问题转换为对数据库的有效Cypher查询的示例，通常可以提高模型的性能，特别是对于复杂的查询。

假设我们有以下示例：


```python
examples = [
    {
        "question": "有多少位艺术家？",
        "query": "MATCH (a:Person)-[:ACTED_IN]->(:Movie) RETURN count(DISTINCT a)",
    },
    {
        "question": "哪些演员在电影《Casino》中出演？",
        "query": "MATCH (m:Movie {{title: 'Casino'}})<-[:ACTED_IN]-(a) RETURN a.name",
    },
    {
        "question": "汤姆·汉克斯参演了多少部电影？",
        "query": "MATCH (a:Person {{name: 'Tom Hanks'}})-[:ACTED_IN]->(m:Movie) RETURN count(m)",
    },
    {
        "question": "列出电影《辛德勒的名单》的所有流派",
        "query": "MATCH (m:Movie {{title: 'Schindler\\'s List'}})-[:IN_GENRE]->(g:Genre) RETURN g.name",
    },
    {
        "question": "哪些演员曾在喜剧和动作两种类型的电影中工作过？",
        "query": "MATCH (a:Person)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g1:Genre), (a)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g2:Genre) WHERE g1.name = 'Comedy' AND g2.name = 'Action' RETURN DISTINCT a.name",
    },
    {
        "question": "哪些导演曾和至少三位名为“约翰”的演员合作过？",
        "query": "MATCH (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person) WHERE a.name STARTS WITH 'John' WITH d, COUNT(DISTINCT a) AS JohnsCount WHERE JohnsCount >= 3 RETURN d.name",
    },
    {
        "question": "识别导演也在电影中扮演了角色的电影。",
        "query": "MATCH (p:Person)-[:DIRECTED]->(m:Movie), (p)-[:ACTED_IN]->(m) RETURN m.title, p.name",
    },
    {
        "question": "找出数据库中拥有最多电影的演员。",
        "query": "MATCH (a:Actor)-[:ACTED_IN]->(m:Movie) RETURN a.name, COUNT(m) AS movieCount ORDER BY movieCount DESC LIMIT 1",
    },
]
```

我们可以创建一个Few-shot提示，例如：


```python
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

example_prompt = PromptTemplate.from_template(
    "用户输入：{question}\nCypher查询：{query}"
)
prompt = FewShotPromptTemplate(
    examples=examples[:5],
    example_prompt=example_prompt,
    prefix="您是Neo4j专家。给定一个输入问题，请创建一个语法正确的Cypher查询来运行。\n\n以下是图模式信息\n{schema}。\n\n下面是一些问题及其对应的Cypher查询的示例。",
    suffix="用户输入：{question}\nCypher查询：",
    input_variables=["question", "schema"],
)
```


```python
print(prompt.format(question="有多少位艺术家？", schema="foo"))
```

    您是Neo4j专家。给定一个输入问题，请创建一个语法正确的Cypher查询来运行。
    
    以下是图模式信息
    foo。
    
    下面是一些问题及其对应的Cypher查询的示例。
    
    用户输入：有多少位艺术家？
    Cypher查询：MATCH (a:Person)-[:ACTED_IN]->(:Movie) RETURN count(DISTINCT a)
    
    用户输入：哪些演员在电影《Casino》中出演？
    Cypher查询：MATCH (m:Movie {title: 'Casino'})<-[:ACTED_IN]-(a) RETURN a.name
    
    用户输入：汤姆·汉克斯参演了多少部电影？
    Cypher查询：MATCH (a:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie) RETURN count(m)
    
    用户输入：列出电影《辛德勒的名单》的所有流派
    Cypher查询：MATCH (m:Movie {title: 'Schindler\'s List'})-[:IN_GENRE]->(g:Genre) RETURN g.name
    
    用户输入：哪些演员曾在喜剧和动作两种类型的电影中工作过？
    Cypher查询：MATCH (a:Person)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g1:Genre), (a)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g2:Genre) WHERE g1.name = 'Comedy' AND g2.name = 'Action' RETURN DISTINCT a.name
    
    用户输入：有多少位艺术家？
    Cypher查询： 
    
------

                

## 动态的few-shot示例

如果我们有足够的示例，我们可能只想在提示中包括最相关的示例，要么是因为它们不适合模型的上下文窗口，要么是因为长尾示例会分散模型的注意力。而且特别地，对于任何输入，我们想要包括与该输入最相关的示例。

我们可以使用ExampleSelector来实现这一点。在这种情况下，我们将使用[SemanticSimilarityExampleSelector](https://api.python.langchain.com/en/latest/example_selectors/langchain_core.example_selectors.semantic_similarity.SemanticSimilarityExampleSelector.html)，它将把示例存储在我们选择的向量数据库中。在运行时，它将在输入和我们的示例之间执行相似性搜索，并返回最具语义相似性的示例：

```python
from langchain_community.vectorstores import Neo4jVector
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    OpenAIEmbeddings(),
    Neo4jVector,
    k=5,
    input_keys=["question"],
)
```

```python
example_selector.select_examples({"question": "有多少个艺术家?"})
```

可以将ExampleSelector直接传递给我们的FewShotPromptTemplate来使用：

```python
prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="你是一个Neo4j专家。给定一个输入问题，创建一个语法正确的Cypher查询来运行。\n\n下面是模式信息\n{schema}.\n\n以下是一些问题及其相应的Cypher查询的示例。",
    suffix="用户输入：{question}\nCypher查询：",
    input_variables=["question", "schema"],
)
```

```python
print(prompt.format(question="有多少个艺术家?", schema="foo"))
```
```python
输出结果如下：

您是Neo4j专家。给定一个输入问题，创建一个语法正确的Cypher查询来运行。

以下是模式信息
foo。

以下是一些问题及其相应的Cypher查询的示例。

用户输入：有多少个艺术家?
Cypher查询：MATCH (a:Person)-[:ACTED_IN]->(:Movie) RETURN count(DISTINCT a)

用户输入：汤姆·汉克斯演了多少部电影？
Cypher查询：MATCH (a:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie) RETURN count(m)

用户输入：哪些演员在喜剧和动作两种类型的电影中都有作品？
Cypher查询：MATCH (a:Person)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g1:Genre), (a)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g2:Genre) WHERE g1.name = 'Comedy' AND g2.name = 'Action' RETURN DISTINCT a.name

用户输入：哪些导演拍摄了至少三部不同演员名字中带有“John”的电影？
Cypher查询：MATCH (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person) WHERE a.name STARTS WITH 'John' WITH d, COUNT(DISTINCT a) AS JohnsCount WHERE JohnsCount >= 3 RETURN d.name

用户输入：数据库中电影数量最多的演员是谁？
Cypher查询：MATCH (a:Actor)-[:ACTED_IN]->(m:Movie) RETURN a.name, COUNT(m) AS movieCount ORDER BY movieCount DESC LIMIT 1

用户输入：有多少个艺术家?
Cypher查询：
```

```python
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = GraphCypherQAChain.from_llm(
    graph=graph, llm=llm, cypher_prompt=prompt, verbose=True
)
```

```python
chain.invoke("图谱中有多少个演员？")
```

输出结果如下：

> 进入新的GraphCypherQAChain链...
生成的Cypher查询：
MATCH (a:Person)-[:ACTED_IN]->(:Movie) RETURN count(DISTINCT a)
完整上下文：
[{'count(DISTINCT a)': 967}]

> 链结束。

查询："图谱中有多少个演员？"
结果："图谱中有967位演员。"

# 提示策略

在本指南中，我们将讨论改进SQL查询生成的提示策略。我们主要关注的是获取与数据库特定信息相关的方法。

## 设置

首先，获取所需的软件包并设置环境变量:


```python
%pip install --upgrade --quiet  langchain langchain-community langchain-experimental langchain-openai
```

在本指南中，我们默认使用OpenAI模型，但您可以将其替换为您选择的模型提供商。


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 如需使用LangSmith，请取消下面的注释。不是必需的。
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

以下示例将使用带有Chinook数据库的SQLite连接。请按照[这些安装步骤](https://database.guide/2-sample-databases-sqlite/)在与此笔记本相同的目录中创建`Chinook.db`：

* 将[此文件](https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql)保存为`Chinook_Sqlite.sql`
* 运行 `sqlite3 Chinook.db`
* 运行 `.read Chinook_Sqlite.sql`
* 测试 `SELECT * FROM Artist LIMIT 10;`

现在，我们的目录中有了`Chinhook.db`，我们可以使用基于SQLAlchemy的`SQLDatabase`类与其进行交互:


```python
from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Chinook.db", sample_rows_in_table_info=3)
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")
```

    sqlite
    ['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track']
    




    "[(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith'), (4, 'Alanis Morissette'), (5, 'Alice In Chains'), (6, 'Antônio Carlos Jobim'), (7, 'Apocalyptica'), (8, 'Audioslave'), (9, 'BackBeat'), (10, 'Billy Cobham')]"



## 特定于方言的提示

我们可以做的最简单的事情之一是使我们的提示特定于正在使用的SQL方言。当使用内置的[create_sql_query_chain](https://api.python.langchain.com/en/latest/chains/langchain.chains.sql_database.query.create_sql_query_chain.html)和[SQLDatabase](https://api.python.langchain.com/en/latest/utilities/langchain_community.utilities.sql_database.SQLDatabase.html)时，这对于以下任何方言都是被处理的:


```python
from langchain.chains.sql_database.prompt import SQL_PROMPTS

list(SQL_PROMPTS)
```




    ['crate',
     'duckdb',
     'googlesql',
     'mssql',
     'mysql',
     'mariadb',
     'oracle',
     'postgresql',
     'sqlite',
     'clickhouse',
     'prestodb']



例如，使用我们当前的数据库，我们可以看到我们将得到一个特定于SQLite的提示:


```python
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature="0")
chain = create_sql_query_chain(llm, db)
chain.get_prompts()[0].pretty_print()
```

    You are a SQLite expert. Given an input question, first create a syntactically correct SQLite query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most 5 results using the LIMIT clause as per SQLite. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use date('now') function to get the current date, if the question involves "today".
    
    Use the following format:
    
    Question: Question here
    SQLQuery: SQL Query to run
    SQLResult: Result of the SQLQuery
    Answer: Final answer here
    
    Only use the following tables:
    [33;1m[1;3m{table_info}[0m
    
    Question: [33;1m[1;3m{input}[0m
    

## 表定义和示例行

在基本的SQL链中，我们将至少需要向模型提供数据库模式的一部分。如果没有这个，它将无法生成有效的查询。我们的数据库提供了一些方便的方法来给我们提供相关上下文。具体来说，我们可以获取表名、它们的模式以及每个表的示例行:


```python
context = db.get_context()
print(list(context))
print(context["table_info"])
```

    ['table_info', 'table_names']
    
    CREATE TABLE "Album" (
    	"AlbumId" INTEGER NOT NULL, 
    	"Title" NVARCHAR(160) NOT NULL, 
    	"ArtistId" INTEGER NOT NULL, 
    	PRIMARY KEY ("AlbumId"), 
    	FOREIGN KEY("ArtistId") REFERENCES "Artist" ("ArtistId")
    )
    
    /*
    3 rows from Album table:
    AlbumId	Title	ArtistId
    1	For Those About To Rock We Salute You	1
    2	Balls to the Wall	2
    3	Restless and Wild	2
    */
    
    
    CREATE TABLE "Artist" (
    	"ArtistId" INTEGER NOT NULL, 
    	"Name" NVARCHAR(120), 
    	PRIMARY KEY ("ArtistId")
    )
    
    /*
    3 rows from Artist table:
    ArtistId	Name
    1	AC/DC
    2	Accept
    3	Aerosmith
    */
    
    
    CREATE TABLE "Customer" (
    	"CustomerId" INTEGER NOT NULL, 
    	"FirstName" NVARCHAR(40) NOT NULL, 
    	"LastName" NVARCHAR(20) NOT NULL, 
    	"Company" NVARCHAR(80), 
    	"Address" NVARCHAR(70), 
    	"City" NVARCHAR(40), 
    	"State" NVARCHAR(40), 
    	"Country" NVARCHAR(40), 
    	"PostalCode" NVARCHAR(10), 
    	"Phone" NVARCHAR(24), 
    	"Fax" NVARCHAR(24), 
    	"Email" NVARCHAR(60) NOT NULL, 
    	"SupportRepId" INTEGER, 
    	PRIMARY KEY ("CustomerId"), 
    	FOREIGN KEY("SupportRepId") REFERENCES "Employee" ("EmployeeId")
    )
    
    /*
    3 rows from Customer table:
    CustomerId	FirstName	LastName	Company	Address	City	State	Country	PostalCode	Phone	Fax	Email	SupportRepId
    1	Luís	Gonçalves	Embraer - Empresa Brasileira de Aeronáutica S.A.	Av. Brigadeiro Faria Lima, 2170	São José dos Campos	SP	Brazil	12227-000	+55 (12) 3923-5555	+55 (12) 3923-5566	luisg@embraer.com.br	3
    2	Leonie	Köhler	None	Theodor-Heuss-Straße 34	Stuttgart	None	Germany	70174	+49 0711 2842222	None	leonekohler@surfeu.de	5
    3	François	Tremblay	None	1498 rue Bélanger	Montréal	QC	Canada	H2G 1A7	+1 (514) 721-4711	None	ftremblay@gmail.com	3
    */
    
    
    CREATE TABLE "Employee" (
    	"EmployeeId" INTEGER NOT NULL, 
    	"LastName" NVARCHAR(20) NOT NULL, 
    	"FirstName" NVARCHAR(20) NOT NULL, 
    	"Title" NVARCHAR(30), 
    	"ReportsTo" INTEGER, 
    	"BirthDate" DATETIME, 
    	"HireDate" DATETIME, 
    	"Address" NVARCHAR(70), 
    	"City" NVARCHAR(40), 
    	"State" NVARCHAR(40), 
    	"Country" NVARCHAR(40), 
    	"PostalCode" NVARCHAR(10), 
    	"Phone" NVARCHAR(24), 
    	"Fax" NVARCHAR(24), 
    	"Email" NVARCHAR(60), 
    	PRIMARY KEY ("EmployeeId"), 
    	FOREIGN KEY("ReportsTo") REFERENCES "Employee" ("EmployeeId")
    )
    
    /*
    3 rows from Employee table:
    EmployeeId	LastName	FirstName	Title	ReportsTo	BirthDate	HireDate	Address	City	State	Country	PostalCode	Phone	Fax	Email
    1	Adams	Andrew	General Manager	None	1962-02-18 00:00:00	2002-08-14 00:00:00	11120 Jasper Ave NW	Edmonton	AB	Canada	T5K 2N1	+1 (780) 428-9482	+1 (780) 428-3457	andrew@chinookcorp.com
    2	Edwards	Nancy	Sales Manager	1	1958-12-08 00:00:00	2002-05-01 00:00:00	825 8 Ave SW	Calgary	AB	Canada	T2P 2T3	+1 (403) 262-3443	+1 (403) 262-3322	nancy@chinookcorp.com
    3	Peacock	Jane	Sales Support Agent	2	1973-08-29 00:00:00	2002-04-01 00:00:00	1111 6 Ave SW	Calgary	AB	Canada	T2P 5M5	+1 (403) 262-3443	+1 (403) 262-6712	jane@chinookcorp.com
    */
    
    
    CREATE TABLE "Genre" (
    	"GenreId" INTEGER NOT NULL, 
    	"Name" NVARCHAR(120), 
    	PRIMARY KEY ("GenreId")
    )
    
    /*
    3 rows from Genre table:
    GenreId	Name
    1	Rock
    2	Jazz
    3	Metal
    */
    
    
    CREATE TABLE "Invoice" (
    	"InvoiceId" INTEGER NOT NULL, 
    	"CustomerId" INTEGER NOT NULL, 
    	"InvoiceDate" DATETIME NOT NULL, 
    	"BillingAddress" NVARCHAR(70), 
    	"BillingCity" NVARCHAR(40), 
    	"BillingState" NVARCHAR(40), 
    	"BillingCountry" NVARCHAR(40), 
    	"BillingPostalCode" NVARCHAR(10), 
    	"Total" NUMERIC(10, 2) NOT NULL, 
    	PRIMARY KEY ("InvoiceId"), 
    	FOREIGN KEY("CustomerId") REFERENCES "Customer" ("CustomerId")
    )
    
    /*
    3 rows from Invoice table:
    InvoiceId	CustomerId	InvoiceDate	BillingAddress	BillingCity	BillingState	BillingCountry	BillingPostalCode	Total
    1	2	2009-01-01 00:00:00	Theodor-Heuss-Straße 34	Stuttgart	None	Germany	70174	1.98
    2	4	2009-01-02 00:00:00	Ullevålsveien 14	Oslo	None	Norway	0171	3.96
    3	8	2009-01-03 00:00:00	Grétrystraat 63	Brussels	None	Belgium	1000	5.94
    */
    
    
    CREATE TABLE "InvoiceLine" (
    	"InvoiceLineId" INTEGER NOT NULL, 
    	"InvoiceId" INTEGER NOT NULL, 
    	"TrackId" INTEGER NOT NULL, 
    	"UnitPrice" NUMERIC(10, 2) NOT NULL, 
    	"Quantity" INTEGER NOT NULL, 
    	PRIMARY KEY ("InvoiceLineId"), 
    	FOREIGN KEY("TrackId") REFERENCES "Track" ("TrackId"), 
    	FOREIGN KEY("InvoiceId") REFERENCES "Invoice" ("InvoiceId")
    )
    
    /*
    3 rows from InvoiceLine table:
    InvoiceLineId	InvoiceId	TrackId	UnitPrice	Quantity
    1	1	2	0.99	1
    2	1	4	0.99	1
    3	2	6	0.99	1
    */
    
    
    CREATE TABLE "MediaType" (
    	"MediaTypeId" INTEGER NOT NULL, 
    	"Name" NVARCHAR(120), 
    	PRIMARY KEY ("MediaTypeId")
    )
    
    /*
    3 rows from MediaType table:
    MediaTypeId	Name
    1	MPEG audio file
    2	Protected AAC audio file
    3	Protected MPEG-4 video file
    */
    
    
    CREATE TABLE "Playlist" (
    	"PlaylistId" INTEGER NOT NULL, 
    	"Name" NVARCHAR(120), 
    	PRIMARY KEY ("PlaylistId")
    )
    
    /*
    3 rows from Playlist table:
    PlaylistId	Name
    1	Music
    2	Movies
    3	TV Shows
    */
    
    
    CREATE TABLE "PlaylistTrack" (
    	"PlaylistId" INTEGER NOT NULL, 
    	"TrackId" INTEGER NOT NULL, 
    	PRIMARY KEY ("PlaylistId", "TrackId"), 
    	FOREIGN KEY("TrackId") REFERENCES "Track" ("TrackId"), 
    	FOREIGN KEY("PlaylistId") REFERENCES "Playlist" ("PlaylistId")
    )
    
    /*
    3 rows from PlaylistTrack table:
    PlaylistId	TrackId
    1	3402
    1	3389
    1	3390
    */
    
    
    CREATE TABLE "Track" (
    	"TrackId" INTEGER NOT NULL, 
    	"Name" NVARCHAR(200) NOT NULL, 
    	"AlbumId" INTEGER, 
    	"MediaTypeId" INTEGER NOT NULL, 
    	"GenreId" INTEGER, 
    	"Composer" NVARCHAR(220), 
    	"Milliseconds" INTEGER NOT NULL, 
    	"Bytes" INTEGER, 
    	"UnitPrice" NUMERIC(10, 2) NOT NULL, 
    	PRIMARY KEY ("TrackId"), 
    	FOREIGN KEY("MediaTypeId") REFERENCES "MediaType" ("MediaTypeId"), 
    	FOREIGN KEY("GenreId") REFERENCES "Genre" ("GenreId"), 
    	FOREIGN KEY("AlbumId") REFERENCES "Album" ("AlbumId")
    )
    
    /*
    3 rows from Track table:
    TrackId	Name	AlbumId	MediaTypeId	GenreId	Composer	Milliseconds	Bytes	UnitPrice
    1	For Those About To Rock (We Salute You)	1	1	1	Angus Young, Malcolm Young, Brian Johnson	343719	11170334	0.99
    2	Balls to the Wall	2	2	1	None	342562	5510424	0.99
    3	Fast As a Shark	3	2	1	F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman	230619	3990994	0.99
    */
    

当我们没有太多或太宽的表时，我们可以将所有这些信息都插入到我们的提示中:


```python
prompt_with_context = chain.get_prompts()[0].partial(table_info=context["table_info"])
print(prompt_with_context.pretty_repr()[:1500])
```

    You are a SQLite expert. Given an input question, first create a syntactically correct SQLite query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most 5 results using the LIMIT clause as per SQLite. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use date('now') function to get the current date, if the question involves "today".
    
    Use the following format:
    
    Question: Question here
    SQLQuery: SQL Query to run
    SQLResult: Result of the SQLQuery
    Answer: Final answer here
    
    Only use the following tables:
    
    CREATE TABLE "Album" (
    	"AlbumId" INTEGER NOT NULL, 
    	"Title" NVARCHAR(160) NOT NULL, 
    	"ArtistId" INTEGER NOT NULL, 
    	PRIMARY KEY ("AlbumId"), 
    	FOREIGN KEY("ArtistId") REFERENCES "Artist" ("ArtistId")
    )
    
    /*
    3 rows from Album table:
    AlbumId	Title	ArtistId
    1	For Those About To Rock We Salute You	1
    2	Balls to the Wall	2
    3	Restless and Wild	2
    */
    
    
    CREATE TABLE "Artist" (
    	"ArtistId" INTEGER NOT NULL, 
    	"Name" NVARCHAR(120)


## 几个示例

在提示中包含将自然语言问题转换为有效SQL查询的示例，通常会提高模型的性能，特别是对于复杂的查询。

假设我们有以下示例：

```python
examples = [
    {"input": "列出所有艺术家。", "query": "SELECT * FROM Artist;"},
    {
        "input": "查找艺术家 'AC/DC' 的所有专辑。",
        "query": "SELECT * FROM Album WHERE ArtistId = (SELECT ArtistId FROM Artist WHERE Name = 'AC/DC');",
    },
    {
        "input": "列出'摇滚'流派的所有曲目。",
        "query": "SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock');",
    },
    {
        "input": "找出所有曲目的总时长。",
        "query": "SELECT SUM(Milliseconds) FROM Track;",
    },
    {
        "input": "列出所有来自加拿大的顾客。",
        "query": "SELECT * FROM Customer WHERE Country = 'Canada';",
    },
    {
        "input": "ID为5的专辑中有多少曲目？",
        "query": "SELECT COUNT(*) FROM Track WHERE AlbumId = 5;",
    },
    {
        "input": "计算总发票数。",
        "query": "SELECT COUNT(*) FROM Invoice;",
    },
    {
        "input": "列出时长超过5分钟的所有曲目。",
        "query": "SELECT * FROM Track WHERE Milliseconds > 300000;",
    },
    {
        "input": "按总购买额排名前5位的客户是谁？",
        "query": "SELECT CustomerId, SUM(Total) AS TotalPurchase FROM Invoice GROUP BY CustomerId ORDER BY TotalPurchase DESC LIMIT 5;",
    },
    {
        "input": "哪些专辑来自于2000年？",
        "query": "SELECT * FROM Album WHERE strftime('%Y', ReleaseDate) = '2000';",
    },
    {
        "input": "公司共有多少名员工",
        "query": 'SELECT COUNT(*) FROM "Employee"',
    },
]
```

我们可以像这样使用它们创建一个few-shot提示：

```python
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

example_prompt = PromptTemplate.from_template("用户输入: {input}\nSQL查询: {query}")
prompt = FewShotPromptTemplate(
    examples=examples[:5],
    example_prompt=example_prompt,
    prefix="你是一个SQLite专家。给定一个输入问题，请创建一个语法正确的SQLite查询以运行。除非另有说明，不要返回超过{top_k}行。\n\n这是相关表的信息: {table_info}\n\n以下是一些问题及其对应的SQL查询的示例。",
    suffix="用户输入: {input}\nSQL查询: ",
    input_variables=["input", "top_k", "table_info"],
)
```

```python
print(prompt.format(input="有多少个艺术家？", top_k=3, table_info="foo"))
```

    你是一个SQLite专家。给定一个输入问题，请创建一个语法正确的SQLite查询以运行。除非另有说明，不要返回超过3行。
    
    这是相关表的信息: foo
    
    以下是一些问题及其对应的SQL查询的示例。
    
    用户输入: 列出所有艺术家。
    SQL查询: SELECT * FROM Artist;
    
    用户输入: 查找艺术家 'AC/DC' 的所有专辑。
    SQL查询: SELECT * FROM Album WHERE ArtistId = (SELECT ArtistId FROM Artist WHERE Name = 'AC/DC');
    
    用户输入: 列出'摇滚'流派的所有曲目。
    SQL查询: SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock');
    
    用户输入: 找出所有曲目的总时长。
    SQL查询: SELECT SUM(Milliseconds) FROM Track;
    
    用户输入: 列出所有来自加拿大的顾客。
    SQL查询: SELECT * FROM Customer WHERE Country = 'Canada';
    
    用户输入: 有多少个艺术家？
    SQL查询: 
    

## 动态few-shot示例

如果我们有足够的示例，我们可能只想在提示中包含最相关的示例，要么是因为它们不适合模型的上下文窗口，要么是因为示例中的长尾部分会分散模型的注意力。具体而言，对于任何输入，我们希望包含与该输入最相关的示例。

我们可以使用ExampleSelector来实现这一点。在这种情况下，我们将使用[SemanticSimilarityExampleSelector](https://api.python.langchain.com/en/latest/example_selectors/langchain_core.example_selectors.semantic_similarity.SemanticSimilarityExampleSelector.html)，它将示例存储在我们选择的向量数据库中。运行时它会在输入和示例之间进行语义相似性搜索，并返回最相似的示例：

```python
from langchain_community.vectorstores import FAISS
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    OpenAIEmbeddings(),
    FAISS,
    k=5,
    input_keys=["input"],
)
```

```python
example_selector.select_examples({"input": "有多少个艺术家？"})
```

返回：

```
[{'input': '列出所有艺术家。', 'query': 'SELECT * FROM Artist;'},
 {'input': '公司共有多少名员工', 'query': 'SELECT COUNT(*) FROM "Employee"'},
 {'input': 'ID为5的专辑中有多少曲目？',
  'query': 'SELECT COUNT(*) FROM Track WHERE AlbumId = 5;'},
 {'input': '哪些专辑来自于2000年？',
  'query': "SELECT * FROM Album WHERE strftime('%Y', ReleaseDate) = '2000';"},
 {'input': "列出'摇滚'流派的所有曲目。",
  'query': "SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock');"}]
```

要使用它，我们可以直接将ExampleSelector传递给我们的FewShotPromptTemplate：

```python
prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="你是一个SQLite专家。给定一个输入问题，请创建一个语法正确的SQLite查询以运行。除非另有说明，不要返回超过{top_k}行。\n\n这是相关表的信息: {table_info}\n\n以下是一些问题及其对应的SQL查询的示例。",
    suffix="用户输入: {input}\nSQL查询: ",
    input_variables=["input", "top_k", "table_info"],
)
```

```python
print(prompt.format(input="有多少个艺术家？", top_k=3, table_info="foo"))
```

    你是一个SQLite专家。给定一个输入问题，请创建一个语法正确的SQLite查询以运行。除非另有说明，不要返回超过3行。
    
    这是相关表的信息: foo
    
    以下是一些问题及其对应的SQL查询的示例。
    
    用户输入: 列出所有艺术家。
    SQL查询: SELECT * FROM Artist;
    
    用户输入: 公司共有多少名员工
    SQL查询: SELECT COUNT(*) FROM "Employee"
    
    用户输入: ID为5的专辑中有多少曲目？
    SQL查询: SELECT COUNT(*) FROM Track WHERE AlbumId = 5;
    
    用户输入: 哪些专辑来自于2000年？
    SQL查询: SELECT * FROM Album WHERE strftime('%Y', ReleaseDate) = '2000';
    
    用户输入: 列出'摇滚'流派的所有曲目。
    SQL查询: SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock');
    
    用户输入: 有多少个艺术家？
    SQL查询: 
    
=======



# 工具使用不需要函数调用

在本指南中，我们将构建一个不依赖于任何特殊模型API（例如函数调用，我们在[快速入门](/use_cases/tool_use/quickstart)中展示过）的链式结构，而是直接提示模型调用工具。

## 设置

我们需要安装以下软件包:

```python
%pip install --upgrade --quiet langchain langchain-openai
```

并设置以下环境变量:

```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 如果您想使用LangSmith，请取消下面的注释:
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 创建一个工具

首先，我们需要创建一个要调用的工具。对于这个示例，我们将从一个函数创建一个自定义工具。关于创建自定义工具的所有详细信息，请参见[此指南](/modules/tools/)。

```python
from langchain_core.tools import tool


@tool
def multiply(first_int: int, second_int: int) -> int:
    """将两个整数相乘。"""
    return first_int * second_int
```

```python
print(multiply.name)
print(multiply.description)
print(multiply.args)
```

输出为:

```
multiply
multiply(first_int: int, second_int: int) -> int - 将两个整数相乘。
{'first_int': {'title': 'First Int', 'type': 'integer'}, 'second_int': {'title': 'Second Int', 'type': 'integer'}}
```

```python
multiply.invoke({"first_int": 4, "second_int": 5})
```

输出为:

```
20
```

## 创建我们的提示信息

我们需要编写一个提示信息，其中指定了模型可以访问的工具、这些工具的参数以及模型的期望输出格式。在这种情况下，我们将指示它输出一个形式为`{"name": "...", "arguments": {...}}`的JSON块。

```python
from langchain.tools.render import render_text_description

rendered_tools = render_text_description([multiply])
rendered_tools
```

输出为:

```
'multiply: multiply(first_int: int, second_int: int) -> int - 将两个整数相乘。'
```

```python
from langchain_core.prompts import ChatPromptTemplate

system_prompt = f"""You are an assistant that has access to the following set of tools. Here are the names and descriptions for each tool:

{rendered_tools}

Given the user input, return the name and input of the tool to use. Return your response as a JSON blob with 'name' and 'arguments' keys."""

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("user", "{input}")]
)
```

## 添加输出解析器

我们将使用`JsonOutputParser`将模型的输出解析为JSON。

```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = prompt | model | JsonOutputParser()
chain.invoke({"input": "13乘以4是多少"})
```

输出为:

```
{'name': 'multiply', 'arguments': {'first_int': 13, 'second_int': 4}}
```

## 调用工具

我们可以通过将模型生成的"arguments"传递给工具来作为链的一部分来调用工具:

```python
from operator import itemgetter

chain = prompt | model | JsonOutputParser() | itemgetter("arguments") | multiply
chain.invoke({"input": "13乘以4是多少"})
```

输出为:

```
52
```

## 从多个工具中选择

假设我们有多个工具希望链式结构能够选择:

```python
@tool
def add(first_int: int, second_int: int) -> int:
    "将两个整数相加。"
    return first_int + second_int

@tool
def exponentiate(base: int, exponent: int) -> int:
    "将基数的指数幂。"
    return base**exponent
```

通过函数调用，我们可以这样做:

如果我们想要运行模型选择的工具，我们可以使用一个根据模型输出返回工具的函数。具体而言，我们的函数将返回它自己的子链，该子链获取模型输出的"arguments"部分并将其传递给所选择的工具:

```python
tools = [add, exponentiate, multiply]

def tool_chain(model_output):
    tool_map = {tool.name: tool for tool in tools}
    chosen_tool = tool_map[model_output["name"]]
    return itemgetter("arguments") | chosen_tool
```

```python
rendered_tools = render_text_description(tools)
system_prompt = f"""You are an assistant that has access to the following set of tools. Here are the names and descriptions for each tool:

{rendered_tools}

Given the user input, return the name and input of the tool to use. Return your response as a JSON blob with 'name' and 'arguments' keys."""

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("user", "{input}")]
)

chain = prompt | model | JsonOutputParser() | tool_chain
chain.invoke({"input": "3加1132等于多少"})
```

输出为:

```
1135
```
------



## 返回工具输入

返回工具的输出以及工具的输入是很有帮助的。我们可以使用LCEL来实现这一点，通过在`RunnablePassthrough`组件上使用`assign`方法来赋值工具的输出。这将接受传递给`RunnablePassthrough`组件的任何输入（假设是一个字典），并在保留当前输入内容的同时添加一个键：

```python
from langchain_core.runnables import RunnablePassthrough

chain = (
    prompt | model | JsonOutputParser() | RunnablePassthrough.assign(output=tool_chain)
)
chain.invoke({"input": "3加上1132等于多少"})
```

输出结果为:

```python
{'name': 'add',
 'arguments': {'first_int': 3, 'second_int': 1132},
 'output': 1135}
```
------
