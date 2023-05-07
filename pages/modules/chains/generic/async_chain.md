## 链的异步API

LangChain通过利用asyncio库为链提供异步支持。

目前LLMChain（通过arun、apredict、acall）、LLMMathChain（通过arun和acall）、ChatVectorDBChain以及QA chains支持异步方法。其他链的异步支持正在路线图中。
 







```
import asyncio
import time

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def generate_serially():
    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    for _ in range(5):
        resp = chain.run(product="toothpaste")
        print(resp)


async def async_generate(chain):
    resp = await chain.arun(product="toothpaste")
    print(resp)


async def generate_concurrently():
    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    tasks = [async_generate(chain) for _ in range(5)]
    await asyncio.gather(\*tasks)

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
BrightSmile Toothpaste Company


BrightSmile Toothpaste Co.


BrightSmile Toothpaste


Gleaming Smile Inc.


SparkleSmile Toothpaste
Concurrent executed in 1.54 seconds.


BrightSmile Toothpaste Co.


MintyFresh Toothpaste Co.


SparkleSmile Toothpaste.


Pearly Whites Toothpaste Co.


BrightSmile Toothpaste.
Serial executed in 6.38 seconds.

```







