# 自定义回调处理程序

您也可以创建一个自定义处理程序来设置在对象上。在下面的示例中，我们将使用自定义处理程序实现流式处理。


```python
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


class MyCustomHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"我的自定义处理程序，token: {token}")


# 要启用流式处理，我们在ChatModel构造函数中传入`streaming=True`
# 另外，我们传入一个包含我们自定义处理程序的列表
chat = ChatOpenAI(max_tokens=25, streaming=True, callbacks=[MyCustomHandler()])

chat.invoke([HumanMessage(content="告诉我一个笑话")])
```

    我的自定义处理程序，token: 
    我的自定义处理程序，token: 为什么
    我的自定义处理程序，token:  科学家们
    我的自定义处理程序，token:  不相信
    我的自定义处理程序，token:  原子
    我的自定义处理程序，token: ？
    
    
    我的自定义处理程序，token: 因为
    我的自定义处理程序，token:  他们
    我的自定义处理程序，token:  组成
    我的自定义处理程序，token:  了
    我的自定义处理程序，token:  一切
    我的自定义处理程序，token: 。
    




    AIMessage(content="为什么科学家们不相信原子？\n\n因为他们组成了一切。", additional_kwargs={}, example=False)






