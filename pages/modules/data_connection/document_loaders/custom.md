
# 自定义文档加载器

## 概述

基于LLMs的应用程序通常涉及从数据库或文件（如PDF）中提取数据，并将其转换为LLMs可以利用的格式。在LangChain中，这通常涉及创建文档对象，该对象封装了提取的文本（`page_content`）以及包含有关文档详细信息的元数据 - 一个包含有关文档的作者姓名或发布日期等详细信息的字典。

`Document`对象通常被格式化为提示，然后被馈送到LLM中，允许LLM使用`Document`中的信息生成所需的响应（例如，对文档进行总结）。`Documents`可以立即使用，也可以索引到矢量存储以供将来检索和使用。

文档加载的主要抽象为：

| 组件           | 描述                          |
|----------------|----------------------------|
| Document       | 包含`text`和`metadata`    |
| BaseLoader     | 用于将原始数据转换为`Documents`  |
| Blob           | 二进制数据的表示，可以位于文件或内存中  |
| BaseBlobParser | 逻辑解析`Blob`以产生`Document`对象 |

本指南将演示如何编写自定义文档加载和文件解析逻辑；具体来说，我们将看到如何：

1. 通过从`BaseLoader`继承而创建标准文档加载器。
2. 使用`BaseBlobParser`创建解析器，并将其与`Blob`和`BlobLoaders`一起使用。这在处理文件时非常有用。

## 标准文档加载器

文档加载器可通过从`BaseLoader`继承实现，后者提供了加载文档的标准接口。

### 接口

| 方法名      | 解释        |
|-------------|-------------|
| lazy_load   | 用于**惰性**逐个加载文档。用于生产代码。 |
| alazy_load  | `lazy_load`的异步变体 |
| load        | 用于**急性**加载所有文档到内存中。用于原型设计或交互工作。 |
| aload       | 用于**急性**加载所有文档到内存中。用于原型设计或交互工作。 **添加于LangChain的2024年04月**。 |

- `load`方法仅适用于原型设计工作 - 它只调用`list(self.lazy_load())`。
- `alazy_load`有一个默认实现，会委托给`lazy_load`。如果您使用异步操作，建议重写默认实现并提供本机异步实现。

::: ⚠⚠⚠
在实现文档加载器时，**不要**通过`lazy_load`或`alazy_load`方法传递参数。
预期所有配置通过初始化程序（__init__）传递。这是LangChain的设计选择，以确保一旦实例化文档加载器，就会具有加载文档所需的所有信息。
:::

### 实现

让我们创建一个标准文档加载器的示例，该加载器会读取文件，并为文件中的每一行创建一个文档。


```python
from typing import AsyncIterator, Iterator

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document


class CustomDocumentLoader(BaseLoader):
    """读取文件的示例文档加载器，每行创建一个文档。"""

    def __init__(self, file_path: str) -> None:
        """使用文件路径初始化加载器。

        Args:
            file_path: 要加载的文件的路径。
        """
        self.file_path = file_path

    def lazy_load(self) -> Iterator[Document]:  # <-- 不带任何参数
        """逐行读取文件的懒加载器。

        在实现惰性加载方法时，应使用生成器逐个生成文档。
        """
        with open(self.file_path, encoding="utf-8") as f:
            line_number = 0
            for line in f:
                yield Document(
                    page_content=line,
                    metadata={"line_number": line_number, "source": self.file_path},
                )
                line_number += 1

    # alazy_load是可选的。
    # 如果省略实现，则将使用一个委托给lazy_load的默认实现！
    async def alazy_load(
        self,
    ) -> AsyncIterator[Document]:  # <-- 不带任何参数
        """逐行读取文件的异步懒加载器。"""
        # 需要aiofiles
        # 使用 `pip install aiofiles` 安装
        # https://github.com/Tinche/aiofiles
        import aiofiles

        async with aiofiles.open(self.file_path, encoding="utf-8") as f:
            line_number = 0
            async for line in f:
                yield Document(
                    page_content=line,
                    metadata={"line_number": line_number, "source": self.file_path},
                )
                line_number += 1
```

### 测试 🧪

要测试文档加载器，我们需要一个包含一些优质内容的文件。


```python
with open("./meow.txt", "w", encoding="utf-8") as f:
    quality_content = "meow meow🐱 \n meow meow🐱 \n meow😻😻"
    f.write(quality_content)

loader = CustomDocumentLoader("./meow.txt")
```


```python
## 测试懒加载接口
for doc in loader.lazy_load():
    print()
    print(type(doc))
    print(doc)
```

    
    <class 'langchain_core.documents.base.Document'>
    page_content='meow meow🐱 \n' metadata={'line_number': 0, 'source': './meow.txt'}
    
    <class 'langchain_core.documents.base.Document'>
    page_content=' meow meow🐱 \n' metadata={'line_number': 1, 'source': './meow.txt'}
    
    <class 'langchain_core.documents.base.Document'>
    page_content=' meow😻😻' metadata={'line_number': 2, 'source': './meow.txt'}
    


```python
## 测试异步实现
async for doc in loader.alazy_load():
    print()
    print(type(doc))
    print(doc)
```

    
    <class 'langchain_core.documents.base.Document'>
    page_content='meow meow🐱 \n' metadata={'line_number': 0, 'source': './meow.txt'}
    
    <class 'langchain_core.documents.base.Document'>
    page_content=' meow meow🐱 \n' metadata={'line_number': 1, 'source': './meow.txt'}
    
    <class 'langchain_core.documents.base.Document'>
    page_content=' meow😻😻' metadata={'line_number': 2, 'source': './meow.txt'}
    

::: {.callout-tip}

`load()`在诸如jupyter笔记本之类的交互环境中很有用。

避免用于生产代码，因为急性加载假定所有内容都可以适合内存，而在某些情况下（特别是企业数据），情况并非总是如此。
:::


```python
loader.load()
```




    [Document(page_content='meow meow🐱 \n', metadata={'line_number': 0, 'source': './meow.txt'}),
     Document(page_content=' meow meow🐱 \n', metadata={'line_number': 1, 'source': './meow.txt'}),
     Document(page_content=' meow😻😻', metadata={'line_number': 2, 'source': './meow.txt'})]



## 使用文件

许多文档加载器涉及解析文件。这些加载器之间的区别通常在于如何解析文件而不是如何加载文件。例如，您可以使用`open`读取PDF文件或标记文件的二进制内容，但您需要不同的解析逻辑将二进制数据转换为文本。

因此，将解析逻辑与加载逻辑分离可能非常有用，这样一来，无论数据如何加载，都可以更容易地重用给定的解析器。

### BaseBlobParser

`BaseBlobParser`是一个接口，接受一个`blob`并输出一个`Document`对象列表。`blob`是一个表示数据的实体，可以在内存中或文件中存在。LangChain python具有`Blob`原语，受[Blob WebAPI规范](https://developer.mozilla.org/zh-CN/docs/Web/API/Blob)的启发。

```python
from langchain_core.document_loaders import BaseBlobParser, Blob

class MyParser(BaseBlobParser):
    """一个将每行转换为文档的简单解析器。"""

    def lazy_parse(self, blob: Blob) -> Iterator[Document]:
        """将一个blob逐行解析为文档。"""
        line_number = 0
        with blob.as_bytes_io() as f:
            for line in f:
                line_number += 1
                yield Document(
                    page_content=line,
                    metadata={"line_number": line_number, "source": blob.source},
                )
```

使用**blob** API还允许从内存直接加载内容，而无需从文件中读取！

```python
blob = Blob.from_path("./meow.txt")
parser = MyParser()
```


```python
list(parser.lazy_parse(blob))
```




    [Document(page_content='meow meow🐱 \n', metadata={'line_number': 1, 'source': './meow.txt'}),
     Document(page_content=' meow meow🐱 \n', metadata={'line_number': 2, 'source': './meow.txt'}),
     Document(page_content=' meow😻😻', metadata={'line_number': 3, 'source': './meow.txt'})]



使用**blob** API还可以直接从内存加载内容，而无需从文件中读取！

```python
blob = Blob(data=b"some data from memory\nmeow")
list(parser.lazy_parse(blob))
```




    [Document(page_content='some data from memory\n', metadata={'line_number': 1, 'source': None}),
     Document(page_content='meow', metadata={'line_number': 2, 'source': None})=======

                

### Blob

让我们简要地浏览一下 Blob API 的一些内容。

```python
blob = Blob.from_path("./meow.txt", metadata={"foo": "bar"})
```

```python
blob.encoding
```

'utf-8'

```python
blob.as_bytes()
```

b'meow meow\xf0\x9f\x90\xb1 \n meow meow\xf0\x9f\x90\xb1 \n meow\xf0\x9f\x98\xbb\xf0\x9f\x98\xbb'

```python
blob.as_string()
```

'meow meow🐱 \n meow meow🐱 \n meow😻😻'

```python
blob.as_bytes_io()
```

<contextlib._GeneratorContextManager at 0x743f34324450>

```python
blob.metadata
```

{'foo': 'bar'}

```python
blob.source
```

'./meow.txt'

### Blob Loaders

虽然解析器封装了将二进制数据解析为文档所需的逻辑，但是 *blob loaders* 封装了从给定存储位置加载 blob 所需的逻辑。

目前， `LangChain` 仅支持 `FileSystemBlobLoader`。

您可以使用 `FileSystemBlobLoader` 来加载 blob，然后使用解析器对其进行解析。

```python
from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoader

blob_loader = FileSystemBlobLoader(path=".", glob="*.mdx", show_progress=True)
```

```python
parser = MyParser()
for blob in blob_loader.yield_blobs():
    for doc in parser.lazy_parse(blob):
        print(doc)
        break
```
```
0%|          | 0/8 [00:00<?, ?it/s]

page_content='# Microsoft Office\n' metadata={'line_number': 1, 'source': 'office_file.mdx'}
page_content='# Markdown\n' metadata={'line_number': 1, 'source': 'markdown.mdx'}
page_content='# JSON\n' metadata={'line_number': 1, 'source': 'json.mdx'}
page_content='---\n' metadata={'line_number': 1, 'source': 'pdf.mdx'}
page_content='---\n' metadata={'line_number': 1, 'source': 'index.mdx'}
page_content='# File Directory\n' metadata={'line_number': 1, 'source': 'file_directory.mdx'}
page_content='# CSV\n' metadata={'line_number': 1, 'source': 'csv.mdx'}
page_content='# HTML\n' metadata={'line_number': 1, 'source': 'html.mdx'}
```

### Generic Loader

LangChain 在 `GenericLoader` 中组合了 `BlobLoader` 和 `BaseBlobParser` 的抽象。

`GenericLoader` 旨在提供标准化的类方法，使使用现有的 `BlobLoader` 实现变得容易。目前，只支持 `FileSystemBlobLoader`。

```python
from langchain_community.document_loaders.generic import GenericLoader

loader = GenericLoader.from_filesystem(
    path=".", glob="*.mdx", show_progress=True, parser=MyParser()
)

for idx, doc in enumerate(loader.lazy_load()):
    if idx < 5:
        print(doc)

print("... output truncated for demo purposes")
```
```
0%|          | 0/8 [00:00<?, ?it/s]

page_content='# Microsoft Office\n' metadata={'line_number': 1, 'source': 'office_file.mdx'}
page_content='\n' metadata={'line_number': 2, 'source': 'office_file.mdx'}
page_content='>[The Microsoft Office](https://www.office.com/) suite of productivity software includes Microsoft Word, Microsoft Excel, Microsoft PowerPoint, Microsoft Outlook, and Microsoft OneNote. It is available for Microsoft Windows and macOS operating systems. It is also available on Android and iOS.\n' metadata={'line_number': 3, 'source': 'office_file.mdx'}
page_content='\n' metadata={'line_number': 4, 'source': 'office_file.mdx'}
page_content='This covers how to load commonly used file formats including `DOCX`, `XLSX` and `PPTX` documents into a document format that we can use downstream.\n' metadata={'line_number': 5, 'source': 'office_file.mdx'}
... output truncated for demo purposes
```

#### Custom Generic Loader

如果您喜欢创建类，可以创建一个类来封装一起的逻辑。

您可以从这个类继承以使用现有的加载器加载内容。

```python
from typing import Any


class MyCustomLoader(GenericLoader):
    @staticmethod
    def get_parser(**kwargs: Any) -> BaseBlobParser:
        """Override this method to associate a default parser with the class."""
        return MyParser()
```

```python
loader = MyCustomLoader.from_filesystem(path=".", glob="*.mdx", show_progress=True)

for idx, doc in enumerate(loader.lazy_load()):
    if idx < 5:
        print(doc)

print("... output truncated for demo purposes")
```
```
0%|          | 0/8 [00:00<?, ?it/s]

page_content='# Microsoft Office\n' metadata={'line_number': 1, 'source': 'office_file.mdx'}
page_content='\n' metadata={'line_number': 2, 'source': 'office_file.mdx'}
page_content='>[The Microsoft Office](https://www.office.com/) suite of productivity software includes Microsoft Word, Microsoft Excel, Microsoft PowerPoint, Microsoft Outlook, and Microsoft OneNote. It is available for Microsoft Windows and macOS operating systems. It is also available on Android and iOS.\n' metadata={'line_number': 3, 'source': 'office_file.mdx'}
page_content='\n' metadata={'line_number': 4, 'source': 'office_file.mdx'}
page_content='This covers how to load commonly used file formats including `DOCX`, `XLSX` and `PPTX` documents into a document format that we can use downstream.\n' metadata={'line_number': 5, 'source': 'office_file.mdx'}
... output truncated for demo purposes# 自定义输出解析器
```

在某些情况下，您可能希望实现一个自定义解析器，以将模型输出结构化为自定义格式。

实现自定义解析器有两种方式：

1. 在 LCEL 中使用 `RunnableLambda` 或 `RunnableGenerator` -- 我们强烈推荐在大多数情况下使用这种方式
2. 通过继承基类之一来实现解析器 -- 这是一种比较困难的方式

这两种方式的区别主要在于触发的回调方式（例如 `on_chain_start` 与 `on_parser_start`），以及可追踪平台中像 LangSmith 这样的可运行 lambda 与解析器的可视化方式。

## 可运行的 Lambda 和生成器

推荐的解析方式是使用 **可运行的 lambda** 和 **可运行的生成器**！

这里，我们将创建一个简单的解析器，将模型输出的大小写颠倒。

例如，如果模型输出为：“喵”，则解析器将生成“mEOW”。

```python
from typing import Iterable

from langchain_anthropic.chat_models import ChatAnthropic
from langchain_core.messages import AIMessage, AIMessageChunk

model = ChatAnthropic(model_name="claude-2.1")

def parse(ai_message: AIMessage) -> str:
    """解析 AI 消息。"""
    return ai_message.content.swapcase()

chain = model | parse
chain.invoke("hello")
```

    'hELLO!'

:::⚠⚠⚠



LCEL 在使用 `|` 语法进行组合时，会自动将函数 `parse` 升级为 `RunnableLambda(parse)`。

如果你不喜欢这种方式，你可以手动导入 `RunnableLambda`，然后运行 `parse = RunnableLambda(parse)`。
:::

流式工作吗？

```python
for chunk in chain.stream("tell me about yourself in one sentence"):
    print(chunk, end="|", flush=True)
```

    i'M cLAUDE, AN ai ASSISTANT CREATED BY aNTHROPIC TO BE HELPFUL, HARMLESS, AND HONEST!|

不行，因为解析器会在解析输出之前聚合输入。

如果我们想要实现流式解析器，可以使解析器接受输入的可迭代对象，并在结果可用时生成结果。

```python
from langchain_core.runnables import RunnableGenerator

def streaming_parse(chunks: Iterable[AIMessageChunk]) -> Iterable[str]:
    for chunk in chunks:
        yield chunk.content.swapcase()

streaming_parse = RunnableGenerator(streaming_parse)
```

:::⚠⚠⚠



请将流式解析器包装在 `RunnableGenerator` 中，因为我们可能不再自动使用 `|` 语法升级它。
:::

```python
chain = model | streaming_parse
chain.invoke("hello")
```

    'hELLO!'

让我们确认一下流式工作！

```python
for chunk in chain.stream("tell me about yourself in one sentence"):
        print(chunk, end="|", flush=True)
```

    i|'M| cLAUDE|,| AN| ai| ASSISTANT| CREATED| BY| aN|THROP|IC| TO| BE| HELPFUL|,| HARMLESS|,| AND| HONEST|.!|

## 继承解析基类

另一种实现解析器的方法是通过继承 `BaseOutputParser`、`BaseGenerationOutputParser` 或其他一个基本解析器中的类，具体取决于您需要做什么。

一般来说，**我们不建议**使用这种方式，因为这样会导致更多需要编写的代码，而且并没有显著的好处。

最简单的输出解析器扩展了 `BaseOutputParser` 类，并且必须实现以下方法：

* `parse`：接收模型的字符串输出并对其进行解析
* （可选）`_type`：标识解析器的名称

当聊天模型或 LLM 的输出格式不正确时，可以抛出 `OutputParserException` 来指示解析失败是由于错误的输入。使用此异常可以让利用解析器的代码以一致的方式处理异常。

:::⚠⚠⚠

 解析器也是可运行的！🏃

由于 `BaseOutputParser` 实现了 `Runnable` 接口，您通过这种方式创建的任何自定义解析器都将成为有效的 LangChain 可运行对象，并且将从自动异步支持、批处理接口、日志支持等中受益。
:::

### 简单解析器

这是一个简单的解析器，可以解析表示布尔值的 **字符串**（例如 `YES` 或 `NO`）并将其转换为相应的 `boolean` 类型。

```python
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import BaseOutputParser

# [bool] 描述了一个泛型的参数化。
# 这基本上表示 parse 的返回类型，即 True 或 False
class BooleanOutputParser(BaseOutputParser[bool]):
    """自定义布尔解析器。"""

    true_val: str = "YES"
    false_val: str = "NO"

    def parse(self, text: str) -> bool:
        cleaned_text = text.strip().upper()
        if cleaned_text not in (self.true_val.upper(), self.false_val.upper()):
            raise OutputParserException(
                f"BooleanOutputParser 期望输出值为 "
                f"{self.true_val} 或 {self.false_val}（不区分大小写）。 "
                f"接收到 {cleaned_text}。"
            )
        return cleaned_text == self.true_val.upper()

    @property
    def _type(self) -> str:
        return "boolean_output_parser"
```

```python
parser = BooleanOutputParser()
parser.invoke("YES")
```

    True

```python
try:
    parser.invoke("MEOW")
except Exception as e:
    print(f"触发了 {type(e)} 类型的异常")
```

    触发了 <class 'langchain_core.exceptions.OutputParserException'> 类型的异常

让我们测试一下更改参数化是否有效

```python
parser = BooleanOutputParser(true_val="OKAY")
parser.invoke("OKAY")
```

    True

让我们确认其他 LCEL 方法是否存在

```python
parser.batch(["OKAY", "NO"])
```

    [True, False]

```python
await parser.abatch(["OKAY", "NO"])
```

    [True, False]

```python
from langchain_anthropic.chat_models import ChatAnthropic

anthropic = ChatAnthropic(model_name="claude-2.1")
anthropic.invoke("say OKAY or NO")
```

    AIMessage(content='OKAY')

让我们测试一下我们的解析器是否能正常工作！

```python
chain = anthropic | parser
chain.invoke("say OKAY or NO")
```

    True

:::{.callout-note}
解析器可以处理 LLM 的输出（字符串）或聊天模型的输出（`AIMessage`）！
:::

### 解析原始模型输出

有时除了原始文本之外，还有一些重要的模型输出元数据。一个例子是工具调用，其中用于传递给调用函数的参数被返回到一个单独的属性中。如果您需要这种更精细的控制，您可以选择继承`BaseGenerationOutputParser`类。

这个类需要一个名为`parse_result`的方法。这个方法接受原始模型输出（例如，`Generation`或`ChatGeneration`的列表）并返回解析后的输出。

支持`Generation`和`ChatGeneration`两种类型，使解析器可以同时与普通语言模型和聊天模型一起使用。

```python
from typing import List

from langchain_core.exceptions import OutputParserException
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import BaseGenerationOutputParser
from langchain_core.outputs import ChatGeneration, Generation


class StrInvertCase(BaseGenerationOutputParser[str]):
    """一个示例解析器，翻转消息中字符的大小写。

    这是一个演示示例，目的是展示简单。
    """

    def parse_result(self, result: List[Generation], *, partial: bool = False) -> str:
        """将模型生成的结果解析成特定格式的方法。

        参数:
            result: 一个待解析的Generation列表。假定这些Generation是用于单个模型输入的不同候选输出。
                    许多解析器假定只传入一个单一生成。
                    我们会对此进行断言
            partial: 是否允许部分结果。这用于支持流式处理的解析器。
        """
        if len(result) != 1:
            raise NotImplementedError(
                "此输出解析器只能用于单个生成。"
            )
        generation = result[0]
        if not isinstance(generation, ChatGeneration):
            # 表示此解析器只能用于聊天生成
            raise OutputParserException(
                "此输出解析器只能用于聊天生成。"
            )
        return generation.message.content.swapcase()


chain = anthropic | StrInvertCase()
```

让我们尝试一下新的解析器！它应该会翻转模型的输出。

```python
chain.invoke("Tell me a short sentence about yourself")
```

'HELLO! MY NAME IS CLAUDE.'


