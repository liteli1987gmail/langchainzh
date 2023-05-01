


 Google Serper API
 [#](#google-serper-api "Permalink to this headline")
=========================================================================



 This notebook goes over how to use the Google Serper component to search the web. First you need to sign up for a free account at
 [serper.dev](https://serper.dev) 
 and get your api key.
 







```
import os
os.environ["SERPER_API_KEY"] = ""

```










```
from langchain.utilities import GoogleSerperAPIWrapper

```










```
search = GoogleSerperAPIWrapper()

```










```
search.run("Obama's first name?")

```








```
'Barack Hussein Obama II'

```







 As part of a Self Ask With Search Chain
 [#](#as-part-of-a-self-ask-with-search-chain "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------







```
os.environ['OPENAI_API_KEY'] = ""

```










```
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

llm = OpenAI(temperature=0)
search = GoogleSerperAPIWrapper()
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
Intermediate answer: Current champions Carlos Alcaraz, 2022 men's singles champion.
Follow up: Where is Carlos Alcaraz from?
Intermediate answer: El Palmar, Spain
So the final answer is: El Palmar, Spain

> Finished chain.

```






```
'El Palmar, Spain'

```








