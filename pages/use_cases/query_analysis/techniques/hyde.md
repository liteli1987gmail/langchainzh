# Hypothetical Document Embeddings

如果我们正在使用基于相似性搜索的索引，比如向量存储，那么直接搜索原始问题可能效果不佳，因为它们的嵌入可能与相关文档的嵌入不太相似。因此，通过生成一个假设的相关文档，然后使用它进行相似性搜索可能会有所帮助。这是[Hypothetical Document Embedding](https://arxiv.org/pdf/2212.10496.pdf)（简称HyDE）的核心思想。

让我们来看一下如何通过假设文档来执行我们的Q&A机器人对LangChain YouTube视频的搜索。

## 设置
#### 安装依赖


```python
# %pip install -qU langchain langchain-openai
```

#### 设置环境变量

在这个例子中，我们将使用OpenAI：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 如果要使用LangSmith进行追踪，请取消注释以下行。在此注册：https://smith.langchain.com。
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 假设文档生成

最终生成一个相关的假设文档的关键在于试图回答用户的问题。由于我们正在为LangChain YouTube视频设计一个Q&A机器人，我们将提供一些关于LangChain的基本背景，并提示模型使用更严谨的风格，以便我们得到更真实的假设文档：


```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

system = """您是一位专家，掌握了一套用于构建基于LLM的应用程序的软件，该软件称为LangChain、LangGraph、LangServe和LangSmith。

LangChain是一个Python框架，提供了一系列可以轻松组合构建LLM应用程序的集成。
LangGraph是建立在LangChain之上的Python软件包，可以轻松构建具有状态的多参与者LLM应用程序。
LangServe是建立在LangChain之上的Python软件包，可以轻松将LangChain应用程序部署为REST API。
LangSmith是一个平台，可以轻松追踪和测试LLM应用程序。

尽力回答用户问题。回答时，撰写一篇针对用户问题的教程样式的文章。"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
qa_no_context = prompt | llm | StrOutputParser()
```


```python
answer = qa_no_context.invoke(
    {
        "question": "如何在链中使用多模态模型并将链转成REST API"
    }
)
print(answer)
```

    要在链中使用多模态模型并将链转换为REST API，您可以利用LangChain、LangGraph和LangServe的功能。接下来是一步一步的操作指南：
    
    1. **使用LangChain构建多模态模型**：
       - 首先，通过使用LangChain来定义您的多模态模型。LangChain提供了与TensorFlow、PyTorch和Hugging Face Transformers等各种深度学习框架的集成，使得可以将不同的模态（如文本、图像和音频）整合到一个链中。
       - 您可以为每个模态创建单独的组件，然后将它们组合在一起构建一个多模态模型。
    
    2. **使用LangGraph构建具有状态的多参与者应用程序**：
       - 一旦您在LangChain中定义了多模态模型，您可以使用LangGraph来构建一个具有状态的、多参与者的应用程序。
       - LangGraph可以定义相互作用并维护状态的参与者，这对于处理链中的多模态输入和输出非常有用。
    
    3. **使用LangServe将链部署为REST API**：
       - 在使用LangChain和LangGraph构建多模态模型和应用程序之后，您可以使用LangServe将链部署为REST API。
       - LangServe简化了将LangChain应用程序作为REST API公开的过程，使您可以通过HTTP请求轻松地与您的多模态模型进行交互。
    
    4. **使用LangSmith进行测试和追踪**：
       - 为了确保多模态模型和REST API的稳定性和性能，您可以使用LangSmith进行测试和追踪。
       - LangSmith提供了用于追踪LLM应用程序执行和运行测试以验证其功能的工具。
    
    通过遵循这些步骤并利用LangChain、LangGraph、LangServe和LangSmith的功能，您可以有效地在链中使用多模态模型并将链转换为REST API。
    

## 返回假设文档和原始问题

为了增加我们的召回率，我们可能希望基于假设文档和原始问题检索文档。我们可以很容易地同时返回两者，如下所示：


```python
from langchain_core.runnables import RunnablePassthrough

hyde_chain = RunnablePassthrough.assign(hypothetical_document=qa_no_context)

hyde_chain.invoke(
    {
        "question": "如何在链中使用多模态模型并将链转成REST API"
    }
)
```




    {'question': '如何在链中使用多模态模型并将链转成REST API',
     'hypothetical_document': "要在链中使用多模态模型并将链转换为REST API，您可以利用LangChain、LangGraph和LangServe的功能。接下来是一步一步的操作指南：\n\n1. **构建多模态模型**：首先，您需要创建或导入多模态模型。这些模型可以包括文本、图像、音频或任何其他您想在LLM应用程序中处理的数据类型。\n\n2. **构建LangGraph应用程序**：使用LangGraph构建一个具有状态的多参与者LLM应用程序，该应用程序可以处理链中的不同模态之间的交互。\n\n3. **在LangChain中集成您的模型**：LangChain为各种类型的模型和数据源提供了集成。您可以使用LangChain的功能轻松地将多模态模型集成到LangGraph应用程序中。\n\n4. **使用LangServe将您的LangChain应用程序部署为REST API**：构建好您的多模态LLM应用程序后，您可以使用LangServe将其部署为REST API。LangServe简化了将LangChain应用程序公开为Web服务的过程，使其可以被其他应用程序和用户访问。\n\n5. **使用LangSmith进行测试和追踪**：最后，您可以使用LangSmith来追踪和测试多模态LLM应用程序。LangSmith提供了用于监视应用程序性能、调试任何问题以及确保应用程序按预期功能的工具。\n\n通过遵循这些步骤并利用LangChain、LangGraph、LangServe和LangSmith的功能，您可以有效地在链中使用多模态模型并将链转换为REST API。"}



## 使用函数调用获得结构化输出

如果我们将这个技术与其他查询分析技术结合使用，我们可能会使用函数调用来获取结构化的查询对象。我们可以像下面这样使用函数调用来进行HyDE：


```python
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.pydantic_v1 import BaseModel, Field


class Query(BaseModel):
    answer: str = Field(
        ...,
        description="Answer the user question as best you can. Answer as though you were writing a tutorial that addressed the user question.",
    )


system = """您是一位专家，掌握了一套用于构建基于LLM的应用程序的软件，该软件称为LangChain、LangGraph、LangServe和LangSmith。

LangChain是一个Python框架，提供了一系列可以轻松组合构建LLM应用程序的集成。
LangGraph是建立在LangChain之上的Python软件包，可以轻松构建具有状态的多参与者LLM应用程序。
LangServe是建立在LangChain之上的Python软件包，可以轻松将LangChain应用程序部署为REST API。
LangSmith是一个平台，可以轻松追踪和测试LLM应用程序。"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
llm_with_tools = llm.bind_tools([Query])
hyde_chain = prompt | llm_with_tools | PydanticToolsParser(tools=[Query])
hyde_chain.invoke(
    {
        "question": "如何在链中使用多模态模型并将链转成REST API"
    }
)
```




    [Query(answer='要在链中使用多模态模型并将链转换为REST API，您可以按照以下步骤操作：\n\n1. 使用LangChain构建多模态模型，通过整合文本、图像和音频等不同模态的方式来定义您的多模态模型。\n2. 使用建立在LangChain之上的Python软件包LangGraph，创建一个具有状态的多参与者LLM应用程序，该应用程序可以处理链中不同模态之间的交互。\n3. 构建好使用LangChain和LangGraph定义的多模态模型后，使用LangServe这个Python软件包将其作为REST API进行部署，从而实现将链转换为REST API的功能。\n4. 使用LangSmith进行测试和追踪，以确保多模态模型的功能和性能。\n\n按照这些步骤，并利用LangChain、LangGraph、LangServe和LangSmith的功能，您可以有效地在链中使用多模态模型，并将链转换为REST API。')]





