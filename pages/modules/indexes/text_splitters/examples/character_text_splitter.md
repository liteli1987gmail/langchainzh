

字符文本分割器[#](#character-text-splitter "Permalink to this headline")
=================================================================

这是一种更简单的方法。默认情况下，它基于字符（默认为“

”）进行拆分，并通过字符数来测量块长度。

- 文本如何拆分：按单个字符

- 块大小如何测量：通过传递的长度函数（默认为字符数）

```
# This is a long document we can split up.
with open('../../../state_of_the_union.txt') as f:
    state_of_the_union = f.read()

```

```
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(        
    separator = "  ",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)

```

```
texts = text_splitter.create_documents([state_of_the_union])
print(texts[0])

```

```
page_content='Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.    Last year COVID-19 kept us apart. This year we are finally together again.   Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans.   With a duty to one another to the American people to the Constitution.   And with an unwavering resolve that freedom will always triumph over tyranny.   Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated.   He thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined.   He met the Ukrainian people.   From President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.' lookup_str='' metadata={} lookup_index=0

```

这是一个将元数据与文档一起传递的示例，注意它与文档一起拆分。

```
metadatas = [{"document": 1}, {"document": 2}]
documents = text_splitter.create_documents([state_of_the_union, state_of_the_union], metadatas=metadatas)
print(documents[0])

```

```
page_content='Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.    Last year COVID-19 kept us apart. This year we are finally together again.   Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans.   With a duty to one another to the American people to the Constitution.   And with an unwavering resolve that freedom will always triumph over tyranny.   Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated.   He thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined.   He met the Ukrainian people.   From President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.' lookup_str='' metadata={'document': 1} lookup_index=0

```

