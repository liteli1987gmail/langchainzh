

OpenAI[#](#openai "跳转到此标题的链接")
==============================

本页面介绍如何在LangChain中使用OpenAI生态系统。页面分为两部分：安装和设置，以及对特定OpenAI封装程序的引用。

安装和设置[#](#installation-and-setup "跳转到此标题的链接")
---------------------------------------------

* 使用`pip install openai`安装Python SDK。

* 获取OpenAI api key并将其设置为环境变量（`OPENAI_API_KEY`）

* 如果要使用OpenAI的分词器（仅适用于Python 3.9+），请使用`pip install tiktoken`安装。

包装器[#](#wrappers "永久链接到此标题")
----------------------------

### LLM[#](#llm "永久链接到此标题")

存在一个OpenAI LLM包装器，你可以通过以下方式访问

```
from langchain.llms import OpenAI

```

如果你使用的是在Azure上托管的模型，那么你应该使用不同的包装器：

```
from langchain.llms import AzureOpenAI

```

有关Azure包装器的更详细步骤，请参见[此笔记本](../modules/models/llms/integrations/azure_openai_example)

### 嵌入[#](#embeddings "永久链接到此标题")

存在一个OpenAI嵌入包装器，你可以通过以下方式访问

```
from langchain.embeddings import OpenAIEmbeddings

```

有关此包装器的更详细步骤，请参见[此笔记本](../modules/models/text_embedding/examples/openai)

### 分词器[#](#tokenizer "永久链接到此标题")

你可以在多个地方使用 `tiktoken` 分词器。默认情况下，它用于计算OpenAI LLM的标记数。

您还可以在拆分文档时使用它来计算标记。

```
from langchain.text_splitter import CharacterTextSplitter
CharacterTextSplitter.from_tiktoken_encoder(...)

```

有关更详细的步骤，请参见[此笔记本](../modules/indexes/text_splitters/examples/tiktoken)

### 审核[#](#moderation "此标题的永久链接")

您还可以使用以下内容访问OpenAI内容审核端点

```
from langchain.chains import OpenAIModerationChain

```

有关更详细的步骤，请参见[此笔记本](../modules/chains/examples/moderation)

