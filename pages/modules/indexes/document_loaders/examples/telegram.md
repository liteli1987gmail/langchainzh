
# Telegram

> [Telegram Messenger](https://web.telegram.org/a/) 是一个全球可访问的付费/免费、跨平台、加密、基于云端和集中化的即时通讯服务。该应用还提供可选的端到端加密聊天和视频通话、VoIP、文件共享和多种其他功能。

本笔记本介绍了如何从Telegram中加载数据到可以摄取到LangChain的格式。
```
from langchain.document_loaders import TelegramChatLoader

```

```
loader = TelegramChatLoader("example_data/telegram.json")

```

```
loader.load()

```

```
[Document(page_content="Henry on 2020-01-01T00:00:02: It's 2020...  Henry on 2020-01-01T00:00:04: Fireworks!  Grace ðŸ§¤ ðŸ\x8d’ on 2020-01-01T00:00:05: You're a minute late!  ", lookup_str='', metadata={'source': 'example_data/telegram.json'}, lookup_index=0)]

```

