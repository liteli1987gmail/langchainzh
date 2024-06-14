# 按标记切分

语言模型有一个标记限制。您不应超越标记限制。所以在将文本分成块时，建议计算标记的数量。有许多分词器。在计算文本中的标记数时，应使用与语言模型中使用的相同的分词器。

## tiktoken

>[tiktoken](https://github.com/openai/tiktoken) 是由 OpenAI 创建的快速 `BPE` 分词器。


我们可以使用它估计使用的标记数。对于 OpenAI 的模型来说，可能会更准确。

1. 文本如何切分：按传入的字符切分。
2. 块大小如何测量：通过 `tiktoken` 分词器。

```python
%pip install --upgrade --quiet langchain-text-splitters tiktoken
```

```python
# 这是一个长文档，我们可以将其切分。
with open("../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()
from langchain_text_splitters import CharacterTextSplitter
```

`from_tiktoken_encoder()` 方法可以使用 `encoding`（例如 `cl100k_base`）或 `model_name`（例如 `gpt-4`）作为参数。所有额外的参数，如 `chunk_size`、`chunk_overlap` 和 `separators`，都用于实例化 `CharacterTextSplitter`：

```python
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding="cl100k_base", chunk_size=100, chunk_overlap=0
)
texts = text_splitter.split_text(state_of_the_union)
```

```python
print(texts[0])
```

    Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  
    
    Last year COVID-19 kept us apart. This year we are finally together again. 
    
    Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. 
    
    With a duty to one another to the American people to the Constitution.

注意，如果使用 `CharacterTextSplitter.from_tiktoken_encoder`，文本仅由 `CharacterTextSplitter` 切分，并使用 `tiktoken` 分词器合并切分。这意味着切分可以比 `tiktoken` 分词器测量的块大小更大。我们可以使用 `RecursiveCharacterTextSplitter.from_tiktoken_encoder` 来确保切分不会超过语言模型允许的块大小，其中每个切分将递归地进行切分（如果它的大小更大）：

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    model_name="gpt-4",
    chunk_size=100,
    chunk_overlap=0,
)
```

我们还可以直接加载一个 tiktoken 分词器，以确保每个切分小于块大小。

```python
from langchain_text_splitters import TokenTextSplitter

text_splitter = TokenTextSplitter(chunk_size=10, chunk_overlap=0)

texts = text_splitter.split_text(state_of_the_union)
print(texts[0])
```

某些书面语言（例如中文和日文）具有将字符编码为2个或多个标记的字符。直接使用 `TokenTextSplitter` 可能会将一个字符的标记分隔在两个块之间，导致不正常的 Unicode 字符。请使用 `RecursiveCharacterTextSplitter.from_tiktoken_encoder` 或 `CharacterTextSplitter.from_tiktoken_encoder`，以确保块包含有效的 Unicode 字符串。

## spaCy

>[spaCy](https://spacy.io/) 是用 Python 和 Cython 编写的高级自然语言处理开源软件库。

除了 `NLTK`，使用 [spaCy 分词器](https://spacy.io/api/tokenizer) 是另一种选择。

1. 文本如何切分：通过 `spaCy` 分词器切分。
2. 块大小如何测量：通过字符数。

```python
%pip install --upgrade --quiet  spacy
```

```python
# 这是一个长文档，我们可以将其切分。
with open("../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()
```

```python
from langchain_text_splitters import SpacyTextSplitter

text_splitter = SpacyTextSplitter(chunk_size=1000)
```

```python
texts = text_splitter.split_text(state_of_the_union)
print(texts[0])
```

    Madam Speaker, Madam Vice President, our First Lady and Second Gentleman.
    
    Members of Congress and the Cabinet.
    
    Justices of the Supreme Court.
    
    My fellow Americans.  
    
    
    
    Last year COVID-19 kept us apart.
    
    This year we are finally together again. 
    
    
    
    Tonight, we meet as Democrats Republicans and Independents.
    
    But most importantly as Americans. 
    
    
    
    With a duty to one another to the American people to the Constitution. 
    
    
    
    And with an unwavering resolve that freedom will always triumph over tyranny. 
    
    
    
    Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways.
    
    But he badly miscalculated. 
    
    
    
    He thought he could roll into Ukraine and the world would roll over.
    
    Instead he met a wall of strength he never imagined. 
    
    
    
    He met the Ukrainian people. 
    
    
    
    From President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.

## SentenceTransformers

`SentenceTransformersTokenTextSplitter` 是专为句子转换模型设计的文本分割器。默认行为是将文本分成适合您希望使用的句子转换模型的标记窗口的块。

```python
from langchain_text_splitters import SentenceTransformersTokenTextSplitter
```

```python
splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=0)
text = "Lorem "
```

```python
count_start_and_stop_tokens = 2
text_token_count = splitter.count_tokens(text=text) - count_start_and_stop_tokens
print(text_token_count)
```

    2

```python
token_multiplier = splitter.maximum_tokens_per_chunk // text_token_count + 1

# `text_to_split` 无法适应单个块
text_to_split = text * token_multiplier

print(f"tokens in text to split: {splitter.count_tokens(text=text_to_split)}")
```

    tokens in text to split: 514

```python
text_chunks = splitter.split_text(text=text_to_split)

print(text_chunks[1])
```

    lorem






## 自然语言处理工具包

>[自然语言处理工具包（Natural Language Toolkit）](https://en.wikipedia.org/wiki/Natural_Language_Toolkit)（通常简称为[NLTK](https://www.nltk.org/)）是一套用于英文符号和统计自然语言处理（NLP）的库和程序，使用Python编程语言编写。

与仅在"\n\n"上拆分不同，我们可以使用`NLTK`基于[NLTK标记器](https://www.nltk.org/api/nltk.tokenize.html)进行分割。

1. 文本如何拆分：通过`NLTK`标记器。
2. 如何测量块大小：通过字符数。

```python
# pip install nltk
```

```python
# 这是一篇长篇文档，我们可以拆分。
with open("../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()
```

```python
from langchain_text_splitters import NLTKTextSplitter

text_splitter = NLTKTextSplitter(chunk_size=1000)
```

```python
texts = text_splitter.split_text(state_of_the_union)
print(texts[0])
```

    Madam Speaker, Madam Vice President, our First Lady and Second Gentleman.
    
    Members of Congress and the Cabinet.
    
    Justices of the Supreme Court.
    
    My fellow Americans.
    
    Last year COVID-19 kept us apart.
    
    This year we are finally together again.
    
    Tonight, we meet as Democrats Republicans and Independents.
    
    But most importantly as Americans.
    
    With a duty to one another to the American people to the Constitution.
    
    And with an unwavering resolve that freedom will always triumph over tyranny.
    
    Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways.
    
    But he badly miscalculated.
    
    He thought he could roll into Ukraine and the world would roll over.
    
    Instead he met a wall of strength he never imagined.
    
    He met the Ukrainian people.
    
    From President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.
    
    Groups of citizens blocking tanks with their bodies.

## KoNLPY

> [KoNLPy：Python中的韩语NLP](https://konlpy.org/en/latest/)是用于韩语自然语言处理（NLP）的Python包。

标记分割涉及将文本分割成更小、更易处理的单元（称为标记）。这些标记通常是单词、短语、符号或其他进一步处理和分析所必需的有意义元素。在英语等语言中，标记分割通常涉及通过空格和标点符号分隔单词。标记分割的效果在很大程度上取决于标记器对语言结构的理解，确保生成有意义的标记。由于为英语设计的标记器无法理解韩语等其他语言的独特语义结构，因此无法有效用于韩语处理。

### 通过KoNLPy的Kkma分析器进行韩语标记划分
就韩语文本而言，KoNLPY包含一个称为`Kkma`的形态分析器（韩语知识形态分析器）。`Kkma`提供对韩语文本的详细形态分析。它将句子分解为单词，并将单词分解为各自的语素，识别每个标记的词性。它可以将一块文本段落分割为单独的句子，对处理长篇文本特别有用。

### 使用注意事项
虽然`Kkma`以其详细分析而闻名，但值得注意的是，这种精确性可能会影响处理速度。因此，`Kkma`最适合于将分析深度放在文本处理之上的应用程序。

```python
# pip install konlpy
```

```python
# 这是一篇很长的韩文文档，我们想将其分割成其组成句子。
with open("./your_korean_doc.txt") as f:
    korean_document = f.read()
```

```python
from langchain_text_splitters import KonlpyTextSplitter

text_splitter = KonlpyTextSplitter()
```

```python
texts = text_splitter.split_text(korean_document)
# 句子通过"\n\n"字符分割。
print(texts[0])
```

    춘향전 옛날에 남원에 이 도령이라는 벼슬아치 아들이 있었다.
    
    그의 외모는 빛나는 달처럼 잘생겼고, 그의 학식과 기예는 남보다 뛰어났다.
    
    한편, 이 마을에는 춘향이라는 절세 가인이 살고 있었다.
    
    춘 향의 아름다움은 꽃과 같아 마을 사람들 로부터 많은 사랑을 받았다.
    
    어느 봄날, 도령은 친구들과 놀러 나갔다가 춘 향을 만 나 첫 눈에 반하고 말았다.
    
    두 사람은 서로 사랑하게 되었고, 이내 비밀스러운 사랑의 맹세를 나누었다.
    
    하지만 좋은 날들은 오래가지 않았다.
    
    도령의 아버지가 다른 곳으로 전근을 가게 되어 도령도 떠나 야만 했다.
    
    이별의 아픔 속에서도, 두 사람은 재회를 기약하며 서로를 믿고 기다리기로 했다.
    
    그러나 새로 부임한 관아의 사또가 춘 향의 아름다움에 욕심을 내 어 그녀에게 강요를 시작했다.
    
    춘 향 은 도령에 대한 자신의 사랑을 지키기 위해, 사또의 요구를 단호히 거절했다.
    
    이에 분노한 사또는 춘 향을 감옥에 가두고 혹독한 형벌을 내렸다.
    
    이야기는 이 도령이 고위 관직에 오른 후, 춘 향을 구해 내는 것으로 끝난다.
    
    두 사람은 오랜 시련 끝에 다시 만나게 되고, 그들의 사랑은 온 세상에 전해 지며 후세에까지 이어진다.
    
    - 춘향전（The Tale of Chunhyang）

## Hugging Face标记器

>[Hugging Face](https://huggingface.co/docs/tokenizers/index)拥有许多标记器。

我们使用Hugging Face标记器，[GPT2TokenizerFast](https://huggingface.co/Ransaka/gpt2-tokenizer-fast)来计算标记长度。

1. 如何拆分文本：通过传入的字符。
2. 如何测量块大小：通过`Hugging Face`标记器计算的标记数。

```python
from transformers import GPT2TokenizerFast

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
```

```python
# 这是一篇长篇文档，我们可以拆分。
with open("../../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()
from langchain_text_splitters import CharacterTextSplitter
```

```python
text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(
    tokenizer, chunk_size=100, chunk_overlap=0
)
texts = text_splitter.split_text(state_of_the_union)
```

```python
print(texts[0])
```

    Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  
    
    Last year COVID-19 kept us apart. This year we are finally together again. 
    
    Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. 
    
    With a duty to one another to the American people to the Constitution.

```python

```