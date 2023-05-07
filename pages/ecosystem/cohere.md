

连贯性[#](#cohere "永久链结到这个标题")
===========================

本页面介绍如何在LangChain中使用Cohere生态系统。 它分为两个部分：安装和设置，以及对特定Cohere包装器的引用。

安装和设置[#](#installation-and-setup "永久链结到这个标题")
---------------------------------------------

* 使用`pip install cohere`安装Python SDK。

* 获取Cohere API密钥并将其设置为环境变量（`COHERE_API_KEY`)

包装器[#](#wrappers "永久链结到这个标题")
-----------------------------

### LLM[#](#llm "永久链结到这个标题")

存在一个Cohere LLM包装器，您可以使用它来访问

```
from langchain.llms import Cohere

```

### 嵌入[#](#embeddings "永久链结到这个标题")

Cohere Embeddings库提供了一个便于使用的包装器，您可以使用如下代码进行访问：

```
from langchain.embeddings import CohereEmbeddings
```

更多的详细信息以及演示可以参考[这个notebook](../modules/models/text_embedding/examples/cohere)。

