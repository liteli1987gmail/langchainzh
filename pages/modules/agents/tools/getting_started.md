入门指南
=====================================================================



工具是代理可以用来与世界互动的功能。这些工具可以是通用工具（例如搜索)，其他链，甚至是其他代理。

目前，可以使用以下代码片段加载工具：

```
from langchain.agents import load_tools
tool_names = [...]
tools = load_tools(tool_names)

```

一些工具（例如链、代理)可能需要基础LLM来初始化它们。在这种情况下，也可以传入LLM：

```
from langchain.agents import load_tools
tool_names = [...]
llm = ...
tools = load_tools(tool_names, llm=llm)

```

下面是所有支持的工具及相关信息的列表：

* Tool Name 工具名称：LLM用来引用该工具的名称。
* Notes 工具描述：传递给LLM的工具描述。
* Requires LLM 注意事项：不传递给LLM的工具相关注意事项。
* (Optional) Extra Parameters（可选）附加参数：初始化此工具需要哪些额外参数。




工具列表
 [#](#list-of-tools "Permalink to this headline")
-----------------------------------------------------------------



**python_repl** 



* Tool Name工具名称：Python REPL
* Tool Description工具描述：Python shell。使用它来执行Python命令。输入应为有效的python命令。如果你期望输出，它应该被打印出来。
* Notes注：保持状态
* Requires LLM 需要LLM：没有



**serpapi** 



* Tool工具名称：搜索
* Tool Description工具描述：搜索引擎。当您需要回答有关当前事件的问题时很有用。输入应为搜索查询。
* Notes注意：调用Serp API，然后解析结果。
* Requires LLM 需要LLM：没有



**wolfram-alpha** 



* Tool Name工具名称：Wolfram Alpha
* Tool Description工具描述：Wolfram Alpha搜索引擎当你需要回答有关数学、科学、技术、文化、社会和日常生活的问题时，这很有用。输入应为搜索查询。
* Notes注释：调用Wolfram Alpha API，然后解析结果。
* Requires LLM 需要LLM：没有
* Extra Parameters 额外参数`wolfram_alpha_appid`：Wolfram Alpha应用程序ID。



**requests** 



* Tool Name工具名称：请求
* Tool Description工具描述：互联网的入口。当您需要从网站获取特定内容时，请使用此选项。输入应该是一个特定的URL，输出将是该页面上的所有文本。
* Notes注意：使用Python请求模块。
* Requires LLM需要LLM：没有



**terminal** 



* Tool Name工具名称：terminal终端
* Tool Description工具描述：在终端中执行命令。输入应该是有效的命令，输出将是运行该命令的任何输出。
* Notes注释：执行带有子进程的命令。
* Requires LLM 需要LLM：没有



**pal-math** 



* Tool Name工具名称：PAL-MATH
* Tool Description工具描述：一种语言模型，擅长解决复杂的文字数学问题。输入应该是一个完整的措辞很难字的数学问题。
* Notes注：基于本文。
 [this paper](https://arxiv.org/pdf/2211.10435.pdf) 
 .
* Requires LLM 需要LLM：是的


**pal-colored-objects** 



* Tool Name 工具名称：PAL-COLOR-OBJ
* Tool Description工具描述：一种语言模型，擅长推理对象的位置和颜色属性。输入应该是一个措辞完整的硬推理问题。确保包括所有关于对象的信息和你想回答的最后一个问题。
* Notes注：基于本文。[this paper](https://arxiv.org/pdf/2211.10435.pdf) 
 .
* Requires LLM 需要LLM：是的



**llm-math** 



* Tool Name工具名称：计算器
* Tool Description工具描述：当你需要回答有关数学的问题时很有用。
* Notes注释： LLMMath 链的实例。
* Requires LLM 需要LLM：是的



**open-meteo-api** 



* Tool Name工具名称：Open Meteo API
* Tool Description工具描述：当你想从OpenMeteo API获取天气信息时很有用。输入应该是这个API可以回答的自然语言问题。
* Notes注：与Open Meteo API（ https://api.open-meteo.com/ ）的自然语言连接，特别是 /v1/forecast 端点。
* Requires LLM:需要LLM：是的



**news-api** 



* Tool Name工具名称：新闻API
* Tool Description工具描述：当你想获得当前新闻报道的头条新闻时，使用这个。输入应该是这个API可以回答的自然语言问题
* Notes注：到News API（ https://newsapi.org ）的自然语言连接，特别是` /v2/top-headlines `端点。
* Requires LLM 需要LLM：是的
* Extra Parameters额外参数： `news_api_key` （访问此端点的API密钥）


**tmdb-api** 



* Tool Name工具名称：TMDB API
* Tool Description工具描述：当你想从电影数据库中获取信息时很有用。输入应该是这个API可以回答的自然语言问题。
* Notes: 注：到TMDB API（ https://api.themoviedb.org/3 ）的自然语言连接，特别是 `/search/movie` 端点。
* Requires LLM 需要LLM：是的
* Extra Parameters 额外参数： `tmdb_bearer_token` （访问此端点的承载令牌-请注意，这与API密钥不同）



**google-search** 



* Tool Name工具名称：搜索
* Tool Description工具描述：Google搜索的包装器。当您需要回答有关当前事件的问题时很有用。输入应为搜索查询。
* Notes注意：使用Google自定义搜索API
* Requires LLM 需要LLM：没有
* Extra Parameters额外参数： `google_api_key` 、 `google_cse_id`
* 有关此方面的详细信息，请参阅此页[this page](../../../ecosystem/google_search)



**searx-search** 



* Tool Name工具名称：搜索
* Tool Description工具描述：一个围绕SearxNG元搜索引擎的包装器。输入应为搜索查询。


* Notes注意：SearxNG易于部署自托管。这是一个很好的隐私友好的替代谷歌搜索。使用SearxNG API。
* Requires LLM 需要LLM：没有
* Extra Parameters额外参数： `searx_host`




**google-serper** 



* Tool Name工具名称：搜索
* Tool Description工具描述：一个低成本的Google搜索API。当您需要回答有关当前事件的问题时很有用。输入应为搜索查询。
* Notes注：调用serper.dev Google Search API，然后解析结果。
* Requires LLM  需要LLM：没有

* Extra Parameters 额外参数： serper_api_key
* 有关此方面的详细信息，请参阅此页[this page](../../../ecosystem/google_serper)



**wikipedia** 



* Tool Name工具名称：维基百科
* Tool Description工具描述：维基百科的包装器。当您需要回答有关人员、地点、公司、历史事件或其他主题的一般性问题时很有用。输入应为搜索查询。
* Notes注意：使用wikipedia Python包调用MediaWiki API，然后解析结果。
* Requires LLM  需要LLM：没有


* Extra Parameters额外参数：
 `top_k_results`



**podcast-api** 



* Tool Name工具名称：Podcast API
* Tool Description工具描述：使用Listen Notes Podcast API搜索所有播客或剧集。输入应该是这个API可以回答的自然语言问题。
* Notes：与Listen Notes Podcast API（ https://www.PodcastAPI.com ）的自然语言连接，特别是 /search/ 端点。
* Requires LLM 需要LLM：是的
* Extra Parameters额外参数： `listen_api_key`（访问此端点的API密钥）



**openweathermap-api** 



* Tool Name工具名称：OpenWeatherMap
* Tool Description工具描述：OpenWeatherMap API的包装器。用于获取指定位置的当前天气信息。输入应为位置字符串（例如伦敦，GB）。
* Notes: A connection to the OpenWeatherMap API (https://api.openweathermap.org), specifically the
 `/data/2.5/weather`
 endpoint.
* Requires LLM  需要LLM：没有


* Extra Parameters额外参数： `openweathermap_api_key `（访问此端点的API密钥）





