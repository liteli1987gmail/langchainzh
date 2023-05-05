

AzureOpenAI[#](#azureopenai "此标题的永久链接")
=========================================================

让我们加载OpenAI嵌入类，并设置环境变量以指示使用Azure端点。
```
# set the environment variables needed for openai package to know to reach out to azure
import os

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_BASE"] = "https://<your-endpoint.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "your AzureOpenAI key"

```

```
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="your-embeddings-deployment-name")

```

```
text = "This is a test document."

```

```
query_result = embeddings.embed_query(text)

```

```
doc_result = embeddings.embed_documents([text])

```

