## 返回引用来源

在问答应用程序中，向用户展示生成答案所使用的来源非常重要。最简单的方法就是返回每一代中检索到的文档。

我们将基于我们在[Lilian Weng的博客文章LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)上构建的问答应用程序进行工作，该应用程序的[快速入门](/use_cases/question_answering/quickstart)。

## 设置

### 依赖项

在本次演示中，我们将使用OpenAI的聊天模型和嵌入，以及Chroma向量存储，但是这里展示的所有内容都适用于任何[ChatModel](/modules/model_io/chat/)或[LLM](/modules/model_io/llms/), [Embeddings](/modules/data_connection/text_embedding/), 和[VectorStore](/modules/data_connection/vectorstores/)或[Retriever](/modules/data_connection/retrievers/)。

我们将使用以下软件包：

```python
%pip install --upgrade --quiet  langchain langchain-community langchainhub langchain-openai chromadb bs4
```

我们需要设置环境变量`OPENAI_API_KEY`，可以直接设置，或者从`.env`文件中加载，如下所示：

```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# import dotenv

# dotenv.load_dotenv()
```

### LangSmith

你使用LangChain构建的许多应用程序会包含多个步骤，并且会多次调用LLM调用。随着这些应用程序变得越来越复杂，能够检查链或代理内部发生的情况变得至关重要。这里使用的最佳方法是使用[LangSmith](https://smith.langchain.com)。

注意，不需要使用LangSmith，但它是有用的。如果你确实想使用LangSmith，在上面的链接中注册后，请确保设置你的环境变量以开始记录跟踪：

```python
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 没有来源的链

以下是我们在[Lilian Weng的博客文章LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)上构建的问答应用程序的快速入门：

```python
import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
```

```python
# 加载、分块和索引博客的内容。
bs_strainer = bs4.SoupStrainer(class_=("post-content", "post-title", "post-header"))
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs={"parse_only": bs_strainer},
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# 使用博客的相关片段进行检索和生成。
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
```

```python
rag_chain.invoke("任务分解是什么？")
```

```plaintext
'任务分解是一种将复杂任务拆分为较小和较简单步骤的技术。可以通过Chain of Thought或Tree of Thoughts等提示技术，或者使用任务特定的指令或人类输入来完成。任务分解有助于代理规划和管理复杂任务。'
```

## 添加来源

使用LCEL很容易返回检索到的文档：

```python
from langchain_core.runnables import RunnableParallel

rag_chain_from_docs = (
    RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
    | prompt
    | llm
    | StrOutputParser()
)

rag_chain_with_source = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
).assign(answer=rag_chain_from_docs)

rag_chain_with_source.invoke("任务分解是什么?")
```

```plaintext
{'context': [Document(page_content='图1. LLM 动力自主代理系统概览\n组件一：计划\n复杂的任务通常涉及许多步骤。代理需要知道这些步骤并提前计划。\n任务分解\nChain of thought (CoT; Wei et al. 2022)已经成为提高模型在复杂任务上表现的标准提示技术。该模型被指示“逐步思考”，以利用更多的测试时间计算将艰难的任务分解为较小和较简单的步骤。CoT将大型任务转化为多个可管理的任务，并为模型的思考过程提供了解释。', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'start_index': 1585}),
      Document(page_content='Tree of Thoughts (Yao et al. 2023)通过在每个步骤上探索多个推理可能性来扩展 CoT。它首先将问题分解为多个思考步骤，并在每个步骤生成多个思考，创建一棵树结构。搜索过程可以使用广度优先搜索 (BFS) 或深度优先搜索 (DFS)，每个状态都会被分类器（通过提示）或多数投票进行评估。\n任务分解可以通过 LLM 以简单的提示（如 "XYZ 的步骤。\\n1."，"实现 XYZ 所需的子目标是什么?"），通过使用任务特定的指令（例如，写小说的写作大纲是什么。）或通过人类输入来完成。', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'start_index': 2192}),
      Document(page_content='AI 助理可以将用户输入解析为多个任务：[{"task": task,"id", task_id, "dep": dependency_task_ids, "args": {"text": text, "image": URL, "audio": URL, "video": URL}}]。"dep"字段表示当前任务依赖于生成的新资源的先前任务的 ID。特殊标记 "-task_id" 用来表示依赖任务中的生成的文本图像、音频和视频，其中 task_id 是任务的 ID。任务必须从以下选项中选择：{{ Available Task List }}。任务之间存在逻辑关系，请注意它们的顺序。如果无法解析用户输入，需要回复空的 JSON。这里有几个案例供您参考：{{ Demonstrations }}。聊天记录记录为{{ Chat History }}。从这个聊天记录中，您可以找到用户提到的资源路径，以便进行任务规划。', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'start_index': 17804}),
      Document(page_content='图11. HuggingGPT 的工作原理示例。（图片来源：沈 et al. 2023）\n系统包括四个阶段：\n（1）任务规划：LLM 作为大脑，将用户请求解析为多个任务。每个任务都有四个属性：任务类型、ID、依赖和参数。他们使用少样本示例来引导 LLM 进行任务解析和规划。\n指令：', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'start_index': 17414}),
      Document(page_content='资源：\n1. 进行搜索和信息收集的互联网访问。\n2. 长期内存管理。\n3. GPT-3.5 动力代理，用于委派简单任务。\n4. 文件输出。\n\n性能评估：\n1. 不断审查和分析你的行为，确保你发挥出最佳的能力。\n2. 对你的大局行为进行建设性的自我批评。\n3. 反思过去的决策和策略，改进你的方法。\n4. 每个命令都有一个成本，所以要聪明而高效。力求以最少的步骤完成任务。', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'start_index': 29630}),
      Document(page_content='（3）任务执行：专家模型对特定任务进行执行并记录结果。\n指令：\n\n根据输入和推断结果，AI助理需要以直接的方式回答用户的请求。然后描述任务的过程和结果，并以第一人称向用户展示分析和模型推断结果。如果推断结果包含文件路径，必须告诉用户完整的文件路径。', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'start_index': 19373})],
 'question': '任务分解是什么?',
 'answer': '任务分解是一种将复杂任务拆分为较小和较简单步骤的技术。它涉及将大型任务转化为多个可管理的任务，以更系统和有序的方式解决问题。谢谢你的提问！'}
```

:::⚠⚠⚠

查看[LangSmith跟踪记录](https://smith.langchain.com/public/007d7e01-cb62-4a84-8b71-b24767f953ee/r)

:::
