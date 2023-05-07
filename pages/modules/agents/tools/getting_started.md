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

* 工具名称：LLM用来引用该工具的名称。
* 工具描述：传递给LLM的工具描述。
* 注意事项：不传递给LLM的工具相关注意事项。
* (Optional) Extra Parameters: What extra parameters are required to initialize this tool.




 List of Tools
 [#](#list-of-tools "Permalink to this headline")
-----------------------------------------------------------------



**python_repl** 



* Tool Name: Python REPL
* Tool Description: A Python shell. Use this to execute python commands. Input should be a valid python command. If you expect output it should be printed out.
* Notes: Maintains state.
* Requires LLM: No



**serpapi** 



* Tool Name: Search
* Tool Description: A search engine. Useful for when you need to answer questions about current events. Input should be a search query.
* Notes: Calls the Serp API and then parses results.
* Requires LLM: No



**wolfram-alpha** 



* Tool Name: Wolfram Alpha
* Tool Description: A wolfram alpha search engine. Useful for when you need to answer questions about Math, Science, Technology, Culture, Society and Everyday Life. Input should be a search query.
* Notes: Calls the Wolfram Alpha API and then parses results.
* Requires LLM: No
* Extra Parameters:
 `wolfram_alpha_appid`
 : The Wolfram Alpha app id.



**requests** 



* Tool Name: Requests
* Tool Description: A portal to the internet. Use this when you need to get specific content from a site. Input should be a specific url, and the output will be all the text on that page.
* Notes: Uses the Python requests module.
* Requires LLM: No



**terminal** 



* Tool Name: Terminal
* Tool Description: Executes commands in a terminal. Input should be valid commands, and the output will be any output from running that command.
* Notes: Executes commands with subprocess.
* Requires LLM: No



**pal-math** 



* Tool Name: PAL-MATH
* Tool Description: A language model that is excellent at solving complex word math problems. Input should be a fully worded hard word math problem.
* Notes: Based on
 [this paper](https://arxiv.org/pdf/2211.10435.pdf) 
 .
* Requires LLM: Yes



**pal-colored-objects** 



* Tool Name: PAL-COLOR-OBJ
* Tool Description: A language model that is wonderful at reasoning about position and the color attributes of objects. Input should be a fully worded hard reasoning problem. Make sure to include all information about the objects AND the final question you want to answer.
* Notes: Based on
 [this paper](https://arxiv.org/pdf/2211.10435.pdf) 
 .
* Requires LLM: Yes



**llm-math** 



* Tool Name: Calculator
* Tool Description: Useful for when you need to answer questions about math.
* Notes: An instance of the
 `LLMMath`
 chain.
* Requires LLM: Yes



**open-meteo-api** 



* Tool Name: Open Meteo API
* Tool Description: Useful for when you want to get weather information from the OpenMeteo API. The input should be a question in natural language that this API can answer.
* Notes: A natural language connection to the Open Meteo API (
 `https://api.open-meteo.com/`
 ), specifically the
 `/v1/forecast`
 endpoint.
* Requires LLM: Yes



**news-api** 



* Tool Name: News API
* Tool Description: Use this when you want to get information about the top headlines of current news stories. The input should be a question in natural language that this API can answer.
* Notes: A natural language connection to the News API (
 `https://newsapi.org`
 ), specifically the
 `/v2/top-headlines`
 endpoint.
* Requires LLM: Yes
* Extra Parameters:
 `news_api_key`
 (your API key to access this endpoint)



**tmdb-api** 



* Tool Name: TMDB API
* Tool Description: Useful for when you want to get information from The Movie Database. The input should be a question in natural language that this API can answer.
* Notes: A natural language connection to the TMDB API (
 `https://api.themoviedb.org/3`
 ), specifically the
 `/search/movie`
 endpoint.
* Requires LLM: Yes
* Extra Parameters:
 `tmdb_bearer_token`
 (your Bearer Token to access this endpoint - note that this is different from the API key)



**google-search** 



* Tool Name: Search
* Tool Description: A wrapper around Google Search. Useful for when you need to answer questions about current events. Input should be a search query.
* Notes: Uses the Google Custom Search API
* Requires LLM: No
* Extra Parameters:
 `google_api_key`
 ,
 `google_cse_id`
* For more information on this, see
 [this page](../../../ecosystem/google_search)



**searx-search** 



* Tool Name: Search
* Tool Description: A wrapper around SearxNG meta search engine. Input should be a search query.
* Notes: SearxNG is easy to deploy self-hosted. It is a good privacy friendly alternative to Google Search. Uses the SearxNG API.
* Requires LLM: No
* Extra Parameters:
 `searx_host`



**google-serper** 



* Tool Name: Search
* Tool Description: A low-cost Google Search API. Useful for when you need to answer questions about current events. Input should be a search query.
* Notes: Calls the
 [serper.dev](https://serper.dev) 
 Google Search API and then parses results.
* Requires LLM: No
* Extra Parameters:
 `serper_api_key`
* For more information on this, see
 [this page](../../../ecosystem/google_serper)



**wikipedia** 



* Tool Name: Wikipedia
* Tool Description: A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, historical events, or other subjects. Input should be a search query.
* Notes: Uses the
 [wikipedia](https://pypi.org/project/wikipedia/) 
 Python package to call the MediaWiki API and then parses results.
* Requires LLM: No
* Extra Parameters:
 `top_k_results`



**podcast-api** 



* Tool Name: Podcast API
* Tool Description: Use the Listen Notes Podcast API to search all podcasts or episodes. The input should be a question in natural language that this API can answer.
* Notes: A natural language connection to the Listen Notes Podcast API (
 `https://www.PodcastAPI.com`
 ), specifically the
 `/search/`
 endpoint.
* Requires LLM: Yes
* Extra Parameters:
 `listen_api_key`
 (your api key to access this endpoint)



**openweathermap-api** 



* Tool Name: OpenWeatherMap
* Tool Description: A wrapper around OpenWeatherMap API. Useful for fetching current weather information for a specified location. Input should be a location string (e.g. ‘London,GB’).
* Notes: A connection to the OpenWeatherMap API (https://api.openweathermap.org), specifically the
 `/data/2.5/weather`
 endpoint.
* Requires LLM: No
* Extra Parameters:
 `openweathermap_api_key`
 (your API key to access this endpoint)





