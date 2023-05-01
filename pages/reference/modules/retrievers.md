




 Retrievers
 [#](#module-langchain.retrievers "Permalink to this headline")
============================================================================




*pydantic
 

 model*


 langchain.retrievers.
 



 ChatGPTPluginRetriever
 

[[source]](../../_modules/langchain/retrievers/chatgpt_plugin_retriever#ChatGPTPluginRetriever)
[#](#langchain.retrievers.ChatGPTPluginRetriever "Permalink to this definition") 




*field*


 aiosession
 

*:
 




 Optional
 


 [
 


 aiohttp.client.ClientSession
 


 ]*
*=
 




 None*
[#](#langchain.retrievers.ChatGPTPluginRetriever.aiosession "Permalink to this definition") 






*field*


 bearer_token
 

*:
 




 str*
*[Required]*
[#](#langchain.retrievers.ChatGPTPluginRetriever.bearer_token "Permalink to this definition") 






*field*


 filter
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.retrievers.ChatGPTPluginRetriever.filter "Permalink to this definition") 






*field*


 top_k
 

*:
 




 int*
*=
 




 3*
[#](#langchain.retrievers.ChatGPTPluginRetriever.top_k "Permalink to this definition") 






*field*


 url
 

*:
 




 str*
*[Required]*
[#](#langchain.retrievers.ChatGPTPluginRetriever.url "Permalink to this definition") 






*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/chatgpt_plugin_retriever#ChatGPTPluginRetriever.aget_relevant_documents)
[#](#langchain.retrievers.ChatGPTPluginRetriever.aget_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/chatgpt_plugin_retriever#ChatGPTPluginRetriever.get_relevant_documents)
[#](#langchain.retrievers.ChatGPTPluginRetriever.get_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










*pydantic
 

 model*


 langchain.retrievers.
 



 ContextualCompressionRetriever
 

[[source]](../../_modules/langchain/retrievers/contextual_compression#ContextualCompressionRetriever)
[#](#langchain.retrievers.ContextualCompressionRetriever "Permalink to this definition") 



 Retriever that wraps a base retriever and compresses the results.
 




*field*


 base_compressor
 

*:
 




 langchain.retrievers.document_compressors.base.BaseDocumentCompressor*
*[Required]*
[#](#langchain.retrievers.ContextualCompressionRetriever.base_compressor "Permalink to this definition") 



 Compressor for compressing retrieved documents.
 






*field*


 base_retriever
 

*:
 




 langchain.schema.BaseRetriever*
*[Required]*
[#](#langchain.retrievers.ContextualCompressionRetriever.base_retriever "Permalink to this definition") 



 Base Retriever to use for getting relevant documents.
 






*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/contextual_compression#ContextualCompressionRetriever.aget_relevant_documents)
[#](#langchain.retrievers.ContextualCompressionRetriever.aget_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/contextual_compression#ContextualCompressionRetriever.get_relevant_documents)
[#](#langchain.retrievers.ContextualCompressionRetriever.get_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 Sequence of relevant documents
 










*class*


 langchain.retrievers.
 



 DataberryRetriever
 


 (
 
*datastore_url
 



 :
 





 str*
 ,
 *top_k
 



 :
 





 Optional
 


 [
 


 int
 


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

 )
 
[[source]](../../_modules/langchain/retrievers/databerry#DataberryRetriever)
[#](#langchain.retrievers.DataberryRetriever "Permalink to this definition") 




*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/databerry#DataberryRetriever.aget_relevant_documents)
[#](#langchain.retrievers.DataberryRetriever.aget_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










 api_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
[#](#langchain.retrievers.DataberryRetriever.api_key "Permalink to this definition") 








 datastore_url
 

*:
 




 str*
[#](#langchain.retrievers.DataberryRetriever.datastore_url "Permalink to this definition") 








 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/databerry#DataberryRetriever.get_relevant_documents)
[#](#langchain.retrievers.DataberryRetriever.get_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










 top_k
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
[#](#langchain.retrievers.DataberryRetriever.top_k "Permalink to this definition") 








*class*


 langchain.retrievers.
 



 ElasticSearchBM25Retriever
 


 (
 
*client
 



 :
 





 Any*
 ,
 *index_name
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/retrievers/elastic_search_bm25#ElasticSearchBM25Retriever)
[#](#langchain.retrievers.ElasticSearchBM25Retriever "Permalink to this definition") 



 Wrapper around Elasticsearch using BM25 as a retrieval method.
 



 To connect to an Elasticsearch instance that requires login credentials,
including Elastic Cloud, use the Elasticsearch URL format
 <https://username:password@es_host:9243>
 . For example, to connect to Elastic
Cloud, create the Elasticsearch URL with the required authentication details and
pass it to the ElasticVectorSearch constructor as the named parameter
elasticsearch_url.
 



 You can obtain your Elastic Cloud URL and login credentials by logging in to the
Elastic Cloud console at
 <https://cloud.elastic.co>
 , selecting your deployment, and
navigating to the “Deployments” page.
 



 To obtain your Elastic Cloud password for the default “elastic” user:
 


1. Log in to the Elastic Cloud console at
 <https://cloud.elastic.co>
2. Go to “Security” > “Users”
3. Locate the “elastic” user and click “Edit”
4. Click “Reset password”
5. Follow the prompts to reset the password



 The format for Elastic Cloud URLs is
 <https://username:password@cluster_id.region_id.gcp.cloud.es.io:9243>
 .
 






 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *refresh_indices
 



 :
 





 bool
 





 =
 





 True*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/retrievers/elastic_search_bm25#ElasticSearchBM25Retriever.add_texts)
[#](#langchain.retrievers.ElasticSearchBM25Retriever.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the retriver.
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the retriever.
* **refresh_indices** 
 – bool to refresh ElasticSearch indices




 Returns
 


 List of ids from adding the texts into the retriever.
 








*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/elastic_search_bm25#ElasticSearchBM25Retriever.aget_relevant_documents)
[#](#langchain.retrievers.ElasticSearchBM25Retriever.aget_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 








*classmethod*


 create
 


 (
 
*elasticsearch_url
 



 :
 





 str*
 ,
 *index_name
 



 :
 





 str*
 ,
 *k1
 



 :
 





 float
 





 =
 





 2.0*
 ,
 *b
 



 :
 





 float
 





 =
 





 0.75*

 )
 


 →
 

[langchain.retrievers.elastic_search_bm25.ElasticSearchBM25Retriever](#langchain.retrievers.ElasticSearchBM25Retriever "langchain.retrievers.elastic_search_bm25.ElasticSearchBM25Retriever")


[[source]](../../_modules/langchain/retrievers/elastic_search_bm25#ElasticSearchBM25Retriever.create)
[#](#langchain.retrievers.ElasticSearchBM25Retriever.create "Permalink to this definition") 








 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/elastic_search_bm25#ElasticSearchBM25Retriever.get_relevant_documents)
[#](#langchain.retrievers.ElasticSearchBM25Retriever.get_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










*class*


 langchain.retrievers.
 



 MetalRetriever
 


 (
 
*client
 



 :
 





 Any*
 ,
 *params
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/retrievers/metal#MetalRetriever)
[#](#langchain.retrievers.MetalRetriever "Permalink to this definition") 




*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/metal#MetalRetriever.aget_relevant_documents)
[#](#langchain.retrievers.MetalRetriever.aget_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/metal#MetalRetriever.get_relevant_documents)
[#](#langchain.retrievers.MetalRetriever.get_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










*pydantic
 

 model*


 langchain.retrievers.
 



 PineconeHybridSearchRetriever
 

[[source]](../../_modules/langchain/retrievers/pinecone_hybrid_search#PineconeHybridSearchRetriever)
[#](#langchain.retrievers.PineconeHybridSearchRetriever "Permalink to this definition") 




*field*


 alpha
 

*:
 




 float*
*=
 




 0.5*
[#](#langchain.retrievers.PineconeHybridSearchRetriever.alpha "Permalink to this definition") 






*field*


 embeddings
 

*:
 




 langchain.embeddings.base.Embeddings*
*[Required]*
[#](#langchain.retrievers.PineconeHybridSearchRetriever.embeddings "Permalink to this definition") 






*field*


 index
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.retrievers.PineconeHybridSearchRetriever.index "Permalink to this definition") 






*field*


 sparse_encoder
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.retrievers.PineconeHybridSearchRetriever.sparse_encoder "Permalink to this definition") 






*field*


 top_k
 

*:
 




 int*
*=
 




 4*
[#](#langchain.retrievers.PineconeHybridSearchRetriever.top_k "Permalink to this definition") 








 add_texts
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *ids
 



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
 


 →
 


 None
 


[[source]](../../_modules/langchain/retrievers/pinecone_hybrid_search#PineconeHybridSearchRetriever.add_texts)
[#](#langchain.retrievers.PineconeHybridSearchRetriever.add_texts "Permalink to this definition") 






*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/pinecone_hybrid_search#PineconeHybridSearchRetriever.aget_relevant_documents)
[#](#langchain.retrievers.PineconeHybridSearchRetriever.aget_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/pinecone_hybrid_search#PineconeHybridSearchRetriever.get_relevant_documents)
[#](#langchain.retrievers.PineconeHybridSearchRetriever.get_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










*pydantic
 

 model*


 langchain.retrievers.
 



 RemoteLangChainRetriever
 

[[source]](../../_modules/langchain/retrievers/remote_retriever#RemoteLangChainRetriever)
[#](#langchain.retrievers.RemoteLangChainRetriever "Permalink to this definition") 




*field*


 headers
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.retrievers.RemoteLangChainRetriever.headers "Permalink to this definition") 






*field*


 input_key
 

*:
 




 str*
*=
 




 'message'*
[#](#langchain.retrievers.RemoteLangChainRetriever.input_key "Permalink to this definition") 






*field*


 metadata_key
 

*:
 




 str*
*=
 




 'metadata'*
[#](#langchain.retrievers.RemoteLangChainRetriever.metadata_key "Permalink to this definition") 






*field*


 page_content_key
 

*:
 




 str*
*=
 




 'page_content'*
[#](#langchain.retrievers.RemoteLangChainRetriever.page_content_key "Permalink to this definition") 






*field*


 response_key
 

*:
 




 str*
*=
 




 'response'*
[#](#langchain.retrievers.RemoteLangChainRetriever.response_key "Permalink to this definition") 






*field*


 url
 

*:
 




 str*
*[Required]*
[#](#langchain.retrievers.RemoteLangChainRetriever.url "Permalink to this definition") 






*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/remote_retriever#RemoteLangChainRetriever.aget_relevant_documents)
[#](#langchain.retrievers.RemoteLangChainRetriever.aget_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/remote_retriever#RemoteLangChainRetriever.get_relevant_documents)
[#](#langchain.retrievers.RemoteLangChainRetriever.get_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










*pydantic
 

 model*


 langchain.retrievers.
 



 SVMRetriever
 

[[source]](../../_modules/langchain/retrievers/svm#SVMRetriever)
[#](#langchain.retrievers.SVMRetriever "Permalink to this definition") 




*field*


 embeddings
 

*:
 




 langchain.embeddings.base.Embeddings*
*[Required]*
[#](#langchain.retrievers.SVMRetriever.embeddings "Permalink to this definition") 






*field*


 index
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.retrievers.SVMRetriever.index "Permalink to this definition") 






*field*


 k
 

*:
 




 int*
*=
 




 4*
[#](#langchain.retrievers.SVMRetriever.k "Permalink to this definition") 






*field*


 relevancy_threshold
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 None*
[#](#langchain.retrievers.SVMRetriever.relevancy_threshold "Permalink to this definition") 






*field*


 texts
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Required]*
[#](#langchain.retrievers.SVMRetriever.texts "Permalink to this definition") 






*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/svm#SVMRetriever.aget_relevant_documents)
[#](#langchain.retrievers.SVMRetriever.aget_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 








*classmethod*


 from_texts
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *embeddings
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.retrievers.svm.SVMRetriever](#langchain.retrievers.SVMRetriever "langchain.retrievers.svm.SVMRetriever")


[[source]](../../_modules/langchain/retrievers/svm#SVMRetriever.from_texts)
[#](#langchain.retrievers.SVMRetriever.from_texts "Permalink to this definition") 








 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/svm#SVMRetriever.get_relevant_documents)
[#](#langchain.retrievers.SVMRetriever.get_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










*pydantic
 

 model*


 langchain.retrievers.
 



 TFIDFRetriever
 

[[source]](../../_modules/langchain/retrievers/tfidf#TFIDFRetriever)
[#](#langchain.retrievers.TFIDFRetriever "Permalink to this definition") 




*field*


 docs
 

*:
 




 List
 


 [
 


 langchain.schema.Document
 


 ]*
*[Required]*
[#](#langchain.retrievers.TFIDFRetriever.docs "Permalink to this definition") 






*field*


 k
 

*:
 




 int*
*=
 




 4*
[#](#langchain.retrievers.TFIDFRetriever.k "Permalink to this definition") 






*field*


 tfidf_array
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.retrievers.TFIDFRetriever.tfidf_array "Permalink to this definition") 






*field*


 vectorizer
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.retrievers.TFIDFRetriever.vectorizer "Permalink to this definition") 






*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/tfidf#TFIDFRetriever.aget_relevant_documents)
[#](#langchain.retrievers.TFIDFRetriever.aget_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 








*classmethod*


 from_texts
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *tfidf_params
 



 :
 





 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.retrievers.tfidf.TFIDFRetriever](#langchain.retrievers.TFIDFRetriever "langchain.retrievers.tfidf.TFIDFRetriever")


[[source]](../../_modules/langchain/retrievers/tfidf#TFIDFRetriever.from_texts)
[#](#langchain.retrievers.TFIDFRetriever.from_texts "Permalink to this definition") 








 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/tfidf#TFIDFRetriever.get_relevant_documents)
[#](#langchain.retrievers.TFIDFRetriever.get_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










*pydantic
 

 model*


 langchain.retrievers.
 



 TimeWeightedVectorStoreRetriever
 

[[source]](../../_modules/langchain/retrievers/time_weighted_retriever#TimeWeightedVectorStoreRetriever)
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever "Permalink to this definition") 



 Retriever combining embededing similarity with recency.
 




*field*


 decay_rate
 

*:
 




 float*
*=
 




 0.01*
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.decay_rate "Permalink to this definition") 



 The exponential decay factor used as (1.0-decay_rate)\*\*(hrs_passed).
 






*field*


 default_salience
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 None*
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.default_salience "Permalink to this definition") 



 The salience to assign memories not retrieved from the vector store.
 



 None assigns no salience to documents not fetched from the vector store.
 






*field*


 k
 

*:
 




 int*
*=
 




 4*
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.k "Permalink to this definition") 



 The maximum number of documents to retrieve in a given call.
 






*field*


 memory_stream
 

*:
 




 List
 


 [
 


 langchain.schema.Document
 


 ]*
*[Optional]*
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.memory_stream "Permalink to this definition") 



 The memory_stream of documents to search through.
 






*field*


 other_score_keys
 

*:
 




 List
 


 [
 


 str
 


 ]*
*=
 




 []*
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.other_score_keys "Permalink to this definition") 



 Other keys in the metadata to factor into the score, e.g. ‘importance’.
 






*field*


 search_kwargs
 

*:
 




 dict*
*[Optional]*
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.search_kwargs "Permalink to this definition") 



 Keyword arguments to pass to the vectorstore similarity search.
 






*field*


 vectorstore
 

*:
 



[langchain.vectorstores.base.VectorStore](vectorstores#langchain.vectorstores.VectorStore "langchain.vectorstores.base.VectorStore")*
*[Required]*
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.vectorstore "Permalink to this definition") 



 The vectorstore to store documents and determine salience.
 






*async*


 aadd_documents
 


 (
 
*documents
 



 :
 





 List
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/retrievers/time_weighted_retriever#TimeWeightedVectorStoreRetriever.aadd_documents)
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.aadd_documents "Permalink to this definition") 



 Add documents to vectorstore.
 








 add_documents
 


 (
 
*documents
 



 :
 





 List
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/retrievers/time_weighted_retriever#TimeWeightedVectorStoreRetriever.add_documents)
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.add_documents "Permalink to this definition") 



 Add documents to vectorstore.
 






*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/time_weighted_retriever#TimeWeightedVectorStoreRetriever.aget_relevant_documents)
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.aget_relevant_documents "Permalink to this definition") 



 Return documents that are relevant to the query.
 








 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/time_weighted_retriever#TimeWeightedVectorStoreRetriever.get_relevant_documents)
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.get_relevant_documents "Permalink to this definition") 



 Return documents that are relevant to the query.
 








 get_salient_docs
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 Dict
 


 [
 


 int
 


 ,
 




 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/retrievers/time_weighted_retriever#TimeWeightedVectorStoreRetriever.get_salient_docs)
[#](#langchain.retrievers.TimeWeightedVectorStoreRetriever.get_salient_docs "Permalink to this definition") 



 Return documents that are salient to the query.
 








*class*


 langchain.retrievers.
 



 VespaRetriever
 


 (
 
*app
 



 :
 





 Vespa*
 ,
 *body
 



 :
 





 dict*
 ,
 *content_field
 



 :
 





 str*

 )
 
[[source]](../../_modules/langchain/retrievers/vespa_retriever#VespaRetriever)
[#](#langchain.retrievers.VespaRetriever "Permalink to this definition") 




*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/vespa_retriever#VespaRetriever.aget_relevant_documents)
[#](#langchain.retrievers.VespaRetriever.aget_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/vespa_retriever#VespaRetriever.get_relevant_documents)
[#](#langchain.retrievers.VespaRetriever.get_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










*class*


 langchain.retrievers.
 



 WeaviateHybridSearchRetriever
 


 (
 
*client
 



 :
 





 Any*
 ,
 *index_name
 



 :
 





 str*
 ,
 *text_key
 



 :
 





 str*
 ,
 *alpha
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *attributes
 



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
 
[[source]](../../_modules/langchain/retrievers/weaviate_hybrid_search#WeaviateHybridSearchRetriever)
[#](#langchain.retrievers.WeaviateHybridSearchRetriever "Permalink to this definition") 




*class*


 Config
 

[[source]](../../_modules/langchain/retrievers/weaviate_hybrid_search#WeaviateHybridSearchRetriever.Config)
[#](#langchain.retrievers.WeaviateHybridSearchRetriever.Config "Permalink to this definition") 



 Configuration for this pydantic object.
 






 arbitrary_types_allowed
 

*=
 




 True*
[#](#langchain.retrievers.WeaviateHybridSearchRetriever.Config.arbitrary_types_allowed "Permalink to this definition") 








 extra
 

*=
 




 'forbid'*
[#](#langchain.retrievers.WeaviateHybridSearchRetriever.Config.extra "Permalink to this definition") 










 add_documents
 


 (
 
*docs
 



 :
 





 List
 


 [
 


 langchain.schema.Document
 


 ]*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/retrievers/weaviate_hybrid_search#WeaviateHybridSearchRetriever.add_documents)
[#](#langchain.retrievers.WeaviateHybridSearchRetriever.add_documents "Permalink to this definition") 



 Upload documents to Weaviate.
 






*async*


 aget_relevant_documents
 


 (
 
*query
 



 :
 





 str*
 ,
 *where_filter
 



 :
 





 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 object
 


 ]
 



 ]
 






 =
 





 None*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/weaviate_hybrid_search#WeaviateHybridSearchRetriever.aget_relevant_documents)
[#](#langchain.retrievers.WeaviateHybridSearchRetriever.aget_relevant_documents "Permalink to this definition") 



 Get documents relevant for a query.
 




 Parameters
 


**query** 
 – string to find relevant documents for
 




 Returns
 


 List of relevant documents
 










 get_relevant_documents
 


 (
 
*query
 



 :
 





 str*
 ,
 *where_filter
 



 :
 





 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 object
 


 ]
 



 ]
 






 =
 





 None*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/weaviate_hybrid_search#WeaviateHybridSearchRetriever.get_relevant_documents)
[#](#langchain.retrievers.WeaviateHybridSearchRetriever.get_relevant_documents "Permalink to this definition") 



 Look up similar documents in Weaviate.
 








