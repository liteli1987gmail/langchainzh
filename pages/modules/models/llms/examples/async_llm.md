

如何使用LLMs的异步API[#](#how-to-use-the-async-api-for-llms "本标题的永久链接")
================================================================

LangChain通过利用[asyncio](https://docs.python.org/3/library/asyncio.html)库为LLMs提供异步支持。

异步支持对于同时调用多个LLMs特别有用，因为这些调用是网络限制的。目前支持`OpenAI`、`PromptLayerOpenAI`、`ChatOpenAI`和`Anthropic`，但是其他LLMs的异步支持正在路上。

您可以使用`agenerate`方法异步调用OpenAI LLM。

```
import time
import asyncio

from langchain.llms import OpenAI

def generate_serially():
    llm = OpenAI(temperature=0.9)
    for _ in range(10):
        resp = llm.generate(["Hello, how are you?"])
        print(resp.generations[0][0].text)

async def async_generate(llm):
    resp = await llm.agenerate(["Hello, how are you?"])
    print(resp.generations[0][0].text)

async def generate_concurrently():
    llm = OpenAI(temperature=0.9)
    tasks = [async_generate(llm) for _ in range(10)]
    await asyncio.gather(*tasks)

s = time.perf_counter()
# If running this outside of Jupyter, use asyncio.run(generate_concurrently())
await generate_concurrently() 
elapsed = time.perf_counter() - s
print('\033[1m' + f"Concurrent executed in {elapsed:0.2f} seconds." + '\033[0m')

s = time.perf_counter()
generate_serially()
elapsed = time.perf_counter() - s
print('\033[1m' + f"Serial executed in {elapsed:0.2f} seconds." + '\033[0m')

```

```
I'm doing well, thank you. How about you?

I'm doing well, thank you. How about you?

I'm doing well, how about you?

I'm doing well, thank you. How about you?

I'm doing well, thank you. How about you?

I'm doing well, thank you. How about yourself?

I'm doing well, thank you! How about you?

I'm doing well, thank you. How about you?

I'm doing well, thank you! How about you?

I'm doing well, thank you. How about you?
Concurrent executed in 1.39 seconds.

I'm doing well, thank you. How about you?

I'm doing well, thank you. How about you?

I'm doing well, thank you. How about you?

I'm doing well, thank you. How about you?

I'm doing well, thank you. How about yourself?

I'm doing well, thanks for asking. How about you?

I'm doing well, thanks! How about you?

I'm doing well, thank you. How about you?

I'm doing well, thank you. How about yourself?

I'm doing well, thanks for asking. How about you?
Serial executed in 5.77 seconds.

```

