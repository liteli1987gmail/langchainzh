

Markdown文本分割器[#](#markdown-text-splitter "此标题的永久链接")
====================================================

MarkdownTextSplitter将文本沿Markdown标题、代码块或水平线分割。它是递归字符分割器的简单子类，具有Markdown特定的分隔符。默认情况下，查看源代码以查看Markdown语法。

- 文本如何拆分：按照Markdown特定字符列表拆分

- 如何测量块大小：通过传递的长度函数测量（默认为字符数)

```
from langchain.text_splitter import MarkdownTextSplitter

```

```
markdown_text = """
# 🦜️🔗 LangChain

⚡ Building applications with LLMs through composability ⚡

## Quick Install

```bash
# Hopefully this code block isn't split
pip install langchain
```

As an open source project in a rapidly developing field, we are extremely open to contributions.
"""
markdown_splitter = MarkdownTextSplitter(chunk_size=100, chunk_overlap=0)

```

```
docs = markdown_splitter.create_documents([markdown_text])

```

```
docs

```

```
[Document(page_content='# 🦜️🔗 LangChain  ⚡ Building applications with LLMs through composability ⚡', lookup_str='', metadata={}, lookup_index=0),
 Document(page_content="Quick Install  ```bash\n# Hopefully this code block isn't split\npip install langchain", lookup_str='', metadata={}, lookup_index=0),
 Document(page_content='As an open source project in a rapidly developing field, we are extremely open to contributions.', lookup_str='', metadata={}, lookup_index=0)]

```

