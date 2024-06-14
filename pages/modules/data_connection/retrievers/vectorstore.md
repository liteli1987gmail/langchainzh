# 向量存储支持的检索器

向量存储检索器是使用向量存储来检索文档的检索器。它是对向量存储类的轻量级包装，以使其符合检索器接口。
它使用向量存储实现的搜索方法，如相似性搜索和MMR，来查询向量存储中的文本。

一旦构建了向量存储，构建一个检索器非常容易。让我们通过一个示例来说明。



```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("../../state_of_the_union.txt")
```


```python
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embeddings)
```


```python
retriever = db.as_retriever()
```


```python
docs = retriever.get_relevant_documents("关于Ketanji Brown Jackson，他说了什么")
```

## 最大边际相关检索
默认情况下，向量存储检索器使用相似性搜索。如果底层向量存储支持最大边际相关搜索，您可以将其指定为搜索类型。




```python
retriever = db.as_retriever(search_type="mmr")
```


```python
docs = retriever.get_relevant_documents("关于Ketanji Brown Jackson，他说了什么")
```


## 相似性分数阈值检索

您还可以设置一个检索方法，设置一个相似性分数阈值，并仅返回得分高于该阈值的文档。


```python
retriever = db.as_retriever(
    search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.5}
)
```


```python
docs = retriever.get_relevant_documents("关于Ketanji Brown Jackson，他说了什么")
```


## 指定top k
您还可以指定搜索参数，例如 `k`，在进行检索时使用。



```python
retriever = db.as_retriever(search_kwargs={"k": 1})
```


```python
docs = retriever.get_relevant_documents("关于Ketanji Brown Jackson，他说了什么")
len(docs)
```




    1






