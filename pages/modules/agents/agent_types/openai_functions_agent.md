# OpenAI函数

:::⚠⚠⚠



OpenAI API已经弃用了`functions`，推荐使用`tools`。两者的区别在于，`tools` API允许模型同时请求多个函数的调用，这在某些架构下可以减少响应时间。建议使用tools代理OpenAI模型。

请参阅以下链接了解更多信息：

[OpenAI工具](/modules/agents/agent_types/openai_tools/)

[OpenAI聊天创建](https://platform.openai.com/docs/api-reference/chat/create)

[OpenAI函数调用](https://platform.openai.com/docs/guides/function-calling)

:::⚠⚠⚠



某些OpenAI模型（如gpt-3.5-turbo-0613和gpt-4-0613）已经进行了微调，以便检测何时应该调用某个函数，并回复应该传递给该函数的输入。在API调用中，您可以描述函数，并使模型智能地选择输出一个包含调用这些函数参数的JSON对象。OpenAI函数API的目标是比通用文本完成或聊天API更可靠地返回有效和有用的函数调用。

许多开源模型采用了相同的函数调用格式，并且还对模型进行了微调，以便检测何时应该调用某个函数。

OpenAI函数代理专为这些模型而设计。

安装所需的langchain-openai tavily-python包，因为LangChain包在内部调用它们。

:::⚠⚠⚠


对于采用该格式的开源模型和提供商来说，`functions`格式仍然相关，预计该代理将为此类模型提供支持。
:::



```python
%pip install --upgrade --quiet  langchain-openai tavily-python
```

## 初始化工具

我们首先创建一些可以使用的工具


```python
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
```


```python
tools = [TavilySearchResults(max_results=1)]
```

## 创建代理


```python
# 获取要使用的提示 - 您可以修改此内容！
prompt = hub.pull("hwchase17/openai-functions-agent")
```


```python
prompt.messages
```




    [SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=[], template='You are a helpful assistant')),
     MessagesPlaceholder(variable_name='chat_history', optional=True),
     HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], template='{input}')),
     MessagesPlaceholder(variable_name='agent_scratchpad')]




```python
# 选择驱动代理的LLM
llm = ChatOpenAI(model="gpt-3.5-turbo-1106")

# 构建OpenAI函数代理
agent = create_openai_functions_agent(llm, tools, prompt)
```

## 运行代理


```python
# 通过传入代理和工具创建代理执行器
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```


```python
agent_executor.invoke({"input": "LangChain是什么？"})
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m
    调用: `tavily_search_results_json` 使用参数 `{'query': 'LangChain'}`


    [0m[36;1m[1;3m[{'url': 'https://www.ibm.com/topics/langchain', 'content': 'LangChain实质上是Python和Javascript的一个抽象库，表示常见步骤和概念  LangChain是一个用于使用大型语言模型开发应用程序的开源编排框架  具有相同功能的其他LangChain功能，如同名的链接  LangChain提供了对25种不同的嵌入方法的集成，以及对50种不同的向量存储的集成LangChain是一种使用大型语言模型（LLM）构建应用程序的工具，例如聊天机器人和虚拟助手。它简化了编程和与外部数据源和软件工作流集成的过程。它支持Python和Javascript语言，并支持各种LLM提供商，包括OpenAI，Google和IBM。'顶层回答'}][0m[32;1m[1;3mLangChain是一种使用大型语言模型（LLM）构建应用程序的工具，例如聊天机器人和虚拟助手。它简化了编程和与外部数据源和软件工作流集成的过程。LangChain提供了对25种不同的嵌入方法和50种不同的向量存储的集成。它实质上是Python和JavaScript的一个抽象库，表示常见步骤和概念。LangChain支持Python和JavaScript语言以及包括OpenAI，Google和IBM在内的各种LLM提供商。您可以在[这里](https://www.ibm.com/topics/langchain)找到有关LangChain的更多信息。[0m
    
    [1m> 完成链。[0m
    




    {'input': 'LangChain是什么？',
     'output': 'LangChain是一种使用大型语言模型（LLM）构建应用程序的工具，例如聊天机器人和虚拟助手。它简化了编程和与外部数据源和软件工作流集成的过程。LangChain提供了对25种不同的嵌入方法和50种不同的向量存储的集成。它实质上是Python和JavaScript的一个抽象库，表示常见步骤和概念。LangChain支持Python和JavaScript语言以及包括OpenAI，Google和IBM在内的各种LLM提供商。您可以在[这里](https://www.ibm.com/topics/langchain)找到有关LangChain的更多信息。'}



## 使用对话记录


```python
from langchain_core.messages import AIMessage, HumanMessage

agent_executor.invoke(
    {
        "input": "我的名字是什么？",
        "chat_history": [
            HumanMessage(content="嗨！我的名字是Bob"),
            AIMessage(content="你好Bob！有什么我可以帮助你的吗？"),
        ],
    }
)
```

    
    
    [1m> 进入新的AgentExecutor链...[0m
    [32;1m[1;3m你的名字是Bob.[0m
    
    [1m> 完成链。[0m
    




    {'input': '我的名字是什么？',
     'chat_history': [HumanMessage(content='嗨！我的名字是Bob'),
      AIMessage(content='你好Bob！有什么我可以帮助你的吗？')],
     'output': '你的名字是Bob.'}




```python

```