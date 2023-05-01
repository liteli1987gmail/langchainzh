


文字分割器
===================================================================

[Conceptual Guide](https://docs.langchain.com/docs/components/indexing/text-splitter) 




当您想要处理较长的文本时，有必要将该文本分成若干小块。尽管这听起来很简单，但这里存在许多潜在的复杂性。理想情况下，您希望将语义相关的文本片段放在一起。“语义相关”的含义取决于文本的类型。这本笔记本展示了几种实现这一目标的方法。

在高级别上，文本分割器的工作原理如下:

把文本分成小块，语义上有意义的块(通常是句子)。

开始将这些小块组合成一个更大的块，直到达到一定的大小(通过某个函数衡量)。

一旦你达到了这个大小，让这个块成为它自己的文本块，然后开始创建一个有一些重叠的新文本块(保持块之间的上下文)。

这意味着有两个不同的轴，可以沿着它们自定义文本分割器:

1. 文本是如何分割的

2. 块大小是如何度量的

有关默认文本分割器和通用功能的介绍，请参见:
 



* [Getting Started](text_splitters/getting_started)




我们还提供了支持的所有类型的文本分割器的文档。请参阅下面的列表。
 



* [Character Text Splitter](text_splitters/examples/character_text_splitter)
* [Hugging Face Length Function](text_splitters/examples/huggingface_length_function)
* [Latex Text Splitter](text_splitters/examples/latex)
* [Markdown Text Splitter](text_splitters/examples/markdown)
* [NLTK Text Splitter](text_splitters/examples/nltk)
* [Python Code Text Splitter](text_splitters/examples/python)
* [RecursiveCharacterTextSplitter](text_splitters/examples/recursive_text_splitter)
* [Spacy Text Splitter](text_splitters/examples/spacy)
* [tiktoken (OpenAI) Length Function](text_splitters/examples/tiktoken)
* [TiktokenText Splitter](text_splitters/examples/tiktoken_splitter)





