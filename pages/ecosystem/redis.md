


 Redis
 [#](#redis "Permalink to this headline")
=================================================



 This page covers how to use the
 [Redis](https://redis.com) 
 ecosystem within LangChain.
It is broken into two parts: installation and setup, and then references to specific Redis wrappers.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Redis Python SDK with
 `pip
 

 install
 

 redis`





 Wrappers
 [#](#wrappers "Permalink to this headline")
-------------------------------------------------------



### 
 Cache
 [#](#cache "Permalink to this headline")



 The Cache wrapper allows for
 [Redis](https://redis.io) 
 to be used as a remote, low-latency, in-memory cache for LLM prompts and responses.
 



#### 
 Standard Cache
 [#](#standard-cache "Permalink to this headline")



 The standard cache is the Redis bread & butter of use case in production for both
 [open source](https://redis.io) 
 and
 [enterprise](https://redis.com) 
 users globally.
 



 To import this cache:
 





```
from langchain.cache import RedisCache

```




 To use this cache with your LLMs:
 





```
import langchain
import redis

redis_client = redis.Redis.from_url(...)
langchain.llm_cache = RedisCache(redis_client)

```





#### 
 Semantic Cache
 [#](#semantic-cache "Permalink to this headline")



 Semantic caching allows users to retrieve cached prompts based on semantic similarity between the user input and previously cached results. Under the hood it blends Redis as both a cache and a vectorstore.
 



 To import this cache:
 





```
from langchain.cache import RedisSemanticCache

```




 To use this cache with your LLMs:
 





```
import langchain
import redis

# use any embedding provider...
from tests.integration_tests.vectorstores.fake_embeddings import FakeEmbeddings

redis_url = "redis://localhost:6379"

langchain.llm_cache = RedisSemanticCache(
    embedding=FakeEmbeddings(),
    redis_url=redis_url
)

```






### 
 VectorStore
 [#](#vectorstore "Permalink to this headline")



 The vectorstore wrapper turns Redis into a low-latency
 [vector database](https://redis.com/solutions/use-cases/vector-database/) 
 for semantic search or LLM content retrieval.
 



 To import this vectorstore:
 





```
from langchain.vectorstores import Redis

```




 For a more detailed walkthrough of the Redis vectorstore wrapper, see
 [this notebook](../modules/indexes/vectorstores/examples/redis)
 .
 




### 
 Retriever
 [#](#retriever "Permalink to this headline")



 The Redis vector store retriever wrapper generalizes the vectorstore class to perform low-latency document retrieval. To create the retriever, simply call
 `.as_retriever()`
 on the base vectorstore class.
 




### 
 Memory
 [#](#memory "Permalink to this headline")



 Redis can be used to persist LLM conversations.
 



#### 
 Vector Store Retriever Memory
 [#](#vector-store-retriever-memory "Permalink to this headline")



 For a more detailed walkthrough of the
 `VectorStoreRetrieverMemory`
 wrapper, see
 [this notebook](../modules/memory/types/vectorstore_retriever_memory)
 .
 




#### 
 Chat Message History Memory
 [#](#chat-message-history-memory "Permalink to this headline")



 For a detailed example of Redis to cache conversation message history, see
 [this notebook](../modules/memory/examples/redis_chat_message_history)
 .
 







