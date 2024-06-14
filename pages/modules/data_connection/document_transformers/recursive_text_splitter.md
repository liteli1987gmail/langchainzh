# 递归按字符分割

这个文本分割器是用于一般文本的推荐方法。它是由一个字符列表参数化的。它会尝试按顺序分割它们，直到块足够小为止。默认列表是 `["\n\n", "\n", " ", ""]`。这样做的效果是尽可能保持所有段落（然后句子，然后单词）在一起，因为这些似乎是最强相关的文本语义上相关的部分。

1. 文本如何分割：由字符列表。
2. 块大小如何测量：按字符数。

```python
%pip install -qU langchain-text-splitters
```

```python
# 这是一个长文档，我们可以将其分割。
with open("../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()
```

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
```

```python
text_splitter = RecursiveCharacterTextSplitter(
    # 设置一个非常小的块大小，只是为了展示。
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)
```

```python
texts = text_splitter.create_documents([state_of_the_union])
print(texts[0])
print(texts[1])
```

    page_content='Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and'
    page_content='of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.'

```python
text_splitter.split_text(state_of_the_union)[:2]
```

['Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and',
'of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.']

```python

```

## 从没有单词边界的语言中分割文本

一些书写系统没有[单词边界](https://en.wikipedia.org/wiki/Category:Writing_systems_without_word_boundaries)，例如中文，日文和泰文。使用默认分隔符列表 `["\n\n", "\n", " ", ""]` 分割文本可能会导致单词在块之间分割。为了保持单词在一起，您可以覆盖分隔符列表以包含额外的标点符号：

* 添加 ASCII 句号 "`.`"，[Unicode全角](https://en.wikipedia.org/wiki/Halfwidth_and_Fullwidth_Forms_(Unicode_block))句号 "`．`"（用于中文文本）和[表意句号](https://en.wikipedia.org/wiki/CJK_Symbols_and_Punctuation) "`。`"（用于日文和中文）
* 添加[零宽空格](https://en.wikipedia.org/wiki/Zero-width_space) 用于泰文，缅甸文，高棉文和日文。
* 添加 ASCII 逗号 "`,`"，Unicode全角逗号 "`，`"和Unicode表意逗号 "`、`"

```python
text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        "\n\n",
        "\n",
        " ",
        ".",
        ",",
        "\u200B",  # 零宽空格
        "\uff0c",  # 全角逗号
        "\u3001",  # 表意逗号
        "\uff0e",  # 全角句号
        "\u3002",  # 表意句号
        "",
    ],
    # 现有参数
)
```

```python

```