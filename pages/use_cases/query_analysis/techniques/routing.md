# 路由

有时我们会针对不同的领域建立多个索引，并且针对不同的问题我们想要查询这些索引的不同子集。例如，假设我们有一个用于所有LangChain Python文档的向量存储索引，以及一个用于所有LangChain JS文档的索引。给定一个关于LangChain用法的问题，我们希望推断出问题所指的是哪种语言，并查询相应的文档。**查询路由**就是确定查询应该在哪个索引或索引子集上执行的过程。

## 设置
#### 安装依赖项


```python
%pip install -qU langchain-core langchain-openai
```

#### 设置环境变量

我们将在这个示例中使用OpenAI：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 可选的，取消下面的注释以使用LangSmith进行追踪。在这里注册：https://smith.langchain.com。
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 使用函数调用模型进行路由

使用函数调用模型对于分类非常简单，而路由实际上就是分类的过程：


```python
from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI


class RouteQuery(BaseModel):
    """将用户查询路由到最相关的数据源。"""

    datasource: Literal["python_docs", "js_docs", "golang_docs"] = Field(
        ...,
        description="给定一个用户问题，选择最相关的数据源来回答他们的问题",
    )


llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
structured_llm = llm.with_structured_output(RouteQuery)

system = """您是一个专家，负责将用户问题路由到适当的数据源。

根据问题所涉及的编程语言，将其路由到相应的数据源。"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

router = prompt | structured_llm
```

    /Users/bagatur/langchain/libs/core/langchain_core/_api/beta_decorator.py:86: LangChainBetaWarning: The function `with_structured_output` is in beta. It is actively being worked on, so the API may change.
      warn_beta(
    


```python
question = """为什么下面的代码不起作用：

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(["human", "speak in {language}"])
prompt.invoke("french")
"""
router.invoke({"question": question})
```




    RouteQuery(datasource='python_docs')




```python
question = """为什么下面的代码不起作用：


import { ChatPromptTemplate } from "@langchain/core/prompts";


const chatPrompt = ChatPromptTemplate.fromMessages([
  ["human", "speak in {language}"],
]);

const formattedChatPrompt = await chatPrompt.invoke({
  input_language: "french"
});
"""
router.invoke({"question": question})
```




    RouteQuery(datasource='js_docs')



## 路由到多个索引

如果我们希望查询多个索引，也可以通过更新模式来实现接受数据源的列表：


```python
from typing import List


class RouteQuery(BaseModel):
    """将用户查询路由到最相关的数据源。"""

    datasources: List[Literal["python_docs", "js_docs", "golang_docs"]] = Field(
        ...,
        description="给定一个用户问题，选择最相关的数据源来回答他们的问题",
    )


llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
structured_llm = llm.with_structured_output(RouteQuery)
router = prompt | structured_llm
router.invoke(
    {
        "question": "Python和JS实现的OpenAI聊天模型之间是否具有功能的平等性"
    }
)
```




    RouteQuery(datasources=['python_docs', 'js_docs'])

------
