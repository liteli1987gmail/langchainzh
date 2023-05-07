

入门指南[#](#getting-started "永久链接到本标题")
====================================

默认推荐的文本分割器是 RecursiveCharacterTextSplitter。该文本分割器需要一个字符列表。它尝试根据第一个字符分割创建块，但如果任何块太大，则移动到下一个字符，依此类推。默认情况下，它尝试分割的字符是`["  ", "\n", " ", ""]`

除了控制可以分割的字符之外，您还可以控制其他一些内容：

* `length_function`: 如何计算块的长度。默认情况下只计算字符数，但通常在此处传递令牌计数器。

* `chunk_size`: 块的最大大小（由长度函数测量）。

* `chunk_overlap`: the maximum overlap between chunks. It can be nice to have some overlap to maintain some continuity between chunks (eg do a sliding window).

```
# This is a long document we can split up.
with open('../../state_of_the_union.txt') as f:
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

