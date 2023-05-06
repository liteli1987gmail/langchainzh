

Jina[#](#jina "跳到此标题的永久链接")
===========================

本页面介绍如何在LangChain中使用Jina生态系统。分为两部分:安装和设置,以及特定Jina包装器的参考。

安装和设置[#](#installation-and-setup "跳到此标题的永久链接")
----------------------------------------------

* 使用`pip install jina`安装Python SDK

* 从[这里](https://cloud.jina.ai/settings/tokens)获取Jina AI Cloud授权令牌，并将其设置为环境变量(`JINA_AUTH_TOKEN`)

包装器[#](#wrappers "跳到此标题的永久链接")
------------------------------

### 嵌入[#](#embeddings "跳到此标题的永久链接")

There exists a Jina Embeddings wrapper, which you can access with

```
from langchain.embeddings import JinaEmbeddings

```

For a more detailed walkthrough of this, see [this notebook](../modules/models/text_embedding/examples/jina)

