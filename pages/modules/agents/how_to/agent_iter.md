# 将Agent作为迭代器运行

有时将Agent作为迭代器运行是很有用的，可以根据需要添加人工审核的检查步骤。

为了演示`AgentExecutorIterator`的功能，我们将设置一个问题，Agent必须执行以下操作：

- 从工具中提取三个素数
- 将它们相乘

在这个简单的问题中，我们可以通过检查中间步骤的输出是否为素数，添加一些逻辑来验证这些步骤。


```python
from langchain.agents import AgentType, initialize_agent
from langchain.chains import LLMMathChain
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
```

```python
%pip install --upgrade --quiet  numexpr
```

```python
# 这里需要使用GPT-4，因为GPT-3.5不理解，无论你如何坚持，它都不会使用计算器执行最后的计算
llm = ChatOpenAI(temperature=0, model="gpt-4")
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
```

定义提供以下功能的工具：

- 提供第`n`个素数（在此示例中使用了较小的子集）
- 作为计算器的`LLMMathChain`

```python
primes = {998: 7901, 999: 7907, 1000: 7919}

class CalculatorInput(BaseModel):
    question: str = Field()

class PrimeInput(BaseModel):
    n: int = Field()

def is_prime(n: int) -> bool:
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_prime(n: int, primes: dict = primes) -> str:
    return str(primes.get(int(n)))

async def aget_prime(n: int, primes: dict = primes) -> str:
    return str(primes.get(int(n)))

tools = [
    Tool(
        name="GetPrime",
        func=get_prime,
        description="用于返回第`n`个素数的工具",
        args_schema=PrimeInput,
        coroutine=aget_prime,
    ),
    Tool.from_function(
        func=llm_math_chain.run,
        name="Calculator",
        description="在需要计算数学表达式时非常有用",
        args_schema=CalculatorInput,
        coroutine=llm_math_chain.arun,
    ),
]
```

构建Agent。这里我们将使用OpenAI Functions agent。

```python
from langchain import hub

# 获取要使用的提示 - 您可以修改此内容！
# 您可以在以下位置查看使用的完整提示：https://smith.langchain.com/hub/hwchase17/openai-functions-agent
prompt = hub.pull("hwchase17/openai-functions-agent")
```

```python
from langchain.agents import create_openai_functions_agent

agent = create_openai_functions_agent(llm, tools, prompt)
```

```python
from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

运行迭代，并对某些步骤执行自定义检查：

```python
question = "第998、999和1000个素数的乘积是多少？"

for step in agent_executor.iter({"input": question}):
    if output := step.get("intermediate_step"):
        action, value = output[0]
        if action.tool == "GetPrime":
            print(f"正在检查 {value} 是否为素数...")
            assert is_prime(int(value))
        # 询问用户是否继续
        _continue = input("是否继续（Y/n）：\n") or "Y"
        if _continue.lower() != "y":
            break
```

```python

```
