import asyncio
import requests
import json


# 这个模板为腾讯云函数
def getapi(encontent):
    url = 'https://api.openai.com/v1/chat/completions'
    # url = 'https://service-k31jp0z6-1317488882.usw.apigw.tencentcs.com/v1/chat/completions'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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" 
    }
    p = """
    请将以下markdown格式的内容，翻译为中文，代码块不用翻译，请保持markdown格式输出。需要翻译的内容是：
    """ + encontent
    payload = {
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": p}],
     "temperature": 0.7
   }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response)
    return response.json()['choices'][0]['message']['content']
    # print(type(res)) IS requests.models.Response
    # return res
    # error: print(response.json()['message'])为报错内容
    # ok response

encnt = """
# Agent Types

Agents use an LLM to determine which actions to take and in what order.
An action can either be using a tool and observing its output, or returning a response to the user.
Here are the agents available in LangChain.

## `zero-shot-react-description`

This agent uses the ReAct framework to determine which tool to use
based solely on the tool's description. Any number of tools can be provided.
This agent requires that a description is provided for each tool.

## `react-docstore`

This agent uses the ReAct framework to interact with a docstore. Two tools must
be provided: a `Search` tool and a `Lookup` tool (they must be named exactly as so).
The `Search` tool should search for a document, while the `Lookup` tool should lookup
a term in the most recently found document.
This agent is equivalent to the
original [ReAct paper](https://arxiv.org/pdf/2210.03629.pdf), specifically the Wikipedia example.

## `self-ask-with-search`

This agent utilizes a single tool that should be named `Intermediate Answer`.
This tool should be able to lookup factual answers to questions. This agent
is equivalent to the original [self ask with search paper](https://ofir.io/self-ask.pdf),
where a Google search API was provided as the tool.

### `conversational-react-description`

This agent is designed to be used in conversational settings.
The prompt is designed to make the agent helpful and conversational.
It uses the ReAct framework to decide which tool to use, and uses memory to remember the previous conversation interactions.
"""

async def main():
    resu = getapi(encnt)
    print(resu)
    # for i in range(1):
    #     await asyncio.sleep(5)
    #     resu = getapi()
    #     print(resu)
        # generate_blog_post()


if __name__ == '__main__':
    asyncio.run(main())
