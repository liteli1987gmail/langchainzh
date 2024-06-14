# 引文

如何让模型在其回答中引用其所引用的源文档的哪些部分？

为了探索一些提取引文的技术，让我们首先创建一个简单的 RAG 链。我们将使用 [WikipediaRetriever](https://api.python.langchain.com/en/latest/retrievers/langchain_community.retrievers.wikipedia.WikipediaRetriever.html)从维基百科中检索文章。

## 设置

首先，我们需要安装一些依赖项并设置我们将使用的模型的环境变量。


```python
%pip install -qU langchain langchain-openai langchain-anthropic langchain-community wikipedia
```


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()
os.environ["ANTHROPIC_API_KEY"] = getpass.getpass()

# 如果要记录到 LangSmith，请取消注释
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```


```python
from langchain_community.retrievers import WikipediaRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
wiki = WikipediaRetriever(top_k_results=6, doc_content_chars_max=2000)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个有用的 AI 助手。给定一个用户的问题和一些维基百科文章摘要，回答用户的问题。如果没有文章可以回答问题，就说你不知道。\n\n这些是维基百科文章:{context}",
        ),
        ("human", "{question}"),
    ]
)
prompt.pretty_print()
```

    ================================[1m 系统消息 [0m================================
    
    你是一个有用的 AI 助手。给定一个用户的问题和一些维基百科文章摘要，回答用户的问题。如果没有文章可以回答问题，就说你不知道。
    
    这些是维基百科文章:[33;1m[1;3m{context}[0m
    
    ================================[1m 用户消息 [0m=================================
    
    [33;1m[1;3m{question}[0m
    

现在，我们已经有了模型、检索器和提示，让我们将它们全部连在一起。我们需要添加一些逻辑来将我们检索到的文档格式化为一个可以传递给提示的字符串。我们将使链返回答案和检索到的文档。


```python
from operator import itemgetter
from typing import List

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)


def format_docs(docs: List[Document]) -> str:
    """将文档转换为一个字符串。"""
    formatted = [
        f"文章标题: {doc.metadata['title']}\n文章摘要: {doc.page_content}"
        for doc in docs
    ]
    return "\n\n" + "\n\n".join(formatted)


format = itemgetter("docs") | RunnableLambda(format_docs)
# 子链，用于生成答案一旦我们完成检索
answer = prompt | llm | StrOutputParser()
# 完整链，调用wiki -> 格式化文档为字符串 -> 运行答案子链 -> 仅返回答案和检索到的文档。
chain = (
    RunnableParallel(question=RunnablePassthrough(), docs=wiki)
    .assign(context=format)
    .assign(answer=answer)
    .pick(["answer", "docs"])
)
```


```python
chain.invoke("猎豹的速度有多快？")
```




    {'answer': '猎豹的奔跑速度可达到每小时 93 到 104 公里（58 到 65 英里）。',
     'docs': [Document(page_content='猎豹（Acinonyx jubatus）是一种大型猫科动物，也是最快的陆地动物。它的皮毛呈棕黄色或奶油色，或淡黄色，以均匀间隔的实心黑色斑点为特征。头部小而圆，有短而突出的口鼻部和黑色的泪状面纹。它的肩高为 67～94 厘米（26～37 英寸），头和身体的长度在 1.1～1.5 米（3 英尺 7 英寸至 4 英尺 11 英寸）之间。成年猎豹的体重在 21～72 公斤（46～159 磅）之间。猎豹能以每小时 93 到 104 公里（58 到 65 英里）的速度奔跑；它为奔跑而进化出了专门的适应性，包括较轻的身材、长而细腿和一条长尾巴。\n\n猎豹最早在 18 世纪末被描述。今天承认有分布在非洲和中伊朗的四个亚种。一种非洲亚种于 2022 年被引进到印度。如今，猎豹主要分布在非洲西北部、东部和南部以及中伊朗的小型、碎片化的种群中。它生活在非洲大草原、撒哈拉沙漠中干旱的山脉地区和丘陵沙漠地形等多种栖息地中。\n\n猎豹生活在三个主要的社会群体中：母猎豹和她们的幼崽、雄性“联盟”以及孤雄。雌性在大范围的家庭领域内寻找猎物，过着流浪的生活，而雄性则更加宅居，而是在有丰富的猎物和接触雌性的地方建立较小的领地。猎豹在白天活动，黎明和黄昏时达到高峰。它以小到中等身材的猎物为食，大多数重量在 40 公斤（88 磅）以下，偏爱中等体型的有蹄动物，如斑羚、跳羚和汤姆森氏瞪羚。猎豹在追击猎物之前通常在 60～100 米（200～330 英尺）范围内悄悄接近，然后朝着猎物冲刺，追逐过程中使它绊倒，并咬住它的咽喉使它窒息而死。猎豹全年都有繁殖。怀孕将近三个月后，雌性会生下三到四只幼崽。猎豹幼崽对其他大型食肉动物的捕食高度脆弱。它们断奶时约四个月大，约 20 个月大时就独立了。\n\n猎豹面临栖息地丧失、与人类的冲突、盗猎和易感疾病的威胁。2016 年，全球猎豹种群估计有 7,100 只野生猎豹；它被列为国际自然保护联盟（IUCN）红色名录上的易危物种。猎豹在艺术、文学、广告和动画中被广泛描绘。古埃及曾驯化它，并训练其狩猎印度和阿拉伯半岛上的有蹄动物。从 19 世纪初以来，它就在动物园里被养殖。\n\n', 'source': 'https://en.wikipedia.org/wiki/Cheetah'})]}=======

### 引用实际的文本片段

如果我们想引用实际的文本片段，该怎么办？我们也可以尝试让我们的模型返回这些内容。

*备注：请注意，如果我们将我们的文档分成许多只有一两句而不是几个长文档的文档，那么引用文档就变得等价于引用片段，并且可能对模型来说更容易，因为模型只需要为每个片段返回一个标识符而不是实际的文本。可能值得尝试两种方法并进行评估。*


```python
class Citation(BaseModel):
    source_id: int = Field(
        ...,
        description="证明答案正确的一个具体来源的整数ID。",
    )
    quote: str = Field(
        ...,
        description="从指定来源中证明答案的逐字引用。",
    )


class quoted_answer(BaseModel):
    """基于给定来源回答用户问题，并引用使用的来源。"""

    answer: str = Field(
        ...,
        description="回答用户问题，该回答仅基于给定的来源。",
    )
    citations: List[Citation] = Field(
        ..., description="证明答案的来源给出的引文。"
    )
```


```python
output_parser_2 = JsonOutputKeyToolsParser(
    key_name="quoted_answer", first_tool_only=True
)
llm_with_tool_2 = llm.bind_tools(
    [quoted_answer],
    tool_choice="quoted_answer",
)
format_2 = itemgetter("docs") | RunnableLambda(format_docs_with_id)
answer_2 = prompt | llm_with_tool_2 | output_parser_2
chain_2 = (
    RunnableParallel(question=RunnablePassthrough(), docs=wiki)
    .assign(context=format_2)
    .assign(quoted_answer=answer_2)
    .pick(["quoted_answer", "docs"])
)
```


```python
chain_2.invoke("How fast are cheetahs?")
```




    {'quoted_answer': {'answer': "猎豹的速度可以达到每小时93到104公里（58到65英里）。", 'citations': [{'source_id': 0, 'quote': '猎豹能够以93到104公里每小时（58到65英里）的速度奔跑；它已进化出了适应速度的特殊适应性，包括轻盈的体格、细长的腿部和长长的尾巴。'}]}, 'docs': [{'page_content': '猎豹（Acinonyx jubatus）是一种大型猫科动物，也是世界上最快的陆地动物。它的被毛呈黄褐色到乳白色或灰色，毛上有均匀分布的实心黑色斑点。它的头小而圆，吻部短，有黑色的泪痕状颜纹。它的肩高为67-94厘米（26-37英寸），头体长在1.1到1.5米（3英尺7英寸到4英尺11英寸）之间。成年猎豹的体重在21到72公斤（46到159磅）之间。猎豹能够以93到104公里每小时（58到65英里）的速度奔跑；它已进化出了适应速度的特殊适应性，包括轻盈的体格、细长的腿部和长长的尾巴。\n猎豹最初在18世纪后期被确诊为可能灭绝的物种。目前已确认有四个亚种是非洲和伊朗中部的本土。一种非洲亚种于2022年被引入到印度。目前，它主要分布在非洲西北部、东部和南部以及伊朗中部的小型、分散的种群中。它生活在包括塞伦盖蒂的大草原、撒哈拉的干旱山脉和丘陵沙漠地带在内的各种栖息地中。\n猎豹分为三个主要的群体：母豹和它们的幼崽，雄性的“联盟”，和独居的雄性。雌性豹在大范围内游牧，寻找丰富的猎物，而雄性则更喜欢定居并在得到丰富的猎物和与雌性交配的机会的地方建立更小的领地。猎豹在白天活动，黎明和黄昏时的活动高峰期。它以小到中型的猎物为食，大部分体重不超过40公斤（88磅），并且偏好中等体型的有蹄动物，如斑羚、跳羚和汤姆森氏瞪羚。猎豹通常在追击之前在60-100米（200-330英尺）内觅食，然后在追逐过程中绊倒猎物，并咬住它的喉咙使其窒息而亡。它在全年都会繁殖。雌性怀孕近三个月后，产下三到四只幼崽。猎豹幼崽极易遭到其他大型食肉动物的捕食。它们在大约四个月大时断奶，到约20个月大时独立。\n猎豹面临的威胁包括栖息地丧失、与人类的冲突、偷猎以及对疾病的高易感性。2016年，全球猎豹种群在野外估计约为7100只，被列为濒危物种。它已广泛被描绘在艺术、文学、广告和动画中。它在古埃及被驯化，并被用于在阿拉伯半岛和印度狩猎偶蹄类动物。早在19世纪初，它就在动物园里饲养。\n', 'source': 'https://en.wikipedia.org/wiki/Cheetah'}]}





## 直接提示支持函数调用

大多数模型还不支持函数调用。我们可以使用直接提示来实现类似的结果。让我们看看使用Anthropic聊天模型的直接提示是什么样子，该模型特别擅长使用XML：


```python
from langchain_anthropic import ChatAnthropicMessages

anthropic = ChatAnthropicMessages(model_name="claude-instant-1.2")
system = """您是一位乐于助人的AI助手。给定用户问题和一些维基百科文章片段，回答用户问题并提供引文。如果没有任何文章回答问题，只需回答您不知道。

请记住，您必须同时返回回答和引文。引文包括证明回答的逐字引用以及引文文章的ID。请使用以下格式返回您的最终输出：

<cited_answer>
    <answer></answer>
    <citations>
        <citation><source_id></source_id><quote></quote></citation>
        <citation><source_id></source_id><quote></quote></citation>
        ...
    </citations>
</cited_answer>

以下是维基百科文章的内容：{context}"""
prompt_3 = ChatPromptTemplate.from_messages(
    [("system", system), ("human", "{question}")]
)
```


```python
from langchain_core.output_parsers import XMLOutputParser


def format_docs_xml(docs: List[Document]) -> str:
    formatted = []
    for i, doc in enumerate(docs):
        doc_str = f"""\
    <source id=\"{i}\">
        <title>{doc.metadata['title']}</title>
        <article_snippet>{doc.page_content}</article_snippet>
    </source>"""
        formatted.append(doc_str)
    return "\n\n<sources>" + "\n".join(formatted) + "</sources>"


format_3 = itemgetter("docs") | RunnableLambda(format_docs_xml)
answer_3 = prompt_3 | anthropic | XMLOutputParser() | itemgetter("cited_answer")
chain_3 = (
    RunnableParallel(question=RunnablePassthrough(), docs=wiki)
    .assign(context=format_3)
    .assign(cited_answer=answer_3)
    .pick(["cited_answer", "docs"])
)
```


```python
chain_3.invoke("How fast are cheetahs?")
```




    {'cited_answer': [{'answer': '猎豹是最快的陆地动物。它们能够以93到104公里每小时（58到65英里）的速度奔跑。'}, {'citations': [{'citation': [{'source_id': '0'}, {'quote': '猎豹能够以93到104公里每小时（58到65英里）的速度奔跑；它已进化出了适应速度的特殊适应性，包括轻盈的体格、细长的腿部和长长的尾巴。'}]}]}]}





## 检索到的文档进行后处理

另一种方法是对我们检索到的文档进行后处理，以压缩内容，这样源内容已经足够简洁，不需要模型引用特定的来源或片段。例如，我们可以将每个文档分成一到两个句子，对其进行嵌入并仅保留最相关的文本。LangChain中有一些内置组件用于此。这里我们将使用[RecursiveCharacterTextSplitter](https://api.python.langchain.com/en/latest/text_splitter/langchain_text_splitters.RecursiveCharacterTextSplitter.html#langchain_text_splitters.RecursiveCharacterTextSplitter)，它通过在分隔子字符串上进行拆分来创建指定大小的块，并且[EmbeddingsFilter](https://api.python.langchain.com/en/latest/retrievers/langchain.retrievers.document_compressors.embeddings_filter.EmbeddingsFilter.html#langchain.retrievers.document_compressors.embeddings_filter.EmbeddingsFilter)，它仅保留具有最相关嵌入的文本。


```python
from langchain.retrievers.document_compressors import EmbeddingsFilter
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=0,
    separators=["\n\n", "\n", ".", " "],
    keep_separator=False,
)
compressor = EmbeddingsFilter(embeddings=OpenAIEmbeddings(), k=10)


def split_and_filter(input) -> List[Document]:
    docs = input["docs"]
    question = input["question"]
    split_docs = splitter.split_documents(docs)
    stateful_docs = compressor.compress_documents(split_docs, question)
    return [stateful_doc for stateful_doc in stateful_docs]


retrieve = (
    RunnableParallel(question=RunnablePassthrough(), docs=wiki) | split_and_filter
)
docs = retrieve.invoke("How fast are cheetahs?")
for doc in docs:
    print(doc.page_content)
    print("\n\n")
```

    成年猎豹的体重在21到72公斤（46到159磅）之间。猎豹能够以93到104公里每小时（58到65英里）的速度奔跑；它已进化出了适应速度的特殊适应性，包括轻盈的体格、细长的腿部和长长的尾巴
    
    
    
    猎豹（Acinonyx jubatus）是一种大型猫科动物，也是世界上最快的陆地动物。它的被毛呈黄褐色到乳白色或灰色，毛上有均匀分布的实心黑色斑点。它的头小而圆，吻部短，有黑色的泪痕状颜纹。它的肩高为67-94厘米（26-37英寸），头体长在1.1到1.5米（3英尺7英寸到4英尺11英寸）之间
    
    
    
    2 mph），或171个体长度每秒。猎豹作为最快的陆地哺乳动物，每秒只有16个体长度，而安娜蜂鸟是所有脊椎动物中已知达到的最高长度特异性速度
    

```python
chain_4 = (
    RunnableParallel(question=RunnablePassthrough(), docs=retrieve)
    .assign(context=format)
    .assign(answer=answer)
    .pick(["answer", "docs"])
)
```


```python



"猎豹是最快的陆地动物。它们能够以93到104公里每小时（58到65英里）的速度奔跑。"**=======**

Cheetahs are capable of running at speeds between 93 to 104 km/h (58 to 65 mph). They have evolved specialized adaptations for speed, including a light build, long thin legs, and a long tail.

```