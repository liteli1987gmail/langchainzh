

LLM Chain[#](#llm-chain "此标题的永久链接")
===================================

`LLMChain` 可能是查询 LLM 对象最流行的方式之一。它使用提供的输入键值（以及可用的内存键值)格式化提示模板，将格式化后的字符串传递给 LLM 并返回 LLM 输出。下面我们展示了 `LLMChain` 类的其他功能。

```
from langchain import PromptTemplate, OpenAI, LLMChain

prompt_template = "What is a good name for a company that makes {product}?"

llm = OpenAI(temperature=0)
llm_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)
llm_chain("colorful socks")

```

```
{'product': 'colorful socks', 'text': '  Socktastic!'}

```

运行 LLM Chain 的其他方法[#](#additional-ways-of-running-llm-chain "此标题的永久链接")
=======================================================================

除了所有 `Chain` 对象共享的 `__call__` 和 `run` 方法（请参见[入门指南](../getting_started)了解更多信息)，`LLMChain` 还提供了几种调用链逻辑的方法：

* `apply` 允许您对输入列表运行链：

```
input_list = [
    {"product": "socks"},
    {"product": "computer"},
    {"product": "shoes"}
]

llm_chain.apply(input_list)

```

```
[{'text': '  Socktastic!'},
 {'text': '  TechCore Solutions.'},
 {'text': '  Footwear Factory.'}]

```

* `generate`与`apply`类似，不同之处在于它返回一个`LLMResult`而不是字符串。`LLMResult`通常包含有用的生成信息，例如标记使用和完成原因。

```
llm_chain.generate(input_list)

```

```
LLMResult(generations=[[Generation(text='  Socktastic!', generation_info={'finish_reason': 'stop', 'logprobs': None})], [Generation(text='  TechCore Solutions.', generation_info={'finish_reason': 'stop', 'logprobs': None})], [Generation(text='  Footwear Factory.', generation_info={'finish_reason': 'stop', 'logprobs': None})]], llm_output={'token_usage': {'prompt_tokens': 36, 'total_tokens': 55, 'completion_tokens': 19}, 'model_name': 'text-davinci-003'})

```

* `predict`与`run`方法类似，不同之处在于输入键是关键字参数而不是Python字典。

```
# Single input example
llm_chain.predict(product="colorful socks")

```

```
'  Socktastic!'

```

```
# Multiple inputs example

template = """Tell me a {adjective} joke about {subject}."""
prompt = PromptTemplate(template=template, input_variables=["adjective", "subject"])
llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0))

llm_chain.predict(adjective="sad", subject="ducks")

```

```
'  Q: What did the duck say when his friend died?\nA: Quack, quack, goodbye.'

```

解析输出[#](#parsing-the-outputs "Permalink to this headline")
==========================================================

默认情况下，即使底层`prompt`对象具有输出解析器，`LLMChain`也不会解析输出。如果您想在LLM输出上应用该输出解析器，请使用`predict_and_parse`代替`predict`和`apply_and_parse`代替`apply`。

使用`predict`：

```
from langchain.output_parsers import CommaSeparatedListOutputParser

output_parser = CommaSeparatedListOutputParser()
template = """List all the colors in a rainbow"""
prompt = PromptTemplate(template=template, input_variables=[], output_parser=output_parser)
llm_chain = LLMChain(prompt=prompt, llm=llm)

llm_chain.predict()

```

```
'  Red, orange, yellow, green, blue, indigo, violet'

```

使用`predict_and_parser`：

```
llm_chain.predict_and_parse()

```

```
['Red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

```

从字符串初始化[#](#initialize-from-string "Permalink to this headline")
================================================================

您还可以直接从字符串模板构建LLMChain。

```
template = """Tell me a {adjective} joke about {subject}."""
llm_chain = LLMChain.from_string(llm=llm, template=template)

```

```
llm_chain.predict(adjective="sad", subject="ducks")

```

```
'  Q: What did the duck say when his friend died?\nA: Quack, quack, goodbye.'

```

