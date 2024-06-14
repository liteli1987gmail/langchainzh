# 使用代理

这是一个专门优化了检索和对话功能的代理。

首先，我们将设置我们想要使用的检索器，然后将其转换为检索工具。接下来，我们将使用这种类型代理的高级构造函数。最后，我们将介绍如何通过组件构建一个对话式检索代理。

```python
%pip install --upgrade --quiet  langchain langchain-community langchainhub langchain-openai faiss-cpu
```

## 检索器

首先，我们需要一个检索器来使用！这里的代码大部分只是示例代码。随意使用自己的检索器并跳到创建检索工具的部分。

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("../../modules/state_of_the_union.txt")
documents = loader.load()
```

```python
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embeddings)
```

```python
retriever = db.as_retriever()
```

## 检索工具

现在我们需要创建一个工具来使用我们的检索器。我们需要传递的主要内容是检索器的名称和描述。这两者都将被语言模型使用，因此它们应该是信息性的。

```python
from langchain.tools.retriever import create_retriever_tool

tool = create_retriever_tool(
    retriever,
    "search_state_of_union",
    "Searches and returns excerpts from the 2022 State of the Union.",
)
tools = [tool]
```

## 代理构造函数

在这里，我们将使用高级的 `create_openai_tools_agent` API 来构建代理。

注意，除了工具列表之外，我们只需要传递一个要使用的语言模型。在底层，该代理使用了 OpenAI 的工具调用功能，因此我们需要使用 ChatOpenAI 模型。

```python
from langchain import hub

prompt = hub.pull("hwchase17/openai-tools-agent")
prompt.messages
```

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)
```

```python
from langchain.agents import AgentExecutor, create_openai_tools_agent

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)
```

我们现在可以试试它！

```python
result = agent_executor.invoke({"input": "hi, im bob"})
```

```python
result["output"]
```

注意，现在它进行了检索

```python
result = agent_executor.invoke(
    {
        "input": "what did the president say about ketanji brown jackson in the most recent state of the union?"
    }
)
```

```python
result["output"]
```

注意，后续的问题询问了先前检索到的信息，所以不需要再进行检索

```python
result = agent_executor.invoke(
    {"input": "how long ago did the president nominate ketanji brown jackson?"}
)
```

```python
result["output"]
```

有关如何使用带有检索器和其他工具的代理的更多信息，请查阅[代理](/modules/agents)部分。

