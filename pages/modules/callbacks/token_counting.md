# 令牌计数
LangChain提供了一个上下文管理器，允许您计算令牌。


```python
import asyncio

from langchain_community.callbacks import get_openai_callback
from langchain_openai import OpenAI

llm = OpenAI(temperature=0)
with get_openai_callback() as cb:
    llm.invoke("4的平方根是多少？")

total_tokens = cb.total_tokens
assert total_tokens > 0

with get_openai_callback() as cb:
    llm.invoke("4的平方根是多少？")
    llm.invoke("4的平方根是多少？")

assert cb.total_tokens == total_tokens * 2

# 您可以在上下文管理器内启动并发运行
with get_openai_callback() as cb:
    await asyncio.gather(
        *[llm.agenerate(["4的平方根是多少？"]) for _ in range(3)]
    )

assert cb.total_tokens == total_tokens * 3

# 上下文管理器是并发安全的
task = asyncio.create_task(llm.agenerate(["4的平方根是多少？"]))
with get_openai_callback() as cb:
    await llm.agenerate(["4的平方根是多少？"])

await task
assert cb.total_tokens == total_tokens

```
------
