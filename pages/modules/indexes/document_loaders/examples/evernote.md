


 EverNote
 [#](#evernote "Permalink to this headline")
=======================================================



 How to load EverNote file from disk.
 







```
# !pip install pypandoc
# import pypandoc

# pypandoc.download_pandoc()

```










```
from langchain.document_loaders import EverNoteLoader

loader = EverNoteLoader("example_data/testing.enex")
loader.load()

```








```
[Document(page_content='testing this\n\nwhat happens?\n\nto the world?\n', lookup_str='', metadata={'source': 'example_data/testing.enex'}, lookup_index=0)]

```







