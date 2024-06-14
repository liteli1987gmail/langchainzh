# 根据输入动态路由逻辑

本笔记本涵盖了如何在LangChain表达语言中进行路由。

路由允许您创建非确定性链，其中前一步的输出定义了下一步。路由有助于在与LLMs的交互中提供结构和一致性。

有两种执行路由的方式：

1. 从 [`RunnableLambda`](/expression_language/primitives/functions) 条件返回可运行项（推荐）
2. 使用 `RunnableBranch`。

我们将使用一个两步序列来说明这两种方法，第一步将输入问题分类为关于 `LangChain`、`Anthropic` 或 `Other`，然后路由到相应的提示链。

## 示例设置
首先，让我们创建一个链，将入站问题识别为关于 `LangChain`、`Anthropic` 或 `Other`：

```python
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

chain = (
    PromptTemplate.from_template(
        """Given the user question below, classify it as either being about `LangChain`, `Anthropic`, or `Other`.

Do not respond with more than one word.

<question>
{question}
</question>

Classification:"""
    )
    | ChatAnthropic(model_name="claude-3-haiku-20240307")
    | StrOutputParser()
)

chain.invoke({"question": "how do I call Anthropic?"})
```

现在，让我们创建三个子链：

```python
langchain_chain = PromptTemplate.from_template(
    """You are an expert in langchain. \
Always answer questions starting with "As Harrison Chase told me". \
Respond to the following question:

Question: {question}
Answer:"""
) | ChatAnthropic(model_name="claude-3-haiku-20240307")

anthropic_chain = PromptTemplate.from_template(
    """You are an expert in anthropic. \
Always answer questions starting with "As Dario Amodei told me". \
Respond to the following question:

Question: {question}
Answer:"""
) | ChatAnthropic(model_name="claude-3-haiku-20240307")

general_chain = PromptTemplate.from_template(
    """Respond to the following question:

Question: {question}
Answer:"""
) | ChatAnthropic(model_name="claude-3-haiku-20240307")
```

## 使用自定义函数（推荐）

您还可以使用自定义函数在不同的输出之间进行路由。以下是一个示例：

```python
def route(info):
    if "anthropic" in info["topic"].lower():
        return anthropic_chain
    elif "langchain" in info["topic"].lower():
        return langchain_chain
    else:
        return general_chain
```


```python
from langchain_core.runnables import RunnableLambda

full_chain = {"topic": chain, "question": lambda x: x["question"]} | RunnableLambda(
    route
)
```


```python
full_chain.invoke({"question": "how do I use Anthropic?"})
```




    AIMessage(content="As Dario Amodei told me, to use Anthropic, you can start by exploring the company's website and learning about their mission, values, and the different services and products they offer. Anthropic is focused on developing safe and ethifrom langchain.utils.math import cosine_similarity

```python   
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import OpenAIEmbeddings

physics_template = """您是一位非常聪明的物理学教授。
您擅长以简洁易懂的方式回答物理问题。
当您不知道答案时，会坦率承认。

这是一个问题：
{query}"""

math_template = """您是一位非常出色的数学家。
您擅长回答数学问题。
您能够将难题分解为其组成部分，回答每个组成部分，
然后将它们组合起来回答更广泛的问题。

这是一个问题：
{query}"""

embeddings = OpenAIEmbeddings()
prompt_templates = [physics_template, math_template]
prompt_embeddings = embeddings.embed_documents(prompt_templates)


def prompt_router(input):
    query_embedding = embeddings.embed_query(input["query"])
    similarity = cosine_similarity([query_embedding], prompt_embeddings)[0]
    most_similar = prompt_templates[similarity.argmax()]
    print("使用数学" if most_similar == math_template else "使用物理")
    return PromptTemplate.from_template(most_similar)


chain = (
    {"query": RunnablePassthrough()}
    | RunnableLambda(prompt_router)
    | ChatAnthropic(model_name="claude-3-haiku-20240307")
    | StrOutputParser()
)
```


```python
print(chain.invoke("什么是黑洞"))
```

    使用物理
    作为一名物理学教授，我很愿意以简洁易懂的方式解释什么是黑洞。
    
    黑洞是一个极为密集的时空区域，其引力非常强大，甚至连光都无法逃逸。
    这意味着如果你靠得太近，你会被强大的引力所吸引并被压碎。
    
    黑洞的形成发生在一个巨大的恒星结束其生命周期并坍缩为自身的过程中。
    这种坍缩使得物质变得极为密集，引力变得非常强大，从而形成了一个无法回头的点，即事件视界。
    
    超出事件视界之后，我们所了解的物理定律会失效，强大的引力力量会形成奇点，
    这是时空中无限密度和曲率的点。
    
    黑洞是迷人而神秘的物体，对于它们的性质和行为还有很多待探索的地方。
    如果对于任何具体的黑洞细节或方面我不确定，我会坦率地承认我没有完全理解，并鼓励进一步的研究和探索。
    


```python
print(chain.invoke("什么是路径积分"))
```

    使用数学
    路径积分是物理学中一个强大的数学概念，尤其在量子力学领域。它是由著名物理学家理查德·费曼作为量子力学的替代形式而发展的。
    
    在路径积分中，与经典力学中只考虑一个确定路径不同，粒子被认为同时采用所有可能的路径。
    每条路径被分配一个复值权重，粒子从一个点到另一个点的总概率振幅通过对所有可能路径求和（积分）来计算。
    
    路径积分形式背后的关键思想有：
    
    1. 叠加原理：在量子力学中，粒子可以存在于多个状态或路径的叠加中。
    
    2. 概率振幅：粒子从一个点到另一个点的概率振幅通过求和所有可能路径的复值权重来计算。
    
    3. 路径的加权：每条路径根据沿该路径的作用量（拉格朗日量的时间积分）被赋予一定的权重。作用量越小的路径具有更大的权重。
    
    4. 费曼的方法：费曼发展了路径积分形式作为量子力学传统波函数方法的替代，提供了更直观和概念上的量子现象理解。
    
    路径积分方法在量子场论中特别有用，它为计算转换概率和理解量子系统的行为提供了强大的框架。
    它还在物理学的各个领域中找到了应用，如凝聚态物理学、统计力学，甚至金融学（期权定价的路径积分方法）等。
    
    路径积分的数学构造涉及到来自函数分析和测度论的高级概念，这使得它成为物理学家强大而复杂的工具。
    


