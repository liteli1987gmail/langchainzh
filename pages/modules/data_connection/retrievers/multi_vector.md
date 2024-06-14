# 多向量检索工具

在一个文档中存储多个向量通常是有益的。有多种情况下这是有益的。LangChain提供了一个基本的`MultiVectorRetriever`，使得查询这种类型的设置变得简单。创建多个向量的复杂性主要是在于如何创建每个文档的多个向量。本笔记本介绍了创建这些向量和使用`MultiVectorRetriever`的一些常见方法。

创建每个文档的多个向量的方法包括：

- 较小的块：将一个文档拆分为较小的块，并对其进行嵌入（这是ParentDocumentRetriever）。
- 摘要：为每个文档创建摘要，将其与文档一起嵌入（或者替换文档）。
- 假设性问题：为每个文档创建假设性问题，将其与文档一起嵌入（或者替换文档）。

请注意，这还可以使用另一种向量嵌入的方法 - 手动方式。这非常好，因为您可以明确地添加应该导致恢复文档的问题或查询，从而更好地控制检索过程。

```python
from langchain.retrievers.multi_vector import MultiVectorRetriever
```

```python
from langchain.storage import InMemoryByteStore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
```

```python
loaders = [
    TextLoader("../../paul_graham_essay.txt"),
    TextLoader("../../state_of_the_union.txt"),
]
docs = []
for loader in loaders:
    docs.extend(loader.load())
text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000)
docs = text_splitter.split_documents(docs)
```

## 较小的块

通常情况下，检索较大块的信息，但嵌入较小块可能是有用的。这样可以尽可能接近地捕捉语义含义，同时在下游传递尽可能多的上下文。请注意，这就是`ParentDocumentRetriever`所做的。以下是我们对其内部操作的演示。

```python
# 用于索引子块的向量存储
vectorstore = Chroma(
    collection_name="full_documents", embedding_function=OpenAIEmbeddings()
)
# 父文档的存储层
store = InMemoryByteStore()
id_key = "doc_id"
# 检索器（初始为空）
retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    byte_store=store,
    id_key=id_key,
)
import uuid

doc_ids = [str(uuid.uuid4()) for _ in docs]
```

```python
# 用于创建较小块的拆分器
child_text_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
```

```python
sub_docs = []
for i, doc in enumerate(docs):
    _id = doc_ids[i]
    _sub_docs = child_text_splitter.split_documents([doc])
    for _doc in _sub_docs:
        _doc.metadata[id_key] = _id
    sub_docs.extend(_sub_docs)
```

```python
retriever.vectorstore.add_documents(sub_docs)
retriever.docstore.mset(list(zip(doc_ids, docs)))
```

```python
# Vectorstore单独检索小块
retriever.vectorstore.similarity_search("justice breyer")[0]
```

```python
# 检索器返回较大的块
len(retriever.get_relevant_documents("justice breyer")[0].page_content)
```

检索器在向量数据库上执行的默认搜索类型是相似度搜索。LangChain向量存储还支持通过[最大边际相关度（MMR）]进行搜索（https://api.python.langchain.com/en/latest/vectorstores/langchain_core.vectorstores.VectorStore.html#langchain_core.vectorstores.VectorStore.max_marginal_relevance_search），所以如果您希望使用这种方法，只需将`search_type`属性设置如下：

```python
from langchain.retrievers.multi_vector import SearchType

retriever.search_type = SearchType.mmr

len(retriever.get_relevant_documents("justice breyer")[0].page_content)
```

## 摘要

摘要通常可以更准确地概括块的内容，从而实现更好的检索。这里我们展示如何创建摘要，然后将其嵌入。

```python
import uuid

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
```

```python
chain = (
    {"doc": lambda x: x.page_content}
    | ChatPromptTemplate.from_template("Summarize the following document:\n\n{doc}")
    | ChatOpenAI(max_retries=0)
    | StrOutputParser()
)
```

```python
summaries = chain.batch(docs, {"max_concurrency": 5})
```

```python
# 用于索引子块的向量存储
vectorstore = Chroma(collection_name="summaries", embedding_function=OpenAIEmbeddings())
# 父文档的存储层
store = InMemoryByteStore()
id_key = "doc_id"
# 检索器（初始为空）
retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    byte_store=store,
    id_key=id_key,
)
doc_ids = [str(uuid.uuid4()) for _ in docs]
```

```python
summary_docs = [
    Document(page_content=s, metadata={id_key: doc_ids[i]})
    for i, s in enumerate(summaries)
]
```

```python
retriever.vectorstore.add_documents(summary_docs)
retriever.docstore.mset(list(zip(doc_ids, docs)))
```

```python
# # We can also add the original chunks to the vectorstore if we so want
# for i, doc in enumerate(docs):
#     doc.metadata[id_key] = doc_ids[i]
# retriever.vectorstore.add_documents(docs)
```

```python
sub_docs = vectorstore.similarity_search("justice breyer")
```

```python
sub_docs[0]
```

```python
retrieved_docs = retriever.get_relevant_documents("justice breyer")
```

```python
len(retrieved_docs[0].page_content)
```

我以上对原文内容进行了翻译，请查看替换后的结果，如果有其他问题，请随时告诉我。=======

## 假设查询

LLM还可以用于生成针对特定文档可能被提出的假设性问题列表。然后可以嵌入这些问题

```python
functions = [
    {
        "name": "hypothetical_questions",
        "description": "生成假设性问题",
        "parameters": {
            "type": "object",
            "properties": {
                "questions": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
            "required": ["questions"],
        },
    }
]
```


```python
from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser

chain = (
    {"doc": lambda x: x.page_content}
    # 只要求3个假设性问题，但可以进行调整
    | ChatPromptTemplate.from_template(
        "生成一个包含3个假设性问题的列表，以下文档可以用来回答这些问题:\n\n{doc}"
    )
    | ChatOpenAI(max_retries=0, model="gpt-4").bind(
        functions=functions, function_call={"name": "hypothetical_questions"}
    )
    | JsonKeyOutputFunctionsParser(key_name="questions")
)
```


```python
chain.invoke(docs[0])
```




    ["作者的编程初体验是什么样的？",
     '为什么作者在研究生阶段将注意力从AI转移到Lisp？',
     '是什么导致作者考虑放弃计算机科学而转向艺术领域？']




```python
hypothetical_questions = chain.batch(docs, {"max_concurrency": 5})
```


```python
# 用于对子块进行索引的向量存储
vectorstore = Chroma(
    collection_name="假设性问题", embedding_function=OpenAIEmbeddings()
)
# 用于存储父文档的存储层
store = InMemoryByteStore()
id_key = "doc_id"
# 检索器（开始时为空）
retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    byte_store=store,
    id_key=id_key,
)
doc_ids = [str(uuid.uuid4()) for _ in docs]
```


```python
question_docs = []
for i, question_list in enumerate(hypothetical_questions):
    question_docs.extend(
        [Document(page_content=s, metadata={id_key: doc_ids[i]}) for s in question_list]
    )
```


```python
retriever.vectorstore.add_documents(question_docs)
retriever.docstore.mset(list(zip(doc_ids, docs)))
```


```python
sub_docs = vectorstore.similarity_search("布赖尔法官")
```


```python
sub_docs
```




    [Document(page_content='谁被提名担任美国最高法院法官？', metadata={'doc_id': '0b3a349e-c936-4e77-9c40-0a39fc3e07f0'}),
     Document(page_content='2010年罗伯特·莫里斯对文档作者的建议的背景和内容是什么？', metadata={'doc_id': 'b2b2cdca-988a-4af1-ba47-46170770bc8c'}),
     Document(page_content='个人情况如何影响放弃领导Y Combinator的决定？', metadata={'doc_id': 'b2b2cdca-988a-4af1-ba47-46170770bc8c'}),
     Document(page_content='作者在1999年夏季离开Yahoo的原因是什么？', metadata={'doc_id': 'ce4f4981-ca60-4f56-86f0-89466de62325'})]




```python
retrieved_docs = retriever.get_relevant_documents("布赖尔法官")
```


```python
len(retrieved_docs[0].page_content)
```




    9194





