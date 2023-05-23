

如何序列化LLM类[#](#how-to-serialize-llm-classes "本标题的永久链接")
======================================================

本教程演示了如何将LLM配置写入磁盘并从磁盘中读取。如果您想保存给定LLM的配置（例如提供程序、温度（temperature）等)，则这非常有用。

```
from langchain.llms import OpenAI
from langchain.llms.loading import load_llm

```

加载[#](#loading "本标题的永久链接")
--------------------------

首先，让我们讨论从磁盘加载LLM。LLMs可以以json或yaml格式保存在磁盘上。无论扩展名如何，它们都以相同的方式加载。

```
!cat llm.json

```

```
{
    "model_name": "text-davinci-003",
    "temperature": 0.7,
    "max_tokens": 256,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
    "n": 1,
    "best_of": 1,
    "request_timeout": null,
    "_type": "openai"
}

```

```
llm = load_llm("llm.json")

```

```
!cat llm.yaml

```

```
_type: openai
best_of: 1
frequency_penalty: 0.0
max_tokens: 256
model_name: text-davinci-003
n: 1
presence_penalty: 0.0
request_timeout: null
temperature: 0.7
top_p: 1.0

```

```
llm = load_llm("llm.yaml")

```

保存[#](#saving "本标题的永久链接")
-------------------------

如果您想从内存中的LLM转换为其序列化版本，可以通过调用`.save`方法轻松完成。同样，它支持json和yaml。

```
llm.save("llm.json")

```

```
llm.save("llm.yaml")

```

