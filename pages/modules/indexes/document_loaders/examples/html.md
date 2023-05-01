


 HTML
 [#](#html "Permalink to this headline")
===============================================



 This covers how to load HTML documents into a document format that we can use downstream.
 







```
from langchain.document_loaders import UnstructuredHTMLLoader

```










```
loader = UnstructuredHTMLLoader("example_data/fake-content")

```










```
data = loader.load()

```










```
data

```








```
[Document(page_content='My First Heading\n\nMy first paragraph.', lookup_str='', metadata={'source': 'example_data/fake-content'}, lookup_index=0)]

```







 Loading HTML with BeautifulSoup4
 [#](#loading-html-with-beautifulsoup4 "Permalink to this headline")
-------------------------------------------------------------------------------------------------------



 We can also use BeautifulSoup4 to load HTML documents using the
 `BSHTMLLoader`
 . This will extract the text from the html into
 `page_content`
 , and the page title as
 `title`
 into
 `metadata`
 .
 







```
from langchain.document_loaders import BSHTMLLoader

```










```
loader = BSHTMLLoader("example_data/fake-content")
data = loader.load()
data

```








```
[Document(page_content='\n\nTest Title\n\n\nMy First Heading\nMy first paragraph.\n\n\n', lookup_str='', metadata={'source': 'example_data/fake-content', 'title': 'Test Title'}, lookup_index=0)]

```








