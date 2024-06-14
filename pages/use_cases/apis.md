# 与API互动

[![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/use_cases/apis.ipynb)

## 实例

假设您想要一个LLM与外部API进行交互。

这对于获取LLM可以利用的背景非常有用。

此外，它还允许我们使用自然语言与API进行交互！

## 概述

有两种将LLM与外部API进行接口的主要方式：

* `函数`：例如，[OpenAI函数](https://platform.openai.com/docs/guides/gpt/function-calling)是一种常用的方法。
* `通过LLM生成的接口`：使用具有API文档访问权限的LLM创建接口。

![图像说明](/img/api_use_case.png)

## 快速入门

许多API已经与OpenAI函数调用兼容。

例如，Klarna有一个描述其API并允许OpenAI与其交互的YAML文件：

```
https://www.klarna.com/us/shopping/public/openai/v0/api-docs/
```

其他选项包括：

* [Speak](https://api.speak.com/openapi.yaml)用于翻译
* [XKCD](https://gist.githubusercontent.com/roaldnefs/053e505b2b7a807290908fe9aa3e1f00/raw/0a212622ebfef501163f91e23803552411ed00e4/openapi.yaml)用于漫画

我们可以直接提供规范给 `get_openapi_chain`，以便使用OpenAI函数查询API：


```python
pip install langchain langchain-openai 

# 设置 OPENAI_API_KEY 环境变量或从 .env 文件加载：
# import dotenv
# dotenv.load_dotenv()
```


```python
from langchain.chains.openai_functions.openapi import get_openapi_chain

chain = get_openapi_chain(
    "https://www.klarna.com/us/shopping/public/openai/v0/api-docs/"
)
chain("What are some options for a men's large blue button down shirt")
```

    正在尝试加载 OpenAPI 3.0.1 规范。这可能会导致性能下降。将您的 OpenAPI 规范转换为 3.1.* 规范以获得更好的支持。
    




    {'query': "What are some options for a men's large blue button down shirt",
     'response': {'products': [{'name': 'Cubavera Four Pocket Guayabera Shirt',
        'url': 'https://www.klarna.com/us/shopping/pl/cl10001/3202055522/Clothing/Cubavera-Four-Pocket-Guayabera-Shirt/?utm_source=openai&ref-site=openai_plugin',
        'price': '$13.50',
        'attributes': ['Material:Polyester,Cotton',
         'Target Group:Man',
         'Color:Red,White,Blue,Black',
         'Properties:Pockets',
         'Pattern:Solid Color',
         'Size (Small-Large):S,XL,L,M,XXL']},
       {'name': 'Polo Ralph Lauren Plaid Short Sleeve Button-down Oxford Shirt',
        'url': 'https://www.klarna.com/us/shopping/pl/cl10001/3207163438/Clothing/Polo-Ralph-Lauren-Plaid-Short-Sleeve-Button-down-Oxford-Shirt/?utm_source=openai&ref-site=openai_plugin',
        'price': '$52.20',
        'attributes': ['Material:Cotton',
         'Target Group:Man',
         'Color:Red,Blue,Multicolor',
         'Size (Small-Large):S,XL,L,M,XXL']},
       {'name': 'Brixton Bowery Flannel Shirt',
        'url': 'https://www.klarna.com/us/shopping/pl/cl10001/3202331096/Clothing/Brixton-Bowery-Flannel-Shirt/?utm_source=openai&ref-site=openai_plugin',
        'price': '$27.48',
        'attributes': ['Material:Cotton',
         'Target Group:Man',
         'Color:Gray,Blue,Black,Orange',
         'Properties:Pockets',
         'Pattern:Checkered',
         'Size (Small-Large):XL,3XL,4XL,5XL,L,M,XXL']},
       {'name': 'Vineyard Vines Gingham On-The-Go brrr Classic Fit Shirt Crystal',
        'url': 'https://www.klarna.com/us/shopping/pl/cl10001/3201938510/Clothing/Vineyard-Vines-Gingham-On-The-Go-brrr-Classic-Fit-Shirt-Crystal/?utm_source=openai&ref-site=openai_plugin',
        'price': '$80.64',
        'attributes': ['Material:Cotton',
         'Target Group:Man',
         'Color:Blue',
         'Size (Small-Large):XL,XS,L,M']},
       {'name': "Carhartt Men's Loose Fit Midweight Short Sleeve Plaid Shirt",
        'url': 'https://www.klarna.com/us/shopping/pl/cl10001/3201826024/Clothing/Carhartt-Men-s-Loose-Fit-Midweight-Short-Sleeve-Plaid-Shirt/?utm_source=openai&ref-site=openai_plugin',
        'price': '$17.99',
        'attributes': ['Material:Cotton',
         'Target Group:Man',
         'Color:Red,Brown,Blue,Green',
         'Properties:Pockets',
         'Pattern:Checkered',
         'Size (Small-Large):S,XL,L,M']}]}}



## 函数

我们可以解析使用函数调用外部API时发生的情况。

让我们看一下[LangSmith跟踪](https://smith.langchain.com/public/76a58b85-193f-4eb7-ba40-747f0d5dd56e/r)：

* 请注意，我们在供应API规范时调用了OpenAI LLM：

```
https://www.klarna.com/us/shopping/public/openai/v0/api-docs/
```

* 然后，提示告诉LLM使用带有输入问题的API规范：

```
使用提供的API响应此用户查询：
What are some options for a men's large blue button down shirt
```

* LLM返回函数调用的参数`productsUsingGET`，该函数在提供的API规范中指定：

```
function_call：
  name：productsUsingGET
  arguments：|-
    {
      "params"：{
        "countryCode"："US"，
        "q"："men's large blue button down shirt"，
        "size"：5，
        "min_price"：0，
        "max_price"：100
      }
    }
 ```

![Image description](/img/api_function_call.png)

* [上面](https://github.com/langchain-ai/langchain/blob/7fc07ba5df99b9fa8bef837b0fafa220bc5c932c/libs/langchain/langchain/chains/openai_functions/openapi.py#L215)我们对API进行了调用。 
=======
### 深入了解

**使用其他API进行测试**


```python
import os

os.environ["TMDB_BEARER_TOKEN"] = ""
from langchain.chains.api import tmdb_docs

headers = {"Authorization": f"Bearer {os.environ['TMDB_BEARER_TOKEN']}"}
chain = APIChain.from_llm_and_api_docs(
    llm,
    tmdb_docs.TMDB_DOCS,
    headers=headers,
    verbose=True,
    limit_to_domains=["https://api.themoviedb.org/"],
)
chain.run("搜索 'Avatar'")
```


```python
import os

from langchain.chains import APIChain
from langchain.chains.api import podcast_docs
from langchain_openai import OpenAI

listen_api_key = "xxx"  # 在这里获取API密钥: https://www.listennotes.com/api/pricing/
llm = OpenAI(temperature=0)
headers = {"X-ListenAPI-Key": listen_api_key}
chain = APIChain.from_llm_and_api_docs(
    llm,
    podcast_docs.PODCAST_DOCS,
    headers=headers,
    verbose=True,
    limit_to_domains=["https://listen-api.listennotes.com/"],
)
chain.run(
    "搜索 'silicon valley bank' 播客剧集，音频长度超过30分钟，只返回1个结果"
)
```

**网络请求**

URL请求是一种非常常见的用例，我们有`LLMRequestsChain`专门进行HTTP GET请求。


```python
from langchain.chains import LLMChain, LLMRequestsChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
```


```python
template = """在 >>> 和 <<< 之间是从谷歌获得的原始搜索结果文本。
提取与问题 '{query}' 相关的答案，如果信息中不包含答案则返回 "not found"。
使用以下格式
Extracted:<answer or "not found">
>>> {requests_result} <<<
Extracted:"""

PROMPT = PromptTemplate(
    input_variables=["query", "requests_result"],
    template=template,
)
```


```python
chain = LLMRequestsChain(llm_chain=LLMChain(llm=OpenAI(temperature=0), prompt=PROMPT))
question = "三个最大的国家及其各自的面积是什么？"
inputs = {
    "query": question,
    "url": "https://www.google.com/search?q=" + question.replace(" ", "+"),
}
chain(inputs)
```




    {'query': '三个最大的国家及其各自的面积是什么？',
     'url': 'https://www.google.com/search?q=三个最大的国家及其各自的面积是什么？',
     'output': ' 俄罗斯（17,098,242平方公里），加拿大（9,984,670平方公里），中国（9,706,961平方公里）'}


