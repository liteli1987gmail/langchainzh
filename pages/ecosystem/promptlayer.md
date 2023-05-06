

提示层[#](#promptlayer "跳转到这个标题的永久链接")
===================================

本页面介绍如何在LangChain中使用[PromptLayer](https://www.promptlayer.com)。分为两个部分：安装和设置，以及特定的PromptLayer包装器的参考。

安装和设置[#](#installation-and-setup "跳转到这个标题的永久链接")
------------------------------------------------

如果您想使用PromptLayer：

* 安装promptlayer python库`pip install promptlayer`

* 创建PromptLayer账号

* 创建API token，并将其设置为环境变量(`PROMPTLAYER_API_KEY`)

包装器[#](#wrappers "跳转到这个标题的永久链接")
--------------------------------

### LLM[#](#llm "Permalink to this headline")

存在一个PromptLayer的OpenAI LLM包装器，可以使用以下方式访问

```
from langchain.llms import PromptLayerOpenAI

```

在实例化LLM时，可以使用`pl_tags`参数来标记您的请求

```
from langchain.llms import PromptLayerOpenAI
llm = PromptLayerOpenAI(pl_tags=["langchain-requests", "chatbot"])

```

在实例化LLM时，可以使用`return_pl_id`参数来获取PromptLayer请求id

```
from langchain.llms import PromptLayerOpenAI
llm = PromptLayerOpenAI(return_pl_id=True)

```

这将在使用`.generate`或`.agenerate`生成文本时，将PromptLayer请求ID添加到`Generation`的`generation_info`字段中进行返回

例如：

```
llm_results = llm.generate(["hello world"])
for res in llm_results.generations:
    print("pl request id: ", res[0].generation_info["pl_request_id"])

```

您可以使用PromptLayer请求ID将提示、分数或其他元数据添加到您的请求中。[在此处阅读更多信息](https://magniv.notion.site/Track-4deee1b1f7a34c1680d085f82567dab9)

这个LLM与OpenAI LLM完全相同，除了

* 所有的请求都将记录到您的PromptLayer账户中

* 当实例化时，您可以添加`pl_tags`来对PromptLayer上的请求进行标记

* 当实例化时，您可以添加`return_pl_id`来返回PromptLayer请求ID，以便[跟踪请求](https://magniv.notion.site/Track-4deee1b1f7a34c1680d085f82567dab9)。

PromptLayer还提供了本地包装器，用于[`PromptLayerChatOpenAI`](../modules/models/chat/integrations/promptlayer_chatopenai)和`PromptLayerOpenAIChat`

