

# 如何访问中间步骤[#](#how-to-access-intermediate-steps "Permalink to this headline")

为了更好地了解代理正在做什么，我们还可以返回中间步骤。

这以返回值中的额外键的形式呈现，它是一个(action, observation)元组的列表。
``` python
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
```

初始化代理所需的组件。

``` python
llm = OpenAI(temperature=0, model_name='text-davinci-002')
tools = load_tools(["serpapi", "llm-math"], llm=llm)
```

使用"return_intermediate_steps=True"初始化代理。

``` python
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, return_intermediate_steps=True)
```

``` python
response = agent({"input":"Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"})

```

``` python
> Entering new AgentExecutor chain...
 I should look up who Leo DiCaprio is dating
Action: Search
Action Input: "Leo DiCaprio girlfriend"
Observation: Camila Morrone
Thought: I should look up how old Camila Morrone is
Action: Search
Action Input: "Camila Morrone age"
Observation: 25 years
Thought: I should calculate what 25 years raised to the 0.43 power is
Action: Calculator
Action Input: 25^0.43
Observation: Answer: 3.991298452658078

Thought: I now know the final answer
Final Answer: Camila Morrone is Leo DiCaprio's girlfriend and she is 3.991298452658078 years old.

> Finished chain.

```

``` python
# The actual return type is a NamedTuple for the agent action, and then an observation
print(response["intermediate_steps"])

```

``` python
[(AgentAction(tool='Search', tool_input='Leo DiCaprio girlfriend', log=' I should look up who Leo DiCaprio is dating\nAction: Search\nAction Input: "Leo DiCaprio girlfriend"'), 'Camila Morrone'), (AgentAction(tool='Search', tool_input='Camila Morrone age', log=' I should look up how old Camila Morrone is\nAction: Search\nAction Input: "Camila Morrone age"'), '25 years'), (AgentAction(tool='Calculator', tool_input='25^0.43', log=' I should calculate what 25 years raised to the 0.43 power is\nAction: Calculator\nAction Input: 25^0.43'), 'Answer: 3.991298452658078\n')]

```

``` python
import json
print(json.dumps(response["intermediate_steps"], indent=2))

```

``` python
[
  [
    [
      "Search",
      "Leo DiCaprio girlfriend",
      " I should look up who Leo DiCaprio is dating\nAction: Search\nAction Input: \"Leo DiCaprio girlfriend\""
    ],
    "Camila Morrone"
  ],
  [
    [
      "Search",
      "Camila Morrone age",
      " I should look up how old Camila Morrone is\nAction: Search\nAction Input: \"Camila Morrone age\""
    ],
    "25 years"
  ],
  [
    [
      "Calculator",
      "25^0.43",
      " I should calculate what 25 years raised to the 0.43 power is\nAction: Calculator\nAction Input: 25^0.43"
    ],
    "Answer: 3.991298452658078\n"
  ]
]

```

