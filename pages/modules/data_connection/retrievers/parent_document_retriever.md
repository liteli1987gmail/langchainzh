# 父文档检索器

在拆分文档以进行检索时，通常存在相互矛盾的需求：

1. 您可能希望拥有小型文档，以便它们的嵌入可以最准确地反映其含义。如果太长，嵌入可能会失去含义。
2. 您希望有足够长的文档，以保留每个块的上下文。

`ParentDocumentRetriever`通过拆分和存储小型数据块来实现这种平衡。在检索过程中，它首先获取小块，然后查找这些块的父ID并返回那些较大的文档。

请注意，“父文档”指的是小块来源的文档。这可以是整个原始文档，也可以是较大的块。

```python
from langchain.retrievers import ParentDocumentRetriever
```

```python
from langchain.storage import InMemoryStore
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
```

## 检索完整文档

在此模式下，我们希望检索完整文档。因此，我们只指定一个子分割器。

```python
# 此文本分割器用于创建子文档
child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
# 用于索引子块的向量存储
vectorstore = Chroma(
    collection_name="full_documents", embedding_function=OpenAIEmbeddings()
)
# 父文档的存储层
store = InMemoryStore()
retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=store,
    child_splitter=child_splitter,
)
```

```python
retriever.add_documents(docs, ids=None)
```

这应该会产生两个键，因为我们添加了两个文档。

```python
list(store.yield_keys())
```

让我们现在调用向量存储搜索功能 - 我们应该看到它返回小块（因为我们存储了小块）。

```python
sub_docs = vectorstore.similarity_search("justice breyer")
```

```python
print(sub_docs[0].page_content)
```

今晚，我想向献身于为这个国家服务的人表示敬意：司法部长斯蒂芬·布雷耶（Stephen Breyer）是一位陆军退伍军人、宪法学者和即将退休的美国最高法院大法官。司法部长布雷耶，感谢您的服务。

总统拥有的最严肃的宪法责任之一是提名某人担任美国最高法院的法官。

让我们现在从整体检索器中检索。这应该返回大文档 - 因为它返回了包含小块的文档。

```python
retrieved_docs = retriever.get_relevant_documents("justice breyer")
```

```python
len(retrieved_docs[0].page_content)
```

## 检索较大块

有时，完整文档可能太大，因此不希望按原样检索它们。在这种情况下，我们真正想要做的是首先将原始文档拆分为较大块，然后将其拆分为较小块。然后我们对小块进行索引，但在检索时我们检索较大块（但仍然不是完整文档）。

```python
# 用于创建父文档的文本分割器
parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000)
# 用于创建子文档的文本分割器
# 它应该创建比父文档小的文档
child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
# 用于索引子块的向量存储
vectorstore = Chroma(
    collection_name="split_parents", embedding_function=OpenAIEmbeddings()
)
# 父文档的存储层
store = InMemoryStore()
```

```python
retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)
```

```python
retriever.add_documents(docs)
```

我们可以看到现在有远远不止两个文档 - 这些是较大的块。

```python
len(list(store.yield_keys()))
```

让我们确保底层向量存储仍然检索小块。

```python
sub_docs = vectorstore.similarity_search("justice breyer")
```

```python
print(sub_docs[0].page_content)
```

今晚，我想向献身于为这个国家服务的人表示敬意：司法部长斯蒂芬·布雷耶（Stephen Breyer）是一位陆军退伍军人、宪法学者和即将退休的美国最高法院大法官。司法部长布雷耶，感谢您的服务。

总统拥有的最严肃的宪法责任之一是提名某人担任美国最高法院的法官。=======

    在一个个州里，已经通过了新法律，不仅压制选举权，还颠覆了整个选举过程。
    
    我们不能让这种事情发生。
    
    今晚。我呼吁参议院：通过《自由选举法》。通过《约翰·刘易斯选举权法案》。还有，通过《披露法案》，这样美国人就能知道谁在资助我们的选举。
    
    今晚，我想向一个致力于为这个国家服务的人致敬：司法史蒂芬·布雷耶—一名陆军退伍军人、宪法学者，即将退休的美国最高法院大法官。司法布雷耶，感谢您的服务。
    
    总统最严肃的宪法责任之一是提名人选担任美国最高法院法官。
    
    我在4天前就已经做到了，当时我提名了联邦上诉法院法官凯坦吉·布朗·杰克逊。她是我们国家顶尖的法律智慧之一，将继承布雷耶大法官的卓越遗产。
    
    前私人执业的顶尖诉讼律师。前联邦公共辩护人。出自公立学校教育和警察家庭。一个取得共识的构建者。自被提名以来，她得到了广泛的支持—从警察兄弟会到民主党和共和党任命的前法官。

    如果我们要推动自由和正义，我们需要确保边境安全并修复移民系统。
    
    我们可以两者兼顾。在我们的边境，我们已经安装了像尖端扫描仪这样的新技术，以更好地检测走私毒品。
    
    我们与墨西哥和危地马拉建立了联合巡逻，以抓捕更多的人口贩运者。
    
    我们正在设立专门的移民法官，这样逃离迫害和暴力的家庭就可以更快地审理他们的案件。
    
    我们正在确保承诺并支持南美和中美的伙伴们接纳更多的难民，并确保他们自己的边界安全。