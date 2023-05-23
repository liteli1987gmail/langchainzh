
Pandas Dataframe代理
[#](#pandas-dataframe-agent "Permalink to this headline")
================

本教程演示如何使用代理与pandas数据框交互。主要优化问答。

**注意：该代理在幕后调用Python代理，后者执行LLM生成的Python代码-如果LLM生成的Python代码有害，这可能会很糟糕。请谨慎使用。**

```  python
from langchain.agents import create_pandas_dataframe_agent
```


```  python
from langchain.llms import OpenAI
import pandas as pd

df = pd.read_csv('titanic.csv')
```


```  python
agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)
```


```  python
agent.run("how many rows are there?")
```


```  python
> Entering new AgentExecutor chain...
Thought: I need to count the number of rows
Action: python_repl_ast
Action Input: len(df)
Observation: 891
Thought: I now know the final answer
Final Answer: There are 891 rows in the dataframe.

> Finished chain.
```


```  python
'There are 891 rows in the dataframe.'
```


```  python
agent.run("how many people have more than 3 siblings")
```


```  python
> Entering new AgentExecutor chain...
Thought: I need to count the number of people with more than 3 siblings
Action: python_repl_ast
Action Input: df[df['SibSp'] > 3].shape[0]
Observation: 30
Thought: I now know the final answer
Final Answer: 30 people have more than 3 siblings.

> Finished chain.
```


```  python
'30 people have more than 3 siblings.'
```


```  python
agent.run("whats the square root of the average age?")
```


```  python
> Entering new AgentExecutor chain...
Thought: I need to calculate the average age first
Action: python_repl_ast
Action Input: df['Age'].mean()
Observation: 29.69911764705882
Thought: I can now calculate the square root
Action: python_repl_ast
Action Input: math.sqrt(df['Age'].mean())
Observation: name 'math' is not defined
Thought: I need to import the math library
Action: python_repl_ast
Action Input: import math
Observation: None
Thought: I can now calculate the square root
Action: python_repl_ast
Action Input: math.sqrt(df['Age'].mean())
Observation: 5.449689683556195
Thought: I now know the final answer
Final Answer: 5.449689683556195

> Finished chain.
```


```  python
'5.449689683556195'
```


