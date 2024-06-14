
# 在运行时配置链内部

通常情况下，您可能希望尝试不同的方法来进行操作，甚至向最终用户公开多种不同的操作方式。
为了使这个体验尽可能简单，我们定义了两种方法。

首先是`configurable_fields`方法。
这使您可以配置可运行对象的特定字段。

其次是`configurable_alternatives`方法。
通过这个方法，您可以列出在运行时可以设置的任何特定可运行对象的替代方法。

## 配置字段

### 使用LLMs
通过LLMs，我们可以配置诸如温度之类的事物


```python
%pip install --upgrade --quiet  langchain langchain-openai
```


```python
from langchain.prompts import PromptTemplate
from langchain_core.runnables import ConfigurableField
from langchain_openai import ChatOpenAI

model = ChatOpenAI(temperature=0).configurable_fields(
    temperature=ConfigurableField(
        id="llm_temperature",
        name="LLM温度",
        description="LLM的温度",
    )
)
```


```python
model.invoke("选择一个随机数")
```




    AIMessage(content='7')




```python
model.with_config(configurable={"llm_temperature": 0.9}).invoke("选择一个随机数")
```




    AIMessage(content='34')



当它作为链的一部分使用时，我们也可以这样做


```python
prompt = PromptTemplate.from_template("选择一个大于{x}的随机数")
chain = prompt | model
```


```python
chain.invoke({"x": 0})
```




    AIMessage(content='57')




```python
chain.with_config(configurable={"llm_temperature": 0.9}).invoke({"x": 0})
```




    AIMessage(content='6')



### 使用HubRunnables

这对于允许切换提示非常有用


```python
from langchain.runnables.hub import HubRunnable
```


```python
prompt = HubRunnable("rlm/rag-prompt").configurable_fields(
    owner_repo_commit=ConfigurableField(
        id="hub_commit",
        name="Hub提交",
        description="从Hub获取的提交",
    )
)
```


```python
prompt.invoke({"question": "foo", "context": "bar"})
```




    ChatPromptValue(messages=[HumanMessage(content="您是一个用于问答任务的助手。使用以下检索上下文的碎片来回答问题。如果您不知道答案，只需说您不知道。最多使用三个句子并保持答案简洁。\n问题: foo \n上下文: bar \n答案:")])




```python
prompt.with_config(configurable={"hub_commit": "rlm/rag-prompt-llama"}).invoke(
    {"question": "foo", "context": "bar"}
)
```




    ChatPromptValue(messages=[HumanMessage(content="[INST]<<SYS>>您是一个用于问答任务的助手。使用以下检索上下文的碎片来回答问题。如果您不知道答案，只需说您不知道。最多使用三个句子并保持答案简洁。<</SYS>> \n问题: foo \n上下文: bar \n答案: [/INST]")])



## 可配置的替代方法



### 使用LLMs

让我们看看如何使用LLMs进行这样的操作


```python
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatAnthropic
from langchain_core.runnables import ConfigurableField
from langchain_openai import ChatOpenAI
```


```python
llm = ChatAnthropic(temperature=0).configurable_alternatives(
    # 这个给予此字段一个id
    # 当配置结束的可运行对象时，我们就可以使用这个id来配置此字段。
    ConfigurableField(id="llm"),
    # 这设置了一个默认的键。
    # 如果我们指定了这个键，则使用默认的LLM（上面初始化的ChatAnthropic）。
    default_key="anthropic",
    # 这添加一个新的选项，名称为`openai`，等于`ChatOpenAI()`
    openai=ChatOpenAI(),
    # 这添加一个新的选项，名称为`gpt4`，等于`ChatOpenAI(model="gpt-4")`
    gpt4=ChatOpenAI(model="gpt-4"),
    # 您可以在这里添加更多的配置选项
)
prompt = PromptTemplate.from_template("给我讲一个关于{topic}的笑话")
chain = prompt | llm
```


```python
# 默认情况下，它将调用Anthropic
chain.invoke({"topic": "bears"})
```




    AIMessage(content="这是一个关于熊的傻笑话：\n\n你如何称呼一个没有牙齿的熊？\n糖果熊！")




```python
# 我们可以使用 `.with_config(configurable={"llm": "openai"})`来指定要使用的llm
chain.with_config(configurable={"llm": "openai"}).invoke({"topic": "bears"})
```




    AIMessage(content="当然，给你讲个关于熊的笑话：\n\n为什么熊不穿鞋子？\n\n因为它们已经有熊脚了！")# 如果我们使用`default_key`，它将使用默认的配置项
chain.with_config(configurable={"llm": "anthropic"}).invoke({"topic": "bears"})
```




    AIMessage(content=" 这是关于熊的一个傻笑话：\n\n你怎么称呼一只没有牙齿的熊？\n一只软糖熊!")



### 使用提示

我们可以做类似的事情，但在提示之间轮流



```python
llm = ChatAnthropic(temperature=0)
prompt = PromptTemplate.from_template(
    "给我讲个关于{topic}的笑话"
).configurable_alternatives(
    # 这给这个字段一个id
    # 配置结束可运行时，我们可以使用这个id来配置这个字段
    ConfigurableField(id="prompt"),
    # 这设置了一个默认键。
    # 如果我们指定了这个键，则使用默认的LLM（ChatAnthropic在上面初始化）将被使用
    default_key="joke",
    # 这添加了一个新的选项，名称为`poem`
    poem=PromptTemplate.from_template("写一首关于{topic}的短诗"),
    # 在这里添加更多的配置选项
)
chain = prompt | llm
```


```python
# 默认情况下，它会写一个笑话
chain.invoke({"topic": "bears"})
```




    AIMessage(content=" 这是关于熊的一个傻笑话：\n\n你怎么称呼一只没有牙齿的熊？\n一只软糖熊!")




```python
# 我们可以配置它写一首诗
chain.with_config(configurable={"prompt": "poem"}).invoke({"topic": "bears"})
```




    AIMessage(content=' 这是关于熊的一首短诗:\n\n熊苏醒于睡梦中\n蹒跚而出进入深林\n高大树木抵达天际\n日落前寻找食物 \n它们毛茸茸的外套和锋利的爪子\n嗅探浆果和鱼\n毫不在乎地闲逛\n强大的灰熊和黑熊\n自豪而野性\n傲视领地\n徘徊于自己的森林\n在孤寂中回到自己的窝')




### 使用提示和LLM

我们也可以配置多个内容！
以下是一个示例，既使用提示又使用LLM进行配置。


```python
llm = ChatAnthropic(temperature=0).configurable_alternatives(
    # 这给这个字段一个id
    # 配置结束可运行时，我们可以使用这个id来配置这个字段
    ConfigurableField(id="llm"),
    # 这设置了一个默认键。
    # 如果我们指定了这个键，则使用默认的LLM（ChatAnthropic在上面初始化）将被使用
    default_key="anthropic",
    # 这添加了一个新的选项，名称为`openai`，它等于`ChatOpenAI()`
    openai=ChatOpenAI(),
    # 这添加了一个新的选项，名称为`gpt4`，它等于`ChatOpenAI(model="gpt-4")`
    gpt4=ChatOpenAI(model="gpt-4"),
    # 在这里添加更多的配置选项
)
prompt = PromptTemplate.from_template(
    "给我讲个关于{topic}的笑话"
).configurable_alternatives(
    # 这给这个字段一个id
    # 配置结束可运行时，我们可以使用这个id来配置这个字段
    ConfigurableField(id="prompt"),
    # 这设置了一个默认键。
    # 如果我们指定了这个键，则使用默认的LLM（ChatAnthropic在上面初始化）将被使用
    default_key="joke",
    # 这添加了一个新的选项，名称为`poem`
    poem=PromptTemplate.from_template("写一首关于{topic}的短诗"),
    # 在这里添加更多的配置选项
)
chain = prompt | llm
```


```python
# 我们可以配置它使用OpenAI写一首诗
chain.with_config(configurable={"prompt": "poem", "llm": "openai"}).invoke(
    {"topic": "bears"}
)
```




    AIMessage(content="在森林中，高大的树木摇摆，\n一种生物徘徊，既凶猛又灰色。\n有着强大的爪子和锐利的眼睛，\n熊，是力量的象征，挑战传统。\n\n在飘雪的山脉上，它徘徊，\n是林地之主的守护者。\n它浓密的皮毛如盔甲一般坚硬，\n它勇敢地面对最寒冷的冬夜。\n\n它是温柔的巨人，也是野性的自由，\n熊，坚定而令人敬畏。\n每一步都留下痕迹，\n展现着未驯服的力量和悠久的优雅。\n\n从甜蜜的盛宴到大马哈鱼的飞跃，\n它找到了自己的位置，在大自然的保卫战中。\n熊，一个奇迹，无论白天还是黑夜。\n\n让我们尊重这个高贵的生物，\n在它的灵魂找到宁静的森林里。\n因为在它的存在中，我们开始了解，\n野性的精神也在我们身上流淌。")




```python
# 如果我们想的话，我们也可以只配置其中一个
chain.with_config(configurable={"llm": "openai"}).invoke({"topic": "bears"})
```




    AIMessage(content="好的，这是一个关于熊的笑话:\n\n为什么熊不穿鞋？\n\n因为它们有熊脚!")


### 保存配置

我们还可以轻松保存配置好的链作为自己的对象


```python
openai_joke = chain.with_config(configurable={"llm": "openai"})
```


```python
openai_joke.invoke({"topic": "bears"})
```




    AIMessage(content="为什么熊不穿鞋？\n\n因为它们有熊脚!")


