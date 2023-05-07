

转换链[#](#transformation-chain "本标题的永久链接")
========================================

本笔记展示了使用通用转换链。

以一个示例为例，我们将创建一个虚拟的转换，将一个超长文本过滤为仅前3段，并将其传递到LLMChain以对其进行摘要。

```
from langchain.chains import TransformChain, LLMChain, SimpleSequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

```

```
with open("../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()

```

```
def transform_func(inputs: dict) -> dict:
    text = inputs["text"]
    shortened_text = "  ".join(text.split("  ")[:3])
    return {"output_text": shortened_text}

transform_chain = TransformChain(input_variables=["text"], output_variables=["output_text"], transform=transform_func)

```

```
template = """Summarize this text:

{output_text}

Summary:"""
prompt = PromptTemplate(input_variables=["output_text"], template=template)
llm_chain = LLMChain(llm=OpenAI(), prompt=prompt)

```

```
sequential_chain = SimpleSequentialChain(chains=[transform_chain, llm_chain])

```

```
sequential_chain.run(state_of_the_union)

```

```
' The speaker addresses the nation, noting that while last year they were kept apart due to COVID-19, this year they are together again. They are reminded that regardless of their political affiliations, they are all Americans.'

```

