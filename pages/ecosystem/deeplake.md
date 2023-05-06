

深湖[#](#deep-lake "本标题的永久链接")
============================

本页面介绍如何在LangChain中使用深湖生态系统。

为什么选择深湖？[#](#why-deep-lake "本标题的永久链接")
--------------------------------------

* 不仅仅是一个（多模态）向量存储。你还可以使用数据集来微调自己的LLM模型。

* 不仅存储嵌入，还有自动版本控制的原始数据。

* 真正的无服务器。不需要另一个服务，并且可以与主要的云提供商（AWS S3、GCS等）一起使用。

更多资源[#](#more-resources "本标题的永久链接")
-----------------------------------

- [LangChain & Deep Lake终极指南：构建ChatGPT以回答你的金融数据问题](https://www.activeloop.ai/resources/ultimate-guide-to-lang-chain-deep-lake-build-chat-gpt-to-answer-questions-on-your-financial-data/)

- [使用Deep Lake进行Twitter算法代码分析](../use_cases/code/twitter-the-algorithm-analysis-deeplake)

- 这里是Deep Lake的[白皮书](https://www.deeplake.ai/whitepaper)和[学术论文](https://arxiv.org/pdf/2209.10785.pdf)

- 以下是可供查看的其他资源：[Deep Lake](https://github.com/activeloopai/deeplake)，[入门指南](https://docs.activeloop.ai/getting-started)和[教程](https://docs.activeloop.ai/hub-tutorials)

安装和设置[#](#installation-and-setup "永久链接到此标题")
--------------------------------------------

* 使用 `pip install deeplake` 命令安装 Python 包

包装器[#](#wrappers "永久链接到此标题")
----------------------------

### VectorStore

Deep Lake是一个面向深度学习应用的数据湖，除了用于语义搜索和示例选择之外，还提供了一个包装器，允许您将其作为向量存储库使用。

使用如下代码导入Deep Lake的向量存储库：

```
from langchain.vectorstores import DeepLake
```

更多的详细信息和示例可以参考[这个notebook](../modules/indexes/vectorstores/examples/deeplake)。

