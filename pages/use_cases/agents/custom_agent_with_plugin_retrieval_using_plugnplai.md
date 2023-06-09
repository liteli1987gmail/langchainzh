

即插即用[#](#plug-and-plai "跳到此标题的永久链接")
======================


此文档建立在[工具检索](custom_agent_with_plugin_retrieval.html)的基础上，但从`plugnplai`中获取所有工具-一个人工智能插件目录。



设置环境[#](#set-up-environment "跳到此标题的永久链接")
-------------------


导入所需的内容， 等等。


安装plugnplai lib以从https://plugplai.com目录获取活动插件列表





```
pip install plugnplai -q



```
```
[notice] A new release of pip available: 22.3.1 -> 23.1.1

[notice] To update, run: pip install --upgrade pip

Note: you may need to restart the kernel to use updated packages.



```


```
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser

from langchain.prompts import StringPromptTemplate

from langchain import OpenAI, SerpAPIWrapper, LLMChain

from typing import List, Union

from langchain.schema import AgentAction, AgentFinish

from langchain.agents.agent_toolkits import NLAToolkit

from langchain.tools.plugin import AIPlugin

import re

import plugnplai



```

设置LLM[#](#setup-llm "跳到此标题的永久链接")
-------------------------





```
llm = OpenAI(temperature=0)



```

设置插件[#](#set-up-plugins "跳到此标题的永久链接")
-----------------------------------


加载和索引插件





```
# Get all plugins from plugnplai.com

urls = plugnplai.get_plugins()



# Get ChatGPT plugins - only ChatGPT verified plugins

urls = plugnplai.get_plugins(filter = 'ChatGPT')



# Get working plugins - only tested plugins (in progress)

urls = plugnplai.get_plugins(filter = 'working')





AI_PLUGINS = [AIPlugin.from_url(url + "/.well-known/ai-plugin.json") for url in urls]



```

工具检索[#](#tool-retriever "跳到此标题的永久链接")
-----------------------------------



我们将使用向量存储为每个工具描述创建嵌入。然后，对于传入的查询，我们可以为该查询创建嵌入，并进行相似性搜索以查找相关工具。




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



我们现在可以测试这个检索器，看看它是否有效。




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

提示模板 Prompt Template
-------------

提示模板非常标准，因为实际上我们在实际提示模板中并没有改变太多逻辑，而是只是更改了检索方式。

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



自定义提示模板现在有一个tools_getter的概念，我们在input上调用它来选择要使用的工具。





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



输出解析器[#](#output-parser "Permalink to this headline")
---------------------------------


由于我们不改变输出格式，所以输出解析器与上个文档没有变化。





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

设置LLM停止序列和代理[#](#set-up-llm-stop-sequence-and-the-agent "Permalink to this headline")
---------------------------------


与上个文档相同





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

使用代理[#](#use-the-agent "Permalink to this headline")
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


