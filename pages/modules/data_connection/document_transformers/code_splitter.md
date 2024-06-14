# 代码分割器（CodeSplitter）

CodeTextSplitter 允许您使用多种语言拆分代码。导入枚举 `Language` 并指定语言。

```python
%pip install -qU langchain-text-splitters
```

```python
from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)
```

```python
# 支持的语言列表
[e.value for e in Language]
```

```python
# 您也可以查看给定语言使用的分隔符
RecursiveCharacterTextSplitter.get_separators_for_language(Language.PYTHON)
```

## Python

这是使用 PythonTextSplitter 的示例：

```python
PYTHON_CODE = """
def hello_world():
    print("Hello, World!")

# 调用函数
hello_world()
"""
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)
python_docs = python_splitter.create_documents([PYTHON_CODE])
python_docs
```

## JS

这是使用 JS 文本拆分器的示例：

```python
JS_CODE = """
function helloWorld() {
  console.log("Hello, World!");
}

// 调用函数
helloWorld();
"""
js_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JS, chunk_size=60, chunk_overlap=0
)
js_docs = js_splitter.create_documents([JS_CODE])
js_docs
```

## TS

这是使用 TS 文本拆分器的示例：

```python
TS_CODE = """
function helloWorld(): void {
  console.log("Hello, World!");
}

// 调用函数
helloWorld();
"""
ts_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.TS, chunk_size=60, chunk_overlap=0
)
ts_docs = ts_splitter.create_documents([TS_CODE])
ts_docs
```

## Markdown

这是使用 Markdown 文本拆分器的示例：

```python
markdown_text = """
# 🦜️🔗 LangChain

⚡ 通过组合性构建应用程序与 LLMs ⚡

## 快速安装

```bash
# 希望此代码块不会被拆分
pip install langchain
```

作为一个快速发展领域的开源项目，我们对贡献非常开放。
"""
```

```python
md_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN, chunk_size=60, chunk_overlap=0
)
md_docs = md_splitter.create_documents([markdown_text])
md_docs
```=======

## LaTex

这里是Latex文本的示例：

```python
latex_text = """
\documentclass{article}

\begin{document}

\maketitle

\section{介绍}
大型语言模型（LLMs）是一种可以根据大量文本数据进行训练以生成类似人类语言的机器学习模型。近年来，LLMs在各种自然语言处理任务中取得了显著进展，包括语言翻译、文本生成和情感分析。

\subsection{LLMs的历史}
最早的LLMs是在上世纪80年代和90年代开发的，但受限于当时可以处理的数据量和计算能力。然而，在过去的十年中，硬件和软件的进步使得在大规模数据集上训练LLMs成为可能，从而显著提高了性能。

\subsection{LLMs的应用}
LLMs在工业界有许多应用，包括聊天机器人、内容创作和虚拟助手。它们也可以被用于学术研究，如语言学、心理学和计算语言学。

\end{document}
"""
```

## HTML

这里是使用HTML文本分割器的示例：

```python
html_text = """
<!DOCTYPE html>
<html>
    <head>
        <title>🦜️🔗 LangChain</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            h1 {
                color: darkblue;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>🦜️🔗 LangChain</h1>
            <p>⚡ 通过组合性构建与LLMs相关的应用 ⚡</p>
        </div>
        <div>
            作为一个在快速发展领域中的开源项目，我们非常欢迎贡献。
        </div>
    </body>
</html>
"""
```

## Solidity

这里是使用Solidity文本分割器的示例：

```python
SOL_CODE = """
pragma solidity ^0.8.20;
contract HelloWorld {
   function add(uint a, uint b) pure public returns(uint) {
       return a + b;
   }
}
"""

sol_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.SOL, chunk_size=128, chunk_overlap=0
)
sol_docs = sol_splitter.create_documents([SOL_CODE])
sol_docs
```

## C#

这里是使用C#文本分割器的示例：

```python
C_CODE = """
using System;
class Program
{
    static void Main()
    {
        int age = 30; // 根据需要更改年龄值

        // 在不输出控制台的情况下对年龄进行分类
        if (age < 18)
        {
            // 年龄小于18岁
        }
        else if (age >= 18 && age < 65)
        {
            // 年龄为成年人
        }
        else
        {
            // 年龄为老年人
        }
    }
}
"""
```


## Haskell
这是使用Haskell文本分割器的示例：


```python
HASKELL_CODE = """
main :: IO ()
main = do
    putStrLn "你好，世界！"
-- 一些示例函数
add :: Int -> Int -> Int
add x y = x + y
"""
haskell_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.HASKELL, chunk_size=50, chunk_overlap=0
)
haskell_docs = haskell_splitter.create_documents([HASKELL_CODE])
haskell_docs
```




    [Document(page_content='main :: IO ()'),
     Document(page_content='main = do\n    putStrLn "你好，世界！"\n-- 一些'),
     Document(page_content='示例函数\nadd :: Int -> Int -> Int\nadd x y'),
     Document(page_content='= x + y')]



## PHP
这是使用PHP文本分割器的示例：


```python
PHP_CODE = """<?php
namespace foo;
class Hello {
    public function __construct() { }
}
function hello() {
    echo "你好世界！";
}
interface Human {
    public function breath();
}
trait Foo { }
enum Color
{
    case Red;
    case Blue;
}"""
php_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PHP, chunk_size=50, chunk_overlap=0
)
haskell_docs = php_splitter.create_documents([PHP_CODE])
haskell_docs
```




    [Document(page_content='<?php\nnamespace foo;'),
     Document(page_content='class Hello {'),
     Document(page_content='public function __construct() { }\n}'),
     Document(page_content='function hello() {\n    echo "你好世界！";\n}'),
     Document(page_content='interface Human {\n    public function breath();\n}'),
     Document(page_content='trait Foo { }\nenum Color\n{\n    case Red;'),
     Document(page_content='case Blue;\n}')]


