

逗号分隔列表输出解析器
=====

这是另一个比Pydantic / JSON解析功能要弱的解析器。

```
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

```

```
output_parser = CommaSeparatedListOutputParser()

```

```
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="List five {subject}.\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions}
)

```

```
model = OpenAI(temperature=0)

```

```
_input = prompt.format(subject="ice cream flavors")
output = model(_input)

```

```
output_parser.parse(output)

```

```
['Vanilla',
 'Chocolate',
 'Strawberry',
 'Mint Chocolate Chip',
 'Cookies and Cream']

```

