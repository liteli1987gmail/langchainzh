自然语言API
[#](#natural-language-apis "Permalink to this headline")
==================

自然语言API工具包（NLAToolkits)使得LangChain代理可以高效地跨终端点进行调用计划和组合。本教程演示了Speak、Klarna和Spoonacluar API的样例组合。

有关包含在NLAToolkit中的OpenAPI链的详细演练，请参见[OpenAPI操作链](openapi)教程。

首先，导入依赖项并加载LLM
[#](#first-import-dependencies-and-load-the-llm "Permalink to this headline")
------------------------------------------------------------------------------
```  python
from typing import List, Optional
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.requests import Requests
from langchain.tools import APIOperation, OpenAPISpec
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.agents.agent_toolkits import NLAToolkit
```


```  python
# 选择要使用的LLM。在这里，我们使用text-davinci-003
llm = OpenAI(temperature=0, max_tokens=700) #您可以在不同的核心LLM之间切换。
```


接下来，加载自然语言API工具包
[#](#next-load-the-natural-language-api-toolkits "Permalink to this headline")
--------------------------------------------------------------------------------
```  python
speak_toolkit = NLAToolkit.from_llm_and_url(llm, "https://api.speak.com/openapi.yaml")
klarna_toolkit = NLAToolkit.from_llm_and_url(llm, "https://www.klarna.com/us/shopping/public/openai/v0/api-docs/")
```



```  python
尝试加载OpenAPI 3.0.1规范。这可能会导致性能降低。将您的OpenAPI规范转换为3.1.*规范以获得更好的支持。
尝试加载OpenAPI 3.0.1规范。这可能会导致性能降低。将您的OpenAPI规范转换为3.1.*规范以获得更好的支持。
尝试加载OpenAPI 3.0.1规范。这可能会导致性能降低。将您的OpenAPI规范转换为3.1.*规范以获得更好的支持。
```









 创建代理
[#](#create-the-agent "Permalink to this headline")
```  python
#稍微修改默认代理的说明
openapi_format_instructions = """使用以下格式：

问题：您必须回答的输入问题
思考：您应该始终思考要做什么
操作：要采取的操作，应为[{tool_names}]中的一个
操作输入：指示AI操作代表要执行的操作
观察：代理的响应
...（这个思考/操作/操作输入/观察可以重复N次)
思路：我现在知道了最终答案。用户看不到我的任何观察结果，API响应，链接或工具。
最终答案：原始输入问题的最终答案，具有适当的详细信息

在回答最终答案时，请记住，您回答的人无法看到您的任何思考/操作/操作输入/观察结果，因此如果有任何相关信息，您需要在回答中明确包含它。"""
```


```  python
natural_language_tools = speak_toolkit.get_tools() + klarna_toolkit.get_tools()
mrkl = initialize_agent(natural_language_tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
                        verbose=True, agent_kwargs={"format_instructions":openapi_format_instructions})
```



```  python
mrkl.run("I have an end of year party for my Italian class and have to buy some Italian clothes for it")
```



```  python
> Entering new AgentExecutor chain...
 我需要了解哪些意大利服装可用
操作：Open_AI_Klarna_product_Api.productsUsingGET
操作输入：意大利服装
观察：API响应包含两个来自Alé品牌的产品，颜色为意大利蓝色。第一个是Alé Colour Block Short Sleeve Jersey Men - Italian Blue，售价为86.49美元，第二个是Alé Dolid Flash Jersey Men - Italian Blue，售价为40.00美元。
思路：现在我知道哪些意大利服装可用，以及它们的价格。
最终答案：您可以为您义大利班的年终派对购买两种颜色为意大利蓝色的Alé品牌产品。Alé Colour Block Short Sleeve Jersey Men - Italian Blue售价为86.49美元，Alé Dolid Flash Jersey Men - Italian Blue售价为40.00美元。

> 链结束。
```


```  python
'您可以为您义大利班的年终派对购买两种颜色为意大利蓝色的Alé品牌产品。Alé Colour Block Short Sleeve Jersey Men - Italian Blue售价为86.49美元，Alé Dolid Flash Jersey Men - Italian Blue售价为40.00美元。'
```




使用Auth + 添加更多终端点
[#](#using-auth-adding-more-endpoints "Permalink to this headline")
========================================

某些终端点可能需要用户通过访问令牌等进行身份验证。在这里，我们展示如何通过`Requests`包装器对象传递验证信息。

由于每个NLATool都向其包装的API公开简洁的自然语言接口，因此顶层对话代理的工作更容易，可以将每个终端点合并到满足用户请求的代理中。


**添加Spoonacular终端点。**


1. 登录[Spoonacular API控制台](https://spoonacular.com/food-api/console#Profile)并注册一个免费帐户。
2. 单击“Profile”，然后在下面复制您的API密钥。






```  python
spoonacular_api_key = "" # Copy from the API Console
```










```  python
requests = Requests(headers={"x-api-key": spoonacular_api_key})
spoonacular_toolkit = NLAToolkit.from_llm_and_url(
    llm, 
    "https://spoonacular.com/application/frontend/downloads/spoonacular-openapi-3.json",
    requests=requests,
    max_text_length=1800, # If you want to truncate the response text
)
```








```  python
Attempting to load an OpenAPI 3.0.0 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.
Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter
Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter
```










```  python
natural_language_api_tools = (speak_toolkit.get_tools() 
                              + klarna_toolkit.get_tools() 
                              + spoonacular_toolkit.get_tools()[:30]
                             )
print(f"{len(natural_language_api_tools)} tools loaded.")
```








```  python34 tools loaded.
```










```  python
# Create an agent with the new tools
mrkl = initialize_agent(natural_language_api_tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
                        verbose=True, agent_kwargs={"format_instructions":openapi_format_instructions})
```










```  python
# Make the query more complex!
user_input = (
    "I'm learning Italian, and my language class is having an end of year party... "
    " Could you help me find an Italian outfit to wear and"
    " an appropriate recipe to prepare so I can present for the class in Italian?"
)
```










```  python
mrkl.run(user_input)
```








```  python
> Entering new AgentExecutor chain...
 I need to find a recipe and an outfit that is Italian-themed.
Action: spoonacular_API.searchRecipes
Action Input: Italian
Observation: The API response contains 10 Italian recipes, including Turkey Tomato Cheese Pizza, Broccolini Quinoa Pilaf, Bruschetta Style Pork & Pasta, Salmon Quinoa Risotto, Italian Tuna Pasta, Roasted Brussels Sprouts With Garlic, Asparagus Lemon Risotto, Italian Steamed Artichokes, Crispy Italian Cauliflower Poppers Appetizer, and Pappa Al Pomodoro.
Thought: I need to find an Italian-themed outfit.
Action: Open_AI_Klarna_product_Api.productsUsingGET
Action Input: Italian
Observation: I found 10 products related to 'Italian' in the API response. These products include Italian Gold Sparkle Perfectina Necklace - Gold, Italian Design Miami Cuban Link Chain Necklace - Gold, Italian Gold Miami Cuban Link Chain Necklace - Gold, Italian Gold Herringbone Necklace - Gold, Italian Gold Claddagh Ring - Gold, Italian Gold Herringbone Chain Necklace - Gold, Garmin QuickFit 22mm Italian Vacchetta Leather Band, Macy's Italian Horn Charm - Gold, Dolce & Gabbana Light Blue Italian Love Pour Homme EdT 1.7 fl oz.
Thought: I now know the final answer.
Final Answer: To present for your Italian language class, you could wear an Italian Gold Sparkle Perfectina Necklace - Gold, an Italian Design Miami Cuban Link Chain Necklace - Gold, or an Italian Gold Miami Cuban Link Chain Necklace - Gold. For a recipe, you could make Turkey Tomato Cheese Pizza, Broccolini Quinoa Pilaf, Bruschetta Style Pork & Pasta, Salmon Quinoa Risotto, Italian Tuna Pasta, Roasted Brussels Sprouts With Garlic, Asparagus Lemon Risotto, Italian Steamed Artichokes, Crispy Italian Cauliflower Poppers Appetizer, or Pappa Al Pomodoro.

> Finished chain.
```






```  python
'To present for your Italian language class, you could wear an Italian Gold Sparkle Perfectina Necklace - Gold, an Italian Design Miami Cuban Link Chain Necklace - Gold, or an Italian Gold Miami Cuban Link Chain Necklace - Gold. For a recipe, you could make Turkey Tomato Cheese Pizza, Broccolini Quinoa Pilaf, Bruschetta Style Pork & Pasta, Salmon Quinoa Risotto, Italian Tuna Pasta, Roasted Brussels Sprouts With Garlic, Asparagus Lemon Risotto, Italian Steamed Artichokes, Crispy Italian Cauliflower Poppers Appetizer, or Pappa Al Pomodoro.'
```









 Thank you!
 [#](#thank-you "Permalink to this headline")
----------------------------------------------------------






```  python
natural_language_api_tools[1].run("Tell the LangChain audience to 'enjoy the meal' in Italian, please!")
```








```  python
"In Italian, you can say 'Buon appetito' to someone to wish them to enjoy their meal. This phrase is commonly used in Italy when someone is about to eat, often at the beginning of a meal. It's similar to saying 'Bon appétit' in French or 'Guten Appetit' in German."
```









