


 WhatsApp Chat
 [#](#whatsapp-chat "Permalink to this headline")
=================================================================



 This notebook covers how to load data from the WhatsApp Chats into a format that can be ingested into LangChain.
 







```
from langchain.document_loaders import WhatsAppChatLoader

```










```
loader = WhatsAppChatLoader("example_data/whatsapp_chat.txt")

```










```
loader.load()

```







