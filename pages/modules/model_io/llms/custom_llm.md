# 自定义LLM

这篇笔记介绍如何创建一个自定义的LLM包装器，以便您可以使用自己的LLM或与LangChain支持的不同包装器不同的包装器。

使用标准的`LLM`接口对您的LLM进行包装，可以在现有的LangChain程序中使用您的LLM并进行最小程度的代码修改！

作为一个奖励，您的LLM将自动成为一个LangChain的`Runnable`，并将受益于一些优化，异步支持，`astream_events`API等等。

## 实现

一个自定义的LLM只需要实现两个必要的事情：


| 方法          | 描述                                                                                        |
|---------------|--------------------------------------------------------------------------------------------|
| `_call`       | 接收一个字符串和一些可选的停用词，并返回一个字符串。被`invoke`使用。                        |
| `_llm_type`   | 一个返回字符串的属性，仅用于记录目的。                                                    



可选实现: 


| 方法          | 描述                                                                                                      |
|--------------------------|----------------------------------------------------------------------------------------------------------|
| `_identifying_params`    | 用于帮助识别模型并打印LLM; 应返回一个字典。 这是一个 **@property**。    |
| `_acall`                | 提供一个`_call`的异步本地实现，被`ainvoke`使用。                                             |
| `_stream`               | 逐个令牌输出的方法。                                                                             |
| `_astream`              | 提供对`_stream`的异步本地实现；在较新的LangChain版本中，默认为`_stream`。                 



让我们实现一个简单的自定义LLM，它只返回输入的前n个字符。


```python
from typing import Any, Dict, Iterator, List, Mapping, Optional

from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM
from langchain_core.outputs import GenerationChunk


class CustomLLM(LLM):
    """一个自定义的聊天模型，将输入的前`n`个字符回声。

    当为LangChain贡献实现时，仔细记录包括初始化参数在内的模型，
    包括如何初始化模型的示例以及包括任何相关的
    链接到基础模型文档或API。

    示例:

        .. code-block:: python

            model = CustomChatModel(n=2)
            result = model.invoke([HumanMessage(content="hello")])
            result = model.batch([[HumanMessage(content="hello")],
                                 [HumanMessage(content="world")]])
    """

    n: int
    """要回声的提示的最后一条消息中的字符数。"""

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """在给定输入上运行LLM。

        重写此方法以实现LLM逻辑。

        参数:
            prompt: 用于生成的提示。
            stop: 生成时使用的停用词。 模型输出在任何停止子串的第一次出现时被截断。
                如果不支持停用词，请考虑引发NotImplementedError。
            run_manager: 运行的回调管理器。
            **kwargs: 任意额外的关键字参数。 通常传递给模型提供者API调用。

        返回:
            模型输出作为字符串。 实际完成不应包括提示。
        """
        if stop is not None:
            raise ValueError("不允许使用停用词参数。")
        return prompt[: self.n]

    def _stream(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[GenerationChunk]:
        """在给定提示上流式传输LLM。

        应该由支持流传输的子类重写此方法。

        如果没有实现，对流进行调用的默认行为将是退回到模型的非流版本并返回
        作为单个块的输出。

        参数:
            prompt: 生成的提示。
            stop: 生成时使用的停用词。 模型输出在任何这些子字符串的第一次出现时被截断。
            run_manager: 运行的回调管理器。
            **kwargs: 任意额外的关键字参数。 通常传递给模型提供者API调用。

        返回:
            一个GenerationChunks的迭代器。
        """
        for char in prompt[: self.n]:
            chunk = GenerationChunk(text=char)
            if run_manager:
                run_manager.on_llm_new_token(chunk.text, chunk=chunk)

            yield chunk

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """返回一组标识参数的字典。"""
        return {
            # 模型名称允许用户在LLM监控应用程序中指定自定义令牌计数规则（例如，在LangSmith用户可以提供用于其模型的每个令牌定价并监控
            # 为给定的LLM的成本。)
            "model_name": "CustomChatModel",
        }

    @property
    def _llm_type(self) -> str:
        """获取此聊天模型所使用的语言模型的类型。 仅用于记录目的。"""
        return "custom"
```

### 让我们来测试一下 🧪

这个LLM将实现LangChain的标准`Runnable`接口，许多LangChain抽象支持！


```python
llm = CustomLLM(n=5)
print(llm)
```

    [1mCustomLLM[0m
    Params: {'model_name': 'CustomChatModel'}
    


```python
llm.invoke("This is a foobar thing")
```




    'This '




```python
await llm.ainvoke("world")
```




    'world'




```python
llm.batch(["woof woof woof", "meow meow meow"])
```




    ['woof ', 'meow ']




```python
await llm.abatch(["woof woof woof", "meow meow meow"])
```




    ['woof ', 'meow ']




```python
async for token in llm.astream("hello"):
    print(token, end="|", flush=True)
```

    h|e|l|l|o|

让我们确认它是否与其他`LangChain`API很好地集成。


```python
from langchain_core.prompts import ChatPromptTemplate
```


```python
prompt = ChatPromptTemplate.from_messages(
    [("system", "you are a bot"), ("human", "{input}")]
)
```


```python
llm = CustomLLM(n=7)
chain = prompt | llm
```


```python
idx = 0
async for event in chain.astream_events({"input": "hello there!"}, version="v1"):
    print(event)
    idx += 1
    if idx > 7:
# Truncate
中断
```

## Contributing

我们欢迎所有聊天模型集成的贡献。

以下是一个检查列表，以确保您的贡献被添加到LangChain中：

文档：

- 模型包含所有初始化参数的文档字符串，因为这些将显示在[APIReference](https://api.python.langchain.com/en/stable/langchain_api_reference.html)中。
- 如果模型由服务支持，则模型的类文档字符串包含指向模型API的链接。

测试：

* [ ] 为重写的方法添加单元或集成测试。如果您重写了相应的代码，请验证`invoke`、`ainvoke`、`batch`和`stream`是否有效。

流式处理（如果您正在实现）：

* [ ] 确保调用`on_llm_new_token`回调
* [ ] 在产生块之前调用`on_llm_new_token`

停止标记行为：

* [ ] 应该尊重停止标记
* [ ] 停止标记应包含在响应中

机密API密钥：

* [ ] 如果您的模型连接到API，则可能会接受API密钥作为初始化的一部分。对于机密信息，请使用Pydantic的`SecretStr`类型，以防止在打印模型时意外打印出这些信息。