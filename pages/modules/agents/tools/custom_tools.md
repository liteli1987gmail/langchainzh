


 Defining Custom Tools
 [#](#defining-custom-tools "Permalink to this headline")
=================================================================================



 When constructing your own agent, you will need to provide it with a list of Tools that it can use. Besides the actual function that is called, the Tool consists of several components:
 


* name (str), is required and must be unique within a set of tools provided to an agent
* description (str), is optional but recommended, as it is used by an agent to determine tool use
* return_direct (bool), defaults to False
* args_schema (Pydantic BaseModel), is optional but recommended, can be used to provide more information or validation for expected parameters.



 The function that should be called when the tool is selected should return a single string.
 



 There are two ways to define a tool, we will cover both in the example below.
 







```
# Import things that are needed generically
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType, Tool, initialize_agent, tool
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool

```






 Initialize the LLM to use for the agent.
 







```
llm = ChatOpenAI(temperature=0)

```







 Completely New Tools
 [#](#completely-new-tools "Permalink to this headline")
-------------------------------------------------------------------------------



 First, we show how to create completely new tools from scratch.
 



 There are two ways to do this: either by using the Tool dataclass, or by subclassing the BaseTool class.
 



### 
 Tool dataclass
 [#](#tool-dataclass "Permalink to this headline")







```
# Load the tool configs that are needed.
search = SerpAPIWrapper()
llm_math_chain = LLMMathChain(llm=llm, verbose=True)
tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    ),
]
# You can also define an args_schema to provide more information about inputs
from pydantic import BaseModel, Field

class CalculatorInput(BaseModel):
    question: str = Field()
        

tools.append(
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
        args_schema=CalculatorInput
    )
)

```










```
# Construct the agent. We will use the default agent type here.
# See documentation for a full list of options.
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

```










```
agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

```








```
> Entering new AgentExecutor chain...
I need to find out Leo DiCaprio's girlfriend's name and her age
Action: Search
Action Input: "Leo DiCaprio girlfriend"DiCaprio broke up with girlfriend Camila Morrone, 25, in the summer of 2022, after dating for four years.I need to find out Camila Morrone's current age
Action: Calculator
Action Input: 25^(0.43)

> Entering new LLMMathChain chain...
25^(0.43)```text
25\*\*(0.43)
```
...numexpr.evaluate("25\*\*(0.43)")...

Answer: 3.991298452658078
> Finished chain.
Answer: 3.991298452658078I now know the final answer
Final Answer: 3.991298452658078

> Finished chain.

```






```
'3.991298452658078'

```







### 
 Subclassing the BaseTool class
 [#](#subclassing-the-basetool-class "Permalink to this headline")







```
from typing import Type

class CustomSearchTool(BaseTool):
    name = "Search"
    description = "useful for when you need to answer questions about current events"

    def _run(self, query: str) -> str:
 """Use the tool."""
        return search.run(query)
    
    async def _arun(self, query: str) -> str:
 """Use the tool asynchronously."""
        raise NotImplementedError("BingSearchRun does not support async")
    
class CustomCalculatorTool(BaseTool):
    name = "Calculator"
    description = "useful for when you need to answer questions about math"
    args_schema: Type[BaseModel] = CalculatorInput

    def _run(self, query: str) -> str:
 """Use the tool."""
        return llm_math_chain.run(query)
    
    async def _arun(self, query: str) -> str:
 """Use the tool asynchronously."""
        raise NotImplementedError("BingSearchRun does not support async")

```










```
tools = [CustomSearchTool(), CustomCalculatorTool()]

```










```
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

```










```
agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

```








```
> Entering new AgentExecutor chain...
I need to find out Leo DiCaprio's girlfriend's name and her age
Action: Search
Action Input: "Leo DiCaprio girlfriend"DiCaprio broke up with girlfriend Camila Morrone, 25, in the summer of 2022, after dating for four years.I need to find out Camila Morrone's current age
Action: Calculator
Action Input: 25^(0.43)

> Entering new LLMMathChain chain...
25^(0.43)```text
25\*\*(0.43)
```
...numexpr.evaluate("25\*\*(0.43)")...

Answer: 3.991298452658078
> Finished chain.
Answer: 3.991298452658078I now know the final answer
Final Answer: 3.991298452658078

> Finished chain.

```






```
'3.991298452658078'

```









 Using the
 `tool`
 decorator
 [#](#using-the-tool-decorator "Permalink to this headline")
-------------------------------------------------------------------------------------------



 To make it easier to define custom tools, a
 `@tool`
 decorator is provided. This decorator can be used to quickly create a
 `Tool`
 from a simple function. The decorator uses the function name as the tool name by default, but this can be overridden by passing a string as the first argument. Additionally, the decorator will use the function’s docstring as the tool’s description.
 







```
from langchain.agents import tool

@tool
def search_api(query: str) -> str:
 """Searches the API for the query."""
    return f"Results for query {query}"

```










```
search_api

```








```
Tool(name='search_api', description='search_api(query: str) -> str - Searches the API for the query.', args_schema=<class 'pydantic.main.SearchApi'>, return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x12748c4c0>, func=<function search_api at 0x16bd664c0>, coroutine=None)

```






 You can also provide arguments like the tool name and whether to return directly.
 







```
@tool("search", return_direct=True)
def search_api(query: str) -> str:
 """Searches the API for the query."""
    return "Results"

```










```
search_api

```








```
Tool(name='search', description='search(query: str) -> str - Searches the API for the query.', args_schema=<class 'pydantic.main.SearchApi'>, return_direct=True, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x12748c4c0>, func=<function search_api at 0x16bd66310>, coroutine=None)

```






 You can also provide
 `args_schema`
 to provide more information about the argument
 







```
class SearchInput(BaseModel):
    query: str = Field(description="should be a search query")
        
@tool("search", return_direct=True, args_schema=SearchInput)
def search_api(query: str) -> str:
 """Searches the API for the query."""
    return "Results"

```










```
search_api

```








```
Tool(name='search', description='search(query: str) -> str - Searches the API for the query.', args_schema=<class '__main__.SearchInput'>, return_direct=True, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x12748c4c0>, func=<function search_api at 0x16bcf0ee0>, coroutine=None)

```








 Modify existing tools
 [#](#modify-existing-tools "Permalink to this headline")
---------------------------------------------------------------------------------



 Now, we show how to load existing tools and just modify them. In the example below, we do something really simple and change the Search tool to have the name
 `Google
 

 Search`
 .
 







```
from langchain.agents import load_tools

```










```
tools = load_tools(["serpapi", "llm-math"], llm=llm)

```










```
tools[0].name = "Google Search"

```










```
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

```










```
agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

```








```
> Entering new AgentExecutor chain...
I need to find out Leo DiCaprio's girlfriend's name and her age.
Action: Google Search
Action Input: "Leo DiCaprio girlfriend"I draw the lime at going to get a Mohawk, though." DiCaprio broke up with girlfriend Camila Morrone, 25, in the summer of 2022, after dating for four years. He's since been linked to another famous supermodel – Gigi Hadid.Now I need to find out Camila Morrone's current age.
Action: Calculator
Action Input: 25^0.43Answer: 3.991298452658078I now know the final answer.
Final Answer: Camila Morrone's current age raised to the 0.43 power is approximately 3.99.

> Finished chain.

```






```
"Camila Morrone's current age raised to the 0.43 power is approximately 3.99."

```








 Defining the priorities among Tools
 [#](#defining-the-priorities-among-tools "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------



 When you made a Custom tool, you may want the Agent to use the custom tool more than normal tools.
 



 For example, you made a custom tool, which gets information on music from your database. When a user wants information on songs, You want the Agent to use
 `the
 

 custom
 

 tool`
 more than the normal
 `Search
 

 tool`
 . But the Agent might prioritize a normal Search tool.
 



 This can be accomplished by adding a statement such as
 `Use
 

 this
 

 more
 

 than
 

 the
 

 normal
 

 search
 

 if
 

 the
 

 question
 

 is
 

 about
 

 Music,
 

 like
 

 'who
 

 is
 

 the
 

 singer
 

 of
 

 yesterday?'
 

 or
 

 'what
 

 is
 

 the
 

 most
 

 popular
 

 song
 

 in
 

 2022?'`
 to the description.
 



 An example is below.
 







```
# Import things that are needed generically
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain import LLMMathChain, SerpAPIWrapper
search = SerpAPIWrapper()
tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    ),
    Tool(
        name="Music Search",
        func=lambda x: "'All I Want For Christmas Is You' by Mariah Carey.", #Mock Function
        description="A Music search engine. Use this more than the normal search if the question is about Music, like 'who is the singer of yesterday?' or 'what is the most popular song in 2022?'",
    )
]

agent = initialize_agent(tools, OpenAI(temperature=0), agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

```










```
agent.run("what is the most famous song of christmas")

```








```
> Entering new AgentExecutor chain...
 I should use a music search engine to find the answer
Action: Music Search
Action Input: most famous song of christmas'All I Want For Christmas Is You' by Mariah Carey. I now know the final answer
Final Answer: 'All I Want For Christmas Is You' by Mariah Carey.

> Finished chain.

```






```
"'All I Want For Christmas Is You' by Mariah Carey."

```








 Using tools to return directly
 [#](#using-tools-to-return-directly "Permalink to this headline")
---------------------------------------------------------------------------------------------------



 Often, it can be desirable to have a tool output returned directly to the user, if it’s called. You can do this easily with LangChain by setting the return_direct flag for a tool to be True.
 







```
llm_math_chain = LLMMathChain(llm=llm)
tools = [
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
        return_direct=True
    )
]

```










```
llm = OpenAI(temperature=0)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

```










```
agent.run("whats 2\*\*.12")

```








```
> Entering new AgentExecutor chain...
 I need to calculate this
Action: Calculator
Action Input: 2\*\*.12Answer: 1.086734862526058

> Finished chain.

```






```
'Answer: 1.086734862526058'

```








