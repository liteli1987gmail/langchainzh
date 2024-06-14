\
[![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/use_cases/tagging.ipynb)

## 应用案例

标签化是指使用类似以下类别进行文档标记：

- 情感
- 语言
- 风格（正式、非正式等）
- 涉及的主题
- 政治倾向

![图像描述](/img/tagging.png)

## 概述

标签化主要包括以下几个组成部分：

* `函数`：与[提取](/use_cases/extraction)类似，标签化使用[函数](https://openai.com/blog/function-calling-and-other-api-updates)指定模型标记文档的方法
* `模式`：定义我们如何标记文档的方式

## 快速入门

让我们看一个非常直接的示例，演示如何在LangChain中使用OpenAI工具进行标签化调用。我们将使用OpenAI模型支持的[`with_structured_output`](/modules/model_io/chat/structured_output)方法：

```python
%pip install --upgrade --quiet langchain langchain-openai

# 设置环境变量 OPENAI_API_KEY，或从 .env 文件加载：
# import dotenv
# dotenv.load_dotenv()
```

让我们在架构中指定一个具有几个属性及其预期类型的Pydantic模型。

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

tagging_prompt = ChatPromptTemplate.from_template(
    """
从以下段落中提取所需信息。

仅提取“分类”函数中提及的属性。

段落:
{input}
"""
)


class Classification(BaseModel):
    sentiment: str = Field(description="文本的情感")
    aggressiveness: int = Field(
        description="文本的侵略性程度（在1到10的尺度上）"
    )
    language: str = Field(description="文本所使用的语言")


# LLM
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0125").with_structured_output(
    Classification
)

tagging_chain = tagging_prompt | llm
```

```python
inp = "Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!"
tagging_chain.invoke({"input": inp})
```

输出结果为：
```
Classification(sentiment='positive', aggressiveness=1, language='Spanish')
```

如果我们希望获得JSON输出，只需调用`.dict()`方法

```python
inp = "Estoy muy enojado con vos! Te voy a dar tu merecido!"
res = tagging_chain.invoke({"input": inp})
res.dict()
```

输出结果为：
```
{'sentiment': 'negative', 'aggressiveness': 8, 'language': 'Spanish'}
```

正如我们在示例中看到的，它正确解释了我们想要的内容。

结果可能会有所不同，例如不同语言的情感（'positive'、'enojado'等）。

在下一节中，我们将介绍如何控制这些结果。

## 更细致的控制

精确的架构定义使我们能够更加控制模型的输出。

具体而言，我们可以定义：

- 每个属性的可能取值
- 描述以确保模型了解属性
- 需返回的必需属性

让我们重新声明我们的Pydantic模型，以使用枚举控制之前提到的每个方面：

```python
class Classification(BaseModel):
    sentiment: str = Field(..., enum=["happy", "neutral", "sad"])
    aggressiveness: int = Field(
        ...,
        description="描述语句的侵略性程度，数字越大，侵略性越高",
        enum=[1, 2, 3, 4, 5],
    )
    language: str = Field(
        ..., enum=["spanish", "english", "french", "german", "italian"]
    )
```

```python
tagging_prompt = ChatPromptTemplate.from_template(
    """
从以下段落中提取所需信息。

仅提取“分类”函数中提及的属性。

段落:
{input}
"""
)

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0125").with_structured_output(
    Classification
)

chain = tagging_prompt | llm
```

现在，答案将限制在我们期望的方式中。

```python
inp = "Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!"
chain.invoke({"input": inp})
```

输出结果为：
```
Classification(sentiment='happy', aggressiveness=1, language='spanish')
```

```python
inp = "Estoy muy enojado con vos! Te voy a dar tu merecido!"
chain.invoke({"input": inp})
```

输出结果为：
```
Classification(sentiment='sad', aggressiveness=5, language='spanish')
```

```python
inp = "Weather is ok here, I can go outside without much more than a coat"
chain.invoke({"input": inp})
```

输出结果为：
```
Classification(sentiment='neutral', aggressiveness=2, language='english')
```

我们可以通过[LangSmith追踪](https://smith.langchain.com/public/38294e04-33d8-4c5a-ae92-c2fe68be8332/r)来深入了解：

![图像描述](/img/tagging_trace.png)

### 深入了解

* 您可以使用[metadata tagger](/docs/integrations/document_transformers/openai_metadata_tagger)文档转换器从LangChain `Document`中提取元数据。
* 这涵盖了与标记链相同的基本功能，只是应用于LangChain `Document`。