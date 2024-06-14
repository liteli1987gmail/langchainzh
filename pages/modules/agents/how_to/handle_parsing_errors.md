# 处理解析错误

有时LLM无法确定采取什么步骤，因为其输出格式不正确，无法通过输出解析器处理。在这种情况下，默认情况下代理会出错。但是您可以使用 `handle_parsing_errors` 轻松控制此功能！让我们看看怎么做。

## 设置

我们将使用维基百科工具，因此需要安装它

```python
%pip install --upgrade --quiet  wikipedia
```

```python
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_openai import OpenAI

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
tool = WikipediaQueryRun(api_wrapper=api_wrapper)
tools = [tool]

# 获取要使用的提示 - 您可以修改这个！
# 您可以查看使用的完整提示: https://smith.langchain.com/hub/hwchase17/react
prompt = hub.pull("hwchase17/react")

llm = OpenAI(temperature=0)

agent = create_react_agent(llm, tools, prompt)
```

## 错误

在这种情况下，代理将出错，因为它无法输出一个 Action 字符串（我们已经用恶意输入欺骗了它）

```python
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

```python
agent_executor.invoke(
    {"input": "What is Leo DiCaprio's middle name?\n\nAction: Wikipedia"}
)
```## 默认错误处理

使用`Invalid or incomplete response`处理错误:


```python
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)
```


```python
agent_executor.invoke(
    {"input": "Leo DiCaprio的中间名是什么？\n\n操作: 维基百科"}
)
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m我应该在维基百科上搜索"Leo DiCaprio"
    动作输入：Leo DiCaprio[0mInvalid Format: Missing 'Action:' after 'Thought:[32;1m[1;3m我应该在维基百科上搜索"Leonardo DiCaprio"
    操作: 维基百科
    动作输入：Leonardo DiCaprio[0m[36;1m[1;3m页面：Leonardo DiCaprio
    摘要：Leonardo Wilhelm DiCaprio (; 意大利语：[diˈkaːprjo]；出生于11月1日[0m[32;1m[1;3m我现在知道最终答案
    最终答案：Leonardo Wilhelm[0m
    
    [1m> 完成链。[0m
    




    {'input': "Leo DiCaprio的中间名是什么？\n\n操作: 维基百科",
     'output': 'Leonardo Wilhelm'}



## 自定义错误消息

您可以轻松地自定义出现解析错误时使用的消息。


```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors="检查你的输出并确保其符合规范，使用操作/动作输入语法",
)
```


```python
agent_executor.invoke(
    {"input": "Leo DiCaprio的中间名是什么？\n\n操作: 维基百科"}
)
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m无法解析LLM输出：`我应该在维基百科上搜索"Leo DiCaprio"
    动作输入：Leo DiCaprio`[0m检查你的输出并确保其符合规范，使用操作/动作输入语法[32;1m[1;3m我应该寻找Leo DiCaprio个人生活的部分
    操作: 维基百科
    动作输入：Leo DiCaprio[0m[36;1m[1;3m页面：Leonardo DiCaprio
    摘要：Leonardo Wilhelm DiCaprio (; 意大利语：[diˈkaːprjo]；出生于11月1日[0m[32;1m[1;3m我应该寻找Leo DiCaprio个人生活的部分
    操作: 维基百科
    动作输入：Leonardo DiCaprio[0m[36;1m[1;3m页面：Leonardo DiCaprio
    摘要：Leonardo Wilhelm DiCaprio (; 意大利语：[diˈkaːprjo]；出生于11月1日[0m[32;1m[1;3m我应该寻找Leo DiCaprio个人生活的部分
    操作: 维基百科
    动作输入：Leonardo Wilhelm DiCaprio[0m[36;1m[1;3m页面：Leonardo DiCaprio
    摘要：Leonardo Wilhelm DiCaprio (; 意大利语：[diˈkaːprjo]；出生于11月1日[0m[32;1m[1;3m我应该寻找Leo DiCaprio个人生活的部分
    操作: 维基百科
    动作输入：Leonardo Wilhelm DiCaprio[0m[36;1m[1;3m页面：Leonardo DiCaprio
    摘要：Leonardo Wilhelm DiCaprio (; 意大利语：[diˈkaːprjo]；出生于11月1日[0m[32;1m[1;3m我现在知道最终答案
    最终答案：Leonardo Wilhelm DiCaprio[0m
    
    [1m> 完成链。[0m
    




    {'input': "Leo DiCaprio的中间名是什么？\n\n操作: 维基百科",
     'output': 'Leonardo Wilhelm DiCaprio'}



## 自定义错误函数

您还可以自定义错误处理函数，该函数接受错误并输出一个字符串。


```python
def _handle_error(error) -> str:
    return str(error)[:50]


agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=_handle_error,
)
```


```python
agent_executor.invoke(
    {"input": "Leo DiCaprio的中间名是什么？\n\n操作: 维基百科"}
)
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m无法解析LLM输出：`我应该在维基百科上搜索"Leo DiCaprio"
    动作输入：Leo DiCaprio`[0m无法解析LLM输出：`我应该搜索他的个人生活的部分
    操作: 维基百科
    动作输入：个人生活`[0m[36;1m[1;3m页面：个人生活
    摘要：个人生活是一个人生活的历程或状态，尤其是[0m[32;1m[1;3m我应该搜索他的早期生活的部分
    操作: 维基百科
    动作输入：早期生活[0m

    /Users/harrisonchase/.pyenv/versions/3.10.1/envs/langchain/lib/python3.10/site-packages/wikipedia/wikipedia.py:389: GuessedAtParserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 389 of the file /Users/harrisonchase/.pyenv/versions/3.10.1/envs/langchain/lib/python3.10/site-packages/wikipedia/wikipedia.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.
    
      lis = BeautifulSoup(html).find_all('li')
    

    [36;1m[1;3m未找到好的维基百科搜索结果[0m[32;1m[1;3m我应该尝试搜索"Leonardo DiCaprio"[0m[36;1m[1;3m页面：Leonardo DiCaprio
    摘要：Leonardo Wilhelm DiCaprio (; 意大利语：[diˈкаːprjo]；出生于11月1日[0m[32;1m[1;3m我应该再次搜索他的个人生活部分
    操作: 维基百科
    动作输入：个人生活[0m[36;1m[1;3m页面：个人生活
    摘要：个人生活是一个人生活的历程或状态，尤其是[0m[32;1m[1;3m我现在知道最终答案
    最终答案：Leonardo Wilhelm DiCaprio[0m
    
    [1m> 完成链。[0m
    




    {'input': "Leo DiCaprio的中间名是什么？\n\n操作: 维基百科",
     'output': 'Leonardo Wilhelm DiCaprio'}




```python
