# 检索

检索是聊天机器人在其训练数据之外使用数据增强其响应的常用技术。本节将介绍如何在聊天机器人的上下文中实现检索，但值得注意的是，检索是一个非常微妙和深入的主题 - 我们鼓励你探索[文档的其他部分](/use_cases/question_answering/)，其中对此进行了更深入的介绍！

## 设置

您需要安装一些软件包，并将您的OpenAI API密钥设置为名为`OPENAI_API_KEY`的环境变量：

```python
％pip install --upgrade --quiet langchain langchain-openai chromadb beautifulsoup4

＃设置环境变量OPENAI_API_KEY或从.env文件加载：
import dotenv

dotenv.load_dotenv()
```

    [33m警告：您正在使用pip版本22.0.4； 但是，版本23.3.2可用。
    您应该考虑通过'/ Users / jacoblee / .pyenv / versions / 3.10.5 / bin / python -m pip install --upgrade pip'命令进行升级。[0m[33m
    [0m注意：您可能需要重新启动内核才能使用更新的软件包。
    




    True



让我们还设置一个聊天模型，我们将在下面的示例中使用它。

```python
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)
```

## 创建一个检索器

我们将使用[LangSmith文档](https://docs.smith.langchain.com/overview)作为源材料，并将内容存储在矢量存储中以供稍后检索。请注意，此示例将忽略有关解析和存储数据源的特定内容 - 您可以在此处查看更多有关创建检索系统的详细文档。

让我们使用一个文档加载器从文档中提取文本：

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
data = loader.load()
```

然后，我们将其分割为较小的块，LLM的上下文窗口可以处理，并将其存储在矢量数据库中：

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)
```

然后，我们嵌入并将这些块存储在矢量数据库中：

```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())
```

最后，让我们从初始化的矢量存储中创建一个检索器：

```python
# k是要检索的块数
retriever = vectorstore.as_retriever(k=4)

docs = retriever.invoke("Can LangSmith help test my LLM applications?")

docs
```

我们可以看到上面检索器的调用结果，其中包含一些LangSmith文档的部分，这些文档包含有关我们的聊天机器人可以在回答问题时使用的测试信息。现在，我们有了一个可以从LangSmith文档中返回相关数据的检索器！

## 文档链

现在我们有了一个可以返回LangChain文档的检索器，让我们创建一个链，可以将它们作为上下文来回答问题。我们将使用一个`create_stuff_documents_chain`帮助函数来将所有输入文档“填充”到提示中。它还将处理将文档格式化为字符串。

除了聊天模型外，该函数还期望有一个具有“context”变量的提示，以及一个名为“messages”的聊天历史消息的占位符。我们将创建一个合适的提示并将其传递如下：

```python
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

SYSTEM_TEMPLATE = """
根据下面的上下文回答用户的问题。
如果上下文中没有任何与问题相关的信息，请不要捏造信息，只需说“我不知道”：

<context>
{context}
</context>
"""

question_answering_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            SYSTEM_TEMPLATE,
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

document_chain = create_stuff_documents_chain(chat, question_answering_prompt)
```

我们可以单独调用此`document_chain`来回答问题。让我们使用上面检索到的文档和相同的问题`如何使用LangSmith进行测试？`：

```python
from langchain_core.messages import HumanMessage

document_chain.invoke(
    {
        "context": docs,
        "messages": [
            HumanMessage(content="Can LangSmith help test my LLM applications?")
        ],
    }
)
```

看起来很好！为了对比，我们可以尝试没有上下文文档并比较结果：

```python
document_chain.invoke(
    {
        "context": [],
        "messages": [
            HumanMessage(content="Can LangSmith help test my LLM applications?")
        ],
    }
)
```

我们可以看到LLM没有返回任何结果。

## 检索链

让我们将这个文档链与检索器结合起来。下面是这种情况下的一种方式：

```python
from typing import Dict

from langchain_core.runnables import RunnablePassthrough


def parse_retriever_input(params: Dict):
    return params["messages"][-1].content


retrieval_chain = RunnablePassthrough.assign(
    context=parse_retriever_input | retriever,
).assign(
    answer=document_chain,
)
```

给定一个输入消息列表，我们提取列表中最后一条消息的内容，并将其传递给检索器以获取一些文档。然后，我们将这些文档作为上下文传递给我们的文档链，以生成最终的响应。

调用此链结合了上面概述的两个步骤：

```python
retrieval_chain.invoke(
    {
        "messages": [
            HumanMessage(content="Can LangSmith help test my LLM applications?")
        ],
    }
)
```

看起来很好！
=======
## 进一步阅读

本指南只是涉及到检索技巧的表面知识。如果想了解更多有关不同摄取、准备和检索最相关数据的方式，请查看[此部分](/docs/modules/data_connection/)的文档。