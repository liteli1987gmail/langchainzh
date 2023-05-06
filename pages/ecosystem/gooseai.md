

GooseAI[#](#gooseai "Permalink to this headline")
=================================================


该页面介绍了如何在LangChain中使用GooseAI生态系统。分为两个部分：安装和设置，以及指向特定GooseAI包装器的参考。

安装和设置[#](#installation-and-setup "Permalink to this headline")
-------------------------------------------------------------------------------

以下是使用GooseAI的步骤：

* 使用 `pip install gooseai` 安装Python SDK。
* 从这个链接 [here](https://goose.ai/) 获取您的GooseAI API密钥。
* 设置环境变量 (`GOOSEAI_API_KEY`)。

```
import os
os.environ["GOOSEAI_API_KEY"] = "YOUR_API_KEY"

```

包装器[#](#wrappers "Permalink to this headline")
---------------------------------------------------

### LLM[#](#llm "Permalink to this headline")

GooseAI LLM包装器可以通过以下代码进行访问：

```
from langchain.llms import GooseAI

```

