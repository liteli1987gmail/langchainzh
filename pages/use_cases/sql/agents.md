# 代理商

LangChain有一个SQL代理，它提供了与SQL数据库交互的更灵活的方式，比链更好。使用SQL代理的主要优势是：

- 它可以根据数据库的模式和数据库的内容（例如描述特定表）来回答问题。
- 它可以通过运行生成的查询、捕获回溯并正确地重新生成它来恢复错误。
- 它可以根据需要多次查询数据库以回答用户的问题。
- 它将只从相关表中检索模式，从而节省令牌。

要初始化代理，我们将使用[create_sql_agent](https://api.python.langchain.com/en/latest/agent_toolkits/langchain_community.agent_toolkits.sql.base.create_sql_agent.html)构造函数。该代理使用`SQLDatabaseToolkit`，其中包含以下工具：

* 创建和执行查询
* 检查查询语法
* 检索表描述
* ...等等

## 设置

首先，获取所需的软件包并设置环境变量：


```python
%pip install --upgrade --quiet  langchain langchain-community langchain-openai
```

在本指南中，我们默认使用OpenAI模型，但您可以根据自己的选择替换它们的模型提供商。


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 若要使用LangSmith，请取消下面的注释。不是必需的。
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

下面的示例将使用SQLite连接和Chinook数据库。按照以下安装步骤在与此笔记本相同的目录中创建`Chinook.db`：

- 将[此文件](https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql)保存为`Chinook_Sqlite.sql`
- 运行`sqlite3 Chinook.db`
- 运行`.read Chinook_Sqlite.sql`
- 测试`SELECT * FROM Artist LIMIT 10;`

现在，`Chinhook.db`在我们的目录中，我们可以使用基于SQLAlchemy的`SQLDatabase`类与它进行接口交互：


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



## 代理

我们将使用OpenAI聊天模型和一个`"openai-tools"`代理，它将使用OpenAI的函数调用API来驱动代理的工具选择和调用。

正如我们可以看到的那样，代理首先会选择哪些表是相关的，然后将这些表的模式和一些示例行添加到提示中。


```python
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
```


```python
agent_executor.invoke(
    "列出每个国家的总销售额。哪个国家的客户花费最多？"
)
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m
    调用: ‘sql_db_list_tables’，参数: ‘{}’
    
    
    [0m[38;5;200m[1;3mAlbum，Artist，Customer，Employee，Genre，Invoice，InvoiceLine，MediaType，Playlist，PlaylistTrack，Track[0m[32;1m[1;3m
    调用: ‘sql_db_schema’，参数: ‘Invoice，Customer’
    
    
    [0m[33;1m[1;3m
    CREATE TABLE “Customer” (
      “CustomerId” INTEGER NOT NULL, 
      “FirstName” NVARCHAR(40) NOT NULL, 
      “LastName” NVARCHAR(20) NOT NULL, 
      “Company” NVARCHAR(80), 
      “Address” NVARCHAR(70), 
      “City” NVARCHAR(40), 
      “State” NVARCHAR(40), 
      “Country” NVARCHAR(40), 
      “PostalCode” NVARCHAR(10), 
      “Phone” NVARCHAR(24), 
      “Fax” NVARCHAR(24), 
      “Email” NVARCHAR(60) NOT NULL, 
      “SupportRepId” INTEGER, 
      PRIMARY KEY (“CustomerId”), 
      FOREIGN KEY(“SupportRepId”) REFERENCES “Employee” (“EmployeeId”)
    )
    
    /*
    Customer表中的3行：
    CustomerId	FirstName	LastName	Company	Address	City	State	Country	PostalCode	Phone	Fax	Email	SupportRepId
    1	LuÃ­s	GonÃ§alves	Embraer - Empresa Brasileira de AeronÃ¡utica S.A.	Av. Brigadeiro Faria Lima, 2170	SÃ£o JosÃ© dos Campos	SP	Brazil	12227-000	+55 (12) 3923-5555	+55 (12) 3923-5566	luisg@embraer.com.br	3
    2	Leonie	KÃ¶hler	None	Theodor-Heuss-StraÃŸe 34	Stuttgart	None	Germany	70174	+49 0711 2842222	None	leonekohler@surfeu.de	5
    3	FranÃ§ois	Tremblay	None	1498 rue BÃ©langer	MontrÃ©al	QC	Canada	H2G 1A7	+1 (514) 721-4711	None	ftremblay@gmail.com	3
    */
    
    
    CREATE TABLE “Invoice” (
      “InvoiceId” INTEGER NOT NULL, 
      “CustomerId” INTEGER NOT NULL, 
      “InvoiceDate” DATETIME NOT NULL, 
      “BillingAddress” NVARCHAR(70), 
      “BillingCity” NVARCHAR(40), 
      “BillingState” NVARCHAR(40), 
      “BillingCountry” NVARCHAR(40), 
      “BillingPostalCode” NVARCHAR(10), 
      “Total” NUMERIC(10, 2) NOT NULL, 
      PRIMARY KEY (“InvoiceId”), 
      FOREIGN KEY(“CustomerId”) REFERENCES “Customer” (“CustomerId”)
    )
    
    /*
    Invoice表中的3行：
    InvoiceId	CustomerId	InvoiceDate	BillingAddress	BillingCity	BillingState	BillingCountry	BillingPostalCode	Total
    1	2	2009-01-01 00:00:00	Theodor-Heuss-StraÃŸe 34	Stuttgart	None	Germany	70174	1.98
    2	4	2009-01-02 00:00:00	UllevÃ¥lsveien 14	Oslo	None	Norway	0171	3.96
    3	8	2009-01-03 00:00:00	GrÃ©trystraat 63	Brussels	None	Belgium	1000	5.94
    */[0m[32;1m[1;3m
    调用: ‘sql_db_query’，参数: ‘SELECT c.Country, SUM(i.Total) AS TotalSales FROM Invoice i JOIN Customer c ON i.CustomerId = c.CustomerId GROUP BY c.Country ORDER BY TotalSales DESC LIMIT 10;’
    响应: 要列出每个国家的总销售额，我可以查询“Invoice”和“Customer”表。我将在“CustomerId”列上加入这些表，并根据“BillingCountry”列对结果进行分组。然后，我将计算“Total”列的总和以获得每个国家的总销售额。最后，我将按总销售额的降序对结果进行排序。
    
    这是SQL查询：
    
    ```sql
    SELECT c.Country, SUM(i.Total) AS TotalSales
    FROM Invoice i
    JOIN Customer c ON i.CustomerId = c.CustomerId
    GROUP BY c.Country
    ORDER BY TotalSales DESC
    LIMIT 10;
    ```
    
    现在，我将执行此查询以获取每个国家的总销售额。
    
    [0m[36;1m[1;3m[('USA', 523.0600000000003), ('Canada', 303.9599999999999), ('France', 195.09999999999994), ('Brazil', 190.09999999999997), ('Germany', 156.48), ('United Kingdom', 112.85999999999999), ('Czech Republic', 90.24000000000001), ('Portugal', 77.23999999999998), ('India', 75.25999999999999), ('Chile', 46.62)][0m[32;1m[1;3m每个国家的总销售额如下：
    
    1. 美国：523.06美元
    2. 加拿大：303.96美元
    3. 法国：195.10美元
    4. 巴西：190.10美元
    5. 德国：156.48美元
    6. 英国：112.86美元
    7. 捷克共和国：90.24美元
    8. 葡萄牙：77.24美元
    9. 印度：75.26美元
    10. 智利：46.62美元
    
    要回答第二个问题，花费最多的国家是美国，总销售额为523.06美元。[0m
    
    [1m> 完成链。[0m
    




    {'input': '列出每个国家的总销售额。哪个国家的客户花费最多？',
     'output': '每个国家的总销售额如下：\n\n1. 美国：523.06美元\n2. 加拿大：303.96美元\n3. 法国：195.10美元\n4. 巴西：190.10美元\n5. 德国：156.48美元\n6. 英国：112.86美元\n7. 捷克共和国：90.24美元\n8. 葡萄牙：77.24美元\n9. 印度：75.26美元\n10. 智利：46.62美元\n\n要回答第二个问题，花费最多的国家是美国，总销售额为523.06美元。'}




```python
agent_executor.invoke("描述playlisttrack表")
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m
    调用: ‘sql_db_list_tables’，参数: ‘{}’
    
    
    [0m[38;5;200m[1;3mAlbum，Artist，Customer，Employee，Genre，Invoice，InvoiceLine，MediaType，Playlist，PlaylistTrack，Track[0m[32;1m[1;3m
    调用: ‘sql_db_schema’，参数: ‘PlaylistTrack’
    
    
    [0m[33;1m[1;3m
    CREATE TABLE “PlaylistTrack” (
      “PlaylistId” INTEGER NOT NULL, 
      “TrackId” INTEGER NOT NULL, 
      PRIMARY KEY (“PlaylistId”, “TrackId”), 
      FOREIGN KEY(“TrackId”) REFERENCES “Track” (“TrackId”), 
      FOREIGN KEY(“PlaylistId”) REFERENCES “Playlist” (“PlaylistId”)
    )
    
    /*
    PlaylistTrack表中的3行：
    PlaylistId	TrackId
    1	3402
    1	3389
    1	3390
    */[0m[32;1m[1;3m“PlaylistTrack”表有两列：“PlaylistId”和“TrackId”。它是一个表示播放列表和曲目之间多对多关系的联接表。 
    
    这是“PlaylistTrack”表的模式：
    
    ```
    CREATE TABLE “PlaylistTrack” (
      “PlaylistId” INTEGER NOT NULL, 
      “TrackId” INTEGER NOT NULL, 
      PRIMARY KEY (“PlaylistId”, “TrackId”), 
      FOREIGN KEY(“TrackId”) REFERENCES “Track” (“TrackId”), 
      FOREIGN KEY(“PlaylistId”) REFERENCES “Playlist” (“PlaylistId”)
    )
    ```
    
    “PlaylistId”列是一个外键，引用“Playlist”表中的“PlaylistId”列。“TrackId”列是一个外键，引用“Track”表中的“TrackId”列。
    
    这是来自“PlaylistTrack”表的三个示例行：
    
    ```
    PlaylistId   TrackId
    1            3402
    1            3389
    1            3390
    ```
    
    如果还有其他问题，请告诉我，我可以提供帮助。[0m
    
    [1m> 完成链。[0m
    




    {'input': '描述playlisttrack表',
     'output': '“PlaylistTrack”表有两列：“PlaylistId”和“TrackId”。它是一个表示播放列表和曲目之间多对多关系的联接表。 \n\n这是“PlaylistTrack”表的模式：\n\n```\nCREATE TABLE “PlaylistTrack” (\n  “PlaylistId” INTEGER NOT NULL, \n  “TrackId” INTEGER NOT NULL, \n  PRIMARY KEY (“PlaylistId”, “TrackId”), \n  FOREIGN KEY(“TrackId”) REFERENCES “Track” (“TrackId”), \n  FOREIGN KEY(“PlaylistId”) REFERENCES “Playlist” (“PlaylistId”)\n)\n```\n\n“PlaylistId”列是一个外键，引用“Playlist”表中的“PlaylistId”列。“TrackId”列是一个外键，引用“Track”表中的“TrackId”列。\n\n这是来自“PlaylistTrack”表的三个示例行：\n\n```\nPlaylistId   TrackId\n1            3402\n1            3389\n1            3390\n```\n\n如果还有其他问题，请告诉我，我可以提供帮助。'}



## 使用动态few-shot提示

为了优化代理性能，我们可以提供一个具有特定领域知识的自定义提示。在这种情况下，我们将创建一个few shot提示，其中包含一个示例选择器，该选择器将根据用户输入动态构建few shot提示。这将帮助模型通过在提示中插入相关查询来更好地进行查询，模型可以将其用作参考。

首先，我们需要一些用户输入<> SQL查询示例:


```python
examples = [
    {"input": "List all artists.", "query": "SELECT * FROM Artist;"},
    {
        "input": "Find all albums for the artist 'AC/DC'.",
        "query": "SELECT * FROM Album WHERE ArtistId = (SELECT ArtistId FROM Artist WHERE Name = 'AC/DC');",
    },
    {
        "input": "List all tracks in the 'Rock' genre.",
        "query": "SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock');",
    },
    {
        "input": "Find the total duration of all tracks.",
        "query": "SELECT SUM(Milliseconds) FROM Track;",
    },
    {
        "input": "List all customers from Canada.",
        "query": "SELECT * FROM Customer WHERE Country = 'Canada';",
    },
    {
        "input": "How many tracks are there in the album with ID 5?",
        "query": "SELECT COUNT(*) FROM Track WHERE AlbumId = 5;",
    },
    {
        "input": "Find the total number of invoices.",
        "query": "SELECT COUNT(*) FROM Invoice;",
    },
    {
        "input": "List all tracks that are longer than 5 minutes.",
        "query": "SELECT * FROM Track WHERE Milliseconds > 300000;",
    },
    {
        "input": "Who are the top 5 customers by total purchase?",
        "query": "SELECT CustomerId, SUM(Total) AS TotalPurchase FROM Invoice GROUP BY CustomerId ORDER BY TotalPurchase DESC LIMIT 5;",
    },
    {
        "input": "Which albums are from the year 2000?",
        "query": "SELECT * FROM Album WHERE strftime('%Y', ReleaseDate) = '2000';",
    },
    {
        "input": "How many employees are there",
        "query": 'SELECT COUNT(*) FROM "Employee"',
    },
]
```

现在我们可以创建一个示例选择器。这将获取实际用户输入并选择一些示例添加到我们的few-shot提示中。我们将使用SemanticSimilarityExampleSelector，它将使用我们配置的嵌入和向量存储执行语义搜索，以找到与我们的输入最相似的示例:


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

现在我们可以创建我们的FewShotPromptTemplate，它接受我们的示例选择器，用于格式化每个示例的示例提示，以及用于放置在我们格式化的示例之前和之后的字符串前缀和后缀:


```python
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotPromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
    SystemMessagePromptTemplate,
)

system_prefix = """You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the given tools. Only use the information returned by the tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

If the question does not seem related to the database, just return "I don't know" as the answer.

Here are some examples of user inputs and their corresponding SQL queries:"""

few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=PromptTemplate.from_template(
        "User input: {input}\nSQL query: {query}"
    ),
    input_variables=["input", "dialect", "top_k"],
    prefix=system_prefix,
    suffix="",
)
```

由于我们底层的代理是一个[OpenAI工具代理](/modules/agents/agent_types/openai_tools)，它使用OpenAI函数调用，所以我们完整的提示应该是一个带有人类消息模板和一个agent_scratchpad `MessagesPlaceholder`的聊天提示。few-shot提示将用于我们的系统消息:


```python
full_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate(prompt=few_shot_prompt),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)
```


```python
# 示例格式化的提示
prompt_val = full_prompt.invoke(
    {
        "input": "How many arists are there",
        "top_k": 5,
        "dialect": "SQLite",
        "agent_scratchpad": [],
    }
)
print(prompt_val.to_string())
```

    System: You are an agent designed to interact with a SQL database.
    Given an input question, create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
    Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
    You can order the results by a relevant column to return the most interesting examples in the database.
    Never query for all the columns from a specific table, only ask for the relevant columns given the question.
    You have access to tools for interacting with the database.
    Only use the given tools. Only use the information returned by the tools to construct your final answer.
    You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.
    
    DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
    
    If the question does not seem related to the database, just return "I don't know" as the answer.
    
    Here are some examples of user inputs and their corresponding SQL queries:
    
    User input: List all artists.
    SQL query: SELECT * FROM Artist;
    
    User input: How many employees are there
    SQL query: SELECT COUNT(*) FROM "Employee"
    
    User input: How many tracks are there in the album with ID 5?
    SQL query: SELECT COUNT(*) FROM Track WHERE AlbumId = 5;
    
    User input: List all tracks in the 'Rock' genre.
    SQL query: SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock');
    
    User input: Which albums are from the year 2000?
    SQL query: SELECT * FROM Album WHERE strftime('%Y', ReleaseDate) = '2000';
    Human: How many arists are there
    

现在我们可以使用自定义提示创建代理:


```python
agent = create_sql_agent(
    llm=llm,
    db=db,
    prompt=full_prompt,
    verbose=True,
    agent_type="openai-tools",
)
```

让我们试试看:


```python
agent.invoke({"input": "How many artists are there?"})
```

    
    
    [1m> Entering new AgentExecutor chain...[0m
    [32;1m[1;3m
    调用: `sql_db_query`，参数为 `{'query': 'SELECT COUNT(*) FROM Artist'}`。
    
    
    [0m[36;1m[1;3m[(275,)][0m[32;1m[1;3m数据库中有275位艺术家。[0m
    
    [1m> Finished chain.[0m
    




    {'input': 'How many artists are there?',
     'output': '数据库中有275位艺术家。'}## 处理高基数列

为了筛选包含专有名词（如地址、歌曲名称或艺术家）的列，我们首先需要仔细检查拼写，以便正确地筛选数据。

我们可以通过创建一个包含数据库中存在的所有不同专有名词的向量存储器来实现这一点。然后，每当用户在问题中包含一个专有名词时，我们可以让代理查询该向量存储器，以找到该单词的正确拼写。通过这种方式，代理可以确保在构建目标查询之前了解用户所指的实体。

首先，我们需要为我们想要的每个实体获取唯一值，我们定义一个将结果解析为元素列表的函数：


```python
import ast
import re


def query_as_list(db, query):
    res = db.run(query)
    res = [el for sub in ast.literal_eval(res) for el in sub if el]
    res = [re.sub(r"\b\d+\b", "", string).strip() for string in res]
    return list(set(res))


artists = query_as_list(db, "SELECT Name FROM Artist")
albums = query_as_list(db, "SELECT Title FROM Album")
albums[:5]
```




    ['Os Cães Ladram Mas A Caravana Não Pára',
     'War',
     'Mais Do Mesmo',
     "Up An' Atom",
     'Riot Act']



现在我们可以继续创建自定义的**检索工具**和最终代理：


```python
from langchain.agents.agent_toolkits import create_retriever_tool

vector_db = FAISS.from_texts(artists + albums, OpenAIEmbeddings())
retriever = vector_db.as_retriever(search_kwargs={"k": 5})
description = """用于查找要筛选值的工具。输入是对专有名词的近似拼写，输出是有效的专有名词。使用与搜索最相似的名词。"""
retriever_tool = create_retriever_tool(
    retriever,
    name="search_proper_nouns",
    description=description,
)
```


```python
system = """你是一个与SQL数据库交互的代理。
给定一个输入问题，创建一个语法正确的{dialect}查询来运行，然后查看查询结果并返回答案。
除非用户指定了他们希望获得的具体示例数，否则每次限制查询至多{top_k}个结果。
您可以通过对相关列进行排序，返回数据库中最有趣的示例。
不要查询特定表的所有列，只需根据问题要求的相关列查询。
您可以使用与数据库交互的工具。
只使用给定的工具。只使用工具返回的信息来构建最终答案。
在执行查询之前，必须仔细检查查询。如果在执行查询时出现错误，请重新编写查询并重试。

不要对数据库进行任何DML语句（INSERT、UPDATE、DELETE、DROP等）。

如果您需要对专有名词进行筛选，则必须始终使用“search_proper_nouns”工具查找筛选值！

您可以访问以下表格：{table_names}

如果问题似乎与数据库无关，请只返回“我不知道”作为答案。"""

prompt = ChatPromptTemplate.from_messages(
    [("system", system), ("human", "{input}"), MessagesPlaceholder("agent_scratchpad")]
)
agent = create_sql_agent(
    llm=llm,
    db=db,
    extra_tools=[retriever_tool],
    prompt=prompt,
    agent_type="openai-tools",
    verbose=True,
)
```


```python
agent.invoke({"input": "alis in chain有多少张专辑？"})
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m
    调用: `search_proper_nouns`，参数为 `{'query': 'alis in chain'}` 
    
    
    [0m[36;1m[1;3mAlice In Chains
    
    Aisha Duo
    
    Xis
    
    Da Lama Ao Caos
    
    A-Sides[0m[32;1m[1;3m
    调用: `sql_db_query`，参数为 `SELECT COUNT(*) FROM Album WHERE ArtistId = (SELECT ArtistId FROM Artist WHERE Name = 'Alice In Chains')` 
    
    
    [0m[36;1m[1;3m[(1,)][0m[32;1m[1;3mAlice In Chains有1张专辑。[0m
    
    [1m> 完成链。[0m
    




    {'input': 'alis in chain有多少张专辑？',
     'output': 'Alice In Chains有1张专辑。'}



正如我们所见，代理使用了`search_proper_nouns`工具来检查如何正确查询数据库以获取该特定艺术家的信息。

## 下一步

在幕后，`create_sql_agent`只是将SQL工具传递给更通用的代理构造函数。要了解有关内置的通用代理类型以及如何构建自定义代理的更多信息，请前往[代理模块](/modules/agents/)。

内置的`AgentExecutor`运行简单的代理操作->工具调用->代理操作...循环。要构建更复杂的代理运行时，请转到[LangGraph部分](/docs/langgraph)。## Agents

当我们知道任何用户输入所需的特定工具使用顺序时，链式工具非常有用。但对于某些用例来说，我们使用工具的次数取决于输入。在这些情况下，我们希望让模型自己决定使用工具的次数和顺序。[Agents](/modules/agents/)正是这样做的。

LangChain提供了许多内置的Agent，针对不同的使用情况进行了优化。在这里阅读有关[agent类型的所有信息](/modules/agents/agent_types/)。

例如，让我们尝试使用OpenAI Tools Agent，它利用了新的OpenAI调用工具的API（这仅适用于最新的OpenAI模型，并且不同于函数调用，因为模型可以一次返回多个函数调用）。

![agent](/img//tool_agent.svg)

## 设置

我们需要安装以下软件包：

```python
%pip install --upgrade --quiet langchain langchain-openai
```

并设置以下环境变量：

```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 如果想使用LangSmith，请取消下面的注释
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 创建工具

首先，我们需要创建一些要调用的工具。对于这个示例，我们将从函数创建自定义工具。有关创建自定义工具的更多信息，请参阅[此指南](/modules/tools/)。

```python
from langchain_core.tools import tool


@tool
def multiply(first_int: int, second_int: int) -> int:
    """Multiply two integers together."""
    return first_int * second_int


@tool
def add(first_int: int, second_int: int) -> int:
    "Add two integers."
    return first_int + second_int


@tool
def exponentiate(base: int, exponent: int) -> int:
    "Exponentiate the base to the exponent power."
    return base**exponent


tools = [multiply, add, exponentiate]
```

## 创建提示

```python
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI
```

```python
# 获取要使用的提示 - 您可以修改此内容！
prompt = hub.pull("hwchase17/openai-tools-agent")
prompt.pretty_print()
```
## 创建Agent

```python
# 选择将驱动该Agent的LLM
# 只有某些模型支持此功能
model = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)

# 构建OpenAI Tools agent
agent = create_openai_tools_agent(model, tools, prompt)
```

```python
# 通过传入agent和tools来创建agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

## 调用Agent

```python
agent_executor.invoke(
    {
        "input": "Take 3 to the fifth power and multiply that by the sum of twelve and three, then square the whole result"
    }
)
```

```

[1m> 进入新的AgentExecutor链...[0m
[32;1m[1;3m
调用：`exponentiate`，参数为`{'base': 3, 'exponent': 5}`

[0m[38;5;200m[1;3m243[0m[32;1m[1;3m
调用：`add`，参数为`{'first_int': 12, 'second_int': 3}`

[0m[33;1m[1;3m15[0m[32;1m[1;3m
调用：`multiply`，参数为`{'first_int': 243, 'second_int': 15}`

[0m[36;1m[1;3m3645[0m[32;1m[1;3m
调用：`exponentiate`，参数为`{'base': 3645, 'exponent': 2}`

[0m[38;5;200m[1;3m13286025[0m[32;1m[1;3m将3的五次方乘以十二和三的和，然后平方整个结果的结果是13,286,025。[0m

[1m> 完成链。[0m
```

```
{'input': 'Take 3 to the fifth power and multiply that by the sum of twelve and three, then square the whole result',
 'output': 'The result of raising 3 to the fifth power and multiplying that by the sum of twelve and three, then squaring the whole result is 13,286,025.'}
```

