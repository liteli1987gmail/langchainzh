
RetrievalQAWithSourcesChain
===============


本笔记本介绍如何使用索引对问题进行基于来源的问答。它通过使用`RetrievalQAWithSourcesChain`来完成从索引中查找文档的工作。

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.elastic_vector_search import ElasticVectorSearch
from langchain.vectorstores import Chroma

```

```
with open("../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(state_of_the_union)

embeddings = OpenAIEmbeddings()

```

```
docsearch = Chroma.from_texts(texts, embeddings, metadatas=[{"source": f"{i}-pl"} for i in range(len(texts))])

```

```
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.

```

```
from langchain.chains import RetrievalQAWithSourcesChain

```

```
from langchain import OpenAI

chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(temperature=0), chain_type="stuff", retriever=docsearch.as_retriever())

```

```
chain({"question": "What did the president say about Justice Breyer"}, return_only_outputs=True)

```

```
{'answer': ' The president honored Justice Breyer for his service and mentioned his legacy of excellence.\n',
 'sources': '31-pl'}

```

链式类型[#](#chain-type "此标题的永久链接")
-------------------------------

您可以轻松指定要加载和使用的不同链式类型。有关这些类型的更详细演示，请参见[本笔记本](qa_with_sources）。

有两种加载不同链式类型的方法。首先，您可以在`from_chain_type`方法中指定链式类型参数。这允许您传递要使用的链式类型的名称。例如，在下面的示例中，我们将链式类型更改为`map_reduce`。

```
chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(temperature=0), chain_type="map_reduce", retriever=docsearch.as_retriever())

```

```
chain({"question": "What did the president say about Justice Breyer"}, return_only_outputs=True)

```

```
{'answer': ' The president said "Justice Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service."\n',
 'sources': '31-pl'}

```

The above way allows you to really simply change the chain_type, but it does provide a ton of flexibility over parameters to that chain type. If you want to control those parameters, you can load the chain directly (as you did in [this notebook](qa_with_sources）) and then pass that directly to the the RetrievalQAWithSourcesChain chain with the `combine_documents_chain` parameter. For example:

```
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
qa_chain = load_qa_with_sources_chain(OpenAI(temperature=0), chain_type="stuff")
qa = RetrievalQAWithSourcesChain(combine_documents_chain=qa_chain, retriever=docsearch.as_retriever())

```

```
qa({"question": "What did the president say about Justice Breyer"}, return_only_outputs=True)

```

```
{'answer': ' The president honored Justice Breyer for his service and mentioned his legacy of excellence.\n',
 'sources': '31-pl'}

```

