# 获取对数概率

某些聊天模型可以配置为返回标记级别的对数概率。本指南介绍了如何为多个模型获取对数概率。

## OpenAI

安装LangChain x OpenAI包并设置您的API密钥

```python
%pip install -qU langchain-openai
```

```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()
```

为了OpenAI API可以返回对数概率，我们需要配置`logprobs=True`参数。

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo-0125").bind(logprobs=True)

msg = llm.invoke(("human", "你今天好吗"))
```

对数概率包含在每个输出消息的`response_metadata`中：

```python
msg.response_metadata["logprobs"]["content"][:5]
```

并且也作为流式消息块的一部分：

```python
ct = 0
full = None
for chunk in llm.stream(("human", "你今天好吗")):
    if ct < 5:
        full = chunk if full is None else full + chunk
        if "logprobs" in full.response_metadata:
            print(full.response_metadata["logprobs"]["content"])
    else:
        break
    ct += 1
```

结果如下：

    []
    [{'token': 'As', 'bytes': [65, 115], 'logprob': -1.7523563, 'top_logprobs': []}]
    [{'token': 'As', 'bytes': [65, 115], 'logprob': -1.7523563, 'top_logprobs': []}, {'token': ' an', 'bytes': [32, 97, 110], 'logprob': -0.019908238, 'top_logprobs': []}]
    [{'token': 'As', 'bytes': [65, 115], 'logprob': -1.7523563, 'top_logprobs': []}, {'token': ' an', 'bytes': [32, 97, 110], 'logprob': -0.019908238, 'top_logprobs': []}, {'token': ' AI', 'bytes': [32, 65, 73], 'logprob': -0.0093033705, 'top_logprobs': []}]
    [{'token': 'As', 'bytes': [65, 115], 'logprob': -1.7523563, 'top_logprobs': []}, {'token': ' an', 'bytes': [32, 97, 110], 'logprob': -0.019908238, 'top_logprobs': []}, {'token': ' AI', 'bytes': [32, 65, 73], 'logprob': -0.0093033705, 'top_logprobs': []}, {'token': ',', 'bytes': [44], 'logprob': -0.08852102, 'top_logprobs': []}]

