# 合成数据生成

合成数据是人为生成的数据，而不是从真实世界事件中收集的数据。它用于模拟真实数据而不会泄露隐私或遇到真实世界的限制。

合成数据的好处：

1. **隐私和安全性**：不存在真实个人数据的泄露风险。
2. **数据增强**：扩展机器学习的数据集。
3. **灵活性**：创建特定或罕见的场景。
4. **具有成本效益**：通常比真实世界的数据收集更便宜。
5. **符合监管要求**：有助于遵守严格的数据保护法律。
6. **模型鲁棒性**：可以导致更好的泛化人工智能模型。
7. **快速原型**：无需真实数据即可进行快速测试。
8. **可控实验**：模拟特定条件。
9. **数据访问**：在真实数据不可用时的替代方法。

注意：尽管有这些好处，合成数据应谨慎使用，因为它可能无法始终捕捉到真实世界的复杂性。

## 快速开始

在本文档中，我们将深入探讨使用langchain库生成合成医疗账单记录。当您想要开发或测试算法，但又不想使用真实患者数据，因为涉及隐私问题或数据可用性问题时，这个工具非常有用。

### 设置
首先，您需要安装langchain库及其依赖项。由于我们使用了OpenAI生成器链，我们还将安装OpenAI。由于这是一个实验性的库，我们需要在安装中包含`langchain_experimental`。然后我们将导入所需的模块。

```python
%pip install --upgrade --quiet  langchain langchain_experimental langchain-openai
# 设置环境变量OPENAI_API_KEY或从.env文件中加载：
# import dotenv
# dotenv.load_dotenv()

from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_experimental.tabular_synthetic_data.openai import (
    OPENAI_TEMPLATE,
    create_openai_data_generator,
)
from langchain_experimental.tabular_synthetic_data.prompts import (
    SYNTHETIC_FEW_SHOT_PREFIX,
    SYNTHETIC_FEW_SHOT_SUFFIX,
)
from langchain_openai import ChatOpenAI
```

## 1. 定义数据模型
每个数据集都有一个结构或“模式”。下面的MedicalBilling类作为我们合成数据的模式。通过定义这个模式，我们向合成数据生成器提供了关于我们期望的数据的形状和性质的信息。

```python
class MedicalBilling(BaseModel):
    patient_id: int
    patient_name: str
    diagnosis_code: str
    procedure_code: str
    total_charge: float
    insurance_claim_amount: float
```

例如，每条记录将具有一个整数类型的`patient_id`，一个字符串类型的`patient_name`，以此类推。

## 2. 示例数据
为了指导合成数据生成器，提供一些类似真实世界的示例数据是有用的。这些示例作为“种子” - 它们代表您想要的数据的类型，并且生成器将使用它们来创建更多外观相似的数据。

下面是一些虚构的医疗账单记录示例：

```python
examples = [
    {
        "example": """Patient ID: 123456, Patient Name: John Doe, Diagnosis Code: 
        J20.9, Procedure Code: 99203, Total Charge: $500, Insurance Claim Amount: $350"""
    },
    {
        "example": """Patient ID: 789012, Patient Name: Johnson Smith, Diagnosis 
        Code: M54.5, Procedure Code: 99213, Total Charge: $150, Insurance Claim Amount: $120"""
    },
    {
        "example": """Patient ID: 345678, Patient Name: Emily Stone, Diagnosis Code: 
        E11.9, Procedure Code: 99214, Total Charge: $300, Insurance Claim Amount: $250"""
    },
]
```

## 3. 创建一个提示模板
生成器不会自动知道如何创建我们的数据；我们需要指导它。为此，我们创建一个提示模板。这个模板有助于向底层语言模型传达有关如何以期望的格式生成合成数据的指令。

```python
OPENAI_TEMPLATE = PromptTemplate(input_variables=["example"], template="{example}")

prompt_template = FewShotPromptTemplate(
    prefix=SYNTHETIC_FEW_SHOT_PREFIX,
    examples=examples,
    suffix=SYNTHETIC_FEW_SHOT_SUFFIX,
    input_variables=["subject", "extra"],
    example_prompt=OPENAI_TEMPLATE,
)
```

`FewShotPromptTemplate` 包含以下内容：

- `prefix` 和 `suffix`：这些可能包含指导上下文或说明。
- `examples`：我们之前定义的示例数据。
- `input_variables`：这些变量 ("subject", "extra") 是您可以稍后动态填充的占位符。例如，"subject" 可以填充为 "medical_billing" 以进一步指导模型。
- `example_prompt`：这个模板是我们在提示中希望每个示例行采用的格式。

## 4. 创建数据生成器
有了模式和提示准备好后，下一步是创建数据生成器。这个对象知道如何与底层语言模型进行通信以获取合成数据。

```python
synthetic_data_generator = create_openai_data_generator(
    output_schema=MedicalBilling,
    llm=ChatOpenAI(
        temperature=1
    ),  # 您需要用实际的语言模型实例替换这里
    prompt=prompt_template,
)
```

## 5. 生成合成数据
最后，让我们获取我们的合成数据！

```python
synthetic_results = synthetic_data_generator.generate(
    subject="medical_billing",
    extra="the name must be chosen at random. Make it something you wouldn't normally choose.",
    runs=10,
)
```

该命令要求生成器生成10条合成医疗账单记录。结果存储在 `synthetic_results` 中。输出将是一个MedicalBilling的pydantic模型列表。

### 其他实现

```python
from langchain_experimental.synthetic_data import (
    DatasetGenerator,
    create_data_generation_chain,
)
from langchain_openai import ChatOpenAI
```

```python
# LLM
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
chain = create_data_generation_chain(model)
```

```python
chain({"fields": ["blue", "yellow"], "preferences": {}})
```

```python
chain(
    {
        "fields": {"colors": ["blue", "yellow"]},
        "preferences": {"style": "Make it in a style of a weather forecast."},
    }
)
```

```python
chain(
    {
        "fields": {"actor": "Tom Hanks", "movies": ["Forrest Gump", "Green Mile"]},
        "preferences": None,
    }
)
```

```python
chain(
    {
        "fields": [
            {"actor": "Tom Hanks", "movies": ["Forrest Gump", "Green Mile"]},
            {"actor": "Mads Mikkelsen", "movies": ["Hannibal", "Another round"]},
        ],
        "preferences": {"minimum_length": 200, "style": "gossip"},
    }
)
```

正如我们所看到的，创建的示例是多样化的，并且具备我们希望它们拥有的信息。而且，它们的风格很好地反映了给定的偏好。


## 用于提取基准测试目的的示例数据集生成


```python
inp = [
    {
        "Actor": "Tom Hanks",
        "Film": [
            "Forrest Gump",
            "Saving Private Ryan",
            "The Green Mile",
            "Toy Story",
            "Catch Me If You Can",
        ],
    },
    {
        "Actor": "Tom Hardy",
        "Film": [
            "Inception",
            "The Dark Knight Rises",
            "Mad Max: Fury Road",
            "The Revenant",
            "Dunkirk",
        ],
    },
]

generator = DatasetGenerator(model, {"style": "informal", "minimal length": 500})
dataset = generator(inp)
```


```python
dataset
```




    [{'fields': {'Actor': 'Tom Hanks',
       'Film': ['Forrest Gump',
        'Saving Private Ryan',
        'The Green Mile',
        'Toy Story',
        'Catch Me If You Can']},
      'preferences': {'style': 'informal', 'minimal length': 500},
      'text': 'Tom Hanks, the versatile and charismatic actor, has graced the silver screen in numerous iconic films including the heartwarming and inspirational "Forrest Gump," the intense and gripping war drama "Saving Private Ryan," the emotionally charged and thought-provoking "The Green Mile," the beloved animated classic "Toy Story," and the thrilling and captivating true story adaptation "Catch Me If You Can." With his impressive range and genuine talent, Hanks continues to captivate audiences worldwide, leaving an indelible mark on the world of cinema.'},
     {'fields': {'Actor': 'Tom Hardy',
       'Film': ['Inception',
        'The Dark Knight Rises',
        'Mad Max: Fury Road',
        'The Revenant',
        'Dunkirk']},
      'preferences': {'style': 'informal', 'minimal length': 500},
      'text': 'Tom Hardy, the versatile actor known for his intense performances, has graced the silver screen in numerous iconic films, including "Inception," "The Dark Knight Rises," "Mad Max: Fury Road," "The Revenant," and "Dunkirk." Whether he\'s delving into the depths of the subconscious mind, donning the mask of the infamous Bane, or navigating the treacherous wasteland as the enigmatic Max Rockatansky, Hardy\'s commitment to his craft is always evident. From his breathtaking portrayal of the ruthless Eames in "Inception" to his captivating transformation into the ferocious Max in "Mad Max: Fury Road," Hardy\'s dynamic range and magnetic presence captivate audiences and leave an indelible mark on the world of cinema. In his most physically demanding role to date, he endured the harsh conditions of the freezing wilderness as he portrayed the rugged frontiersman John Fitzgerald in "The Revenant," earning him critical acclaim and an Academy Award nomination. In Christopher Nolan\'s war epic "Dunkirk," Hardy\'s stoic and heroic portrayal of Royal Air Force pilot Farrier showcases his ability to convey deep emotion through nuanced performances. With his chameleon-like ability to inhabit a wide range of characters and his unwavering commitment to his craft, Tom Hardy has undoubtedly solidified his place as one of the most talented and sought-after actors of his generation.'}]



## 从生成的示例中提取内容
好的，让我们看看我们现在是否可以从生成的数据中提取输出，并将其与我们的情况进行比较！


```python
from typing import List

from langchain.chains import create_extraction_chain_pydantic
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from pydantic import BaseModel, Field
```


```python
class Actor(BaseModel):
    Actor: str = Field(description="演员姓名")
    Film: List[str] = Field(description="他们出演的电影列表")
```

### 解析器


```python
llm = OpenAI()
parser = PydanticOutputParser(pydantic_object=Actor)

prompt = PromptTemplate(
    template="从给定文本中提取字段。\n{format_instructions}\n{text}\n",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

_input = prompt.format_prompt(text=dataset[0]["text"])
output = llm(_input.to_string())

parsed = parser.parse(output)
parsed
```




    Actor(Actor='Tom Hanks', Film=['Forrest Gump', 'Saving Private Ryan', 'The Green Mile', 'Toy Story', 'Catch Me If You Can'])




```python
(parsed.Actor == inp[0]["Actor"]) & (parsed.Film == inp[0]["Film"])
```




    True



### 提取器


```python
extractor = create_extraction_chain_pydantic(pydantic_schema=Actor, llm=model)
extracted = extractor.run(dataset[1]["text"])
extracted
```




    [Actor(Actor='Tom Hardy', Film=['Inception', 'The Dark Knight Rises', 'Mad Max: Fury Road', 'The Revenant', 'Dunkirk'])]




```python
(extracted[0].Actor == inp[1]["Actor"]) & (extracted[0].Film == inp[1]["Film"])
```




    True






