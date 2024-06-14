# 结构化

将文本输入转化为正确的搜索和过滤参数是检索中最重要的步骤之一。从非结构化输入中提取结构化参数的过程被称为**查询结构化**。

为了说明这一点，让我们回到我们的示例，即在LangChain YouTube视频上建立一个问答机器人的例子，来看看在这种情况下更复杂的结构化查询可能是什么样子的。

## 设置
#### 安装依赖项


```python
# %pip install -qU langchain langchain-openai youtube-transcript-api pytube
```

#### 设置环境变量

在本示例中，我们将使用OpenAI:


```python
import getpass
import os

# os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 可选，取消注释以使用LangSmith跟踪运行。在这里注册: https://smith.langchain.com。
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

### 加载示例文档

让我们加载一个代表性的文档


```python
from langchain_community.document_loaders import YoutubeLoader

docs = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=pbAd8O1Lvm4", add_video_info=True
).load()
```

这是与视频相关的元数据:


```python
docs[0].metadata
```




    {'source': 'pbAd8O1Lvm4',
     'title': 'Self-reflective RAG with LangGraph: Self-RAG and CRAG',
     'description': 'Unknown',
     'view_count': 9006,
     'thumbnail_url': 'https://i.ytimg.com/vi/pbAd8O1Lvm4/hq720.jpg',
     'publish_date': '2024-02-07 00:00:00',
     'length': 1058,
     'author': 'LangChain'}



这是文档内容的一部分示例:


```python
docs[0].page_content[:500]
```




    "hi this is Lance from Lang chain I'm going to be talking about using Lang graph to build a diverse and sophisticated rag flows so just to set the stage the basic rag flow you can see here starts with a question retrieval of relevant documents from an index which are passed into the context window of an llm for generation of an answer grounded in the ret documents so that's kind of the basic outline and we can see it's like a very linear path um in practice though you often encounter a few differ"



## 查询模式

为了生成结构化查询，我们首先需要定义我们的查询模式。我们可以看到每个文档都有一个标题、浏览次数、发布日期和长度（以秒为单位）。让我们假设我们建立了一个索引，允许我们对每个文档的内容和标题进行非结构化搜索，并对浏览次数、发布日期和长度进行范围过滤。

首先，我们将创建一个带有浏览次数、发布日期和视频长度的明确的最小和最大属性的模式，以便可以进行筛选。我们将根据内容和视频标题对搜索进行分别处理。

我们也可以创建一个更通用的模式，其中对于每个可过滤字段，我们不是为每个字段创建一个或多个过滤属性，而是创建一个单独的`filters`属性，该属性接受一个（属性、条件、值）元组的列表。我们也会演示如何做到这一点。哪种方法最好取决于索引的复杂性。如果您有许多可过滤字段，那么最好使用单一的`filters`查询属性。如果您只有几个可过滤的字段和/或有一些字段只能以非常特定的方式进行过滤，则为每个字段分别创建查询属性，每个属性都有自己的描述，可能会有所帮助。


```python
import datetime
from typing import Literal, Optional, Tuple

from langchain_core.pydantic_v1 import BaseModel, Field


class TutorialSearch(BaseModel):
    """Search over a database of tutorial videos about a software library."""

    content_search: str = Field(
        ...,
        description="Similarity search query applied to video transcripts.",
    )
    title_search: str = Field(
        ...,
        description=(
            "Alternate version of the content search query to apply to video titles. "
            "Should be succinct and only include key words that could be in a video "
            "title."
        ),
    )
    min_view_count: Optional[int] = Field(
        None,
        description="Minimum view count filter, inclusive. Only use if explicitly specified.",
    )
    max_view_count: Optional[int] = Field(
        None,
        description="Maximum view count filter, exclusive. Only use if explicitly specified.",
    )
    earliest_publish_date: Optional[datetime.date] = Field(
        None,
        description="Earliest publish date filter, inclusive. Only use if explicitly specified.",
    )
    latest_publish_date: Optional[datetime.date] = Field(
        None,
        description="Latest publish date filter, exclusive. Only use if explicitly specified.",
    )
    min_length_sec: Optional[int] = Field(
        None,
        description="Minimum video length in seconds, inclusive. Only use if explicitly specified.",
    )
    max_length_sec: Optional[int] = Field(
        None,
        description="Maximum video length in seconds, exclusive. Only use if explicitly specified.",
    )

    def pretty_print(self) -> None:
        for field in self.__fields__:
            if getattr(self, field) is not None and getattr(self, field) != getattr(
                self.__fields__[field], "default", None
            ):
                print(f"{field}: {getattr(self, field)}")
```

## 查询生成

为了将用户问题转换为结构化查询，我们将使用一个函数调用模型，比如ChatOpenAI。LangChain有一些很好的构造函数，可以通过一个Pydantic类轻松地指定所需的函数调用模式:


```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

system = """You are an expert at converting user questions into database queries. \
You have access to a database of tutorial videos about a software library for building LLM-powered applications. \
Given a question, return a database query optimized to retrieve the most relevant results.

If there are acronyms or words you are not familiar with, do not try to rephrase them."""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
structured_llm = llm.with_structured_output(TutorialSearch)
query_analyzer = prompt | structured_llm
```

让我们试一下:


```python
query_analyzer.invoke({"question": "rag from scratch"}).pretty_print()
```

    content_search: rag from scratch
    title_search: rag from scratch
    


```python
query_analyzer.invoke(
    {"question": "videos on chat langchain published in 2023"}
).pretty_print()
```

    content_search: chat langchain
    title_search: chat langchain
    earliest_publish_date: 2023-01-01
    latest_publish_date: 2024-01-01
    


```python
query_analyzer.invoke(
    {
        "question": "how to use multi-modal models in an agent, only videos under 5 minutes"
    }
).pretty_print()
```

    content_search: multi-modal models agent
    title_search: multi-modal models agent
    max_length_sec: 300
    
------



## 替代方案：简明模式

如果我们有许多可过滤字段，那么具有冗长模式的架构可能会影响性能，或者由于函数架构的大小限制可能根本不可能。在这种情况下，我们可以尝试更简洁的查询模式，以换取一些明确指示的简洁性：

```python
from typing import List, Literal, Union

class Filter(BaseModel):
    field: Literal["view_count", "publish_date", "length_sec"]
    comparison: Literal["eq", "lt", "lte", "gt", "gte"]
    value: Union[int, datetime.date] = Field(..., description="如果字段是publish_date，则值必须是ISO-8601格式的日期")

class TutorialSearch(BaseModel):
    """对软件库的教程视频进行搜索。"""
    content_search: str = Field(..., description="应用于视频转录的相似性搜索查询。")
    title_search: str = Field(..., description="应用于视频标题的替代版本的相似性搜索查询。应简洁并仅包括可能出现在视频标题中的关键词。")
    filters: List[Filter] = Field(default_factory=list, description="对特定字段的过滤器。最终条件是所有过滤器的逻辑合取。")

    def pretty_print(self) -> None:
        for field in self.__fields__:
            if getattr(self, field) is not None and getattr(self, field) != getattr(self.__fields__[field], "default", None):
                print(f"{field}: {getattr(self, field)}")
```

```python
structured_llm = llm.with_structured_output(TutorialSearch)
query_analyzer = prompt | structured_llm
```

让我们试试看：

```python
query_analyzer.invoke({"question": "从头开始学习拉格"}).pretty_print()
```
输出结果:
```
content_search: 从头开始学习拉格
title_search: 从头开始学习拉格
filters: []
```

```python
query_analyzer.invoke(
    {"question": "在2023年发布的有关Chat LangChain的视频"}
).pretty_print()
```
输出结果:
```
content_search: Chat LangChain
title_search: Chat LangChain
filters: [Filter(field='publish_date', comparison='eq', value=datetime.date(2023, 1, 1))]
```

```python
query_analyzer.invoke(
    {
        "question": "如何在一个代理商中使用多模态模型，只列出不到5分钟且观看超过276次的视频"
    }
).pretty_print()
```
输出结果:
```
content_search: 在一个代理商中使用多模态模型
title_search: 在一个代理商中使用多模态模型
filters: [Filter(field='length_sec', comparison='lt', value=300), Filter(field='view_count', comparison='gte', value=276)]
```

我们可以看到分析器很好地处理整数，但在处理日期范围时遇到了困难。我们可以尝试调整模式描述和/或提示以纠正此问题：

```python
class TutorialSearch(BaseModel):
    """对软件库的教程视频进行搜索。"""

    content_search: str = Field(..., description="应用于视频转录的相似性搜索查询。")
    title_search: str = Field(
        ...,
        description=(
            "应用于视频标题的替代版本的相似性搜索查询。应简洁并仅包括可能出现在视频标题中的关键词。"
        ),
    )
    filters: List[Filter] = Field(
        default_factory=list,
        description=(
            "对特定字段的过滤器。最终条件是所有过滤器的逻辑合取。"
            "如果指定了长于一天的时间段，则必须产生定义日期范围的过滤器。"
            f"请记住当前日期是{datetime.date.today().strftime('%m-%d-%Y')}。"
        ),
    )

    def pretty_print(self) -> None:
        for field in self.__fields__:
            if getattr(self, field) is not None and getattr(self, field) != getattr(
                    self.__fields__[field], "default", None
            ):
                print(f"{field}: {getattr(self, field)}")

structured_llm = llm.with_structured_output(TutorialSearch)
query_analyzer = prompt | structured_llm
```

```python
query_analyzer.invoke(
    {"question": "在2023年发布的有关Chat LangChain的视频"}
).pretty_print()
```

输出结果：
```
content_search: Chat LangChain
title_search: Chat LangChain
filters: [Filter(field='publish_date', comparison='gte', value=datetime.date(2023, 1, 1)), Filter(field='publish_date', comparison='lte', value=datetime.date(2023, 12, 31))]
```

看起来这个方案可行！

## 排序：超越搜索

在某些索引中，按字段进行搜索不是检索结果的唯一方法-我们还可以通过字段对文档进行排序，并检索排名靠前的结果。通过结构化查询，可以通过添加单独的查询字段来指定如何对结果进行排序。

```python
class TutorialSearch(BaseModel):
    """对软件库的教程视频进行搜索。"""

    content_search: str = Field("", description="应用于视频转录的相似性搜索查询。")
    title_search: str = Field(
        "",
        description=(
            "应用于视频标题的替代版本的相似性搜索查询。应简洁并仅包括可能出现在视频标题中的关键词。"
        ),
    )
    min_view_count: Optional[int] = Field(
        None, description="最低观看次数过滤器，包含边界值。"
    )
    max_view_count: Optional[int] = Field(
        None, description="最高观看次数过滤器，不包含边界值。"
    )
    earliest_publish_date: Optional[datetime.date] = Field(
        None, description="最早发布日期的过滤器，包含边界值。"
    )
    latest_publish_date: Optional[datetime.date] = Field(
        None, description="最近发布日期的过滤器，不包含边界值。"
    )
    min_length_sec: Optional[int] = Field(
        None, description="最短视频长度（以秒为单位），包含边界值。"
    )
    max_length_sec: Optional[int] = Field(
        None, description="最长视频长度（以秒为单位），不包含边界值。"
    )
    sort_by: Literal[
        "relevance",
        "view_count",
        "publish_date",
        "length",
    ] = Field("relevance", description="排序依据属性。")
    sort_order: Literal["ascending", "descending"] = Field(
        "descending", description="排序的升序或降序。"
    )

    def pretty_print(self) -> None:
        for field in self.__fields__:
            if getattr(self, field) is not None and getattr(self, field) != getattr(
                    self.__fields__[field], "default", None
            ):
                print(f"{field}: {getattr(self, field)}")
```

```
structured_llm = llm.with_structured_output(TutorialSearch)
query_analyzer = prompt | structured_llm
```


```python
query_analyzer.invoke(
    {"question": "What has LangChain released lately?"}
).pretty_print()
```

    title_search: LangChain
    sort_by: publish_date
    


```python
query_analyzer.invoke({"question": "What are the longest videos?"}).pretty_print()
```

    sort_by: length
    

我们甚至可以支持搜索和排序的结合使用。这可能看起来像是首先检索所有高于相关性阈值的结果，然后根据指定的属性对它们进行排序：


```python
query_analyzer.invoke(
    {"question": "What are the shortest videos about agents?"}
).pretty_print()
```

    content_search: agents
    sort_by: length
    sort_order: ascending
    
