# 聊天模型缓存
LangChain为聊天模型提供了一个可选的缓存层。这有两个好处：

- 如果您经常多次请求相同的完成结果，它可以通过减少您对LLM提供程序的API调用次数来帮您节省费用。
- 它可以通过减少您对LLM提供程序的API调用次数来加快您的应用程序速度。



```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
```


```python
# <!-- ruff: noqa: F821 -->
from langchain.globals import set_llm_cache
```

## 内存缓存

%%time 是一个魔术命令，用于在代码中测量代码块的执行时间。它是Python编程语言中的一个内置命令，可以用来计算代码块的执行时间。通过在代码块前加上"%%time"，可以获取代码块的执行时间信息，包括总时间、CPU时间和内存使用情况等。
```python
%%time
from langchain.cache import InMemoryCache

set_llm_cache(InMemoryCache())

# 第一次，它尚未在缓存中，所以需要更长的时间
llm.predict("告诉我一个笑话")
```

    CPU times: user 17.7 ms, sys: 9.35 ms, total: 27.1 ms
    Wall time: 801 ms
    




    "当然，这里有一个经典笑话给你：\n\n为什么科学家不相信原子？\n\n因为它们构成了一切！"




```python
%%time
# 第二次，由于已存在于缓存中，因此速度更快
llm.predict("告诉我一个笑话")
```

    CPU times: user 1.42 ms, sys: 419 µs, total: 1.83 ms
    Wall time: 1.83 ms
    




    "当然，这里有一个经典笑话给你：\n\n为什么科学家不相信原子？\n\n因为它们构成了一切！"

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
# 第一次，它尚未在缓存中，所以需要更长的时间
llm.predict("告诉我一个笑话")
```

    CPU times: user 23.2 ms, sys: 17.8 ms, total: 40.9 ms
    Wall time: 592 ms
    




    "当然，这里有一个经典笑话给你：\n\n为什么科学家不相信原子？\n\n因为它们构成了一切！"




```python
%%time
# 第二次，由于已存在于缓存中，因此速度更快
llm.predict("告诉我一个笑话")
```

    CPU times: user 5.61 ms, sys: 22.5 ms, total: 28.1 ms
    Wall time: 47.5 ms
    




    "当然，这里有一个经典笑话给你：\n\n为什么科学家不相信原子？\n\n因为它们构成了一切！"


