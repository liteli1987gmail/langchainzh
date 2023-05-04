

如何缓存LLM调用[#](#how-to-cache-llm-calls "跳转到本标题的永久链接")
===================================================

本笔记介绍如何缓存单个LLM调用的结果。

```
from langchain.llms import OpenAI

```

内存缓存[#](#in-memory-cache "跳转到本标题的永久链接")
---------------------------------------

```
import langchain
from langchain.cache import InMemoryCache
langchain.llm_cache = InMemoryCache()

```

```
# To make the caching really obvious, lets use a slower model.
llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)

```

```
%%time
# The first time, it is not yet in cache, so it should take longer
llm("Tell me a joke")

```

```
CPU times: user 26.1 ms, sys: 21.5 ms, total: 47.6 ms
Wall time: 1.68 s

```

```
'  Why did the chicken cross the road?  To get to the other side.'

```

```
%%time
# The second time it is, so it goes faster
llm("Tell me a joke")

```

```
CPU times: user 238 µs, sys: 143 µs, total: 381 µs
Wall time: 1.76 ms

```

```
'  Why did the chicken cross the road?  To get to the other side.'

```

SQLite缓存[#](#sqlite-cache "跳转到本标题的永久链接")
----------------------------------------

```
!rm .langchain.db

```

```
# We can do the same thing with a SQLite cache
from langchain.cache import SQLiteCache
langchain.llm_cache = SQLiteCache(database_path=".langchain.db")

```

```
%%time
# The first time, it is not yet in cache, so it should take longer
llm("Tell me a joke")

```

```
CPU times: user 17 ms, sys: 9.76 ms, total: 26.7 ms
Wall time: 825 ms

```

```
'  Why did the chicken cross the road?  To get to the other side.'

```

```
%%time
# The second time it is, so it goes faster
llm("Tell me a joke")

```

```
CPU times: user 2.46 ms, sys: 1.23 ms, total: 3.7 ms
Wall time: 2.67 ms

```

```
'  Why did the chicken cross the road?  To get to the other side.'

```

Redis缓存[#](#redis-cache "跳转到本标题的永久链接")
--------------------------------------

### 标准缓存[#](#standard-cache "跳转到本标题的永久链接")

使用[Redis](../../../../ecosystem/redis.html)缓存提示和响应。

```
# We can do the same thing with a Redis cache
# (make sure your local Redis instance is running first before running this example)
from redis import Redis
from langchain.cache import RedisCache

langchain.llm_cache = RedisCache(redis_=Redis())

```

```
%%time
# The first time, it is not yet in cache, so it should take longer
llm("Tell me a joke")

```

```
CPU times: user 6.88 ms, sys: 8.75 ms, total: 15.6 ms
Wall time: 1.04 s

```

```
'  Why did the chicken cross the road?  To get to the other side!'

```

```
%%time
# The second time it is, so it goes faster
llm("Tell me a joke")

```

```
CPU times: user 1.59 ms, sys: 610 µs, total: 2.2 ms
Wall time: 5.58 ms

```

```
'  Why did the chicken cross the road?  To get to the other side!'

```

### 语义缓存[#](#semantic-cache "跳转到本标题的永久链接")

使用[Redis](../../../../ecosystem/redis.html)缓存提示和响应，并根据语义相似性评估命中率。

```
from langchain.embeddings import OpenAIEmbeddings
from langchain.cache import RedisSemanticCache

langchain.llm_cache = RedisSemanticCache(
    redis_url="redis://localhost:6379",
    embedding=OpenAIEmbeddings()
)

```

```
%%time
# The first time, it is not yet in cache, so it should take longer
llm("Tell me a joke")

```

```
CPU times: user 351 ms, sys: 156 ms, total: 507 ms
Wall time: 3.37 s

```

```
"  Why don't scientists trust atoms?\nBecause they make up everything."

```

```
%%time
# The second time, while not a direct hit, the question is semantically similar to the original question,
# so it uses the cached result!
llm("Tell me one joke")

```

```
CPU times: user 6.25 ms, sys: 2.72 ms, total: 8.97 ms
Wall time: 262 ms

```

```
"  Why don't scientists trust atoms?\nBecause they make up everything."

```

GPTCache[#](#gptcache "到这个标题的永久链接")
-----------------------------------

我们可以使用[GPTCache](https://github.com/zilliztech/GPTCache)进行精确匹配缓存，或者根据语义相似性缓存结果

让我们首先从一个精确匹配的例子开始

```
import gptcache
from gptcache.processor.pre import get_prompt
from gptcache.manager.factory import get_data_manager
from langchain.cache import GPTCache

# Avoid multiple caches using the same file, causing different llm model caches to affect each other
i = 0
file_prefix = "data_map"

def init_gptcache_map(cache_obj: gptcache.Cache):
    global i
    cache_path = f'{file_prefix}_{i}.txt'
    cache_obj.init(
        pre_embedding_func=get_prompt,
        data_manager=get_data_manager(data_path=cache_path),
    )
    i += 1

langchain.llm_cache = GPTCache(init_gptcache_map)

```

```
%%time
# The first time, it is not yet in cache, so it should take longer
llm("Tell me a joke")

```

```
CPU times: user 8.6 ms, sys: 3.82 ms, total: 12.4 ms
Wall time: 881 ms

```

```
'  Why did the chicken cross the road?  To get to the other side.'

```

```
%%time
# The second time it is, so it goes faster
llm("Tell me a joke")

```

```
CPU times: user 286 µs, sys: 21 µs, total: 307 µs
Wall time: 316 µs

```

```
'  Why did the chicken cross the road?  To get to the other side.'

```

现在让我们展示一个相似性缓存的例子

```
import gptcache
from gptcache.processor.pre import get_prompt
from gptcache.manager.factory import get_data_manager
from langchain.cache import GPTCache
from gptcache.manager import get_data_manager, CacheBase, VectorBase
from gptcache import Cache
from gptcache.embedding import Onnx
from gptcache.similarity_evaluation.distance import SearchDistanceEvaluation

# Avoid multiple caches using the same file, causing different llm model caches to affect each other
i = 0
file_prefix = "data_map"
llm_cache = Cache()

def init_gptcache_map(cache_obj: gptcache.Cache):
    global i
    cache_path = f'{file_prefix}_{i}.txt'
    onnx = Onnx()
    cache_base = CacheBase('sqlite')
    vector_base = VectorBase('faiss', dimension=onnx.dimension)
    data_manager = get_data_manager(cache_base, vector_base, max_size=10, clean_size=2)
    cache_obj.init(
        pre_embedding_func=get_prompt,
        embedding_func=onnx.to_embeddings,
        data_manager=data_manager,
        similarity_evaluation=SearchDistanceEvaluation(),
    )
    i += 1

langchain.llm_cache = GPTCache(init_gptcache_map)

```

```
%%time
# The first time, it is not yet in cache, so it should take longer
llm("Tell me a joke")

```

```
CPU times: user 1.01 s, sys: 153 ms, total: 1.16 s
Wall time: 2.49 s

```

```
'  Why did the chicken cross the road?  To get to the other side.'

```

```
%%time
# This is an exact match, so it finds it in the cache
llm("Tell me a joke")

```

```
CPU times: user 745 ms, sys: 13.2 ms, total: 758 ms
Wall time: 136 ms

```

```
'  Why did the chicken cross the road?  To get to the other side.'

```

```
%%time
# This is not an exact match, but semantically within distance so it hits!
llm("Tell me joke")

```

```
CPU times: user 737 ms, sys: 7.79 ms, total: 745 ms
Wall time: 135 ms

```

```
'  Why did the chicken cross the road?  To get to the other side.'

```

SQLAlchemy缓存[#](#sqlalchemy-cache "到这个标题的永久链接")
-----------------------------------------------

```
# You can use SQLAlchemyCache to cache with any SQL database supported by SQLAlchemy.

# from langchain.cache import SQLAlchemyCache
# from sqlalchemy import create_engine

# engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
# langchain.llm_cache = SQLAlchemyCache(engine)

```

### 自定义SQLAlchemy模式[#](#custom-sqlalchemy-schemas "到这个标题的永久链接")

```
# You can define your own declarative SQLAlchemyCache child class to customize the schema used for caching. For example, to support high-speed fulltext prompt indexing with Postgres, use:

from sqlalchemy import Column, Integer, String, Computed, Index, Sequence
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import TSVectorType
from langchain.cache import SQLAlchemyCache

Base = declarative_base()

class FulltextLLMCache(Base):  # type: ignore
 """Postgres table for fulltext-indexed LLM Cache"""

    __tablename__ = "llm_cache_fulltext"
    id = Column(Integer, Sequence('cache_id'), primary_key=True)
    prompt = Column(String, nullable=False)
    llm = Column(String, nullable=False)
    idx = Column(Integer)
    response = Column(String)
    prompt_tsv = Column(TSVectorType(), Computed("to_tsvector('english', llm || ' ' || prompt)", persisted=True))
    __table_args__ = (
        Index("idx_fulltext_prompt_tsv", prompt_tsv, postgresql_using="gin"),
    )

engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
langchain.llm_cache = SQLAlchemyCache(engine, FulltextLLMCache)

```

可选缓存[#](#optional-caching "到这个标题的永久链接")
---------------------------------------

您也可以选择关闭特定LLM的缓存。在下面的示例中，即使启用了全局缓存，我们也关闭了特定LLM的缓存

```
llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2, cache=False)

```

```
%%time
llm("Tell me a joke")

```

```
CPU times: user 5.8 ms, sys: 2.71 ms, total: 8.51 ms
Wall time: 745 ms

```

```
'  Why did the chicken cross the road?  To get to the other side!'

```

```
%%time
llm("Tell me a joke")

```

```
CPU times: user 4.91 ms, sys: 2.64 ms, total: 7.55 ms
Wall time: 623 ms

```

```
'  Two guys stole a calendar. They got six months each.'

```

链式可选缓存[#](#optional-caching-in-chains "到这个标题的永久链接")
---------------------------------------------------

您还可以关闭链中特定节点的缓存。请注意，由于某些接口，通常更容易首先构建链，然后再编辑LLM。

作为示例，我们将加载一个摘要生成器MapReduce链。我们将缓存映射步骤的结果，但在合并步骤中不冻结它。

```
llm = OpenAI(model_name="text-davinci-002")
no_cache_llm = OpenAI(model_name="text-davinci-002", cache=False)

```

```
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain

text_splitter = CharacterTextSplitter()

```

```
with open('../../../state_of_the_union.txt') as f:
    state_of_the_union = f.read()
texts = text_splitter.split_text(state_of_the_union)

```

```
from langchain.docstore.document import Document
docs = [Document(page_content=t) for t in texts[:3]]
from langchain.chains.summarize import load_summarize_chain

```

```
chain = load_summarize_chain(llm, chain_type="map_reduce", reduce_llm=no_cache_llm)

```

```
%%time
chain.run(docs)

```

```
CPU times: user 452 ms, sys: 60.3 ms, total: 512 ms
Wall time: 5.09 s

```

```
'  President Biden is discussing the American Rescue Plan and the Bipartisan Infrastructure Law, which will create jobs and help Americans. He also talks about his vision for America, which includes investing in education and infrastructure. In response to Russian aggression in Ukraine, the United States is joining with European allies to impose sanctions and isolate Russia. American forces are being mobilized to protect NATO countries in the event that Putin decides to keep moving west. The Ukrainians are bravely fighting back, but the next few weeks will be hard for them. Putin will pay a high price for his actions in the long run. Americans should not be alarmed, as the United States is taking action to protect its interests and allies.'

```

当我们再次运行它时，我们会发现它运行得更快，但最终结果不同。这是由于在映射步骤中进行了缓存，但在减少步骤中没有进行缓存。

```
%%time
chain.run(docs)

```

```
CPU times: user 11.5 ms, sys: 4.33 ms, total: 15.8 ms
Wall time: 1.04 s

```

```
'  President Biden is discussing the American Rescue Plan and the Bipartisan Infrastructure Law, which will create jobs and help Americans. He also talks about his vision for America, which includes investing in education and infrastructure.'

```

```
!rm .langchain.db sqlite.db

```

