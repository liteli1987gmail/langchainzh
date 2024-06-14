# OpenAI助手

> [助手API](https://platform.openai.com/docs/assistants/overview)允许您在自己的应用程序中构建AI助手。助手具有说明并可以利用模型、工具和知识来回答用户查询。助手API当前支持三种类型的工具：代码解释器、检索和功能调用。

您可以使用OpenAI工具或自定义工具与OpenAI助手进行交互。当仅使用OpenAI工具时，您可以直接调用助手并获得最终答案。当使用自定义工具时，您可以使用内置的AgentExecutor运行助手和工具执行循环，或者轻松地编写您自己的执行程序。

以下是与助手交互的不同方式。作为一个简单的例子，让我们构建一个数学辅导员，可以编写和运行代码。

### 仅使用OpenAI工具


```python
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
```


```python
interpreter_assistant = OpenAIAssistantRunnable.create_assistant(
    name="langchain assistant",
    instructions="您是一位个人数学辅导员。编写和运行代码来回答数学问题。",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview",
)
output = interpreter_assistant.invoke({"content": "10 - 4的2.7次方是多少"})
output
```




    [ThreadMessage(id='msg_qgxkD5kvkZyl0qOaL4czPFkZ', assistant_id='asst_0T8S7CJuUa4Y4hm1PF6n62v7', content=[MessageContentText(text=Text(annotations=[], value='计算\\(10 - 4^{2.7}\\)的结果约为\\(-32.224\\)。'), type='text')], created_at=1700169519, file_ids=[], metadata={}, object='thread.message', role='assistant', run_id='run_aH3ZgSWNk3vYIBQm3vpE8tr4', thread_id='thread_9K6cYfx1RBh0pOWD8SxwVWW9')]



### 作为LangChain代理使用任意工具

现在让我们使用自己的工具重新创建此功能。在这个例子中，我们将使用[E2B sandbox runtime工具](https://e2b.dev/docs?ref=landing-page-get-started)。


```python
%pip install --upgrade --quiet  e2b duckduckgo-search
```


```python
import getpass

from langchain_community.tools import DuckDuckGoSearchRun, E2BDataAnalysisTool

tools = [E2BDataAnalysisTool(api_key=getpass.getpass()), DuckDuckGoSearchRun()]
```


```python
agent = OpenAIAssistantRunnable.create_assistant(
    name="langchain assistant e2b tool",
    instructions="您是一位个人数学辅导员。编写和运行代码来回答数学问题。您还可以搜索互联网。",
    tools=tools,
    model="gpt-4-1106-preview",
    as_agent=True,
)
```

#### 使用AgentExecutor

OpenAIAssistantRunnable兼容AgentExecutor，因此我们可以直接将其作为一个代理传递给执行程序。AgentExecutor负责调用所调用的工具并将工具输出上传到Assistants API。此外，它还附带内置的LangSmith跟踪。


```python
from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools)
agent_executor.invoke({"content": "旧金山今天的天气除以2.7"})
```




    {'content': '旧金山今天的天气除以2.7',
     'output': '搜索结果显示，旧金山的天气为67°F。现在我将这个温度除以2.7并为您提供结果。请注意，这是一个数学运算，不代表一个有意义的物理量。\n\n我们计算一下67°F除以2.7。\n当前旧金山的温度为67°F，除以2.7的结果约为24.815。',
     'thread_id': 'thread_hcpYI0tfpB9mHa9d95W7nK2B',
     'run_id': 'run_qOuVmPXS9xlV3XNPcfP8P9W2'}



:::⚠⚠⚠



[LangSmith跟踪](https://smith.langchain.com/public/6750972b-0849-4beb-a8bb-353d424ffade/r)

:::

#### 自定义执行

或者使用LCEL，我们可以轻松编写自己的执行循环来运行助手。这样我们就完全控制了执行过程。


```python
agent = OpenAIAssistantRunnable.create_assistant(
    name="langchain assistant e2b tool",
    instructions="您是一位个人数学辅导员。编写和运行代码来回答数学问题。",
    tools=tools,
    model="gpt-4-1106-preview",
    as_agent=True,
)
```


```python
from langchain_core.agents import AgentFinish


def execute_agent(agent, tools, input):
    tool_map = {tool.name: tool for tool in tools}
    response = agent.invoke(input)
    while not isinstance(response, AgentFinish):
        tool_outputs = []
        for action in response:
            tool_output = tool_map[action.tool].invoke(action.tool_input)
            print(action.tool, action.tool_input, tool_output, end="\n\n")
            tool_outputs.append(
                {"output": tool_output, "tool_call_id": action.tool_call_id}
            )
        response = agent.invoke(
            {
                "tool_outputs": tool_outputs,
                "run_id": action.run_id,
                "thread_id": action.thread_id,
            }
        )

    return response
```


```python
response = execute_agent(agent, tools, {"content": "10 - 4的2.7次方是多少"})
print(response.return_values["output"])
```

    e2b_data_analysis {'python_code': 'result = 10 - 4 ** 2.7\nprint(result)'} {"stdout": "-32.22425314473263", "stderr": "", "artifacts": []}
    
    \( 10 - 4^{2.7} \) 约为 -32.224。
    

## 使用现有线程

要使用现有线程，我们只需要在调用代理时传递“thread_id”即可。


```python
next_response = execute_agent(
    agent,
    tools,
    {"content": "现在加上17.241", "thread_id": response.return_values["thread_id"]},
)
print(next_response.return_values["output"])
```

    e2b_data_analysis {'python_code': 'result = 10 - 4 ** 2.7 + 17.241\nprint(result)'} {"stdout": "-14.983253144732629", "stderr": "", "artifacts": []}
    
    \( 10 - 4^{2.7} + 17.241 \) 约为 -14.983。
    

## 使用现有助手

要使用现有助手，我们可以直接使用`OpenAIAssistantRunnable`初始化，并将`assistant_id`传递给它。


```python
agent = OpenAIAssistantRunnable(assistant_id="<ASSISTANT_ID>", as_agent=True)
```