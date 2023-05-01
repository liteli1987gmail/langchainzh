


 EPubs
 [#](#epubs "Permalink to this headline")
=================================================



 This covers how to load
 `.epub`
 documents into a document format that we can use downstream. You’ll need to install the
 [`pandocs`](https://pandoc.org/installing)
 package for this loader to work.
 







```
from langchain.document_loaders import UnstructuredEPubLoader

```










```
loader = UnstructuredEPubLoader("winter-sports.epub")

```










```
data = loader.load()

```







 Retain Elements
 [#](#retain-elements "Permalink to this headline")
---------------------------------------------------------------------



 Under the hood, Unstructured creates different “elements” for different chunks of text. By default we combine those together, but you can easily keep that separation by specifying
 `mode="elements"`
 .
 







```
loader = UnstructuredEPubLoader("winter-sports.epub", mode="elements")

```










```
data = loader.load()

```










```
data[0]

```








```
Document(page_content='The Project Gutenberg eBook of Winter Sports in\nSwitzerland, by E. F. Benson', lookup_str='', metadata={'source': 'winter-sports.epub', 'page_number': 1, 'category': 'Title'}, lookup_index=0)

```








