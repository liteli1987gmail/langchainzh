# 长上下文重排序

无论您的模型架构是什么，当您包括10个以上的检索文档时，性能都会大幅下降。
简而言之：当模型必须在长上下文中间访问相关信息时，它们往往会忽略提供的文档。
参见：https://arxiv.org/abs/230903172

为了避免这个问题，您可以在检索后重新排序文档以避免性能下降。

```python
%pip install --upgrade --quiet  sentence-transformers > /dev/null
```

```python
from langchain.chains import LLMChain, StuffDocumentsChain
from langchain.prompts import PromptTemplate
from langchain_community.document_transformers import (
    长上下文重排序,
)
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI

# 获取嵌入。
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

texts = [
    "篮球是一项伟大的运动。",
    "带我去月球是我最喜欢的歌曲之一。",
    "凯尔特人队是我最喜欢的球队。",
    "这是一份关于波士顿凯尔特人的文件",
    "我就是喜欢去看电影",
    "波士顿凯尔特人队以20分的优势赢得了比赛",
    "这只是一个随机文本。",
    "埃尔登之环是过去15年中最好的游戏之一。",
    "L·科内特是最好的凯尔特人队球员之一。",
    "拉里·伯德是一名标志性的NBA球员。",
]

# 创建一个检索器
retriever = Chroma.from_texts(texts, embedding=embeddings).as_retriever(
    search_kwargs={"k": 10}
)
query = "你能告诉我关于凯尔特人的信息吗？"

# 获取相关文档按相关性得分排序
docs = retriever.get_relevant_documents(query)
docs
```

```python
# 重新排序文档：
# 相对不相关的文档将位于列表中间，更相关的元素位于开头/结尾。
reordering = 长上下文重排序()
reordered_docs = reordering.transform_documents(docs)

# 确认4个相关文档位于列表的开头和结尾。
reordered_docs
```

```python
# 我们准备并运行一个使用重新排序文档作为上下文的自定义Stuff链。

# 重写提示
document_prompt = PromptTemplate(
    input_variables=["page_content"], template="{page_content}"
)
document_variable_name = "context"
llm = OpenAI()
stuff_prompt_override = """鉴于以下文本摘录：
-----
{context}
-----
请回答以下问题：
{query}"""
prompt = PromptTemplate(
    template=stuff_prompt_override, input_variables=["context", "query"]
)

# 实例化链
llm_chain = LLMChain(llm=llm, prompt=prompt)
chain = StuffDocumentsChain(
    llm_chain=llm_chain,
    document_prompt=document_prompt,
    document_variable_name=document_variable_name,
)
chain.run(input_documents=reordered_docs, query=query)

```
------
