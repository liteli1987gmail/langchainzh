# [beta] 结构化输出 (Structured Output)

通常情况下，让LLM返回结构化输出非常重要。这是因为LLM的输出通常用于下游应用程序，这些应用程序需要特定的参数。使LLM可靠地返回结构化输出是必要的。

有几种不同的高级策略可用于实现此目的：

- 提问式：这是你（非常友好地）要求LLM以期望的格式（JSON、XML）返回输出的方式。这样做很好，因为它适用于所有LLM。但这样做不好的地方在于无法保证LLM以正确的格式返回输出。
- 函数调用：这是指LLM经过微调，可以生成函数调用而不仅仅是生成完整文本。这些LLM可以调用的函数通常作为额外参数传递给模型API。函数名称和描述应视为提示的一部分（它们通常计入令牌计数，并由LLM用于决定下一步的操作）。
- 工具调用：这是一种类似于函数调用的技术，但它允许LLM同时调用多个函数。
- JSON模式：这是指当LLM确保返回JSON格式时。

不同的模型可能支持这些策略的不同变体，参数可能略有不同。为了方便让LLMs返回结构化输出，我们为LangChain模型添加了一个公共接口：`.with_structured_output`。

通过调用这个方法（并传递一个JSON模式或Pydantic模型），模型将添加任何必要的模型参数和输出解析器，以便获得结构化输出。可能有多种方法可以实现这一目标（例如函数调用vs JSON模式），你可以通过传递参数来配置使用哪种方法。

让我们看一些实际示例！

我们将使用Pydantic来轻松定义响应模式。

```python
from langchain_core.pydantic_v1 import BaseModel, Field
```

```python
class Joke(BaseModel):
    setup: str = Field(description="笑话的设置部分")
    punchline: str = Field(description="笑话的结尾部分")
```

## OpenAI

OpenAI提供了几种不同的方法来获得结构化输出。

[API参考](https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html#langchain_openai.chat_models.base.ChatOpenAI.with_structured_output)

```python
from langchain_openai import ChatOpenAI
```

### 函数调用

默认情况下，我们将使用`function_calling`

```python
model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
structured_llm = model.with_structured_output(Joke)
```

```python
structured_llm.invoke("给我讲一个关于猫的笑话")
```

### JSON模式

我们也支持JSON模式。注意，我们需要在提示中指定它应该以哪种格式进行响应。

```python
structured_llm = model.with_structured_output(Joke, method="json_mode")
```

```python
structured_llm.invoke(
    "给我讲一个关于猫的笑话，用`setup`和`punchline`键以JSON形式响应"
)
```

## Fireworks

[Fireworks](https://fireworks.ai/)也为某些模型提供函数调用和JSON模式的支持。

[API参考](https://api.python.langchain.com/en/latest/chat_models/langchain_fireworks.chat_models.ChatFireworks.html#langchain_fireworks.chat_models.ChatFireworks.with_structured_output)

```python
from langchain_fireworks import ChatFireworks
```

### 函数调用

默认情况下，我们将使用`function_calling`

```python
model = ChatFireworks(model="accounts/fireworks/models/firefunction-v1")
structured_llm = model.with_structured_output(Joke)
```

```python
structured_llm.invoke("给我讲一个关于猫的笑话")
```

### JSON模式

我们也支持JSON模式。注意，我们需要在提示中指定它应该以哪种格式进行响应。

```python
structured_llm = model.with_structured_output(Joke, method="json_mode")
```

```python
structured_llm.invoke(
    "给我讲一个关于狗的笑话，用`setup`和`punchline`键以JSON形式响应"
)
```

## Mistral

我们还支持在Mistral模型中返回结构化输出，尽管我们只支持函数调用。

[API参考](https://api.python.langchain.com/en/latest/chat_models/langchain_mistralai.chat_models.ChatMistralAI.html#langchain_mistralai.chat_models.ChatMistralAI.with_structured_output)

```python
from langchain_mistralai import ChatMistralAI
```

```python
model = ChatMistralAI(model="mistral-large-latest")
structured_llm = model.with_structured_output(Joke)
```

```python
structured_llm.invoke("给我讲一个关于猫的笑话")
```

## Together

由于[TogetherAI](https://www.together.ai/)只是OpenAI的替代品，我们可以直接使用OpenAI的集成方式。

```python
import os

from langchain_openai import ChatOpenAI
```

```python
model = ChatOpenAI(
    base_url="https://api.together.xyz/v1",
    api_key=os.environ["TOGETHER_API_KEY"],
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
)
structured_llm = model.with_structured_output(Joke)
```

```python
structured_llm.invoke("给我讲一个关于猫的笑话")
```

# Groq

Groq提供了一个兼容OpenAI的函数调用API。

[API参考链接](https://api.python.langchain.com/en/latest/chat_models/langchain_groq.chat_models.ChatGroq.html#langchain_groq.chat_models.ChatGroq.with_structured_output)


```python
from langchain_groq import ChatGroq
```

### 函数调用

默认情况下，我们将使用`function_calling`


```python
model = ChatGroq()
structured_llm = model.with_structured_output(Joke)
```

    /Users/reag/src/langchain/libs/core/langchain_core/_api/beta_decorator.py:87: LangChainBetaWarning: 函数`with_structured_output`处于beta版。它正在积极开发中，因此API可能会有变化。
      warn_beta(
    


```python
structured_llm.invoke("给我讲一个关于猫的笑话")
```




    Joke(setup="为什么猫不在丛林中玩扑克？", punchline='有太多的猎豹！')



### JSON模式

我们还支持JSON模式。请注意，我们需要在提示中指定它应该以哪种格式进行响应。


```python
structured_llm = model.with_structured_output(Joke, method="json_mode")
```


```python
structured_llm.invoke(
    "给我讲一个关于猫的笑话，以JSON格式回复，包含`setup`和`punchline`键"
)
```




    Joke(setup="为什么猫不在丛林中玩扑克？", punchline='有太多的猎豹！')



## Anthropic

Anthropic的工具调用API可以用于结构化输出。请注意，目前没有通过API强制执行工具调用的方法，因此正确提示模型仍然很重要。

[API参考链接](https://api.python.langchain.com/en/latest/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html#langchain_anthropic.chat_models.ChatAnthropic.with_structured_output)


```python
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0)
structured_llm = model.with_structured_output(Joke)
structured_llm.invoke("给我讲一个关于猫的笑话。确保调用Joke函数。")
```




    Joke(setup='你如何称呼一个热爱打保龄球的猫？', punchline='一个保龄球猫！')



# Vertex AI

Google的Gemini模型支持[函数调用](https://ai.google.dev/docs/function_calling)，我们可以通过Vertex AI访问并用于结构化输出。

[API参考链接](https://api.python.langchain.com/en/latest/chat_models/langchain_google_vertexai.chat_models.ChatVertexAI.html#langchain_google_vertexai.chat_models.ChatVertexAI.with_structured_output)


```python
from langchain_google_vertexai import ChatVertexAI

llm = ChatVertexAI(model="gemini-pro", temperature=0)
structured_llm = llm.with_structured_output(Joke)
structured_llm.invoke("给我讲一个关于猫的笑话")
```




    Joke(setup='一个猫-Ch', punchline='你如何称呼一个热爱玩接球的猫？')

