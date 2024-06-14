# 向链状态中添加值

`RunnablePassthrough.assign(...)` 静态方法接受一个输入值，并将额外的参数传递给分配函数。

当以加法的方式创建一个字典作为后续步骤的输入时，这对于常见的LCEL模式非常有用。

这是一个示例：

```python
%pip install --upgrade --quiet langchain langchain-openai
```

```python
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

runnable = RunnableParallel(
    extra=RunnablePassthrough.assign(mult=lambda x: x["num"] * 3),
    modified=lambda x: x["num"] + 1,
)

runnable.invoke({"num": 1})
```

让我们来解析这里发生的情况。

- 输入链是 `{"num": 1}`。它被传递到 `RunnableParallel` 中，在并行调用传入的可运行对象。
- 调用了 `extra` 键。`RunnablePassthrough.assign()` 保留了输入字典中的原始键 (`{"num": 1}`)，并分配了一个名为 `mult` 的新键。值是 `lambda x: x["num"] * 3)`，即 `3`。因此，结果是 `{"num": 1, "mult": 3}`。
- `{"num": 1, "mult": 3}` 被返回给 `RunnableParallel` 调用，并设置为键 `extra` 的值。
- 同时，调用了 `modified` 键。结果是 `2`，因为 lambda 从其输入中提取了一个名为 `"num"` 的键，并加上了 `1`。

因此，结果是 `{'extra': {'num': 1, 'mult': 3}, 'modified': 2}`。

## 流式传输

这种方法的一个好处是它允许值在可用时立即传递。为了展示这一点，我们将使用 `RunnablePassthrough.assign()` 来立即在检索链中返回源文档：

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

generation_chain = prompt | model | StrOutputParser()

retrieval_chain = {
    "context": retriever,
    "question": RunnablePassthrough(),
} | RunnablePassthrough.assign(output=generation_chain)

stream = retrieval_chain.stream("where did harrison work?")

for chunk in stream:
    print(chunk)
```

我们可以看到，第一个块包含原始的 `"question"`，因为它是立即可用的。第二个块包含 `"context"`，因为检索器排在第二位。最后，`generation_chain` 的输出会根据可用情况以块形式流出。

----