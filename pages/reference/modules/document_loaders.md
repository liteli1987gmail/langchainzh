




 Document Loaders
 [#](#module-langchain.document_loaders "Permalink to this headline")
========================================================================================



 All different types of document loaders.
 




*class*


 langchain.document_loaders.
 



 AZLyricsLoader
 


 (
 
*web_path
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ]*
 ,
 *header_template
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/azlyrics#AZLyricsLoader)
[#](#langchain.document_loaders.AZLyricsLoader "Permalink to this definition") 



 Loader that loads AZLyrics webpages.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/azlyrics#AZLyricsLoader.load)
[#](#langchain.document_loaders.AZLyricsLoader.load "Permalink to this definition") 



 Load webpage.
 








 web_paths
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.document_loaders.AZLyricsLoader.web_paths "Permalink to this definition") 








*class*


 langchain.document_loaders.
 



 AirbyteJSONLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/airbyte_json#AirbyteJSONLoader)
[#](#langchain.document_loaders.AirbyteJSONLoader "Permalink to this definition") 



 Loader that loads local airbyte json files.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/airbyte_json#AirbyteJSONLoader.load)
[#](#langchain.document_loaders.AirbyteJSONLoader.load "Permalink to this definition") 



 Load file.
 








*pydantic
 

 model*


 langchain.document_loaders.
 



 ApifyDatasetLoader
 

[[source]](../../_modules/langchain/document_loaders/apify_dataset#ApifyDatasetLoader)
[#](#langchain.document_loaders.ApifyDatasetLoader "Permalink to this definition") 



 Logic for loading documents from Apify datasets.
 




*field*


 apify_client
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.document_loaders.ApifyDatasetLoader.apify_client "Permalink to this definition") 






*field*


 dataset_id
 

*:
 




 str*
*[Required]*
[#](#langchain.document_loaders.ApifyDatasetLoader.dataset_id "Permalink to this definition") 



 The ID of the dataset on the Apify platform.
 






*field*


 dataset_mapping_function
 

*:
 




 Callable
 


 [
 



 [
 


 Dict
 


 ]
 



 ,
 




 langchain.schema.Document
 


 ]*
*[Required]*
[#](#langchain.document_loaders.ApifyDatasetLoader.dataset_mapping_function "Permalink to this definition") 



 A custom function that takes a single dictionary (an Apify dataset item)
and converts it to an instance of the Document class.
 








 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/apify_dataset#ApifyDatasetLoader.load)
[#](#langchain.document_loaders.ApifyDatasetLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 ArxivLoader
 


 (
 
*query
 



 :
 





 str*
 ,
 *load_max_docs
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 100*
 ,
 *load_all_available_meta
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 False*

 )
 
[[source]](../../_modules/langchain/document_loaders/arxiv#ArxivLoader)
[#](#langchain.document_loaders.ArxivLoader "Permalink to this definition") 



 Loads a query result from arxiv.org into a list of Documents.
 



 Each document represents one Document.
The loader converts the original PDF format into the text.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/arxiv#ArxivLoader.load)
[#](#langchain.document_loaders.ArxivLoader.load "Permalink to this definition") 



 Load data into document objects.
 








*class*


 langchain.document_loaders.
 



 AzureBlobStorageContainerLoader
 


 (
 
*conn_str
 



 :
 





 str*
 ,
 *container
 



 :
 





 str*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 ''*

 )
 
[[source]](../../_modules/langchain/document_loaders/azure_blob_storage_container#AzureBlobStorageContainerLoader)
[#](#langchain.document_loaders.AzureBlobStorageContainerLoader "Permalink to this definition") 



 Loading logic for loading documents from Azure Blob Storage.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/azure_blob_storage_container#AzureBlobStorageContainerLoader.load)
[#](#langchain.document_loaders.AzureBlobStorageContainerLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 AzureBlobStorageFileLoader
 


 (
 
*conn_str
 



 :
 





 str*
 ,
 *container
 



 :
 





 str*
 ,
 *blob_name
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/azure_blob_storage_file#AzureBlobStorageFileLoader)
[#](#langchain.document_loaders.AzureBlobStorageFileLoader "Permalink to this definition") 



 Loading logic for loading documents from Azure Blob Storage.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/azure_blob_storage_file#AzureBlobStorageFileLoader.load)
[#](#langchain.document_loaders.AzureBlobStorageFileLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 BSHTMLLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *open_encoding
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *bs_kwargs
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *get_text_separator
 



 :
 





 str
 





 =
 





 ''*

 )
 
[[source]](../../_modules/langchain/document_loaders/html_bs#BSHTMLLoader)
[#](#langchain.document_loaders.BSHTMLLoader "Permalink to this definition") 



 Loader that uses beautiful soup to parse HTML files.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/html_bs#BSHTMLLoader.load)
[#](#langchain.document_loaders.BSHTMLLoader.load "Permalink to this definition") 



 Load data into document objects.
 








*class*


 langchain.document_loaders.
 



 BigQueryLoader
 


 (
 
*query
 



 :
 





 str*
 ,
 *project
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *page_content_columns
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *metadata_columns
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/bigquery#BigQueryLoader)
[#](#langchain.document_loaders.BigQueryLoader "Permalink to this definition") 



 Loads a query result from BigQuery into a list of documents.
 



 Each document represents one row of the result. The
 
 page_content_columns
 
 are written into the
 
 page_content
 
 of the document. The
 
 metadata_columns
 
 are written into the
 
 metadata
 
 of the document. By default, all columns
are written into the
 
 page_content
 
 and none into the
 
 metadata
 
 .
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/bigquery#BigQueryLoader.load)
[#](#langchain.document_loaders.BigQueryLoader.load "Permalink to this definition") 



 Load data into document objects.
 








*class*


 langchain.document_loaders.
 



 BiliBiliLoader
 


 (
 
*video_urls
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 
[[source]](../../_modules/langchain/document_loaders/bilibili#BiliBiliLoader)
[#](#langchain.document_loaders.BiliBiliLoader "Permalink to this definition") 



 Loader that loads bilibili transcripts.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/bilibili#BiliBiliLoader.load)
[#](#langchain.document_loaders.BiliBiliLoader.load "Permalink to this definition") 



 Load from bilibili url.
 








*class*


 langchain.document_loaders.
 



 BlackboardLoader
 


 (
 
*blackboard_course_url
 



 :
 





 str*
 ,
 *bbrouter
 



 :
 





 str*
 ,
 *load_all_recursively
 



 :
 





 bool
 





 =
 





 True*
 ,
 *basic_auth
 



 :
 





 Optional
 


 [
 


 Tuple
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *cookies
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/blackboard#BlackboardLoader)
[#](#langchain.document_loaders.BlackboardLoader "Permalink to this definition") 



 Loader that loads all documents from a Blackboard course.
 



 This loader is not compatible with all Blackboard courses. It is only
compatible with courses that use the new Blackboard interface.
To use this loader, you must have the BbRouter cookie. You can get this
cookie by logging into the course and then copying the value of the
BbRouter cookie from the browser’s developer tools.
 



 Example
 





```
from langchain.document_loaders import BlackboardLoader

loader = BlackboardLoader(
    blackboard_course_url="https://blackboard.example.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_123456_1",
    bbrouter="expires:12345...",
)
documents = loader.load()

```







 base_url
 

*:
 




 str*
[#](#langchain.document_loaders.BlackboardLoader.base_url "Permalink to this definition") 








 check_bs4
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/document_loaders/blackboard#BlackboardLoader.check_bs4)
[#](#langchain.document_loaders.BlackboardLoader.check_bs4 "Permalink to this definition") 



 Check if BeautifulSoup4 is installed.
 




 Raises
 


**ImportError** 
 – If BeautifulSoup4 is not installed.
 










 download
 


 (
 
*path
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/document_loaders/blackboard#BlackboardLoader.download)
[#](#langchain.document_loaders.BlackboardLoader.download "Permalink to this definition") 



 Download a file from a url.
 




 Parameters
 


**path** 
 – Path to the file.
 










 folder_path
 

*:
 




 str*
[#](#langchain.document_loaders.BlackboardLoader.folder_path "Permalink to this definition") 








 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/blackboard#BlackboardLoader.load)
[#](#langchain.document_loaders.BlackboardLoader.load "Permalink to this definition") 



 Load data into document objects.
 




 Returns
 


 List of documents.
 










 load_all_recursively
 

*:
 




 bool*
[#](#langchain.document_loaders.BlackboardLoader.load_all_recursively "Permalink to this definition") 








 parse_filename
 


 (
 
*url
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/document_loaders/blackboard#BlackboardLoader.parse_filename)
[#](#langchain.document_loaders.BlackboardLoader.parse_filename "Permalink to this definition") 



 Parse the filename from a url.
 




 Parameters
 


**url** 
 – Url to parse the filename from.
 




 Returns
 


 The filename.
 










*class*


 langchain.document_loaders.
 



 BlockchainDocumentLoader
 


 (
 
*contract_address
 



 :
 





 str*
 ,
 *blockchainType
 



 :
 





 langchain.document_loaders.blockchain.BlockchainType
 





 =
 





 BlockchainType.ETH_MAINNET*
 ,
 *api_key
 



 :
 





 str
 





 =
 





 'docs-demo'*
 ,
 *startToken
 



 :
 





 str
 





 =
 





 ''*

 )
 
[[source]](../../_modules/langchain/document_loaders/blockchain#BlockchainDocumentLoader)
[#](#langchain.document_loaders.BlockchainDocumentLoader "Permalink to this definition") 



 Loads elements from a blockchain smart contract into Langchain documents.
 



 The supported blockchains are: Ethereum mainnet, Ethereum Goerli testnet,
Polygon mainnet, and Polygon Mumbai testnet.
 



 If no BlockchainType is specified, the default is Ethereum mainnet.
 



 The Loader uses the Alchemy API to interact with the blockchain.
 



 The API returns 100 NFTs per request and can be paginated using the
startToken parameter.
 



 ALCHEMY_API_KEY environment variable must be set to use this loader.
 




 Future versions of this loader can:
 

* Support additional Alchemy APIs (e.g. getTransactions, etc.)
* Support additional blockain APIs (e.g. Infura, Opensea, etc.)








 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/blockchain#BlockchainDocumentLoader.load)
[#](#langchain.document_loaders.BlockchainDocumentLoader.load "Permalink to this definition") 



 Load data into document objects.
 








*class*


 langchain.document_loaders.
 



 CSVLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *source_column
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *csv_args
 



 :
 





 Optional
 


 [
 


 Dict
 


 ]
 






 =
 





 None*
 ,
 *encoding
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/csv_loader#CSVLoader)
[#](#langchain.document_loaders.CSVLoader "Permalink to this definition") 



 Loads a CSV file into a list of documents.
 



 Each document represents one row of the CSV file. Every row is converted into a
key/value pair and outputted to a new line in the document’s page_content.
 



 The source for each document loaded from csv is set to the value of the
 
 file_path
 
 argument for all doucments by default.
You can override this by setting the
 
 source_column
 
 argument to the
name of a column in the CSV file.
The source of each document will then be set to the value of the column
with the name specified in
 
 source_column
 
 .
 




 Output Example:
 




```
column1: value1
column2: value2
column3: value3

```









 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/csv_loader#CSVLoader.load)
[#](#langchain.document_loaders.CSVLoader.load "Permalink to this definition") 



 Load data into document objects.
 








*class*


 langchain.document_loaders.
 



 ChatGPTLoader
 


 (
 
*log_file
 



 :
 





 str*
 ,
 *num_logs
 



 :
 





 int
 





 =
 





 -
 

 1*

 )
 
[[source]](../../_modules/langchain/document_loaders/chatgpt#ChatGPTLoader)
[#](#langchain.document_loaders.ChatGPTLoader "Permalink to this definition") 



 Loader that loads conversations from exported ChatGPT data.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/chatgpt#ChatGPTLoader.load)
[#](#langchain.document_loaders.ChatGPTLoader.load "Permalink to this definition") 



 Load data into document objects.
 








*class*


 langchain.document_loaders.
 



 CoNLLULoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/conllu#CoNLLULoader)
[#](#langchain.document_loaders.CoNLLULoader "Permalink to this definition") 



 Load CoNLL-U files.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/conllu#CoNLLULoader.load)
[#](#langchain.document_loaders.CoNLLULoader.load "Permalink to this definition") 



 Load from file path.
 








*class*


 langchain.document_loaders.
 



 CollegeConfidentialLoader
 


 (
 
*web_path
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ]*
 ,
 *header_template
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/college_confidential#CollegeConfidentialLoader)
[#](#langchain.document_loaders.CollegeConfidentialLoader "Permalink to this definition") 



 Loader that loads College Confidential webpages.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/college_confidential#CollegeConfidentialLoader.load)
[#](#langchain.document_loaders.CollegeConfidentialLoader.load "Permalink to this definition") 



 Load webpage.
 








 web_paths
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.document_loaders.CollegeConfidentialLoader.web_paths "Permalink to this definition") 








*class*


 langchain.document_loaders.
 



 ConfluenceLoader
 


 (
 
*url
 



 :
 





 str*
 ,
 *api_key
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *username
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *oauth2
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *cloud
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 True*
 ,
 *number_of_retries
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 3*
 ,
 *min_retry_seconds
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 2*
 ,
 *max_retry_seconds
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 10*
 ,
 *confluence_kwargs
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader)
[#](#langchain.document_loaders.ConfluenceLoader "Permalink to this definition") 



 Load Confluence pages. Port of
 <https://llamahub.ai/l/confluence>
 This currently supports both username/api_key and Oauth2 login.
 



 Specify a list page_ids and/or space_key to load in the corresponding pages into
Document objects, if both are specified the union of both sets will be returned.
 



 You can also specify a boolean
 
 include_attachments
 
 to include attachments, this
is set to False by default, if set to True all attachments will be downloaded and
ConfluenceReader will extract the text from the attachments and add it to the
Document object. Currently supported attachment types are: PDF, PNG, JPEG/JPG,
SVG, Word and Excel.
 



 Hint: space_key and page_id can both be found in the URL of a page in Confluence
-
 <https://yoursite.atlassian.com/wiki/spaces>
 /<space_key>/pages/<page_id>
 



 Example
 





```
from langchain.document_loaders import ConfluenceLoader

loader = ConfluenceLoader(
    url="https://yoursite.atlassian.com/wiki",
    username="me",
    api_key="12345"
)
documents = loader.load(space_key="SPACE",limit=50)

```





 Parameters
 

* **url** 
 (
 *str* 
 ) – _description_
* **api_key** 
 (
 *str* 
*,* 
*optional* 
 ) – _description_, defaults to None
* **username** 
 (
 *str* 
*,* 
*optional* 
 ) – _description_, defaults to None
* **oauth2** 
 (
 *dict* 
*,* 
*optional* 
 ) – _description_, defaults to {}
* **cloud** 
 (
 *bool* 
*,* 
*optional* 
 ) – _description_, defaults to True
* **number_of_retries** 
 (
 *Optional* 
*[* 
*int* 
*]* 
*,* 
*optional* 
 ) – How many times to retry, defaults to 3
* **min_retry_seconds** 
 (
 *Optional* 
*[* 
*int* 
*]* 
*,* 
*optional* 
 ) – defaults to 2
* **max_retry_seconds** 
 (
 *Optional* 
*[* 
*int* 
*]* 
*,* 
*optional* 
 ) – defaults to 10
* **confluence_kwargs** 
 (
 *dict* 
*,* 
*optional* 
 ) – additional kwargs to initialize confluence with




 Raises
 

* **ValueError** 
 – Errors while validating input
* **ImportError** 
 – Required dependencies not installed.








 is_public_page
 


 (
 
*page
 



 :
 





 dict*

 )
 


 →
 


 bool
 


[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.is_public_page)
[#](#langchain.document_loaders.ConfluenceLoader.is_public_page "Permalink to this definition") 



 Check if a page is publicly accessible.
 








 load
 


 (
 
*space_key
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *page_ids
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *label
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *cql
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *include_restricted_content
 



 :
 





 bool
 





 =
 





 False*
 ,
 *include_archived_content
 



 :
 





 bool
 





 =
 





 False*
 ,
 *include_attachments
 



 :
 





 bool
 





 =
 





 False*
 ,
 *include_comments
 



 :
 





 bool
 





 =
 





 False*
 ,
 *limit
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 50*
 ,
 *max_pages
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 1000*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.load)
[#](#langchain.document_loaders.ConfluenceLoader.load "Permalink to this definition") 




 Parameters
 

* **space_key** 
 (
 *Optional* 
*[* 
*str* 
*]* 
*,* 
*optional* 
 ) – Space key retrieved from a confluence URL, defaults to None
* **page_ids** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*str* 
*]* 
*]* 
*,* 
*optional* 
 ) – List of specific page IDs to load, defaults to None
* **label** 
 (
 *Optional* 
*[* 
*str* 
*]* 
*,* 
*optional* 
 ) – Get all pages with this label, defaults to None
* **cql** 
 (
 *Optional* 
*[* 
*str* 
*]* 
*,* 
*optional* 
 ) – CQL Expression, defaults to None
* **include_restricted_content** 
 (
 *bool* 
*,* 
*optional* 
 ) – defaults to False
* **include_archived_content** 
 (
 *bool* 
*,* 
*optional* 
 ) – Whether to include archived content,
defaults to False
* **include_attachments** 
 (
 *bool* 
*,* 
*optional* 
 ) – defaults to False
* **include_comments** 
 (
 *bool* 
*,* 
*optional* 
 ) – defaults to False
* **limit** 
 (
 *int* 
*,* 
*optional* 
 ) – Maximum number of pages to retrieve per request, defaults to 50
* **max_pages** 
 (
 *int* 
*,* 
*optional* 
 ) – Maximum number of pages to retrieve in total, defaults 1000




 Raises
 

* **ValueError** 
 – _description_
* **ImportError** 
 – _description_




 Returns
 


 _description_
 




 Return type
 


 List[Document]
 










 paginate_request
 


 (
 
*retrieval_method
 



 :
 





 Callable*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.paginate_request)
[#](#langchain.document_loaders.ConfluenceLoader.paginate_request "Permalink to this definition") 



 Paginate the various methods to retrieve groups of pages.
 



 Unfortunately, due to page size, sometimes the Confluence API
doesn’t match the limit value. If
 
 limit
 
 is >100 confluence
seems to cap the response to 100. Also, due to the Atlassian Python
package, we don’t get the “next” values from the “_links” key because
they only return the value from the results key. So here, the pagination
starts from 0 and goes until the max_pages, getting the
 
 limit
 
 number
of pages with each request. We have to manually check if there
are more docs based on the length of the returned list of pages, rather than
just checking for the presence of a
 
 next
 
 key in the response like this page
would have you do:
 <https://developer.atlassian.com/server/confluence/pagination-in-the-rest-api/>





 Parameters
 


**retrieval_method** 
 (
 *callable* 
 ) – Function used to retrieve docs
 




 Returns
 


 List of documents
 




 Return type
 


 List
 










 process_attachment
 


 (
 
*page_id
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.process_attachment)
[#](#langchain.document_loaders.ConfluenceLoader.process_attachment "Permalink to this definition") 








 process_doc
 


 (
 
*link
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.process_doc)
[#](#langchain.document_loaders.ConfluenceLoader.process_doc "Permalink to this definition") 








 process_image
 


 (
 
*link
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.process_image)
[#](#langchain.document_loaders.ConfluenceLoader.process_image "Permalink to this definition") 








 process_page
 


 (
 
*page
 



 :
 





 dict*
 ,
 *include_attachments
 



 :
 





 bool*
 ,
 *include_comments
 



 :
 





 bool*

 )
 


 →
 


 langchain.schema.Document
 


[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.process_page)
[#](#langchain.document_loaders.ConfluenceLoader.process_page "Permalink to this definition") 








 process_pages
 


 (
 
*pages
 



 :
 





 List
 


 [
 


 dict
 


 ]*
 ,
 *include_restricted_content
 



 :
 





 bool*
 ,
 *include_attachments
 



 :
 





 bool*
 ,
 *include_comments
 



 :
 





 bool*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.process_pages)
[#](#langchain.document_loaders.ConfluenceLoader.process_pages "Permalink to this definition") 



 Process a list of pages into a list of documents.
 








 process_pdf
 


 (
 
*link
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.process_pdf)
[#](#langchain.document_loaders.ConfluenceLoader.process_pdf "Permalink to this definition") 








 process_svg
 


 (
 
*link
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.process_svg)
[#](#langchain.document_loaders.ConfluenceLoader.process_svg "Permalink to this definition") 








 process_xls
 


 (
 
*link
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.process_xls)
[#](#langchain.document_loaders.ConfluenceLoader.process_xls "Permalink to this definition") 






*static*


 validate_init_args
 


 (
 
*url
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *api_key
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *username
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *oauth2
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 


 →
 


 Optional
 


 [
 


 List
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/confluence#ConfluenceLoader.validate_init_args)
[#](#langchain.document_loaders.ConfluenceLoader.validate_init_args "Permalink to this definition") 



 Validates proper combinations of init arguments
 








*class*


 langchain.document_loaders.
 



 DataFrameLoader
 


 (
 
*data_frame
 



 :
 





 Any*
 ,
 *page_content_column
 



 :
 





 str
 





 =
 





 'text'*

 )
 
[[source]](../../_modules/langchain/document_loaders/dataframe#DataFrameLoader)
[#](#langchain.document_loaders.DataFrameLoader "Permalink to this definition") 



 Load Pandas DataFrames.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/dataframe#DataFrameLoader.load)
[#](#langchain.document_loaders.DataFrameLoader.load "Permalink to this definition") 



 Load from the dataframe.
 








*class*


 langchain.document_loaders.
 



 DiffbotLoader
 


 (
 
*api_token
 



 :
 





 str*
 ,
 *urls
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *continue_on_failure
 



 :
 





 bool
 





 =
 





 True*

 )
 
[[source]](../../_modules/langchain/document_loaders/diffbot#DiffbotLoader)
[#](#langchain.document_loaders.DiffbotLoader "Permalink to this definition") 



 Loader that loads Diffbot file json.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/diffbot#DiffbotLoader.load)
[#](#langchain.document_loaders.DiffbotLoader.load "Permalink to this definition") 



 Extract text from Diffbot on all the URLs and return Document instances
 








*class*


 langchain.document_loaders.
 



 DirectoryLoader
 


 (
 
*path:
 

 str,
 

 glob:
 

 str
 

 =
 

 '\*\*/[!.]\*',
 

 silent_errors:
 

 bool
 

 =
 

 False,
 

 load_hidden:
 

 bool
 

 =
 

 False,
 

 loader_cls:
 

 typing.Union[typing.Type[langchain.document_loaders.unstructured.UnstructuredFileLoader],
 

 typing.Type[langchain.document_loaders.text.TextLoader],
 

 typing.Type[langchain.document_loaders_bs.BSHTMLLoader]]
 

 =
 

 <class
 

 'langchain.document_loaders.unstructured.UnstructuredFileLoader'>,
 

 loader_kwargs:
 

 typing.Optional[dict]
 

 =
 

 None,
 

 recursive:
 

 bool
 

 =
 

 False,
 

 show_progress:
 

 bool
 

 =
 

 False*

 )
 
[[source]](../../_modules/langchain/document_loaders/directory#DirectoryLoader)
[#](#langchain.document_loaders.DirectoryLoader "Permalink to this definition") 



 Loading logic for loading documents from a directory.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/directory#DirectoryLoader.load)
[#](#langchain.document_loaders.DirectoryLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 DiscordChatLoader
 


 (
 
*chat_log
 



 :
 





 pd.DataFrame*
 ,
 *user_id_col
 



 :
 





 str
 





 =
 





 'ID'*

 )
 
[[source]](../../_modules/langchain/document_loaders/discord#DiscordChatLoader)
[#](#langchain.document_loaders.DiscordChatLoader "Permalink to this definition") 



 Load Discord chat logs.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/discord#DiscordChatLoader.load)
[#](#langchain.document_loaders.DiscordChatLoader.load "Permalink to this definition") 



 Load all chat messages.
 








*class*


 langchain.document_loaders.
 



 Docx2txtLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/word_document#Docx2txtLoader)
[#](#langchain.document_loaders.Docx2txtLoader "Permalink to this definition") 



 Loads a DOCX with docx2txt and chunks at character level.
 



 Defaults to check for local file, but if the file is a web path, it will download it
to a temporary file, and use that, then clean up the temporary file after completion
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/word_document#Docx2txtLoader.load)
[#](#langchain.document_loaders.Docx2txtLoader.load "Permalink to this definition") 



 Load given path as single page.
 








*class*


 langchain.document_loaders.
 



 DuckDBLoader
 


 (
 
*query
 



 :
 





 str*
 ,
 *database
 



 :
 





 str
 





 =
 





 ':memory:'*
 ,
 *read_only
 



 :
 





 bool
 





 =
 





 False*
 ,
 *config
 



 :
 





 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *page_content_columns
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *metadata_columns
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/duckdb_loader#DuckDBLoader)
[#](#langchain.document_loaders.DuckDBLoader "Permalink to this definition") 



 Loads a query result from DuckDB into a list of documents.
 



 Each document represents one row of the result. The
 
 page_content_columns
 
 are written into the
 
 page_content
 
 of the document. The
 
 metadata_columns
 
 are written into the
 
 metadata
 
 of the document. By default, all columns
are written into the
 
 page_content
 
 and none into the
 
 metadata
 
 .
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/duckdb_loader#DuckDBLoader.load)
[#](#langchain.document_loaders.DuckDBLoader.load "Permalink to this definition") 



 Load data into document objects.
 








*class*


 langchain.document_loaders.
 



 EverNoteLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/evernote#EverNoteLoader)
[#](#langchain.document_loaders.EverNoteLoader "Permalink to this definition") 



 Loader to load in EverNote files..
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/evernote#EverNoteLoader.load)
[#](#langchain.document_loaders.EverNoteLoader.load "Permalink to this definition") 



 Load document from EverNote file.
 








*class*


 langchain.document_loaders.
 



 FacebookChatLoader
 


 (
 
*path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/facebook_chat#FacebookChatLoader)
[#](#langchain.document_loaders.FacebookChatLoader "Permalink to this definition") 



 Loader that loads Facebook messages json directory dump.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/facebook_chat#FacebookChatLoader.load)
[#](#langchain.document_loaders.FacebookChatLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 GCSDirectoryLoader
 


 (
 
*project_name
 



 :
 





 str*
 ,
 *bucket
 



 :
 





 str*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 ''*

 )
 
[[source]](../../_modules/langchain/document_loaders/gcs_directory#GCSDirectoryLoader)
[#](#langchain.document_loaders.GCSDirectoryLoader "Permalink to this definition") 



 Loading logic for loading documents from GCS.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/gcs_directory#GCSDirectoryLoader.load)
[#](#langchain.document_loaders.GCSDirectoryLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 GCSFileLoader
 


 (
 
*project_name
 



 :
 





 str*
 ,
 *bucket
 



 :
 





 str*
 ,
 *blob
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/gcs_file#GCSFileLoader)
[#](#langchain.document_loaders.GCSFileLoader "Permalink to this definition") 



 Loading logic for loading documents from GCS.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/gcs_file#GCSFileLoader.load)
[#](#langchain.document_loaders.GCSFileLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 GitLoader
 


 (
 
*repo_path
 



 :
 





 str*
 ,
 *clone_url
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *branch
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'main'*
 ,
 *file_filter
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 str
 


 ]
 



 ,
 




 bool
 


 ]
 



 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/git#GitLoader)
[#](#langchain.document_loaders.GitLoader "Permalink to this definition") 



 Loads files from a Git repository into a list of documents.
Repository can be local on disk available at
 
 repo_path
 
 ,
or remote at
 
 clone_url
 
 that will be cloned to
 
 repo_path
 
 .
Currently supports only text files.
 



 Each document represents one file in the repository. The
 
 path
 
 points to
the local Git repository, and the
 
 branch
 
 specifies the branch to load
files from. By default, it loads from the
 
 main
 
 branch.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/git#GitLoader.load)
[#](#langchain.document_loaders.GitLoader.load "Permalink to this definition") 



 Load data into document objects.
 








*class*


 langchain.document_loaders.
 



 GitbookLoader
 


 (
 
*web_page
 



 :
 





 str*
 ,
 *load_all_paths
 



 :
 





 bool
 





 =
 





 False*
 ,
 *base_url
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *content_selector
 



 :
 





 str
 





 =
 





 'main'*

 )
 
[[source]](../../_modules/langchain/document_loaders/gitbook#GitbookLoader)
[#](#langchain.document_loaders.GitbookLoader "Permalink to this definition") 



 Load GitBook data.
 


1. load from either a single page, or
2. load all (relative) paths in the navbar.






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/gitbook#GitbookLoader.load)
[#](#langchain.document_loaders.GitbookLoader.load "Permalink to this definition") 



 Fetch text from one single GitBook page.
 








 web_paths
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.document_loaders.GitbookLoader.web_paths "Permalink to this definition") 








*class*


 langchain.document_loaders.
 



 GoogleApiClient
 


 (
 
*credentials_path
 



 :
 





 pathlib.Path
 





 =
 





 PosixPath('/home/docs/.credentials/credentials.json')*
 ,
 *service_account_path
 



 :
 





 pathlib.Path
 





 =
 





 PosixPath('/home/docs/.credentials/credentials.json')*
 ,
 *token_path
 



 :
 





 pathlib.Path
 





 =
 





 PosixPath('/home/docs/.credentials/token.json')*

 )
 
[[source]](../../_modules/langchain/document_loaders/youtube#GoogleApiClient)
[#](#langchain.document_loaders.GoogleApiClient "Permalink to this definition") 



 A Generic Google Api Client.
 



 To use, you should have the
 `google_auth_oauthlib,youtube_transcript_api,google`
 python package installed.
As the google api expects credentials you need to set up a google account and
register your Service. “
 <https://developers.google.com/docs/api/quickstart/python>
 ”
 



 Example
 





```
from langchain.document_loaders import GoogleApiClient
google_api_client = GoogleApiClient(
    service_account_path=Path("path_to_your_sec_file.json")
)

```







 credentials_path
 

*:
 




 pathlib.Path*
*=
 




 PosixPath('/home/docs/.credentials/credentials.json')*
[#](#langchain.document_loaders.GoogleApiClient.credentials_path "Permalink to this definition") 








 service_account_path
 

*:
 




 pathlib.Path*
*=
 




 PosixPath('/home/docs/.credentials/credentials.json')*
[#](#langchain.document_loaders.GoogleApiClient.service_account_path "Permalink to this definition") 








 token_path
 

*:
 




 pathlib.Path*
*=
 




 PosixPath('/home/docs/.credentials/token.json')*
[#](#langchain.document_loaders.GoogleApiClient.token_path "Permalink to this definition") 






*classmethod*


 validate_channel_or_videoIds_is_set
 


 (
 
*values
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*

 )
 


 →
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/youtube#GoogleApiClient.validate_channel_or_videoIds_is_set)
[#](#langchain.document_loaders.GoogleApiClient.validate_channel_or_videoIds_is_set "Permalink to this definition") 



 Validate that either folder_id or document_ids is set, but not both.
 








*class*


 langchain.document_loaders.
 



 GoogleApiYoutubeLoader
 


 (
 
*google_api_client
 



 :
 




[langchain.document_loaders.youtube.GoogleApiClient](#langchain.document_loaders.GoogleApiClient "langchain.document_loaders.youtube.GoogleApiClient")*
 ,
 *channel_name
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *video_ids
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *add_video_info
 



 :
 





 bool
 





 =
 





 True*
 ,
 *captions_language
 



 :
 





 str
 





 =
 





 'en'*
 ,
 *continue_on_failure
 



 :
 





 bool
 





 =
 





 False*

 )
 
[[source]](../../_modules/langchain/document_loaders/youtube#GoogleApiYoutubeLoader)
[#](#langchain.document_loaders.GoogleApiYoutubeLoader "Permalink to this definition") 



 Loader that loads all Videos from a Channel
 



 To use, you should have the
 `googleapiclient,youtube_transcript_api`
 python package installed.
As the service needs a google_api_client, you first have to initialize
the GoogleApiClient.
 



 Additionally you have to either provide a channel name or a list of videoids
“
 <https://developers.google.com/docs/api/quickstart/python>
 ”
 



 Example
 





```
from langchain.document_loaders import GoogleApiClient
from langchain.document_loaders import GoogleApiYoutubeLoader
google_api_client = GoogleApiClient(
    service_account_path=Path("path_to_your_sec_file.json")
)
loader = GoogleApiYoutubeLoader(
    google_api_client=google_api_client,
    channel_name = "CodeAesthetic"
)
load.load()

```







 add_video_info
 

*:
 




 bool*
*=
 




 True*
[#](#langchain.document_loaders.GoogleApiYoutubeLoader.add_video_info "Permalink to this definition") 








 captions_language
 

*:
 




 str*
*=
 




 'en'*
[#](#langchain.document_loaders.GoogleApiYoutubeLoader.captions_language "Permalink to this definition") 








 channel_name
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.document_loaders.GoogleApiYoutubeLoader.channel_name "Permalink to this definition") 








 continue_on_failure
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.document_loaders.GoogleApiYoutubeLoader.continue_on_failure "Permalink to this definition") 








 google_api_client
 

*:
 



[langchain.document_loaders.youtube.GoogleApiClient](#langchain.document_loaders.GoogleApiClient "langchain.document_loaders.youtube.GoogleApiClient")*
[#](#langchain.document_loaders.GoogleApiYoutubeLoader.google_api_client "Permalink to this definition") 








 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/youtube#GoogleApiYoutubeLoader.load)
[#](#langchain.document_loaders.GoogleApiYoutubeLoader.load "Permalink to this definition") 



 Load documents.
 






*classmethod*


 validate_channel_or_videoIds_is_set
 


 (
 
*values
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*

 )
 


 →
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/youtube#GoogleApiYoutubeLoader.validate_channel_or_videoIds_is_set)
[#](#langchain.document_loaders.GoogleApiYoutubeLoader.validate_channel_or_videoIds_is_set "Permalink to this definition") 



 Validate that either folder_id or document_ids is set, but not both.
 








 video_ids
 

*:
 




 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.document_loaders.GoogleApiYoutubeLoader.video_ids "Permalink to this definition") 








*pydantic
 

 model*


 langchain.document_loaders.
 



 GoogleDriveLoader
 

[[source]](../../_modules/langchain/document_loaders/googledrive#GoogleDriveLoader)
[#](#langchain.document_loaders.GoogleDriveLoader "Permalink to this definition") 



 Loader that loads Google Docs from Google Drive.
 




 Validators
 

* `validate_credentials_path`
 »
 `credentials_path`
* `validate_folder_id_or_document_ids`
 »
 `all
 

 fields`






*field*


 credentials_path
 

*:
 




 pathlib.Path*
*=
 




 PosixPath('/home/docs/.credentials/credentials.json')*
[#](#langchain.document_loaders.GoogleDriveLoader.credentials_path "Permalink to this definition") 






*field*


 document_ids
 

*:
 




 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.document_loaders.GoogleDriveLoader.document_ids "Permalink to this definition") 






*field*


 file_ids
 

*:
 




 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.document_loaders.GoogleDriveLoader.file_ids "Permalink to this definition") 






*field*


 folder_id
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.document_loaders.GoogleDriveLoader.folder_id "Permalink to this definition") 






*field*


 recursive
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.document_loaders.GoogleDriveLoader.recursive "Permalink to this definition") 






*field*


 service_account_key
 

*:
 




 pathlib.Path*
*=
 




 PosixPath('/home/docs/.credentials/keys.json')*
[#](#langchain.document_loaders.GoogleDriveLoader.service_account_key "Permalink to this definition") 






*field*


 token_path
 

*:
 




 pathlib.Path*
*=
 




 PosixPath('/home/docs/.credentials/token.json')*
[#](#langchain.document_loaders.GoogleDriveLoader.token_path "Permalink to this definition") 








 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/googledrive#GoogleDriveLoader.load)
[#](#langchain.document_loaders.GoogleDriveLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 GutenbergLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/gutenberg#GutenbergLoader)
[#](#langchain.document_loaders.GutenbergLoader "Permalink to this definition") 



 Loader that uses urllib to load .txt web files.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/gutenberg#GutenbergLoader.load)
[#](#langchain.document_loaders.GutenbergLoader.load "Permalink to this definition") 



 Load file.
 








*class*


 langchain.document_loaders.
 



 HNLoader
 


 (
 
*web_path
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ]*
 ,
 *header_template
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/hn#HNLoader)
[#](#langchain.document_loaders.HNLoader "Permalink to this definition") 



 Load Hacker News data from either main page results or the comments page.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/hn#HNLoader.load)
[#](#langchain.document_loaders.HNLoader.load "Permalink to this definition") 



 Get important HN webpage information.
 




 Components are:
 

* title
* content
* source url,
* time of post
* author of the post
* number of comments
* rank of the post










 load_comments
 


 (
 
*soup_info
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/hn#HNLoader.load_comments)
[#](#langchain.document_loaders.HNLoader.load_comments "Permalink to this definition") 



 Load comments from a HN post.
 








 load_results
 


 (
 
*soup
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/hn#HNLoader.load_results)
[#](#langchain.document_loaders.HNLoader.load_results "Permalink to this definition") 



 Load items from an HN page.
 








 web_paths
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.document_loaders.HNLoader.web_paths "Permalink to this definition") 








*class*


 langchain.document_loaders.
 



 HuggingFaceDatasetLoader
 


 (
 
*path
 



 :
 





 str*
 ,
 *page_content_column
 



 :
 





 str
 





 =
 





 'text'*
 ,
 *name
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *data_dir
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *data_files
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 str
 


 ,
 




 Sequence
 


 [
 


 str
 


 ]
 



 ,
 




 Mapping
 


 [
 


 str
 


 ,
 




 Union
 


 [
 


 str
 


 ,
 




 Sequence
 


 [
 


 str
 


 ]
 



 ]
 



 ]
 



 ]
 



 ]
 






 =
 





 None*
 ,
 *cache_dir
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *keep_in_memory
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 None*
 ,
 *save_infos
 



 :
 





 bool
 





 =
 





 False*
 ,
 *use_auth_token
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 bool
 


 ,
 




 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *num_proc
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/hugging_face_dataset#HuggingFaceDatasetLoader)
[#](#langchain.document_loaders.HuggingFaceDatasetLoader "Permalink to this definition") 



 Loading logic for loading documents from the Hugging Face Hub.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/hugging_face_dataset#HuggingFaceDatasetLoader.load)
[#](#langchain.document_loaders.HuggingFaceDatasetLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 IFixitLoader
 


 (
 
*web_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/ifixit#IFixitLoader)
[#](#langchain.document_loaders.IFixitLoader "Permalink to this definition") 



 Load iFixit repair guides, device wikis and answers.
 



 iFixit is the largest, open repair community on the web. The site contains nearly
100k repair manuals, 200k Questions & Answers on 42k devices, and all the data is
licensed under CC-BY.
 



 This loader will allow you to download the text of a repair guide, text of Q&A’s
and wikis from devices on iFixit using their open APIs and web scraping.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/ifixit#IFixitLoader.load)
[#](#langchain.document_loaders.IFixitLoader.load "Permalink to this definition") 



 Load data into document objects.
 








 load_device
 


 (
 
*url_override
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *include_guides
 



 :
 





 bool
 





 =
 





 True*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/ifixit#IFixitLoader.load_device)
[#](#langchain.document_loaders.IFixitLoader.load_device "Permalink to this definition") 








 load_guide
 


 (
 
*url_override
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/ifixit#IFixitLoader.load_guide)
[#](#langchain.document_loaders.IFixitLoader.load_guide "Permalink to this definition") 








 load_questions_and_answers
 


 (
 
*url_override
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/ifixit#IFixitLoader.load_questions_and_answers)
[#](#langchain.document_loaders.IFixitLoader.load_questions_and_answers "Permalink to this definition") 






*static*


 load_suggestions
 


 (
 
*query
 



 :
 





 str
 





 =
 





 ''*
 ,
 *doc_type
 



 :
 





 str
 





 =
 





 'all'*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/ifixit#IFixitLoader.load_suggestions)
[#](#langchain.document_loaders.IFixitLoader.load_suggestions "Permalink to this definition") 








*class*


 langchain.document_loaders.
 



 IMSDbLoader
 


 (
 
*web_path
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ]*
 ,
 *header_template
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/imsdb#IMSDbLoader)
[#](#langchain.document_loaders.IMSDbLoader "Permalink to this definition") 



 Loader that loads IMSDb webpages.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/imsdb#IMSDbLoader.load)
[#](#langchain.document_loaders.IMSDbLoader.load "Permalink to this definition") 



 Load webpage.
 








 web_paths
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.document_loaders.IMSDbLoader.web_paths "Permalink to this definition") 








*class*


 langchain.document_loaders.
 



 ImageCaptionLoader
 


 (
 
*path_images
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ]*
 ,
 *blip_processor
 



 :
 





 str
 





 =
 





 'Salesforce/blip-image-captioning-base'*
 ,
 *blip_model
 



 :
 





 str
 





 =
 





 'Salesforce/blip-image-captioning-base'*

 )
 
[[source]](../../_modules/langchain/document_loaders/image_captions#ImageCaptionLoader)
[#](#langchain.document_loaders.ImageCaptionLoader "Permalink to this definition") 



 Loader that loads the captions of an image
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/image_captions#ImageCaptionLoader.load)
[#](#langchain.document_loaders.ImageCaptionLoader.load "Permalink to this definition") 



 Load from a list of image files
 








*class*


 langchain.document_loaders.
 



 MathpixPDFLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *processed_file_format
 



 :
 





 str
 





 =
 





 'mmd'*
 ,
 *max_wait_time_seconds
 



 :
 





 int
 





 =
 





 500*
 ,
 *should_clean_pdf
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/pdf#MathpixPDFLoader)
[#](#langchain.document_loaders.MathpixPDFLoader "Permalink to this definition") 






 clean_pdf
 


 (
 
*contents
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/document_loaders/pdf#MathpixPDFLoader.clean_pdf)
[#](#langchain.document_loaders.MathpixPDFLoader.clean_pdf "Permalink to this definition") 






*property*


 data
 

*:
 




 dict*
[#](#langchain.document_loaders.MathpixPDFLoader.data "Permalink to this definition") 








 get_processed_pdf
 


 (
 
*pdf_id
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/document_loaders/pdf#MathpixPDFLoader.get_processed_pdf)
[#](#langchain.document_loaders.MathpixPDFLoader.get_processed_pdf "Permalink to this definition") 






*property*


 headers
 

*:
 




 dict*
[#](#langchain.document_loaders.MathpixPDFLoader.headers "Permalink to this definition") 








 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/pdf#MathpixPDFLoader.load)
[#](#langchain.document_loaders.MathpixPDFLoader.load "Permalink to this definition") 



 Load data into document objects.
 








 send_pdf
 


 (
 

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/document_loaders/pdf#MathpixPDFLoader.send_pdf)
[#](#langchain.document_loaders.MathpixPDFLoader.send_pdf "Permalink to this definition") 






*property*


 url
 

*:
 




 str*
[#](#langchain.document_loaders.MathpixPDFLoader.url "Permalink to this definition") 








 wait_for_processing
 


 (
 
*pdf_id
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/document_loaders/pdf#MathpixPDFLoader.wait_for_processing)
[#](#langchain.document_loaders.MathpixPDFLoader.wait_for_processing "Permalink to this definition") 








*class*


 langchain.document_loaders.
 



 NotebookLoader
 


 (
 
*path
 



 :
 





 str*
 ,
 *include_outputs
 



 :
 





 bool
 





 =
 





 False*
 ,
 *max_output_length
 



 :
 





 int
 





 =
 





 10*
 ,
 *remove_newline
 



 :
 





 bool
 





 =
 





 False*
 ,
 *traceback
 



 :
 





 bool
 





 =
 





 False*

 )
 
[[source]](../../_modules/langchain/document_loaders/notebook#NotebookLoader)
[#](#langchain.document_loaders.NotebookLoader "Permalink to this definition") 



 Loader that loads .ipynb notebook files.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/notebook#NotebookLoader.load)
[#](#langchain.document_loaders.NotebookLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 NotionDBLoader
 


 (
 
*integration_token
 



 :
 





 str*
 ,
 *database_id
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/notiondb#NotionDBLoader)
[#](#langchain.document_loaders.NotionDBLoader "Permalink to this definition") 



 Notion DB Loader.
Reads content from pages within a Noton Database.
:param integration_token: Notion integration token.
:type integration_token: str
:param database_id: Notion database id.
:type database_id: str
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/notiondb#NotionDBLoader.load)
[#](#langchain.document_loaders.NotionDBLoader.load "Permalink to this definition") 



 Load documents from the Notion database.
:returns: List of documents.
:rtype: List[Document]
 








 load_page
 


 (
 
*page_id
 



 :
 





 str*

 )
 


 →
 


 langchain.schema.Document
 


[[source]](../../_modules/langchain/document_loaders/notiondb#NotionDBLoader.load_page)
[#](#langchain.document_loaders.NotionDBLoader.load_page "Permalink to this definition") 



 Read a page.
 








*class*


 langchain.document_loaders.
 



 NotionDirectoryLoader
 


 (
 
*path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/notion#NotionDirectoryLoader)
[#](#langchain.document_loaders.NotionDirectoryLoader "Permalink to this definition") 



 Loader that loads Notion directory dump.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/notion#NotionDirectoryLoader.load)
[#](#langchain.document_loaders.NotionDirectoryLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 ObsidianLoader
 


 (
 
*path
 



 :
 





 str*
 ,
 *encoding
 



 :
 





 str
 





 =
 





 'UTF-8'*
 ,
 *collect_metadata
 



 :
 





 bool
 





 =
 





 True*

 )
 
[[source]](../../_modules/langchain/document_loaders/obsidian#ObsidianLoader)
[#](#langchain.document_loaders.ObsidianLoader "Permalink to this definition") 



 Loader that loads Obsidian files from disk.
 






 FRONT_MATTER_REGEX
 

*=
 




 re.compile('^---\\n(.\*?)\\n---\\n',
 

 re.MULTILINE|re.DOTALL)*
[#](#langchain.document_loaders.ObsidianLoader.FRONT_MATTER_REGEX "Permalink to this definition") 








 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/obsidian#ObsidianLoader.load)
[#](#langchain.document_loaders.ObsidianLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 OnlinePDFLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/pdf#OnlinePDFLoader)
[#](#langchain.document_loaders.OnlinePDFLoader "Permalink to this definition") 



 Loader that loads online PDFs.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/pdf#OnlinePDFLoader.load)
[#](#langchain.document_loaders.OnlinePDFLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 OutlookMessageLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/email#OutlookMessageLoader)
[#](#langchain.document_loaders.OutlookMessageLoader "Permalink to this definition") 



 Loader that loads Outlook Message files using extract_msg.
 [TeamMsgExtractor/msg-extractor](https://github.com/TeamMsgExtractor/msg-extractor) 







 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/email#OutlookMessageLoader.load)
[#](#langchain.document_loaders.OutlookMessageLoader.load "Permalink to this definition") 



 Load data into document objects.
 








*class*


 langchain.document_loaders.
 



 PDFMinerLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/pdf#PDFMinerLoader)
[#](#langchain.document_loaders.PDFMinerLoader "Permalink to this definition") 



 Loader that uses PDFMiner to load PDF files.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/pdf#PDFMinerLoader.load)
[#](#langchain.document_loaders.PDFMinerLoader.load "Permalink to this definition") 



 Load file.
 








*class*


 langchain.document_loaders.
 



 PDFMinerPDFasHTMLLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/pdf#PDFMinerPDFasHTMLLoader)
[#](#langchain.document_loaders.PDFMinerPDFasHTMLLoader "Permalink to this definition") 



 Loader that uses PDFMiner to load PDF files as HTML content.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/pdf#PDFMinerPDFasHTMLLoader.load)
[#](#langchain.document_loaders.PDFMinerPDFasHTMLLoader.load "Permalink to this definition") 



 Load file.
 










 langchain.document_loaders.
 



 PagedPDFSplitter
 

[#](#langchain.document_loaders.PagedPDFSplitter "Permalink to this definition") 



 alias of
 [`langchain.document_loaders.pdf.PyPDFLoader`](#langchain.document_loaders.PyPDFLoader "langchain.document_loaders.pdf.PyPDFLoader")







*class*


 langchain.document_loaders.
 



 PlaywrightURLLoader
 


 (
 
*urls
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *continue_on_failure
 



 :
 





 bool
 





 =
 





 True*
 ,
 *headless
 



 :
 





 bool
 





 =
 





 True*
 ,
 *remove_selectors
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/url_playwright#PlaywrightURLLoader)
[#](#langchain.document_loaders.PlaywrightURLLoader "Permalink to this definition") 



 Loader that uses Playwright and to load a page and unstructured to load the html.
This is useful for loading pages that require javascript to render.
 






 urls
 

[#](#langchain.document_loaders.PlaywrightURLLoader.urls "Permalink to this definition") 



 List of URLs to load.
 




 Type
 


 List[str]
 










 continue_on_failure
 

[#](#langchain.document_loaders.PlaywrightURLLoader.continue_on_failure "Permalink to this definition") 



 If True, continue loading other URLs on failure.
 




 Type
 


 bool
 










 headless
 

[#](#langchain.document_loaders.PlaywrightURLLoader.headless "Permalink to this definition") 



 If True, the browser will run in headless mode.
 




 Type
 


 bool
 










 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/url_playwright#PlaywrightURLLoader.load)
[#](#langchain.document_loaders.PlaywrightURLLoader.load "Permalink to this definition") 



 Load the specified URLs using Playwright and create Document instances.
 




 Returns
 


 A list of Document instances with loaded content.
 




 Return type
 


 List[Document]
 










*class*


 langchain.document_loaders.
 



 PyMuPDFLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/pdf#PyMuPDFLoader)
[#](#langchain.document_loaders.PyMuPDFLoader "Permalink to this definition") 



 Loader that uses PyMuPDF to load PDF files.
 






 load
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Optional
 


 [
 


 Any
 


 ]*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/pdf#PyMuPDFLoader.load)
[#](#langchain.document_loaders.PyMuPDFLoader.load "Permalink to this definition") 



 Load file.
 








*class*


 langchain.document_loaders.
 



 PyPDFDirectoryLoader
 


 (
 
*path
 



 :
 





 str*
 ,
 *glob
 



 :
 





 str
 





 =
 





 '\*\*/[!.]\*.pdf'*
 ,
 *silent_errors
 



 :
 





 bool
 





 =
 





 False*
 ,
 *load_hidden
 



 :
 





 bool
 





 =
 





 False*
 ,
 *recursive
 



 :
 





 bool
 





 =
 





 False*

 )
 
[[source]](../../_modules/langchain/document_loaders/pdf#PyPDFDirectoryLoader)
[#](#langchain.document_loaders.PyPDFDirectoryLoader "Permalink to this definition") 



 Loads a directory with PDF files with pypdf and chunks at character level.
 



 Loader also stores page numbers in metadatas.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/pdf#PyPDFDirectoryLoader.load)
[#](#langchain.document_loaders.PyPDFDirectoryLoader.load "Permalink to this definition") 



 Load data into document objects.
 








*class*


 langchain.document_loaders.
 



 PyPDFLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/pdf#PyPDFLoader)
[#](#langchain.document_loaders.PyPDFLoader "Permalink to this definition") 



 Loads a PDF with pypdf and chunks at character level.
 



 Loader also stores page numbers in metadatas.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/pdf#PyPDFLoader.load)
[#](#langchain.document_loaders.PyPDFLoader.load "Permalink to this definition") 



 Load given path as pages.
 








*class*


 langchain.document_loaders.
 



 PythonLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/python#PythonLoader)
[#](#langchain.document_loaders.PythonLoader "Permalink to this definition") 



 Load Python files, respecting any non-default encoding if specified.
 






*class*


 langchain.document_loaders.
 



 ReadTheDocsLoader
 


 (
 
*path
 



 :
 





 str*
 ,
 *encoding
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *errors
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Optional
 


 [
 


 Any
 


 ]*

 )
 
[[source]](../../_modules/langchain/document_loaders/readthedocs#ReadTheDocsLoader)
[#](#langchain.document_loaders.ReadTheDocsLoader "Permalink to this definition") 



 Loader that loads ReadTheDocs documentation directory dump.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/readthedocs#ReadTheDocsLoader.load)
[#](#langchain.document_loaders.ReadTheDocsLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 RedditPostsLoader
 


 (
 
*client_id
 



 :
 





 str*
 ,
 *client_secret
 



 :
 





 str*
 ,
 *user_agent
 



 :
 





 str*
 ,
 *search_queries
 



 :
 





 Sequence
 


 [
 


 str
 


 ]*
 ,
 *mode
 



 :
 





 str*
 ,
 *categories
 



 :
 





 Sequence
 


 [
 


 str
 


 ]
 






 =
 





 ['new']*
 ,
 *number_posts
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 10*

 )
 
[[source]](../../_modules/langchain/document_loaders/reddit#RedditPostsLoader)
[#](#langchain.document_loaders.RedditPostsLoader "Permalink to this definition") 



 Reddit posts loader.
Read posts on a subreddit.
First you need to go to
 <https://www.reddit.com/prefs/apps/>
 and create your application
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/reddit#RedditPostsLoader.load)
[#](#langchain.document_loaders.RedditPostsLoader.load "Permalink to this definition") 



 Load reddits.
 








*class*


 langchain.document_loaders.
 



 RoamLoader
 


 (
 
*path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/roam#RoamLoader)
[#](#langchain.document_loaders.RoamLoader "Permalink to this definition") 



 Loader that loads Roam files from disk.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/roam#RoamLoader.load)
[#](#langchain.document_loaders.RoamLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 S3DirectoryLoader
 


 (
 
*bucket
 



 :
 





 str*
 ,
 *prefix
 



 :
 





 str
 





 =
 





 ''*

 )
 
[[source]](../../_modules/langchain/document_loaders/s3_directory#S3DirectoryLoader)
[#](#langchain.document_loaders.S3DirectoryLoader "Permalink to this definition") 



 Loading logic for loading documents from s3.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/s3_directory#S3DirectoryLoader.load)
[#](#langchain.document_loaders.S3DirectoryLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 S3FileLoader
 


 (
 
*bucket
 



 :
 





 str*
 ,
 *key
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/s3_file#S3FileLoader)
[#](#langchain.document_loaders.S3FileLoader "Permalink to this definition") 



 Loading logic for loading documents from s3.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/s3_file#S3FileLoader.load)
[#](#langchain.document_loaders.S3FileLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 SRTLoader
 


 (
 
*file_path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/srt#SRTLoader)
[#](#langchain.document_loaders.SRTLoader "Permalink to this definition") 



 Loader for .srt (subtitle) files.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/srt#SRTLoader.load)
[#](#langchain.document_loaders.SRTLoader.load "Permalink to this definition") 



 Load using pysrt file.
 








*class*


 langchain.document_loaders.
 



 SeleniumURLLoader
 


 (
 
*urls
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *continue_on_failure
 



 :
 





 bool
 





 =
 





 True*
 ,
 *browser
 



 :
 





 Literal
 


 [
 



 'chrome'
 



 ,
 





 'firefox'
 



 ]
 






 =
 





 'chrome'*
 ,
 *executable_path
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *headless
 



 :
 





 bool
 





 =
 





 True*

 )
 
[[source]](../../_modules/langchain/document_loaders/url_selenium#SeleniumURLLoader)
[#](#langchain.document_loaders.SeleniumURLLoader "Permalink to this definition") 



 Loader that uses Selenium and to load a page and unstructured to load the html.
This is useful for loading pages that require javascript to render.
 






 urls
 

[#](#langchain.document_loaders.SeleniumURLLoader.urls "Permalink to this definition") 



 List of URLs to load.
 




 Type
 


 List[str]
 










 continue_on_failure
 

[#](#langchain.document_loaders.SeleniumURLLoader.continue_on_failure "Permalink to this definition") 



 If True, continue loading other URLs on failure.
 




 Type
 


 bool
 










 browser
 

[#](#langchain.document_loaders.SeleniumURLLoader.browser "Permalink to this definition") 



 The browser to use, either ‘chrome’ or ‘firefox’.
 




 Type
 


 str
 










 executable_path
 

[#](#langchain.document_loaders.SeleniumURLLoader.executable_path "Permalink to this definition") 



 The path to the browser executable.
 




 Type
 


 Optional[str]
 










 headless
 

[#](#langchain.document_loaders.SeleniumURLLoader.headless "Permalink to this definition") 



 If True, the browser will run in headless mode.
 




 Type
 


 bool
 










 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/url_selenium#SeleniumURLLoader.load)
[#](#langchain.document_loaders.SeleniumURLLoader.load "Permalink to this definition") 



 Load the specified URLs using Selenium and create Document instances.
 




 Returns
 


 A list of Document instances with loaded content.
 




 Return type
 


 List[Document]
 










*class*


 langchain.document_loaders.
 



 SitemapLoader
 


 (
 
*web_path
 



 :
 





 str*
 ,
 *filter_urls
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *parsing_function
 



 :
 





 Optional
 


 [
 


 Callable
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/sitemap#SitemapLoader)
[#](#langchain.document_loaders.SitemapLoader "Permalink to this definition") 



 Loader that fetches a sitemap and loads those URLs.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/sitemap#SitemapLoader.load)
[#](#langchain.document_loaders.SitemapLoader.load "Permalink to this definition") 



 Load sitemap.
 








 parse_sitemap
 


 (
 
*soup
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 dict
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/sitemap#SitemapLoader.parse_sitemap)
[#](#langchain.document_loaders.SitemapLoader.parse_sitemap "Permalink to this definition") 



 Parse sitemap xml and load into a list of dicts.
 








 web_paths
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.document_loaders.SitemapLoader.web_paths "Permalink to this definition") 








*class*


 langchain.document_loaders.
 



 SlackDirectoryLoader
 


 (
 
*zip_path
 



 :
 





 str*
 ,
 *workspace_url
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/slack_directory#SlackDirectoryLoader)
[#](#langchain.document_loaders.SlackDirectoryLoader "Permalink to this definition") 



 Loader for loading documents from a Slack directory dump.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/slack_directory#SlackDirectoryLoader.load)
[#](#langchain.document_loaders.SlackDirectoryLoader.load "Permalink to this definition") 



 Load and return documents from the Slack directory dump.
 








*class*


 langchain.document_loaders.
 



 StripeLoader
 


 (
 
*access_token
 



 :
 





 str*
 ,
 *resource
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/stripe#StripeLoader)
[#](#langchain.document_loaders.StripeLoader "Permalink to this definition") 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/stripe#StripeLoader.load)
[#](#langchain.document_loaders.StripeLoader.load "Permalink to this definition") 



 Load data into document objects.
 








*class*


 langchain.document_loaders.
 



 TelegramChatLoader
 


 (
 
*path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/telegram#TelegramChatLoader)
[#](#langchain.document_loaders.TelegramChatLoader "Permalink to this definition") 



 Loader that loads Telegram chat json directory dump.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/telegram#TelegramChatLoader.load)
[#](#langchain.document_loaders.TelegramChatLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 TextLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *encoding
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/text#TextLoader)
[#](#langchain.document_loaders.TextLoader "Permalink to this definition") 



 Load text files.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/text#TextLoader.load)
[#](#langchain.document_loaders.TextLoader.load "Permalink to this definition") 



 Load from file path.
 








*class*


 langchain.document_loaders.
 



 TwitterTweetLoader
 


 (
 
*auth_handler
 



 :
 





 Union
 


 [
 


 OAuthHandler
 


 ,
 




 OAuth2BearerHandler
 


 ]*
 ,
 *twitter_users
 



 :
 





 Sequence
 


 [
 


 str
 


 ]*
 ,
 *number_tweets
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 100*

 )
 
[[source]](../../_modules/langchain/document_loaders/twitter#TwitterTweetLoader)
[#](#langchain.document_loaders.TwitterTweetLoader "Permalink to this definition") 



 Twitter tweets loader.
Read tweets of user twitter handle.
 



 First you need to go to
 
 https://developer.twitter.com/en/docs/twitter-api
/getting-started/getting-access-to-the-twitter-api
 
 to get your token. And create a v2 version of the app.
 




*classmethod*


 from_bearer_token
 


 (
 
*oauth2_bearer_token
 



 :
 





 str*
 ,
 *twitter_users
 



 :
 





 Sequence
 


 [
 


 str
 


 ]*
 ,
 *number_tweets
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 100*

 )
 


 →
 

[langchain.document_loaders.twitter.TwitterTweetLoader](#langchain.document_loaders.TwitterTweetLoader "langchain.document_loaders.twitter.TwitterTweetLoader")


[[source]](../../_modules/langchain/document_loaders/twitter#TwitterTweetLoader.from_bearer_token)
[#](#langchain.document_loaders.TwitterTweetLoader.from_bearer_token "Permalink to this definition") 



 Create a TwitterTweetLoader from OAuth2 bearer token.
 






*classmethod*


 from_secrets
 


 (
 
*access_token
 



 :
 





 str*
 ,
 *access_token_secret
 



 :
 





 str*
 ,
 *consumer_key
 



 :
 





 str*
 ,
 *consumer_secret
 



 :
 





 str*
 ,
 *twitter_users
 



 :
 





 Sequence
 


 [
 


 str
 


 ]*
 ,
 *number_tweets
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 100*

 )
 


 →
 

[langchain.document_loaders.twitter.TwitterTweetLoader](#langchain.document_loaders.TwitterTweetLoader "langchain.document_loaders.twitter.TwitterTweetLoader")


[[source]](../../_modules/langchain/document_loaders/twitter#TwitterTweetLoader.from_secrets)
[#](#langchain.document_loaders.TwitterTweetLoader.from_secrets "Permalink to this definition") 



 Create a TwitterTweetLoader from access tokens and secrets.
 








 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/twitter#TwitterTweetLoader.load)
[#](#langchain.document_loaders.TwitterTweetLoader.load "Permalink to this definition") 



 Load tweets.
 








*class*


 langchain.document_loaders.
 



 UnstructuredEPubLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/epub#UnstructuredEPubLoader)
[#](#langchain.document_loaders.UnstructuredEPubLoader "Permalink to this definition") 



 Loader that uses unstructured to load epub files.
 






*class*


 langchain.document_loaders.
 



 UnstructuredEmailLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/email#UnstructuredEmailLoader)
[#](#langchain.document_loaders.UnstructuredEmailLoader "Permalink to this definition") 



 Loader that uses unstructured to load email files.
 






*class*


 langchain.document_loaders.
 



 UnstructuredFileIOLoader
 


 (
 
*file
 



 :
 





 IO*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/unstructured#UnstructuredFileIOLoader)
[#](#langchain.document_loaders.UnstructuredFileIOLoader "Permalink to this definition") 



 Loader that uses unstructured to load file IO objects.
 






*class*


 langchain.document_loaders.
 



 UnstructuredFileLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/unstructured#UnstructuredFileLoader)
[#](#langchain.document_loaders.UnstructuredFileLoader "Permalink to this definition") 



 Loader that uses unstructured to load files.
 






*class*


 langchain.document_loaders.
 



 UnstructuredHTMLLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/html#UnstructuredHTMLLoader)
[#](#langchain.document_loaders.UnstructuredHTMLLoader "Permalink to this definition") 



 Loader that uses unstructured to load HTML files.
 






*class*


 langchain.document_loaders.
 



 UnstructuredImageLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/image#UnstructuredImageLoader)
[#](#langchain.document_loaders.UnstructuredImageLoader "Permalink to this definition") 



 Loader that uses unstructured to load image files, such as PNGs and JPGs.
 






*class*


 langchain.document_loaders.
 



 UnstructuredMarkdownLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/markdown#UnstructuredMarkdownLoader)
[#](#langchain.document_loaders.UnstructuredMarkdownLoader "Permalink to this definition") 



 Loader that uses unstructured to load markdown files.
 






*class*


 langchain.document_loaders.
 



 UnstructuredPDFLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/pdf#UnstructuredPDFLoader)
[#](#langchain.document_loaders.UnstructuredPDFLoader "Permalink to this definition") 



 Loader that uses unstructured to load PDF files.
 






*class*


 langchain.document_loaders.
 



 UnstructuredPowerPointLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/powerpoint#UnstructuredPowerPointLoader)
[#](#langchain.document_loaders.UnstructuredPowerPointLoader "Permalink to this definition") 



 Loader that uses unstructured to load powerpoint files.
 






*class*


 langchain.document_loaders.
 



 UnstructuredRTFLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/rtf#UnstructuredRTFLoader)
[#](#langchain.document_loaders.UnstructuredRTFLoader "Permalink to this definition") 



 Loader that uses unstructured to load rtf files.
 






*class*


 langchain.document_loaders.
 



 UnstructuredURLLoader
 


 (
 
*urls
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *continue_on_failure
 



 :
 





 bool
 





 =
 





 True*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/url#UnstructuredURLLoader)
[#](#langchain.document_loaders.UnstructuredURLLoader "Permalink to this definition") 



 Loader that uses unstructured to load HTML files.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/url#UnstructuredURLLoader.load)
[#](#langchain.document_loaders.UnstructuredURLLoader.load "Permalink to this definition") 



 Load file.
 








*class*


 langchain.document_loaders.
 



 UnstructuredWordDocumentLoader
 


 (
 
*file_path
 



 :
 





 str*
 ,
 *mode
 



 :
 





 str
 





 =
 





 'single'*
 ,
 *\*\*
 



 unstructured_kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/document_loaders/word_document#UnstructuredWordDocumentLoader)
[#](#langchain.document_loaders.UnstructuredWordDocumentLoader "Permalink to this definition") 



 Loader that uses unstructured to load word documents.
 






*class*


 langchain.document_loaders.
 



 WebBaseLoader
 


 (
 
*web_path
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ]*
 ,
 *header_template
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/document_loaders/web_base#WebBaseLoader)
[#](#langchain.document_loaders.WebBaseLoader "Permalink to this definition") 



 Loader that uses urllib and beautiful soup to load webpages.
 






 aload
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/web_base#WebBaseLoader.aload)
[#](#langchain.document_loaders.WebBaseLoader.aload "Permalink to this definition") 



 Load text from the urls in web_path async into Documents.
 








 default_parser
 

*:
 




 str*
*=
 




 'html.parser'*
[#](#langchain.document_loaders.WebBaseLoader.default_parser "Permalink to this definition") 



 Default parser to use for BeautifulSoup.
 






*async*


 fetch_all
 


 (
 
*urls
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 Any
 


[[source]](../../_modules/langchain/document_loaders/web_base#WebBaseLoader.fetch_all)
[#](#langchain.document_loaders.WebBaseLoader.fetch_all "Permalink to this definition") 



 Fetch all urls concurrently with rate limiting.
 








 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/web_base#WebBaseLoader.load)
[#](#langchain.document_loaders.WebBaseLoader.load "Permalink to this definition") 



 Load text from the url(s) in web_path.
 








 requests_per_second
 

*:
 




 int*
*=
 




 2*
[#](#langchain.document_loaders.WebBaseLoader.requests_per_second "Permalink to this definition") 



 Max number of concurrent requests to make.
 








 scrape
 


 (
 
*parser
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 


 →
 


 Any
 


[[source]](../../_modules/langchain/document_loaders/web_base#WebBaseLoader.scrape)
[#](#langchain.document_loaders.WebBaseLoader.scrape "Permalink to this definition") 



 Scrape data from webpage and return it in BeautifulSoup format.
 








 scrape_all
 


 (
 
*urls
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *parser
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 


 →
 


 List
 


 [
 


 Any
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/web_base#WebBaseLoader.scrape_all)
[#](#langchain.document_loaders.WebBaseLoader.scrape_all "Permalink to this definition") 



 Fetch all urls, then return soups for all results.
 






*property*


 web_path
 

*:
 




 str*
[#](#langchain.document_loaders.WebBaseLoader.web_path "Permalink to this definition") 








 web_paths
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.document_loaders.WebBaseLoader.web_paths "Permalink to this definition") 








*class*


 langchain.document_loaders.
 



 WhatsAppChatLoader
 


 (
 
*path
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/document_loaders/whatsapp_chat#WhatsAppChatLoader)
[#](#langchain.document_loaders.WhatsAppChatLoader "Permalink to this definition") 



 Loader that loads WhatsApp messages text file.
 






 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/whatsapp_chat#WhatsAppChatLoader.load)
[#](#langchain.document_loaders.WhatsAppChatLoader.load "Permalink to this definition") 



 Load documents.
 








*class*


 langchain.document_loaders.
 



 YoutubeLoader
 


 (
 
*video_id
 



 :
 





 str*
 ,
 *add_video_info
 



 :
 





 bool
 





 =
 





 False*
 ,
 *language
 



 :
 





 str
 





 =
 





 'en'*
 ,
 *continue_on_failure
 



 :
 





 bool
 





 =
 





 False*

 )
 
[[source]](../../_modules/langchain/document_loaders/youtube#YoutubeLoader)
[#](#langchain.document_loaders.YoutubeLoader "Permalink to this definition") 



 Loader that loads Youtube transcripts.
 




*classmethod*


 from_youtube_url
 


 (
 
*youtube_url
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.document_loaders.youtube.YoutubeLoader](#langchain.document_loaders.YoutubeLoader "langchain.document_loaders.youtube.YoutubeLoader")


[[source]](../../_modules/langchain/document_loaders/youtube#YoutubeLoader.from_youtube_url)
[#](#langchain.document_loaders.YoutubeLoader.from_youtube_url "Permalink to this definition") 



 Given youtube URL, load video.
 








 load
 


 (
 

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_loaders/youtube#YoutubeLoader.load)
[#](#langchain.document_loaders.YoutubeLoader.load "Permalink to this definition") 



 Load documents.
 








