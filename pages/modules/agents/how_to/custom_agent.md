# 自定义代理

这个文档演示了如何创建自定义代理。

在这个例子中，我们将使用OpenAI的工具调用来创建这个代理。
**这通常是创建代理最可靠的方式。**

首先，我们将创建一个没有内存的代理，然后再展示如何添加内存。
内存是用来实现对话的必要条件。

## 加载LLM
首先，让我们加载我们要用来控制代理的语言模型。


```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
```

## 定义工具
接下来，让我们定义一些要使用的工具。
我们编写一个非常简单的Python函数来计算传入单词的长度。

请注意，这里我们使用的函数文档字符串非常重要。了解更多关于为什么这样是重要的信息，请阅读[这里](/modules/tools/custom_tools)


```python
from langchain.agents import tool


@tool
def get_word_length(word: str) -> int:
    """返回一个单词的长度。"""
    return len(word)


get_word_length.invoke("abc")
```




    3




```python
tools = [get_word_length]
```

## 创建提示信息
现在让我们创建提示信息。
由于OpenAI函数调用是针对工具使用进行微调的，我们几乎不需要任何有关如何推理或输出格式的说明。
我们只需要两个输入变量：`input`和`agent_scratchpad`。`input`应该是一个包含用户目标的字符串。`agent_scratchpad`应该是一个包含先前代理工具调用和对应工具输出的消息序列。


```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "您是一个非常强大的助手，但不知道当前的事件",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
```

## 将工具与LLM绑定

代理如何知道可以使用哪些工具呢？

在这种情况下，我们依赖于OpenAI工具调用LLM，它将工具作为一个单独的参数，并且专门训练了如何在何时调用这些工具。

为了将工具传递给代理，我们只需要将它们格式化为[OpenAI工具格式](https://platform.openai.com/docs/api-reference/chat/create)，并将其传递给我们的模型。（通过`bind`函数将函数绑定，确保每次调用模型时都会将它们传递过去。）


```python
llm_with_tools = llm.bind_tools(tools)
```

## 创建代理
把这些组件放在一起，我们现在可以创建代理了。
我们将导入最后的两个实用函数：一个用于将中间步骤（代理动作、工具输出对）格式化为可以发送到模型的输入消息的组件，一个用于将输出消息转换为代理动作/代理结束。

```python
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)
```


```python
from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```


```python
list(agent_executor.stream({"input": "单词eudca有多少个字母"}))
```

    
    
    [1m> 开始新的AgentExecutor链条...[0m
    [32;1m[1;3m
    正在调用：get_word_length，输入参数为{'word': 'eudca'}
    
    
    [0m[36;1m[1;3m5[0m[32;1m[1;3m单词"eudca"有5个字母。[0m
    
    [1m> 完成链条。[0m
    




    [{'actions': [OpenAIToolAgentAction(tool='get_word_length', tool_input={'word': 'eudca'}, log="\n正在调用：get_word_length，输入参数为{'word': 'eudca'}\n\n\n", message_log=[AIMessageChunk(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_A07D5TuyqcNIL0DIEVRPpZkg', 'function': {'arguments': '{\n  "word": "eudca"\n}', 'name': 'get_word_length'}, 'type': 'function'}]})], tool_call_id='call_A07D5TuyqcNIL0DIEVRPpZkg')],
      'messages': [AIMessageChunk(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_A07D5TuyqcNIL0DIEVRPpZkg', 'function': {'arguments': '{\n  "word": "eudca"\n}', 'name': 'get_word_length'}, 'type': 'function'}]})]},
     {'steps': [AgentStep(action=OpenAIToolAgentAction(tool='get_word_length', tool_input={'word': 'eudca'}, log="\n正在调用：get_word_length，输入参数为{'word': 'eudca'}\n\n\n", message_log=[AIMessageChunk(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_A07D5TuyqcNIL0DIEVRPpZkg', 'function': {'arguments': '{\n  "word": "eudca"\n}', 'name': 'get_word_length'}, 'type': 'function'}]})], tool_call_id='call_A07D5TuyqcNIL0DIEVRPpZkg'), observation=5)],
      'messages': [FunctionMessage(content='5', name='get_word_length')]},
     {'output': '单词"eudca"有5个字母。',
      'messages': [AIMessage(content='单词"eudca"有5个字母。')]}]



如果我们将其与基本LLM进行对比，可以看到单独使用LLM的结果并不理想


```python
llm.invoke("单词educa有多少个字母")
```




    AIMessage(content='单词"educa"有6个字母。')



## 添加内存

这很棒 - 我们有了一个代理！
然而，这个代理是无状态的 - 它不会记住任何关于先前交互的信息。
这意味着您不能轻松地提出跟进问题。
让我们通过添加内存来解决这个问题。

为了做到这一点，我们需要做两件事：

1. 在提示信息中添加一个内存变量的位置
2. 跟踪聊天历史记录

首先，让我们在提示信息中添加一个内存的位置。
我们通过在`prompt`中添加一个键为`"chat_history"`的消息占位符来实现。
请注意，我们将此放在新的用户输入之上（以便遵循对话流程）。

---

# 自定义代理

这本笔记本介绍了如何创建您自己的自定义代理。

在这个例子中，我们将使用 OpenAI 工具调用来创建这个代理。
**这通常是创建代理的最可靠方式。**

我们首先将创建一个**没有记忆**的代理，但随后我们将展示如何添加记忆。
记忆是实现对话所必需的。

## 加载 LLM
首先，让我们加载我们将用于控制代理的语言模型。

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
```

## 定义工具
接下来，让我们定义一些要使用的工具。
让我们编写一个非常简单的 Python 函数来计算传入单词的长度。

注意，这里我们使用的函数文档字符串非常重要。了解更多为什么这是这样[这里](/modules/tools/custom_tools)

```python
from langchain.agents import tool


@tool
def get_word_length(word: str) -> int:
    """返回一个单词的长度。"""
    return len(word)


get_word_length.invoke("abc")
```

    3

```python
tools = [get_word_length]
```

## 创建提示

现在让我们创建提示。
因为 OpenAI 功能调用针对工具使用进行了微调，我们几乎不需要任何关于如何推理或如何输出格式的说明。
我们只需要两个输入变量：`input` 和 `agent_scratchpad`。`input` 应该是包含用户目标的字符串。`agent_scratchpad` 应该是包含先前代理工具调用及相应工具输出的消息序列。

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个非常强大的助手，但不了解当前事件",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
```

## 将工具绑定到 LLM

代理如何知道它可以使用什么工具？

在这种情况下，我们依赖于 OpenAI 工具调用 LLM，它们将工具作为单独的参数，并经过特别训练以知道何时调用这些工具。

要将我们的工具传递给代理，我们只需要将它们格式化为[OpenAI 工具格式](https://platform.openai.com/docs/api-reference/chat/create) 并将它们传递到我们的模型。（通过`绑定`函数，我们确保它们每次模型被调用时都会传入。）

```python
llm_with_tools = llm.bind_tools(tools)
```

## 创建代理

将这些部分组合起来，我们现在可以创建代理了。
我们将导入两个最后的实用函数：一个用于将中间步骤（代理动作、工具输出对）格式化为可以发送到模型的输入消息的组件，以及一个用于将输出消息转换为代理动作/代理完成的组件。



```python
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)
```


```python
from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```


```python
list(agent_executor.stream({"input": "How many letters in the word eudca"}))
```

    
    
    [1m> Entering new AgentExecutor chain...[0m
    [32;1m[1;3m
    Invoking: `get_word_length` with `{'word': 'eudca'}`
    
    
    [0m[36;1m[1;3m5[0m[32;1m[1;3mThere are 5 letters in the word "eudca".[0m
    
    [1m> Finished chain.[0m
    




    [{'actions': [OpenAIToolAgentAction(tool='get_word_length', tool_input={'word': 'eudca'}, log="\nInvoking: `get_word_length` with `{'word': 'eudca'}`\n\n\n", message_log=[AIMessageChunk(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_A07D5TuyqcNIL0DIEVRPpZkg', 'function': {'arguments': '{\n  "word": "eudca"\n}', 'name': 'get_word_length'}, 'type': 'function'}]})], tool_call_id='call_A07D5TuyqcNIL0DIEVRPpZkg')],
      'messages': [AIMessageChunk(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_A07D5TuyqcNIL0DIEVRPpZkg', 'function': {'arguments': '{\n  "word": "eudca"\n}', 'name': 'get_word_length'}, 'type': 'function'}]})]},
     {'steps': [AgentStep(action=OpenAIToolAgentAction(tool='get_word_length', tool_input={'word': 'eudca'}, log="\nInvoking: `get_word_length` with `{'word': 'eudca'}`\n\n\n", message_log=[AIMessageChunk(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_A07D5TuyqcNIL0DIEVRPpZkg', 'function': {'arguments': '{\n  "word": "eudca"\n}', 'name': 'get_word_length'}, 'type': 'function'}]})], tool_call_id='call_A07D5TuyqcNIL0DIEVRPpZkg'), observation=5)],
      'messages': [FunctionMessage(content='5', name='get_word_length')]},
     {'output': 'There are 5 letters in the word "eudca".',
      'messages': [AIMessage(content='There are 5 letters in the word "eudca".')]}]



If we compare this to the base LLM, we can see that the LLM alone struggles


```python
llm.invoke("How many letters in the word educa")
```




    AIMessage(content='There are 6 letters in the word "educa".')



如果我们将这个与基础的大型语言模型（LLM）进行比较，我们可以看到单独的LLM在挣扎

```python
llm.invoke("How many letters in the word educa")
```

    AIMessage(content='There are 6 letters in the word "educa".')

## 添加记忆

这很棒 - 我们有一个代理了！
然而，这个代理是无状态的 - 它不记得任何关于之前交互的事情。
这意味着你不能轻松地提出后续问题。
让我们通过添加记忆来解决这个问题。

为了做到这一点，我们需要做两件事：

1. 在提示中添加记忆变量的位置
2. 跟踪聊天历史

首先，让我们在提示中为记忆添加一个位置。
我们通过添加一个键为 `"chat_history"` 的消息占位符来实现这一点。
注意，我们将这个放在新用户输入的上方（以符合对话流程）。

```python
from langchain.prompts import MessagesPlaceholder

MEMORY_KEY = "chat_history"
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个非常强大的助手，但不擅长计算单词的长度。",
        ),
        MessagesPlaceholder(variable_name=MEMORY_KEY),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
```

然后我们可以设置一个列表来跟踪聊天历史

```python
from langchain_core.messages import AIMessage, HumanMessage

chat_history = []
```

然后我们可以将所有东西整合在一起！

```python
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
        "chat_history": lambda x: x["chat_history"],
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

在运行时，我们现在需要跟踪输入和输出作为聊天历史



```python
input1 = "how many letters in the word educa?"
result = agent_executor.invoke({"input": input1, "chat_history": chat_history})
chat_history.extend(
    [
        HumanMessage(content=input1),
        AIMessage(content=result["output"]),
    ]
)
agent_executor.invoke({"input": "is that a real word?", "chat_history": chat_history})
```

    
    
    [1m> Entering new AgentExecutor chain...[0m
    [32;1m[1;3m
    Invoking: `get_word_length` with `{'word': 'educa'}`
    
    
    [0m[36;1m[1;3m5[0m[32;1m[1;3mThere are 5 letters in the word "educa".[0m
    
    [1m> Finished chain.[0m
    
    
    [1m> Entering new AgentExecutor chain...[0m
    [32;1m[1;3mNo, "educa" is not a real word in English.[0m
    
    [1m> Finished chain.[0m
    




    {'input': 'is that a real word?',
     'chat_history': [HumanMessage(content='how many letters in the word educa?'),
      AIMessage(content='There are 5 letters in the word "educa".')],
     'output': 'No, "educa" is not a real word in English.'}


