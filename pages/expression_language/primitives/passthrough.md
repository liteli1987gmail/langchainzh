# 将数据传递

RunnablePassthrough本身允许你传递未改变的输入。这通常与RunnableParallel一起使用，以将数据传递到映射中的新键。

请参考下面的示例：

```python
%pip install --upgrade --quiet  langchain langchain-openai
```

```python
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

runnable = RunnableParallel(
    passed=RunnablePassthrough(),
    modified=lambda x: x["num"] + 1,
)

runnable.invoke({"num": 1})
```

如上所示，`passed`键被调用了`RunnablePassthrough()`，所以它简单地将 `{'num': 1}`传递了下去。

我们还在映射中设置了一个带有`modified`键的第二个键。这使用lambda函数设置一个单独的值，将1添加到num中，结果是`modified`键的值为`2`。

## 检索示例

在下面的示例中，我们看到了一个使用`RunnablePassthrough`和`RunnableParallel`的用例。

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

在这里，prompt的输入需要是一个具有"context"和"question"键的映射。用户输入只是问题。所以我们需要使用检索器获取上下文，并将用户输入通过"question"键传递。在这种情况下，RunnablePassthrough允许我们将用户的问题传递给prompt和model。

------