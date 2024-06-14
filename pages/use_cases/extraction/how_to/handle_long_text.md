# 处理长文本

当处理文件（如PDF）时，您可能会遇到超出语言模型上下文窗口的文本。为了处理这些文本，考虑以下策略：

1. **更改LLM**选择支持更大上下文窗口的不同LLM。
2. **蛮力**将文档分块，并从每个块中提取内容。
3. **RAG**将文档分块，对块进行索引，并仅从看起来“相关”的块中提取内容。

请记住，这些策略有不同的权衡，最佳策略可能取决于您正在设计的应用程序！

## 设置

我们需要一些示例数据！让我们下载一篇关于[汽车的维基百科文章](https://en.wikipedia.org/wiki/Car)，并将其作为LangChain`Document`加载。


```python
import re

import requests
from langchain_community.document_loaders import BSHTMLLoader

# 下载内容
response = requests.get("https://en.wikipedia.org/wiki/Car")
# 将其写入文件
with open("car.html", "w", encoding="utf-8") as f:
    f.write(response.text)
# 使用HTML解析器加载它
loader = BSHTMLLoader("car.html")
document = loader.load()[0]
# 清理代码
# 将连续的换行符替换为一个换行符
document.page_content = re.sub("\n\n+", "\n", document.page_content)
```


```python
print(len(document.page_content))
```

    78967
    

## 定义模式

在这里，我们将定义模式来提取文本中的关键发展信息。


```python
from typing import List, Optional

from langchain.chains import create_structured_output_runnable
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI


class KeyDevelopment(BaseModel):
    """关于汽车历史中发展的信息。"""

    # ^ 人物实体的文档字符串。
    # 此文档字符串将作为描述模式Person的LLM发送到，它可以帮助改进提取结果。
    # 请注意，所有字段都是必需的，而不是可选的！
    year: int = Field(
        ..., description="重要历史发展发生的年份。"
    )
    description: str = Field(
        ..., description="这一年发生了什么？有什么发展？"
    )
    evidence: str = Field(
        ...,
        description="重复从中提取年份和描述信息的句子的原文",
    )


class ExtractionData(BaseModel):
    """关于汽车历史中关键发展的提取信息。"""

    key_developments: List[KeyDevelopment]


# 定义自定义提示以提供说明和任何额外的上下文。
# 1）您可以将示例添加到提示模板中以改善提取质量
# 2）引入其他参数以考虑上下文（例如，包括从中提取文本的文档的元数据）。
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "您是一个在文本中识别关键历史发展的专家。"
            "仅提取重要的历史发展信息。如果在文本中找不到重要信息，请不要提取任何内容。",
        ),
        # MessagesPlaceholder('examples'), # 继续阅读此用例以了解如何使用示例来提高性能
        ("human", "{text}"),
    ]
)


# 我们将使用工具调用模式，这需要一个支持工具调用的模型。
llm = ChatOpenAI(
    # 考虑使用一个好的模型进行基准测试，以了解可能的最佳质量。
    model="gpt-4-0125-preview",
    # 记得将温度设为0来进行提取！
    temperature=0,
)

extractor = prompt | llm.with_structured_output(
    schema=ExtractionData,
    method="function_calling",
    include_raw=False,
)
```

    /home/eugene/.pyenv/versions/3.11.2/envs/langchain_3_11/lib/python3.11/site-packages/langchain_core/_api/beta_decorator.py:86: LangChainBetaWarning: The function `with_structured_output` is in beta. It is actively being worked on, so the API may change.
      warn_beta(
    

## 蛮力方法

将文档分块，使每个块适合LLM的上下文窗口。


```python
from langchain_text_splitters import TokenTextSplitter

text_splitter = TokenTextSplitter(
    # 控制每个块的大小
    chunk_size=2000,
    # 控制块之间的重叠
    chunk_overlap=20,
)

texts = text_splitter.split_text(document.page_content)
```

使用`.batch`功能在每个块上以**并行**方式运行提取！ 

:::⚠⚠⚠


通常可以使用`.batch()`来并行化提取！ `batch`在幕后使用线程池来帮助并行化工作负载。

如果您的模型通过API公开，这可能会加速提取流程！

:::


```python
# 仅限前3个块
# 这样可以快速重新运行代码
first_few = texts[:3]

extractions = extractor.batch(
    [{"text": text} for text in first_few],
    {"max_concurrency": 5},  # 通过传递最大并发限制并发性！
)
```

### 合并结果

在提取了各个块的数据之后，我们将要合并这些提取。


```python
key_developments = []

for extraction in extractions:
    key_developments.extend(extraction.key_developments)

key_developments[:20]
```




    [KeyDevelopment(year=1966, description="丰田卡罗拉开始生产，并被认为是世界上销量最好的汽车。", evidence="丰田卡罗拉自1966年开始生产，被认为是世界上销量最好的汽车。"),
     KeyDevelopment(year=1769, description='Nicolas-Joseph Cugnot制造了第一辆蒸汽动力公路车。', evidence='法国发明家Nicolas-Joseph Cugnot于1769年制造了世界上第一辆蒸汽动力公路车。'),
     KeyDevelopment(year=1808, description='François Isaac de Rivaz设计并制造了第一辆内燃机汽车。', evidence='法籍瑞士发明家François Isaac de Rivaz于1808年设计并制造了世界上第一辆内燃机汽车。'),
     KeyDevelopment(year=1886, description='Carl Benz获得了他的Benz Patent-Motorwagen专利，发明了现代汽车。', evidence='现代汽车——作为实用的、可销售的日常使用汽车——在1886年被发明出来，当时德国发明家Carl Benz获得了他的Benz Patent-Motorwagen专利。'),
     KeyDevelopment(year=1908, description='福特汽车公司制造了大规模生产的经济车型1908款T型车，用于大众市场。', evidence='1908款T型车是一辆大众市场可负担的汽车，由福特汽车公司制造。'),
     KeyDevelopment(year=1881, description='Gustave Trouvé展示了一辆由电力驱动的三轮车。', evidence='1881年11月，法国发明家Gustave Trouvé在电气展览会上展示了一辆由电力驱动的三轮车。'),
     KeyDevelopment(year=1888, description="Bertha Benz乘汽车进行了第一次公路旅行，以证明丈夫发明的汽车的适应公路能力。", evidence="1888年8月，卡尔·本茨的妻子Bertha Benz乘汽车进行了第一次公路旅行，以证明丈夫发明的汽车的适应公路能力。"),
     KeyDevelopment(year=1896, description='本茨设计并获得了第一个内燃平面发动机的专利，称为boxermotor。', evidence='1896年，本茨设计并获得了第一个内燃平面发动机的专利，称为boxermotor。'),
     KeyDevelopment(year=1897, description='Nesselsdorfer Wagenbau生产了Präsident automobil，世界上第一批量生产的汽车之一。', evidence='第一辆内燃机汽车在中欧由捷克公司Nesselsdorfer Wagenbau（后更名为Tatra）于1897年生产，名为Präsident automobil。'),
     KeyDevelopment(year=1890, description='Daimler Motoren Gesellschaft（DMG）由Daimler和Maybach在Cannstatt成立。', evidence='Daimler和Maybach于1890年在Cannstatt成立了Daimler Motoren Gesellschaft（DMG）。'),
     KeyDevelopment(year=1902, description='新型的DMG车型投产，并以Maybach引擎命名为Mercedes。', evidence='两年后，即1902年，生产了一款新型的DMG汽车，并以Maybach引擎的名字命名该型号，该引擎产生35马力。'),
     KeyDevelopment(year=1891, description='Auguste Doriot和Louis Rigoulot乘坐由Daimler动力的Peugeot Type 3车完成了最长的汽油驱动车辆旅行。', evidence='1891年，Auguste Doriot和他的Peugeot同事Louis Rigoulot乘坐他们自己设计和制造的以Daimler动力为驱动的Peugeot Type 3汽车完成了2100公里（1300英里）的旅行，从Valentigney到巴黎和布雷斯特，然后返回。'),
     KeyDevelopment(year=1895, description='George Selden获得了一项有关二冲程汽车发动机的美国专利。', evidence='经过16年的延迟和一系列附件的附加，Selden于1895年11月5日获得了一项关于二冲程汽车发动机的美国专利（美国专利号549,160）。'),
     KeyDevelopment(year=1893, description='Duryea兄弟制造了第一辆运行良好、以汽油驱动的美国汽车，并对其进行了路试。', evidence='1893年，斯普林菲尔德（马萨诸塞州）的Duryea兄弟制造了第一辆运行良好、以汽油驱动的美国汽车，并对其进行了路试。'),
     KeyDevelopment(year=1897, description='鲁道夫·迪泽尔制造了第一台柴油发动机。', evidence='1897年，他制造了第一台柴油发动机。'),
     KeyDevelopment(year=1901, description='Ransom Olds在他的Oldsmobile工厂开始大规模生产经济汽车的流水线制造。', evidence='Ransom Olds于1901年在他的Lansing（密歇根州）的Oldsmobile工厂开始大规模生产经济汽车的流水线制造。'),
     KeyDevelopment(year=1913, description='Henry Ford在Highland Park Ford工厂开始世界上第一个车辆流水线组装线。', evidence='这个概念由Henry Ford在1913年开始大幅发展，他在Highland Park Ford工厂开设了世界上第一个车辆流水线组装线。'),
     KeyDevelopment(year=1914, description='变速器车间工人工资可以购买一辆Model T汽车。', evidence='1914年，一个变速器车间工人的工资足以购买一辆Model T汽车。'),
     KeyDevelopment(year=1926, description='开发了干燥快速的Duco涂料，可提供各种汽车颜色。', evidence='只有日本黑漆可以干得足够快，迫使该公司在1913年之前放弃了多种可用颜色的选择，直到1926年开发出了干燥快速的Duco涂料。')]## 常见问题

不同的方法在成本、速度和准确性方面都有各自的优缺点。

请注意以下问题：

* 对内容进行分块处理意味着如果信息分散在多个块上，LLM可能无法提取到信息。
* 大块的重叠可能导致相同的信息被提取两次，因此需要做好去重的准备！
* LLM可能会编造数据。如果在大文本中寻找一个单一事实并采用蛮力方法，可能会得到更多编造的数据。