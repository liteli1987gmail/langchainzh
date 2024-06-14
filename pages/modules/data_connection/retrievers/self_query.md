# 自查询

:::

转到[Integrations](/docs/integrations/retrievers/self_query)，查看具有内置自查询支持的向量存储的文档。

:::

自查询检索机制是指具有查询自身能力的检索机制。具体而言，给定任何自然语言查询，检索器使用查询构造LLM链来编写结构化查询，然后将该结构化查询应用于其基础的VectorStore。这使得检索器不仅可以使用用户输入的查询与存储文档内容进行语义相似性比较，还可以从用户查询中提取存储文档的元数据上的过滤器，并执行这些过滤器。

![](/img/self_querying.jpg)

## 开始

为了演示目的，我们将使用`Chroma`向量存储。我们创建了一组包含电影摘要的小演示文档。

**注意:** 自查询检索器需要您安装`lark`包。


```python
%pip install --upgrade --quiet lark chromadb
```


```python
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

docs = [
    Document(
        page_content="一群科学家带回了恐龙，然后一团混乱爆发了",
        metadata={"year": 1993, "rating": 7.7, "genre": "科幻"},
    ),
    Document(
        page_content="莱昂纳多·迪卡普里奥在梦中迷失，一层层梦境中的梦境中......",
        metadata={"year": 2010, "director": "克里斯托弗·诺兰", "rating": 8.2},
    ),
    Document(
        page_content="一名心理学家/侦探陷入了一系列梦中的梦中的梦中，而《盗梦空间》重复了这一想法",
        metadata={"year": 2006, "director": "今敏", "rating": 8.6},
    ),
    Document(
        page_content="一群身材正常的女性非常健康，有些男性向她们追求",
        metadata={"year": 2019, "director": "格蕾塔·葛韦格", "rating": 8.3},
    ),
    Document(
        page_content="玩具活了起来，在此过程中尽情玩耍",
        metadata={"year": 1995, "genre": "动画"},
    ),
    Document(
        page_content="三名男子走进区域，三名男子走出区域",
        metadata={
            "year": 1979,
            "director": "安德烈·塔可夫斯基",
            "genre": "惊悚",
            "rating": 9.9,
        },
    ),
]
vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())
```

### 创建我们的自查询检索器

现在我们可以实例化我们的检索器。为此，我们需要提前提供关于文档支持的元数据字段和文档内容的简短描述。


```python
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_openai import ChatOpenAI

metadata_field_info = [
    AttributeInfo(
        name="genre",
        description="电影的类型。其中之一['科幻', '喜剧', '戏剧', '惊悚', '爱情', '动作', '动画']",
        type="string",
    ),
    AttributeInfo(
        name="year",
        description="电影上映年份",
        type="integer",
    ),
    AttributeInfo(
        name="director",
        description="电影导演的姓名",
        type="string",
    ),
    AttributeInfo(
        name="rating", description="电影的评分（1-10）", type="float"
    ),
]
document_content_description = "电影简介"
llm = ChatOpenAI(temperature=0)
retriever = SelfQueryRetriever.from_llm(
    llm,
    vectorstore,
    document_content_description,
    metadata_field_info,
)
```

### 测试

现在我们可以尝试使用我们的检索器了！


```python
# 此示例仅指定了一个过滤器
retriever.invoke("我想看一部评分高于8.5的电影")
```




    [Document(page_content='三名男子走进区域，三名男子走出区域', metadata={'director': '安德烈·塔可夫斯基', 'genre': '惊悚', 'rating': 9.9, 'year': 1979}),
     Document(page_content='一名心理学家/侦探陷入了一系列梦中的梦中的梦中，而《盗梦空间》重复了这一想法', metadata={'director': '今敏', 'rating': 8.6, 'year': 2006})]




```python
# 此示例指定查询和过滤器
retriever.invoke("格蕾塔·葛韦格导演过关于女性的任何电影吗")
```




    [Document(page_content='一群身材正常的女性非常健康，有些男性向她们追求', metadata={'director': '格蕾塔·葛韦格', 'rating': 8.3, 'year': 2019})]




```python
# 此示例指定复合过滤器
retriever.invoke("评分高于8.5的科幻电影是什么")
```




    [Document(page_content='一名心理学家/侦探陷入了一系列梦中的梦中的梦中，而《盗梦空间》重复了这一想法', metadata={'director': '今敏', 'rating': 8.6, 'year': 2006}),
     Document(page_content='三名男子走进区域，三名男子走出区域', metadata={'director': '安德烈·塔可夫斯基', 'genre': '惊悚', 'rating': 9.9, 'year': 1979})]




```python
# 此示例指定查询和复合过滤器
retriever.invoke(
    "1990年后但2005年前的电影中关于玩具的有哪些，最好是动画的"
)
```




    [Document(page_content='玩具活了起来，在此过程中尽情玩耍', metadata={'genre': '动画', 'year': 1995})]



### 过滤器 k

我们还可以使用自查询检索器指定`k`：要获取的文档数。

可以通过将`enable_limit=True`传递给构造函数实现此目的。


```python
retriever = SelfQueryRetriever.from_llm(
    llm,
    vectorstore,
    document_content_description,
    metadata_field_info,
    enable_limit=True,
)

# 此示例仅指定了一个相关查询
retriever.invoke("有哪两部关于恐龙的电影")
```




    [Document(page_content='一群科学家带回了恐龙，然后一团混乱爆发了', metadata={'genre': '科幻', 'rating': 7.7, 'year': 1993}),
     Document(page_content='玩具活了起来，在此过程中尽情玩耍', metadata={'genre': '动画', 'year': 1995})]



## 使用LCEL从头开始构建

要了解内部工作原理，并具有更多自定义控制，我们可以从头开始重建我们的检索器。

首先，我们需要创建一个查询构造链。此链将接受用户查询并生成一个捕获用户指定的过滤器的`StructuredQuery`对象。我们提供了一些辅助函数用于创建提示和输出解析器。这些函数有许多可调参数，我们将在这里简单忽略。


```python
from langchain.chains.query_constructor.base import (
    StructuredQueryOutputParser,
    StructuredQueryPrompt,
)
``````python
    prompt = get_query_constructor_prompt(
    document_content_description_,
    metadata_field_info_,
)
output_parser = StructuredQueryOutputParser.from_components()
query_constructor = prompt | llm | output_parser
```

让我们看看我们的提示语:


```python
print(prompt.format(query="dummy question"))
```

你的目标是将用户的查询结构化，以匹配下面提供的请求模式。

<< 结构化请求模式 >>
在回应时，使用一个 markdown 代码片段，其中包含一个 JSON 对象，格式如下：

```json
{
    "query": string \ 要与文档内容匹配的文本字符串
    "filter": string \ 用于筛选文档的逻辑条件语句
}
```

查询字符串应该只包含预期与文档内容匹配的文本。任何 filter 中的条件也不应出现在查询中。

逻辑条件语句由一个或多个比较和逻辑操作语句组成。

比较语句采用以下形式：`comp(attr, val)`：
- `comp` (eq | ne | gt | gte | lt | lte | contain | like | in | nin)：比较器
- `attr` (字符串)：要应用比较的属性名称
- `val` (字符串)：比较值

逻辑操作语句采用形式 `op(statement1, statement2, ...)`：
- `op` (and | or | not)：逻辑运算符
- `statement1`、`statement2` 等 (比较语句或逻辑操作语句)：要应用操作的一个或多个语句

确保只使用上面列出的比较器和逻辑运算符，不要使用其他的。
确保筛选器只引用数据源中存在的属性。
确保筛选器只使用带有其函数名称的属性名称（如果对它们应用了函数）。
确保只在处理日期数据类型值时使用格式 `YYYY-MM-DD`。
确保筛选器考虑到属性的描述，并且只进行可能的数据类型比较。
确保只在需要时使用筛选器。如果没有需要应用的筛选器，则返回筛选值为 "NO_FILTER"。

<< 示例 1. >>
数据源:
```json
{
    "content": "歌曲歌词",
    "attributes": {
        "artist": {
            "type": "string",
            "description": "歌曲艺术家的名字"
        },
        "length": {
            "type": "integer",
            "description": "歌曲长度（秒）"
        },
        "genre": {
            "type": "string",
            "description": "歌曲流派，其中之一为 “流行”，“摇滚” 或 “说唱”"
        }
    }
}
```

用户查询:
Taylor Swift 或 Katy Perry 演唱的有关少年漂亮的歌曲中长度不超过3分钟，并且流派是舞蹈流行的有哪些？

结构化请求:
```json
{
    "query": "teenager love",
    "filter": "and(or(eq(\"artist\", \"Taylor Swift\"), eq(\"artist\", \"Katy Perry\")), lt(\"length\", 180), eq(\"genre\", \"pop\"))"
}
```

<< 示例 2. >>
数据源:
```json
{
    "content": "歌曲歌词",
    "attributes": {
        "artist": {
            "type": "string",
            "description": "歌曲艺术家的名字"
        },
        "length": {
            "type": "integer",
            "description": "歌曲长度（秒）"
        },
        "genre": {
            "type": "string",
            "description": "歌曲流派，其中之一为 “流行”，“摇滚” 或 “说唱”"
        }
    }
}
```

用户查询:
没有在 Spotify 上发布的歌曲有哪些？

结构化请求:
```json
{
    "query": "",
    "filter": "NO_FILTER"
}
```

<< 示例 3. >>
数据源:
```json
{
    "content": "电影简介",
    "attributes": {
        "genre": {
            "description": "电影的流派。 ['科幻', '喜剧', '戏剧', '惊悚', '浪漫', '动作', '动画'] 中的一种",
            "type": "string"
        },
        "year": {
            "description": "电影发行的年份",
            "type": "integer"
        },
        "director": {
            "description": "电影导演的名字",
            "type": "string"
        },
        "rating": {
            "description": "电影的 1-10 评分",
            "type": "float"
        }
    }
}
```

用户查询:
dummy question

结构化请求:
```

和我们的完整查询结果:


```python
query_constructor.invoke(
    {
        "query": "What are some sci-fi movies from the 90's directed by Luc Besson about taxi drivers"
    }
)
```


查询构造器是自查询检索器的关键要素。要创建一个优秀的检索系统，您需要确保您的查询构造器运行良好。通常需要调整提示、提示中的示例、属性描述等。有一个例子可以指导您如何在一些酒店库存数据上完善查询构造器，在[这个 Cookbook 中查看](https://github.com/langchain-ai/langchain/blob/master/cookbook/self_query_hotel_search.ipynb)。

下一个关键要素是结构化查询转换器。这个对象负责将通用的 `StructuredQuery` 对象转换为您使用的向量存储语法中的元数据过滤器。LangChain 提供了许多内置的转换器。要查看所有转换器，请转到[集成部分](/docs/integrations/retrievers/self_query)。


```python
from langchain.retrievers.self_query.chroma import ChromaTranslator

retriever = SelfQueryRetriever(
    query_constructor=query_constructor,
    vectorstore=vectorstore,
    structured_query_translator=ChromaTranslator(),
)
```


```python
retriever.invoke(
    "What's a movie after 1990 but before 2005 that's all about toys, and preferably is animated"
)
```

```python
[Document(page_content='Toys come alive and have a blast doing so', metadata={'genre': 'animated', 'year': 1995})]
```