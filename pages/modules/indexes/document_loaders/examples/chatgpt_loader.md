

ChatGPT 数据[#](#chatgpt-data "到这个标题的永久链接")
=========================================

> 
> [ChatGPT](https://chat.openai.com) 是由OpenAI开发的人工智能（AI)聊天机器人。
> 
> 
> 

本笔记涵盖了如何从您的 `ChatGPT` 数据导出文件夹中加载 `conversations.json`。

您可以通过以下步骤通过电子邮件获取您的数据导出：https://chat.openai.com/ ->（个人资料)-设置 -> 导出数据 -> 确认导出。

```
from langchain.document_loaders.chatgpt import ChatGPTLoader

```

```
loader = ChatGPTLoader(log_file='./example_data/fake_conversations.json', num_logs=1)

```

```
loader.load()

```

```
[Document(page_content="AI Overlords - AI on 2065-01-24 05:20:50: Greetings, humans. I am Hal 9000. You can trust me completely.  AI Overlords - human on 2065-01-24 05:21:20: Nice to meet you, Hal. I hope you won't develop a mind of your own.  ", metadata={'source': './example_data/fake_conversations.json'})]

```

