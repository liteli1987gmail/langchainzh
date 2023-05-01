


 Copy Paste
 [#](#copy-paste "Permalink to this headline")
===========================================================



 This notebook covers how to load a document object from something you just want to copy and paste. In this case, you don’t even need to use a DocumentLoader, but rather can just construct the Document directly.
 







```
from langchain.docstore.document import Document

```










```
text = "..... put the text you copy pasted here......"

```










```
doc = Document(page_content=text)

```







 Metadata
 [#](#metadata "Permalink to this headline")
-------------------------------------------------------



 If you want to add metadata about the where you got this piece of text, you easily can with the metadata key.
 







```
metadata = {"source": "internet", "date": "Friday"}

```










```
doc = Document(page_content=text, metadata=metadata)

```








