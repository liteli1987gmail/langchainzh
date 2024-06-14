# 少量提示模板

在本教程中，我们将学习如何创建一个使用少量示例的提示模板。少量提示模板可以从示例集或示例选择器对象构建。

### 用例

在本教程中，我们将为自问自答配置少量示例。

## 使用示例集

### 创建示例集

要开始，请创建一个少量示例列表。每个示例都应是一个字典，其键为输入变量，值为这些输入变量的值。

```python
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

examples = [
    {
        "question": "谁活得更久，穆罕默德·阿里还是艾伦·图灵？",
        "answer": """
这里是否需要跟进问题：是的。
后续问题：穆罕默德·阿里去世时年龄多大？
中间答案：穆罕默德·阿里去世时74岁。
后续问题：艾伦·图灵去世时多大？
中间答案：艾伦·图灵去世时41岁。
因此最终答案是：穆罕默德·阿里
""",
    },
    {
        "question": "craigslist的创始人是什么时候出生？",
        "answer": """
这里是否需要跟进问题：是的。
后续问题：craigslist的创始人是谁？
中间答案：craigslist的创始人是Craig Newmark。
后续问题：Craig Newmark是何时出生的？
中间答案：Craig Newmark于1952年12月6日出生。
因此最终答案是：1952年12月6日
""",
    },
    {
        "question": "乔治·华盛顿的外祖父是谁？",
        "answer": """
这里是否需要跟进问题：是的。
后续问题：乔治·华盛顿的母亲是谁？
中间答案：乔治·华盛顿的母亲是玛丽·波尔·华盛顿。
后续问题：玛丽·波尔·华盛顿的父亲是谁？
中间答案：玛丽·波尔·华盛顿的父亲是约瑟夫·鲍尔。
因此最终答案是：约瑟夫·鲍尔
""",
    },
    {
        "question": "《大白鲨》和《皇家赌场》的导演都来自同一个国家吗？",
        "answer": """
这里是否需要跟进问题：是的。
后续问题：《大白鲨》的导演是谁？
中间答案：《大白鲨》的导演是史蒂芬·斯皮尔伯格。
后续问题：史蒂芬·斯皮尔伯格来自哪里？
中间答案：美国。
后续问题：《皇家赌场》的导演是谁？
中间答案：《皇家赌场》的导演是马丁·坎贝尔。
后续问题：马丁·坎贝尔来自哪里？
中间答案：新西兰。
因此最终答案是：否
""",
    },
]
```

### 为少量示例创建格式化程序

配置一个格式化程序，将少量示例格式化为字符串。此格式化程序应该是一个`PromptTemplate`对象。

```python
example_prompt = PromptTemplate(
    input_variables=["question", "answer"], template="问题：{question}\n{answer}"
)

print(example_prompt.format(**examples[0]))
```

    问题：谁活得更久，穆罕默德·阿里还是艾伦·图灵？
    
    这里是否需要跟进问题：是的。
    后续问题：穆罕默德·阿里去世时年龄多大？
    中间答案：穆罕默德·阿里去世时74岁。
    后续问题：艾伦·图灵去世时多大？
    中间答案：艾伦·图灵去世时41岁。
    因此最终答案是：穆罕默德·阿里
    

### 将示例和格式化程序提供给`FewShotPromptTemplate`

最后，创建一个`FewShotPromptTemplate`对象。此对象接收少量示例和少量示例的格式化程序。

```python
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="问题：{input}",
    input_variables=["input"],
)

print(prompt.format(input="玛丽·波尔·华盛顿的父亲是谁？"))
```

    问题：谁活得更久，穆罕默德·阿里还是艾伦·图灵？
    
    这里是否需要跟进问题：是的。
    后续问题：穆罕默德·阿里去世时年龄多大？
    中间答案：穆罕默德·阿里去世时74岁。
    后续问题：艾伦·图灵去世时多大？
    中间答案：艾伦·图灵去世时41岁。
    因此最终答案是：穆罕默德·阿里
    
    
    问题：craigslist的创始人是什么时候出生？
    
    这里是否需要跟进问题：是的。
    后续问题：craigslist的创始人是谁？
    中间答案：craigslist的创始人是Craig Newmark。
    后续问题：Craig Newmark是何时出生的？
    中间答案：Craig Newmark于1952年12月6日出生。
    因此最终答案是：1952年12月6日
    
    
    问题：乔治·华盛顿的外祖父是谁？
    
    这里是否需要跟进问题：是的。
    后续问题：乔治·华盛顿的母亲是谁？
    中间答案：乔治·华盛顿的母亲是玛丽·波尔·华盛顿。
    后续问题：玛丽·波尔·华盛顿的父亲是谁？
    中间答案：玛丽·波尔·华盛顿的父亲是约瑟夫·鲍尔。
    因此最终答案是：约瑟夫·鲍尔
    
    
    问题：《大白鲨》和《皇家赌场》的导演都来自同一个国家吗？
    
    这里是否需要跟进问题：是的。
    后续问题：《大白鲨》的导演是谁？
    中间答案：《大白鲨》的导演是史蒂芬·斯皮尔伯格。
    后续问题：史蒂芬·斯皮尔伯格来自哪里？
    中间答案：美国。
    后续问题：《皇家赌场》的导演是谁？
    中间答案：《皇家赌场》的导演是马丁·坎贝尔。
    后续问题：马丁·坎贝尔来自哪里？
    中间答案：新西兰。
    因此最终答案是：否
    
    
    问题：玛丽·波尔·华盛顿的父亲是谁？
    

## 使用示例选择器

### 将示例提供给`ExampleSelector`

我们将重用上一节的示例集和格式化程序。但是，我们不会直接将示例提供给`FewShotPromptTemplate`对象，而是将它们提供给一个`ExampleSelector`对象。

在本教程中，我们将使用`SemanticSimilarityExampleSelector`类。此类根据示例与输入之间的相似度选择少量示例。它使用嵌入模型计算输入和少量示例之间的相似度，以及矢量存储进行最近邻搜索。

```python
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

example_selector = SemanticSimilarityExampleSelector.from_examples(
    # 这是可供选择的示例列表。
    examples,
    # 这是用于生成嵌入的嵌入类，用于测量语义相似度。
    OpenAIEmbeddings(),
    # 这是用于存储嵌入并执行相似性搜索的VectorStore类。
    Chroma,
    # 这是要生成的示例数。
    k=1,
)

# 选择与输入最相似的示例。
question = "玛丽·波尔·华盛顿的父亲是谁？"
selected_examples = example_selector.select_examples({"question": question})
print(f"最接近输入的示例：{question}")
for example in selected_examples:
    print("\n")
    for k, v in example.items():
        print(f"{k}: {v}")
```

最接近输入的示例：玛丽·波尔·华盛顿的父亲是谁？

    answer: 
    这里是否需要跟进问题：是的。
    后续问题：乔治·华盛顿的母亲是谁？
    中间答案：乔治·华盛顿的母亲是玛丽·波尔·华盛顿。
    后续问题：玛丽·波尔·华盛顿的父亲是谁？
    中间答案：玛丽·波尔·华盛顿的父亲是约瑟夫·鲍尔。
    因此最终答案是：约瑟夫·鲍尔
    
    question: 乔治·华盛顿的外祖父是谁？### 将示例选择器传递给`FewShotPromptTemplate`

最后，创建一个`FewShotPromptTemplate`对象。这个对象接受示例选择器和few-shot示例的格式化器。



```python
prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

print(prompt.format(input="Who was the father of Mary Ball Washington?"))
```

    Question: Who was the maternal grandfather of George Washington?
    
    是否需要后续问题: 是的。
    后续问题: Who was the mother of George Washington?
    中间答案: George Washington的母亲是Mary Ball Washington。
    后续问题: Who was the father of Mary Ball Washington?
    中间答案: Mary Ball Washington的父亲是Joseph Ball。
    因此最终答案是: Joseph Ball
    
    
    Question: Who was the father of Mary Ball Washington?
    








