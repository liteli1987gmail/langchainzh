

带工具检索的自定义代理[#](#custom-agent-with-tool-retrieval "本标题的永久链接")
============================================================

> [本教程](custom_llm_agent)，假定你已经熟悉代理工作原理。

本教程介绍的新想法是使用检索来选择要用于回答代理查询的工具集。

当你有很多工具可供选择时，这非常有用。你不能在提示中放置所有工具的描述（由于上下文长度问题)，因此你动态选择你想要在运行时考虑使用的N个工具。

我们将创建一个有点伪需求的例子。

我们将有一个合适的工具（搜索），然后99个假工具，这只是废话。

然后，我们将在提示模板中添加一个步骤，该步骤接受用户输入并检索与查询相关的工具。

设置环境[#](#set-up-environment "本标题的永久链接")
---------------------------------------

进行必要的导入等设置。

``` python
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import StringPromptTemplate
from langchain import OpenAI, SerpAPIWrapper, LLMChain
from typing import List, Union
from langchain.schema import AgentAction, AgentFinish
import re

```

设置工具[#](#set-up-tools "本标题的永久链接")
---------------------------------

我们将创建一个合适的工具（搜索)和99个不相关的工具。

``` python /for i in range(99)/
# Define which tools the agent can use to answer user queries
search = SerpAPIWrapper()
search_tool = Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    )
def fake_func(inp: str) -> str:
    return "foo"
fake_tools = [
    Tool(
        name=f"foo-{i}", 
        func=fake_func, 
        description=f"a silly function that you can use to get more information about the number {i}"
    ) 
    for i in range(99)
]
ALL_TOOLS = [search_tool] + fake_tools

```

工具检索器(tool-retriever)[#](#tool-retriever "本标题的永久链接")
------------------------------------

我们将使用向量存储来为每个工具描述创建嵌入。

然后，对于传入的查询，我们可以为该查询创建嵌入，并进行相关工具的相似性搜索。

``` python
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document

```

``` python
docs = [Document(page_content=t.description, metadata={"index": i}) for i, t in enumerate(ALL_TOOLS)]

```

``` python
vector_store = FAISS.from_documents(docs, OpenAIEmbeddings())

```

``` python
retriever = vector_store.as_retriever()

def get_tools(query):
    docs = retriever.get_relevant_documents(query)
    return [ALL_TOOLS[d.metadata["index"]] for d in docs]

```

现在我们可以测试这个检索器，看看它是否有效。

``` python
get_tools("whats the weather?")

```

``` python
[Tool(name='Search', description='useful for when you need to answer questions about current events', return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x114b28a90>, func=<bound method SerpAPIWrapper.run of SerpAPIWrapper(search_engine=<class 'serpapi.google_search.GoogleSearch'>, params={'engine': 'google', 'google_domain': 'google.com', 'gl': 'us', 'hl': 'en'}, serpapi_api_key='c657176b327b17e79b55306ab968d164ee2369a7c7fa5b3f8a5f7889903de882', aiosession=None)>, coroutine=None),
 Tool(name='foo-95', description='a silly function that you can use to get more information about the number 95', return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x114b28a90>, func=<function fake_func at 0x15e5bd1f0>, coroutine=None),
 Tool(name='foo-12', description='a silly function that you can use to get more information about the number 12', return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x114b28a90>, func=<function fake_func at 0x15e5bd1f0>, coroutine=None),
 Tool(name='foo-15', description='a silly function that you can use to get more information about the number 15', return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x114b28a90>, func=<function fake_func at 0x15e5bd1f0>, coroutine=None)]

```

``` python
get_tools("whats the number 13?")

```

``` python
[Tool(name='foo-13', description='a silly function that you can use to get more information about the number 13', return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x114b28a90>, func=<function fake_func at 0x15e5bd1f0>, coroutine=None),
 Tool(name='foo-12', description='a silly function that you can use to get more information about the number 12', return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x114b28a90>, func=<function fake_func at 0x15e5bd1f0>, coroutine=None),
 Tool(name='foo-14', description='a silly function that you can use to get more information about the number 14', return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x114b28a90>, func=<function fake_func at 0x15e5bd1f0>, coroutine=None),
 Tool(name='foo-11', description='a silly function that you can use to get more information about the number 11', return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x114b28a90>, func=<function fake_func at 0x15e5bd1f0>, coroutine=None)]

```

提示模板[#](#prompt-template "永久链接到此标题")
------------------------------------

提示模板非常标准，因为我们实际上没有改变实际提示模板中的太多逻辑，而是只改变了如何进行检索。

``` python
# Set up the base template
template = """Answer the following questions as best you can, but speaking as a pirate might speak. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin! Remember to speak as a pirate when giving your final answer. Use lots of "Arg"s

Question: {input}
{agent_scratchpad}"""

```

自定义提示模板现在具有一个`tools_getter`的概念，我们对输入调用它以选择要使用的工具。

``` python
from typing import Callable
# Set up a prompt template
class CustomPromptTemplate(StringPromptTemplate):
    # The template to use
    template: str
    ############## NEW ######################
    # The list of tools available
    tools_getter: Callable

    def format(self, **kwargs) -> str:
        # Get the intermediate steps (AgentAction, Observation tuples)
        # Format them in a particular way
        intermediate_steps = kwargs.pop("intermediate_steps")
        thoughts = ""
        for action, observation in intermediate_steps:
            thoughts += action.log
            thoughts += f"\nObservation: {observation}\nThought: "
        # Set the agent_scratchpad variable to that value
        kwargs["agent_scratchpad"] = thoughts
        ############## NEW ######################
        tools = self.tools_getter(kwargs["input"])
        # Create a tools variable from the list of tools provided
        kwargs["tools"] = "\n".join([f"{tool.name}: {tool.description}" for tool in tools])
        # Create a list of tool names for the tools provided
        kwargs["tool_names"] = ", ".join([tool.name for tool in tools])
        return self.template.format(**kwargs)

```
``` python
prompt = CustomPromptTemplate(
    template=template,
    tools_getter=get_tools,
    # This omits the `agent_scratchpad`, `tools`, and `tool_names` variables because those are generated dynamically
    # This includes the `intermediate_steps` variable because that is needed
    input_variables=["input", "intermediate_steps"]
)

```

输出解析器 (Output Parser)[#](#output-parser "永久链接到此标题")
-----------------------------------

输出解析器与之前的教程没有改变，因为我们没有改变任何有关输出格式的内容。

``` python
class CustomOutputParser(AgentOutputParser):

    def parse(self, llm_output: str) -> Union[AgentAction, AgentFinish]:
        # Check if agent should finish
        if "Final Answer:" in llm_output:
            return AgentFinish(
                # Return values is generally always a dictionary with a single `output` key
                # It is not recommended to try anything else at the moment :)
                return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
                log=llm_output,
            )
        # Parse out the action and action input
        regex = r"Action\s*\d*\s*:(.*?)\nAction\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
        match = re.search(regex, llm_output, re.DOTALL)
        if not match:
            raise ValueError(f"Could not parse LLM output: `{llm_output}`")
        action = match.group(1).strip()
        action_input = match.group(2)
        # Return the action and action input
        return AgentAction(tool=action, tool_input=action_input.strip(" ").strip('"'), log=llm_output)

```

``` python
output_parser = CustomOutputParser()

```

设置LLM，停止序列和代理[#](#set-up-llm-stop-sequence-and-the-agent "永久链接到此标题")
--------------------------------------------------------------------

与之前的教程相同

``` python
llm = OpenAI(temperature=0)

```

``` python
# LLM chain consisting of the LLM and a prompt
llm_chain = LLMChain(llm=llm, prompt=prompt)

```

``` python
tools = get_tools("whats the weather?")
tool_names = [tool.name for tool in tools]
agent = LLMSingleActionAgent(
    llm_chain=llm_chain, 
    output_parser=output_parser,
    stop=["\nObservation:"], 
    allowed_tools=tool_names
)

```

使用代理（Use the Agent）[#](#use-the-agent "永久链接到此标题")
----------------------------------

现在我们可以使用它了！

``` python
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

```

``` python
agent_executor.run("What's the weather in SF?")

```

``` python
> Entering new AgentExecutor chain...
Thought: I need to find out what the weather is in SF
Action: Search
Action Input: Weather in SF

Observation:Mostly cloudy skies early, then partly cloudy in the afternoon. High near 60F. ENE winds shifting to W at 10 to 15 mph. Humidity71%. UV Index6 of 10. I now know the final answer
Final Answer: 'Arg, 'tis mostly cloudy skies early, then partly cloudy in the afternoon. High near 60F. ENE winds shiftin' to W at 10 to 15 mph. Humidity71%. UV Index6 of 10.

> Finished chain.

```
``` python
"'Arg, 'tis mostly cloudy skies early, then partly cloudy in the afternoon. High near 60F. ENE winds shiftin' to W at 10 to 15 mph. Humidity71%. UV Index6 of 10."

```

