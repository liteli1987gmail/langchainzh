# MultiQueryRetriever

基于距离的向量数据库检索嵌入（表示）查询在高维空间中，并根据“距离”找到相似的嵌入文档。但是，如果查询措辞微妙变化或嵌入不很好地捕捉到数据的语义，检索可能会产生不同的结果。有时候会手动进行提示工程/调优来解决这些问题，但这可能很繁琐。

`MultiQueryRetriever`通过使用LLM自动生成多个具有不同观点的查询来自动化提示调优过程，以满足给定用户输入查询的需求。对于每个查询，它检索一组相关文档，并对所有查询进行唯一并集，从而获得一组更大的可能相关文档。通过在同一个问题上生成多个不同观点，`MultiQueryRetriever`可能能够克服基于距离的检索的一些限制，并获得更丰富的结果集。


```python
# 构建样本向量DB
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 加载博文
loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
data = loader.load()

# 拆分
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splits = text_splitter.split_documents(data)

# 向量DB
embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=splits, embedding=embedding)
```

#### 简单用法

指定要用于查询生成的LLM，其余的由检索器处理。


```python
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI

question = "任务分解的方法有哪些?"
llm = ChatOpenAI(temperature=0)
retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=vectordb.as_retriever(), llm=llm
)
```


```python
# 设置查询日志记录
import logging

logging.basicConfig()
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)
```


```python
unique_docs = retriever_from_llm.get_relevant_documents(query=question)
len(unique_docs)
```

    INFO:langchain.retrievers.multi_query:生成的查询: ['1. 怎么处理任务分解?', '2. 任务分解有哪些不同的方法?', '3. 任务分解有哪些不同的途径?']
    




    5



#### 提供自定义提示

您还可以提供提示以及一个输出解析器，将结果拆分为查询列表。


```python
from typing import List

from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field


# 输出解析器将LLM结果拆分为查询列表
class LineList(BaseModel):
    # "lines" 是解析输出的键（属性名）
    lines: List[str] = Field(description="文本行")


class LineListOutputParser(PydanticOutputParser):
    def __init__(self) -> None:
        super().__init__(pydantic_object=LineList)

    def parse(self, text: str) -> LineList:
        lines = text.strip().split("\n")
        return LineList(lines=lines)


output_parser = LineListOutputParser()

QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""您是一个AI语言模型助手。您的任务是根据给定的用户问题生成五个不同版本的查询，以从向量数据库中检索相关文档。通过在用户问题上生成多个观点，您的目标是帮助用户克服基于距离的相似性搜索的某些限制。请以新行分隔的方式提供这些替代问题。
原始问题: {question}""",
)
llm = ChatOpenAI(temperature=0)

# 链
llm_chain = LLMChain(llm=llm, prompt=QUERY_PROMPT, output_parser=output_parser)

# 其他输入
question = "任务分解的方法有哪些?"
```


```python
# 运行
retriever = MultiQueryRetriever(
    retriever=vectordb.as_retriever(), llm_chain=llm_chain, parser_key="lines"
)  # "lines" 是解析输出的键（属性名）

# 结果
unique_docs = retriever.get_relevant_documents(
    query="课程中对回归有什么涵盖?"
)
len(unique_docs)
```

    INFO:langchain.retrievers.multi_query:生成的查询: ["1. 课程对回归有什么观点?", '2. 您能提供课程中关于回归的信息吗?', '3. 课程如何涵盖回归主题?', "4. 课程对回归的教授是怎样的?", '5. 关于课程，有提到回归吗?']
    




    11

