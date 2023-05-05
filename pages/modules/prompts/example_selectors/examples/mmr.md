

最大边际相关性示例选择器[#](#maximal-marginal-relevance-exampleselector "本标题的永久链接")
=======================================================================

MaxMarginalRelevanceExampleSelector基于哪些示例与输入最相似以及优化多样性的组合选择示例。它通过找到嵌入与输入具有最大余弦相似度的示例，然后迭代地添加它们，同时惩罚它们与已选择示例的接近程度来实现这一目的。

```
from langchain.prompts.example_selector import MaxMarginalRelevanceExampleSelector
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}",
)

# These are a lot of examples of a pretend task of creating antonyms.
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]

```

```
example_selector = MaxMarginalRelevanceExampleSelector.from_examples(
    # This is the list of examples available to select from.
    examples, 
    # This is the embedding class used to produce embeddings which are used to measure semantic similarity.
    OpenAIEmbeddings(), 
    # This is the VectorStore class that is used to store the embeddings and do a similarity search over.
    FAISS, 
    # This is the number of examples to produce.
    k=2
)
mmr_prompt = FewShotPromptTemplate(
    # We provide an ExampleSelector instead of examples.
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="Give the antonym of every input",
    suffix="Input: {adjective}\nOutput:", 
    input_variables=["adjective"],
)

```

```
# Input is a feeling, so should select the happy/sad example as the first one
print(mmr_prompt.format(adjective="worried"))

```

```
Give the antonym of every input

Input: happy
Output: sad

Input: windy
Output: calm

Input: worried
Output:

```

```
# Let's compare this to what we would just get if we went solely off of similarity
similar_prompt = FewShotPromptTemplate(
    # We provide an ExampleSelector instead of examples.
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="Give the antonym of every input",
    suffix="Input: {adjective}\nOutput:", 
    input_variables=["adjective"],
)
similar_prompt.example_selector.k = 2
print(similar_prompt.format(adjective="worried"))

```

```
Give the antonym of every input

Input: happy
Output: sad

Input: windy
Output: calm

Input: worried
Output:

```

