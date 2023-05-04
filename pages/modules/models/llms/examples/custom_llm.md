

如何编写自定义LLM包装器[#](#how-to-write-a-custom-llm-wrapper "Permalink to this headline")
=================================================================================

本笔记介绍如何创建自定义LLM包装器，以便您可以使用自己的LLM或与LangChain支持的不同包装器。

自定义LLM仅需要实现一件必需的事情：

- 一个 `_call` 方法，它接收一个字符串，一些可选的停用词，并返回一个字符串

它还可以实现第二个可选项：

- 一个 `_identifying_params` 属性，用于帮助打印该类。应该返回一个字典。

让我们实现一个非常简单的自定义LLM，它只返回输入的前N个字符。

```
from typing import Any, List, Mapping, Optional

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

```

```
class CustomLLM(LLM):

    n: int

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        return prompt[:self.n]

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
 """Get the identifying parameters."""
        return {"n": self.n}

```

现在我们可以像使用任何其他LLM一样使用它。

```
llm = CustomLLM(n=10)

```

```
llm("This is a foobar thing")

```

```
'This is a '

```

我们还可以打印LLM并查看其自定义打印。

```
print(llm)

```

```
CustomLLM
Params: {'n': 10}

```

