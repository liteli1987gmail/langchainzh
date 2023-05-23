
序列化
========


通常最好将提示存储为文件而不是Python代码。这样做可以方便地共享、存储和版本控制提示。本教程介绍了如何在LangChain中执行此操作，涵盖了所有不同类型的提示和不同的序列化选项。

在高层次上，序列化应用以下设计原则：

- 支持JSON和YAML。我们希望支持在磁盘上易于人类阅读的序列化方法，而YAML和JSON是两种最流行的方法。请注意，此规则适用于提示。对于其他资产（如示例)，可能支持不同的序列化方法。

- 我们支持在一个文件中指定所有内容，或者将不同的组件（模板、示例等)存储在不同的文件中并引用它们。对于某些情况，将所有内容存储在文件中是最合适的，但对于其他情况，拆分一些资产（长模板、大示例、可重用组件)可能更好。LangChain支持两种方式。

还有一个单一入口可以从硬盘加载提示，使得加载任何类型的提示变得容易。

```
# All prompts are loaded through the `load_prompt` function.
from langchain.prompts import load_prompt

```

PromptTemplate
------------------------

本部分涵盖了加载PromptTemplate的示例。

### 从YAML中加载

这是从YAML加载PromptTemplate的示例。

```
!cat simple_prompt.yaml

```

```
_type: prompt
input_variables:
    ["adjective", "content"]
template: 
    Tell me a {adjective} joke about {content}.

```

```
prompt = load_prompt("simple_prompt.yaml")
print(prompt.format(adjective="funny", content="chickens"))

```

```
Tell me a funny joke about chickens.

```

### 从JSON中加载

这是从JSON加载PromptTemplate的示例。

```
!cat simple_prompt.json

```

```
{
    "_type": "prompt",
    "input_variables": ["adjective", "content"],
    "template": "Tell me a {adjective} joke about {content}."
}

```

```
prompt = load_prompt("simple_prompt.json")
print(prompt.format(adjective="funny", content="chickens"))

```

Tell me a funny joke about chickens.

### Loading Template from a File[#](#loading-template-from-a-file "Permalink to this headline")

这显示了将模板存储在单独的文件中，然后在配置中引用它的示例。请注意，键从`template`更改为`template_path`。

```
!cat simple_template.txt

```

```
Tell me a {adjective} joke about {content}.

```

```
!cat simple_prompt_with_template_file.json

```

```
{
    "_type": "prompt",
    "input_variables": ["adjective", "content"],
    "template_path": "simple_template.txt"
}

```

```
prompt = load_prompt("simple_prompt_with_template_file.json")
print(prompt.format(adjective="funny", content="chickens"))

```

```
Tell me a funny joke about chickens.

```

few shot prompt模板的示例[#](#fewshotprompttemplate "Permalink to this headline")
-----------------------------------------------------------------------------

本节介绍了加载few shot prompt模板的示例。

### 示例[#](#examples "Permalink to this headline")

这显示了json格式的示例看起来像什么。

```
!cat examples.json

```

```
[
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"}
]

```

这是相同的示例存储为yaml可能看起来像什么。

```
!cat examples.yaml

```

```
- input: happy
  output: sad
- input: tall
  output: short

```

### 从YAML加载[#](#id1 "Permalink to this headline")

这显示了从YAML加载few shot示例的示例。

```
!cat few_shot_prompt.yaml

```

```
_type: few_shot
input_variables:
    ["adjective"]
prefix: 
    Write antonyms for the following words.
example_prompt:
    _type: prompt
    input_variables:
        ["input", "output"]
    template:
        "Input: {input}\nOutput: {output}"
examples:
    examples.json
suffix:
    "Input: {adjective}\nOutput:"

```

```
prompt = load_prompt("few_shot_prompt.yaml")
print(prompt.format(adjective="funny"))

```

```
Write antonyms for the following words.

Input: happy
Output: sad

Input: tall
Output: short

Input: funny
Output:

```

如果您从yaml文件加载示例，则同样适用。

```
!cat few_shot_prompt_yaml_examples.yaml

```

```
_type: few_shot
input_variables:
    ["adjective"]
prefix: 
    Write antonyms for the following words.
example_prompt:
    _type: prompt
    input_variables:
        ["input", "output"]
    template:
        "Input: {input}\nOutput: {output}"
examples:
    examples.yaml
suffix:
    "Input: {adjective}\nOutput:"

```

```
prompt = load_prompt("few_shot_prompt_yaml_examples.yaml")
print(prompt.format(adjective="funny"))

```

```
Write antonyms for the following words.

Input: happy
Output: sad

Input: tall
Output: short

Input: funny
Output:

```

### 从JSON加载[#](#id2 "Permalink to this headline")

这显示了从JSON加载few shot示例的示例。

```
!cat few_shot_prompt.json

```

```
{
    "_type": "few_shot",
    "input_variables": ["adjective"],
    "prefix": "Write antonyms for the following words.",
    "example_prompt": {
        "_type": "prompt",
        "input_variables": ["input", "output"],
        "template": "Input: {input}\nOutput: {output}"
    },
    "examples": "examples.json",
    "suffix": "Input: {adjective}\nOutput:"
}   

```

```
prompt = load_prompt("few_shot_prompt.json")
print(prompt.format(adjective="funny"))

```

```
Write antonyms for the following words.

Input: happy
Output: sad

Input: tall
Output: short

Input: funny
Output:

```

### 在配置中的示例[#](#examples-in-the-config "Permalink to this headline")

这是一个直接在配置文件中引用示例的示例。

```
!cat few_shot_prompt_examples_in.json

```

```
{
    "_type": "few_shot",
    "input_variables": ["adjective"],
    "prefix": "Write antonyms for the following words.",
    "example_prompt": {
        "_type": "prompt",
        "input_variables": ["input", "output"],
        "template": "Input: {input}\nOutput: {output}"
    },
    "examples": [
        {"input": "happy", "output": "sad"},
        {"input": "tall", "output": "short"}
    ],
    "suffix": "Input: {adjective}\nOutput:"
}   

```

```
prompt = load_prompt("few_shot_prompt_examples_in.json")
print(prompt.format(adjective="funny"))

```

```
Write antonyms for the following words.

Input: happy
Output: sad

Input: tall
Output: short

Input: funny
Output:

```

### 来自文件的示例提示[#](#example-prompt-from-a-file "Permalink to this headline")

这是一个从单独的文件加载用于格式化示例的PromptTemplate的示例。请注意，键从`example_prompt`更改为`example_prompt_path`。

```
!cat example_prompt.json

```

```
{
    "_type": "prompt",
    "input_variables": ["input", "output"],
    "template": "Input: {input}\nOutput: {output}" 
}

```

```
!cat few_shot_prompt_example_prompt.json 

```

```
{
    "_type": "few_shot",
    "input_variables": ["adjective"],
    "prefix": "Write antonyms for the following words.",
    "example_prompt_path": "example_prompt.json",
    "examples": "examples.json",
    "suffix": "Input: {adjective}\nOutput:"
}   

```

```
prompt = load_prompt("few_shot_prompt_example_prompt.json")
print(prompt.format(adjective="funny"))

```

```
Write antonyms for the following words.

Input: happy
Output: sad

Input: tall
Output: short

Input: funny
Output:

```

