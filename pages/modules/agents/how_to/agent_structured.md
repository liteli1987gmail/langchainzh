# 返回结构化输出

这个笔记本涵盖了如何让代理程序返回结构化输出。
默认情况下，大多数代理程序返回一个单个字符串。
通常有用的是让代理程序返回更具结构性的内容。


一个很好的例子是一个被要求对一些来源进行问答的代理程序。
假设我们希望代理程序不仅回答问题，还会提供一个使用的来源列表。
然后我们希望我们的输出大致遵循下面的模式：

```python
class Response(BaseModel):
    """对所问问题的最终回应"""
    answer: str = Field(description = "向用户回复的最终答案")
    sources: List[int] = Field(description="包含问题答案的页面块的列表。仅在页面块包含相关信息时包含")
```


在这个笔记本中，我们将学习一个具有检索工具且以正确格式响应的代理程序。

## 创建检索器

在这一部分，我们将进行一些设置工作，以创建我们的检索器，它将在包含“国情咨文”的一些模拟数据上进行检索。重要的是，我们将在每个文档的元数据中添加一个“page_chunk”标签。这只是一些假数据，旨在模拟一个来源字段。实际上，这更可能是文档的URL或路径。


```python
%pip install -qU chromadb langchain langchain-community langchain-openai
```


```python
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
```


```python
# 加载要检索的文档
loader = TextLoader("../../state_of_the_union.txt")
documents = loader.load()

# 将文档分成块
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# 在这里，我们添加了假的来源信息
for i, doc in enumerate(texts):
    doc.metadata["page_chunk"] = i

# 创建我们的检索器
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(texts, embeddings, collection_name="state-of-union")
retriever = vectorstore.as_retriever()
```

## 创建工具

我们现在将创建要提供给代理程序的工具。在这种情况下，我们只有一个 - 包装我们的检索器的工具。


```python
from langchain.tools.retriever import create_retriever_tool

retriever_tool = create_retriever_tool(
    retriever,
    "state-of-union-retriever",
    "查询检索器以获取有关国情咨文的信息",
)
```

## 创建响应模式

在这里，我们将定义响应模式。在这种情况下，我们希望最终答案有两个字段：一个用于“answer”，另一个是“sources”的列表


```python
from typing import List

from langchain_core.pydantic_v1 import BaseModel, Field


class Response(BaseModel):
    """对所问问题的最终回应"""

    answer: str = Field(description="向用户回复的最终答案")
    sources: List[int] = Field(
        description="包含问题答案的页面块的列表。仅在页面块包含相关信息时包含"
    )
```

## 创建自定义解析逻辑

现在我们创建一些自定义解析逻辑。
其工作原理是，我们将“Response”模式传递给OpenAI LLM，通过它们的“functions”参数来调用。
这类似于我们如何传递工具供代理程序使用。

当OpenAI调用“Response”函数时，我们希望将其作为向用户返回的信号。
当OpenAI调用其他任何函数时，我们将其视为工具调用。

因此，我们的解析逻辑具有以下几个块：

- 如果没有调用任何函数，则假定我们应该使用响应来回复用户，因此返回“AgentFinish”
- 如果调用了“Response”函数，则使用该函数的输入（我们的结构化输出）回复用户，因此返回“AgentFinish”
- 如果调用了任何其他函数，则将其视为工具调用，因此返回“AgentActionMessageLog”

请注意，我们使用“AgentActionMessageLog”而不是“AgentAction”，因为它允许我们附加消息日志，以便将来可以将其传递回代理提示。


```python
import json

from langchain_core.agents import AgentActionMessageLog, AgentFinish
```


```python
def parse(output):
    # 如果没有调用任何函数，则返回给用户
    if "function_call" not in output.additional_kwargs:
        return AgentFinish(return_values={"output": output.content}, log=output.content)

    # 解析出函数调用
    function_call = output.additional_kwargs["function_call"]
    name = function_call["name"]
    inputs = json.loads(function_call["arguments"])

    # 如果调用了“Response”函数，则使用函数输入回复用户
    if name == "Response":
        return AgentFinish(return_values=inputs, log=str(function_call))
    # 否则，返回代理操作
    else:
        return AgentActionMessageLog(
            tool=name, tool_input=inputs, log="", message_log=[output]
        )
```

## 创建代理程序

现在我们把所有这些放在一起！这个代理程序的组成部分是：

- 提示：一个简单的提示，包含用户问题的占位符，然后是“agent_scratchpad”（任何中间步骤）
- 工具：我们可以将工具和“Response”格式附加到LLM作为函数
- 格式化scratchpad：为了将中间步骤的“agent_scratchpad”格式化，我们将使用标准的“format_to_openai_function_messages”。这将中间步骤格式化为AIMessages和FunctionMessages。
- 输出解析器：我们将使用上面的自定义解析器来解析LLM的响应
- AgentExecutor：我们将使用标准的AgentExecutor来运行代理-工具-代理-工具...的循环


```python
from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
```


```python
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
```


```python
llm = ChatOpenAI(temperature=0)
```


```python
llm_with_tools = llm.bind_functions([retriever_tool, Response])
```


```python
agent = (
    {
        "input": lambda x: x["input"],
        # 从中间步骤格式化agent scratchpad
        "agent_scratchpad": lambda x: format_to_openai_function_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | parse
)
```


```python
agent_executor = AgentExecutor(tools=[retriever_tool], agent=agent, verbose=True)
```

## 运行代理程序



请注意：以上内容是机器翻译结果，可能存在偏差，仅供参考。=======

We can now run the agent! Notice how it responds with a dictionary with two keys: `answer` and `sources`


```python
agent_executor.invoke(
    {"input": "what did the president say about ketanji brown jackson"},
    return_only_outputs=True,
)
```

    
    
    [1m> Entering new AgentExecutor chain...[0m
    [32;1m[1;3m[0m[36;1m[1;3m今晚。我呼吁参议院：通过《自由选举法》。通过约翰·刘易斯选举权法案。而且你们正在做的时候，通过“披露法”，这样美国人就可以知道谁在资助我们的选举。 
    
    今晚，我想给一个致力于为这个国家服务的人致敬：司法部史蒂芬·布雷耶尔（Stephen Breyer）-一名陆军老兵，宪法学者，美国最高法院即将退休的法官。司法部布雷耶尔，感谢您的服务。 
    
    总统拥有的最严肃的宪法责任之一是提名某人为美国最高法院法官。 
    
    就在4天前，也就是我提名上诉法院法官凯坦吉·布朗·杰克逊（Ketanji Brown Jackson）担任法官的时候。她是我国最优秀的法律思想家之一，将继续延续布雷耶尔司法部的优秀传统。
    
    对于我们的 LGBTQ+ 美国人，让我们最终把两党共识的《平等法案》交到我的桌子上。针对变性美国人及其家庭的一连串州法违背了道义。 
    
    正如我去年所说，尤其是对我们年轻的跨性别美国人，作为你们的总统，我永远支持你们，这样你们可以做自己，并发挥上帝赋予你们的潜力。 
    
    尽管看起来我们永远不会达成一致，但那并不是真的。我去年签署了80项两党法案。从防止政府停摆到保护仍然普遍存在的针对亚裔美国人的仇恨犯罪，再到改革军事司法。 
    
    而且很快，我们将加强我30年前首次起草的《打击妇女暴力法》。对我们来说，向这个国家展示我们可以团结起来，做大事是很重要的。 
    
    因此，今晚我提供了一个全国统一议程。四件我们可以共同做的大事。  
    
    首先，战胜阿片类药物滥用。
    
    让我们第一夫人，副总统，内阁成员。最高法院法官。我国同胞们。  
    
    去年新冠疫情让我们分开。今年我们终于再次团聚。 
    
    今晚，我们作为民主党人、共和党人和独立人士相聚。但最重要的是作为美国人。 
    
    有一个互相责任的义务，对美国人民，对宪法。 
    
    并且始终坚信自由将永远战胜暴政。 
    
    六天前，俄罗斯的弗拉基米尔·普京试图动摇自由世界的基础，以为他可以让其屈从于他威胁的方式。但他严重误判了。 
    
    他以为可以进入乌克兰，而世界会屈服。相反，他遇到了他从未想象的一堵坚固墙。 
    
    他遇到了乌克兰人。 
    
    从泽连斯基总统到每一名乌克兰人，他们的无畏，勇气和决心激励着世界。
    
    一位从事私人律师执业的前高级诉讼律师。前联邦公共辩护人。出自公立学校教育工作者和警察家庭。一个共识建设者。自提名以来，她得到了广泛的支持-从警察工会到民主党和共和党任命的前法官。 
    
    如果我们要促进自由和正义，我们需要确保边境安全和修复移民系统。 
    
    我们可以两者兼顾。在我们的边境，我们安装了新技术，如尖端扫描仪，以更好地检测毒品走私。  
    
    我们与墨西哥和危地马拉设立了联合巡逻，以抓捕更多的人口贩运者。  
    
    我们正在设立专门的移民法官，以便逃离迫害和暴力的家庭可以更快地审理他们的案件。 
    
    我们正在承诺并支持南美和中美的伙伴承诺接纳更多的难民和确保本国边界安全。[0m[32;1m[1;3m{'arguments': '{\n"answer": "拜登总统提名凯坦吉·布朗·杰克逊（Ketanji Brown Jackson）担任美国最高法院法官，并称她是我国最优秀的法律思想家之一，将继续延续布雷耶尔司法部的优秀传统。",\n"sources": [6]\n}', 'name': 'Response'}[0m
    
    [1m> Finished chain.[0m
    




    {'answer': "拜登总统提名凯坦吉·布朗·杰克逊（Ketanji Brown Jackson）担任美国最高法院法官，并称她是我国最优秀的法律思想家之一，将继续延续布雷耶尔司法部的优秀传统。",
     'sources': [6]}






