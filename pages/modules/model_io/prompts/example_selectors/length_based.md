# 选择依据长度

该示例选择器根据长度选择要使用的示例。当您担心构建的提示超过上下文窗口的长度时，这将非常有用。对于较长的输入，它会选择少量要包含的示例，而对于较短的输入，它会选择更多。

```python
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector

# 创建反义词的假任务示例。
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}",
)
example_selector = LengthBasedExampleSelector(
    # 可供选择的示例。
    examples=examples,
    # 用于格式化示例的PromptTemplate。
    example_prompt=example_prompt,
    # 格式化示例的最大长度。
    # 长度由下方的get_text_length函数测量。
    max_length=25,
    # 用于获取字符串长度的函数，用于确定要包含哪些示例。如果未指定，则将其作为默认值提供。
    # get_text_length: Callable[[str], int] = lambda x: len(re.split("\n| ", x))
)
dynamic_prompt = FewShotPromptTemplate(
    # 我们提供一个ExampleSelector而不是示例。
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="给出每个输入的反义词",
    suffix="Input: {adjective}\nOutput:",
    input_variables=["adjective"],
)
```


```python
# 一个具有较小输入的示例，因此它选择了全部示例。
print(dynamic_prompt.format(adjective="big"))
```

    给出每个输入的反义词
    
    Input: happy
    Output: sad
    
    Input: tall
    Output: short
    
    Input: energetic
    Output: lethargic
    
    Input: sunny
    Output: gloomy
    
    Input: windy
    Output: calm
    
    Input: big
    Output:
    


```python
# 一个具有较长输入的示例，因此它只选择一个示例。
long_string = "big and huge and massive and large and gigantic and tall and much much much much much bigger than everything else"
print(dynamic_prompt.format(adjective=long_string))
```

    给出每个输入的反义词
    
    Input: happy
    Output: sad
    
    Input: big and huge and massive and large and gigantic and tall and much much much much much bigger than everything else
    Output:
    


```python
# 您还可以将示例添加到示例选择器中。
new_example = {"input": "big", "output": "small"}
dynamic_prompt.example_selector.add_example(new_example)
print(dynamic_prompt.format(adjective="enthusiastic"))
```

    给出每个输入的反义词
    
    Input: happy
    Output: sad
    
    Input: tall
    Output: short
    
    Input: energetic
    Output: lethargic
    
    Input: sunny
    Output: gloomy
    
    Input: windy
    Output: calm
    
    Input: big
    Output: small
    
    Input: enthusiastic
    Output:
    




