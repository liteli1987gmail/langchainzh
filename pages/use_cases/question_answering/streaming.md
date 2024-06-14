
# 流媒体

在问答应用程序中，向用户显示生成答案的来源非常重要。最简单的方法是让链条返回每个生成过程中检索到的文档。

我们将基于我们在[Lilian Weng的“LLM动力自主代理](https://lilianweng.github.io/posts/2023-06-23-agent/)博客文章中构建的具有源码的Q&A应用程序进行操作，该博客文章的详细信息请参阅[返回源码](/use_cases/question_answering/sources)指南。

## 设置

### 依赖关系

在本教程中，我们将使用OpenAI聊天模型、嵌入向量和Chroma向量库，但是这里展示的所有内容都适用于任何[ChatModel](/modules/model_io/chat/)或[LLM](/modules/model_io/llms/)，[Embeddings](/modules/data_connection/text_embedding/)和[VectorStore](/modules/data_connection/vectorstores/)或[Retriever](/modules/data_connection/retrievers/)。

我们将使用以下软件包：


```python
%pip install --upgrade --quiet  langchain langchain-community langchainhub langchain-openai chromadb bs4
```

我们需要设置环境变量`OPENAI_API_KEY`，可以直接设置，也可以从`.env`文件中加载，示例代码如下：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# import dotenv

# dotenv.load_dotenv()
```

### LangSmith

使用LangChain构建的许多应用程序都包含多个步骤，需要多次调用LLM。随着这些应用程序的复杂性越来越高，能够检查链条或代理内部发生的情况变得至关重要。最好的方法是使用[LangSmith](https://smith.langchain.com)。

请注意，不需要使用LangSmith，但这是非常有帮助的。如果您确实想使用LangSmith，请在上面的链接中注册后，确保设置环境变量以开始记录追踪信息：


```python
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 具有源代码的链条

下面是我们在[Lilian Weng的“LLM动力自主代理](https://lilianweng.github.io/posts/2023-06-23-agent/)博客文章中构建的具有源码的Q&A应用程序：


```python
import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
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

# 检索并生成相关博客片段。
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain_from_docs = (
    RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
    | prompt
    | llm
    | StrOutputParser()
)

rag_chain_with_source = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
).assign(answer=rag_chain_from_docs)
```

## 流式输出

使用LCEL很容易流式输出：


```python
for chunk in rag_chain_with_source.stream("任务拆分是什么"):
    print(chunk)
```

    {'question': 'What is Task Decomposition'}
    {'context': [Document(page_content='Fig. 1. Overview of a LLM-powered autonomous agent system.\nComponent One: Planning#\nA complicated task usually involves many steps. An agent needs to know what they are and plan ahead.\nTask Decomposition#\nChain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}), Document(page_content='Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.\nTask decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}), Document(page_content='The AI assistant can parse user input to several tasks: [{"task": task, "id", task_id, "dep": dependency_task_ids, "args": {"text": text, "image": URL, "audio": URL, "video": URL}}]. The "dep" field denotes the id of the previous task which generates a new resource that the current task relies on. A special tag "-task_id" refers to the generated text image, audio and video in the dependency task with id as task_id. The task MUST be selected from the following options: {{ Available Task List }}. There is a logical relationship between tasks, please note their order. If the user input can\'t be parsed, you need to reply empty JSON. Here are several cases for your reference: {{ Demonstrations }}. The chat history is recorded as {{ Chat History }}. From this chat history, you can find the path of the user-mentioned resources for your task planning.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}), Document(page_content='Fig. 11. Illustration of how HuggingGPT works. (Image source: Shen et al. 2023)\nThe system comprises of 4 stages:\n(1) Task planning: LLM works as the brain and parses the user requests into multiple tasks. There are four attributes associated with each task: task type, ID, dependencies, and arguments. They use few-shot examples to guide LLM to do task parsing and planning.\nInstruction:', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'})]}
    {'answer': ''}
    {'answer': 'Task'}
    {'answer': ' decomposition'}
    {'answer': ' is'}
    {'answer': ' a'}
    {'answer': ' technique'}
    {'answer': ' used'}
    {'answer': ' to'}
    {'answer': ' break'}
    {'answer': ' down'}
    {'answer': ' complex'}
    {'answer': ' tasks'}
    {'answer': ' into'}
    {'answer': ' smaller'}
    {'answer': ' and'}
    {'answer': ' simpler'}
    {'answer': ' steps'}
    {'answer': '.'}
    {'answer': ' It'}
    {'answer': ' can'}
    {'answer': ' be'}
    {'answer': ' done'}
    {'answer': ' through'}
    {'answer': ' methods'}
    {'answer': ' like'}
    {'answer': ' Chain'}
    {'answer': ' of'}
    {'answer': ' Thought'}
    {'answer': ' (CoT)'}
    {'answer': ' or'}
    {'answer': ' Tree'}
    {'answer': ' of'}
    {'answer': ' Thoughts'}
    {'answer': ','}
    {'answer': ' which'}
    {'answer': ' involve'}
    {'answer': ' dividing'}
    {'answer': ' the'}
    {'answer': ' task'}
    {'answer': ' into'}
    {'answer': ' manageable'}
    {'answer': ' subtasks'}
    {'answer': ' and'}
    {'answer': ' exploring'}
    {'answer': ' multiple'}
    {'answer': ' reasoning'}
    {'answer': ' possibilities'}
    {'answer': ' at'}
    {'answer': ' each'}
    {'answer': ' step'}
    {'answer': '.'}
    {'answer': ' Task'}
    {'answer': ' decomposition'}
    {'answer': ' can'}
    {'answer': ' be'}
    {'answer': ' performed'}
    {'answer': ' by'}
    {'answer': ' using'}
    {'answer': ' simple'}
    {'answer': ' prompts'}
    {'answer': ','}
    {'answer': ' task-specific'}
    {'answer': ' instructions'}
    {'answer': ','}
    {'answer': ' or'}
    {'answer': ' human'}
    {'answer': ' inputs'}
    {'answer': '.'}
    {'answer': ''}
    

我们可以添加一些逻辑来编译返回的流式输出：


```python
output = {}
curr_key = None
for chunk in rag_chain_with_source.stream("任务拆分是什么"):
    for key in chunk:
        if key not in output:
            output[key] = chunk[key]
        else:
            output[key] += chunk[key]
        if key != curr_key:
            print(f"\n\n{key}: {chunk[key]}", end="", flush=True)
        else:
            print(chunk[key], end="", flush=True)
        curr_key = key
output
```

    
    
    question: What is Task Decomposition
    
    context: [Document(page_content='Fig. 1. Overview of a LLM-powered autonomous agent system.\nComponent One: Planning#\nA complicated task usually involves many steps. An agent needs to know what they are and plan ahead.\nTask Decomposition#\nChain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}), Document(page_content='Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.\nTask decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}), Document(page_content='The AI assistant can parse user input to several tasks: [{"task": task, "id", task_id, "dep": dependency_task_ids, "args": {"text": text, "image": URL, "audio": URL, "video": URL}}]. The "dep" field denotes the id of the previous task which generates a new resource that the current task relies on. A special tag "-task_id" refers to the generated text image, audio and video in the dependency task with id as task_id. The task MUST be selected from the following options: {{ Available Task List }}. There is a logical relationship between tasks, please note their order. If the user input can\'t be parsed, you need to reply empty JSON. Here are several cases for your reference: {{ Demonstrations }}. The chat history is recorded as {{ Chat History }}. From this chat history, you can find the path of the user-mentioned resources for your task planning.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}), Document(page_content='Fig. 11. Illustration of how HuggingGPT works. (Image source: Shen et al. 2023)\nThe system comprises of 4 stages:\n(1) Task planning: LLM works as the brain and parses the user requests into multiple tasks. There are four attributes associated with each task: task type, ID, dependencies, and arguments. They use few-shot examples to guide LLM to do task parsing and planning.\nInstruction:', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'})]
    
    answer: Task decomposition is a technique used to break down complex tasks into smaller and simpler steps. It can be done through methods like Chain of Thought (CoT) or Tree of Thoughts, which involve dividing the task into manageable subtasks and exploring multiple reasoning possibilities at each step. Task decomposition can be performed by using simple prompts, task-specific instructions, or human inputs.




    {'question': 'What is Task Decomposition',
     'context': [Document(page_content='Fig. 1. Overview of a LLM-powered autonomous agent system.\nComponent One: Planning#\nA complicated task usually involves many steps. An agent needs to know what they are and plan ahead.\nTask Decomposition#\nChain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}),
      Document(page_content='Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.\nTask decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}),
      Document(page_content='The AI assistant can parse user input to several tasks: [{"task": task, "id", task_id, "dep": dependency_task_ids, "args": {"text": text, "image": URL, "audio": URL, "video": URL}}]. The "dep" field denotes the id of the previous task which generates a new resource that the current task relies on. A special tag "-task_id" refers to the generated text image, audio and video in the dependency task with id as task_id. The task MUST be selected from the following options: {{ Available Task List }}. There is a logical relationship between tasks, please note their order. If the user input can\'t be parsed, you need to reply empty JSON. Here are several cases for your reference: {{ Demonstrations }}. The chat history is recorded as {{ Chat History }}. From this chat history, you can find the path of the user-mentioned resources for your task planning.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}),
      Document(page_content='Fig. 11. Illustration of how HuggingGPT works. (Image source: Shen et al. 2023)\nThe system comprises of 4 stages:\n(1) Task planning: LLM works as the brain and parses the user requests into multiple tasks. There are four attributes associated with each task: task type, ID, dependencies, and arguments. They use few-shot examples to guide LLM to do task parsing and planning.\nInstruction:', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'})],
     'answer': 'Task decomposition is a technique used to break down complex tasks into smaller and simpler steps. It can be done through methods like Chain of Thought (CoT) or Tree of Thoughts, which involve dividing the task into manageable subtasks and exploring multiple reasoning possibilities at each step. Task decomposition can be performed by using simple prompts, task-specific instructions, or human inputs.'}## 流式中间步骤

假设我们想要在链的最终输出之外，还可以流式传输一些中间步骤。让我们以我们的[聊天记录](/use_cases/question_answering/chat_history)链为例。在将用户问题传递给检索器之前，我们对用户问题进行了重新表述。这个重新表述的问题不作为最终输出的一部分返回。我们可以修改我们的链条来返回新问题，但为了演示目的，我们将保持不变。

```python
from operator import itemgetter

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tracers.log_stream import LogStreamCallbackHandler

contextualize_q_system_prompt = """给定一个聊天记录和最新的用户问题，可能引用聊天记录中的上下文，请组成一个独立的问题，可以不使用聊天记录来理解。如果需要，重新表述问题，否则原样返回它。"""
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)
contextualize_q_chain = (contextualize_q_prompt | llm | StrOutputParser()).with_config(
    tags=["contextualize_q_chain"]
)

qa_system_prompt = """你是一个用于问答任务的助手。使用下面检索到的上下文片段来回答问题。如果不知道答案，只需说不知道。使用最多三个句子，回答简明扼要。\n\n{context}"""
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)


def contextualized_question(input: dict):
    if input.get("chat_history"):
        return contextualize_q_chain
    else:
        return input["question"]


rag_chain = (
    RunnablePassthrough.assign(context=contextualize_q_chain | retriever | format_docs)
    | qa_prompt
    | llm
)
```

要流式传输中间步骤，我们将使用`astream_log`方法。这是一个异步方法，它产生JSONPatch操作，在按接收到的相同顺序应用时构建RunState：

```python
class RunState(TypedDict):
    id: str
    """运行的ID。"""
    streamed_output: List[Any]
    """Runnable.stream()流式传输的输出块列表"""
    final_output: Optional[Any]
    """运行的最终输出，通常是聚合(`+`)streamed_output的结果。只有在运行成功完成后才可用。"""

    logs: Dict[str, LogEntry]
    """运行名称到子运行的映射。如果提供了过滤器，则此列表将仅包含与过滤器匹配的运行。"""
```

您可以流式传输所有步骤（默认）或按名称、标签或元数据包含/排除步骤。在本例中，我们只流式传输属于`contextualize_q_chain`的中间步骤和最终输出。请注意，在定义`contextualize_q_chain`时，我们给它赋予了相应的标签，现在我们可以根据该标签进行过滤。

为了可读性，我们只显示流的前20个块：

```python
# Jupyter笔记本中运行异步函数所需的操作:
import nest_asyncio

nest_asyncio.apply()
```

```python
from langchain_core.messages import HumanMessage

chat_history = []

question = "什么是任务分解？"
ai_msg = rag_chain.invoke({"question": question, "chat_history": chat_history})
chat_history.extend([HumanMessage(content=question), ai_msg])

second_question = "常见的执行任务分解的方法有哪些？"
ct = 0
async for jsonpatch_op in rag_chain.astream_log(
    {"question": second_question, "chat_history": chat_history},
    include_tags=["contextualize_q_chain"],
):
    print(jsonpatch_op)
    print("\n" + "-" * 30 + "\n")
    ct += 1
    if ct > 20:
        break
```
```
    RunLogPatch({'op': 'replace',
      'path': '',
      'value': {'final_output': None,
                'id': 'df0938b3-3ff2-451b-a233-6c882b640e4d',
                'logs': {},
                'streamed_output': []}})
    
    ------------------------------
    
    RunLogPatch({'op': 'add',
      'path': '/logs/RunnableSequence',
      'value': {'end_time': None,
                'final_output': None,
                'id': '2e2af851-9e1f-4260-b004-c30dea4affe9',
                'metadata': {},
                'name': 'RunnableSequence',
                'start_time': '2023-12-29T20:08:28.923',
                'streamed_output': [],
                'streamed_output_str': [],
                'tags': ['seq:step:1', 'contextualize_q_chain'],
                'type': 'chain'}})
    
    ------------------------------
    
    RunLogPatch({'op': 'add',
      'path': '/logs/ChatPromptTemplate',
      'value': {'end_time': None,
                'final_output': None,
                'id': '7ad34564-337c-4362-ae7a-655d79cf0ab0',
                'metadata': {},
                'name': 'ChatPromptTemplate',
                'start_time': '2023-12-29T20:08:28.926',
                'streamed_output': [],
                'streamed_output_str': [],
                'tags': ['seq:step:1', 'contextualize_q_chain'],
                'type': 'prompt'}})
    
    ------------------------------
    
    RunLogPatch({'op': 'add',
      'path': '/logs/ChatPromptTemplate/final_output',
      'value': ChatPromptValue(messages=[SystemMessage(content='给定一个聊天记录和最新的用户问题，可能引用聊天记录中的上下文，请组成一个独立的问题，可以不使用聊天记录来理解。如果需要，重新表述问题，否则原样返回它。'), HumanMessage(content='什么是任务分解？'), AIMessage(content='任务分解是一种将复杂任务分解为较小更易管理的子任务的技术。它涉及将任务分解为多个步骤或子目标，允许代理人或模型更好地理解和规划整体任务。任务分解可以通过各种方法进行，例如使用链式思维或思维树等提示技术，任务特定的说明，或人类输入。'), HumanMessage(content='常见的执行任务分解的方法有哪些？')])},
     {'op': 'add',
      'path': '/logs/ChatPromptTemplate/end_time',
      'value': '2023-12-29T20:08:28.926'})
    
    ------------------------------
    
    RunLogPatch({'op': 'add',
      'path': '/logs/ChatOpenAI',
      'value': {'end_time': None,
                'final_output': None,
                'id': '228792d6-1d76-4209-8d25-08c484b6df57',
                'metadata': {},
                'name': 'ChatOpenAI',
                'start_time': '2023-12-29T20:08:28.931',
                'streamed_output': [],
                'streamed_output_str': [],
                'tags': ['seq:step:2', 'contextualize_q_chain'],
                'type': 'llm'}})
    
    ------------------------------
    
    RunLogPatch({'op': 'add',
      'path': '/logs/StrOutputParser',
      'value': {'end_time': None,
                'final_output': None,
                'id': 'f740f235-2b14-412d-9f54-53bbc4fa8fd8',
                'metadata': {},
                'name': 'StrOutputParser',
                'start_time': '2023-12-29T20:08:29.487',
                'streamed_output': [],
                'streamed_output_str': [],
                'tags': ['seq:step:3', 'contextualize_q_chain'],
                'type': 'parser'}})
    
    ------------------------------
    
    RunLogPatch({'op': 'add', 'path': '/logs/ChatOpenAI/streamed_output_str/-', 'value': ''},
     {'op': 'add',
      'path': '/logs/ChatOpenAI/streamed_output/-',
      'value': AIMessageChunk(content='')})
    
    ------------------------------
    
    RunLogPatch({'op': 'add',
      'path': '/logs/ChatOpenAI/streamed_output_str/-',
      'value': 'What'},
     {'op': 'add',
      'path': '/logs/ChatOpenAI/streamed_output/-',
      'value': AIMessageChunk(content='What')})
    





------------------------------
RunLogPatch({'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output_str/-',
  'value': ' are'},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content=' are')})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output_str/-',
  'value': ' some'},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content=' some')})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output_str/-',
  'value': ' commonly'},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content=' commonly')})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output_str/-',
  'value': ' used'},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content=' used')})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output_str/-',
  'value': ' methods'},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content=' methods')})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output_str/-',
  'value': ' or'},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content=' or')})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output_str/-',
  'value': ' approaches'},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content=' approaches')})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output_str/-',
  'value': ' for'},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content=' for')})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output_str/-',
  'value': ' task'},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content=' task')})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output_str/-',
  'value': ' decomposition'},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content=' decomposition')})

------------------------------

RunLogPatch({'op': 'add', 'path': '/logs/ChatOpenAI/streamed_output_str/-', 'value': '?'},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content='?')})

------------------------------

RunLogPatch({'op': 'add', 'path': '/logs/ChatOpenAI/streamed_output_str/-', 'value': ''},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/streamed_output/-',
  'value': AIMessageChunk(content='')})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/ChatOpenAI/final_output',
  'value': {'generations': [[{'generation_info': {'finish_reason': 'stop'},
                              'message': AIMessageChunk(content='What are some commonly used methods or approaches for task decomposition?'),
                              'text': 'What are some commonly used methods or '
                                      'approaches for task decomposition?',
                              'type': 'ChatGenerationChunk'}]],
            'llm_output': None,
            'run': None}},
 {'op': 'add',
  'path': '/logs/ChatOpenAI/end_time',
  'value': '2023-12-29T20:08:29.688'})

------------------------------

```


如果我们想要获取检索到的文档，我们可以按名称 "Retriever" 进行过滤：


```python
ct = 0
async for jsonpatch_op in rag_chain.astream_log(
    {"question": second_question, "chat_history": chat_history},
    include_names=["Retriever"],
    with_streamed_output_list=False,
):
    print(jsonpatch_op)
    print("\n" + "-" * 30 + "\n")
    ct += 1
    if ct > 20:
        break
```
```
RunLogPatch({'op': 'replace',
  'path': '',
  'value': {'final_output': None,
            'id': '9d122c72-378c-41f8-96fe-3fd9a214e9bc',
            'logs': {},
            'streamed_output': []}})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/Retriever',
  'value': {'end_time': None,
            'final_output': None,
            'id': 'c83481fb-7ca3-4125-9280-96da0c14eee9',
            'metadata': {},
            'name': 'Retriever',
            'start_time': '2023-12-29T20:10:13.794',
            'streamed_output': [],
            'streamed_output_str': [],
            'tags': ['seq:step:2', 'Chroma', 'OpenAIEmbeddings'],
            'type': 'retriever'}})

------------------------------

RunLogPatch({'op': 'add',
  'path': '/logs/Retriever/final_output',
  'value': {'documents': [Document(page_content='Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.\nTask decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}),
                          Document(page_content='Fig. 1. Overview of a LLM-powered autonomous agent system.\nComponent One: Planning#\nA complicated task usually involves many steps. An agent needs to know what they are and plan ahead.\nTask Decomposition#\nChain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}),
                          Document(page_content='Resources:\n1. Internet access for searches and information gathering.\n2. Long Term memory management.\n3. GPT-3.5 powered Agents for delegation of simple tasks.\n4. File output.\n\nPerformance Evaluation:\n1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.\n2. Constructively self-criticize your big-picture behavior constantly.\n3. Reflect on past decisions and strategies to refine your approach.\n4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}),
                          Document(page_content='Fig. 9. Comparison of MIPS algorithms, measured in recall@10. (Image source: Google Blog, 2020)\nCheck more MIPS algorithms and performance comparison in ann-benchmarks.com.\nComponent Three: Tool Use#\nTool use is a remarkable and distinguishing characteristic of human beings. We create, modify and utilize external objects to do things that go beyond our physical and cognitive limits. Equipping LLMs with external tools can significantly extend the model capabilities.', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'})]}},
 {'op': 'add',
  'path': '/logs/Retriever/end_time',
  'value': '2023-12-29T20:10:14.234'})

------------------------------

RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='')})

------------------------------

RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='Common')})

------------------------------

RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='Common ways')})

------------------------------

RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='Common ways of')})

------------------------------

RunLogPatch({'op': 'replace',
```

```

'path': '/final_output',
'value': AIMessageChunk(content='任务的常见方法')}
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法')})
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法包括')})
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法包括:\n')})
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法包括:\n1')})
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法包括:\n1.')})
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法包括:\n1. 使用')})
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法包括:\n1. 使用提示')})
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法包括:\n1. 使用提示技巧')})
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法包括:\n1. 使用提示技巧，比如')})
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法包括:\n1. 使用提示技巧，比如链式')})
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法包括:\n1. 使用提示技巧，比如链式思维')})
    
------------------------------
    
RunLogPatch({'op': 'replace',
  'path': '/final_output',
  'value': AIMessageChunk(content='任务分解的常见方法包括:\n1. 使用提示技巧，比如链式思维(')})
    
------------------------------
```



