# 上下文压缩

检索中的一个挑战通常是您在将数据导入系统时不知道文档存储系统将面临的具体查询。这意味着与查询相关的信息可能深藏在包含大量无关文本的文档中。将完整文档通过应用程序传递可能会导致更昂贵的LLM调用和更差的响应。

上下文压缩旨在解决此问题。思路很简单：不是立即返回检索到的文档，而是使用给定查询的上下文对其进行压缩，以便只返回相关信息。这里的“压缩”既指单个文档内容的压缩，也指整个文档的过滤。

要使用上下文压缩检索器，您需要：
- 一个基本检索器
- 一个文档压缩器

上下文压缩检索器将查询传递给基本检索器，获取初始文档并将其通过文档压缩器传递。文档压缩器接受文档列表，通过减少文档内容或完全删除文档来缩短列表。

![](https://drive.google.com/uc?id=1CtNgWODXZudxAWSRiWgSGEoTNrUFT98v)

## 入门指南

```python
# 用于打印文档的辅助函数


def pretty_print_docs(docs):
    print(
        f"\n{'-' * 100}\n".join(
            [f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]
        )
    )
```

## 使用简单的向量存储检索器
让我们从初始化一个简单的向量存储检索器开始，并存储2023年的国情咨文（分块）。我们可以看到，给定一个示例问题，我们的检索器返回一个或两个相关文档和几个不相关文档。即使相关文档中也包含大量不相关信息。



```python
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

documents = TextLoader("../../state_of_the_union.txt").load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
retriever = FAISS.from_documents(texts, OpenAIEmbeddings()).as_retriever()

docs = retriever.get_relevant_documents(
    "What did the president say about Ketanji Brown Jackson"
)
pretty_print_docs(docs)
```

    Document 1:
    
    Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 
    
    Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 
    
    One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 
    
    And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.
    ----------------------------------------------------------------------------------------------------
    Document 2:
    
    A former top litigator in private practice. A former federal public defender. And from a family of public school educators and police officers. A consensus builder. Since she’s been nominated, she’s received a broad range of support—from the Fraternal Order of Police to former judges appointed by Democrats and Republicans. 
    
    And if we are to advance liberty and justice, we need to secure the Border and fix the immigration system. 
    
    We can do both. At our border, we’ve installed new technology like cutting-edge scanners to better detect drug smuggling.  
    
    We’ve set up joint patrols with Mexico and Guatemala to catch more human traffickers.  
    
    We’re putting in place dedicated immigration judges so families fleeing persecution and violence can have their cases heard faster. 
    
    We’re securing commitments and supporting partners in South and Central America to host more refugees and secure their own borders.
    ----------------------------------------------------------------------------------------------------
    Document 3:
    
    And for our LGBTQ+ Americans, let’s finally get the bipartisan Equality Act to my desk. The onslaught of state laws targeting transgender Americans and their families is wrong. 
    
    As I said last year, especially to our younger transgender Americans, I will always have your back as your President, so you can be yourself and reach your God-given potential. 
    
    While it often appears that we never agree, that isn’t true. I signed 80 bipartisan bills into law last year. From preventing government shutdowns to protecting Asian-Americans from still-too-common hate crimes to reforming military justice. 
    
    And soon, we’ll strengthen the Violence Against Women Act that I first wrote three decades ago. It is important for us to show the nation that we can come together and do big things. 
    
    So tonight I’m offering a Unity Agenda for the Nation. Four big things we can do together.  
    
    First, beat the opioid epidemic.
    ----------------------------------------------------------------------------------------------------
    Document 4:
    
    Tonight, I’m announcing a crackdown on these companies overcharging American businesses and consumers. 
    
    And as Wall Street firms take over more nursing homes, quality in those homes has gone down and costs have gone up.  
    
    That ends on my watch. 
    
    Medicare is going to set higher standards for nursing homes and make sure your loved ones get the care they deserve and expect. 
    
    We’ll also cut costs and keep the economy going strong by giving workers a fair shot, provide more training and apprenticeships, hire them based on their skills not degrees. 
    
    Let’s pass the Paycheck Fairness Act and paid leave.  
    
    Raise the minimum wage to $15 an hour and extend the Child Tax Credit, so no one has to raise a family in poverty. 
    
    Let’s increase Pell Grants and increase our historic support of HBCUs, and invest in what Jill—our First Lady who teaches full-time—calls America’s best-kept secret: community colleges.
    

## 使用带有`LLMChainExtractor`的上下文压缩
现在让我们用`ContextualCompressionRetriever`包装我们的基本检索器。我们添加一个`LLMChainExtractor`，它将迭代最初返回的文档，并从每个文档中提取与查询相关的内容。



```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import OpenAI

llm = OpenAI(temperature=0)
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriever
)

compressed_docs = compression_retriever.get_relevant_documents(
    "What did the president say about Ketanji Jackson Brown"
)
pretty_print_docs(compressed_docs)
```

    Document 1:
    
    I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson.
    

## 更多内置压缩器：过滤器
### `LLMChainFilter`
`LLMChainFilter`是一个略微简单但更强大的压缩器，它使用LLM链来决定最初检索到的文档中应过滤掉哪些文档，哪些文档应返回，而不更改文档内容。



```python
from langchain.retrievers.document_compressors import LLMChainFilter

_filter = LLMChainFilter.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=_filter, base_retriever=retriever
)

compressed_docs = compression_retriever.get_relevant_documents(
    "What did the president say about Ketanji Jackson Brown"
)
pretty_print_docs(compressed_docs)
```

    Document 1:
    
    Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 
    
    Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 
    
    One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 
    
    And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.
    

### `EmbeddingsFilter`

在每个检索到的文档上进行额外的LLM调用是昂贵且慢的。`EmbeddingsFilter`提供了一种更便宜更快的选项，它通过嵌入文档和查询，并仅返回那些嵌入与查询足够相似的文档。



```python
from langchain.retrievers.document_compressors import EmbeddingsFilter
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
embeddings_filter = EmbeddingsFilter(embeddings=embeddings, similarity_threshold=0.76)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=embeddings_filter, base_retriever=retriever
)

compressed_docs = compression_retriever.get_relevant_documents(
    "What did the president say about Ketanji Jackson Brown"
)
pretty_print_docs(compressed_docs)
```

    Document 1:
    
    Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 
    
    Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 
    
    One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 
    
    And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.
    ----------------------------------------------------------------------------------------------------
    Document 2:
    
    A former top litigator in private practice. A former federal public defender. And from a family of public school educators and police officers. A consensus builder. Since she’s been nominated, she’s received a broad range of support—from the Fraternal Order of Police to former judges appointed by Democrats and Republicans. 
    
    And if we are to advance liberty and justice, we need to secure the Border and fix the immigration system. 
    
    We can do both. At our border, we’ve installed new technology like cutting-edge scanners to better detect drug smuggling.  
    
    We’ve set up joint patrols with Mexico and Guatemala to catch more human traffickers.  
    
    We’re putting in place dedicated immigration judges so families fleeing persecution and violence can have their cases heard faster. 
    
    We’re securing commitments and supporting partners in South and Central America to host more refugees and secure their own borders.
    ----------------------------------------------------------------------------------------------------
    Document 3:
    
    And for our LGBTQ+ Americans, let’s finally get the bipartisan Equality Act to my desk. The onslaught of state laws targeting transgender Americans and their families is wrong. 
    
    As I said last year, especially to our younger transgender Americans, I will always have your back as your President, so you can be yourself and reach your God-given potential. 
    
    While it often appears that we never agree, that isn’t true. I signed 80 bipartisan bills into law last year. From preventing government shutdowns to protecting Asian-Americans from still-too-common hate crimes to reforming military justice. 
    
    And soon, we’ll strengthen the Violence Against Women Act that I first wrote three decades ago. It is important for us to show the nation that we can come together and do big things. 
    
    So tonight I’m offering a Unity-Agenda for the Nation. Four big things we can do together.  
    
    First, beat the opioid epidemic.
    


## 将多个压缩器依次组合在一起
使用`DocumentCompressorPipeline`，我们还可以轻松地将多个压缩器依次组合在一起。除了压缩器之外，我们还可以向管线中添加`BaseDocumentTransformer`，这些转换器不执行任何上下文压缩，而只是对一组文档进行一些转换。例如，`TextSplitter`可以用作文档转换器，将文档拆分为较小的片段，而`EmbeddingsRedundantFilter`可以用于基于文档之间的嵌入相似性来过滤冗余文档。

在下面的示例中，我们首先将文档拆分为较小的块，然后删除冗余文档，然后根据与查询相关性进行过滤。

```python
from langchain.retrievers.document_compressors import DocumentCompressorPipeline
from langchain_community.document_transformers import EmbeddingsRedundantFilter
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=0, separator=". ")
redundant_filter = EmbeddingsRedundantFilter(embeddings=embeddings)
relevant_filter = EmbeddingsFilter(embeddings=embeddings, similarity_threshold=0.76)
pipeline_compressor = DocumentCompressorPipeline(
    transformers=[splitter, redundant_filter, relevant_filter]
)
```


```python
compression_retriever = ContextualCompressionRetriever(
    base_compressor=pipeline_compressor, base_retriever=retriever
)

compressed_docs = compression_retriever.get_relevant_documents(
    "What did the president say about Ketanji Jackson Brown"
)
pretty_print_docs(compressed_docs)
```

    Document 1:
    
    一个总统最严肃的宪法责任之一是提名某人担任美国最高法院的法官。
    
    我在4天前做到了这一点，当时我提名了联邦上诉法院法官Ketanji Brown Jackson
    ----------------------------------------------------------------------------------------------------
    Document 2:
    
    正如我去年所说，特别是对我们年轻的跨性别美国人，作为你们的总统，我会永远支持你们，让你们做自己，并实现上帝赋予你们的潜力。
    
    尽管我们经常出现分歧，但事实并非如此。去年，我签署了80项跨党派法案
    ----------------------------------------------------------------------------------------------------
    Document 3:
    
    一位曾在私人执业中担任领先辩护律师。一位前联邦公共辩护人。来自一系列公立学校教育工作者和警察。一个达成共识的人
    ----------------------------------------------------------------------------------------------------
    Document 4:
    
    自提名以来，她得到了广泛的支持——从警察友爱协会到民主党和共和党任命的前法官。
    
    如果我们要推进自由和正义，我们需要保护边境并修复移民制度。
    
    我们两者都能做到
    


```python

```