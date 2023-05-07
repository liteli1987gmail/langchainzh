

序列化[#](#serialization "跳转至该标题的锚点")
==================================

该笔记本涵盖了如何将链序列化到磁盘并从磁盘反序列化。我们使用的序列化格式是json或yaml。目前仅有一些链支持此类型的序列化。我们将逐步增加支持的链数。

将链保存到磁盘[#](#saving-a-chain-to-disk "跳转至该标题的锚点")
-----------------------------------------------

首先，让我们了解如何将链保存到磁盘。这可以通过`.save`方法完成，并指定一个具有json或yaml扩展名的文件路径。

```
from langchain import PromptTemplate, OpenAI, LLMChain
template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

```

```
llm_chain.save("llm_chain.json")

```

现在让我们来看看保存的文件中的内容

```
!cat llm_chain.json

```

```
{
    "memory": null,
    "verbose": true,
    "prompt": {
        "input_variables": [
            "question"
        ],
        "output_parser": null,
        "template": "Question: {question}  Answer: Let's think step by step.",
        "template_format": "f-string"
    },
    "llm": {
        "model_name": "text-davinci-003",
        "temperature": 0.0,
        "max_tokens": 256,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "n": 1,
        "best_of": 1,
        "request_timeout": null,
        "logit_bias": {},
        "_type": "openai"
    },
    "output_key": "text",
    "_type": "llm_chain"
}

```

从磁盘加载链[#](#loading-a-chain-from-disk "跳转至该标题的锚点")
-------------------------------------------------

我们可以使用`load_chain`方法从磁盘加载链。

```
from langchain.chains import load_chain

```

```
chain = load_chain("llm_chain.json")

```

```
chain.run("whats 2 + 2")

```

```
> Entering new LLMChain chain...
Prompt after formatting:
Question: whats 2 + 2

Answer: Let's think step by step.

> Finished chain.

```

```
' 2 + 2 = 4'

```

分别保存组件[#](#saving-components-separately "跳转至该标题的锚点")
----------------------------------------------------

在上面的例子中，我们可以看到提示和llm配置信息保存在与整个链相同的json中。或者，我们可以将它们拆分并分别保存。这通常有助于使保存的组件更加模块化。为了做到这一点，我们只需要指定`llm_path`而不是`llm`组件，以及`prompt_path`而不是`prompt`组件。

```
llm_chain.prompt.save("prompt.json")

```

```
!cat prompt.json

```

```
{
    "input_variables": [
        "question"
    ],
    "output_parser": null,
    "template": "Question: {question}  Answer: Let's think step by step.",
    "template_format": "f-string"
}

```

```
llm_chain.llm.save("llm.json")

```

```
!cat llm.json

```

```
{
    "model_name": "text-davinci-003",
    "temperature": 0.0,
    "max_tokens": 256,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "n": 1,
    "best_of": 1,
    "request_timeout": null,
    "logit_bias": {},
    "_type": "openai"
}

```

```
config = {
    "memory": None,
    "verbose": True,
    "prompt_path": "prompt.json",
    "llm_path": "llm.json",
    "output_key": "text",
    "_type": "llm_chain"
}
import json
with open("llm_chain_separate.json", "w") as f:
    json.dump(config, f, indent=2)

```

```
!cat llm_chain_separate.json

```

```
{
  "memory": null,
  "verbose": true,
  "prompt_path": "prompt.json",
  "llm_path": "llm.json",
  "output_key": "text",
  "_type": "llm_chain"
}

```

然后我们可以以相同的方式加载它。

```
chain = load_chain("llm_chain_separate.json")

```

```
chain.run("whats 2 + 2")

```

```
> Entering new LLMChain chain...
Prompt after formatting:
Question: whats 2 + 2

Answer: Let's think step by step.

> Finished chain.

```

```
' 2 + 2 = 4'

```

