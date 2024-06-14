# 格式化输入和输出

`RunnableParallel` 基本上是一个字典，其值是可运行的对象（或可以转换为可运行对象，比如函数）。它会并行运行所有的值，并且每个值都会使用 `RunnableParallel` 的整体输入进行调用。最终的返回值是一个字典，其中包含每个值的结果及其相应的键。

它适用于并行化操作，但也可以用于将一个 Runnable 的输出调整为下一个 Runnable 的输入格式。

在这里，prompt 的输入应该是一个具有 "context" 和 "question" 键的映射。用户的输入只是问题。所以我们需要使用我们的 retriever 获取上下文，并将用户输入通过 "question" 键传递。

```python
%pip install --upgrade --quiet langchain langchain-openai
```

```python
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

vectorstore = FAISS.from_texts(
    ["harrison worked at kensho"], embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI()

retrieval_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

retrieval_chain.invoke("where did harrison work?")
```

::: {.callout-tip}
请注意，当将一个 RunnableParallel 与另一个 Runnable 组合时，我们甚至不需要将字典包装在 RunnableParallel 类中 - 类型转换会自动处理。在链的上下文中，下面这些是等价的：
:::
```
{"context": retriever, "question": RunnablePassthrough()}
```
```
RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
```
```
RunnableParallel(context=retriever, question=RunnablePassthrough())
```

## 使用 itemgetter 作为简写

请注意，可以使用 Python 的 `itemgetter` 作为简写来从映射中提取数据，用于与 `RunnableParallel` 结合时。关于 itemgetter 的更多信息，请参阅 [Python 文档](https://docs.python.org/3/library/operator.html#operator.itemgetter)。

在下面的示例中，我们使用 itemgetter 从映射中提取特定的键：

```python
from operator import itemgetter

from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

vectorstore = FAISS.from_texts(
    ["harrison worked at kensho"], embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}

Answer in the following language: {language}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    {
        "context": itemgetter("question") | retriever,
        "question": itemgetter("question"),
        "language": itemgetter("language"),
    }
    | prompt
    | model
    | StrOutputParser()
)

chain.invoke({"question": "where did harrison work", "language": "italian"})
```

## 并行化步骤

RunnableParallel（又名 RunnableMap）使得在并行执行多个 Runnables 并将这些 Runnables 的输出作为一个映射返回变得容易。

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI

model = ChatOpenAI()
joke_chain = ChatPromptTemplate.from_template("tell me a joke about {topic}") | model
poem_chain = (
    ChatPromptTemplate.from_template("write a 2-line poem about {topic}") | model
)

map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)

map_chain.invoke({"topic": "bear"})
```

## 并行处理

RunnableParallel 也适用于并行运行独立的进程，因为映射中的每个 Runnable 都会并行执行。例如，我们可以看到我们之前的 `joke_chain`、`poem_chain` 和 `map_chain` 都具有大致相同的运行时间，尽管 `map_chain` 执行了这两个任务。

```python
%%timeit

joke_chain.invoke({"topic": "bear"})
```

```python
%%timeit

poem_chain.invoke({"topic": "bear"})
```

```python
%%timeit

map_chain.invoke({"topic": "bear"})
```

