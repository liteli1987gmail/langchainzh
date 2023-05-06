Shell工具
============================================================

让代理能够访问shell是一种很强大的方法（在沙箱环境之外有风险）。

LLM可以使用它来执行任何Shell命令。这种情况的常见用例是让LLM与本地文件系统进行交互。

```
from langchain.tools import ShellTool

shell_tool = ShellTool()

```

```
print(shell_tool.run({"commands": ["echo 'Hello World!'", "time"]}))

```

```
Hello World!

real	0m0.000s
user	0m0.000s
sys	0m0.000s

```

```
/Users/wfh/code/lc/lckg/langchain/tools/shell/tool.py:34: UserWarning: The shell tool has no safeguards by default. Use at your own risk.
  warnings.warn(

```

与代理一起使用
-----------------------------------------------------------------

与所有工具一样，可以将其提供给代理以完成更复杂的任务。让代理从网页中获取一些链接。

```
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType

llm = ChatOpenAI(temperature=0)

shell_tool.description = shell_tool.description + f"args {shell_tool.args}".replace("{", "{{").replace("}", "}}")
self_ask_with_search = initialize_agent([shell_tool], llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
self_ask_with_search.run("Download the langchain.com webpage and grep for all urls. Return only a sorted list of them. Be sure to use double quotes.")

```

```
> Entering new AgentExecutor chain...
Question: What is the task?
Thought: We need to download the langchain.com webpage and extract all the URLs from it. Then we need to sort the URLs and return them.
Action:
```

```
{
 "action": "shell",
 "action_input": {
 "commands": [
 "curl -s https://langchain.com | grep -o 'http[s]*://[^\" ]*' | sort"
 ]
 }
}
```



```
/Users/wfh/code/lc/lckg/langchain/tools/shell/tool.py:34: UserWarning: 
The shell tool has no safeguards by default. Use at your own risk.

```

```
Observation: https://blog.langchain.dev/
https://discord.gg/6adMQxSpJS
https://docs.langchain.com/docs/
https://github.com/hwchase17/chat-langchain
https://github.com/hwchase17/langchain
https://github.com/hwchase17/langchainjs
https://github.com/sullivan-sean/chat-langchainjs
https://js.langchain.com/docs/
https://python.langchain.com/en/latest/
https://twitter.com/langchainai

Thought:The URLs have been successfully extracted and sorted. We can return the list of URLs as the final answer.
Final Answer: ["https://blog.langchain.dev/", 
"https://discord.gg/6adMQxSpJS", 
"https://docs.langchain.com/docs/", 
"https://github.com/hwchase17/chat-langchain", 
"https://github.com/hwchase17/langchain", 
"https://github.com/hwchase17/langchainjs", 
"https://github.com/sullivan-sean/chat-langchainjs", 
"https://js.langchain.com/docs/", 
"https://python.langchain.com/en/latest/", 
"https://twitter.com/langchainai"]

> Finished chain.

```

```
'["https://blog.langchain.dev/", 
"https://discord.gg/6adMQxSpJS", 
"https://docs.langchain.com/docs/",
 "https://github.com/hwchase17/chat-langchain", 
 "https://github.com/hwchase17/langchain", 
 "https://github.com/hwchase17/langchainjs", 
 "https://github.com/sullivan-sean/chat-langchainjs", 
 "https://js.langchain.com/docs/", 
 "https://python.langchain.com/en/latest/", 
 "https://twitter.com/langchainai"]'

```

