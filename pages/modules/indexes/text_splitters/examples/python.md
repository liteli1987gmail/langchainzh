Python Code Text Splitter[#](#python-code-text-splitter "Permalink to this headline")
=====================================================================================

PythonCodeTextSplitter可以将文本按Python类和方法定义进行拆分，它是RecursiveCharacterSplitter的一个简单子类，具有Python特定的分隔符。默认情况下，请参阅源代码以查看Python语法。

- 文本如何拆分：通过Python特定字符列表进行拆分

- 如何测量块大小：通过传递的长度函数测量（默认为字符数)

```
from langchain.text_splitter import PythonCodeTextSplitter

```

```
python_text = """
class Foo:

 def bar():

def foo():

def testing_func():

def bar():
"""
python_splitter = PythonCodeTextSplitter(chunk_size=30, chunk_overlap=0)

```

```
docs = python_splitter.create_documents([python_text])

```

```
docs

```

```
[Document(page_content='Foo:      def bar():', lookup_str='', metadata={}, lookup_index=0),
 Document(page_content='foo():  def testing_func():', lookup_str='', metadata={}, lookup_index=0),
 Document(page_content='bar():', lookup_str='', metadata={}, lookup_index=0)]

```
