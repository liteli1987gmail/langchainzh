# 处理高基数分类变量

您可能希望进行查询分析以创建对分类列进行过滤的筛选器。其中一个困难在于您通常需要指定确切的分类值。问题在于您需要确保LLM准确生成该分类值。当只有少数有效值时，这可以相对容易地完成。当有大量有效值时，情况就变得更加困难，因为这些值可能不适合LLM上下文，或者（如果适合）可能太多以至于LLM无法正确处理。

在这个笔记本中，我们来看一下如何解决这个问题。

## 设置
#### 安装依赖包


```python
# %pip install -qU langchain langchain-community langchain-openai faker
```

#### 设置环境变量

我们将在此示例中使用OpenAI：


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 可选的，取消注释以通过LangSmith跟踪运行。 在此处注册：https://smith.langchain.com。
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

#### 设置数据

我们将生成一系列虚假姓名


```python
from faker import Faker

fake = Faker()

names = [fake.name() for _ in range(10000)]
```

让我们看一些姓名


```python
names[0]
```




    'Hayley Gonzalez'




```python
names[567]
```




    'Jesse Knight'



## 查询分析

现在，我们可以设置基准查询分析


```python
from langchain_core.pydantic_v1 import BaseModel, Field
```


```python
class Search(BaseModel):
    query: str
    author: str
```


```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

system = """为图书馆系统生成相关的搜索查询"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
structured_llm = llm.with_structured_output(Search)
query_analyzer = {"question": RunnablePassthrough()} | prompt | structured_llm
```

/Users/harrisonchase/workplace/langchain/libs/core/langchain_core/_api/beta_decorator.py:86: LangChainBetaWarning: The function `with_structured_output` is in beta. It is actively being worked on, so the API may change.
  warn_beta(
    

我们可以看到，如果拼写姓名完全正确，它知道如何处理


```python
query_analyzer.invoke("Jesse Knight的外星人图书")
```




    Search(query='外星人图书', author='Jesse Knight')



问题在于您要筛选的值可能不是拼写完全正确的


```python
query_analyzer.invoke("jess knight的外星人图书")
```




    Search(query='外星人图书', author='Jess Knight')



### 添加所有值

解决此问题的一种方法是将所有可能的值添加到提示中。这通常会引导查询朝着正确的方向发展


```python
system = """为图书馆系统生成相关的搜索查询。

`作者`属性必须是以下之一：

{authors}

不要误写作者姓名!"""
base_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
prompt = base_prompt.partial(authors=", ".join(names))
```


```python
query_analyzer_all = {"question": RunnablePassthrough()} | prompt | structured_llm
```

然而...如果分类变量的列表足够长，它可能会报错！


```python
try:
    res = query_analyzer_all.invoke("jess knight的外星人图书")
except Exception as e:
    print(e)
```

错误代码：400 - {'error'：{'message'：'此模型的最大上下文长度为16385个标记。但是，您的消息导致生成了33885个标记（消息中有33855个标记，函数中有30个标记）。请减少消息或函数的长度。'，'type'：'invalid_request_error'，'param'：'messages'，'code'：'context_length_exceeded'}}
    

我们可以尝试使用更长的上下文窗口...但是由于信息太多，不保证可靠地捕捉到它们


```python
llm_long = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)
structured_llm_long = llm_long.with_structured_output(Search)
query_analyzer_all = {"question": RunnablePassthrough()} | prompt | structured_llm_long
```


```python
query_analyzer_all.invoke("jess knight的外星人图书")
```




    Search(query='aliens', author='Kevin Knight')



### 查找并选择相关的值

相反，我们可以创建一个索引，该索引包含相关值，然后查询前N个最相关值，


```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma.from_texts(names, embeddings, collection_name="author_names")
```


```python
def select_names(question):
    _docs = vectorstore.similarity_search(question, k=10)
    _names = [d.page_content for d in _docs]
    return ", ".join(_names)
```


```python
create_prompt = {
    "question": RunnablePassthrough(),
    "authors": select_names,
} | base_prompt
```


```python
query_analyzer_select = create_prompt | structured_llm
```


```python
create_prompt.invoke("jess knight的图书是什么")
```




    ChatPromptValue(messages=[SystemMessage(content='为图书馆系统生成相关的搜索查询。\n\n`作者`属性必须是以下之一：\n\nJesse Knight, Kelly Knight, Scott Knight, Richard Knight, Andrew Knight, Katherine Knight, Erica Knight, Ashley Knight, Becky Knight, Kevin Knight\n\n不要误写作者姓名!'), HumanMessage(content='jess knight的图书是什么')])




```python
query_analyzer_select.invoke("jess knight的外星人图书")
```




    Search(query='外星人图书', author='Jesse Knight')





### 替换选择之后

另一种方法是让LLM填写任何值，然后将该值转换为有效值。
实际上，这可以通过Pydantic类本身来实现！


```python
from langchain_core.pydantic_v1 import validator


class 搜索(BaseModel):
    查询: str
    作者: str

    @validator("作者")
    def double(cls, v: str) -> str:
        return vectorstore.similarity_search(v, k=1)[0].page_content
```


```python
系统 = """为图书馆系统生成相关的搜索查询"""
提示 = ChatPromptTemplate.from_messages(
    [
        ("system", 系统),
        ("human", "{问题}"),
    ]
)
纠错结构_llm = llm.with_structured_output(搜索)
纠错查询分析器 = (
    {"问题": RunnablePassthrough()} | 提示 | 纠错结构_llm
)
```


```python
纠错查询分析器.invoke("关于外星人的书籍由Jesse Knight写的有哪些")
```




    搜索(查询='关于外星人的书籍', 作者='Jesse Knight')




```python
# TODO: 显示三元组相似性

```
------
