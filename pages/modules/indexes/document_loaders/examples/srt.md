


 Subtitle Files
 [#](#subtitle-files "Permalink to this headline")
===================================================================



 How to load data from subtitle (
 `.srt`
 ) files
 







```
from langchain.document_loaders import SRTLoader

```










```
loader = SRTLoader("example_data/Star_Wars_The_Clone_Wars_S06E07_Crisis_at_the_Heart.srt")

```










```
docs = loader.load()

```










```
docs[0].page_content[:100]

```








```
'<i>Corruption discovered\nat the core of the Banking Clan!</i> <i>Reunited, Rush Clovis\nand Senator A'

```







