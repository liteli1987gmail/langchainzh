

TiktokenText 分割器[#](#tiktokentext-splitter "永久链接至本标题")
======================================================

- 文本如何分割：按照 `tiktoken` 标记分割

- 块大小如何测量：按照 `tiktoken` 标记计算

```
# This is a long document we can split up.
with open('../../../state_of_the_union.txt') as f:
    state_of_the_union = f.read()

```

```
from langchain.text_splitter import TokenTextSplitter

```

```
text_splitter = TokenTextSplitter(chunk_size=10, chunk_overlap=0)

```

```
texts = text_splitter.split_text(state_of_the_union)
print(texts[0])

```

```
Madam Speaker, Madam Vice President, our

```

