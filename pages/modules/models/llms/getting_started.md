

入门[#](#getting-started "到此标题的永久链接")
===================================

本教程介绍了如何使用LangChain中的LLM类。

LLM类是设计用于与LLMs进行接口交互的类。有许多LLM提供商（OpenAI、Cohere、Hugging Face等)-该类旨在为所有LLM提供商提供标准接口。在本文档的这部分中，我们将重点介绍通用LLM功能。有关使用特定LLM包装器的详细信息，请参见[如何指南](how_to_guides.html)中的示例。

对于本教程，我们将使用OpenAI LLM包装器进行工作，尽管突出显示的功能对于所有LLM类型都是通用的。

```
from langchain.llms import OpenAI

```

```
llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)

```

**生成文本：**LLM最基本的功能就是能够调用它，传入一个字符串并返回一个字符串。

```
llm("Tell me a joke")

```

```
'  Why did the chicken cross the road?  To get to the other side.'

```

**生成：**更广泛地说，您可以使用输入列表调用它，获取比仅文本更完整的响应。此完整响应包括多个顶部响应，以及LLM提供商特定的信息

```
llm_result = llm.generate(["Tell me a joke", "Tell me a poem"]*15)

```

```
len(llm_result.generations)

```

```
30

```

```
llm_result.generations[0]

```

```
[Generation(text='  Why did the chicken cross the road?  To get to the other side!'),
 Generation(text='  Why did the chicken cross the road?  To get to the other side.')]

```

```
llm_result.generations[-1]

```

```
[Generation(text="  What if love neverspeech  What if love never ended  What if love was only a feeling  I'll never know this love  It's not a feeling  But it's what we have for each other  We just know that love is something strong  And we can't help but be happy  We just feel what love is for us  And we love each other with all our heart  We just don't know how  How it will go  But we know that love is something strong  And we'll always have each other  In our lives."),
 Generation(text='  Once upon a time  There was a love so pure and true  It lasted for centuries  And never became stale or dry  It was moving and alive  And the heart of the love-ick  Is still beating strong and true.')]

```

您还可以访问返回的特定于提供程序的信息。此信息在提供程序之间**不**标准化。

```
llm_result.llm_output

```

```
{'token_usage': {'completion_tokens': 3903,
  'total_tokens': 4023,
  'prompt_tokens': 120}}

```

**标记数量：**您还可以估计模型中一段文本将有多少个标记。这很有用，因为模型具有上下文长度（并且对于更多标记的成本更高)，这意味着您需要注意传递的文本的长度。

请注意，默认情况下使用 [tiktoken](https://github.com/openai/tiktoken) 进行令牌估计（除了旧版本 <3.8，这些版本使用 Hugging Face tokenizer)

```
llm.get_num_tokens("what a joke")

```

```
3

```

