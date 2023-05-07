

递归字符文本分割器[#](#recursivecharactertextsplitter "此标题的永久链接")
========================================================

此文本分割器是通用文本的推荐分割器。它由字符列表参数化。它尝试按顺序在它们上进行分割，直到块足够小。默认列表为`["  ", "\n", " ", ""]`。这样做的效果是尽可能地保持所有段落（然后是句子，然后是单词)在一起，因为它们通常看起来是最强的语义相关的文本片段。

- 文本如何分割：通过字符列表

- 如何测量块大小：通过传递的长度函数（默认为字符数)

```
# This is a long document we can split up.
with open('../../../state_of_the_union.txt') as f:
    state_of_the_union = f.read()

```

```
from langchain.text_splitter import RecursiveCharacterTextSplitter

```

```
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 100,
    chunk_overlap  = 20,
    length_function = len,
)

```

```
texts = text_splitter.create_documents([state_of_the_union])
print(texts[0])
print(texts[1])

```

```
page_content='Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and' lookup_str='' metadata={} lookup_index=0
page_content='of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.' lookup_str='' metadata={} lookup_index=0

```

