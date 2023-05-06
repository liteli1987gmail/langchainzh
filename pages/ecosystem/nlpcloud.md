

NLPCloud[#](#nlpcloud "此标题的永久链接")
=================================

本页面介绍如何在LangChain中使用NLPCloud生态系统。  
它分为两个部分：安装和设置，以及对特定NLPCloud包装器的引用。

安装和设置[#](#installation-and-setup "此标题的永久链接")
--------------------------------------------

* 使用`pip install nlpcloud`安装Python SDK

* 获取一个NLPCloud API密钥，并将其设置为环境变量（`NLPCLOUD_API_KEY`）

包装器[#](#wrappers "此标题的永久链接")
----------------------------

### LLM[#](#llm "此标题的永久链接")

存在一个NLPCloud LLM包装器，您可以使用以下方式访问它

```
from langchain.llms import NLPCloud

```

