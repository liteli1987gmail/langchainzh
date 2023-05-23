开始
=============================================================
LangChain 主要关注于构建索引，目标是使用它们作为检索器。为了更好地理解这意味着什么，有必要突出显示基本检索器接口是什么。LangChain 的 baseRetriever 类如下:

```
from abc import ABC, abstractmethod
from typing import List
from langchain.schema import Document

class BaseRetriever(ABC):
    @abstractmethod
    def get_relevant_documents(self, query: str) -> List[Document]:
        """Get texts relevant for a query.

        Args:
            query: string to find relevant texts for

        Returns:
            List of relevant documents
        """
```

就是这么简单! get _ relevant _ document 方法可以按照您认为合适的方式实现。

当然，我们也帮助构建我们认为有用的检索器是什么。我们主要关注的检索器类型是 Vectorstore 检索器。在本指南的其余部分中，我们将关注这一点。

为了理解什么是向量库检索器，理解向量库是什么非常重要。我们来看看。

默认情况下，LangChain 使用 Chroma 作为向量存储来索引和搜索嵌入。要学习本教程，我们首先需要安装 chromadb。

```
pip install chromadb
```

这个例子展示了对文档的问题回答。我们选择这个例子作为开始的例子，因为它很好地组合了许多不同的元素(文本分割器、嵌入、向量存储) ，然后还演示了如何在链中使用它们。

通过文件回答问题包括四个步骤:

    1. 创建索引

    2. 从该索引创建检索器

    3. 创建一个问题回答链

    4. 问问题！

每个步骤都有多个子步骤和可能的配置。在本教程中，我们将主要关注(1)。我们将首先展示这样做的一行程序，然后分解实际发生的情况。

首先，让我们导入一些无论如何都会使用的通用类。

```
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
```
接下来在通用设置中，让我们指定要使用的文档加载程序。您可以在这里下载 state _ of _ the _ union.txt 文件

```
from langchain.document_loaders import TextLoader
loader = TextLoader('../state_of_the_union.txt', encoding='utf8')
```
创建一行索引 
-------------------------------------------------------------


为了尽快开始，我们可以使用 VectorstoreIndexCreator。

```
from langchain.indexes import VectorstoreIndexCreator
```

```
index = VectorstoreIndexCreator().from_loaders([loader])
```

```
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.
```
现在已经创建了索引，我们可以使用它来询问数据的问题！请注意，在引擎盖下，这实际上也在执行一些步骤，我们将在本指南后面介绍这些步骤。

```
query = "What did the president say about Ketanji Brown Jackson"
index.query(query)
```

```
" The president said that Ketanji Brown Jackson is one of the nation's top legal minds, a former top litigator in private practice, a former federal public defender, and from a family of public school educators and police officers. He also said that she is a consensus builder and has received a broad range of support from the Fraternal Order of Police to former judges appointed by Democrats and Republicans."
```
```
query = "What did the president say about Ketanji Brown Jackson"
index.query_with_sources(query)
```

```
{'question': 'What did the president say about Ketanji Brown Jackson',
 'answer': " The president said that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson, one of the nation's top legal minds, to continue Justice Breyer's legacy of excellence, and that she has received a broad range of support from the Fraternal Order of Police to former judges appointed by Democrats and Republicans.\n",
 'sources': '../state_of_the_union.txt'}

```
从 VectorstoreIndexCreator 返回的是 VectorStoreIndexWrapper，它提供了这些优秀的查询和 query _ with _ source 功能。如果我们只是想直接访问向量存储，我们也可以这样做。

```
index.vectorstore
```

```
<langchain.vectorstores.chroma.Chroma at 0x119aa5940>
```

如果我们想要访问 VectorstoreRetriever，我们可以使用:

```
index.vectorstore.as_retriever()
```

```
VectorStoreRetriever(vectorstore=<langchain.vectorstores.chroma.Chroma object at 0x119aa5940>, search_kwargs={})

```

演练
-------------------------------------------------------

好吧，到底是怎么回事? 这个索引是怎么创建的？

这个 VectorstoreIndexCreator 隐藏了很多魔力，这是在做什么？

加载文件后有三个主要步骤:

1. 将文档分割成块

1. 为每个文档创建嵌入

1. 在向量库中存储文档和嵌入

让我们用代码来演示一下

```
documents = loader.load()
```

接下来，我们将把文档分割成块。

```

from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

```

然后，我们将选择要使用的嵌入。

```
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
```

现在我们创建用作索引的向量存储。
```
from langchain.vectorstores import Chroma
db = Chroma.from_documents(texts, embeddings)
```

```
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.
```

这就是创建索引的过程，然后，我们在一个检索接口中公开这个索引。

```
retriever = db.as_retriever()
```

然后，像以前一样，我们创建一个链，并使用它来回答问题！

```
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)
```

```
query = "What did the president say about Ketanji Brown Jackson"
qa.run(query)
```
```
" The President said that Judge Ketanji Brown Jackson is one of the nation's top legal minds, a former top litigator in private practice, a former federal public defender, and from a family of public school educators and police officers. He said she is a consensus builder and has received a broad range of support from organizations such as the Fraternal Order of Police and former judges appointed by Democrats and Republicans."

```

VectorstoreIndexCreator 只是所有这些逻辑的包装器。它可以在它使用的文本分割器、它使用的嵌入以及它使用的向量存储中进行配置。例如，您可以按以下方式配置它:

```
index_creator = VectorstoreIndexCreator(
    vectorstore_cls=Chroma, 
    embedding=OpenAIEmbeddings(),
    text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
)

```

希望这能够突出显示 VectorstoreIndexCreator 的底层正在发生的事情。虽然我们认为用一种简单的方法来创建索引很重要，但是我们也认为了解底下发生了什么也很重要。



