# XML parser
这个输出解析器允许用户以流行的XML格式从LLM中获取结果。

请记住，大型语言模型是有漏洞的抽象！您必须使用具有足够容量的LLM来生成格式良好的XML。

在下面的示例中，我们使用了Claude模型（https://docs.anthropic.com/claude/docs），它非常适合使用XML标记。


```python
from langchain.output_parsers import XMLOutputParser
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatAnthropic
```


```python
model = ChatAnthropic(model="claude-2", max_tokens_to_sample=512, temperature=0.1)
```

让我们从对模型进行简单请求开始。


```python
actor_query = "Generate the shortened filmography for Tom Hanks."
output = model.invoke(
    f"""{actor_query}
Please enclose the movies in <movie></movie> tags"""
)
print(output.content)
```

     这里是汤姆·汉克斯的简短电影作品列表，放在XML标记中：
    
    <movie>Splash</movie>
    <movie>Big</movie>
    <movie>A League of Their Own</movie>
    <movie>Sleepless in Seattle</movie>
    <movie>Forrest Gump</movie>
    <movie>Toy Story</movie>
    <movie>Apollo 13</movie>
    <movie>Saving Private Ryan</movie>
    <movie>Cast Away</movie>
    <movie>The Da Vinci Code</movie>
    <movie>Captain Phillips</movie>
    

现在我们将使用XMLOutputParser来获取结构化的输出。


```python
parser = XMLOutputParser()

prompt = PromptTemplate(
    template="""{query}\n{format_instructions}""",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

output = chain.invoke({"query": actor_query})
print(output)
```

    {'filmography': [{'movie': [{'title': 'Big'}, {'year': '1988'}]}, {'movie': [{'title': 'Forrest Gump'}, {'year': '1994'}]}, {'movie': [{'title': 'Toy Story'}, {'year': '1995'}]}, {'movie': [{'title': 'Saving Private Ryan'}, {'year': '1998'}]}, {'movie': [{'title': 'Cast Away'}, {'year': '2000'}]}]}
    

最后，让我们添加一些标记，以符合我们的需求。


```python
parser = XMLOutputParser(tags=["movies", "actor", "film", "name", "genre"])
prompt = PromptTemplate(
    template="""{query}\n{format_instructions}""",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


chain = prompt | model | parser

output = chain.invoke({"query": actor_query})

print(output)
```

    {'movies': [{'actor': [{'name': 'Tom Hanks'}, {'film': [{'name': 'Forrest Gump'}, {'genre': 'Drama'}]}, {'film': [{'name': 'Cast Away'}, {'genre': 'Adventure'}]}, {'film': [{'name': 'Saving Private Ryan'}, {'genre': 'War'}]}]}]}
    


```python
for s in chain.stream({"query": actor_query}):
    print(s)
```

    {'movies': [{'actor': [{'name': 'Tom Hanks'}]}]}
    {'movies': [{'actor': [{'film': [{'name': 'Forrest Gump'}]}]}]}
    {'movies': [{'actor': [{'film': [{'genre': 'Drama'}]}]}]}
    {'movies': [{'actor': [{'film': [{'name': 'Cast Away'}]}]}]}
    {'movies': [{'actor': [{'film': [{'genre': 'Adventure'}]}]}]}
    {'movies': [{'actor': [{'film': [{'name': 'Saving Private Ryan'}]}]}]}
    {'movies': [{'actor': [{'film': [{'genre': 'War'}]}]}]}
    


```python

```