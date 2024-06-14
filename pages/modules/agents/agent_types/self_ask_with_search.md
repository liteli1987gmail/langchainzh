# 自问自答带搜索

这个演示展示了带搜索代理的自问自答功能。

```python
from langchain import hub
from langchain.agents import AgentExecutor, create_self_ask_with_search_agent
from langchain_community.llms import Fireworks
from langchain_community.tools.tavily_search import TavilyAnswer
```

## 初始化工具

我们将初始化我们想要使用的工具。这是一个很好的工具，因为它给我们提供了**答案**（而不是文档）

对于这个代理，只能使用一个工具，它需要被命名为"Intermediate Answer"。

```python
tools = [TavilyAnswer(max_results=1, name="Intermediate Answer")]
```

## 创建代理

```python
# 获取要使用的提示 - 您可以修改这个提示！
prompt = hub.pull("hwchase17/self-ask-with-search")
```


```python
# 选择将驱动代理的LLM
llm = Fireworks()

# 构建自问自答带搜索代理
agent = create_self_ask_with_search_agent(llm, tools, prompt)
```

## 运行代理

```python
# 通过传入代理和工具来创建一个代理执行器
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```


```python
agent_executor.invoke(
    {"input": "What is the hometown of the reigning men's U.S. Open champion?"}
)
```

    
    
    [1m> 进入新的代理执行器链...[0m
    [32;1m[1;3m是的。
    追问：谁是现任美国网球公开赛男单冠军？[0m[36;1m[1;3m现任美国网球公开赛男单冠军是诺瓦克·德约科维奇。他在2023年美国网球公开赛的决赛中击败丹尼尔·梅德韦杰夫赢得了他的第24个大满贯单打冠军。[0m[32;1m[1;3m
    所以最终答案是：诺瓦克·德约科维奇。[0m
    
    [1m> 完成链条。[0m
    




    {'input': "What is the hometown of the reigning men's U.S. Open champion?",
     'output': 'Novak Djokovic.'}




```python

```