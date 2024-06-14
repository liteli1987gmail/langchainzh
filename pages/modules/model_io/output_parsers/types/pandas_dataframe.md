# Pandas DataFrame 解析器

Pandas DataFrame 是 Python 编程语言中常用的数据结构，通常用于数据操作和分析。它提供了一套全面的工具，用于处理结构化数据，使其成为数据清洗、转换和分析等任务的多功能选择。

该输出解析器允许用户指定任意 Pandas DataFrame，并查询 LLM 来以字典格式提取相应 DataFrame 中的数据。请记住，大型语言模型是有缺陷的抽象！您将需要使用具有足够容量的 LLM 生成符合定义格式指令的查询。

使用 Pandas 的 DataFrame 对象声明要执行查询的 DataFrame。


```python
import pprint
from typing import Any, Dict

import pandas as pd
from langchain.output_parsers import PandasDataFrameOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
```


```python
model = ChatOpenAI(temperature=0)
```


```python
# 仅用于文档目的。
def format_parser_output(parser_output: Dict[str, Any]) -> None:
    for key in parser_output.keys():
        parser_output[key] = parser_output[key].to_dict()
    return pprint.PrettyPrinter(width=4, compact=True).pprint(parser_output)
```


```python
# 定义您想要的 Pandas DataFrame。
df = pd.DataFrame(
    {
        "num_legs": [2, 4, 8, 0],
        "num_wings": [2, 0, 0, 0],
        "num_specimen_seen": [10, 2, 1, 8],
    }
)

# 设置解析器 + 将说明注入到提示模板中。
parser = PandasDataFrameOutputParser(dataframe=df)
```


```python
# 这是正在执行的列操作示例。
df_query = "检索 num_wings 列。"

# 设置提示。
prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser
parser_output = chain.invoke({"query": df_query})

format_parser_output(parser_output)
```

    {'num_wings': {0: 2,
                   1: 0,
                   2: 0,
                   3: 0}}
    


```python
# 这是正在执行的行操作示例。
df_query = "检索第一行。"

# 设置提示。
prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser
parser_output = chain.invoke({"query": df_query})

format_parser_output(parser_output)
```

    {'0': {'num_legs': 2,
           'num_specimen_seen': 10,
           'num_wings': 2}}
    


```python
# 这是限制行数的随机 Pandas DataFrame 操作的示例。
df_query = "从第 1 行到第 3 行检索 num_legs 列的平均值。"

# 设置提示。
prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser
parser_output = chain.invoke({"query": df_query})

print(parser_output)
```

    {'mean': 4.0}
    


```python
# 这是一个格式错误查询的示例
df_query = "检索 num_fingers 列的平均值。"

# 设置提示。
prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser
parser_output = chain.invoke({"query": df_query})
```=======

        I provide the mdx document for translation, only need to translate the content of the headings, paragraphs, and lists in the md syntax. Words with camel case and underscores do not need to be translated. Please keep the punctuation marks in md syntax. After you finish the translation, replace the original content and return the result to me. The mdx document is:=======
        307     kwargs["run_manager"] = run_manager
    --> 308 return func(input, **kwargs)
    

    File ~/workplace/langchain/libs/core/langchain_core/output_parsers/base.py:171, in BaseOutputParser.invoke.<locals>.<lambda>(inner_input)
        166 def invoke(
        167     self, input: Union[str, BaseMessage], config: Optional[RunnableConfig] = None
        168 ) -> T:
        169     if isinstance(input, BaseMessage):
        170         return self._call_with_config(
    --> 171             lambda inner_input: self.parse_result(
        172                 [ChatGeneration(message=inner_input)]
        173             ),
        174             input,
        175             config,
        176             run_type="parser",
        177         )
        178     else:
        179         return self._call_with_config(
        180             lambda inner_input: self.parse_result([Generation(text=inner_input)]),
        181             input,
        182             config,
        183             run_type="parser",
        184         )
    

    File ~/workplace/langchain/libs/core/langchain_core/output_parsers/base.py:222, in BaseOutputParser.parse_result(self, result, partial)
        209 def parse_result(self, result: List[Generation], *, partial: bool = False) -> T:
        210     """Parse a list of candidate model Generations into a specific format.
        211 
        212     The return value is parsed from only the first Generation in the result, which
       (...)
        220         Structured output.
        221     """
    --> 222     return self.parse(result[0].text)
    

    File ~/workplace/langchain/libs/langchain/langchain/output_parsers/pandas_dataframe.py:90, in PandasDataFrameOutputParser.parse(self, request)
         88 request_type, request_params = splitted_request
         89 if request_type in {"Invalid column", "Invalid operation"}:
    ---> 90     raise OutputParserException(
         91         f"{request}. Please check the format instructions."
         92     )
         93 array_exists = re.search(r"(\[.*?\])", request_params)
         94 if array_exists:
    

    OutputParserException: Invalid column: num_fingers. Please check the format instructions.






                Wrap your answer with a format starting with 7 equal signs and ending with 7 equal signs. Your answer is: