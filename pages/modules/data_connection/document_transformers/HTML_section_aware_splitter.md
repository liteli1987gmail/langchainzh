# 按HTML部分分割

## 描述和动机
与[HTMLHeaderTextSplitter](/modules/data_connection/document_transformers/HTML_header_metadata)的概念类似，`HTMLSectionSplitter`是一个“结构感知”的分块器，它在元素级别上分割文本，并为每个标题添加元数据，有助于将相关文本（或多或少）语义地分组，并在文档结构中保留上下文丰富的信息编码。它可以与其他文本分割器一起使用，作为分块流水线的一部分。在段大小大于块大小时，它使用`RecursiveCharacterTextSplitter`。它还考虑文本的字体大小，以确定是否根据确定的字体大小阈值将其划分为段落。使用`xslt_path`提供HTML的绝对路径，以便根据提供的标签检测段落。默认情况下，使用`data_connection/document_transformers`目录中的`converting_to_header.xslt`文件。这是为了将HTML转换为更容易检测段落的格式/布局。例如，可以根据它们的字体大小将`span`转换为标题标签以便检测为段落。

## 使用示例
#### 1）使用HTML字符串：

```python
from langchain_text_splitters import HTMLSectionSplitter

html_string = """
    <!DOCTYPE html>
    <html>
    <body>
        <div>
            <h1>Foo</h1>
            <p>关于Foo的一些简介文字。</p>
            <div>
                <h2>主要部分Bar</h2>
                <p>关于Bar的一些简介文字。</p>
                <h3>Bar子部分1</h3>
                <p>关于Bar的第一个子主题的一些文字。</p>
                <h3>Bar子部分2</h3>
                <p>关于Bar的第二个子主题的一些文字。</p>
            </div>
            <div>
                <h2>Baz</h2>
                <p>关于Baz的一些文字。</p>
            </div>
            <br>
            <p>关于Foo的一些结论性文字。</p>
        </div>
    </body>
    </html>
"""

headers_to_split_on = [("h1", "标题 1"), ("h2", "标题 2")]

html_splitter = HTMLSectionSplitter(headers_to_split_on=headers_to_split_on)
html_header_splits = html_splitter.split_text(html_string)
html_header_splits
```

#### 2）管道连接到另一个分割器，从HTML字符串内容加载HTML：

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

html_string = """
    <!DOCTYPE html>
    <html>
    <body>
        <div>
            <h1>Foo</h1>
            <p>关于Foo的一些简介文字。</p>
            <div>
                <h2>主要部分Bar</h2>
                <p>关于Bar的一些简介文字。</p>
                <h3>Bar子部分1</h3>
                <p>关于Bar的第一个子主题的一些文字。</p>
                <h3>Bar子部分2</h3>
                <p>关于Bar的第二个子主题的一些文字。</p>
            </div>
            <div>
                <h2>Baz</h2>
                <p>关于Baz的一些文字。</p>
            </div>
            <br>
            <p>关于Foo的一些结论性文字。</p>
        </div>
    </body>
    </html>
"""

headers_to_split_on = [
    ("h1", "标题 1"),
    ("h2", "标题 2"),
    ("h3", "标题 3"),
    ("h4", "标题 4"),
]

html_splitter = HTMLSectionSplitter(headers_to_split_on=headers_to_split_on)

html_header_splits = html_splitter.split_text(html_string)

chunk_size = 500
chunk_overlap = 30
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap
)

# 分割
splits = text_splitter.split_documents(html_header_splits)
splits

```
------
