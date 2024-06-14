# 工具调用代理

[工具调用](/modules/model_io/chat/function_calling) 允许模型检测何时应调用一个或多个工具，并响应应传递给这些工具的输入。在 API 调用中，您可以描述工具，并让模型智能选择输出一个结构化对象，比如 JSON，其中包含调用这些工具所需的参数。工具 API 的目标是比使用通用文本完成或聊天 API 更可靠地返回有效和有用的工具调用。

我们可以利用这种结构化输出，结合您可以将多个工具绑定到[工具调用聊天模型](/docs/integrations/chat/)，并允许模型选择调用哪一个，从而创建一个代理，反复调用工具并接收结果，直到查询解决为止。

这是[OpenAI 工具代理](/modules/agents/agent_types/openai_tools/)的更通用版本，它专为 OpenAI 的特定风格的工具调用设计。它使用 LangChain 的 ToolCall 接口来支持更广泛的提供者实现，例如[Anthropic](/docs/integrations/chat/anthropic/)、[Google Gemini](/docs/integrations/chat/google_vertex_ai_palm/) 和 [Mistral](/docs/integrations/chat/mistralai/)，还有[OpenAI](/docs/integrations/chat/openai/)。

## 设置

任何支持工具调用的模型都可以在这个代理中使用。您可以在[这里](/docs/integrations/chat/)查看哪些模型支持工具调用。

这个演示使用 [Tavily](https://app.tavily.com)，但您也可以替换成任何其他[内置工具](/docs/integrations/tools)，或添加[自定义工具](/modules/tools/custom_tools/)。您需要注册一个 API 密钥，并将其设置为 `process.env.TAVILY_API_KEY`。

```{=mdx}
import ChatModelTabs from "@theme/ChatModelTabs";

<ChatModelTabs customVarName="llm" />
```

```python
# | output: false
# | echo: false

from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0)
```

## 初始化工具

我们首先会创建一个可以搜索网络的工具：


```python
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate

tools = [TavilySearchResults(max_results=1)]
```

## 创建代理

接下来，让我们初始化我们的工具调用代理：


```python
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Make sure to use the tavily_search_results_json tool for information.",
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

# 构建工具代理
agent = create_tool_calling_agent(llm, tools, prompt)
```

## 执行代理

现在，让我们初始化执行我们的代理的执行器！


```python
# 通过传入代理和工具来创建一个代理执行器
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke({"input": "what is LangChain?"})
```

```{=mdx}
:::tip
[LangSmith trace](https://smith.langchain.com/public/2f956a2e-0820-47c4-a798-c83f024e5ca1/r)
:::
```

## 使用聊天记录

这种类型的代理可以选择接收表示以前对话轮的聊天消息。它可以使用以前的历史记录来进行对话回复。有关更多详细信息，请参阅[代理快速入门中的此部分](/modules/agents/quick_start#adding-in-memory)。


```python
from langchain_core.messages import AIMessage, HumanMessage

agent_executor.invoke(
    {
        "input": "what's my name? Don't use tools to look this up unless you NEED to",
        "chat_history": [
            HumanMessage(content="hi! my name is bob"),
            AIMessage(content="Hello Bob! How can I assist you today?"),
        ],
    }
)
```

```{=mdx}
:::tip
[LangSmith trace](https://smith.langchain.com/public/e21ececb-2e60-49e5-9f06-a91b0fb11fb8/r)
:::
```

