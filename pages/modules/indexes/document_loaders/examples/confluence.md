


 Confluence
 [#](#confluence "Permalink to this headline")
===========================================================



 A loader for Confluence pages.
 



 This currently supports both username/api_key and Oauth2 login.
 



 Specify a list page_ids and/or space_key to load in the corresponding pages into Document objects, if both are specified the union of both sets will be returned.
 



 You can also specify a boolean
 `include_attachments`
 to include attachments, this is set to False by default, if set to True all attachments will be downloaded and ConfluenceReader will extract the text from the attachments and add it to the Document object. Currently supported attachment types are: PDF, PNG, JPEG/JPG, SVG, Word and Excel.
 



 Hint: space_key and page_id can both be found in the URL of a page in Confluence - https://yoursite.atlassian.com/wiki/spaces/<space_key>/pages/<page_id>
 







```
from langchain.document_loaders import ConfluenceLoader

loader = ConfluenceLoader(
    url="https://yoursite.atlassian.com/wiki",
    username="me",
    api_key="12345"
)
documents = loader.load(space_key="SPACE", include_attachments=True, limit=50)

```







