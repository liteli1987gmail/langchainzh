

拥抱面部长度函数[#](#hugging-face-length-function "Permalink to this headline")
=======================================================================

大多数LLM受到可以传递的令牌数量的限制，这与字符数不同。为了获得更准确的估计，我们可以使用Hugging Face令牌化器来计算文本长度。

- 文本如何分割：按传入的字符

- 块大小如何测量：通过Hugging Face令牌化器

```
from transformers import GPT2TokenizerFast

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

```

```
# This is a long document we can split up.
with open('../../../state_of_the_union.txt') as f:
    state_of_the_union = f.read()
from langchain.text_splitter import CharacterTextSplitter

```

```
text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(tokenizer, chunk_size=100, chunk_overlap=0)
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

