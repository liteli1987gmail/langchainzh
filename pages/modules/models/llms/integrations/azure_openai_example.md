

Azure OpenAI[#](#azure-openai "此标题的永久链接")
=========================================

本文介绍如何在[Azure OpenAI](https://aka.ms/azure-openai)上使用Langchain。

Azure OpenAI API与OpenAI API兼容。使用`openai` Python包可以轻松使用OpenAI和Azure OpenAI。你可以像调用OpenAI一样调用Azure OpenAI，但有以下例外。

API配置[#](#api-configuration "此标题的永久链接")
---------------------------------------

你可以通过环境变量配置`openai`包使用Azure OpenAI。下面是`bash`的示例：

```
# Set this to `azure`
export OPENAI_API_TYPE=azure
# The API version you want to use: set this to `2022-12-01` for the released version.
export OPENAI_API_VERSION=2022-12-01
# The base URL for your Azure OpenAI resource. You can find this in the Azure portal under your Azure OpenAI resource.
export OPENAI_API_BASE=https://your-resource-name.openai.azure.com
# The API key for your Azure OpenAI resource. You can find this in the Azure portal under your Azure OpenAI resource.
export OPENAI_API_KEY=<your Azure OpenAI API key>

```

或者，你可以在运行的Python环境中直接配置API：

```
import os
os.environ["OPENAI_API_TYPE"] = "azure"
...

```

部署[#](#deployments "此标题的永久链接")
------------------------------

使用Azure OpenAI，你可以设置自己的GPT-3和Codex模型的部署。调用API时，你需要指定要使用的部署。

假设你的部署名称是`text-davinci-002-prod`。在`openai` Python API中，您可以使用`engine`参数指定此部署。例如：

```
import openai

response = openai.Completion.create(
    engine="text-davinci-002-prod",
    prompt="This is a test",
    max_tokens=5
)

```

```
!pip install openai

```

```
# Import Azure OpenAI
from langchain.llms import AzureOpenAI

```

```
# Create an instance of Azure OpenAI
# Replace the deployment name with your own
llm = AzureOpenAI(deployment_name="text-davinci-002-prod", model_name="text-davinci-002")

```

```
# Run the LLM
llm("Tell me a joke")

```

```
'  Why did the chicken cross the road?  To get to the other side.'

```

我们还可以打印LLM并查看其自定义打印。

```
print(llm)

```

```
AzureOpenAI
Params: {'deployment_name': 'text-davinci-002', 'model_name': 'text-davinci-002', 'temperature': 0.7, 'max_tokens': 256, 'top_p': 1, 'frequency_penalty': 0, 'presence_penalty': 0, 'n': 1, 'best_of': 1}

```

