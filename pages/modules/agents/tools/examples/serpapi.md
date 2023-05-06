

SerpAPI[#](#serpapi "Permalink to this headline")
=================================================

本笔记介绍如何使用SerpAPI组件搜索网络。

```
from langchain.utilities import SerpAPIWrapper

```

```
search = SerpAPIWrapper()

```

```
search.run("Obama's first name?")

```

```
'Barack Hussein Obama II'

```

自定义参数[#](#custom-parameters "Permalink to this headline")
---------------------------------------------------------

您还可以使用任意参数自定义SerpAPI包装器。例如，在下面的示例中，我们将使用`bing`而不是`google`。

```
params = {
    "engine": "bing",
    "gl": "us",
    "hl": "en",
}
search = SerpAPIWrapper(params=params)

```

```
search.run("Obama's first name?")

```

```
'Barack Hussein Obama II is an American politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Obama was the first African-American presi…New content will be added above the current area of focus upon selectionBarack Hussein Obama II is an American politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Obama was the first African-American president of the United States. He previously served as a U.S. senator from Illinois from 2005 to 2008 and as an Illinois state senator from 1997 to 2004, and previously worked as a civil rights lawyer before entering politics.Wikipediabarackobama.com'

```

```
from langchain.agents import Tool
# You can create the tool to pass to an agent
repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
    func=search.run,
)

```

