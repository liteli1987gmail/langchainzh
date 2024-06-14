# 多链

可将可运行对象轻松用于多个链的串联


```python
%pip install --upgrade --quiet  langchain langchain-openai
```


```python
from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt1 = ChatPromptTemplate.from_template("城市 {person} 来自于哪里?")
prompt2 = ChatPromptTemplate.from_template(
    "城市 {city} 在哪个国家？用语言 {language} 回答"
)

model = ChatOpenAI()

chain1 = prompt1 | model | StrOutputParser()

chain2 = (
    {"city": chain1, "language": itemgetter("language")}
    | prompt2
    | model
    | StrOutputParser()
)

chain2.invoke({"person": "obama", "language": "spanish"})
```




    '巴拉克·奥巴马是美国第44任总统，他出生在檀香山，檀香山所在的国家是美国。檀香山位于夏威夷州的瓦胡岛上。'




```python
from langchain_core.runnables import RunnablePassthrough

prompt1 = ChatPromptTemplate.from_template(
    "生成一种 {attribute} 的颜色。只返回颜色的名称:"
)
prompt2 = ChatPromptTemplate.from_template(
    "颜色 {color} 的水果是什么？只返回水果的名称:"
)
prompt3 = ChatPromptTemplate.from_template(
    "国旗的颜色中有颜色 {color} 的国家是哪个？只返回国家的名称:"
)
prompt4 = ChatPromptTemplate.from_template(
    "{fruit} 的颜色和 {country} 的国旗是什么？"
)

model_parser = model | StrOutputParser()

color_generator = (
    {"attribute": RunnablePassthrough()} | prompt1 | {"color": model_parser}
)
color_to_fruit = prompt2 | model_parser
color_to_country = prompt3 | model_parser
question_generator = (
    color_generator | {"fruit": color_to_fruit, "country": color_to_country} | prompt4
)
```


```python
question_generator.invoke("温暖的")
```




    ChatPromptValue(messages=[HumanMessage(content='草莓的颜色和中国的国旗是什么？', additional_kwargs={}, example=False)])




```python
prompt = question_generator.invoke("温暖的")
model.invoke(prompt)
```




    AIMessage(content='苹果通常是红色或绿色的。中国的国旗主要是红色的，左上角有一个大的黄色星星，周围还有四颗较小的黄色星星。', additional_kwargs={}, example=False)



### 分支和合并

您可能希望将一个组件的输出结果处理为两个或多个其他组件的输入。[RunnableParallels](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.base.RunnableParallel.html#langchain_core.runnables.base.RunnableParallel) 使您可以将链分割或分叉，以便多个组件可以并行处理输入。稍后，其他组件可以合并结果，以合成最终的响应。这种类型的链创建了一个计算图，如下所示：

```text
     输入
      / \
     /   \
 分支1 分支2
     \   /
      \ /
      合并
```


```python
planner = (
    ChatPromptTemplate.from_template("关于 {input} 生成一个论点")
    | ChatOpenAI()
    | StrOutputParser()
    | {"base_response": RunnablePassthrough()}
)

arguments_for = (
    ChatPromptTemplate.from_template(
        "列举 {base_response} 的优点或正面方面"
    )
    | ChatOpenAI()
    | StrOutputParser()
)
arguments_against = (
    ChatPromptTemplate.from_template(
        "列举 {base_response} 的缺点或负面方面"
    )
    | ChatOpenAI()
    | StrOutputParser()
)

final_responder = (
    ChatPromptTemplate.from_messages(
        [
            ("ai", "{original_response}"),
            ("human", "优点:\n{results_1}\n\n缺点:\n{results_2}"),
            ("system", "根据批评生成最终响应"),
        ]
    )
    | ChatOpenAI()
    | StrOutputParser()
)

chain = (
    planner
    | {
        "results_1": arguments_for,
        "results_2": arguments_against,
        "original_response": itemgetter("base_response"),
    }
    | final_responder
)
```


```python
chain.invoke({"input": "scrum"})
```




    '尽管Scrum存在潜在的缺点和挑战，但许多组织已经成功地采用和实施了这一项目管理框架，取得了很大的效果。上述的缺点可以通过适当的培训、支持和持续改进来减轻或克服。还需要注意的是，并非所有的缺点都适用于每个组织或项目。\n\n例如，尽管Scrum在最初可能较为复杂，但通过适当的培训和指导，团队可以迅速掌握相关概念和实践。可以通过实施速度追踪和发布计划等技术来缓解预测性不足的问题。通过保持轻量级文档和团队成员之间的清晰沟通之间取得平衡可以解决文档不足的问题。通过有效的沟通渠道和定期的团队建设活动可以改善对团队协作的依赖。\n\nScrum可以通过使用Scrum of Scrums或LeSS（Large Scale Scrum）等框架来进行扩展和适应更大型的项目。通过将质量保证实践（如持续集成和自动化测试）纳入Scrum过程中，可以解决速度与质量之间的问题。可以通过具有明确定义和优先级的产品待办事项以及通过培训和指导发展强大的产品负责人来管理范围蔓延的问题。\n\n通过为利益相关者提供适当的教育和沟通，并将其融入决策过程，可以克服对变革的抵抗。最后，Scrum的缺点可以被视为增长和改进的机会，在正确的心态和支持下，可以有效地管理。\n\n总之，尽管Scrum可能存在挑战和潜在的缺点，但其在协作、灵活性、适应性、透明度和客户满意度等方面所提供的益处和优势使其成为一个被广泛采用和成功的项目管理框架。通过适当的实施和持续改进，组织可以利用Scrum推动创新、效率和项目的成功。'


------
