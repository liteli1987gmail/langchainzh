


 Bilibili
 [#](#bilibili "Permalink to this headline")
=======================================================



 This loader utilizes the
 `bilibili-api`
 to fetch the text transcript from Bilibili, one of the most beloved long-form video sites in China.
 



 With this BiliBiliLoader, users can easily obtain the transcript of their desired video content on the platform.
 







```
from langchain.document_loaders.bilibili import BiliBiliLoader

```










```
#!pip install bilibili-api

```










```
loader = BiliBiliLoader(
    ["https://www.bilibili.com/video/BV1xt411o7Xu/"]
)

```










```
loader.load()

```







