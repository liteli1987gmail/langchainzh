


托管在Azure上的OpenAI端点
=============

本笔记本将介绍如何连接到托管在Azure上的OpenAI端点。

```
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

```

```
BASE_URL = "https://${TODO}.openai.azure.com"
API_KEY = "..."
DEPLOYMENT_NAME = "chat"
model = AzureChatOpenAI(
    openai_api_base=BASE_URL,
    openai_api_version="2023-03-15-preview",
    deployment_name=DEPLOYMENT_NAME,
    openai_api_key=API_KEY,
    openai_api_type = "azure",
)

```

```
model([HumanMessage(content="Translate this sentence from English to French. I love programming.")])

```

```
AIMessage(content="  J'aime programmer.", additional_kwargs={})

```

