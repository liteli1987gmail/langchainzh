


 OpenSearch
 [#](#opensearch "Permalink to this headline")
===========================================================



> 
> 
> 
> [OpenSearch](https://opensearch.org/) 
>  is a scalable, flexible, and extensible open-source software suite for search, analytics, and observability applications licensed under Apache 2.0.
>  `OpenSearch`
>  is a distributed search and analytics engine based on
>  `Apache
>  
> 
>  Lucene`
>  .
>  
> 
> 
> 
> 



 This notebook shows how to use functionality related to the
 `OpenSearch`
 database.
 



 To run, you should have the opensearch instance up and running:
 [here](https://opensearch.org/docs/latest/install-and-configure/install-opensearch/index/) 
`similarity_search`
 by default performs the Approximate k-NN Search which uses one of the several algorithms like lucene, nmslib, faiss recommended for
large datasets. To perform brute force search we have other search methods known as Script Scoring and Painless Scripting.
Check
 [this](https://opensearch.org/docs/latest/search-plugins/knn/index/) 
 for more details.
 







```
!pip install opensearch-py

```






 We want to use OpenAIEmbeddings so we have to get the OpenAI API Key.
 







```
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

```










```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import OpenSearchVectorSearch
from langchain.document_loaders import TextLoader

```










```
from langchain.document_loaders import TextLoader
loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

```










```
docsearch = OpenSearchVectorSearch.from_documents(docs, embeddings, opensearch_url="http://localhost:9200")

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)

```










```
print(docs[0].page_content)

```







 similarity_search using Approximate k-NN Search with Custom Parameters
 [#](#similarity-search-using-approximate-k-nn-search-with-custom-parameters "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







```
docsearch = OpenSearchVectorSearch.from_documents(docs, embeddings, opensearch_url="http://localhost:9200", engine="faiss", space_type="innerproduct", ef_construction=256, m=48)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)

```










```
print(docs[0].page_content)

```








 similarity_search using Script Scoring with Custom Parameters
 [#](#similarity-search-using-script-scoring-with-custom-parameters "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------







```
docsearch = OpenSearchVectorSearch.from_documents(docs, embeddings, opensearch_url="http://localhost:9200", is_appx_search=False)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search("What did the president say about Ketanji Brown Jackson", k=1, search_type="script_scoring")

```










```
print(docs[0].page_content)

```








 similarity_search using Painless Scripting with Custom Parameters
 [#](#similarity-search-using-painless-scripting-with-custom-parameters "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------







```
docsearch = OpenSearchVectorSearch.from_documents(docs, embeddings, opensearch_url="http://localhost:9200", is_appx_search=False)
filter = {"bool": {"filter": {"term": {"text": "smuggling"}}}}
query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search("What did the president say about Ketanji Brown Jackson", search_type="painless_scripting", space_type="cosineSimilarity", pre_filter=filter)

```










```
print(docs[0].page_content)

```








 Using a preexisting OpenSearch instance
 [#](#using-a-preexisting-opensearch-instance "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------



 It’s also possible to use a preexisting OpenSearch instance with documents that already have vectors present.
 







```
# this is just an example, you would need to change these values to point to another opensearch instance
docsearch = OpenSearchVectorSearch(index_name="index-\*", embedding_function=embeddings, opensearch_url="http://localhost:9200")

# you can specify custom field names to match the fields you're using to store your embedding, document text value, and metadata
docs = docsearch.similarity_search("Who was asking about getting lunch today?", search_type="script_scoring", space_type="cosinesimil", vector_field="message_embedding", text_field="message", metadata_field="message_metadata")

```








