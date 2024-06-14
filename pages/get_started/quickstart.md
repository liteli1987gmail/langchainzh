## 快速入门

在这个快速入门中，我们将向您展示如何：
- 设置LangChain、LangSmith和LangServe
- 使用LangChain的最基本和常见的组件：提示模板、模型和输出解析器
- 使用LangChain表达语言，这是LangChain构建的协议，也是组件链接的基础
- 使用LangChain构建一个简单的应用程序
- 使用LangSmith跟踪您的应用程序
- 使用LangServe为您的应用程序提供服务

要涵盖的内容很多！让我们开始吧。

## 设置

### Jupyter Notebook

本指南（以及文档中的大多数其他指南）使用[Jupyter笔记本](https://jupyter.org/)，并假定读者也在使用。Jupyter笔记本非常适合学习如何使用LLM系统，因为往往会出现一些问题（意外输出、API宕机等），通过在交互环境中进行指南可以更好地理解它们。

您不需要在Jupyter笔记本中进行指南，但建议这样做。有关如何安装的说明，请参阅[这里](https://jupyter.org/install)。

### 安装

要安装LangChain，请运行：

```
pip install langchain
```

详细信息请参阅我们的[安装指南](/get_started/installation)。

### LangSmith

您使用LangChain构建的许多应用程序将包含多个步骤，其中使用LLM调用的多个调用。
随着这些应用程序变得越来越复杂，能够检查链路或代理内部发生的情况变得至关重要。
最好的方法是使用[LangSmith](https://smith.langchain.com)。

请注意，LangSmith并非必需，但非常有用。
如果您确实想使用LangSmith，请在上面的链接上注册后，确保设置环境变量以开始记录跟踪：

```shell
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY="..."
```

## 使用LangChain构建

LangChain使其能够将外部数据源和计算与LLM连接起来。
在这个快速入门中，我们将介绍一些不同的方法来实现这一点。
我们将从一个简单的LLM链开始，它只依赖于提示模板中的信息来回复。
接下来，我们将构建一个检索链，该链从单独的数据库获取数据并将其传递到提示模板中。
然后，我们将添加聊天记录，以创建一个对话检索链。这使您可以以聊天方式与此LLM进行交互，因此它会记住以前的问题。
最后，我们将构建一个代理，该代理利用LLM来确定是否需要获取数据来回答问题。
我们将简要介绍这些内容，但是所有这些都有很多细节！我们会链接到相关的文档。

## LLM Chain

我们将展示如何使用API提供的模型，如OpenAI，以及使用Ollama等集成的本地开源模型。

<Tabs>
  <TabItem value="openai" label="OpenAI" default>

首先，我们需要导入LangChain x OpenAI集成包。

```shell
pip install langchain-openai
```

访问API需要一个API密钥，您可以通过创建一个帐户并转到[此处](https://platform.openai.com/account/api-keys)来获取它。一旦我们有了一个密钥，我们希望通过运行以下命令将其设置为环境变量：

```shell
export OPENAI_API_KEY="..."
```

然后，我们可以初始化模型：

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
```

如果您不想设置环境变量，可以在初始化OpenAI LLM类时通过`api_key`命名参数直接传递密钥：

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(api_key="...")
```

  </TabItem>
  <TabItem value="local" label="本地（使用Ollama）">

[Ollama](https://ollama.ai/)允许您在本地运行开源大型语言模型，例如Llama 2。

首先，按照[这些说明](https://github.com/jmorganca/ollama)设置和运行本地Ollama实例：

* [下载](https://ollama.ai/download)
* 通过`ollama pull llama2`获取模型

然后，确保Ollama服务器正在运行。之后，您可以执行以下操作：
```python
from langchain_community.llms import Ollama
llm = Ollama(model="llama2")
```

  </TabItem>
  <TabItem value="anthropic" label="Anthropic">

首先，我们需要导入LangChain x Anthropic包。

```shell
pip install langchain-anthropic
```

访问API需要一个API密钥，您可以通过在[此处](https://claude.ai/login)创建一个帐户来获取它。一旦我们有了一个密钥，我们希望通过运行以下命令将其设置为环境变量：

```shell
export ANTHROPIC_API_KEY="..."
```

然后，我们可以初始化模型：

```python
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.2, max_tokens=1024)
```

如果您不想设置环境变量，可以在初始化Anthropic聊天模型类时通过`api_key`命名参数直接传递密钥：

```python
llm = ChatAnthropic(api_key="...")
```

  </TabItem>
  <TabItem value="cohere" label="Cohere">

首先，我们需要导入Cohere SDK包。

```shell
pip install langchain-cohere
```

访问API需要一个API密钥，您可以通过创建一个帐户并转到[此处](https://dashboard.cohere.com/api-keys)来获取它。一旦我们有了一个密钥，我们希望通过运行以下命令将其设置为环境变量：

```shell
export COHERE_API_KEY="..."
```

然后，我们可以初始化模型：

```python
from langchain_cohere import ChatCohere

llm = ChatCohere()
```

如果您不想设置环境变量，可以在初始化Cohere LLM类时通过`cohere_api_key`命名参数直接传递密钥：

```python
from langchain_cohere import ChatCohere

llm = ChatCohere(cohere_api_key="...")
```

  </TabItem>
</Tabs>

一旦您安装和初始化了您选择的LLM，我们就可以尝试使用它！让我们问它什么是LangSmith - 这是训练数据中没有的内容，所以它应该不会有一个很好的回答。

```python
llm.invoke("how can langsmith help with testing?")
```

我们还可以使用提示模板来指导其回答。
提示模板将原始用户输入转换为更好的输入以供LLM使用。

```python
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])
```

现在，我们可以将它们组合成一个简单的LLM链：

```python
chain = prompt | llm 
```

现在，我们可以调用它并问相同的问题。它仍然不会知道答案，但是它应该以更适合技术作家的方式回答。

```python
chain.invoke({"input": "how can langsmith help with testing?"})
```

ChatModel的输出（因此，也是这个链的输出）是一个消息。然而，使用字符串更方便。让我们添加一个简单的输出解析器将聊天消息转换为字符串。

```python
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
```

现在，我们可以将其添加到之前的链中：

```python
chain = prompt | llm | output_parser
```

现在，我们可以调用它并问相同的问题。答案现在将是一个字符串（而不是ChatMessage）。

```python
chain.invoke({"input": "how can langsmith help with testing?"})
```


### 深入了解

我们现在已成功设置了一个基本的LLM链。我们只触及了提示符、模型和输出解析器的基础知识-要更深入地了解这里提到的所有内容，请参阅[文档的此部分](/modules/model_io)。


## 检索链

为了正确回答原始问题（“langsmith如何帮助测试？”），我们需要为LLM提供附加上下文。我们可以通过*检索*来实现这一点。当您有**过多数据**需要传递给LLM时，可使用检索工具仅检索相关数据并传递给LLM。 

在此过程中，我们将从*检索器*中查找相关文档，然后将它们传递给提示符。检索器可以由任何东西支持-一个SQL表、互联网等-但在本例中，我们将填充一个向量存储并将其用作检索器。有关向量存储的更多信息，请参阅[此文档](/modules/data_connection/vectorstores)。

首先，我们需要加载要索引的数据。为此，我们将使用WebBaseLoader。这需要安装[BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)：

```shell
pip install beautifulsoup4
```

然后，我们可以导入并使用WebBaseLoader。

```python
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")

docs = loader.load()
```

接下来，我们需要将其索引到向量存储中。这需要一些组件，即[嵌入模型](/modules/data_connection/text_embedding)和[向量存储](/modules/data_connection/vectorstores)。

对于嵌入模型，我们再次提供通过API访问或通过运行本地模型的示例。

<Tabs>
  <TabItem value="openai" label="OpenAI (API)" default>
  
确保您已安装`langchain_openai`包并设置了适当的环境变量（与LLM所需的相同）。

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
```

</TabItem>
<TabItem value="local" label="Local (using Ollama)">

确保Ollama正在运行（与LLM相同的设置）。

```python
from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings()
```

</TabItem>
<TabItem value="cohere" label="Cohere (API)" default>

确保您已安装`cohere`包并设置了适当的环境变量（与LLM所需的相同）。

```python
from langchain_community.embeddings import CohereEmbeddings

embeddings = CohereEmbeddings()
```

</TabItem>
</Tabs>

现在，我们可以使用这个嵌入模型将文档导入向量存储。为了简单起见，我们将使用一个简单的本地向量存储[FAISS](/integrations/vectorstores/faiss)。

首先，我们需要安装所需的软件包：

```shell
pip install faiss-cpu
```

然后，我们可以构建我们的索引：

```python
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)
```

现在，我们在向量存储中索引了这些数据，我们将创建一个检索链。该链将接收一个输入问题，查找相关文档，然后将这些文档连同原始问题一起传递给LLM，并要求它回答原始问题。

首先，让我们设置链来接收一个问题和检索到的文档，并生成一个回答。

```python
from langchain.chains.combine_documents import create_stuff_documents_chain

prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)
```

如果我们想的话，可以直接传递文档来运行它：

```python
from langchain_core.documents import Document

document_chain.invoke({
    "input": "how can langsmith help with testing?",
    "context": [Document(page_content="langsmith can let you visualize test results")]
})
```

然而，我们希望文档首先来自我们刚刚设置的检索器。这样，我们就可以使用检索器动态选择最相关的文档并将其传递给给定的问题。

```python
from langchain.chains import create_retrieval_chain

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)
```

现在，我们可以调用此链。这将返回一个词典-LLM的响应在`answer`键中。

```python
response = retrieval_chain.invoke({"input": "how can langsmith help with testing?"})
print(response["answer"])

# LangSmith提供了几个功能，可以帮助进行测试:...
```

这个答案应该更准确一些！

### 深入了解

我们现在已经成功设置了一个基本的检索链。我们只触及了检索的基础知识-要更深入地了解这里提到的所有内容，请参阅[文档的此部分](/modules/data_connection)。


## 对话检索链

到目前为止，我们创建的链只能回答单个问题。人们正在构建的LLM应用程序的主要类型之一是聊天机器人。那么我们如何将这个链转变为可以回答后续问题的链呢？

我们仍然可以使用`create_retrieval_chain`函数，但我们需要更改两件事情：

1. 检索方法现在不仅适用于最近的输入，而且还应考虑整个历史记录。
2. 最终的LLM链也应考虑整个历史记录

**更新检索器**

为了更新检索器，我们将创建一个新的链。该链将接收最新的输入（`input`）和对话历史（`chat_history`），并使用LLM生成一个搜索查询。

```python
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder

# 首先，我们需要一个可以传递给LLM来生成此搜索查询的提示

prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    ("user", "根据上面的对话，生成一个搜索查询来获取与对话相关的信息")
])
retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
```

我们可以通过传递一个实例来测试这一点，其中用户提出了一个后续问题。

```python
from langchain_core.messages import HumanMessage, AIMessage

chat_history = [HumanMessage(content="Can LangSmith help test my LLM applications?"), AIMessage(content="Yes!")]
retriever_chain.invoke({
    "chat_history": chat_history,
    "input": "Tell me how"
})
```
您应该看到这返回了关于在LangSmith中进行测试的文档。这是因为LLM生成了一个新的查询，将对话历史与后续问题结合起来。

既然我们有了这个新的检索器，我们就可以创建一个新的链，以在考虑到这些检索到的文档的情况下继续对话。

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "根据下面的上下文回答用户的问题：\n\n{context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
])
document_chain = create_stuff_documents_chain(llm, prompt)

retrieval_chain = create_retrieval_chain(retriever_chain, document_chain)
```

现在，我们可以端到端地测试这个：

```python
chat_history = [HumanMessage(content="Can LangSmith help test my LLM applications?"), AIMessage(content="Yes!")]
retrieval_chain.invoke({
    "chat_history": chat_history,
    "input": "Tell me how"
})
```
我们可以看到这给出了一个连贯的答案-我们已成功将我们的检索链转变为一个聊天机器人！## 代理人

我们迄今为止已经创建了链的示例 - 在这些示例中，每个步骤都是预先确定的。
最后我们将创建一个代理人 - 在这种情况下，LLM决定要采取的步骤。

**注意：对于此示例，我们只会展示如何使用OpenAI模型创建一个代理人，因为本地模型尚不够可靠。**

构建代理人时的第一件事是决定它应该具有哪些工具的访问权限。
在此示例中，我们将授予代理人访问两个工具的权限：

1. 我们刚刚创建的检索器。这将使其能够轻松回答关于LangSmith的问题。
2. 一个搜索工具。这将使其能够轻松回答需要最新信息的问题。

首先，让我们为我们刚刚创建的检索器设置一个工具：

```python
from langchain.tools.retriever import create_retriever_tool

retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "搜索与LangSmith相关的信息。有关LangSmith的任何问题，您必须使用此工具！",
)
```

我们将使用的搜索工具是[Tavily](/integrations/retrievers/tavily)。这需要一个API密钥（他们提供慷慨的免费层级）。在其平台上创建后，您需要将其设置为环境变量：

```shell
export TAVILY_API_KEY=...
```

如果您不想设置API密钥，可以跳过创建此工具。

```python
from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults()
```

现在我们可以创建一个我们想要使用的工具列表：

```python
tools = [retriever_tool, search]
```

现在我们有了工具，我们可以创建一个代理人来使用它们。我们将快速浏览一下 - 如果您想更深入地了解正在发生的事情，请查看[代理人入门文档](/modules/agents)。

首先安装langchain hub
```bash
pip install langchainhub
```
然后安装langchain-openai包
要与OpenAI进行交互，我们需要使用与OpenAI SDK[https://github.com/langchain-ai/langchain/tree/master/libs/partners/openai]连接的langchain-openai。
```bash
pip install langchain-openai
```

现在我们可以使用它来获取预定义的提示

```python
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

# 获取要使用的提示 - 您可以修改此提示！
prompt = hub.pull("hwchase17/openai-functions-agent")

# 您需要设置OPENAI_API_KEY环境变量，或者将其作为参数`api_key`传递。
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

现在我们可以调用代理人并查看它的响应！我们可以问关于LangSmith的问题：

```python
agent_executor.invoke({"input": "langsmith如何帮助测试？"})
```

我们可以询问天气情况：

```python
agent_executor.invoke({"input": "旧金山的天气如何？"})
```

我们可以与代理人进行交谈：

```python
chat_history = [HumanMessage(content="LangSmith可以帮助测试我的LLM应用程序吗？"), AIMessage(content="可以！")]
agent_executor.invoke({
    "chat_history": chat_history,
    "input": "告诉我如何进行"
})
```

### 进一步深入

我们现在成功地设置了一个基本的代理人。我们只触及了代理人的基础知识 - 如果您想更深入地了解这里提到的所有内容，请参阅[文档的这一部分](/modules/agents)。

## 使用LangServe进行服务

现在我们已经构建了一个应用程序，我们需要提供服务。这就是LangServe的作用。
LangServe帮助开发人员将LangChain链部署为REST API。您不需要使用LangServe来使用LangChain，但在本指南中，我们将展示如何使用LangServe部署您的应用程序。

虽然本指南的第一部分是在Jupyter Notebook中运行的，但现在我们将移出该环境。我们将创建一个Python文件，然后从命令行与其交互。

使用以下命令安装LangServe：
```bash
pip install "langserve[all]"
```

### 服务器

为了为我们的应用程序创建一个服务器，我们将创建一个`serve.py`文件。其中包含用于提供我们的应用程序的逻辑。它由以下三个部分组成：
1. 我们刚刚构建的链的定义
2. 我们的FastAPI应用程序
3. 定义一个路径以提供链的那部分代码，可以使用`langserve.add_routes`来实现

```python
#!/usr/bin/env python
from typing import List

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.messages import BaseMessage
from langserve import add_routes

# 1. 加载检索器
loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
embeddings = OpenAIEmbeddings()
vector = FAISS.from_documents(documents, embeddings)
retriever = vector.as_retriever()

# 2. 创建工具
retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "搜索与LangSmith相关的信息。有关LangSmith的任何问题，您必须使用此工具！",
)
search = TavilySearchResults()
tools = [retriever_tool, search]


# 3. 创建代理人
prompt = hub.pull("hwchase17/openai-functions-agent")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


# 4. 应用程序定义
app = FastAPI(
  title="LangChain服务器",
  version="1.0",
  description="使用LangChain的可运行接口的简单API服务器",
)

# 5. 添加链路由

# 我们需要添加这些输入/输出模式，因为当前的AgentExecutor缺乏模式。

class Input(BaseModel):
    input: str
    chat_history: List[BaseMessage] = Field(
        ...,
        extra={"widget": {"type": "chat", "input": "location"}},
    )


class Output(BaseModel):
    output: str

add_routes(
    app,
    agent_executor.with_types(input_type=Input, output_type=Output),
    path="/agent",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
```

大功告成！如果我们执行以下命令：

```bash
python serve.py
```
我们应该在localhost:8000上看到我们的链正在提供服务。

### 游乐场

每个LangServe服务都自带一个简单的内置UI，用于配置和调用具有流式输出和对中间步骤的可见性的应用程序。
请访问http://localhost:8000/agent/playground/ 尝试一下！传入与之前相同的问题 - "how can langsmith help with testing?" - 它应该与之前的响应一样。

### 客户端

现在让我们为与服务进行编程交互设置一个客户端。我们可以使用`[langserve.RemoteRunnable](/langserve#client)`来轻松实现这一点。
使用这个，我们可以像客户端一样与服务链交互。

```python
from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/agent/")
remote_chain.invoke({
    "input": "how can langsmith help with testing?",
    "chat_history": []  # 提供空列表作为这是第一个调用
})
```

要了解有关LangServe的许多其他功能的更多信息，请[在此处查看](/langserve)。

## 下一步

我们已经了解了如何使用LangChain构建应用程序，如何使用LangSmith跟踪它，以及如何使用LangServe提供服务。
这三者中有许多更多的功能，我们无法在这里全部涵盖。
要继续您的旅程，我们建议按照以下顺序阅读：

- 所有这些功能都由[LangChain表达式语言（LCEL）](/expression_language)支持 - 一种将这些组件链接在一起的方法。查看该文档以更好地了解如何创建自定义链。
- [模型IO](/modules/model_io)涵盖了有关提示、LLMs和输出解析器的更多细节。
- [检索](/modules/data_connection)涵盖了与检索有关的所有细节
- [代理](/modules/agents)涵盖了与代理有关的所有细节
- 探索常见的[端到端用例](/use_cases/)和[模板应用程序](/templates)
- [阅读关于LangSmith的更多信息](/langsmith/)，这是用于调试、测试、监控等的平台
- 了解如何使用[LangServe](/langserve)提供您的应用程序