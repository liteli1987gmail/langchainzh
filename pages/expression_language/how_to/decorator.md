# 使用 @chain 装饰器创建可运行的链式函数

您还可以通过添加 `@chain` 装饰器将任意函数转换为链式函数。这在功能上等同于在 [`RunnableLambda`](/expression_language/primitives/functions) 中进行包装。

这将通过正确跟踪您的链式函数来改善可观察性。在此函数内部对可运行函数的任何调用将被跟踪为嵌套子项。

它还将允许您像使用任何其他可运行函数一样使用它，将其组合成链式函数等。

让我们看看实际操作！

```python
%pip install --upgrade --quiet  langchain langchain-openai
```

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain
from langchain_openai import ChatOpenAI
```

```python
prompt1 = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
prompt2 = ChatPromptTemplate.from_template("What is the subject of this joke: {joke}")
```

```python
@chain
def custom_chain(text):
    prompt_val1 = prompt1.invoke({"topic": text})
    output1 = ChatOpenAI().invoke(prompt_val1)
    parsed_output1 = StrOutputParser().invoke(output1)
    chain2 = prompt2 | ChatOpenAI() | StrOutputParser()
    return chain2.invoke({"joke": parsed_output1})
```

`custom_chain` 现在是一个可运行的函数，这意味着您需要使用 `invoke`

```python
custom_chain.invoke("bears")
```

查看您的 LangSmith 跟踪，您应该会在其中看到一个名为 `custom_chain` 的跟踪，并在其下面嵌套调用 OpenAI 的调用
