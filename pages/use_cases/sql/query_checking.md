# 查询验证

也许任何SQL链路或代理的最容易出错的部分就是编写有效和安全的SQL查询。在本指南中，我们将介绍一些验证查询和处理无效查询的策略。

## 设置

首先，获取所需的软件包并设置环境变量：


```python
%pip install --upgrade --quiet  langchain langchain-community langchain-openai
```

在本指南中，默认使用OpenAI模型，但您可以根据自己的选择将其替换为所需的模型提供程序。


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 如果使用LangSmith，请取消下面的注释。不是必需的。
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

以下示例将使用带有Chinook数据库的SQLite连接。按照[这些安装步骤](https://database.guide/2-sample-databases-sqlite/)在与此笔记本相同的目录中创建`Chinook.db`：

* 将[此文件](https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql)保存为`Chinook_Sqlite.sql`
* 运行`sqlite3 Chinook.db`
* 运行`.read Chinook_Sqlite.sql`
* 测试`SELECT * FROM Artist LIMIT 10;`

现在，`Chinook.db`位于我们的目录中，我们可以使用基于SQLAlchemy的`SQLDatabase`类与其交互：


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



## 查询检查器

也许最简单的策略是要求模型本身检查原始查询中常见的错误。假设我们有以下SQL查询链：


```python
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = create_sql_query_chain(llm, db)
```

我们想要验证其输出。我们可以通过在链中添加第二个提示和模型调用来实现：


```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

system = """为了检查用户的{dialect}查询中是否存在常见错误，请使用以下方法：
- 当NULL值是使用NOT IN时
- UNION ALL应该替代使用UNION
- 对于排除性范围，请使用BETWEEN
- 在谓词中数据类型不匹配
- 正确引用标识符
- 对于函数，使用正确数量的参数
- 将类型转换为正确的数据类型
- 在联接中使用正确的列名

如果存在上述任何错误，请重新编写查询。如果没有错误，请只复制原始查询。

请仅输出最终的SQL查询。"""
prompt = ChatPromptTemplate.from_messages(
    [("system", system), ("human", "{query}")]
).partial(dialect=db.dialect)
validation_chain = prompt | llm | StrOutputParser()

full_chain = {"query": chain} | validation_chain
```


```python
query = full_chain.invoke(
    {
        "question": "美国顾客中从2003年到2010年之间，因传真缺失计算最平均发票额是多少"
    }
)
query
```




    "SELECT AVG(Invoice.Total) AS AverageInvoice\nFROM Invoice\nJOIN Customer ON Invoice.CustomerId = Customer.CustomerId\nWHERE Customer.Country = 'USA'\nAND Customer.Fax IS NULL\nAND Invoice.InvoiceDate >= '2003-01-01'\nAND Invoice.InvoiceDate < '2010-01-01'"




```python
db.run(query)
```




    '[(6.632999999999998,)]'



这种方法的明显缺点是我们需要进行两次模型调用，而不是一次生成查询。为了解决这个问题，我们可以尝试在单个模型调用中执行查询生成和查询检查：


```python
system = """你是一个{dialect}专家。给定一个问题，创建一个在语法上正确的{dialect}查询来运行。
除非用户在问题中指定了要获取的示例数量，否则最多使用LIMIT子句从{dialect}查询中获取{top_k}个结果。您可以对结果进行排序，以返回数据库中最有信息的数据。
不要从表格中查询所有列。您必须仅查询回答问题所需的列。将每个列名用双引号（"）括起来，以将其表示为分隔符标识符。
请注意，仅使用您在下面的表格中看到的列名。小心不要查询不存在的列。还要注意哪个列在哪个表中。
请注意，如果问题涉及“today”，请使用date('now')函数获取当前日期。

只使用以下表格：
{table_info}

编写查询的初始草稿。然后，双重检查{dialect}查询以查找常见错误，包括：
- 当NULL值是使用NOT IN时
- UNION ALL应该替代使用UNION
- 对于排除性范围，请使用BETWEEN
- 在谓词中数据类型不匹配
- 正确引用标识符
- 对于函数，使用正确数量的参数
- 将类型转换为正确的数据类型
- 在联接中使用正确的列名

使用格式：

初始草稿：<<FIRST_DRAFT_QUERY>>
最终答案：<<FINAL_ANSWER_QUERY>>
"""
prompt = ChatPromptTemplate.from_messages(
    [("system", system), ("human", "{input}")]
).partial(dialect=db.dialect)


def parse_final_answer(output: str) -> str:
    return output.split("最终答案：")[1]


chain = create_sql_query_chain(llm, db, prompt=prompt) | parse_final_answer
prompt.pretty_print()
```

    ================================[1m System Message [0m================================
    
    你是一个[33;1m[1;3m{dialect}[0m专家。给定一个问题，创建一个在语法上正确的[33;1m[1;3m{dialect}[0m查询来运行。
    除非用户在问题中指定了要获取的示例数量，否则最多使用LIMIT子句从[33;1m[1;3m{dialect}[0m查询中获取[33;1m[1;3m{top_k}[0m个结果。您可以对结果进行排序，以返回数据库中最有信息的数据。
    不要从表格中查询所有列。您必须仅查询回答问题所需的列。将每个列名用双引号（"）括起来，以将其表示为分隔符标识符。
    请注意，仅使用您在下面的表格中看到的列名。小心不要查询不存在的列。还要注意哪个列在哪个表中。
    请注意，如果问题涉及“today”，请使用date('now')函数获取当前日期。
    
    只使用以下表格：
    [33;1m[1;3m{table_info}[0m
    
    编写查询的初始草稿。然后，双重检查[33;1m[1;3m{dialect}[0m查询以查找常见错误，包括：
    - 当NULL值是使用NOT IN时
    - UNION ALL应该替代使用UNION
    - 对于排除性范围，请使用BETWEEN
    - 在谓词中数据类型不匹配
    - 正确引用标识符
    - 对于函数，使用正确数量的参数
    - 将类型转换为正确的数据类型
    - 在联接中使用正确的列名
    
    使用格式：
    
    初始草稿：<<FIRST_DRAFT_QUERY>>
    最终答案：<<FINAL_ANSWER_QUERY>>
    
    
    ================================[1m Human Message [0m=================================
    
    [33;1m[1;3m{input}[0m
    


```python
query = chain.invoke(
    {
        "question": "美国顾客中从2003年到2010年之间，因传真缺失计算最平均发票额是多少"
    }
)
query
```




    "\nSELECT AVG(i.Total) AS AverageInvoice\nFROM Invoice i\nJOIN Customer c ON i.CustomerId = c.CustomerId\nWHERE c.Country = 'USA' AND c.Fax IS NULL AND i.InvoiceDate >= date('2003-01-01') AND i.InvoiceDate < date('2010-01-01')"




```python
db.run(query)
```




    '[(6.632999999999998,)]'


------

## 人在循环中

在某些情况下，我们的数据非常敏感，我们不希望在没有人的批准下执行SQL查询。前往[工具使用：人在循环中](/use_cases/tool_use/human_in_the_loop)页面了解如何将人员引入到任何工具、链或代理中。

## 错误处理

在某些时候，模型会出错并生成一个无效的SQL查询，或者我们的数据库出现问题，或者模型API停止运行。我们希望为我们的链条和代理添加一些错误处理行为，以便在这些情况下优雅地失败，甚至可能自动恢复。要了解有关工具错误处理的信息，请前往[工具使用：错误处理](/use_cases/tool_use/tool_error_handling)页面。
