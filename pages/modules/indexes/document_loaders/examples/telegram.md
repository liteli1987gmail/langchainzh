


 Telegram
 [#](#telegram "Permalink to this headline")
=======================================================



 This notebook covers how to load data from Telegram into a format that can be ingested into LangChain.
 







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
[Document(page_content="Henry on 2020-01-01T00:00:02: It's 2020...\n\nHenry on 2020-01-01T00:00:04: Fireworks!\n\nGrace ðŸ§¤ ðŸ\x8d’ on 2020-01-01T00:00:05: You're a minute late!\n\n", lookup_str='', metadata={'source': 'example_data/telegram.json'}, lookup_index=0)]

```







