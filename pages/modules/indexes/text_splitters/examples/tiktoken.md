

tiktoken (OpenAI) 长度函数[#](#tiktoken-openai-length-function "永久链接到此标题")
======================================================================

您还可以使用tiktoken，这是OpenAI的一个开源分词器包，以估计使用的令牌。对于他们的模型可能更准确。

- 文本如何拆分：通过传入的字符

- 块大小如何测量：通过`tiktoken`分词器

```
# This is a long document we can split up.
with open('../../../state_of_the_union.txt') as f:
    state_of_the_union = f.read()
from langchain.text_splitter import CharacterTextSplitter

```

```
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_text(state_of_the_union)

```

```
print(texts[0])

```

```
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  

Last year COVID-19 kept us apart. This year we are finally together again. 

Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. 

With a duty to one another to the American people to the Constitution.

```

