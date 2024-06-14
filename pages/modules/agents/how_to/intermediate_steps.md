# 访问中间步骤

为了更好地了解代理正在做什么，我们还可以返回中间步骤。这以额外的键的形式出现在返回值中，这是一个(action, observation)元组的列表。


```python
# pip install wikipedia
```


```python
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
tool = WikipediaQueryRun(api_wrapper=api_wrapper)
tools = [tool]

# 获取要使用的提示 - 您可以修改此内容！
# 如果要查看完整提示，可以在以下网址查看：https://smith.langchain.com/hub/hwchase17/openai-functions-agent
prompt = hub.pull("hwchase17/openai-functions-agent")

llm = ChatOpenAI(temperature=0)

agent = create_openai_functions_agent(llm, tools, prompt)
```

使用`return_intermediate_steps=True`初始化AgentExecutor：


```python
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, return_intermediate_steps=True
)
```


```python
response = agent_executor.invoke({"input": "What is Leo DiCaprio's middle name?"})
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m
    调用：使用`Leo DiCaprio`进行`Wikipedia`查询
    
    
    [0m[36;1m[1;3m页面：Leonardo DiCaprio
    摘要：Leonardo Wilhelm DiCaprio（; 意大利语：[diˈkaːprjo]；生于11月1日[0m[32;1m[1;3mLeonardo DiCaprio的中间名是Wilhelm。[0m
    
    [1m> 链结束。[0m
    


```python
# 实际的返回类型是代理操作的NamedTuple，然后是一个观察结果
print(response["intermediate_steps"])
```

    [(AgentActionMessageLog(tool='Wikipedia', tool_input='Leo DiCaprio', log='\n调用：使用`Leo DiCaprio`进行`Wikipedia`查询\n\n\n', message_log=[AIMessage(content='', additional_kwargs={'function_call': {'name': 'Wikipedia', 'arguments': '{\n  "__arg1": "Leo DiCaprio"\n}'}})]), '页面：Leonardo DiCaprio\n摘要：Leonardo Wilhelm DiCaprio（; 意大利语：[diˈkaːprjo]；生于11月1日')]