# 提示LLM解析器（PromptLlmParser）

最常见和有价值的组合是：

``PromptTemplate`` / ``ChatPromptTemplate`` -> ``LLM`` / ``ChatModel`` -> ``OutputParser``

几乎任何其他链都将使用这个构建块。

## PromptTemplate + LLM

最简单的组合就是将提示和模型组合起来，创建一个链条，它接受用户输入，将其添加到提示中，传递给模型，并返回原始模型输出。

注意，在这里您可以任意混合匹配PromptTemplate/ChatPromptTemplate和LLMs/ChatModels。
%pip install --upgrade --quiet  langchain langchain-openai

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("给我讲一个关于{foo}的笑话")
model = ChatOpenAI()
chain = prompt | model
```


```python
chain.invoke({"foo": "bears"})
```




    AIMessage(content="为什么熊不穿鞋子?\n\n因为它们有熊脚!", additional_kwargs={}, example=False)



通常我们希望附加每个模型调用将传递的kwargs。以下是一些示例：

### 添加停止序列

```python
chain = prompt | model.bind(stop=["\n"])
```


```python
chain.invoke({"foo": "bears"})
```




    AIMessage(content='为什么熊从不穿鞋子?', additional_kwargs={}, example=False)



### 添加函数调用信息

```python
functions = [
    {
        "name": "joke",
        "description": "一个笑话",
        "parameters": {
            "type": "object",
            "properties": {
                "setup": {"type": "string", "description": "笑话的设定"},
                "punchline": {
                    "type": "string",
                    "description": "笑话的结尾",
                },
            },
            "required": ["setup", "punchline"],
        },
    }
]
chain = prompt | model.bind(function_call={"name": "joke"}, functions=functions)
```


```python
chain.invoke({"foo": "bears"}, config={})
```




    AIMessage(content='', additional_kwargs={'function_call': {'name': 'joke', 'arguments': '{\n  "setup": "为什么熊不穿鞋子?",\n  "punchline": "因为它们有熊脚!"\n}'}}, example=False)



## PromptTemplate + LLM + OutputParser

我们还可以添加一个输出解析器，将原始的LLM/ChatModel输出方便地转换为更易处理的格式。

```python
from langchain_core.output_parsers import StrOutputParser

chain = prompt | model | StrOutputParser()
```

注意，这现在返回一个字符串 - 一个更易处理的格式，用于下游任务。


```python
chain.invoke({"foo": "bears"})
```




    "为什么熊不穿鞋子?\n\n因为它们有熊脚!"



### 函数输出解析器

当您指定要返回的函数时，您可能只想直接解析它。

```python
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser

chain = (
    prompt
    | model.bind(function_call={"name": "joke"}, functions=functions)
    | JsonOutputFunctionsParser()
)
```


```python
chain.invoke({"foo": "bears"})
```




    {'setup': '为什么熊不喜欢快餐？',
     'punchline': '因为它们抓不住它！'}




```python
from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser

chain = (
    prompt
    | model.bind(function_call={"name": "joke"}, functions=functions)
    | JsonKeyOutputFunctionsParser(key_name="setup")
)
```


```python
chain.invoke({"foo": "bears"})
```




    "为什么熊不穿鞋子?"



## 简化输入

为了使调用更简单，我们可以添加一个`RunnableParallel`来为我们创建提示输入字典：

```python
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

map_ = RunnableParallel(foo=RunnablePassthrough())
chain = (
    map_
    | prompt
    | model.bind(function_call={"name": "joke"}, functions=functions)
    | JsonKeyOutputFunctionsParser(key_name="setup")
)
```


```python
chain.invoke("bears")
```




    "为什么熊不穿鞋子?"


------由于我无法直接翻译mdx文档，但我可以解释一下md文档中的内容：

```python
chain = (
    {"foo": RunnablePassthrough()}
    | prompt
    | model.bind(function_call={"name": "joke"}, functions=functions)
    | JsonKeyOutputFunctionsParser(key_name="setup")
)
```

以上是一段Python代码，创建了一个名为`chain`的可调用链。在这个代码段中使用了一些语法糖，使用了一个字典作为参数。

```python
chain.invoke("bears")
```

以上代码是调用`chain`对象的`invoke`函数，传入了参数`"bears"`。

希望这些解释对您有所帮助。