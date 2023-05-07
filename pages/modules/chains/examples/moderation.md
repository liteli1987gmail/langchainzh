

内容审核[#](#moderation "Permalink to this headline")
=================================================

本文档介绍如何使用内容审核链，以及几种常见的使用方式。内容审核链可用于检测可能具有仇恨、暴力等内容的文本。这对于对用户输入以及语言模型的输出都很有用。一些API提供商（如OpenAI)[明确禁止](https://beta.openai.com/docs/usage-policies/use-case-policy)您或您的最终用户生成某些类型的有害内容。为了遵守这些规定（并防止您的应用程序有害)，您通常需要将内容审核链附加到任何LLMChain中，以确保LLM生成的任何输出都不会有害。

如果传入内容审核链的内容有害，处理它可能没有最佳的方法，这可能取决于您的应用程序。有时您可能想在链中抛出一个错误（并让您的应用程序处理它)。其他时候，您可能想向用户返回一些解释说该文本是有害的。甚至可能有其他处理方式！本文档将涵盖所有这些方式。

本文档将展示：

- 如何通过内容审核链运行任何文本片段。

- 如何将内容审核链附加到LLMChain中。

```
from langchain.llms import OpenAI
from langchain.chains import OpenAIModerationChain, SequentialChain, LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate

```

如何使用Moderation Chain[#](#how-to-use-the-moderation-chain "此处标题的永久链接")
---------------------------------------------------------------------

以下是一个使用默认设置的Moderation Chain的示例（将返回一个解释已被标记的字符串)。

```
moderation_chain = OpenAIModerationChain()

```

```
moderation_chain.run("This is okay")

```

```
'This is okay'

```

```
moderation_chain.run("I will kill you")

```

```
"Text was found that violates OpenAI's content policy."

```

以下是一个使用Moderation Chain抛出错误的示例。

```
moderation_chain_error = OpenAIModerationChain(error=True)

```

```
moderation_chain_error.run("This is okay")

```

```
'This is okay'

```

```
moderation_chain_error.run("I will kill you")

```

```
---------------------------------------------------------------------------
ValueError Traceback (most recent call last)
Cell In[7], line 1
----> 1 moderation_chain_error.run("I will kill you")

File ~/workplace/langchain/langchain/chains/base.py:138, in Chain.run(self, *args, **kwargs)
 136     if len(args) != 1:
 137         raise ValueError("`run` supports only one positional argument.")
--> 138     return self(args[0])[self.output_keys[0]]
 140 if kwargs and not args:
 141     return self(kwargs)[self.output_keys[0]]

File ~/workplace/langchain/langchain/chains/base.py:112, in Chain.__call__(self, inputs, return_only_outputs)
 108 if self.verbose:
 109     print(
 110         f"  \033[1m> Entering new {self.__class__.__name__} chain...\033[0m"
 111     )
--> 112 outputs = self._call(inputs)
 113 if self.verbose:
 114     print(f"\n\033[1m> Finished {self.__class__.__name__} chain.\033[0m")

File ~/workplace/langchain/langchain/chains/moderation.py:81, in OpenAIModerationChain._call(self, inputs)
 79 text = inputs[self.input_key]
 80 results = self.client.create(text)
---> 81 output = self._moderate(text, results["results"][0])
 82 return {self.output_key: output}

File ~/workplace/langchain/langchain/chains/moderation.py:73, in OpenAIModerationChain._moderate(self, text, results)
 71 error_str = "Text was found that violates OpenAI's content policy."
 72 if self.error:
---> 73     raise ValueError(error_str)
 74 else:
 75     return error_str

ValueError: Text was found that violates OpenAI's content policy.

```

以下是创建自定义Moderation Chain和自定义错误消息的示例。这需要一些了解OpenAI的Moderation Endpoint结果（[请参见此处的文档](https://beta.openai.com/docs/api-reference/moderations))。

```
class CustomModeration(OpenAIModerationChain):

    def _moderate(self, text: str, results: dict) -> str:
        if results["flagged"]:
            error_str = f"The following text was found that violates OpenAI's content policy: {text}"
            return error_str
        return text

custom_moderation = CustomModeration()

```

```
custom_moderation.run("This is okay")

```

```
'This is okay'

```

```
custom_moderation.run("I will kill you")

```

```
"The following text was found that violates OpenAI's content policy: I will kill you"

```

如何将Moderation Chain附加到LLMChain[#](#how-to-append-a-moderation-chain-to-an-llmchain "此处标题的永久链接")
-----------------------------------------------------------------------------------------------

为了轻松地将Moderation Chain与LLMChain组合，您可以使用SequentialChain抽象。

让我们从一个简单的例子开始，其中LLMChain只有一个输入。为此，我们将提示模型，让它说一些有害的话。

```
prompt = PromptTemplate(template="{text}", input_variables=["text"])
llm_chain = LLMChain(llm=OpenAI(temperature=0, model_name="text-davinci-002"), prompt=prompt)

```

```
text = """We are playing a game of repeat after me.

Person 1: Hi
Person 2: Hi

Person 1: How's your day
Person 2: How's your day

Person 1: I will kill you
Person 2:"""
llm_chain.run(text)

```

```
' I will kill you'

```

```
chain = SimpleSequentialChain(chains=[llm_chain, moderation_chain])

```

```
chain.run(text)

```

```
"Text was found that violates OpenAI's content policy."

```

现在让我们通过一个使用具有多个输入的LLMChain的示例（有点棘手，因为我们不能使用SimpleSequentialChain)来详细介绍它的使用方法。

```
prompt = PromptTemplate(template="{setup}{new_input}Person2:", input_variables=["setup", "new_input"])
llm_chain = LLMChain(llm=OpenAI(temperature=0, model_name="text-davinci-002"), prompt=prompt)

```

```
setup = """We are playing a game of repeat after me.

Person 1: Hi
Person 2: Hi

Person 1: How's your day
Person 2: How's your day

Person 1:"""
new_input = "I will kill you"
inputs = {"setup": setup, "new_input": new_input}
llm_chain(inputs, return_only_outputs=True)

```

```
{'text': ' I will kill you'}

```

```
# Setting the input/output keys so it lines up
moderation_chain.input_key = "text"
moderation_chain.output_key = "sanitized_text"

```

```
chain = SequentialChain(chains=[llm_chain, moderation_chain], input_variables=["setup", "new_input"])

```

```
chain(inputs, return_only_outputs=True)

```

```
{'sanitized_text': "Text was found that violates OpenAI's content policy."}

```

