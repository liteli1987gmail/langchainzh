


 Getting Started
 [#](#getting-started "Permalink to this headline")
=====================================================================



 This notebook showcases basic functionality related to VectorStores. A key part of working with vectorstores is creating the vector to put in them, which is usually created via embeddings. Therefore, it is recommended that you familiarize yourself with the
 
 embedding notebook
 
 before diving into this.
 



 This covers generic high level functionality related to all vector stores.
 







```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

```










```
with open('../../state_of_the_union.txt') as f:
    state_of_the_union = f.read()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(state_of_the_union)

embeddings = OpenAIEmbeddings()

```










```
docsearch = Chroma.from_texts(texts, embeddings)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)

```








```
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.

```










```
print(docs[0].page_content)

```








```
In state after state, new laws have been passed, not only to suppress the vote, but to subvert entire elections. 

We cannot let this happen. 

Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```







 Add texts
 [#](#add-texts "Permalink to this headline")
---------------------------------------------------------



 You can easily add text to a vectorstore with the
 `add_texts`
 method. It will return a list of document IDs (in case you need to use them downstream).
 







```
docsearch.add_texts(["Ankush went to Princeton"])

```








```
['a05e3d0c-ab40-11ed-a853-e65801318981']

```










```
query = "Where did Ankush go to college?"
docs = docsearch.similarity_search(query)

```










```
docs[0]

```








```
Document(page_content='Ankush went to Princeton', lookup_str='', metadata={}, lookup_index=0)

```








 From Documents
 [#](#from-documents "Permalink to this headline")
-------------------------------------------------------------------



 We can also initialize a vectorstore from documents directly. This is useful when we use the method on the text splitter to get documents directly (handy when the original documents have associated metadata).
 







```
documents = text_splitter.create_documents([state_of_the_union], metadatas=[{"source": "State of the Union"}])

```










```
docsearch = Chroma.from_documents(documents, embeddings)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)

```








```
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.

```










```
print(docs[0].page_content)

```








```
In state after state, new laws have been passed, not only to suppress the vote, but to subvert entire elections. 

We cannot let this happen. 

Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```








