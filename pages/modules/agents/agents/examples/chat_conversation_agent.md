


 Conversation Agent (for Chat Models)
 [#](#conversation-agent-for-chat-models "Permalink to this headline")
=============================================================================================================



 This notebook walks through using an agent optimized for conversation, using ChatModels. Other agents are often optimized for using tools to figure out the best response, which is not ideal in a conversational setting where you may want the agent to be able to chat with the user as well.
 



 This is accomplished with a specific type of agent (
 `chat-conversational-react-description`
 ) which expects to be used with a memory component.
 







```
import os
os.environ["LANGCHAIN_HANDLER"] = "langchain"

```










```
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
from langchain.agents import AgentType

```








```
WARNING:root:Failed to default session, using empty session: HTTPConnectionPool(host='localhost', port=8000): Max retries exceeded with url: /sessions (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x10a1767c0>: Failed to establish a new connection: [Errno 61] Connection refused'))

```










```
search = SerpAPIWrapper()
tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world. the input to this should be a single search term."
    ),
]

```










```
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

```










```
llm=ChatOpenAI(temperature=0)
agent_chain = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)

```










```
agent_chain.run(input="hi, i am bob")

```








```
> Entering new AgentExecutor chain...

```






```
WARNING:root:Failed to persist run: HTTPConnectionPool(host='localhost', port=8000): Max retries exceeded with url: /chain-runs (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x13fab40d0>: Failed to establish a new connection: [Errno 61] Connection refused'))

```






```
{
 "action": "Final Answer",
 "action_input": "Hello Bob! How can I assist you today?"
}

> Finished chain.

```






```
'Hello Bob! How can I assist you today?'

```










```
agent_chain.run(input="what's my name?")

```








```
> Entering new AgentExecutor chain...

```






```
WARNING:root:Failed to persist run: HTTPConnectionPool(host='localhost', port=8000): Max retries exceeded with url: /chain-runs (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x13fab44f0>: Failed to establish a new connection: [Errno 61] Connection refused'))

```






```
{
 "action": "Final Answer",
 "action_input": "Your name is Bob."
}

> Finished chain.

```






```
'Your name is Bob.'

```










```
agent_chain.run("what are some good dinners to make this week, if i like thai food?")

```








```
> Entering new AgentExecutor chain...
{
 "action": "Current Search",
 "action_input": "Thai food dinner recipes"
}
Observation: 59 easy Thai recipes for any night of the week · Marion Grasby's Thai spicy chilli and basil fried rice · Thai curry noodle soup · Marion Grasby's Thai Spicy ...
Thought:

```






```
WARNING:root:Failed to persist run: HTTPConnectionPool(host='localhost', port=8000): Max retries exceeded with url: /chain-runs (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x13fae8be0>: Failed to establish a new connection: [Errno 61] Connection refused'))

```






```
{
 "action": "Final Answer",
 "action_input": "Here are some Thai food dinner recipes you can make this week: Thai spicy chilli and basil fried rice, Thai curry noodle soup, and Thai Spicy ... (59 recipes in total)."
}

> Finished chain.

```






```
'Here are some Thai food dinner recipes you can make this week: Thai spicy chilli and basil fried rice, Thai curry noodle soup, and Thai Spicy ... (59 recipes in total).'

```










```
agent_chain.run(input="tell me the last letter in my name, and also tell me who won the world cup in 1978?")

```








```
> Entering new AgentExecutor chain...
```json
{
 "action": "Current Search",
 "action_input": "who won the world cup in 1978"
}
```
Observation: Argentina national football team
Thought:

```






```
WARNING:root:Failed to persist run: HTTPConnectionPool(host='localhost', port=8000): Max retries exceeded with url: /chain-runs (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x13fae86d0>: Failed to establish a new connection: [Errno 61] Connection refused'))

```






```
```json
{
 "action": "Final Answer",
 "action_input": "The last letter in your name is 'b', and the winner of the 1978 World Cup was the Argentina national football team."
}
```

> Finished chain.

```






```
"The last letter in your name is 'b', and the winner of the 1978 World Cup was the Argentina national football team."

```










```
agent_chain.run(input="whats the weather like in pomfret?")

```








```
> Entering new AgentExecutor chain...
{
 "action": "Current Search",
 "action_input": "weather in pomfret"
}
Observation: 10 Day Weather-Pomfret, CT ; Sun 16. 64° · 50°. 24% · NE 7 mph ; Mon 17. 58° · 45°. 70% · ESE 8 mph ; Tue 18. 57° · 37°. 8% · WSW 15 mph.
Thought:

```






```
WARNING:root:Failed to persist run: HTTPConnectionPool(host='localhost', port=8000): Max retries exceeded with url: /chain-runs (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x13fa9d7f0>: Failed to establish a new connection: [Errno 61] Connection refused'))

```






```
{
 "action": "Final Answer",
 "action_input": "The weather in Pomfret, CT for the next 10 days is as follows: Sun 16. 64° · 50°. 24% · NE 7 mph ; Mon 17. 58° · 45°. 70% · ESE 8 mph ; Tue 18. 57° · 37°. 8% · WSW 15 mph."
}

> Finished chain.

```






```
'The weather in Pomfret, CT for the next 10 days is as follows: Sun 16. 64° · 50°. 24% · NE 7 mph ; Mon 17. 58° · 45°. 70% · ESE 8 mph ; Tue 18. 57° · 37°. 8% · WSW 15 mph.'

```







