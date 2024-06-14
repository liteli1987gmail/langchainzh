# 按相似性选择

这个对象根据与输入的相似性选择示例。它通过找到具有与输入具有最大余弦相似度的嵌入的示例来实现这一点。

```python
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}",
)

# 一个假设任务的示例，创建反义词。
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]
```

```python
example_selector = SemanticSimilarityExampleSelector.from_examples(
    # 可供选择的示例列表。
    examples,
    # 用于生成嵌入的嵌入类，用于测量语义相似性。
    OpenAIEmbeddings(),
    # 用于存储嵌入并进行相似性搜索的VectorStore类。
    Chroma,
    # 要生成的示例数量。
    k=1,
)
similar_prompt = FewShotPromptTemplate(
    # 我们提供ExampleSelector而不是示例。
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="给出每个输入的反义词",
    suffix="Input: {adjective}\nOutput:",
    input_variables=["adjective"],
)
```

```python
# 输入是一种感觉，所以应选择happy/sad示例
print(similar_prompt.format(adjective="worried"))
```

    给出每个输入的反义词
    
    Input: happy
    Output: sad
    
    Input: worried
    Output:
```

```python
# 输入是一个测量，所以应选择tall/short示例
print(similar_prompt.format(adjective="large"))
```

    给出每个输入的反义词
    
    Input: tall
    Output: short
    
    Input: large
    Output:
```

```python
# 您也可以向SemanticSimilarityExampleSelector添加新示例
similar_prompt.example_selector.add_example(
    {"input": "enthusiastic", "output": "apathetic"}
)
print(similar_prompt.format(adjective="passionate"))
```

    给出每个输入的反义词
    
    Input: enthusiastic
    Output: apathetic
    
    Input: passionate
    Output:
```



