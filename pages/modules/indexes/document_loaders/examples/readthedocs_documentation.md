


 ReadTheDocs Documentation
 [#](#readthedocs-documentation "Permalink to this headline")
=========================================================================================



 This notebook covers how to load content from html that was generated as part of a Read-The-Docs build.
 



 For an example of this in the wild, see
 [here](https://github.com/hwchase17/chat-langchain) 
 .
 



 This assumes that the html has already been scraped into a folder. This can be done by uncommenting and running the following command
 







```
#!wget -r -A -P rtdocs https://langchain.readthedocs.io/en/latest/

```










```
from langchain.document_loaders import ReadTheDocsLoader

```










```
loader = ReadTheDocsLoader("rtdocs", features='html.parser')

```










```
docs = loader.load()

```







