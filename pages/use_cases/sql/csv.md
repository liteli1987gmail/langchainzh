# CSV

大型语言模型（LLMs）非常适合构建各种数据源上的问题-答案系统。在这一部分，我们将介绍如何在存储在CSV文件中的数据上构建问答系统。与使用SQL数据库一样，与CSV文件工作的关键也是让LLM能够使用查询和与数据交互的工具。主要有两种方法：

* **推荐**：将CSV文件加载到SQL数据库中，并使用[SQL用例文档](/use_cases/sql/)中概述的方法。
* 让LLM访问Python环境，在那里它可以使用Pandas等库与数据交互。

## ⚠️ 安全说明 ⚠️

上述两种方法都存在显著风险。使用SQL需要执行模型生成的SQL查询。使用Pandas这样的库需要让模型执行Python代码。由于限制SQL连接权限和清理SQL查询比沙箱化Python环境更容易，**我们强烈推荐通过SQL与CSV数据交互。** 有关一般安全最佳实践的更多信息，请[查看此处](/docs/security)。

## 设置
本指南的依赖项：

```python
%pip install -qU langchain langchain-openai langchain-community langchain-experimental pandas
```

设置所需的环境变量：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# Using LangSmith is recommended but not required. Uncomment below lines to use.
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

Download the [Titanic dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset) if you don't already have it:


```python
!wget https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv -O titanic.csv
```


```python
import pandas as pd

df = pd.read_csv("titanic.csv")
print(df.shape)
print(df.columns.tolist())
```

    (887, 8)
    ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare']
    

## SQL

使用SQL与CSV数据交互是推荐的方法，因为与任意Python代码相比，限制权限和验证SQL查询更加容易。

大多数SQL数据库都可以将CSV文件轻松加载为表格（[DuckDB](https://duckdb.org/docs/data/csv/overview.html)，[SQLite](https://www.sqlite.org/csv.html)，等等）。一旦完成此操作，您可以使用SQL用例指南中概述的所有连锁和产生代理的技术。下面是使用SQLite的快速示例：


```python
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine

engine = create_engine("sqlite:///titanic.db")
df.to_sql("titanic", engine, index=False)
```




    887




```python
db = SQLDatabase(engine=engine)
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM titanic WHERE Age < 2;")
```

    sqlite
    ['titanic']
    




    "[(1, 2, 'Master. Alden Gates Caldwell', 'male', 0.83, 0, 2, 29.0), (0, 3, 'Master. Eino Viljami Panula', 'male', 1.0, 4, 1, 39.6875), (1, 3, 'Miss. Eleanor Ileen Johnson', 'female', 1.0, 1, 1, 11.1333), (1, 2, 'Master. Richard F Becker', 'male', 1.0, 2, 1, 39.0), (1, 1, 'Master. Hudson Trevor Allison', 'male', 0.92, 1, 2, 151.55), (1, 3, 'Miss. Maria Nakid', 'female', 1.0, 0, 2, 15.7417), (0, 3, 'Master. Sidney Leonard Goodwin', 'male', 1.0, 5, 2, 46.9), (1, 3, 'Miss. Helene Barbara Baclini', 'female', 0.75, 2, 1, 19.2583), (1, 3, 'Miss. Eugenie Baclini', 'female', 0.75, 2, 1, 19.2583), (1, 2, 'Master. Viljo Hamalainen', 'male', 0.67, 1, 1, 14.5), (1, 3, 'Master. Bertram Vere Dean', 'male', 1.0, 1, 2, 20.575), (1, 3, 'Master. Assad Alexander Thomas', 'male', 0.42, 0, 1, 8.5167), (1, 2, 'Master. Andre Mallet', 'male', 1.0, 0, 2, 37.0042), (1, 2, 'Master. George Sibley Richards', 'male', 0.83, 1, 1, 18.75)]"



并创建一个[SQL代理](/use_cases/sql/agents)与之交互：


```python
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
```


```python
agent_executor.invoke({"input": "what's the average age of survivors"})
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m
    Invoking: `sql_db_list_tables` with `{}`
    
    
    [0m[38;5;200m[1;3mtitanic[0m[32;1m[1;3m
    Invoking: `sql_db_schema` with `{'table_names': 'titanic'}`
    
    
    [0m[33;1m[1;3m
    CREATE TABLE titanic (
    	"Survived" BIGINT, 
    	"Pclass" BIGINT, 
    	"Name" TEXT, 
    	"Sex" TEXT, 
    	"Age" FLOAT, 
    	"Siblings/Spouses Aboard" BIGINT, 
    	"Parents/Children Aboard" BIGINT, 
    	"Fare" FLOAT
    )
    
    /*
    3 rows from titanic table:
    Survived	Pclass	Name	Sex	Age	Siblings/Spouses Aboard	Parents/Children Aboard	Fare
    0	3	Mr. Owen Harris Braund	male	22.0	1	0	7.25
    1	1	Mrs. John Bradley (Florence Briggs Thayer) Cumings	female	38.0	1	0	71.2833
    1	3	Miss. Laina Heikkinen	female	26.0	0	0	7.925
    */[0m[32;1m[1;3m
    Invoking: `sql_db_query` with `{'query': 'SELECT AVG(Age) AS AverageAge FROM titanic WHERE Survived = 1'}`
    responded: 要找到幸存者的平均年龄，我将查询“titanic”表，并计算“Survived”等于1的行的“Age”列的平均值。
    
     以下是SQL查询语句：
    
    ```sql
    SELECT AVG(Age) AS AverageAge
    FROM titanic
    WHERE Survived = 1
    ```
    
    执行此查询将给出幸存者的平均年龄。
    
    [0m[36;1m[1;3m[(28.408391812865496,)][0m[32;1m[1;3m幸存者的平均年龄约为28.41岁。[0m
    
    [1m> 链结束。[0m
    




    {'input': "what's the average age of survivors",
     'output': '幸存者的平均年龄约为28.41岁。'}



此方法很容易扩展到多个CSV文件，因为我们可以将每个文件加载到我们的数据库作为一个单独的表。详细信息请参阅[SQL指南](/use_cases/sql/)。

## Pandas

除了SQL，我们还可以使用诸如Pandas之类的数据分析库和LLMs的代码生成能力与CSV数据进行交互。同样，**在没有建立充分安全保障的情况下，此方法不适用于生产环境**。因此，我们的代码执行实用程序和构造函数位于`langchain-experimental`包中。

### Chain

大多数LLMs经过足够的训练，可以通过被要求产生它来生成Pandas的Python代码：


```python
ai_msg = llm.invoke(
    "我有一个名为'df'的pandas DataFrame，具有'Age'和'Fare'列。编写代码计算两列之间的相关性。只返回Python代码的Markdown片段，不返回其他任何内容。"
)
print(ai_msg.content)
```

    ```python
    correlation = df['Age'].corr(df['Fare'])
    correlation
    ```
    

我们可以将此功能与Python执行工具结合使用，创建一个简单的数据分析链。首先，我们将希望将CSV表加载为数据帧，并使工具能够访问此数据帧：


```python
import pandas as pd
from langchain_core.prompts import ChatPromptTemplate
from langchain_experimental.tools import PythonAstREPLTool

df = pd.read_csv("titanic.csv")
tool = PythonAstREPLTool(locals={"df": df})
tool.invoke("df['Fare'].mean()")
```




    32.30542018038331



为了帮助强制执行我们的Python工具的正确使用，我们将使用[函数调用](/modules/model_io/chat/function_calling)：


```python
llm_with_tools = llm.bind_tools([tool], tool_choice=tool.name)
llm_with_tools.invoke(
    "我有一个名为'df'的数据帧，想要知道'Age'和'Fare'列之间的相关性"
)
```




    AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_6TZsNaCqOcbP7lqWudosQTd6', 'function': {'arguments': '{\n  "query": "df[[\'Age\', \'Fare\']].corr()"\n}', 'name': 'python_repl_ast'}, 'type': 'function'}]})



我们将添加一个[OpenAI工具输出解析器](/modules/model_io/output_parsers/types/openai_tools)将函数调用提取为字典：


```python
from langchain.output_parsers.openai_tools import JsonOutputKeyToolsParser

parser = JsonOutputKeyToolsParser(tool.name, first_tool_only=True)
(llm_with_tools | parser).invoke(
    "我有一个名为'df'的数据帧，想要知道'Age'和'Fare'列之间的相关性"
)
```




    {'query': "df[['Age', 'Fare']].corr()"}



然后，我们将与一个提示组合，这样我们就可以只指定一个问题，而无需在每次调用时指定数据帧信息：


```python
system = f"""您可以访问一个名为'df'的pandas数据帧。\
这是'df.head().to_markdown()'的输出：

```
{df.head().to_markdown()}
```

给定一个用户问题，编写回答问题的Python代码。\
只返回有效的Python代码，不返回其他任何内容。\
不要假设你可以访问除内置的Python库和pandas之外的任何库。"""
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", "{question}")])
code_chain = prompt | llm_with_tools | parser
code_chain.invoke({"question": "年龄和费用之间的相关性是多少"})
```




    {'query': "df[['Age', 'Fare']].corr()"}



最后，我们将添加我们的Python工具，以便执行生成的代码：


```python
chain = prompt | llm_with_tools | parser | tool  # noqa
chain.invoke({"question": "年龄和费用之间的相关性是多少"})
```




    0.11232863699941621



就这样，我们就有了一个简单的数据分析链。我们可以通过查看LangSmith跟踪来查看中间步骤：https://smith.langchain.com/public/b1309290-7212-49b7-bde2-75b39a32b49a/r

我们可以在最后添加另一个LLM调用来生成对话回复，这样我们不仅仅会用工具的输出来回应。为此，我们将在提示中添加一个聊天历史记录`MessagesPlaceholder`：


```python
from operator import itemgetter

from langchain_core.messages import ToolMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough

system = f"""您可以访问一个名为'df'的pandas数据帧。\
这是'df.head().to_markdown()'的输出：

```
{df.head().to_markdown()}
```

给定一个用户问题，编写回答问题的Python代码。\
不要假设你可以访问除内置的Python库和pandas之外的任何库。\
一旦您有足够的信息来回答问题，请直接回答问题。"""
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            system,
        ),
        ("human", "{question}"),
>>>>>>> fix typo
    ]
)
code_chain = prompt | llm_with_tools | parser | tool  # noqa
chain = code_chain | MessagesPlaceholder()
conversation = [("human", "What's the correlation between age and fare?")]
for index, (role, message) in enumerate(conversation):
    if index == len(conversation) - 1:
        output = chain.invoke({"question": message})
    else:
        output = RunnablePassthrough(role=role, content=message)
    chain = chain | output | StrOutputParser() | itemgetter("output")
    print(f"{role}: {message}")
    print("Bot:", chain.invoke({}))
    print()
```

以上就是使用Pandas进行数据分析的一个简单示例。请注意，执行生成的代码可能存在安全风险，请务必验证和审查生成的代码。


```python
# This MessagesPlaceholder allows us to optionally append an arbitrary number of messages
# at the end of the prompt using the 'chat_history' arg.
MessagesPlaceholder("chat_history", optional=True),
]
)


def _get_chat_history(x: dict) -> list:
"""Parse the chain output up to this point into a list of chat history messages to insert in the prompt."""
ai_msg = x["ai_msg"]
tool_call_id = x["ai_msg"].additional_kwargs["tool_calls"][0]["id"]
tool_msg = ToolMessage(tool_call_id=tool_call_id, content=str(x["tool_output"]))
return [ai_msg, tool_msg]


chain = (
RunnablePassthrough.assign(ai_msg=prompt | llm_with_tools)
.assign(tool_output=itemgetter("ai_msg") | parser | tool)
.assign(chat_history=_get_chat_history)
.assign(response=prompt | llm | StrOutputParser())
.pick(["tool_output", "response"])
)
```


```python
chain.invoke({"question": "What's the correlation between age and fare"})
```




    {'tool_output': 0.11232863699941621,
    'response': 'The correlation between age and fare is approximately 0.112.'}


LangSmith追踪轨迹: [https://smith.langchain.com/public/ca689f8a-5655-4224-8bcf-982080744462/r](https://smith.langchain.com/public/ca689f8a-5655-4224-8bcf-982080744462/r)


### 代理

对于复杂的问题，让LLM能够在保持先前执行的输入和输出的情况下迭代执行代码是非常有帮助的。这就是代理的作用所在。它们允许LLM决定需要调用工具的次数，并跟踪到目前为止的执行情况。[create_pandas_dataframe_agent](https://api.python.langchain.com/en/latest/agents/langchain_experimental.agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent.html) 是一个内置代理，使处理数据框变得容易：


```python
from langchain_experimental.agents import create_pandas_dataframe_agent

agent = create_pandas_dataframe_agent(llm, df, agent_type="openai-tools", verbose=True)
agent.invoke(
{
"input": "What's the correlation between age and fare? is that greater than the correlation between fare and survival?"
}
)
```



[错误] 代理的 agent_type 'openai-tools' 不正确。请提供正确的 agent_type。

LangSmith追踪轨迹: [https://smith.langchain.com/public/8e6c23cc-782c-4203-bac6-2a28c770c9f0/r](https://smith.langchain.com/public/8e6c23cc-782c-4203-bac6-2a28c770c9f0/r)

### 多个 CSV

要处理多个 CSV（或数据框），我们只需将多个数据框传递给我们的 Python 工具。我们的 `create_pandas_dataframe_agent` 构造函数可以开箱即用，我们可以传递一个数据框列表，而不仅仅是一个。如果我们自己构建一个链，可以这样做：

```python
df_1 = df[["Age", "Fare"]]
df_2 = df[["Fare", "Survived"]]

tool = PythonAstREPLTool(locals={"df_1": df_1, "df_2": df_2})
llm_with_tool = llm.bind_tools(tools=[tool], tool_choice=tool.name)
df_template = "```python\n{df_name}.head().to_markdown()\n>>> {df_head}\n```"
df_context = "\n\n".join(
df_template.format(df_head=_df.head().to_markdown(), df_name=df_name)
for _df, df_name in [(df_1, "df_1"), (df_2, "df_2")]
)

system = f"You have access to a number of pandas dataframes. \
Here is a sample of rows from each dataframe and the python code that was used to generate the sample:\n\n{df_context}\n\nGiven a user question about the dataframes, write the Python code to answer it. \
Don't assume you have access to any libraries other than built-in Python ones and pandas. \
Make sure to refer only to the variables mentioned above."
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", "{question}")])

chain = prompt | llm_with_tool | parser | tool
chain.invoke(
{
"question": "return the difference in the correlation between age and fare and the correlation between fare and survival"
}
)
```

-0.14384991262954416

LangSmith追踪轨迹: [https://smith.langchain.com/public/653e499f-179c-4757-8041-f5e2a5f11fcc/r](https://smith.langchain.com/public/653e499f-179c-4757-8041-f5e2a5f11fcc/r)

### 沙盒代码执行

有许多工具如 [E2B](/docs/integrations/tools/e2b_data_analysis) 和 [Bearly](/docs/integrations/tools/bearly) 提供了用于 Python 代码执行的沙盒环境，以允许更安全的代码执行链和代理。

## 下一步

对于更高级的数据分析应用，我们建议查看：

* [SQL 用例](/use_cases/sql/): 处理 SQL 数据库和 CSV 文件的许多挑战对任何结构化数据类型都是通用的，因此即使您使用 Pandas 进行 CSV 数据分析，也有必要阅读 SQL 技术。
* [工具使用](/use_cases/tool_use/): 涉及链和代理调用工具时的一般最佳实践指南。
* [代理](/modules/agents/): 了解构建 LLM 代理的基础知识。
* 集成：沙盒环境如 [E2B](/docs/integrations/tools/e2b_data_analysis) 和 [Bearly](/docs/integrations/tools/bearly)，实用工具如 [SQLDatabase](https://api.python.langchain.com/en/latest/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase)，相关代理如 [Spark DataFrame agent](/docs/integrations/toolkits/spark)。

