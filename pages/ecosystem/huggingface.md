

拥抱面孔[#](#hugging-face "此标题的永久链接")
=================================

本页面介绍如何在LangChain中使用拥抱面孔生态系统（包括[拥抱面孔中心](https://huggingface.co))。  
它分为两个部分：安装和设置，然后是特定的拥抱面孔包装器的引用。

安装和设置[#](#installation-and-setup "此标题的永久链接")
--------------------------------------------

如果您想使用拥抱面孔中心：

* 使用`pip install huggingface_hub`安装中心客户端库

* 创建一个拥抱面孔账户（免费！)

* 创建一个[访问令牌](https://huggingface.co/docs/hub/security-tokens)并将其设置为环境变量（`HUGGINGFACEHUB_API_TOKEN`)

如果您想使用Hugging Face Python库进行工作：

* 安装`pip install transformers`以使用模型和分词器

* 安装`pip install datasets`以使用数据集

Wrappers[#](#wrappers "Permalink to this headline")
---------------------------------------------------

### LLM[#](#llm "Permalink to this headline")

存在两个Hugging Face LLM包装器，一个用于本地管道，另一个用于托管在Hugging Face Hub上的模型。
请注意，这些包装器仅适用于支持以下任务的模型：[`text2text-generation`](https://huggingface.co/models?library=transformers&pipeline_tag=text2text-generation&sort=downloads)，[`text-generation`](https://huggingface.co/models?library=transformers&pipeline_tag=text-classification&sort=downloads)

使用本地管道包装器：

```
from langchain.llms import HuggingFacePipeline

```

使用Hugging Face Hub上托管的模型的包装器：

```
from langchain.llms import HuggingFaceHub

```

有关Hugging Face Hub包装器的更详细演练，请参见[这个notebook](../modules/models/llms/integrations/huggingface_hub)

### 嵌入[#](#embeddings "Permalink to this headline")

有两个Hugging Face嵌入包装器，一个用于本地模型，一个用于Hugging Face Hub上托管的模型。
请注意，这些包装器仅适用于[`sentence-transformers`模型](https://huggingface.co/models?library=sentence-transformers&sort=downloads)。

要使用本地管道包装器：

```
from langchain.embeddings import HuggingFaceEmbeddings

```

要使用Hugging Face Hub上托管的模型的包装器：

```
from langchain.embeddings import HuggingFaceHubEmbeddings

```

有关更详细的操作说明，请参见[此笔记本电脑](../modules/models/text_embedding/examples/huggingfacehub)

### 分词器[#](#tokenizer "Permalink to this headline")

您可以通过`transformers`包中提供的几个地方使用标记器。
默认情况下，它用于计算所有LLM的标记数。

您还可以在拆分文档时使用它来计算标记数

```
from langchain.text_splitter import CharacterTextSplitter
CharacterTextSplitter.from_huggingface_tokenizer(...)

```

有关更详细的操作说明，请参见[此笔记本电脑](../modules/indexes/text_splitters/examples/huggingface_length_function)

### 数据集[#](#datasets "Permalink to this headline")

Hugging Face Hub有很多非常好的[数据集](https://huggingface.co/datasets)，可以用来评估您的LLM链。

关于如何使用它们进行评估的详细步骤，请参见这个notebook

