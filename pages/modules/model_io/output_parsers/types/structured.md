# 结构化输出解析器

当您想要返回多个字段时，可以使用此输出解析器。虽然Pydantic/JSON解析器更强大，但对于功能较弱的模型非常有用。

```python
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
```

```python
response_schemas = [
    ResponseSchema(name="answer", description="用户问题的答案"),
    ResponseSchema(
        name="source",
        description="用于回答用户问题的来源，应为网站。",
    ),
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
```

现在，我们获得一个字符串，其中包含有关如何格式化响应的说明，然后将其插入到我们的提示中。

```python
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="尽可能最好地回答用户的问题。\n{format_instructions}\n{question}",
    input_variables=["question"],
    partial_variables={"format_instructions": format_instructions},
)
```

```python
model = ChatOpenAI(temperature=0)
chain = prompt | model | output_parser
```

```python
chain.invoke({"question": "法国的首都是什么？"})
```

    {'answer': '法国的首都是巴黎。',
     'source': 'https://en.wikipedia.org/wiki/Paris'}

```python
for s in chain.stream({"question": "法国的首都是什么？"}):
    print(s)
```

    {'answer': '法国的首都是巴黎。', 'source': 'https://en.wikipedia.org/wiki/Paris'}

```python

```



