# 代理程序中的内存

本笔记本介绍了如何给代理程序添加内存。在阅读本笔记本之前，请先阅读以下两个笔记本，因为本笔记本是在这两个笔记本的基础上构建的:

- [LLMChain中的内存](/modules/memory/adding_memory)
- [自定义代理程序](/modules/agents/how_to/custom_agent)

为了给代理程序添加内存，我们需要执行以下步骤:

1. 我们将创建一个带有内存的`LLMChain`。
2. 我们将使用该`LLMChain`来创建一个自定义代理程序。

为了完成这个练习，我们将创建一个简单的自定义代理程序，该代理程序可以访问一个搜索工具，并利用`ConversationBufferMemory`类。

```python
from langchain.agents import AgentExecutor, Tool, ZeroShotAgent
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_openai import OpenAI
```

```python
search = GoogleSearchAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="有助于回答有关当前事件的问题",
    )
]
```

注意在`PromptTemplate`中使用的`chat_history`变量，它与`ConversationBufferMemory`中的动态键名匹配。

```python
prefix = """与人类进行对话，尽力回答以下问题。你可以使用以下工具:"""
suffix = """开始！

{chat_history}
问题: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
    tools,
    prefix=prefix,
    suffix=suffix,
    input_variables=["input", "chat_history", "agent_scratchpad"],
)
memory = ConversationBufferMemory(memory_key="chat_history")
```

现在，我们可以构造带有内存对象的`LLMChain`，然后创建代理程序。

```python
llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
agent_chain = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True, memory=memory
)
```

```python
agent_chain.run(input="加拿大有多少人口?")
```

```
 [1m> 进入新的AgentExecutor链...[0m
 [32;1m[1;3mThought: 我需要找出加拿大的人口数
 行动: 搜索
 行动输入: 加拿大的人口[0m
 观察: [36;1m[1;3m根据最新的联合国数据，加拿大的当前人口截至2022年12月31日星期六为38,566,192人。来自Statistics Canada有关加拿大人口趋势的更多信息可以在其人口和人口统计学门户网站上找到。加拿大的人口 (实际。年度，每个季度和每年的人数估计值，加拿大的省份和地区，这是2021年加拿大人口普查统计了总人口37,991,981，比2016年的数字增长约5.2％。。在1990年至2008年之间，该。... (2)来自国家统计局的人口普查报告和其他统计出版物、(3)联合国、Eurostat:人。统计数据、(4)。加拿大是一个位于北美洲的国家。它的十个省份和三个地区。其总土著人口和每个三...“土著”或“土著”这个词在Statistics Canada已经...2022年6月14日。“决定健康的因素是个人、社会、经济和环境。决定个体和人群。......根据人口统计数据的接种人次分为人口统计数据和激活密钥横跨加拿大和人。大，每周五更新每周十二：00 PM东部时间。[0m
 思考:[32;1m[1;3m现在我知道了最终答案
 最终答案: 加拿大的当前人口截至2022年12月31日星期六为38,566,192人，这是根据最新的联合国数据由世界计量组织解释的结果。[0m
 [1m> 完成AgentExecutor链。[0m
 ```

'The current population of Canada is 38,566,192 as of Saturday, December 31, 2022, based on Worldometer elaboration of the latest United Nations data.'

我们可以测试该代理的记忆功能，我们可以问一个随后的问题，这个问题依赖于之前的交流中的信息才能正确回答。

```python
agent_chain.run(input="他们的国歌叫什么?")
```

```
 [1m> 进入新的AgentExecutor链...[0m
 [32;1m[1;3m思考: 我需要找出加拿大的国歌叫什么。
 行动: 搜索
 行动输入: 加拿大的国歌[0m
 观察: [36;1m[1;3m2010年6月7日... https://twitter.com/CanadaImmigrant加拿大国歌O Canada HQ版 - 包括歌词、字幕、演唱和音乐。歌词:O Canada! 2022年11月23日... 继100年的传统之后，《O Canada》在1980年被宣布为加拿大的国歌。《O Canada》的音乐于1880年由加利昂... O Canada，加拿大的国歌。在1980年7月1日宣布为官方国歌。 "God Save the Queen"仍然是加拿大的皇室国歌...O Canada! 我们的家园和祖陆！真正的爱国者之爱统帅我们所有人。Car ton bras sait porter l'épée,。Il sait porter la croix！《O Canada》（法语：Ô Canada）是加拿大的国歌。该歌曲最初由魁北克的省长代表Théodore Robitaille委托创作...2018年2月1日...这是一个简单的调整——只是两个字。但通过这一点，加拿大刚刚投票成为其国歌“O Canada”性别中立... 《O Canada》在1980年7月1日被宣布为加拿大的国歌，距离1880年6月24日首次演唱已有100年。.音乐。爱国主义音乐在加拿大的历史可以追溯到超过200年，已经。两个诸多国家和地区中首先的法定程序之前...2022年2月4日...英文版：O Canada！我们的家园和土生土产的土地！爱国主义的真爱。我们所有人的命令。我们所有人开心黄。2022年2月1日，加拿大的议会通过了一项使该国的国歌性别中性化的法案。如果你对“O Canada”的歌词不熟悉...[0m
 思考:[32;1m[1;3m现在我知道了最终答案。
 最终答案: 加拿大的国歌叫做“O Canada”。[0m
 [1m> 完成AgentExecutor链。[0m
```

'The national anthem of Canada is called "O Canada".'

我们可以看到，代理记得之前的问题是关于加拿大的，并正确地询问Google搜索加拿大的国歌叫什么。

为了好玩，让我们将其与没有内存的代理进行比较。

```python
prefix = """与人类进行对话，尽力回答以下问题。你有以下工具可用:"""
suffix = """开始!

问题: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
    tools, prefix=prefix, suffix=suffix, input_variables=["input", "agent_scratchpad"]
)
llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
agent_without_memory = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True
)
```

```python
agent_without_memory.run("加拿大有多少人口?")
```

```
 [1m> 进入新的AgentExecutor链...[0m
 [32;1m[1;3m思考: 我需要找出加拿大的人口数
 行动: 搜索
 行动输入: 加拿大的人口[0m
 观察: [36;1m[1;3m根据最新的联合国数据，加拿大的当前人口截至2022年12月31日星期六为38,566,192人。来自Statistics Canada有关加拿大人口趋势的更多信息可以在其人口和人口统计学门户网站上找到。加拿大的人口 (实际。年度，每个季度和每年的人数估计值，加拿大的省份和地区，这是2021年加拿大人口普查统计了总人口37,991,981，比2016年的数字增长约5.2％。。在1990年至2008年之间，该。... (2)来自国家统计局的人口普查报告和其他统计出版物、(3)联合国、Eurostat:人。统计数据、(4)。加拿大是一个位于北美洲的国家。它的十个省份和三个地区。其总土著人口和每个三...“土著”或“土著”这个词在Statistics Canada已经...2022年6月14日。“决定健康的因素是个人、社会、经济和环境。决定个体和人群。......根据人口统计数据的接种人次分为人口统计数据和激活密钥横跨加拿大和人。大，每周五更新每周十二：00 PM东部时间。[0m
 思考:[32;1m[1;3m现在我知道了最终答案
 最终答案: 加拿大的当前人口截至2022年12月31日星期六为38,566,192人，这是根据最新的联合国数据由世界计量组织解释的结果。[0m
 [1m> 完成AgentExecutor链。[0m
```

'The current population of Canada is 38,566,192 as of Saturday, December 31, 2022, based on Worldometer elaboration of the latest United Nations data.'

```python
agent_without_memory.run("他们的国歌叫什么?")
```
```
 [1m> 进入新的AgentExecutor链...[0m
 [32;1m[1;3m思考: 我应该寻找答案
 行动: 搜索
 行动输入: 国歌 of [country][0m
 观察: [36;1m[1;3m大多数国家都有一首国歌，定义为“一首赞美、奉献或爱国主义的歌曲”。大多数国歌的风格要么是进行曲要么是赞美诗。 具有其国歌的世界各国清单。...用国家的语言和英文翻译的标题和歌词，2021年8月1日...阿富汗，“Milli Surood” (国歌) · 2. 亚美尼亚，“Mer Hayrenik” (我们的祖国) · 3. 阿塞拜疆(一个跨大陆的国家 ... 国歌是一首代表和唤起对一个国家或民族历史和传统的颂扬的爱国音乐作品。每个国家的国歌；斐济，“Meda Dau Doka” (“上帝保佑斐济”)；芬兰，“Maamme”。 （“我们的土地”）；法国，“La Marseillaise” （“马赛曲”）。你可以在上面的菜单中按照字母顺序找到国歌，也可以使用搜索功能。本网站侧重于对国歌进行学术研究...2022年2月13日...38岁的乡村音乐艺术家在今年的大型比赛中有幸演唱国歌，她表现出色。世界最古老的国歌；法国，La Marseillaise，1795；阿根廷，Himno Nacional Argentino（阿根廷国歌）...2022年3月3日...乡村音乐明星杰西杰姆斯德克以一种令人瞠目的方式赢得了音乐和曲棍球迷的尊重，她深情演唱了奉献给美国国歌《星条旗》中的片段...该列表显示的国家在左侧，国歌在...世界上有许多国家拥有自己的国歌。[0m
 思考:[32;1m[1;3m现在我知道了最终答案
 最终答案: [国家的国歌]的国歌叫做[name of anthem]。[0m
 [1m> 完成AgentExecutor链。[0m
```

'The national anthem of [country] is [name of anthem].'

我们可以看到，不带内存的代理使用相同的输入，但无法记住之前的交流。

结果表明，通过添加内存，代理程序可以记住对话的历史，从而在后续的交谈中更多地参考先前的信息。这使得代理程序能够回答依赖于之前的交流的问题，并提供更一致和准确的答案。