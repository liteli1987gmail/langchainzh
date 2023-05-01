


 Redis
 [#](#redis "Permalink to this headline")
=================================================



> 
> 
> 
> [Redis (Remote Dictionary Server)](https://en.wikipedia.org/wiki/Redis) 
>  is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability.
>  
> 
> 
> 
> 



 This notebook shows how to use functionality related to the
 [Redis vector database](https://redis.com/solutions/use-cases/vector-database/) 
 .
 







```
!pip install redis

```






 We want to use
 `OpenAIEmbeddings`
 so we have to get the OpenAI API Key.
 







```
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

```










```
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.redis import Redis

```










```
from langchain.document_loaders import TextLoader

loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

```










```
rds = Redis.from_documents(docs, embeddings, redis_url="redis://localhost:6379",  index_name='link')

```










```
rds.index_name

```








```
'link'

```










```
query = "What did the president say about Ketanji Brown Jackson"
results = rds.similarity_search(query)
print(results[0].page_content)

```








```
Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```










```
print(rds.add_texts(["Ankush went to Princeton"]))

```








```
['doc:link:d7d02e3faf1b40bbbe29a683ff75b280']

```










```
query = "Princeton"
results = rds.similarity_search(query)
print(results[0].page_content)

```








```
Ankush went to Princeton

```










```
# Load from existing index
rds = Redis.from_existing_index(embeddings, redis_url="redis://localhost:6379", index_name='link')

query = "What did the president say about Ketanji Brown Jackson"
results = rds.similarity_search(query)
print(results[0].page_content)

```








```
Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```







 RedisVectorStoreRetriever
 [#](#redisvectorstoreretriever "Permalink to this headline")
-----------------------------------------------------------------------------------------



 Here we go over different options for using the vector store as a retriever.
 



 There are three different search methods we can use to do retrieval. By default, it will use semantic similarity.
 







```
retriever = rds.as_retriever()

```










```
docs = retriever.get_relevant_documents(query)

```






 We can also use similarity_limit as a search method. This is only return documents if they are similar enough
 







```
retriever = rds.as_retriever(search_type="similarity_limit")

```










```
# Here we can see it doesn't return any results because there are no relevant documents
retriever.get_relevant_documents("where did ankush go to college?")

```








