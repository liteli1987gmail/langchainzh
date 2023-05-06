

CoNLL-U[#](#conll-u "这个标题的永久链接")
================================

> 
> [CoNLL-U](https://universaldependencies.org/format)是CoNLL-X格式的修订版本。注释以纯文本文件的形式进行编码（UTF-8，规范为NFC，仅使用LF字符作为换行符，包括文件末尾的LF字符），其中包含三种类型的行：
> 
> 
> * 单词行包含10个字段的单词/标记注释，由单个制表符分隔；请参见下文。
> 
> * 空行标记句子边界。
> 
> * 以井号（＃）开头的注释行。
> 
> 
> 

这是如何在[CoNLL-U](https://universaldependencies.org/format)格式中加载文件的示例。整个文件被视为一个文档。示例数据（`conllu.conllu`）基于标准UD / CoNLL-U示例之一。

```
from langchain.document_loaders import CoNLLULoader

```

```
loader = CoNLLULoader("example_data/conllu.conllu")

```

```
document = loader.load()

```

```
document

```

```
[Document(page_content='They buy and sell books.', metadata={'source': 'example_data/conllu.conllu'})]

```

