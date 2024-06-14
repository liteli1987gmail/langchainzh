# CSV

>  [逗号分隔值（CSV）](https://en.wikipedia.org/wiki/Comma-separated_values) 文件是一个使用逗号来分隔值的分隔文本文件。文件的每一行是一个数据记录。每个记录由一个或多个字段组成，由逗号分隔。

用每个文档一个行的方式加载CSV数据。

```python
from langchain_community.document_loaders.csv_loader import CSVLoader


loader = CSVLoader(file_path='./example_data/mlb_teams_2012.csv')
data = loader.load()
```


```python
print(data)
```

---



```
    [Document(page_content='Team: Nationals\n"Payroll (millions)": 81.34\n"Wins": 98', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 0}, lookup_index=0), Document(page_content='Team: Reds\n"Payroll (millions)": 82.20\n"Wins": 97', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 1}, lookup_index=0), Document(page_content='Team: Yankees\n"Payroll (millions)": 197.96\n"Wins": 95', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 2}, lookup_index=0), Document(page_content='Team: Giants\n"Payroll (millions)": 117.62\n"Wins": 94', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 3}, lookup_index=0), Document(page_content='Team: Braves\n"Payroll (millions)": 83.31\n"Wins": 94', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 4}, lookup_index=0), Document(page_content='Team: Athletics\n"Payroll (millions)": 55.37\n"Wins": 94', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 5}, lookup_index=0), Document(page_content='Team: Rangers\n"Payroll (millions)": 120.51\n"Wins": 93', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 6}, lookup_index=0), Document(page_content='Team: Orioles\n"Payroll (millions)": 81.43\n"Wins": 93', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 7}, lookup_index=0), Document(page_content='Team: Rays\n"Payroll (millions)": 64.17\n"Wins": 90', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 8}, lookup_index=0), Document(page_content='Team: Angels\n"Payroll (millions)": 154.49\n"Wins": 89', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 9}, lookup_index=0), Document(page_content='Team: Tigers\n"Payroll (millions)": 132.30\n"Wins": 88', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 10}, lookup_index=0), Document(page_content='Team: Cardinals\n"Payroll (millions)": 110.30\n"Wins": 88', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 11}, lookup_index=0), Document(page_content='Team: Dodgers\n"Payroll (millions)": 95.14\n"Wins": 86', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 12}, lookup_index=0), Document(page_content='Team: White Sox\n"Payroll (millions)": 96.92\n"Wins": 85', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 13}, lookup_index=0), Document(page_content='Team: Brewers\n"Payroll (millions)": 97.65\n"Wins": 83', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 14}, lookup_index=0), Document(page_content='Team: Phillies\n"Payroll (millions)": 174.54\n"Wins": 81', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 15}, lookup_index=0), Document(page_content='Team: Diamondbacks\n"Payroll (millions)": 74.28\n"Wins": 81', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 16}, lookup_index=0), Document(page_content='Team: Pirates\n"Payroll (millions)": 63.43\n"Wins": 79', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 17}, lookup_index=0), Document(page_content='Team: Padres\n"Payroll (millions)": 55.24\n"Wins": 76', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 18}, lookup_index=0), Document(page_content='Team: Mariners\n"Payroll (millions)": 81.97\n"Wins": 75', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 19}, lookup_index=0), Document(page_content='Team: Mets\n"Payroll (millions)": 93.35\n"Wins": 74', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 20}, lookup_index=0), Document(page_content='Team: Blue Jays\n"Payroll (millions)": 75.48\n"Wins": 73', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 21}, lookup_index=0), Document(page_content='Team: Royals\n"Payroll (millions)": 60.91\n"Wins": 72', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 22}, lookup_index=0), Document(page_content='Team: Marlins\n"Payroll (millions)": 118.07\n"Wins": 69', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 23}, lookup_index=0), Document(page_content='Team: Red Sox\n"Payroll (millions)": 173.18\n"Wins": 69', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 24}, lookup_index=0), Document(page_content='Team: Indians\n"Payroll (millions)": 78.43\n"Wins": 68', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 25}, lookup_index=0), Document(page_content='Team: Twins\n"Payroll (millions)": 94.08\n"Wins": 66', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 26}, lookup_index=0), Document(page_content='Team: Rockies\n"Payroll (millions)": 78.06\n"Wins": 64', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 27}, lookup_index=0), Document(page_content='Team: Cubs\n"Payroll (millions)": 88.19\n"Wins": 61', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 28}, lookup_index=0), Document(page_content='Team: Astros\n"Payroll (millions)": 60.65\n"Wins": 55', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 29}, lookup_index=0)]
```

---



## 自定义CSV解析和加载

查看[CSV模块](https://docs.python.org/3/library/csv.html)文档，了解支持的csv参数的更多信息。


```python
loader = CSVLoader(file_path='./example_data/mlb_teams_2012.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['MLB Team', 'Payroll in millions', 'Wins']
})

data = loader.load()
```


```python
print(data)
```

---



```
    [Document(page_content='MLB Team: Team\nPayroll in millions: "Payroll (millions)"\nWins: "Wins"', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 0}, lookup_index=0), Document(page_content='MLB Team: Nationals\nPayroll in millions: 81.34\nWins: 98', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 1}, lookup_index=0), Document(page_content='MLB Team: Reds\nPayroll in millions: 82.20\nWins: 97', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 2}, lookup_index=0), Document(page_content='MLB Team: Yankees\nPayroll in millions: 197.96\nWins: 95', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 3}, lookup_index=0), Document(page_content='MLB Team: Giants\nPayroll in millions: 117.62\nWins: 94', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 4}, lookup_index=0), Document(page_content='MLB Team: Braves\nPayroll in millions: 83.31\nWins: 94', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 5}, lookup_index=0), Document(page_content='MLB Team: Athletics\nPayroll in millions: 55.37\nWins: 94', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 6}, lookup_index=0), Document(page_content='MLB Team: Rangers\nPayroll in millions: 120.51\nWins: 93', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 7}, lookup_index=0), Document(page_content='MLB Team: Orioles\nPayroll in millions: 81.43\nWins: 93', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 8}, lookup_index=0), Document(page_content='MLB Team: Rays\nPayroll in millions: 64.17\nWins: 90', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 9}, lookup_index=0), Document(page_content='MLB Team: Angels\nPayroll in millions: 154.49\nWins: 89', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 10}, lookup_index=0), Document(page_content='MLB Team: Tigers\nPayroll in millions: 132.30\nWins: 88', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 11}, lookup_index=0), Document(page_content='MLB Team: Cardinals\nPayroll in millions: 110.30\nWins: 88', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 12}, lookup_index=0), Document(page_content='MLB Team: Dodgers\nPayroll in millions: 95.14\nWins: 86', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 13}, lookup_index=0), Document(page_content='MLB Team: White Sox\nPayroll in millions: 96.92\nWins: 85', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 14}, lookup_index=0), Document(page_content='MLB Team: Brewers\nPayroll in millions: 97.65\nWins: 83', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 15}, lookup_index=0), Document(page_content='MLB Team: Phillies\nPayroll in millions: 174.54\nWins: 81', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 16}, lookup_index=0), Document(page_content='MLB Team: Diamondbacks\nPayroll in millions: 74.28\nWins: 81', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 17}, lookup_index=0), Document(page_content='MLB Team: Pirates\nPayroll in millions: 63.43\nWins: 79', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 18}, lookup_index=0), Document(page_content='MLB Team: Padres\nPayroll in millions: 55.24\nWins: 76', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 19}, lookup_index=0), Document(page_content='MLB Team: Mariners\nPayroll in millions: 81.97\nWins: 75', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 20}, lookup_index=0), Document(page_content='MLB Team: Mets\nPayroll in millions: 93.35\nWins: 74', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 21}, lookup_index=0), Document(page_content='MLB Team: Blue Jays\nPayroll in millions: 75.48\nWins: 73', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 22}, lookup_index=0), Document(page_content='MLB Team: Royals\nPayroll in millions: 60.91\nWins: 72', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 23}, lookup_index=0), Document(page_content='MLB Team: Marlins\nPayroll in millions: 118.07\nWins: 69', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 24}, lookup_index=0), Document(page_content='MLB Team: Red Sox\nPayroll in millions: 173.18\nWins: 69', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 25}, lookup_index=0), Document(page_content='MLB Team: Indians\nPayroll in millions: 78.43\nWins: 68', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 26}, lookup_index=0), Document(page_content='MLB Team: Twins\nPayroll in millions: 94.08\nWins: 66', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 27}, lookup_index=0), Document(page_content='MLB Team: Rockies\nPayroll in millions: 78.06\nWins: 64', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 28}, lookup_index=0), Document(page_content='MLB Team: Cubs\nPayroll in millions: 88.19\nWins: 61', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 29}, lookup_index=0), Document(page_content='MLB Team: Astros\nPayroll in millions: 60.65\nWins: 55', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 30}, lookup_index=0)]
```

---



## 自定义CSV解析和加载

查看[CSV模块](https://docs.python.org/3/library/csv.html)文档，了解支持的csv参数的更多信息。


```python
loader = CSVLoader(file_path='./example_data/mlb_teams_2012.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['MLB Team', 'Payroll in millions', 'Wins']
})

data = loader.load()
```


```python
print(data)
```

---



```
    [Document(page_content='MLB Team: Team\nPayroll in millions: "Payroll (millions)"\nWins: "Wins"', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 0}, lookup_index=0), Document(page_content='MLB Team: Nationals\nPayroll in millions: 81.34\nWins: 98', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 1}, lookup_index=0), Document(page_content='MLB Team: Reds\nPayroll in millions: 82.20\nWins: 97', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 2}, lookup_index=0), Document(page_content='MLB Team: Yankees\nPayroll in millions: 197.96\nWins: 95', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 3}, lookup_index=0), Document(page_content='MLB Team: Giants\nPayroll in millions: 117.62\nWins: 94', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 4}, lookup_index=0), Document(page_content='MLB Team: Braves\nPayroll in millions: 83.31\nWins: 94', lookup_str='', metadata={'source': './example_data/mlb_teams_2012.csv', 'row': 5}, lookup_index=0), Document(page_content='MLB Team# CSV解析器

当您想返回一个逗号分隔的项目列表时，可以使用此输出解析器。

```python
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

output_parser = CommaSeparatedListOutputParser()

format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="列举五个{subject}。\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions},
)

model = ChatOpenAI(temperature=0)

chain = prompt | model | output_parser
```


```python
chain.invoke({"subject": "冰淇淋口味"})
```




    ['香草',
     '巧克力',
     '草莓',
     '薄荷巧克力碎片',
     '曲奇与奶油']




```python
for s in chain.stream({"subject": "冰淇淋口味"}):
    print(s)
```

    ['香草']
    ['巧克力']
    ['草莓']
    ['薄荷巧克力碎片']
    ['曲奇与奶油']
    




