# 聊天少样本示例（FewShotExamplesChat）

这个笔记本介绍如何在聊天模型中使用few-shot示例。目前并没有关于如何最好地进行few-shot提示的一致意见，最佳的提示编译可能因模型而异。因此，我们提供few-shot提示模板，如[FewShotChatMessagePromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.few_shot.FewShotChatMessagePromptTemplate.html?highlight=fewshot#langchain_core.prompts.few_shot.FewShotChatMessagePromptTemplate)，作为灵活的起点，您可以根据需要修改或替换它们。

few-shot提示模板的目标是根据输入动态选择示例，然后将这些示例格式化为最终提示，以供模型使用。

**注意：**以下代码示例适用于聊天模型。有关类似完整模型（LLMs）的few-shot提示示例，请参阅[few-shot提示模板](/modules/model_io/prompts/few_shot_examples/)指南。

### 固定示例

最基本（也是最常见）的few-shot提示技术是使用固定的提示示例。这样，您可以选择一个链并对其进行评估，而不必担心额外的移动部件。

模板的基本组成部分包括：
- `examples`：包含在最终提示中的字典示例列表。
- `example_prompt`：通过其[`format_messages`](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html?highlight=format_messages#langchain_core.prompts.chat.ChatPromptTemplate.format_messages)方法将每个示例转换为1个或多个消息。一个常见的例子是将每个示例转换为一个人类消息和一个AI消息响应，或者一个人类消息后面跟着一个函数调用消息。

下面是一个简单的演示。首先，导入此示例的模块：

```python
from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
```

然后，定义要包含的示例。

```python
examples = [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
]
```

接下来，将它们组装到few-shot提示模板中。

```python
# 这是用于格式化每个单独示例的提示模板。
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

print(few_shot_prompt.format())
```

    Human: 2+2
    AI: 4
    Human: 2+3
    AI: 5

最后，组装最终的提示并将其与模型一起使用。

```python
final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a wondrous wizard of math."),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)
```

```python
from langchain_community.chat_models import ChatAnthropic

chain = final_prompt | ChatAnthropic(temperature=0.0)

chain.invoke({"input": "What's the square of a triangle?"})
```

    AIMessage(content=' 三角形没有"平方"。"平方"指的是具有4条相等边和4个直角的形状。三角形有3条边和3个角。\n\n可以使用下述公式计算三角形的面积：\n\nA = 1/2 * b * h\n\n其中：\n\nA 是面积\nb 是底边（其中一条边的长度）\nh 是高度（从底边到相对顶点的距离的长度）\n\n因此，面积取决于三角形的具体尺寸。没有一个单一的"三角形的平方"。根据底边和高度的测量，面积可以有很大的变化。', additional_kwargs={}, example=False)

## 动态few-shot提示

有时，您可能希望根据输入条件选择要显示的示例。为此，可以将`examples`替换为`example_selector`。其他组件与上述相同！回顾一下，动态few-shot提示模板将如下所示：

- `example_selector`：负责为给定输入选择few-shot示例（以及它们返回的顺序）。这些实现了[BaseExampleSelector](https://api.python.langchain.com/en/latest/example_selectors/langchain_core.example_selectors.base.BaseExampleSelector.html?highlight=baseexampleselector#langchain_core.example_selectors.base.BaseExampleSelector)接口。一个常见的例子是基于向量存储的[SemanticSimilarityExampleSelector](https://api.python.langchain.com/en/latest/example_selectors/langchain_core.example_selectors.semantic_similarity.SemanticSimilarityExampleSelector.html?highlight=semanticsimilarityexampleselector#langchain_core.example_selectors.semantic_similarity.SemanticSimilarityExampleSelector)
- `example_prompt`：通过其[`format_messages`](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html?highlight=chatprompttemplate#langchain_core.prompts.chat.ChatPromptTemplate.format_messages)方法将每个示例转换为1个或多个消息。一个常见的例子是将每个示例转换为一个人类消息和一个AI消息响应，或者一个人类消息后面跟着一个函数调用消息。

同样可以将这些组合与其他消息和聊天模板组合起来，以组装最终的提示。

```python
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
```

由于我们使用向量存储来根据语义相似性选择示例，我们首先需要填充存储。

```python
examples = [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
    {"input": "2+4", "output": "6"},
    {"input": "What did the cow say to the moon?", "output": "nothing at all"},
    {
        "input": "Write me a poem about the moon",
        "output": "One for the moon, and one for me, who are we to talk about the moon?",
    },
]

to_vectorize = [" ".join(example.values()) for example in examples]
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=examples)
```

#### 创建`example_selector`

创建向量存储后，可以创建`example_selector`。在这里，我们将指示它仅获取前2个示例。

```python
example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=2,
)

# prompt模板将通过将输入传递给`select_examples`方法来加载示例
example_selector.select_examples({"input": "horse"})
```

    [{'input': 'What did the cow say to the moon?', 'output': 'nothing at all'}, {'input': '2+4', 'output': '6'}]

#### 创建prompt模板

使用上述创建的`example_selector`组装prompt模板。

```python
from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

# 定义few-shot提示。
few_shot_prompt = FewShotChatMessagePromptTemplate(
    # 输入变量选择要传递给example_selector的值
    input_variables=["input"],
    example_selector=example_selector,
    # 定义每个示例的格式。
    # 在本例中，每个示例将成为2个消息：
    # 1个人类消息和1个AI消息
    example_prompt=ChatPromptTemplate.from_messages(
        [("human", "{input}"), ("ai", "{output}")]
    ),
)
```

下面是它的一个示例。

```python
print(few_shot_prompt.format(input="What's 3+3?"))
```

    Human: 2+3
    AI: 5
    Human: 2+2
    AI: 4

组装最终的prompt模板：

```python
final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a wondrous wizard of math."),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)
```

```python
print(few_shot_prompt.format(input="What's 3+3?"))
```

    Human: 2+3
    AI: 5
    Human: 2+2
    AI: 4
    
#### 用于LLM

现在，您可以将您的模型连接到few-shot提示。


```python
from langchain_community.chat_models import ChatAnthropic

chain = final_prompt | ChatAnthropic(temperature=0.0)

chain.invoke({"input": "3+3等于多少?"})
```




    AIMessage(content=' 3 + 3 = 6', additional_kwargs={}, example=False)




                

