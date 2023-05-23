会话代理（用于聊天模型） Conversation Agent (for Chat Models)
===


这个笔记本使用ChatModels，使用针对对话优化的代理进行了演示。其他代理通常针对使用工具来计算最佳响应进行了优化.

这在会话设置中并不理想，因为您可能希望代理也能够与用户聊天。

这是通过期望与存储器组件一起使用的特定类型的代理（ `chat-conversational-react-description` ）来实现的。
```  python
!pip install langchain
!pip install google-search-results
!pip install openai
```

```  python
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from getpass import getpass
```

```  python
SERPAPI_API_KEY = getpass()
```

```  python
search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)
tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world. the input to this should be a single search term."
    ),
]
```


```  python
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
```

```  python
OPENAI_API_KEY = getpass()
```

```  python
llm=ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
agent_chain = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)
```

```  python
agent_chain.run(input="hi, i am bob")
```

```  python
> Entering new AgentExecutor chain...
{
    "action": "Final Answer",
    "action_input": "Hello Bob! How can I assist you today?"
}

> Finished chain.
```

```  python
'Hello Bob! How can I assist you today?'
```
```  python
agent_chain.run(input="what's my name?")
```
```  python
> Entering new AgentExecutor chain...
{
    "action": "Final Answer",
    "action_input": "Your name is Bob."
}

> Finished chain.
```


```  python
'Your name is Bob.'
```


```  python
agent_chain.run("what are some good dinners to make this week, if i like thai food?")
```

```  python
> Entering new AgentExecutor chain...
{
    "action": "Current Search",
    "action_input": "Thai food dinner recipes"
}
Observation: 64 easy Thai recipes for any night of the week · Thai curry noodle soup · Thai yellow cauliflower, snake bean and tofu curry · Thai-spiced chicken hand pies · Thai ...
Thought:{
    "action": "Final Answer",
    "action_input": "Here are some Thai food dinner recipes you can try this week: Thai curry noodle soup, Thai yellow cauliflower, snake bean and tofu curry, Thai-spiced chicken hand pies, and many more. You can find the full list of recipes at the source I found earlier."
}

> Finished chain.
```

```  python
'Here are some Thai food dinner recipes you can try this week: Thai curry noodle soup, Thai yellow cauliflower, snake bean and tofu curry, Thai-spiced chicken hand pies, and many more. You can find the full list of recipes at the source I found earlier.'
```

```  python
agent_chain.run(input="tell me the last letter in my name, and also tell me who won the world cup in 1978?")
```

```  python
agent_chain.run(input="tell me the last letter in my name, and also tell me who won the world cup in 1978?")
```

```  python
> Entering new AgentExecutor chain...
{
    "action": "Final Answer",
    "action_input": "The last letter in your name is 'b'. Argentina won the World Cup in 1978."
}

> Finished chain.
```

```  python
"The last letter in your name is 'b'. Argentina won the World Cup in 1978."
```

```  python
agent_chain.run(input="whats the weather like in pomfret?")
```


```  python
> Entering new AgentExecutor chain...
{
    "action": "Current Search",
    "action_input": "weather in pomfret"
}
Observation: Cloudy with showers. Low around 55F. Winds S at 5 to 10 mph. Chance of rain 60%. Humidity76%.
Thought:{
    "action": "Final Answer",
    "action_input": "Cloudy with showers. Low around 55F. Winds S at 5 to 10 mph. Chance of rain 60%. Humidity76%."
}

> Finished chain.

```


```  python

'Cloudy with showers. Low around 55F. Winds S at 5 to 10 mph. Chance of rain 60%. Humidity76%.'
```
