# 缓存
LangChain为LLM提供了一个可选的缓存层。这有两个好处：

它可以通过减少您向LLM提供商发出的API调用次数来节省您的费用，如果您经常多次请求相同的完成。
通过减少您向LLM提供商发出的API调用次数，可以加快应用程序的速度。



```python
from langchain.globals import set_llm_cache
from langchain_openai import OpenAI

# 为了使缓存更加明显，让我们使用一个更慢的模型。
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", n=2, best_of=2)
```


```python
%%time
from langchain.cache import InMemoryCache

set_llm_cache(InMemoryCache())

# 第一次，尚未缓存，所以需要更长的时间
llm.predict("Tell me a joke")
```

    CPU times: user 13.7 ms, sys: 6.54 ms, total: 20.2 ms
    Wall time: 330 ms
    




    "\n\n为什么自行车站不起来呢？因为它双胎！"




```python
%%time
# 第二次时，已缓存，速度更快
llm.predict("Tell me a joke")
```

    CPU times: user 436 µs, sys: 921 µs, total: 1.36 ms
    Wall time: 1.36 ms
    




    "\n\n为什么自行车站不起来呢？因为它双胎！"



## SQLite缓存


```python
!rm .langchain.db
```


```python
# 我们可以使用SQLite缓存做同样的事情
from langchain.cache import SQLiteCache

set_llm_cache(SQLiteCache(database_path=".langchain.db"))
```


```python
%%time
# 第一次，尚未缓存，所以需要更长的时间
llm.predict("Tell me a joke")
```

    CPU times: user 29.3 ms, sys: 17.3 ms, total: 46.7 ms
    Wall time: 364 ms
    




    '\n\n为什么番茄变红了？\n\n因为它看到了沙拉酱！'




```python
%%time
# 第二次时，已缓存，速度更快
llm.predict("Tell me a joke")
```

    CPU times: user 4.58 ms, sys: 2.23 ms, total: 6.8 ms
    Wall time: 4.68 ms
    




    '\n\n为什么番茄变红了？\n\n因为它看到了沙拉酱！'
