PromptLayer
============================================================

`PromptLayer`是第一个允许您跟踪、管理和共享GPT提示工程的平台。`PromptLayer`充当您的代码和`OpenAI Python`库之间的中间件。

`PromptLayer`记录所有您的`OpenAI API`请求，允许您在`PromptLayer`仪表板中搜索和探索请求历史记录。

此示例演示了如何连接到[PromptLayer]（https://www.promptlayer.com)，以开始记录您的OpenAI请求。

另一个示例在[这里]（https://python.langchain.com/en/latest/ecosystem/promptlayer.html) 。

Install PromptLayer[#](#install-promptlayer "Permalink to this headline")
-------------------------------------------------------------------------

The `promptlayer` package is required to use PromptLayer with OpenAI. Install `promptlayer` using pip.

```
!pip install promptlayer

```

Imports[#](#imports "Permalink to this headline")
-------------------------------------------------

```
import os
from langchain.llms import PromptLayerOpenAI
import promptlayer

```

Set the Environment API Key[#](#set-the-environment-api-key "Permalink to this headline")
-----------------------------------------------------------------------------------------

You can create a PromptLayer API Key at [www.promptlayer.com](https://www.promptlayer.com) by clicking the settings cog in the navbar.

Set it as an environment variable called `PROMPTLAYER_API_KEY`.

You also need an OpenAI Key, called `OPENAI_API_KEY`.

```
from getpass import getpass

PROMPTLAYER_API_KEY = getpass()

```

```
os.environ["PROMPTLAYER_API_KEY"] = PROMPTLAYER_API_KEY

```

```
from getpass import getpass

OPENAI_API_KEY = getpass()

```

```
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

```

Use the PromptLayerOpenAI LLM like normal[#](#use-the-promptlayeropenai-llm-like-normal "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------

*You can optionally pass in `pl_tags` to track your requests with PromptLayer’s tagging feature.*

```
llm = PromptLayerOpenAI(pl_tags=["langchain"])
llm("I am a cat and I want")

```

**The above request should now appear on your [PromptLayer dashboard](https://www.promptlayer.com).**

Using PromptLayer Track[#](#using-promptlayer-track "Permalink to this headline")
---------------------------------------------------------------------------------

If you would like to use any of the [PromptLayer tracking features](https://magniv.notion.site/Track-4deee1b1f7a34c1680d085f82567dab9), you need to pass the argument `return_pl_id` when instantializing the PromptLayer LLM to get the request id.

```
llm = PromptLayerOpenAI(return_pl_id=True)
llm_results = llm.generate(["Tell me a joke"])

for res in llm_results.generations:
    pl_request_id = res[0].generation_info["pl_request_id"]
    promptlayer.track.score(request_id=pl_request_id, score=100)

```

Using this allows you to track the performance of your model in the PromptLayer dashboard. If you are using a prompt template, you can attach a template to a request as well.
Overall, this gives you the opportunity to track the performance of different templates and models in the PromptLayer dashboard.

