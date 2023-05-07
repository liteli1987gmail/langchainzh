入门
=========

语言模型输出的是文本。但是很多时候，您可能想要获得的信息比仅仅是文本。这就是输出解析器的用处。

输出解析器是帮助结构化语言模型响应的类。输出解析器必须实现两种主要方法：

* `get_format_instructions() -> str`：该方法返回一个包含语言模型输出格式说明的字符串。
* `parse(str) -> Any`：该方法接受一个字符串（假定为语言模型的响应)，并将其解析成某种结构。

还有一个可选方法：

* `parse_with_prompt(str, PromptValue) -> Any`：该方法接受一个字符串（假定为语言模型的响应)和一个提示（假定为生成此类响应的提示)，然后将其解析成某种结构。提示在很大程度上是提供的，以防OutputParser希望以某种方式重试或修复输出，并需要提示信息来执行此操作。

下面我们介绍主要类型的输出解析器——`PydanticOutputParser`。其他选项请参见`examples`文件夹。

```
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator
from typing import List

```

```
model_name = 'text-davinci-003'
temperature = 0.0
model = OpenAI(model_name=model_name, temperature=temperature)

```

```
# Define your desired data structure.
class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

    # You can add custom validation logic easily with Pydantic.
    @validator('setup')
    def question_ends_with_question_mark(cls, field):
        if field[-1] != '?':
            raise ValueError("Badly formed question!")
        return field

```

```
# Set up a parser + inject instructions into the prompt template.
parser = PydanticOutputParser(pydantic_object=Joke)

```

```
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

```

```
# And a query intented to prompt a language model to populate the data structure.
joke_query = "Tell me a joke."
_input = prompt.format_prompt(query=joke_query)

```

```
output = model(_input.to_string())

```

```
parser.parse(output)

```

```
Joke(setup='Why did the chicken cross the road?', punchline='To get to the other side!')

```

