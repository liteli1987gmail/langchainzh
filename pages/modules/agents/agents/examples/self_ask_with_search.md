


 Self Ask With Search
 [#](#self-ask-with-search "Permalink to this headline")
===============================================================================



 This notebook showcases the Self Ask With Search chain.
 







```
from langchain import OpenAI, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

llm = OpenAI(temperature=0)
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search"
    )
]

self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)
self_ask_with_search.run("What is the hometown of the reigning men's U.S. Open champion?")

```








```
> Entering new AgentExecutor chain...
 Yes.
Follow up: Who is the reigning men's U.S. Open champion?
Intermediate answer: Carlos Alcaraz Garfia
Follow up: Where is Carlos Alcaraz Garfia from?
Intermediate answer: El Palmar, Spain
So the final answer is: El Palmar, Spain

> Finished chain.

```






```
'El Palmar, Spain'

```







