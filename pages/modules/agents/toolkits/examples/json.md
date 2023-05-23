# JSON代理[#](#json-agent "Permalink to this headline")

本教程展示了一个代理，旨在与大型JSON/dict对象进行交互。

当您想回答关于JSON blob的问题时，它非常有用，而此JSON blob过大，无法放入LLM的上下文窗口中。

代理能够迭代地探索blob以找到需要回答用户问题的内容。

在下面的示例中，我们使用OpenAI API的OpenAPI规范，可以在此处找到：[https://github.com/openai/openai-openapi/blob/master/openapi.yaml](https://github.com/openai/openai-openapi/blob/master/openapi.yaml)。

我们将使用JSON代理回答有关API规范的一些问题。

初始化
[#](#initialization "Permalink to this headline")
--------------------------------------------------






``` python
import os
import yaml

from langchain.agents import (
    create_json_agent,
    AgentExecutor
)
from langchain.agents.agent_toolkits import JsonToolkit
from langchain.chains import LLMChain
from langchain.llms.openai import OpenAI
from langchain.requests import TextRequestsWrapper
from langchain.tools.json.tool import JsonSpec
 ``` 







``` python
with open("openai_openapi.yml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
json_spec = JsonSpec(dict_=data, max_value_length=4000)
json_toolkit = JsonToolkit(spec=json_spec)

json_agent_executor = create_json_agent(
    llm=OpenAI(temperature=0),
    toolkit=json_toolkit,
    verbose=True
)
 ``` 






示例：获取请求所需的POST参数 
 [#](#example-getting-the-required-post-parameters-for-a-request "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------






``` python
json_agent_executor.run("What are the required parameters in the request body to the /completions endpoint?")
 ``` 





``` python
> Entering new AgentExecutor chain...
Action: json_spec_list_keys
Action Input: data
Observation: ['openapi', 'info', 'servers', 'tags', 'paths', 'components', 'x-oaiMeta']
Thought: I should look at the paths key to see what endpoints exist
Action: json_spec_list_keys
Action Input: data["paths"]
Observation: ['/engines', '/engines/{engine_id}', '/completions', '/edits', '/images/generations', '/images/edits', '/images/variations', '/embeddings', '/engines/{engine_id}/search', '/files', '/files/{file_id}', '/files/{file_id}/content', '/answers', '/classifications', '/fine-tunes', '/fine-tunes/{fine_tune_id}', '/fine-tunes/{fine_tune_id}/cancel', '/fine-tunes/{fine_tune_id}/events', '/models', '/models/{model}', '/moderations']
Thought: I should look at the /completions endpoint to see what parameters are required
Action: json_spec_list_keys
Action Input: data["paths"]["/completions"]
Observation: ['post']
Thought: I should look at the post key to see what parameters are required
Action: json_spec_list_keys
Action Input: data["paths"]["/completions"]["post"]
Observation: ['operationId', 'tags', 'summary', 'requestBody', 'responses', 'x-oaiMeta']
Thought: I should look at the requestBody key to see what parameters are required
Action: json_spec_list_keys
Action Input: data["paths"]["/completions"]["post"]["requestBody"]
Observation: ['required', 'content']
Thought: I should look at the required key to see what parameters are required
Action: json_spec_get_value
Action Input: data["paths"]["/completions"]["post"]["requestBody"]["required"]
Observation: True
Thought: I should look at the content key to see what parameters are required
Action: json_spec_list_keys
Action Input: data["paths"]["/completions"]["post"]["requestBody"]["content"]
Observation: ['application/json']
Thought: I should look at the application/json key to see what parameters are required
Action: json_spec_list_keys
Action Input: data["paths"]["/completions"]["post"]["requestBody"]["content"]["application/json"]
Observation: ['schema']
Thought: I should look at the schema key to see what parameters are required
Action: json_spec_list_keys
Action Input: data["paths"]["/completions"]["post"]["requestBody"]["content"]["application/json"]["schema"]
Observation: ['$ref']
Thought: I should look at the $ref key to see what parameters are required
Action: json_spec_get_value
Action Input: data["paths"]["/completions"]["post"]["requestBody"]["content"]["application/json"]["schema"]["$ref"]
Observation: #/components/schemas/CreateCompletionRequest
Thought: I should look at the CreateCompletionRequest schema to see what parameters are required
Action: json_spec_list_keys
Action Input: data["components"]["schemas"]["CreateCompletionRequest"]
Observation: ['type', 'properties', 'required']
Thought: I should look at the required key to see what parameters are required
Action: json_spec_get_value
Action Input: data["components"]["schemas"]["CreateCompletionRequest"]["required"]
Observation: ['model']
Thought: I now know the final answer
Final Answer: The required parameters in the request body to the /completions endpoint are 'model'.

> Finished chain.
 ``` 



``` python
"The required parameters in the request body to the /completions endpoint are 'model'."
 ``` 






