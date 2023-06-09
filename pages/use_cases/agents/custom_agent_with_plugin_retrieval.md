 
 
使用插件检索的自定义代理[#](#custom-agent-with-plugin-retrieval  "Permalink to this headline")
===========
 
 
这篇笔记将两个概念结合起来，构建一个可以与人工智能插件交互的自定义代理：
 
 
1.具有检索的自定义代理这介绍了检索多个工具的概念，这在尝试使用任意多个插件时非常有用。
2. [自然语言API Chains]（../../ modules/chains/examples/openapi.html）这会在OpenAPI端点周围创建自然语言包装器。 这很有用，因为：
    -（1）插件在内部使用OpenAPI端点， 
    -（2）将它们包装在NLAChain中允许路由代理更轻松地调用它们。
 
 
本笔记中介绍的新颖思想是使用检索来选择不是显式工具， 但要使用的OpenAPI规范集。 

然后我们可以从这些OpenAPI规范中生成工具。 

这种用例是在尝试让代理使用插件时。 

选择插件可能更有效率， 然后选择端点而不是直接选择端点。 

这是因为插件可能包含更有用的选择信息。
 
 
 
设置环境[#](#set-up-environment "Permalink to this headline")
-------------------
 
 
进行必要的导入，等等。
 
 
 
 
 
 ```
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser

from langchain.prompts import StringPromptTemplate

from langchain import OpenAI, SerpAPIWrapper, LLMChain

from typing import List, Union

from langchain.schema import AgentAction, AgentFinish

from langchain.agents.agent_toolkits import NLAToolkit

from langchain.tools.plugin import AIPlugin

import re



```

 
 
 
 
 
 
设置LLM[#](#setup-llm "Permalink to this headline")
-------------------------
 
 
 
 


```
llm = OpenAI(temperature=0)



```

设置插件[#](#set-up-plugins  "Permalink to this headline")
-----------------------------------


加载和索引插件





```
urls = [

    "https://datasette.io/.well-known/ai-plugin.json",

    "https://api.speak.com/.well-known/ai-plugin.json",

    "https://www.wolframalpha.com/.well-known/ai-plugin.json",

    "https://www.zapier.com/.well-known/ai-plugin.json",

    "https://www.klarna.com/.well-known/ai-plugin.json",

    "https://www.joinmilo.com/.well-known/ai-plugin.json",

    "https://slack.com/.well-known/ai-plugin.json",

    "https://schooldigger.com/.well-known/ai-plugin.json",

]



AI_PLUGINS = [AIPlugin.from_url(url) for url in urls]



```

工具检索[#](#tool-retriever  "Permalink to this headline")
-----------------------------------


我们将使用一个向量存储库为每个工具描述创建嵌入。

然后，对于传入的查询，我们可以为该查询创建嵌入并进行相似性搜索以获取相关工具。





```
from langchain.vectorstores import FAISS

from langchain.embeddings import OpenAIEmbeddings

from langchain.schema import Document



```


```
embeddings = OpenAIEmbeddings()

docs = [

    Document(page_content=plugin.description_for_model, 

             metadata={"plugin_name": plugin.name_for_model}

            )

    for plugin in AI_PLUGINS

]

vector_store = FAISS.from_documents(docs, embeddings)

toolkits_dict = {plugin.name_for_model: 

                 NLAToolkit.from_llm_and_ai_plugin(llm, plugin) 

                 for plugin in AI_PLUGINS}



```
```
Attempting to load an OpenAPI 3.0.1 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.

Attempting to load an OpenAPI 3.0.1 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.

Attempting to load an OpenAPI 3.0.1 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.

Attempting to load an OpenAPI 3.0.2 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.

Attempting to load an OpenAPI 3.0.1 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.

Attempting to load an OpenAPI 3.0.1 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.

Attempting to load an OpenAPI 3.0.1 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.

Attempting to load an OpenAPI 3.0.1 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.

Attempting to load a Swagger 2.0 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.



```


```
retriever = vector_store.as_retriever()



def get_tools(query):

    # Get documents, which contain the Plugins to use

    docs = retriever.get_relevant_documents(query)

    # Get the toolkits, one for each plugin

    tool_kits = [toolkits_dict[d.metadata["plugin_name"]] for d in docs]

    # Get the tools: a separate NLAChain for each endpoint

    tools = []

    for tk in tool_kits:

        tools.extend(tk.nla_tools)

    return tools



```





现在，我们可以测试该检索器是否有效。





```
tools = get_tools("What could I do today with my kiddo")

[t.name for t in tools]



```
```
['Milo.askMilo',

 'Zapier_Natural_Language_Actions_(NLA)_API_(Dynamic)_-_Beta.search_all_actions',

 'Zapier_Natural_Language_Actions_(NLA)_API_(Dynamic)_-_Beta.preview_a_zap',

 'Zapier_Natural_Language_Actions_(NLA)_API_(Dynamic)_-_Beta.get_configuration_link',

 'Zapier_Natural_Language_Actions_(NLA)_API_(Dynamic)_-_Beta.list_exposed_actions',

 'SchoolDigger_API_V2.0.Autocomplete_GetSchools',

 'SchoolDigger_API_V2.0.Districts_GetAllDistricts2',

 'SchoolDigger_API_V2.0.Districts_GetDistrict2',

 'SchoolDigger_API_V2.0.Rankings_GetSchoolRank2',

 'SchoolDigger_API_V2.0.Rankings_GetRank_District',

 'SchoolDigger_API_V2.0.Schools_GetAllSchools20',

 'SchoolDigger_API_V2.0.Schools_GetSchool20',

 'Speak.translate',

 'Speak.explainPhrase',

 'Speak.explainTask']



```


```
tools = get_tools("what shirts can i buy?")

[t.name for t in tools]



```
```
['Open_AI_Klarna_product_Api.productsUsingGET',

 'Milo.askMilo',

 'Zapier_Natural_Language_Actions_(NLA)_API_(Dynamic)_-_Beta.search_all_actions',

 'Zapier_Natural_Language_Actions_(NLA)_API_(Dynamic)_-_Beta.preview_a_zap',

 'Zapier_Natural_Language_Actions_(NLA)_API_(Dynamic)_-_Beta.get_configuration_link',

 'Zapier_Natural_Language_Actions_(NLA)_API_(Dynamic)_-_Beta.list_exposed_actions',

 'SchoolDigger_API_V2.0.Autocomplete_GetSchools',

 'SchoolDigger_API_V2.0.Districts_GetAllDistricts2',

 'SchoolDigger_API_V2.0.Districts_GetDistrict2',

 'SchoolDigger_API_V2.0.Rankings_GetSchoolRank2',

 'SchoolDigger_API_V2.0.Rankings_GetRank_District',

 'SchoolDigger_API_V2.0.Schools_GetAllSchools20',

 'SchoolDigger_API_V2.0.Schools_GetSchool20']



```

提示模板[#](#prompt-template  "Permalink to this headline")
-------------



提示模板非常标准，因为我们实际上并没有改变太多的逻辑在实际提示模板中，而是改变了检索方式。




```

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



自定义提示模板现在有了 tools_getter 的概念，我们在输入中调用它来选择要使用的工具




```

from typing import Callable

# Set up a prompt template

class CustomPromptTemplate(StringPromptTemplate):

    # The template to use

    template: str

    ############## NEW ######################

    # The list of tools available

    tools_getter: Callable

    

    def format(self, \*\*kwargs) -> str:

        # Get the intermediate steps (AgentAction, Observation tuples)

        # Format them in a particular way

        intermediate_steps = kwargs.pop("intermediate_steps")

        thoughts = ""

        for action, observation in intermediate_steps:

            thoughts += action.log

            thoughts += f"Observation: {observation}Thought: "

        # Set the agent_scratchpad variable to that value

        kwargs["agent_scratchpad"] = thoughts

        ############## NEW ######################

        tools = self.tools_getter(kwargs["input"])

        # Create a tools variable from the list of tools provided

        kwargs["tools"] = "".join([f"{tool.name}: {tool.description}" for tool in tools])

        # Create a list of tool names for the tools provided

        kwargs["tool_names"] = ", ".join([tool.name for tool in tools])

        return self.template.format(\*\*kwargs)



```



```

prompt = CustomPromptTemplate(

    template=template,

    tools_getter=get_tools,

    # This omits the `agent_scratchpad`, `tools`, and `tool_names` variables because those are generated dynamically

    # This includes the `intermediate_steps` variable because that is needed

    input_variables=["input", "intermediate_steps"]

)



```

输出解析器
---------------------------------





输出解析器与之前的文档没有改变，因为我们没有改变任何关于输出格式的内容。




```

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

        regex = r"Action\s\*\d\*\s\*:(.\*?)Action\s\*\d\*\s\*Input\s\*\d\*\s\*:[\s]\*(.\*)"

        match = re.search(regex, llm_output, re.DOTALL)

        if not match:

            raise ValueError(f"Could not parse LLM output: `{llm_output}`")

        action = match.group(1).strip()

        action_input = match.group(2)

        # Return the action and action input

        return AgentAction(tool=action, tool_input=action_input.strip(" ").strip('"'), log=llm_output)



```



```

output_parser = CustomOutputParser()



```

设置 LLM 停止序列和代理
---------------------------------


同前。





```

llm = OpenAI(temperature=0)



```



```

# LLM chain consisting of the LLM and a prompt

llm_chain = LLMChain(llm=llm, prompt=prompt)



```



```

tool_names = [tool.name for tool in tools]

agent = LLMSingleActionAgent(

    llm_chain=llm_chain, 

    output_parser=output_parser,

    stop=["Observation:"], 

    allowed_tools=tool_names

)



```





使用代理[#](#use-the-agent  "Permalink to this headline")
---------------------------------


现在我们可以使用它了！





```
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)



```


```
agent_executor.run("what shirts can i buy?")



```
```
> Entering new AgentExecutor chain...

Thought: I need to find a product API

Action: Open_AI_Klarna_product_Api.productsUsingGET

Action Input: shirts



Observation:I found 10 shirts from the API response. They range in price from $9.99 to $450.00 and come in a variety of materials, colors, and patterns. I now know what shirts I can buy

Final Answer: Arg, I found 10 shirts from the API response. They range in price from $9.99 to $450.00 and come in a variety of materials, colors, and patterns.



> Finished chain.



```




```
'Arg, I found 10 shirts from the API response. They range in price from $9.99 to $450.00 and come in a variety of materials, colors, and patterns.'



```


