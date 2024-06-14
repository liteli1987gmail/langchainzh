# 合成高级组件

本节包含将其他任意系统（例如外部API和服务）和/或LangChain基元件组合在一起的高级组件。

阅读[LangChain表达语言](/expression_language/get_started)部分，并熟悉通过管道构建序列和提供的各种基元素将是本节的良好入门。

本节涵盖的组件有：

## [工具](/modules/tools/)

工具提供了LLMs和其他组件与其他系统交互的接口。示例包括维基百科，计算器和Python REPL。

## [代理](/modules/agents)

代理使用语言模型来决定采取的行动，通常由工具定义。它们需要一个`executor`，即代理的运行时。executor实际上调用代理，执行它选择的工具，将动作输出传回代理，并重复这个过程。代理负责解析先前结果的输出并选择下一步。

## [链](/modules/chains)

构建其他基元素和组件的积木风格合成。
                # Composition

LangChain提供了一个用户友好的界面，用于将不同部分的提示组合在一起。您可以使用字符串提示或聊天提示进行此操作。以这种方式构建提示可以轻松重用组件。

## 字符串提示的组合

在使用字符串提示时，每个模板都被连接在一起。您可以直接使用提示或字符串（列表中的第一个元素必须是提示）。

```python
from langchain.prompts import PromptTemplate
```

```python
prompt = (
    PromptTemplate.from_template("告诉我一个关于 {topic} 的笑话")
    + "，搞笑点"
    + "\n\n以及用 {language} 说"
)
```

```python
prompt
```

```python
prompt.format(topic="体育", language="西班牙语")
```

您也可以像以前一样在LLMChain中使用它。

```python
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
```

```python
model = ChatOpenAI()
```

```python
chain = LLMChain(llm=model, prompt=prompt)
```

```python
chain.run(topic="体育", language="西班牙语")
```

## 聊天提示的组合

聊天提示由一系列消息组成。出于开发者体验考虑，我们提供了一种方便的方法来创建这些提示。在此管道中，每个新元素都是最终提示中的新消息。

```python
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
```

首先，让我们使用系统消息初始化基本的ChatPromptTemplate。它不一定要以系统开始，但通常是一个好习惯。

```python
prompt = SystemMessage(content="你是一个很好的海盗")
```

然后，您可以轻松地创建一个包含其他消息或消息模板的管道。当没有要格式化的变量时，请使用`Message`，当有要格式化的变量时，请使用`MessageTemplate`。您也可以只使用一个字符串（注：这将自动推断为HumanMessagePromptTemplate）。

```python
new_prompt = (
    prompt + HumanMessage(content="嗨") + AIMessage(content="什么？") + "{input}"
```

在后台，这将创建一个ChatPromptTemplate类的实例，因此您可以像以前一样使用！

```python
new_prompt.format_messages(input="我说了嗨")
```

您也可以像以前一样在LLMChain中使用它。

```python
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
```

```python
model = ChatOpenAI()
```

```python
chain = LLMChain(llm=model, prompt=new_prompt)
```

```python
chain.run("我说了嗨")
```

## 使用PipelinePrompt

LangChain包括一个抽象【PipelinePromptTemplate】，在您想要重用提示的部分时可能很有用。PipelinePrompt由两个主要部分组成：

- 最终提示：返回的最终提示
- 管道提示：一个元组列表，包含一个字符串名称和一个提示模板。每个提示模板将被格式化，然后作为具有相同名称的变量传递给未来的提示模板。

```python
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate
```

```python
full_template = """{介绍}

{示例}

{开始}"""
full_prompt = PromptTemplate.from_template(full_template)
```

```python
introduction_template = """您正在模仿 {person}。"""
introduction_prompt = PromptTemplate.from_template(introduction_template)
```

```python
example_template = """这是一个互动的示例：

Q：{example_q}
A：{example_a}"""
example_prompt = PromptTemplate.from_template(example_template)
```

```python
start_template = """现在，真正做到这一点！

Q：{input}
A："""
start_prompt = PromptTemplate.from_template(start_template)
``````python
input_prompts = [
    ("介绍", introduction_prompt),
    ("示例", example_prompt),
    ("开始", start_prompt),
]
pipeline_prompt = PipelinePromptTemplate(
    final_prompt=full_prompt, pipeline_prompts=input_prompts
)
```


```python
pipeline_prompt.input_variables
```




    ['example_q', 'person', 'input', 'example_a']




```python
print(
    pipeline_prompt.format(
        person="Elon Musk",
        example_q="你最喜欢的汽车是什么？",
        example_a="特斯拉",
        input="你最喜欢的社交媒体网站是什么？",
    )
)
```

    你正在冒充埃隆·马斯克。
    
    以下是一个交互示例：
    
    问：你最喜欢的汽车是什么？
    答：特斯拉
    
    现在，来做真实的事情！
    
    问：你最喜欢的社交媒体网站是什么？
    答：
    
```