

Google搜索包装器[#](#google-serper-wrapper "到这个标题的永久链接")
===================================================

本页面介绍如何在LangChain中使用[Serper](https://serper.dev) Google搜索API。Serper是一款低成本的Google搜索API，可用于添加来自Google搜索的答案框、知识图和有机结果数据。它分为两部分：设置和对特定Google Serper包装器的引用。

设置[#](#setup "到这个标题的永久链接")
--------------------------

* 前往[serper.dev](https://serper.dev)注册一个免费账户

* 获取API密钥并将其设置为环境变量(`SERPER_API_KEY`)

包装器[#](#wrappers "到这个标题的永久链接")
------------------------------

### 实用工具[#](#utility "到这个标题的永久链接")

有一个名为GoogleSerperAPIWrapper的工具可以包装 GoogleSerper API。使用以下代码导入此实用程序：

```
from langchain.utilities import GoogleSerperAPIWrapper

```

您可以将其作为Self Ask 链的一部分来使用：

```
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

import os

os.environ["SERPER_API_KEY"] = ""
os.environ['OPENAI_API_KEY'] = ""

llm = OpenAI(temperature=0)
search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search"
    )
]

self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)
self_ask_with_search.run("What is the hometown of the reigning men's U.S. Open champion?")

```

#### Output[#](#output "Permalink to this headline")

```
Entering new AgentExecutor chain...
 Yes.
Follow up: Who is the reigning men's U.S. Open champion?
Intermediate answer: Current champions Carlos Alcaraz, 2022 men's singles champion.
Follow up: Where is Carlos Alcaraz from?
Intermediate answer: El Palmar, Spain
So the final answer is: El Palmar, Spain

> Finished chain.

'El Palmar, Spain'

```

更多关于这个包装器的详细说明，可以参考这个[this notebook](../modules/agents/tools/examples/google_serper).

### Tool[#](#tool "Permalink to this headline")

您还可以将此包装器作为工具轻松地加载到代理中使用。可以使用以下代码完成此操作：



```
from langchain.agents import load_tools
tools = load_tools(["google-serper"])

```

[这里](../modules/agents/tools/getting_started)查看更多信息。

