# 处理文件 (Handle Files)

除了原始文本数据之外，您可能还希望从其他文件类型（如PowerPoint演示文稿或PDF文件）中提取信息。

您可以使用LangChain [文档加载器](/modules/data_connection/document_loaders/) 将文件解析为可以输入到LLM中的文本格式。

LangChain提供了大量的[文档加载器集成](/docs/integrations/document_loaders)。

## 基于MIME类型的解析

有关基本解析示例，请查看[文档加载器](/modules/data_connection/document_loaders/)。

在这里，我们将查看基于MIME类型的解析，这对于抽取应用程序非常有用，特别是当您正在编写接受用户上传文件的服务器代码时，但用户提供的文件后缀可能错误，因此最好从文件的二进制内容中推断MIME类型。

让我们下载一些内容。这将是一个HTML文件，但下面的代码也适用于其他文件类型。

```python
import requests

response = requests.get("https://en.wikipedia.org/wiki/Car")
data = response.content
data[:20]
```

配置解析器

```python
import magic
from langchain.document_loaders.parsers import BS4HTMLParser, PDFMinerParser
from langchain.document_loaders.parsers.generic import MimeTypeBasedParser
from langchain.document_loaders.parsers.txt import TextParser
from langchain_community.document_loaders import Blob

# 配置您想要根据MIME类型使用的解析器！
HANDLERS = {
    "application/pdf": PDFMinerParser(),
    "text/plain": TextParser(),
    "text/html": BS4HTMLParser(),
}

# 使用给定的解析器实例化基于MIME类型的解析器
MIMETYPE_BASED_PARSER = MimeTypeBasedParser(
    handlers=HANDLERS,
    fallback_parser=None,
)

mime = magic.Magic(mime=True)
mime_type = mime.from_buffer(data)

# 一个Blob代表二进制数据，可通过引用（文件系统上的路径）或值（内存中的字节）来表示。
blob = Blob.from_data(
    data=data,
    mime_type=mime_type,
)

parser = HANDLERS[mime_type]
documents = parser.parse(blob=blob)
```

```python
print(documents[0].page_content[:30].strip())
```

Car - Wikipedia