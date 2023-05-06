

鸭子DB[#](#duckdb "此标题的永久链接")
===========================

> 
> [鸭子DB](https://duckdb.org/)是一种进程内SQL OLAP数据库管理系统。
> 
> 
> 

每行一份文档，加载`鸭子DB`查询。

```
#!pip install duckdb

```

```
from langchain.document_loaders import DuckDBLoader

```

```
%%file example.csv
Team,Payroll
Nationals,81.34
Reds,82.20

```

```
Writing example.csv

```

```
loader = DuckDBLoader("SELECT * FROM read_csv_auto('example.csv')")

data = loader.load()

```

```
print(data)

```

```
[Document(page_content='Team: Nationals\nPayroll: 81.34', metadata={}), Document(page_content='Team: Reds\nPayroll: 82.2', metadata={})]

```

指定哪些列是内容而不是元数据[#](#specifying-which-columns-are-content-vs-metadata "此标题的永久链接")
-------------------------------------------------------------------------------

```
loader = DuckDBLoader(
    "SELECT * FROM read_csv_auto('example.csv')",
    page_content_columns=["Team"],
    metadata_columns=["Payroll"]
)

data = loader.load()

```

```
print(data)

```

```
[Document(page_content='Team: Nationals', metadata={'Payroll': 81.34}), Document(page_content='Team: Reds', metadata={'Payroll': 82.2})]

```

将源添加到元数据中[#](#adding-source-to-metadata "此标题的永久链接")
---------------------------------------------------

```
loader = DuckDBLoader(
    "SELECT Team, Payroll, Team As source FROM read_csv_auto('example.csv')",
    metadata_columns=["source"]
)

data = loader.load()

```

```
print(data)

```

```
[Document(page_content='Team: Nationals\nPayroll: 81.34\nsource: Nationals', metadata={'source': 'Nationals'}), Document(page_content='Team: Reds\nPayroll: 82.2\nsource: Reds', metadata={'source': 'Reds'})]

```

