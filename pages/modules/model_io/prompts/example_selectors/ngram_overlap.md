# 通过n-gram重叠选择

`NGramOverlapExampleSelector`根据示例与输入的相似度来选择和排序示例，并根据ngram重叠分数进行排序。 ngram重叠分数是一个范围在0.0到1.0之间的浮点数。

该选择器允许设置阈值分数。 ngram重叠分数小于或等于阈值的示例将被排除。默认情况下，阈值设置为-1.0，因此不会排除任何示例，只会重新排序它们。将阈值设置为0.0将排除与输入没有ngram重叠的示例。

```python
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.prompts.example_selector.ngram_overlap import NGramOverlapExampleSelector

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="输入：{input}\n输出：{output}",
)

# 一个虚构的翻译任务的示例。
examples = [
    {"input": "See Spot run.", "output": "Ver correr a Spot."},
    {"input": "My dog barks.", "output": "Mi perro ladra."},
    {"input": "Spot can run.", "output": "Spot puede correr."},
]
```

```python
example_selector = NGramOverlapExampleSelector(
    # 可供选择的示例。
    examples=examples,
    # 用于格式化示例的PromptTemplate。
    example_prompt=example_prompt,
    # 阈值，选择器停止的位置。
    # 默认设置为-1.0。
    threshold=-1.0,
    # 对于负阈值：
    # 选择器按ngram重叠分数对示例进行排序，并不排除任何示例。
    # 对于大于1.0的阈值：
    # 选择器排除所有示例，并返回一个空列表。
    # 对于等于0.0的阈值：
    # 选择器按ngram重叠分数对示例进行排序，
    # 并排除那些与输入没有ngram重叠的示例。
)
dynamic_prompt = FewShotPromptTemplate(
    # 我们提供一个ExampleSelector而不是示例。
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="给出每个输入的西班牙语翻译",
    suffix="输入: {sentence}\n输出:",
    input_variables=["sentence"],
)
```

```python
# 一个与"Spot can run."有很高ngram重叠的例子输入
# 与"My dog barks."没有重叠。
print(dynamic_prompt.format(sentence="Spot can run fast."))
```

    给出每个输入的西班牙语翻译
    
    输入: Spot can run.
    输出: Spot puede correr.
    
    输入: See Spot run.
    输出: Ver correr a Spot.
    
    输入: My dog barks.
    输出: Mi perro ladra.
    
    输入: Spot can run fast.
    输出:
```

```python
# 也可以向NGramOverlapExampleSelector添加示例。
new_example = {"input": "Spot plays fetch.", "output": "Spot juega a buscar."}

example_selector.add_example(new_example)
print(dynamic_prompt.format(sentence="Spot can run fast."))
```

    给出每个输入的西班牙语翻译
    
    输入: Spot can run.
    输出: Spot puede correr.
    
    输入: See Spot run.
    输出: Ver correr a Spot.
    
    输入: Spot plays fetch.
    输出: Spot juega a buscar.
    
    输入: My dog barks.
    输出: Mi perro ladra.
    
    输入: Spot can run fast.
    输出:
```

```python
# 可以设置一个阈值，以排除示例。
# 例如，将阈值设置为0.0
# 排除与输入没有ngram重叠的示例。
# 由于"My dog barks."与"Spot can run fast."没有ngram重叠
# 将被排除。
example_selector.threshold = 0.0
print(dynamic_prompt.format(sentence="Spot can run fast."))
```

    给出每个输入的西班牙语翻译
    
    输入: Spot can run.
    输出: Spot puede correr.
    
    输入: See Spot run.
    输出: Ver correr a Spot.
    
    输入: Spot plays fetch.
    输出: Spot juega a buscar.
    
    输入: Spot can run fast.
    输出:
```

```python
# 设置一个小的非零阈值
example_selector.threshold = 0.09
print(dynamic_prompt.format(sentence="Spot can play fetch."))
```

    给出每个输入的西班牙语翻译
    
    输入: Spot can run.
    输出: Spot puede correr.
    
    输入: Spot plays fetch.
    输出: Spot juega a buscar.
    
    输入: Spot can play fetch.
    输出:
```

```python
# 将阈值设置为大于1.0
example_selector.threshold = 1.0 + 1e-9
print(dynamic_prompt.format(sentence="Spot can play fetch."))
```

    给出每个输入的西班牙语翻译
    
    输入: Spot can play fetch.
    输出:
```