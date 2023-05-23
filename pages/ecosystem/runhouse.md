

Runhouse[#](#runhouse "跳转到这个标题的永久链接")
=====================================

本页面介绍如何在LangChain中使用[Runhouse](https://github.com/run-house/runhouse)生态系统。它分为三个部分：安装和设置、LLMs和嵌入。

安装和设置[#](#installation-and-setup "跳转到这个标题的永久链接")
------------------------------------------------

* 使用`pip install runhouse`安装Python SDK。

* 如果您想使用按需群集，请使用`sky check`检查您的云凭据。

自托管LLMs[#](#self-hosted-llms "跳转到这个标题的永久链接")
--------------------------------------------

对于基本的自托管LLM，您可以使用`SelfHostedHuggingFaceLLM`类。对于更多定制的LLM，您可以使用`SelfHostedPipeline`父类。

```
from langchain.llms import SelfHostedPipeline, SelfHostedHuggingFaceLLM

```

有关自托管LLM的更详细演练，请参见[此教程](../modules/models/llms/integrations/runhouse)

自托管嵌入[#](#self-hosted-embeddings "Permalink to this headline")
--------------------------------------------------------------

通过Runhouse，使用自托管嵌入的LangChain有几种方法。

对于来自Hugging Face Transformers模型的基本自托管嵌入，您可以使用`SelfHostedEmbedding`类。

```
from langchain.llms import SelfHostedPipeline, SelfHostedHuggingFaceLLM

```

有关自托管嵌入的更详细演练，请参见[此教程](../modules/models/text_embedding/examples/self-hosted)

