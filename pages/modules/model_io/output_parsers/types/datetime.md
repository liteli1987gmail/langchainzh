# 日期时间解析器

此OutputParser可用于将LLM输出解析为日期时间格式。


```python
from langchain.output_parsers import DatetimeOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
```


```python
output_parser = DatetimeOutputParser()
template = """回答用户的问题:

{question}

{format_instructions}"""
prompt = PromptTemplate.from_template(
    template,
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)
```


```python
prompt
```




    PromptTemplate(input_variables=['question'], partial_variables={'format_instructions': "写一个符合以下模式的日期时间字符串：'%Y-%m-%dT%H:%M:%S.%fZ'。\n\n示例：0668-08-09T12:56:32.732651Z, 1213-06-23T21:01:36.868629Z, 0713-07-06T18:19:02.257488Z\n\n仅返回此字符串，不要其他单词！"}, template='回答用户的问题:\n\n{question}\n\n{format_instructions}')




```python
chain = prompt | OpenAI() | output_parser
```


```python
output = chain.invoke({"question": "比特币是什么时候成立的？"})
```


```python
print(output)
```

    2009-01-03 18:15:05
    








