

PipelineAI[#](#pipelineai "本标题的永久链接")
=====================================

本页面介绍如何在LangChain中使用PipelineAI生态系统。
它分为两部分：安装和设置，以及对特定的PipelineAI包装器的引用。

安装和设置[#](#installation-and-setup "本标题的永久链接")
--------------------------------------------

* 使用`pip install pipeline-ai`进行安装

* 获取Pipeline Cloud API密钥并将其设置为环境变量（`PIPELINE_API_KEY`）

包装器[#](#wrappers "本标题的永久链接")
----------------------------

### LLM[#](#llm "本标题的永久链接")

存在一个PipelineAI LLM包装器，你可以通过它来访问

```
from langchain.llms import PipelineAI

```
