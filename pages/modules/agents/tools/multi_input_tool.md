多输入工具
=========================================================================

本教程展示了如何使用需要多个输入的工具与代理交互。

这样做的困难在于代理根据语言模型决定其下一步，该模型输出一个字符串。因此，如果该步骤需要多个输入，则需要从字符串中解析它们。因此，目前支持的方法是编写一个更小的包装函数，将字符串解析为多个输入。

作为具体示例，我们将使用一个乘法函数，该函数以两个整数作为输入，让代理访问该函数。为了使用它，我们将告诉代理将“操作输入”生成为长度为两个的逗号分隔列表。然后，我们将编写一个薄薄的包装器，将字符串分成两个逗号周围的部分，并将两个解析后的侧作为整数传递给乘法函数。





```
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

```






 Here is the multiplication function, as well as a wrapper to parse a string as input.
 







```
def multiplier(a, b):
    return a \* b

def parsing_multiplier(string):
    a, b = string.split(",")
    return multiplier(int(a), int(b))

```










```
llm = OpenAI(temperature=0)
tools = [
    Tool(
        name = "Multiplier",
        func=parsing_multiplier,
        description="useful for when you need to multiply two numbers together. The input to this tool should be a comma separated list of numbers of length two, representing the two numbers you want to multiply together. For example, `1,2` would be the input if you wanted to multiply 1 by 2."
    )
]
mrkl = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

```










```
mrkl.run("What is 3 times 4")

```








```
> Entering new AgentExecutor chain...
 I need to multiply two numbers
Action: Multiplier
Action Input: 3,4
Observation: 12
Thought: I now know the final answer
Final Answer: 3 times 4 is 12

> Finished chain.

```






```
'3 times 4 is 12'

```








