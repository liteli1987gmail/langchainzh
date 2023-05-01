


 CSV Agent
 [#](#csv-agent "Permalink to this headline")
=========================================================



 This notebook shows how to use agents to interact with a csv. It is mostly optimized for question answering.
 



**NOTE: this agent calls the Pandas DataFrame agent under the hood, which in turn calls the Python agent, which executes LLM generated Python code - this can be bad if the LLM generated Python code is harmful. Use cautiously.** 








```
from langchain.agents import create_csv_agent

```










```
from langchain.llms import OpenAI

```










```
agent = create_csv_agent(OpenAI(temperature=0), 'titanic.csv', verbose=True)

```










```
agent.run("how many rows are there?")

```








```
> Entering new AgentExecutor chain...
Thought: I need to count the number of rows
Action: python_repl_ast
Action Input: len(df)
Observation: 891
Thought: I now know the final answer
Final Answer: There are 891 rows in the dataframe.

> Finished chain.

```






```
'There are 891 rows in the dataframe.'

```










```
agent.run("how many people have more than 3 sibligngs")

```








```
> Entering new AgentExecutor chain...
Thought: I need to count the number of people with more than 3 siblings
Action: python_repl_ast
Action Input: df[df['SibSp'] > 3].shape[0]
Observation: 30
Thought: I now know the final answer
Final Answer: 30 people have more than 3 siblings.

> Finished chain.

```






```
'30 people have more than 3 siblings.'

```










```
agent.run("whats the square root of the average age?")

```








```
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
Observation: 
Thought: I can now calculate the square root
Action: python_repl_ast
Action Input: math.sqrt(df['Age'].mean())
Observation: 5.449689683556195
Thought: I now know the final answer
Final Answer: 5.449689683556195

> Finished chain.

```






```
'5.449689683556195'

```







