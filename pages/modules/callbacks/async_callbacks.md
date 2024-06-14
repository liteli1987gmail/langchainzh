# 异步回调

如果你计划使用异步API，建议使用`AsyncCallbackHandler`来避免阻塞运行循环。

**高级**如果你在使用异步方法运行LLM / Chain / Tool / Agent的同时使用同步的`CallbackHandler`，它仍然可以工作。然而，在幕后，它将使用[`run_in_executor`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor)进行调用，如果你的`CallbackHandler`不是线程安全的，可能会引起问题。

```python
import asyncio
from typing import Any, Dict, List

from langchain.callbacks.base import AsyncCallbackHandler, BaseCallbackHandler
from langchain_core.messages import HumanMessage
from langchain_core.outputs import LLMResult
from langchain_openai import ChatOpenAI


class MyCustomSyncHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"在`thread_pool_executor`中调用同步处理程序：token: {token}")


class MyCustomAsyncHandler(AsyncCallbackHandler):
    """可用于处理来自langchain的回调的异步回调处理程序。"""

    async def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """链开始运行时运行。"""
        print("zzzz....")
        await asyncio.sleep(0.3)
        class_name = serialized["name"]
        print("嗨！我刚刚醒来。您的LLM正在启动")

    async def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """链结束运行时运行。"""
        print("zzzz....")
        await asyncio.sleep(0.3)
        print("嗨！我刚刚醒来。您的LLM正在结束")


# 要启用流式传输，我们向ChatModel构造函数传入`streaming=True`
# 另外，我们传入一个包含我们自定义处理程序的列表
chat = ChatOpenAI(
    max_tokens=25,
    streaming=True,
    callbacks=[MyCustomSyncHandler(), MyCustomAsyncHandler()],
)

await chat.agenerate([[HumanMessage(content="给我讲个笑话")]])
```

    zzzz....
    嗨！我刚刚醒来。您的LLM正在启动
    在`thread_pool_executor`中调用同步处理程序：token: 
    在`thread_pool_executor`中调用同步处理程序：token: 为什么
    在`thread_pool_executor`中调用同步处理程序：token: 不
    在`thread_pool_executor`中调用同步处理程序：token: 相信
    在`thread_pool_executor`中调用同步处理程序：token: 科学家
    在`thread_pool_executor`中调用同步处理程序：token: 原子
    在`thread_pool_executor`中调用同步处理程序：token: ？
    在`thread_pool_executor`中调用同步处理程序：token:  
    
    
    在`thread_pool_executor`中调用同步处理程序：token: 因为
    在`thread_pool_executor`中调用同步处理程序：token: 他们
    在`thread_pool_executor`中调用同步处理程序：token: 编造
    在`thread_pool_executor`中调用同步处理程序：token: 一切
    在`thread_pool_executor`中调用同步处理程序：token: 。
    在`thread_pool_executor`中调用同步处理程序：token: 
    zzzz....
    嗨！我刚刚醒来。您的LLM正在结束
    




    LLMResult(generations=[[ChatGeneration(text="为什么科学家不相信原子？\n\n因为他们编造一切。", generation_info=None, message=AIMessage(content="为什么科学家不相信原子？\n\n因为他们编造一切。", additional_kwargs={}, example=False))]], llm_output={'token_usage': {}, 'model_name': 'gpt-3.5-turbo'})




```python

```