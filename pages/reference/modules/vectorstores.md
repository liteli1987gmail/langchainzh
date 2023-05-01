




 Vector Stores
 [#](#module-langchain.vectorstores "Permalink to this headline")
=================================================================================



 Wrappers on top of vector stores.
 




*class*


 langchain.vectorstores.
 



 AnalyticDB
 


 (
 
*connection_string
 



 :
 





 str*
 ,
 *embedding_function
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *collection_name
 



 :
 





 str
 





 =
 





 'langchain'*
 ,
 *collection_metadata
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *pre_delete_collection
 



 :
 





 bool
 





 =
 





 False*
 ,
 *logger
 



 :
 





 Optional
 


 [
 


 logging.Logger
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB)
[#](#langchain.vectorstores.AnalyticDB "Permalink to this definition") 



 VectorStore implementation using AnalyticDB.
AnalyticDB is a distributed full PostgresSQL syntax cloud-native database.
-
 
 connection_string
 
 is a postgres connection string.
-
 
 embedding_function
 
 any embedding function implementing
 



> 
> 
> 
> 
>  langchain.embeddings.base.Embeddings
>  
>  interface.
>  
> 
> 
> 
> 


* collection_name
 
 is the name of the collection to use. (default: langchain)
 


	+ NOTE: This is not the name of the table, but the name of the collection.
	 
	
	
	 The tables will be created when initializing the store (if not exists)
	So, make sure the user has the right permissions to create tables.
* pre_delete_collection
 
 if True, will delete the collection if it exists.
 


 (default: False)
- Useful for testing.






 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
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
 



[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.add_texts)
[#](#langchain.vectorstores.AnalyticDB.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the vectorstore.
* **metadatas** 
 – Optional list of metadatas associated with the texts.
* **kwargs** 
 – vectorstore specific parameters




 Returns
 


 List of ids from adding the texts into the vectorstore.
 










 connect
 


 (
 

 )
 


 →
 


 sqlalchemy.engine.base.Connection
 


[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.connect)
[#](#langchain.vectorstores.AnalyticDB.connect "Permalink to this definition") 






*classmethod*


 connection_string_from_db_params
 


 (
 
*driver
 



 :
 





 str*
 ,
 *host
 



 :
 





 str*
 ,
 *port
 



 :
 





 int*
 ,
 *database
 



 :
 





 str*
 ,
 *user
 



 :
 





 str*
 ,
 *password
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.connection_string_from_db_params)
[#](#langchain.vectorstores.AnalyticDB.connection_string_from_db_params "Permalink to this definition") 



 Return connection string from database parameters.
 








 create_collection
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.create_collection)
[#](#langchain.vectorstores.AnalyticDB.create_collection "Permalink to this definition") 








 create_tables_if_not_exists
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.create_tables_if_not_exists)
[#](#langchain.vectorstores.AnalyticDB.create_tables_if_not_exists "Permalink to this definition") 








 delete_collection
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.delete_collection)
[#](#langchain.vectorstores.AnalyticDB.delete_collection "Permalink to this definition") 








 drop_tables
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.drop_tables)
[#](#langchain.vectorstores.AnalyticDB.drop_tables "Permalink to this definition") 






*classmethod*


 from_documents
 


 (
 
*documents
 



 :
 





 List
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *collection_name
 



 :
 





 str
 





 =
 





 'langchain'*
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
 ,
 *pre_delete_collection
 



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
 


 →
 

[langchain.vectorstores.analyticdb.AnalyticDB](#langchain.vectorstores.AnalyticDB "langchain.vectorstores.analyticdb.AnalyticDB")


[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.from_documents)
[#](#langchain.vectorstores.AnalyticDB.from_documents "Permalink to this definition") 



 Return VectorStore initialized from documents and embeddings.
Postgres connection string is required
Either pass it as a parameter
or set the PGVECTOR_CONNECTION_STRING environment variable.
 






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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *collection_name
 



 :
 





 str
 





 =
 





 'langchain'*
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
 ,
 *pre_delete_collection
 



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
 


 →
 

[langchain.vectorstores.analyticdb.AnalyticDB](#langchain.vectorstores.AnalyticDB "langchain.vectorstores.analyticdb.AnalyticDB")


[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.from_texts)
[#](#langchain.vectorstores.AnalyticDB.from_texts "Permalink to this definition") 



 Return VectorStore initialized from texts and embeddings.
Postgres connection string is required
Either pass it as a parameter
or set the PGVECTOR_CONNECTION_STRING environment variable.
 








 get_collection
 


 (
 
*session
 



 :
 





 sqlalchemy.orm.session.Session*

 )
 


 →
 


 Optional
 


 [
 


 CollectionStore
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.get_collection)
[#](#langchain.vectorstores.AnalyticDB.get_collection "Permalink to this definition") 






*classmethod*


 get_connection_string
 


 (
 
*kwargs
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.get_connection_string)
[#](#langchain.vectorstores.AnalyticDB.get_connection_string "Permalink to this definition") 








 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



 :
 





 Optional
 


 [
 


 dict
 


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
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.similarity_search)
[#](#langchain.vectorstores.AnalyticDB.similarity_search "Permalink to this definition") 



 Run similarity search with AnalyticDB with distance.
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – Query text to search for.
* **k** 
 (
 *int* 
 ) – Number of results to return. Defaults to 4.
* **filter** 
 (
 *Optional* 
*[* 
*Dict* 
*[* 
*str* 
*,* 
*str* 
*]* 
*]* 
 ) – Filter by metadata. Defaults to None.




 Returns
 


 List of Documents most similar to the query.
 










 similarity_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



 :
 





 Optional
 


 [
 


 dict
 


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
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.similarity_search_by_vector)
[#](#langchain.vectorstores.AnalyticDB.similarity_search_by_vector "Permalink to this definition") 



 Return docs most similar to embedding vector.
 




 Parameters
 

* **embedding** 
 – Embedding to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **filter** 
 (
 *Optional* 
*[* 
*Dict* 
*[* 
*str* 
*,* 
*str* 
*]* 
*]* 
 ) – Filter by metadata. Defaults to None.




 Returns
 


 List of Documents most similar to the query vector.
 










 similarity_search_with_score
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.similarity_search_with_score)
[#](#langchain.vectorstores.AnalyticDB.similarity_search_with_score "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **filter** 
 (
 *Optional* 
*[* 
*Dict* 
*[* 
*str* 
*,* 
*str* 
*]* 
*]* 
 ) – Filter by metadata. Defaults to None.




 Returns
 


 List of Documents most similar to the query and score for each
 










 similarity_search_with_score_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/analyticdb#AnalyticDB.similarity_search_with_score_by_vector)
[#](#langchain.vectorstores.AnalyticDB.similarity_search_with_score_by_vector "Permalink to this definition") 








*class*


 langchain.vectorstores.
 



 Annoy
 


 (
 
*embedding_function
 



 :
 





 Callable*
 ,
 *index
 



 :
 





 Any*
 ,
 *metric
 



 :
 





 str*
 ,
 *docstore
 



 :
 





 langchain.docstore.base.Docstore*
 ,
 *index_to_docstore_id
 



 :
 





 Dict
 


 [
 


 int
 


 ,
 




 str
 


 ]*

 )
 
[[source]](../../_modules/langchain/vectorstores/annoy#Annoy)
[#](#langchain.vectorstores.Annoy "Permalink to this definition") 



 Wrapper around Annoy vector database.
 



 To use, you should have the
 `annoy`
 python package installed.
 



 Example
 





```
from langchain import Annoy
db = Annoy(embedding_function, index, docstore, index_to_docstore_id)

```







 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.add_texts)
[#](#langchain.vectorstores.Annoy.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the vectorstore.
* **metadatas** 
 – Optional list of metadatas associated with the texts.
* **kwargs** 
 – vectorstore specific parameters




 Returns
 


 List of ids from adding the texts into the vectorstore.
 








*classmethod*


 from_embeddings
 


 (
 
*text_embeddings
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 float
 


 ]
 



 ]
 



 ]*
 ,
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *metric
 



 :
 





 str
 





 =
 





 'angular'*
 ,
 *trees
 



 :
 





 int
 





 =
 





 100*
 ,
 *n_jobs
 



 :
 





 int
 





 =
 





 -
 

 1*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.annoy.Annoy](#langchain.vectorstores.Annoy "langchain.vectorstores.annoy.Annoy")


[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.from_embeddings)
[#](#langchain.vectorstores.Annoy.from_embeddings "Permalink to this definition") 



 Construct Annoy wrapper from embeddings.
 




 Parameters
 

* **text_embeddings** 
 – List of tuples of (text, embedding)
* **embedding** 
 – Embedding function to use.
* **metadatas** 
 – List of metadata dictionaries to associate with documents.
* **metric** 
 – Metric to use for indexing. Defaults to “angular”.
* **trees** 
 – Number of trees to use for indexing. Defaults to 100.
* **n_jobs** 
 – Number of jobs to use for indexing. Defaults to -1






 This is a user friendly interface that:
 

1. Creates an in memory docstore with provided embeddings
2. Initializes the Annoy database





 This is intended to be a quick way to get started.
 



 Example
 





```
from langchain import Annoy
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
text_embeddings = embeddings.embed_documents(texts)
text_embedding_pairs = list(zip(texts, text_embeddings))
db = Annoy.from_embeddings(text_embedding_pairs, embeddings)

```







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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *metric
 



 :
 





 str
 





 =
 





 'angular'*
 ,
 *trees
 



 :
 





 int
 





 =
 





 100*
 ,
 *n_jobs
 



 :
 





 int
 





 =
 





 -
 

 1*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.annoy.Annoy](#langchain.vectorstores.Annoy "langchain.vectorstores.annoy.Annoy")


[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.from_texts)
[#](#langchain.vectorstores.Annoy.from_texts "Permalink to this definition") 



 Construct Annoy wrapper from raw documents.
 




 Parameters
 

* **texts** 
 – List of documents to index.
* **embedding** 
 – Embedding function to use.
* **metadatas** 
 – List of metadata dictionaries to associate with documents.
* **metric** 
 – Metric to use for indexing. Defaults to “angular”.
* **trees** 
 – Number of trees to use for indexing. Defaults to 100.
* **n_jobs** 
 – Number of jobs to use for indexing. Defaults to -1.






 This is a user friendly interface that:
 

1. Embeds documents.
2. Creates an in memory docstore
3. Initializes the Annoy database





 This is intended to be a quick way to get started.
 



 Example
 





```
from langchain import Annoy
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
index = Annoy.from_texts(texts, embeddings)

```







*classmethod*


 load_local
 


 (
 
*folder_path
 



 :
 





 str*
 ,
 *embeddings
 



 :
 





 langchain.embeddings.base.Embeddings*

 )
 


 →
 

[langchain.vectorstores.annoy.Annoy](#langchain.vectorstores.Annoy "langchain.vectorstores.annoy.Annoy")


[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.load_local)
[#](#langchain.vectorstores.Annoy.load_local "Permalink to this definition") 



 Load Annoy index, docstore, and index_to_docstore_id to disk.
 




 Parameters
 

* **folder_path** 
 – folder path to load index, docstore,
and index_to_docstore_id from.
* **embeddings** 
 – Embeddings to use when generating queries.










 max_marginal_relevance_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.max_marginal_relevance_search)
[#](#langchain.vectorstores.Annoy.max_marginal_relevance_search "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 



 Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5.




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 max_marginal_relevance_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.max_marginal_relevance_search_by_vector)
[#](#langchain.vectorstores.Annoy.max_marginal_relevance_search_by_vector "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 



 Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
 




 Parameters
 

* **embedding** 
 – Embedding to look up documents similar to.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5.




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 process_index_results
 


 (
 
*idxs
 



 :
 





 List
 


 [
 


 int
 


 ]*
 ,
 *dists
 



 :
 





 List
 


 [
 


 float
 


 ]*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.process_index_results)
[#](#langchain.vectorstores.Annoy.process_index_results "Permalink to this definition") 



 Turns annoy results into a list of documents and scores.
 




 Parameters
 

* **idxs** 
 – List of indices of the documents in the index.
* **dists** 
 – List of distances of the documents in the index.




 Returns
 


 List of Documents and scores.
 










 save_local
 


 (
 
*folder_path
 



 :
 





 str*
 ,
 *prefault
 



 :
 





 bool
 





 =
 





 False*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.save_local)
[#](#langchain.vectorstores.Annoy.save_local "Permalink to this definition") 



 Save Annoy index, docstore, and index_to_docstore_id to disk.
 




 Parameters
 

* **folder_path** 
 – folder path to save index, docstore,
and index_to_docstore_id to.
* **prefault** 
 – Whether to pre-load the index into memory.










 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *search_k
 



 :
 





 int
 





 =
 





 -
 

 1*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.similarity_search)
[#](#langchain.vectorstores.Annoy.similarity_search "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **search_k** 
 – inspect up to search_k nodes which defaults
to n_trees \* n if not provided




 Returns
 


 List of Documents most similar to the query.
 










 similarity_search_by_index
 


 (
 
*docstore_index
 



 :
 





 int*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *search_k
 



 :
 





 int
 





 =
 





 -
 

 1*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.similarity_search_by_index)
[#](#langchain.vectorstores.Annoy.similarity_search_by_index "Permalink to this definition") 



 Return docs most similar to docstore_index.
 




 Parameters
 

* **docstore_index** 
 – Index of document in docstore
* **k** 
 – Number of Documents to return. Defaults to 4.
* **search_k** 
 – inspect up to search_k nodes which defaults
to n_trees \* n if not provided




 Returns
 


 List of Documents most similar to the embedding.
 










 similarity_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *search_k
 



 :
 





 int
 





 =
 





 -
 

 1*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.similarity_search_by_vector)
[#](#langchain.vectorstores.Annoy.similarity_search_by_vector "Permalink to this definition") 



 Return docs most similar to embedding vector.
 




 Parameters
 

* **embedding** 
 – Embedding to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **search_k** 
 – inspect up to search_k nodes which defaults
to n_trees \* n if not provided




 Returns
 


 List of Documents most similar to the embedding.
 










 similarity_search_with_score
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *search_k
 



 :
 





 int
 





 =
 





 -
 

 1*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.similarity_search_with_score)
[#](#langchain.vectorstores.Annoy.similarity_search_with_score "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **search_k** 
 – inspect up to search_k nodes which defaults
to n_trees \* n if not provided




 Returns
 


 List of Documents most similar to the query and score for each
 










 similarity_search_with_score_by_index
 


 (
 
*docstore_index
 



 :
 





 int*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *search_k
 



 :
 





 int
 





 =
 





 -
 

 1*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.similarity_search_with_score_by_index)
[#](#langchain.vectorstores.Annoy.similarity_search_with_score_by_index "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **search_k** 
 – inspect up to search_k nodes which defaults
to n_trees \* n if not provided




 Returns
 


 List of Documents most similar to the query and score for each
 










 similarity_search_with_score_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *search_k
 



 :
 





 int
 





 =
 





 -
 

 1*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/annoy#Annoy.similarity_search_with_score_by_vector)
[#](#langchain.vectorstores.Annoy.similarity_search_with_score_by_vector "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **search_k** 
 – inspect up to search_k nodes which defaults
to n_trees \* n if not provided




 Returns
 


 List of Documents most similar to the query and score for each
 










*class*


 langchain.vectorstores.
 



 AtlasDB
 


 (
 
*name
 



 :
 





 str*
 ,
 *embedding_function
 



 :
 





 Optional
 


 [
 


 langchain.embeddings.base.Embeddings
 


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
 *description
 



 :
 





 str
 





 =
 





 'A
 

 description
 

 for
 

 your
 

 project'*
 ,
 *is_public
 



 :
 





 bool
 





 =
 





 True*
 ,
 *reset_project_if_exists
 



 :
 





 bool
 





 =
 





 False*

 )
 
[[source]](../../_modules/langchain/vectorstores/atlas#AtlasDB)
[#](#langchain.vectorstores.AtlasDB "Permalink to this definition") 



 Wrapper around Atlas: Nomic’s neural database and rhizomatic instrument.
 



 To use, you should have the
 `nomic`
 python package installed.
 



 Example
 





```
from langchain.vectorstores import AtlasDB
from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = AtlasDB("my_project", embeddings.embed_query)

```







 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
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
 ,
 *refresh
 



 :
 





 bool
 





 =
 





 True*
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
 



[[source]](../../_modules/langchain/vectorstores/atlas#AtlasDB.add_texts)
[#](#langchain.vectorstores.AtlasDB.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 (
 *Iterable* 
*[* 
*str* 
*]* 
 ) – Texts to add to the vectorstore.
* **metadatas** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*dict* 
*]* 
*]* 
*,* 
*optional* 
 ) – Optional list of metadatas.
* **ids** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*str* 
*]* 
*]* 
 ) – An optional list of ids.
* **refresh** 
 (
 *bool* 
 ) – Whether or not to refresh indices with the updated data.
Default True.




 Returns
 


 List of IDs of the added texts.
 




 Return type
 


 List[str]
 










 create_index
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Any
 


[[source]](../../_modules/langchain/vectorstores/atlas#AtlasDB.create_index)
[#](#langchain.vectorstores.AtlasDB.create_index "Permalink to this definition") 



 Creates an index in your project.
 



 See
 <https://docs.nomic.ai/atlas_api#nomic.project.AtlasProject.create_index>
 for full detail.
 






*classmethod*


 from_documents
 


 (
 
*documents
 



 :
 





 List
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *embedding
 



 :
 





 Optional
 


 [
 


 langchain.embeddings.base.Embeddings
 


 ]
 






 =
 





 None*
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
 *api_key
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *persist_directory
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *description
 



 :
 





 str
 





 =
 





 'A
 

 description
 

 for
 

 your
 

 project'*
 ,
 *is_public
 



 :
 





 bool
 





 =
 





 True*
 ,
 *reset_project_if_exists
 



 :
 





 bool
 





 =
 





 False*
 ,
 *index_kwargs
 



 :
 





 Optional
 


 [
 


 dict
 


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
 

[langchain.vectorstores.atlas.AtlasDB](#langchain.vectorstores.AtlasDB "langchain.vectorstores.atlas.AtlasDB")


[[source]](../../_modules/langchain/vectorstores/atlas#AtlasDB.from_documents)
[#](#langchain.vectorstores.AtlasDB.from_documents "Permalink to this definition") 



 Create an AtlasDB vectorstore from a list of documents.
 




 Parameters
 

* **name** 
 (
 *str* 
 ) – Name of the collection to create.
* **api_key** 
 (
 *str* 
 ) – Your nomic API key,
* **documents** 
 (
 *List* 
*[* 
*Document* 
*]* 
 ) – List of documents to add to the vectorstore.
* **embedding** 
 (
 *Optional* 
*[* 
*Embeddings* 
*]* 
 ) – Embedding function. Defaults to None.
* **ids** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*str* 
*]* 
*]* 
 ) – Optional list of document IDs. If None,
ids will be auto created
* **description** 
 (
 *str* 
 ) – A description for your project.
* **is_public** 
 (
 *bool* 
 ) – Whether your project is publicly accessible.
True by default.
* **reset_project_if_exists** 
 (
 *bool* 
 ) – Whether to reset this project if
it already exists. Default False.
Generally userful during development and testing.
* **index_kwargs** 
 (
 *Optional* 
*[* 
*dict* 
*]* 
 ) – Dict of kwargs for index creation.
See
 <https://docs.nomic.ai/atlas_api>




 Returns
 


 Nomic’s neural database and finest rhizomatic instrument
 




 Return type
 


[AtlasDB](#langchain.vectorstores.AtlasDB "langchain.vectorstores.AtlasDB") 









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
 *embedding
 



 :
 





 Optional
 


 [
 


 langchain.embeddings.base.Embeddings
 


 ]
 






 =
 





 None*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
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
 *api_key
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *description
 



 :
 





 str
 





 =
 





 'A
 

 description
 

 for
 

 your
 

 project'*
 ,
 *is_public
 



 :
 





 bool
 





 =
 





 True*
 ,
 *reset_project_if_exists
 



 :
 





 bool
 





 =
 





 False*
 ,
 *index_kwargs
 



 :
 





 Optional
 


 [
 


 dict
 


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
 

[langchain.vectorstores.atlas.AtlasDB](#langchain.vectorstores.AtlasDB "langchain.vectorstores.atlas.AtlasDB")


[[source]](../../_modules/langchain/vectorstores/atlas#AtlasDB.from_texts)
[#](#langchain.vectorstores.AtlasDB.from_texts "Permalink to this definition") 



 Create an AtlasDB vectorstore from a raw documents.
 




 Parameters
 

* **texts** 
 (
 *List* 
*[* 
*str* 
*]* 
 ) – The list of texts to ingest.
* **name** 
 (
 *str* 
 ) – Name of the project to create.
* **api_key** 
 (
 *str* 
 ) – Your nomic API key,
* **embedding** 
 (
 *Optional* 
*[* 
*Embeddings* 
*]* 
 ) – Embedding function. Defaults to None.
* **metadatas** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*dict* 
*]* 
*]* 
 ) – List of metadatas. Defaults to None.
* **ids** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*str* 
*]* 
*]* 
 ) – Optional list of document IDs. If None,
ids will be auto created
* **description** 
 (
 *str* 
 ) – A description for your project.
* **is_public** 
 (
 *bool* 
 ) – Whether your project is publicly accessible.
True by default.
* **reset_project_if_exists** 
 (
 *bool* 
 ) – Whether to reset this project if it
already exists. Default False.
Generally userful during development and testing.
* **index_kwargs** 
 (
 *Optional* 
*[* 
*dict* 
*]* 
 ) – Dict of kwargs for index creation.
See
 <https://docs.nomic.ai/atlas_api>




 Returns
 


 Nomic’s neural database and finest rhizomatic instrument
 




 Return type
 


[AtlasDB](#langchain.vectorstores.AtlasDB "langchain.vectorstores.AtlasDB") 











 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/atlas#AtlasDB.similarity_search)
[#](#langchain.vectorstores.AtlasDB.similarity_search "Permalink to this definition") 



 Run similarity search with AtlasDB
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – Query text to search for.
* **k** 
 (
 *int* 
 ) – Number of results to return. Defaults to 4.




 Returns
 


 List of documents most similar to the query text.
 




 Return type
 


 List[Document]
 










*class*


 langchain.vectorstores.
 



 Chroma
 


 (
 
*collection_name
 



 :
 





 str
 





 =
 





 'langchain'*
 ,
 *embedding_function
 



 :
 





 Optional
 


 [
 


 Embeddings
 


 ]
 






 =
 





 None*
 ,
 *persist_directory
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *client_settings
 



 :
 





 Optional
 


 [
 


 chromadb.config.Settings
 


 ]
 






 =
 





 None*
 ,
 *collection_metadata
 



 :
 





 Optional
 


 [
 


 Dict
 


 ]
 






 =
 





 None*
 ,
 *client
 



 :
 





 Optional
 


 [
 


 chromadb.Client
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/vectorstores/chroma#Chroma)
[#](#langchain.vectorstores.Chroma "Permalink to this definition") 



 Wrapper around ChromaDB embeddings platform.
 



 To use, you should have the
 `chromadb`
 python package installed.
 



 Example
 





```
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = Chroma("langchain_store", embeddings.embed_query)

```







 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
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
 



[[source]](../../_modules/langchain/vectorstores/chroma#Chroma.add_texts)
[#](#langchain.vectorstores.Chroma.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 (
 *Iterable* 
*[* 
*str* 
*]* 
 ) – Texts to add to the vectorstore.
* **metadatas** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*dict* 
*]* 
*]* 
*,* 
*optional* 
 ) – Optional list of metadatas.
* **ids** 
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
 ) – Optional list of IDs.




 Returns
 


 List of IDs of the added texts.
 




 Return type
 


 List[str]
 










 delete_collection
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/chroma#Chroma.delete_collection)
[#](#langchain.vectorstores.Chroma.delete_collection "Permalink to this definition") 



 Delete the collection.
 






*classmethod*


 from_documents
 


 (
 
*documents
 



 :
 





 List
 


 [
 


 Document
 


 ]*
 ,
 *embedding
 



 :
 





 Optional
 


 [
 


 Embeddings
 


 ]
 






 =
 





 None*
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
 ,
 *collection_name
 



 :
 





 str
 





 =
 





 'langchain'*
 ,
 *persist_directory
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *client_settings
 



 :
 





 Optional
 


 [
 


 chromadb.config.Settings
 


 ]
 






 =
 





 None*
 ,
 *client
 



 :
 





 Optional
 


 [
 


 chromadb.Client
 


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
 

[Chroma](#langchain.vectorstores.Chroma "langchain.vectorstores.Chroma")


[[source]](../../_modules/langchain/vectorstores/chroma#Chroma.from_documents)
[#](#langchain.vectorstores.Chroma.from_documents "Permalink to this definition") 



 Create a Chroma vectorstore from a list of documents.
 



 If a persist_directory is specified, the collection will be persisted there.
Otherwise, the data will be ephemeral in-memory.
 




 Parameters
 

* **collection_name** 
 (
 *str* 
 ) – Name of the collection to create.
* **persist_directory** 
 (
 *Optional* 
*[* 
*str* 
*]* 
 ) – Directory to persist the collection.
* **ids** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*str* 
*]* 
*]* 
 ) – List of document IDs. Defaults to None.
* **documents** 
 (
 *List* 
*[* 
*Document* 
*]* 
 ) – List of documents to add to the vectorstore.
* **embedding** 
 (
 *Optional* 
*[* 
*Embeddings* 
*]* 
 ) – Embedding function. Defaults to None.
* **client_settings** 
 (
 *Optional* 
*[* 
*chromadb.config.Settings* 
*]* 
 ) – Chroma client settings




 Returns
 


 Chroma vectorstore.
 




 Return type
 


[Chroma](#langchain.vectorstores.Chroma "langchain.vectorstores.Chroma") 









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
 *embedding
 



 :
 





 Optional
 


 [
 


 Embeddings
 


 ]
 






 =
 





 None*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
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
 ,
 *collection_name
 



 :
 





 str
 





 =
 





 'langchain'*
 ,
 *persist_directory
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *client_settings
 



 :
 





 Optional
 


 [
 


 chromadb.config.Settings
 


 ]
 






 =
 





 None*
 ,
 *client
 



 :
 





 Optional
 


 [
 


 chromadb.Client
 


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
 

[Chroma](#langchain.vectorstores.Chroma "langchain.vectorstores.Chroma")


[[source]](../../_modules/langchain/vectorstores/chroma#Chroma.from_texts)
[#](#langchain.vectorstores.Chroma.from_texts "Permalink to this definition") 



 Create a Chroma vectorstore from a raw documents.
 



 If a persist_directory is specified, the collection will be persisted there.
Otherwise, the data will be ephemeral in-memory.
 




 Parameters
 

* **texts** 
 (
 *List* 
*[* 
*str* 
*]* 
 ) – List of texts to add to the collection.
* **collection_name** 
 (
 *str* 
 ) – Name of the collection to create.
* **persist_directory** 
 (
 *Optional* 
*[* 
*str* 
*]* 
 ) – Directory to persist the collection.
* **embedding** 
 (
 *Optional* 
*[* 
*Embeddings* 
*]* 
 ) – Embedding function. Defaults to None.
* **metadatas** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*dict* 
*]* 
*]* 
 ) – List of metadatas. Defaults to None.
* **ids** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*str* 
*]* 
*]* 
 ) – List of document IDs. Defaults to None.
* **client_settings** 
 (
 *Optional* 
*[* 
*chromadb.config.Settings* 
*]* 
 ) – Chroma client settings




 Returns
 


 Chroma vectorstore.
 




 Return type
 


[Chroma](#langchain.vectorstores.Chroma "langchain.vectorstores.Chroma") 











 max_marginal_relevance_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *filter
 



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
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/chroma#Chroma.max_marginal_relevance_search)
[#](#langchain.vectorstores.Chroma.max_marginal_relevance_search "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
:param query: Text to look up documents similar to.
:param k: Number of Documents to return. Defaults to 4.
:param fetch_k: Number of Documents to fetch to pass to MMR algorithm.
:param lambda_mult: Number between 0 and 1 that determines the degree
 



> 
> 
> 
>  of diversity among the results with 0 corresponding
> to maximum diversity and 1 to minimum diversity.
> Defaults to 0.5.
>  
> 
> 
> 
> 




 Parameters
 


**filter** 
 (
 *Optional* 
*[* 
*Dict* 
*[* 
*str* 
*,* 
*str* 
*]* 
*]* 
 ) – Filter by metadata. Defaults to None.
 




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 max_marginal_relevance_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *filter
 



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
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/chroma#Chroma.max_marginal_relevance_search_by_vector)
[#](#langchain.vectorstores.Chroma.max_marginal_relevance_search_by_vector "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
:param embedding: Embedding to look up documents similar to.
:param k: Number of Documents to return. Defaults to 4.
:param fetch_k: Number of Documents to fetch to pass to MMR algorithm.
:param lambda_mult: Number between 0 and 1 that determines the degree
 



> 
> 
> 
>  of diversity among the results with 0 corresponding
> to maximum diversity and 1 to minimum diversity.
> Defaults to 0.5.
>  
> 
> 
> 
> 




 Parameters
 


**filter** 
 (
 *Optional* 
*[* 
*Dict* 
*[* 
*str* 
*,* 
*str* 
*]* 
*]* 
 ) – Filter by metadata. Defaults to None.
 




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 persist
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/chroma#Chroma.persist)
[#](#langchain.vectorstores.Chroma.persist "Permalink to this definition") 



 Persist the collection.
 



 This can be used to explicitly persist the data to disk.
It will also be called automatically when the object is destroyed.
 








 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



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
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/chroma#Chroma.similarity_search)
[#](#langchain.vectorstores.Chroma.similarity_search "Permalink to this definition") 



 Run similarity search with Chroma.
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – Query text to search for.
* **k** 
 (
 *int* 
 ) – Number of results to return. Defaults to 4.
* **filter** 
 (
 *Optional* 
*[* 
*Dict* 
*[* 
*str* 
*,* 
*str* 
*]* 
*]* 
 ) – Filter by metadata. Defaults to None.




 Returns
 


 List of documents most similar to the query text.
 




 Return type
 


 List[Document]
 










 similarity_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



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
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/chroma#Chroma.similarity_search_by_vector)
[#](#langchain.vectorstores.Chroma.similarity_search_by_vector "Permalink to this definition") 



 Return docs most similar to embedding vector.
:param embedding: Embedding to look up documents similar to.
:param k: Number of Documents to return. Defaults to 4.
 




 Returns
 


 List of Documents most similar to the query vector.
 










 similarity_search_with_score
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



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
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/chroma#Chroma.similarity_search_with_score)
[#](#langchain.vectorstores.Chroma.similarity_search_with_score "Permalink to this definition") 



 Run similarity search with Chroma with distance.
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – Query text to search for.
* **k** 
 (
 *int* 
 ) – Number of results to return. Defaults to 4.
* **filter** 
 (
 *Optional* 
*[* 
*Dict* 
*[* 
*str* 
*,* 
*str* 
*]* 
*]* 
 ) – Filter by metadata. Defaults to None.




 Returns
 




 List of documents most similar to the query
 


 text with distance in float.
 









 Return type
 


 List[Tuple[Document, float]]
 










 update_document
 


 (
 
*document_id
 



 :
 





 str*
 ,
 *document
 



 :
 





 langchain.schema.Document*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/chroma#Chroma.update_document)
[#](#langchain.vectorstores.Chroma.update_document "Permalink to this definition") 



 Update a document in the collection.
 




 Parameters
 

* **document_id** 
 (
 *str* 
 ) – ID of the document to update.
* **document** 
 (
 *Document* 
 ) – Document to update.










*class*


 langchain.vectorstores.
 



 DeepLake
 


 (
 
*dataset_path
 



 :
 





 str
 





 =
 





 './deeplake/'*
 ,
 *token
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *embedding_function
 



 :
 





 Optional
 


 [
 


 langchain.embeddings.base.Embeddings
 


 ]
 






 =
 





 None*
 ,
 *read_only
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 False*
 ,
 *ingestion_batch_size
 



 :
 





 int
 





 =
 





 1024*
 ,
 *num_workers
 



 :
 





 int
 





 =
 





 0*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake)
[#](#langchain.vectorstores.DeepLake "Permalink to this definition") 



 Wrapper around Deep Lake, a data lake for deep learning applications.
 



 We implement naive similarity search and filtering for fast prototyping,
but it can be extended with Tensor Query Language (TQL) for production use cases
over billion rows.
 



 Why Deep Lake?
 


* Not only stores embeddings, but also the original data with version control.
* Serverless, doesn’t require another service and can be used with major
 


 cloud providers (S3, GCS, etc.)
* More than just a multi-modal vector store. You can use the dataset
 


 to fine-tune your own LLM models.



 To use, you should have the
 `deeplake`
 python package installed.
 



 Example
 





```
from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = DeepLake("langchain_store", embeddings.embed_query)

```







 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
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
 



[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake.add_texts)
[#](#langchain.vectorstores.DeepLake.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 (
 *Iterable* 
*[* 
*str* 
*]* 
 ) – Texts to add to the vectorstore.
* **metadatas** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*dict* 
*]* 
*]* 
*,* 
*optional* 
 ) – Optional list of metadatas.
* **ids** 
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
 ) – Optional list of IDs.




 Returns
 


 List of IDs of the added texts.
 




 Return type
 


 List[str]
 










 delete
 


 (
 
*ids
 



 :
 





 Any
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ,
 




 None
 


 ]
 






 =
 





 None*
 ,
 *filter
 



 :
 





 Any
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ,
 




 None
 


 ]
 






 =
 





 None*
 ,
 *delete_all
 



 :
 





 Any
 


 [
 


 bool
 


 ,
 




 None
 


 ]
 






 =
 





 None*

 )
 


 →
 


 bool
 


[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake.delete)
[#](#langchain.vectorstores.DeepLake.delete "Permalink to this definition") 



 Delete the entities in the dataset
 




 Parameters
 

* **ids** 
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
 ) – The document_ids to delete.
Defaults to None.
* **filter** 
 (
 *Optional* 
*[* 
*Dict* 
*[* 
*str* 
*,* 
*str* 
*]* 
*]* 
*,* 
*optional* 
 ) – The filter to delete by.
Defaults to None.
* **delete_all** 
 (
 *Optional* 
*[* 
*bool* 
*]* 
*,* 
*optional* 
 ) – Whether to drop the dataset.
Defaults to None.










 delete_dataset
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake.delete_dataset)
[#](#langchain.vectorstores.DeepLake.delete_dataset "Permalink to this definition") 



 Delete the collection.
 






*classmethod*


 force_delete_by_path
 


 (
 
*path
 



 :
 





 str*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake.force_delete_by_path)
[#](#langchain.vectorstores.DeepLake.force_delete_by_path "Permalink to this definition") 



 Force delete dataset by path
 






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
 *embedding
 



 :
 





 Optional
 


 [
 


 langchain.embeddings.base.Embeddings
 


 ]
 






 =
 





 None*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
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
 ,
 *dataset_path
 



 :
 





 str
 





 =
 





 './deeplake/'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.deeplake.DeepLake](#langchain.vectorstores.DeepLake "langchain.vectorstores.deeplake.DeepLake")


[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake.from_texts)
[#](#langchain.vectorstores.DeepLake.from_texts "Permalink to this definition") 



 Create a Deep Lake dataset from a raw documents.
 



 If a dataset_path is specified, the dataset will be persisted in that location,
otherwise by default at
 
 ./deeplake
 





 Parameters
 

* **path** 
 (
 *str* 
*,* 
*pathlib.Path* 
 ) –
 
	+ The full path to the dataset. Can be:
	+ Deep Lake cloud path of the form
	 `hub://username/dataset_name`
	 .
	 
	
	
	 To write to Deep Lake cloud datasets,
	ensure that you are logged in to Deep Lake
	(use ‘activeloop login’ from command line)
	+ AWS S3 path of the form
	 `s3://bucketname/path/to/dataset`
	 .
	 
	
	
	 Credentials are required in either the environment
	+ Google Cloud Storage path of the form
	 
	
	
	[``](#id1)
	 gcs://bucketname/path/to/dataset``Credentials are required
	in either the environment
	+ Local file system path of the form
	 `./path/to/dataset`
	 or
	 
	
	
	`~/path/to/dataset`
	 or
	 `path/to/dataset`
	 .
	+ In-memory path of the form
	 `mem://path/to/dataset`
	 which doesn’t
	 
	
	
	 save the dataset, but keeps it in memory instead.
	Should be used only for testing as it does not persist.
* **documents** 
 (
 *List* 
*[* 
*Document* 
*]* 
 ) – List of documents to add.
* **embedding** 
 (
 *Optional* 
*[* 
*Embeddings* 
*]* 
 ) – Embedding function. Defaults to None.
* **metadatas** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*dict* 
*]* 
*]* 
 ) – List of metadatas. Defaults to None.
* **ids** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*str* 
*]* 
*]* 
 ) – List of document IDs. Defaults to None.




 Returns
 


 Deep Lake dataset.
 




 Return type
 


[DeepLake](#langchain.vectorstores.DeepLake "langchain.vectorstores.DeepLake") 











 max_marginal_relevance_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake.max_marginal_relevance_search)
[#](#langchain.vectorstores.DeepLake.max_marginal_relevance_search "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
:param query: Text to look up documents similar to.
:param k: Number of Documents to return. Defaults to 4.
:param fetch_k: Number of Documents to fetch to pass to MMR algorithm.
:param lambda_mult: Number between 0 and 1 that determines the degree
 



> 
> 
> 
>  of diversity among the results with 0 corresponding
> to maximum diversity and 1 to minimum diversity.
> Defaults to 0.5.
>  
> 
> 
> 
> 




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 max_marginal_relevance_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake.max_marginal_relevance_search_by_vector)
[#](#langchain.vectorstores.DeepLake.max_marginal_relevance_search_by_vector "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
:param embedding: Embedding to look up documents similar to.
:param k: Number of Documents to return. Defaults to 4.
:param fetch_k: Number of Documents to fetch to pass to MMR algorithm.
:param lambda_mult: Number between 0 and 1 that determines the degree
 



> 
> 
> 
>  of diversity among the results with 0 corresponding
> to maximum diversity and 1 to minimum diversity.
> Defaults to 0.5.
>  
> 
> 
> 
> 




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 persist
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake.persist)
[#](#langchain.vectorstores.DeepLake.persist "Permalink to this definition") 



 Persist the collection.
 








 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake.similarity_search)
[#](#langchain.vectorstores.DeepLake.similarity_search "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – text to embed and run the query on.
* **k** 
 – Number of Documents to return.
Defaults to 4.
* **query** 
 – Text to look up documents similar to.
* **embedding** 
 – Embedding function to use.
Defaults to None.
* **k** 
 – Number of Documents to return.
Defaults to 4.
* **distance_metric** 
 –
 
 L2
 
 for Euclidean,
 
 L1
 
 for Nuclear,
 
 max
 
 L-infinity distance,
 
 cos
 
 for cosine similarity, ‘dot’ for dot product
Defaults to
 
 L2
 
 .
* **filter** 
 – Attribute filter by metadata example {‘key’: ‘value’}.
Defaults to None.
* **maximal_marginal_relevance** 
 – Whether to use maximal marginal relevance.
Defaults to False.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
Defaults to 20.
* **return_score** 
 – Whether to return the score. Defaults to False.




 Returns
 


 List of Documents most similar to the query vector.
 










 similarity_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake.similarity_search_by_vector)
[#](#langchain.vectorstores.DeepLake.similarity_search_by_vector "Permalink to this definition") 



 Return docs most similar to embedding vector.
 




 Parameters
 

* **embedding** 
 – Embedding to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.




 Returns
 


 List of Documents most similar to the query vector.
 










 similarity_search_with_score
 


 (
 
*query
 



 :
 





 str*
 ,
 *distance_metric
 



 :
 





 str
 





 =
 





 'L2'*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



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

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/deeplake#DeepLake.similarity_search_with_score)
[#](#langchain.vectorstores.DeepLake.similarity_search_with_score "Permalink to this definition") 



 Run similarity search with Deep Lake with distance returned.
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – Query text to search for.
* **distance_metric** 
 –
 
 L2
 
 for Euclidean,
 
 L1
 
 for Nuclear,
 
 max
 
 L-infinity
distance,
 
 cos
 
 for cosine similarity, ‘dot’ for dot product.
Defaults to
 
 L2
 
 .
* **k** 
 (
 *int* 
 ) – Number of results to return. Defaults to 4.
* **filter** 
 (
 *Optional* 
*[* 
*Dict* 
*[* 
*str* 
*,* 
*str* 
*]* 
*]* 
 ) – Filter by metadata. Defaults to None.




 Returns
 




 List of documents most similar to the query
 


 text with distance in float.
 









 Return type
 


 List[Tuple[Document, float]]
 










*class*


 langchain.vectorstores.
 



 ElasticVectorSearch
 


 (
 
*elasticsearch_url
 



 :
 





 str*
 ,
 *index_name
 



 :
 





 str*
 ,
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*

 )
 
[[source]](../../_modules/langchain/vectorstores/elastic_vector_search#ElasticVectorSearch)
[#](#langchain.vectorstores.ElasticVectorSearch "Permalink to this definition") 



 Wrapper around Elasticsearch as a vector database.
 



 To connect to an Elasticsearch instance that does not require
login credentials, pass the Elasticsearch URL and index name along with the
embedding object to the constructor.
 



 Example
 





```
from langchain import ElasticVectorSearch
from langchain.embeddings import OpenAIEmbeddings

embedding = OpenAIEmbeddings()
elastic_vector_search = ElasticVectorSearch(
    elasticsearch_url="http://localhost:9200",
    index_name="test_index",
    embedding=embedding
)

```




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
 



 Example
 





```
from langchain import ElasticVectorSearch
from langchain.embeddings import OpenAIEmbeddings

embedding = OpenAIEmbeddings()

elastic_host = "cluster_id.region_id.gcp.cloud.es.io"
elasticsearch_url = f"https://username:password@{elastic_host}:9243"
elastic_vector_search = ElasticVectorSearch(
    elasticsearch_url=elasticsearch_url,
    index_name="test_index",
    embedding=embedding
)

```





 Parameters
 

* **elasticsearch_url** 
 (
 *str* 
 ) – The URL for the Elasticsearch instance.
* **index_name** 
 (
 *str* 
 ) – The name of the Elasticsearch index for the embeddings.
* **embedding** 
 (
 *Embeddings* 
 ) – An object that provides the ability to embed text.
It should be an instance of a class that subclasses the Embeddings
abstract base class, such as OpenAIEmbeddings()




 Raises
 


**ValueError** 
 – If the elasticsearch python package is not installed.
 








 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *refresh_indices
 



 :
 





 bool
 





 =
 





 True*
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
 



[[source]](../../_modules/langchain/vectorstores/elastic_vector_search#ElasticVectorSearch.add_texts)
[#](#langchain.vectorstores.ElasticVectorSearch.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the vectorstore.
* **metadatas** 
 – Optional list of metadatas associated with the texts.
* **refresh_indices** 
 – bool to refresh ElasticSearch indices




 Returns
 


 List of ids from adding the texts into the vectorstore.
 








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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 

[langchain.vectorstores.elastic_vector_search.ElasticVectorSearch](#langchain.vectorstores.ElasticVectorSearch "langchain.vectorstores.elastic_vector_search.ElasticVectorSearch")


[[source]](../../_modules/langchain/vectorstores/elastic_vector_search#ElasticVectorSearch.from_texts)
[#](#langchain.vectorstores.ElasticVectorSearch.from_texts "Permalink to this definition") 



 Construct ElasticVectorSearch wrapper from raw documents.
 




 This is a user-friendly interface that:
 

1. Embeds documents.
2. Creates a new index for the embeddings in the Elasticsearch instance.
3. Adds the documents to the newly created Elasticsearch index.





 This is intended to be a quick way to get started.
 



 Example
 





```
from langchain import ElasticVectorSearch
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
elastic_vector_search = ElasticVectorSearch.from_texts(
    texts,
    embeddings,
    elasticsearch_url="http://localhost:9200"
)

```









 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



 :
 





 Optional
 


 [
 


 dict
 


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
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/elastic_vector_search#ElasticVectorSearch.similarity_search)
[#](#langchain.vectorstores.ElasticVectorSearch.similarity_search "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.




 Returns
 


 List of Documents most similar to the query.
 










 similarity_search_with_score
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



 :
 





 Optional
 


 [
 


 dict
 


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
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/elastic_vector_search#ElasticVectorSearch.similarity_search_with_score)
[#](#langchain.vectorstores.ElasticVectorSearch.similarity_search_with_score "Permalink to this definition") 



 Return docs most similar to query.
:param query: Text to look up documents similar to.
:param k: Number of Documents to return. Defaults to 4.
 




 Returns
 


 List of Documents most similar to the query.
 










*class*


 langchain.vectorstores.
 



 FAISS
 


 (
 
*embedding_function:
 

 typing.Callable,
 

 index:
 

 typing.Any,
 

 docstore:
 

 langchain.docstore.base.Docstore,
 

 index_to_docstore_id:
 

 typing.Dict[int,
 

 str],
 

 relevance_score_fn:
 

 typing.Optional[typing.Callable[[float],
 

 float]]
 

 =
 

 <function
 

 _default_relevance_score_fn>*

 )
 
[[source]](../../_modules/langchain/vectorstores/faiss#FAISS)
[#](#langchain.vectorstores.FAISS "Permalink to this definition") 



 Wrapper around FAISS vector database.
 



 To use, you should have the
 `faiss`
 python package installed.
 



 Example
 





```
from langchain import FAISS
faiss = FAISS(embedding_function, index, docstore, index_to_docstore_id)

```







 add_embeddings
 


 (
 
*text_embeddings
 



 :
 





 Iterable
 


 [
 


 Tuple
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 float
 


 ]
 



 ]
 



 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.add_embeddings)
[#](#langchain.vectorstores.FAISS.add_embeddings "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **text_embeddings** 
 – Iterable pairs of string and embedding to
add to the vectorstore.
* **metadatas** 
 – Optional list of metadatas associated with the texts.




 Returns
 


 List of ids from adding the texts into the vectorstore.
 










 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.add_texts)
[#](#langchain.vectorstores.FAISS.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the vectorstore.
* **metadatas** 
 – Optional list of metadatas associated with the texts.




 Returns
 


 List of ids from adding the texts into the vectorstore.
 








*classmethod*


 from_embeddings
 


 (
 
*text_embeddings
 



 :
 





 List
 


 [
 


 Tuple
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 float
 


 ]
 



 ]
 



 ]*
 ,
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 

[langchain.vectorstores.faiss.FAISS](#langchain.vectorstores.FAISS "langchain.vectorstores.faiss.FAISS")


[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.from_embeddings)
[#](#langchain.vectorstores.FAISS.from_embeddings "Permalink to this definition") 



 Construct FAISS wrapper from raw documents.
 




 This is a user friendly interface that:
 

1. Embeds documents.
2. Creates an in memory docstore
3. Initializes the FAISS database





 This is intended to be a quick way to get started.
 



 Example
 





```
from langchain import FAISS
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
text_embeddings = embeddings.embed_documents(texts)
text_embedding_pairs = list(zip(texts, text_embeddings))
faiss = FAISS.from_embeddings(text_embedding_pairs, embeddings)

```







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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 

[langchain.vectorstores.faiss.FAISS](#langchain.vectorstores.FAISS "langchain.vectorstores.faiss.FAISS")


[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.from_texts)
[#](#langchain.vectorstores.FAISS.from_texts "Permalink to this definition") 



 Construct FAISS wrapper from raw documents.
 




 This is a user friendly interface that:
 

1. Embeds documents.
2. Creates an in memory docstore
3. Initializes the FAISS database





 This is intended to be a quick way to get started.
 



 Example
 





```
from langchain import FAISS
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
faiss = FAISS.from_texts(texts, embeddings)

```







*classmethod*


 load_local
 


 (
 
*folder_path
 



 :
 





 str*
 ,
 *embeddings
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *index_name
 



 :
 





 str
 





 =
 





 'index'*

 )
 


 →
 

[langchain.vectorstores.faiss.FAISS](#langchain.vectorstores.FAISS "langchain.vectorstores.faiss.FAISS")


[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.load_local)
[#](#langchain.vectorstores.FAISS.load_local "Permalink to this definition") 



 Load FAISS index, docstore, and index_to_docstore_id to disk.
 




 Parameters
 

* **folder_path** 
 – folder path to load index, docstore,
and index_to_docstore_id from.
* **embeddings** 
 – Embeddings to use when generating queries
* **index_name** 
 – for saving with a specific index file name










 max_marginal_relevance_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.max_marginal_relevance_search)
[#](#langchain.vectorstores.FAISS.max_marginal_relevance_search "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 



 Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5.




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 max_marginal_relevance_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.max_marginal_relevance_search_by_vector)
[#](#langchain.vectorstores.FAISS.max_marginal_relevance_search_by_vector "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 



 Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
 




 Parameters
 

* **embedding** 
 – Embedding to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5.




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 merge_from
 


 (
 
*target
 



 :
 




[langchain.vectorstores.faiss.FAISS](#langchain.vectorstores.FAISS "langchain.vectorstores.faiss.FAISS")*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.merge_from)
[#](#langchain.vectorstores.FAISS.merge_from "Permalink to this definition") 



 Merge another FAISS object with the current one.
 



 Add the target FAISS to the current one.
 




 Parameters
 


**target** 
 – FAISS object you wish to merge into the current one
 




 Returns
 


 None.
 










 save_local
 


 (
 
*folder_path
 



 :
 





 str*
 ,
 *index_name
 



 :
 





 str
 





 =
 





 'index'*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.save_local)
[#](#langchain.vectorstores.FAISS.save_local "Permalink to this definition") 



 Save FAISS index, docstore, and index_to_docstore_id to disk.
 




 Parameters
 

* **folder_path** 
 – folder path to save index, docstore,
and index_to_docstore_id to.
* **index_name** 
 – for saving with a specific index file name










 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.similarity_search)
[#](#langchain.vectorstores.FAISS.similarity_search "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.




 Returns
 


 List of Documents most similar to the query.
 










 similarity_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.similarity_search_by_vector)
[#](#langchain.vectorstores.FAISS.similarity_search_by_vector "Permalink to this definition") 



 Return docs most similar to embedding vector.
 




 Parameters
 

* **embedding** 
 – Embedding to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.




 Returns
 


 List of Documents most similar to the embedding.
 










 similarity_search_with_score
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.similarity_search_with_score)
[#](#langchain.vectorstores.FAISS.similarity_search_with_score "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.




 Returns
 


 List of Documents most similar to the query and score for each
 










 similarity_search_with_score_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/faiss#FAISS.similarity_search_with_score_by_vector)
[#](#langchain.vectorstores.FAISS.similarity_search_with_score_by_vector "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.




 Returns
 


 List of Documents most similar to the query and score for each
 










*class*


 langchain.vectorstores.
 



 LanceDB
 


 (
 
*connection
 



 :
 





 Any*
 ,
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *vector_key
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'vector'*
 ,
 *id_key
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'id'*
 ,
 *text_key
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'text'*

 )
 
[[source]](../../_modules/langchain/vectorstores/lancedb#LanceDB)
[#](#langchain.vectorstores.LanceDB "Permalink to this definition") 



 Wrapper around LanceDB vector database.
 



 To use, you should have
 `lancedb`
 python package installed.
 



 Example
 





```
db = lancedb.connect('./lancedb')
table = db.open_table('my_table')
vectorstore = LanceDB(table, embedding_function)
vectorstore.add_texts(['text1', 'text2'])
result = vectorstore.similarity_search('text1')

```







 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
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
 



[[source]](../../_modules/langchain/vectorstores/lancedb#LanceDB.add_texts)
[#](#langchain.vectorstores.LanceDB.add_texts "Permalink to this definition") 



 Turn texts into embedding and add it to the database
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the vectorstore.
* **metadatas** 
 – Optional list of metadatas associated with the texts.
* **ids** 
 – Optional list of ids to associate with the texts.




 Returns
 


 List of ids of the added texts.
 








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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *connection
 



 :
 





 Optional
 


 [
 


 Any
 


 ]
 






 =
 





 None*
 ,
 *vector_key
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'vector'*
 ,
 *id_key
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'id'*
 ,
 *text_key
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'text'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.lancedb.LanceDB](#langchain.vectorstores.LanceDB "langchain.vectorstores.lancedb.LanceDB")


[[source]](../../_modules/langchain/vectorstores/lancedb#LanceDB.from_texts)
[#](#langchain.vectorstores.LanceDB.from_texts "Permalink to this definition") 



 Return VectorStore initialized from texts and embeddings.
 








 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/lancedb#LanceDB.similarity_search)
[#](#langchain.vectorstores.LanceDB.similarity_search "Permalink to this definition") 



 Return documents most similar to the query
 




 Parameters
 

* **query** 
 – String to query the vectorstore with.
* **k** 
 – Number of documents to return.




 Returns
 


 List of documents most similar to the query.
 










*class*


 langchain.vectorstores.
 



 Milvus
 


 (
 
*embedding_function
 



 :
 





 Embeddings*
 ,
 *collection_name
 



 :
 





 str
 





 =
 





 'LangChainCollection'*
 ,
 *connection_args
 



 :
 





 Optional
 


 [
 


 dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *consistency_level
 



 :
 





 str
 





 =
 





 'Session'*
 ,
 *index_params
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *search_params
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *drop_old
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 False*

 )
 
[[source]](../../_modules/langchain/vectorstores/milvus#Milvus)
[#](#langchain.vectorstores.Milvus "Permalink to this definition") 



 Wrapper around the Milvus vector database.
 






 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *timeout
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 None*
 ,
 *batch_size
 



 :
 





 int
 





 =
 





 1000*
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
 



[[source]](../../_modules/langchain/vectorstores/milvus#Milvus.add_texts)
[#](#langchain.vectorstores.Milvus.add_texts "Permalink to this definition") 



 Insert text data into Milvus.
 



 Inserting data when the collection has not be made yet will result
in creating a new Collection. The data of the first entity decides
the schema of the new collection, the dim is extracted from the first
embedding and the columns are decided by the first metadata dict.
Metada keys will need to be present for all inserted values. At
the moment there is no None equivalent in Milvus.
 




 Parameters
 

* **texts** 
 (
 *Iterable* 
*[* 
*str* 
*]* 
 ) – The texts to embed, it is assumed
that they all fit in memory.
* **metadatas** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*dict* 
*]* 
*]* 
 ) – Metadata dicts attached to each of
the texts. Defaults to None.
* **timeout** 
 (
 *Optional* 
*[* 
*int* 
*]* 
 ) – Timeout for each batch insert. Defaults
to None.
* **batch_size** 
 (
 *int* 
*,* 
*optional* 
 ) – Batch size to use for insertion.
Defaults to 1000.




 Raises
 


**MilvusException** 
 – Failure to add texts
 




 Returns
 


 The resulting keys for each inserted element.
 




 Return type
 


 List[str]
 








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
 *embedding
 



 :
 





 Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *collection_name
 



 :
 





 str
 





 =
 





 'LangChainCollection'*
 ,
 *connection_args
 



 :
 





 dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 






 =
 





 {'host':
 

 'localhost',
 

 'password':
 

 '',
 

 'port':
 

 '19530',
 

 'secure':
 

 False,
 

 'user':
 

 ''}*
 ,
 *consistency_level
 



 :
 





 str
 





 =
 





 'Session'*
 ,
 *index_params
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *search_params
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *drop_old
 



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
 


 →
 

[Milvus](#langchain.vectorstores.Milvus "langchain.vectorstores.Milvus")


[[source]](../../_modules/langchain/vectorstores/milvus#Milvus.from_texts)
[#](#langchain.vectorstores.Milvus.from_texts "Permalink to this definition") 



 Create a Milvus collection, indexes it with HNSW, and insert data.
 




 Parameters
 

* **texts** 
 (
 *List* 
*[* 
*str* 
*]* 
 ) – Text data.
* **embedding** 
 (
 *Embeddings* 
 ) – Embedding function.
* **metadatas** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*dict* 
*]* 
*]* 
 ) – Metadata for each text if it exists.
Defaults to None.
* **collection_name** 
 (
 *str* 
*,* 
*optional* 
 ) – Collection name to use. Defaults to
“LangChainCollection”.
* **connection_args** 
 (
 *dict* 
*[* 
*str* 
*,* 
*Any* 
*]* 
*,* 
*optional* 
 ) – Connection args to use. Defaults
to DEFAULT_MILVUS_CONNECTION.
* **consistency_level** 
 (
 *str* 
*,* 
*optional* 
 ) – Which consistency level to use. Defaults
to “Session”.
* **index_params** 
 (
 *Optional* 
*[* 
*dict* 
*]* 
*,* 
*optional* 
 ) – Which index_params to use. Defaults
to None.
* **search_params** 
 (
 *Optional* 
*[* 
*dict* 
*]* 
*,* 
*optional* 
 ) – Which search params to use.
Defaults to None.
* **drop_old** 
 (
 *Optional* 
*[* 
*bool* 
*]* 
*,* 
*optional* 
 ) – Whether to drop the collection with
that name if it exists. Defaults to False.




 Returns
 


 Milvus Vector Store
 




 Return type
 


[Milvus](#langchain.vectorstores.Milvus "langchain.vectorstores.Milvus") 











 max_marginal_relevance_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *param
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *expr
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *timeout
 



 :
 





 Optional
 


 [
 


 int
 


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
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/milvus#Milvus.max_marginal_relevance_search)
[#](#langchain.vectorstores.Milvus.max_marginal_relevance_search "Permalink to this definition") 



 Perform a search and return results that are reordered by MMR.
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – The text being searched.
* **k** 
 (
 *int* 
*,* 
*optional* 
 ) – How many results to give. Defaults to 4.
* **fetch_k** 
 (
 *int* 
*,* 
*optional* 
 ) – Total results to select k from.
Defaults to 20.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5
* **param** 
 (
 *dict* 
*,* 
*optional* 
 ) – The search params for the specified index.
Defaults to None.
* **expr** 
 (
 *str* 
*,* 
*optional* 
 ) – Filtering expression. Defaults to None.
* **timeout** 
 (
 *int* 
*,* 
*optional* 
 ) – How long to wait before timeout error.
Defaults to None.
* **kwargs** 
 – Collection.search() keyword arguments.




 Returns
 


 Document results for search.
 




 Return type
 


 List[Document]
 










 max_marginal_relevance_search_by_vector
 


 (
 
*embedding
 



 :
 





 list
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *param
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *expr
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *timeout
 



 :
 





 Optional
 


 [
 


 int
 


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
 


 List
 


 [
 


 Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/milvus#Milvus.max_marginal_relevance_search_by_vector)
[#](#langchain.vectorstores.Milvus.max_marginal_relevance_search_by_vector "Permalink to this definition") 



 Perform a search and return results that are reordered by MMR.
 




 Parameters
 

* **embedding** 
 (
 *str* 
 ) – The embedding vector being searched.
* **k** 
 (
 *int* 
*,* 
*optional* 
 ) – How many results to give. Defaults to 4.
* **fetch_k** 
 (
 *int* 
*,* 
*optional* 
 ) – Total results to select k from.
Defaults to 20.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5
* **param** 
 (
 *dict* 
*,* 
*optional* 
 ) – The search params for the specified index.
Defaults to None.
* **expr** 
 (
 *str* 
*,* 
*optional* 
 ) – Filtering expression. Defaults to None.
* **timeout** 
 (
 *int* 
*,* 
*optional* 
 ) – How long to wait before timeout error.
Defaults to None.
* **kwargs** 
 – Collection.search() keyword arguments.




 Returns
 


 Document results for search.
 




 Return type
 


 List[Document]
 










 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *param
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *expr
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *timeout
 



 :
 





 Optional
 


 [
 


 int
 


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
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/milvus#Milvus.similarity_search)
[#](#langchain.vectorstores.Milvus.similarity_search "Permalink to this definition") 



 Perform a similarity search against the query string.
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – The text to search.
* **k** 
 (
 *int* 
*,* 
*optional* 
 ) – How many results to return. Defaults to 4.
* **param** 
 (
 *dict* 
*,* 
*optional* 
 ) – The search params for the index type.
Defaults to None.
* **expr** 
 (
 *str* 
*,* 
*optional* 
 ) – Filtering expression. Defaults to None.
* **timeout** 
 (
 *int* 
*,* 
*optional* 
 ) – How long to wait before timeout error.
Defaults to None.
* **kwargs** 
 – Collection.search() keyword arguments.




 Returns
 


 Document results for search.
 




 Return type
 


 List[Document]
 










 similarity_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *param
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *expr
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *timeout
 



 :
 





 Optional
 


 [
 


 int
 


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
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/milvus#Milvus.similarity_search_by_vector)
[#](#langchain.vectorstores.Milvus.similarity_search_by_vector "Permalink to this definition") 



 Perform a similarity search against the query string.
 




 Parameters
 

* **embedding** 
 (
 *List* 
*[* 
*float* 
*]* 
 ) – The embedding vector to search.
* **k** 
 (
 *int* 
*,* 
*optional* 
 ) – How many results to return. Defaults to 4.
* **param** 
 (
 *dict* 
*,* 
*optional* 
 ) – The search params for the index type.
Defaults to None.
* **expr** 
 (
 *str* 
*,* 
*optional* 
 ) – Filtering expression. Defaults to None.
* **timeout** 
 (
 *int* 
*,* 
*optional* 
 ) – How long to wait before timeout error.
Defaults to None.
* **kwargs** 
 – Collection.search() keyword arguments.




 Returns
 


 Document results for search.
 




 Return type
 


 List[Document]
 










 similarity_search_with_score
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *param
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *expr
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *timeout
 



 :
 





 Optional
 


 [
 


 int
 


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
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/milvus#Milvus.similarity_search_with_score)
[#](#langchain.vectorstores.Milvus.similarity_search_with_score "Permalink to this definition") 



 Perform a search on a query string and return results with score.
 



 For more information about the search parameters, take a look at the pymilvus
documentation found here:
 <https://milvus.io/api-reference/pymilvus/v2.2.6/Collection/search().md>





 Parameters
 

* **query** 
 (
 *str* 
 ) – The text being searched.
* **k** 
 (
 *int* 
*,* 
*optional* 
 ) – The amount of results ot return. Defaults to 4.
* **param** 
 (
 *dict* 
 ) – The search params for the specified index.
Defaults to None.
* **expr** 
 (
 *str* 
*,* 
*optional* 
 ) – Filtering expression. Defaults to None.
* **timeout** 
 (
 *int* 
*,* 
*optional* 
 ) – How long to wait before timeout error.
Defaults to None.
* **kwargs** 
 – Collection.search() keyword arguments.




 Return type
 


 List[float], List[Tuple[Document, any, any]]
 










 similarity_search_with_score_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *param
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *expr
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *timeout
 



 :
 





 Optional
 


 [
 


 int
 


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
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/milvus#Milvus.similarity_search_with_score_by_vector)
[#](#langchain.vectorstores.Milvus.similarity_search_with_score_by_vector "Permalink to this definition") 



 Perform a search on a query string and return results with score.
 



 For more information about the search parameters, take a look at the pymilvus
documentation found here:
 <https://milvus.io/api-reference/pymilvus/v2.2.6/Collection/search().md>





 Parameters
 

* **embedding** 
 (
 *List* 
*[* 
*float* 
*]* 
 ) – The embedding vector being searched.
* **k** 
 (
 *int* 
*,* 
*optional* 
 ) – The amount of results ot return. Defaults to 4.
* **param** 
 (
 *dict* 
 ) – The search params for the specified index.
Defaults to None.
* **expr** 
 (
 *str* 
*,* 
*optional* 
 ) – Filtering expression. Defaults to None.
* **timeout** 
 (
 *int* 
*,* 
*optional* 
 ) – How long to wait before timeout error.
Defaults to None.
* **kwargs** 
 – Collection.search() keyword arguments.




 Returns
 


 Result doc and score.
 




 Return type
 


 List[Tuple[Document, float]]
 










*class*


 langchain.vectorstores.
 



 MyScale
 


 (
 
*embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *config
 



 :
 





 Optional
 


 [
 

[langchain.vectorstores.myscale.MyScaleSettings](#langchain.vectorstores.MyScaleSettings "langchain.vectorstores.myscale.MyScaleSettings")


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/vectorstores/myscale#MyScale)
[#](#langchain.vectorstores.MyScale "Permalink to this definition") 



 Wrapper around MyScale vector database
 



 You need a
 
 clickhouse-connect
 
 python package, and a valid account
to connect to MyScale.
 



 MyScale can not only search with simple vector indexes,
it also supports complex query with multiple conditions,
constraints and even sub-queries.
 




 For more information, please visit
 


 [myscale official site](
 <https://docs.myscale.com/en/overview/>
 )
 








 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *batch_size
 



 :
 





 int
 





 =
 





 32*
 ,
 *ids
 



 :
 





 Optional
 


 [
 


 Iterable
 


 [
 


 str
 


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
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/myscale#MyScale.add_texts)
[#](#langchain.vectorstores.MyScale.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the vectorstore.
* **ids** 
 – Optional list of ids to associate with the texts.
* **batch_size** 
 – Batch size of insertion
* **metadata** 
 – Optional column data to be inserted




 Returns
 


 List of ids from adding the texts into the vectorstore.
 










 drop
 


 (
 

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/vectorstores/myscale#MyScale.drop)
[#](#langchain.vectorstores.MyScale.drop "Permalink to this definition") 



 Helper function: Drop data
 








 escape_str
 


 (
 
*value
 



 :
 





 str*

 )
 


 →
 


 str
 


[[source]](../../_modules/langchain/vectorstores/myscale#MyScale.escape_str)
[#](#langchain.vectorstores.MyScale.escape_str "Permalink to this definition") 






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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 Dict
 


 [
 


 Any
 


 ,
 




 Any
 


 ]
 



 ]
 



 ]
 






 =
 





 None*
 ,
 *config
 



 :
 





 Optional
 


 [
 

[langchain.vectorstores.myscale.MyScaleSettings](#langchain.vectorstores.MyScaleSettings "langchain.vectorstores.myscale.MyScaleSettings")


 ]
 






 =
 





 None*
 ,
 *text_ids
 



 :
 





 Optional
 


 [
 


 Iterable
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *batch_size
 



 :
 





 int
 





 =
 





 32*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.myscale.MyScale](#langchain.vectorstores.MyScale "langchain.vectorstores.myscale.MyScale")


[[source]](../../_modules/langchain/vectorstores/myscale#MyScale.from_texts)
[#](#langchain.vectorstores.MyScale.from_texts "Permalink to this definition") 



 Create Myscale wrapper with existing texts
 




 Parameters
 

* **embedding_function** 
 (
 *Embeddings* 
 ) – Function to extract text embedding
* **texts** 
 (
 *Iterable* 
*[* 
*str* 
*]* 
 ) – List or tuple of strings to be added
* **config** 
 (
 [*MyScaleSettings*](#langchain.vectorstores.MyScaleSettings "langchain.vectorstores.MyScaleSettings")
*,* 
*Optional* 
 ) – Myscale configuration
* **text_ids** 
 (
 *Optional* 
*[* 
*Iterable* 
*]* 
*,* 
*optional* 
 ) – IDs for the texts.
Defaults to None.
* **batch_size** 
 (
 *int* 
*,* 
*optional* 
 ) – Batchsize when transmitting data to MyScale.
Defaults to 32.
* **metadata** 
 (
 *List* 
*[* 
*dict* 
*]* 
*,* 
*optional* 
 ) – metadata to texts. Defaults to None.
* **into** 
 (
 *Other keyword arguments will pass* 
 ) – [clickhouse-connect](
 <https://clickhouse.com/docs/en/integrations/python#clickhouse-connect-driver-api>
 )




 Returns
 


 MyScale Index
 








*property*


 metadata_column
 

*:
 




 str*
[#](#langchain.vectorstores.MyScale.metadata_column "Permalink to this definition") 








 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *where_str
 



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
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/myscale#MyScale.similarity_search)
[#](#langchain.vectorstores.MyScale.similarity_search "Permalink to this definition") 



 Perform a similarity search with MyScale
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – query string
* **k** 
 (
 *int* 
*,* 
*optional* 
 ) – Top K neighbors to retrieve. Defaults to 4.
* **where_str** 
 (
 *Optional* 
*[* 
*str* 
*]* 
*,* 
*optional* 
 ) – where condition string.
Defaults to None.
* **NOTE** 
 – Please do not let end-user to fill this and always be aware
of SQL injection. When dealing with metadatas, remember to
use
 
 {self.metadata_column}.attribute
 
 instead of
 
 attribute
 
 alone. The default name for it is
 
 metadata
 
 .




 Returns
 


 List of Documents
 




 Return type
 


 List[Document]
 










 similarity_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *where_str
 



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
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/myscale#MyScale.similarity_search_by_vector)
[#](#langchain.vectorstores.MyScale.similarity_search_by_vector "Permalink to this definition") 



 Perform a similarity search with MyScale by vectors
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – query string
* **k** 
 (
 *int* 
*,* 
*optional* 
 ) – Top K neighbors to retrieve. Defaults to 4.
* **where_str** 
 (
 *Optional* 
*[* 
*str* 
*]* 
*,* 
*optional* 
 ) – where condition string.
Defaults to None.
* **NOTE** 
 – Please do not let end-user to fill this and always be aware
of SQL injection. When dealing with metadatas, remember to
use
 
 {self.metadata_column}.attribute
 
 instead of
 
 attribute
 
 alone. The default name for it is
 
 metadata
 
 .




 Returns
 


 List of (Document, similarity)
 




 Return type
 


 List[Document]
 










 similarity_search_with_relevance_scores
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *where_str
 



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
 





 Any*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/myscale#MyScale.similarity_search_with_relevance_scores)
[#](#langchain.vectorstores.MyScale.similarity_search_with_relevance_scores "Permalink to this definition") 



 Perform a similarity search with MyScale
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – query string
* **k** 
 (
 *int* 
*,* 
*optional* 
 ) – Top K neighbors to retrieve. Defaults to 4.
* **where_str** 
 (
 *Optional* 
*[* 
*str* 
*]* 
*,* 
*optional* 
 ) – where condition string.
Defaults to None.
* **NOTE** 
 – Please do not let end-user to fill this and always be aware
of SQL injection. When dealing with metadatas, remember to
use
 
 {self.metadata_column}.attribute
 
 instead of
 
 attribute
 
 alone. The default name for it is
 
 metadata
 
 .




 Returns
 


 List of documents
 




 Return type
 


 List[Document]
 










*pydantic
 

 settings*


 langchain.vectorstores.
 



 MyScaleSettings
 

[[source]](../../_modules/langchain/vectorstores/myscale#MyScaleSettings)
[#](#langchain.vectorstores.MyScaleSettings "Permalink to this definition") 



 MyScale Client Configuration
 




 Attribute:
 



 myscale_host (str)
 
 An URL to connect to MyScale backend.
 



 Defaults to ‘localhost’.
 





 myscale_port (int) : URL port to connect with HTTP. Defaults to 8443.
username (str) : Usernamed to login. Defaults to None.
password (str) : Password to login. Defaults to None.
index_type (str): index type string.
index_param (dict): index build parameter.
database (str) : Database name to find the table. Defaults to ‘default’.
table (str) : Table name to operate on.
 



> 
> 
> 
>  Defaults to ‘vector_table’.
>  
> 
> 
> 
> 




 metric (str)
 
 Metric to compute distance,
 



 supported are (‘l2’, ‘cosine’, ‘ip’). Defaults to ‘cosine’.
 




 column_map (Dict)
 
 Column type map to project column name onto langchain
 



 semantics. Must have keys:
 
 text
 
 ,
 
 id
 
 ,
 
 vector
 
 ,
must be same size to number of columns. For example:
.. code-block:: python
{
 



> 
> 
> 
>  ‘id’: ‘text_id’,
> ‘vector’: ‘text_embedding’,
> ‘text’: ‘text_plain’,
> ‘metadata’: ‘metadata_dictionary_in_json’,
>  
> 
> 
> 
> 



 }
 



 Defaults to identity map.
 









 Show JSON schema
 



```
{
 "title": "MyScaleSettings",
 "description": "MyScale Client Configuration\n\nAttribute:\n myscale_host (str) : An URL to connect to MyScale backend.\n Defaults to 'localhost'.\n myscale_port (int) : URL port to connect with HTTP. Defaults to 8443.\n username (str) : Usernamed to login. Defaults to None.\n password (str) : Password to login. Defaults to None.\n index_type (str): index type string.\n index_param (dict): index build parameter.\n database (str) : Database name to find the table. Defaults to 'default'.\n table (str) : Table name to operate on.\n Defaults to 'vector_table'.\n metric (str) : Metric to compute distance,\n supported are ('l2', 'cosine', 'ip'). Defaults to 'cosine'.\n column_map (Dict) : Column type map to project column name onto langchain\n semantics. Must have keys: `text`, `id`, `vector`,\n must be same size to number of columns. For example:\n .. code-block:: python\n {\n 'id': 'text_id',\n 'vector': 'text_embedding',\n 'text': 'text_plain',\n 'metadata': 'metadata_dictionary_in_json',\n }\n\n Defaults to identity map.",
 "type": "object",
 "properties": {
 "host": {
 "title": "Host",
 "default": "localhost",
 "env_names": "{'myscale_host'}",
 "type": "string"
 },
 "port": {
 "title": "Port",
 "default": 8443,
 "env_names": "{'myscale_port'}",
 "type": "integer"
 },
 "username": {
 "title": "Username",
 "env_names": "{'myscale_username'}",
 "type": "string"
 },
 "password": {
 "title": "Password",
 "env_names": "{'myscale_password'}",
 "type": "string"
 },
 "index_type": {
 "title": "Index Type",
 "default": "IVFFLAT",
 "env_names": "{'myscale_index_type'}",
 "type": "string"
 },
 "index_param": {
 "title": "Index Param",
 "env_names": "{'myscale_index_param'}",
 "type": "object",
 "additionalProperties": {
 "type": "string"
 }
 },
 "column_map": {
 "title": "Column Map",
 "default": {
 "id": "id",
 "text": "text",
 "vector": "vector",
 "metadata": "metadata"
 },
 "env_names": "{'myscale_column_map'}",
 "type": "object",
 "additionalProperties": {
 "type": "string"
 }
 },
 "database": {
 "title": "Database",
 "default": "default",
 "env_names": "{'myscale_database'}",
 "type": "string"
 },
 "table": {
 "title": "Table",
 "default": "langchain",
 "env_names": "{'myscale_table'}",
 "type": "string"
 },
 "metric": {
 "title": "Metric",
 "default": "cosine",
 "env_names": "{'myscale_metric'}",
 "type": "string"
 }
 },
 "additionalProperties": false
}

```









 Config
 

* **env_file** 
 :
 *str = .env*
* **env_file_encoding** 
 :
 *str = utf-8*
* **env_prefix** 
 :
 *str = myscale_*




 Fields
 

* `column_map
 

 (Dict[str,
 

 str])`
* `database
 

 (str)`
* `host
 

 (str)`
* `index_param
 

 (Optional[Dict[str,
 

 str]])`
* `index_type
 

 (str)`
* `metric
 

 (str)`
* `password
 

 (Optional[str])`
* `port
 

 (int)`
* `table
 

 (str)`
* `username
 

 (Optional[str])`






*field*


 column_map
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]*
*=
 




 {'id':
 

 'id',
 

 'metadata':
 

 'metadata',
 

 'text':
 

 'text',
 

 'vector':
 

 'vector'}*
[#](#langchain.vectorstores.MyScaleSettings.column_map "Permalink to this definition") 






*field*


 database
 

*:
 




 str*
*=
 




 'default'*
[#](#langchain.vectorstores.MyScaleSettings.database "Permalink to this definition") 






*field*


 host
 

*:
 




 str*
*=
 




 'localhost'*
[#](#langchain.vectorstores.MyScaleSettings.host "Permalink to this definition") 






*field*


 index_param
 

*:
 




 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.vectorstores.MyScaleSettings.index_param "Permalink to this definition") 






*field*


 index_type
 

*:
 




 str*
*=
 




 'IVFFLAT'*
[#](#langchain.vectorstores.MyScaleSettings.index_type "Permalink to this definition") 






*field*


 metric
 

*:
 




 str*
*=
 




 'cosine'*
[#](#langchain.vectorstores.MyScaleSettings.metric "Permalink to this definition") 






*field*


 password
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.vectorstores.MyScaleSettings.password "Permalink to this definition") 






*field*


 port
 

*:
 




 int*
*=
 




 8443*
[#](#langchain.vectorstores.MyScaleSettings.port "Permalink to this definition") 






*field*


 table
 

*:
 




 str*
*=
 




 'langchain'*
[#](#langchain.vectorstores.MyScaleSettings.table "Permalink to this definition") 






*field*


 username
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.vectorstores.MyScaleSettings.username "Permalink to this definition") 








*class*


 langchain.vectorstores.
 



 OpenSearchVectorSearch
 


 (
 
*opensearch_url
 



 :
 





 str*
 ,
 *index_name
 



 :
 





 str*
 ,
 *embedding_function
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/vectorstores/opensearch_vector_search#OpenSearchVectorSearch)
[#](#langchain.vectorstores.OpenSearchVectorSearch "Permalink to this definition") 



 Wrapper around OpenSearch as a vector database.
 



 Example
 





```
from langchain import OpenSearchVectorSearch
opensearch_vector_search = OpenSearchVectorSearch(
    "http://localhost:9200",
    "embeddings",
    embedding_function
)

```







 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *bulk_size
 



 :
 





 int
 





 =
 





 500*
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
 



[[source]](../../_modules/langchain/vectorstores/opensearch_vector_search#OpenSearchVectorSearch.add_texts)
[#](#langchain.vectorstores.OpenSearchVectorSearch.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the vectorstore.
* **metadatas** 
 – Optional list of metadatas associated with the texts.
* **bulk_size** 
 – Bulk API request count; Default: 500




 Returns
 


 List of ids from adding the texts into the vectorstore.
 






 Optional Args:
 


 vector_field: Document field embeddings are stored in. Defaults to
“vector_field”.
 



 text_field: Document field the text of the document is stored in. Defaults
to “text”.
 








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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *bulk_size
 



 :
 





 int
 





 =
 





 500*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.opensearch_vector_search.OpenSearchVectorSearch](#langchain.vectorstores.OpenSearchVectorSearch "langchain.vectorstores.opensearch_vector_search.OpenSearchVectorSearch")


[[source]](../../_modules/langchain/vectorstores/opensearch_vector_search#OpenSearchVectorSearch.from_texts)
[#](#langchain.vectorstores.OpenSearchVectorSearch.from_texts "Permalink to this definition") 



 Construct OpenSearchVectorSearch wrapper from raw documents.
 



 Example
 





```
from langchain import OpenSearchVectorSearch
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
opensearch_vector_search = OpenSearchVectorSearch.from_texts(
    texts,
    embeddings,
    opensearch_url="http://localhost:9200"
)

```




 OpenSearch by default supports Approximate Search powered by nmslib, faiss
and lucene engines recommended for large datasets. Also supports brute force
search through Script Scoring and Painless Scripting.
 




 Optional Args:
 


 vector_field: Document field embeddings are stored in. Defaults to
“vector_field”.
 



 text_field: Document field the text of the document is stored in. Defaults
to “text”.
 




 Optional Keyword Args for Approximate Search:
 


 engine: “nmslib”, “faiss”, “lucene”; default: “nmslib”
 



 space_type: “l2”, “l1”, “cosinesimil”, “linf”, “innerproduct”; default: “l2”
 



 ef_search: Size of the dynamic list used during k-NN searches. Higher values
lead to more accurate but slower searches; default: 512
 



 ef_construction: Size of the dynamic list used during k-NN graph creation.
Higher values lead to more accurate graph but slower indexing speed;
default: 512
 



 m: Number of bidirectional links created for each new element. Large impact
on memory consumption. Between 2 and 100; default: 16
 




 Keyword Args for Script Scoring or Painless Scripting:
 


 is_appx_search: False
 










 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/opensearch_vector_search#OpenSearchVectorSearch.similarity_search)
[#](#langchain.vectorstores.OpenSearchVectorSearch.similarity_search "Permalink to this definition") 



 Return docs most similar to query.
 



 By default supports Approximate Search.
Also supports Script Scoring and Painless Scripting.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.




 Returns
 


 List of Documents most similar to the query.
 






 Optional Args:
 


 vector_field: Document field embeddings are stored in. Defaults to
“vector_field”.
 



 text_field: Document field the text of the document is stored in. Defaults
to “text”.
 



 metadata_field: Document field that metadata is stored in. Defaults to
“metadata”.
Can be set to a special value “\*” to include the entire document.
 




 Optional Args for Approximate Search:
 


 search_type: “approximate_search”; default: “approximate_search”
 



 size: number of results the query actually returns; default: 4
 



 boolean_filter: A Boolean filter consists of a Boolean query that
contains a k-NN query and a filter.
 



 subquery_clause: Query clause on the knn vector field; default: “must”
 



 lucene_filter: the Lucene algorithm decides whether to perform an exact
k-NN search with pre-filtering or an approximate search with modified
post-filtering.
 




 Optional Args for Script Scoring Search:
 


 search_type: “script_scoring”; default: “approximate_search”
 



 space_type: “l2”, “l1”, “linf”, “cosinesimil”, “innerproduct”,
“hammingbit”; default: “l2”
 



 pre_filter: script_score query to pre-filter documents before identifying
nearest neighbors; default: {“match_all”: {}}
 




 Optional Args for Painless Scripting Search:
 


 search_type: “painless_scripting”; default: “approximate_search”
 



 space_type: “l2Squared”, “l1Norm”, “cosineSimilarity”; default: “l2Squared”
 



 pre_filter: script_score query to pre-filter documents before identifying
nearest neighbors; default: {“match_all”: {}}
 










*class*


 langchain.vectorstores.
 



 Pinecone
 


 (
 
*index
 



 :
 





 Any*
 ,
 *embedding_function
 



 :
 





 Callable*
 ,
 *text_key
 



 :
 





 str*
 ,
 *namespace
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/vectorstores/pinecone#Pinecone)
[#](#langchain.vectorstores.Pinecone "Permalink to this definition") 



 Wrapper around Pinecone vector database.
 



 To use, you should have the
 `pinecone-client`
 python package installed.
 



 Example
 





```
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

# The environment should be the one specified next to the API key
# in your Pinecone console
pinecone.init(api_key="\*\*\*", environment="...")
index = pinecone.Index("langchain-demo")
embeddings = OpenAIEmbeddings()
vectorstore = Pinecone(index, embeddings.embed_query, "text")

```







 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
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
 ,
 *namespace
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *batch_size
 



 :
 





 int
 





 =
 





 32*
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
 



[[source]](../../_modules/langchain/vectorstores/pinecone#Pinecone.add_texts)
[#](#langchain.vectorstores.Pinecone.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the vectorstore.
* **metadatas** 
 – Optional list of metadatas associated with the texts.
* **ids** 
 – Optional list of ids to associate with the texts.
* **namespace** 
 – Optional pinecone namespace to add the texts to.




 Returns
 


 List of ids from adding the texts into the vectorstore.
 








*classmethod*


 from_existing_index
 


 (
 
*index_name
 



 :
 





 str*
 ,
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *text_key
 



 :
 





 str
 





 =
 





 'text'*
 ,
 *namespace
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*

 )
 


 →
 

[langchain.vectorstores.pinecone.Pinecone](#langchain.vectorstores.Pinecone "langchain.vectorstores.pinecone.Pinecone")


[[source]](../../_modules/langchain/vectorstores/pinecone#Pinecone.from_existing_index)
[#](#langchain.vectorstores.Pinecone.from_existing_index "Permalink to this definition") 



 Load pinecone vectorstore from index name.
 






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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
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
 ,
 *batch_size
 



 :
 





 int
 





 =
 





 32*
 ,
 *text_key
 



 :
 





 str
 





 =
 





 'text'*
 ,
 *index_name
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *namespace
 



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
 





 Any*

 )
 


 →
 

[langchain.vectorstores.pinecone.Pinecone](#langchain.vectorstores.Pinecone "langchain.vectorstores.pinecone.Pinecone")


[[source]](../../_modules/langchain/vectorstores/pinecone#Pinecone.from_texts)
[#](#langchain.vectorstores.Pinecone.from_texts "Permalink to this definition") 



 Construct Pinecone wrapper from raw documents.
 




 This is a user friendly interface that:
 

1. Embeds documents.
2. Adds the documents to a provided Pinecone index





 This is intended to be a quick way to get started.
 



 Example
 





```
from langchain import Pinecone
from langchain.embeddings import OpenAIEmbeddings
import pinecone

# The environment should be the one specified next to the API key
# in your Pinecone console
pinecone.init(api_key="\*\*\*", environment="...")
embeddings = OpenAIEmbeddings()
pinecone = Pinecone.from_texts(
    texts,
    embeddings,
    index_name="langchain-demo"
)

```









 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *namespace
 



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
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/pinecone#Pinecone.similarity_search)
[#](#langchain.vectorstores.Pinecone.similarity_search "Permalink to this definition") 



 Return pinecone documents most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **filter** 
 – Dictionary of argument(s) to filter on metadata
* **namespace** 
 – Namespace to search in. Default will search in ‘’ namespace.




 Returns
 


 List of Documents most similar to the query and score for each
 










 similarity_search_with_score
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *namespace
 



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
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/pinecone#Pinecone.similarity_search_with_score)
[#](#langchain.vectorstores.Pinecone.similarity_search_with_score "Permalink to this definition") 



 Return pinecone documents most similar to query, along with scores.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **filter** 
 – Dictionary of argument(s) to filter on metadata
* **namespace** 
 – Namespace to search in. Default will search in ‘’ namespace.




 Returns
 


 List of Documents most similar to the query and score for each
 










*class*


 langchain.vectorstores.
 



 Qdrant
 


 (
 
*client
 



 :
 





 Any*
 ,
 *collection_name
 



 :
 





 str*
 ,
 *embedding_function
 



 :
 





 Callable*
 ,
 *content_payload_key
 



 :
 





 str
 





 =
 





 'page_content'*
 ,
 *metadata_payload_key
 



 :
 





 str
 





 =
 





 'metadata'*

 )
 
[[source]](../../_modules/langchain/vectorstores/qdrant#Qdrant)
[#](#langchain.vectorstores.Qdrant "Permalink to this definition") 



 Wrapper around Qdrant vector database.
 



 To use you should have the
 `qdrant-client`
 package installed.
 



 Example
 





```
from qdrant_client import QdrantClient
from langchain import Qdrant

client = QdrantClient()
collection_name = "MyCollection"
qdrant = Qdrant(client, collection_name, embedding_function)

```







 CONTENT_KEY
 

*=
 




 'page_content'*
[#](#langchain.vectorstores.Qdrant.CONTENT_KEY "Permalink to this definition") 








 METADATA_KEY
 

*=
 




 'metadata'*
[#](#langchain.vectorstores.Qdrant.METADATA_KEY "Permalink to this definition") 








 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/qdrant#Qdrant.add_texts)
[#](#langchain.vectorstores.Qdrant.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the vectorstore.
* **metadatas** 
 – Optional list of metadatas associated with the texts.




 Returns
 


 List of ids from adding the texts into the vectorstore.
 








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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *location
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *url
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *port
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 6333*
 ,
 *grpc_port
 



 :
 





 int
 





 =
 





 6334*
 ,
 *prefer_grpc
 



 :
 





 bool
 





 =
 





 False*
 ,
 *https
 



 :
 





 Optional
 


 [
 


 bool
 


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
 *prefix
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *timeout
 



 :
 





 Optional
 


 [
 


 float
 


 ]
 






 =
 





 None*
 ,
 *host
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *path
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *collection_name
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *distance_func
 



 :
 





 str
 





 =
 





 'Cosine'*
 ,
 *content_payload_key
 



 :
 





 str
 





 =
 





 'page_content'*
 ,
 *metadata_payload_key
 



 :
 





 str
 





 =
 





 'metadata'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.qdrant.Qdrant](#langchain.vectorstores.Qdrant "langchain.vectorstores.qdrant.Qdrant")


[[source]](../../_modules/langchain/vectorstores/qdrant#Qdrant.from_texts)
[#](#langchain.vectorstores.Qdrant.from_texts "Permalink to this definition") 



 Construct Qdrant wrapper from a list of texts.
 




 Parameters
 

* **texts** 
 – A list of texts to be indexed in Qdrant.
* **embedding** 
 – A subclass of
 
 Embeddings
 
 , responsible for text vectorization.
* **metadatas** 
 – An optional list of metadata. If provided it has to be of the same
length as a list of texts.
* **location** 
 – If
 
 :memory:
 
 - use in-memory Qdrant instance.
If
 
 str
 
 - use it as a
 
 url
 
 parameter.
If
 
 None
 
 - fallback to relying on
 
 host
 
 and
 
 port
 
 parameters.
* **url** 
 – either host or str of “Optional[scheme], host, Optional[port],
Optional[prefix]”. Default:
 
 None
* **port** 
 – Port of the REST API interface. Default: 6333
* **grpc_port** 
 – Port of the gRPC interface. Default: 6334
* **prefer_grpc** 
 – If true - use gPRC interface whenever possible in custom methods.
Default: False
* **https** 
 – If true - use HTTPS(SSL) protocol. Default: None
* **api_key** 
 – API key for authentication in Qdrant Cloud. Default: None
* **prefix** 
 –
 
 If not None - add prefix to the REST URL path.
Example: service/v1 will result in
 



> 
> 
> 
> <http://localhost:6333/service/v1>
>  /{qdrant-endpoint} for REST API.
>  
> 
> 
> 
> 



 Default: None
* **timeout** 
 – Timeout for REST and gRPC API requests.
Default: 5.0 seconds for REST and unlimited for gRPC
* **host** 
 – Host name of Qdrant service. If url and host are None, set to
‘localhost’. Default: None
* **path** 
 – Path in which the vectors will be stored while using local mode.
Default: None
* **collection_name** 
 – Name of the Qdrant collection to be used. If not provided,
it will be created randomly. Default: None
* **distance_func** 
 – Distance function. One of: “Cosine” / “Euclid” / “Dot”.
Default: “Cosine”
* **content_payload_key** 
 – A payload key used to store the content of the document.
Default: “page_content”
* **metadata_payload_key** 
 – A payload key used to store the metadata of the document.
Default: “metadata”
* **\*\*kwargs** 
 – Additional arguments passed directly into REST client initialization






 This is a user friendly interface that:
 

1. Creates embeddings, one for each text
2. Initializes the Qdrant database as an in-memory docstore by default
(and overridable to a remote docstore)
3. Adds the text embeddings to the Qdrant database





 This is intended to be a quick way to get started.
 



 Example
 





```
from langchain import Qdrant
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
qdrant = Qdrant.from_texts(texts, embeddings, "localhost")

```









 max_marginal_relevance_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/qdrant#Qdrant.max_marginal_relevance_search)
[#](#langchain.vectorstores.Qdrant.max_marginal_relevance_search "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 



 Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
Defaults to 20.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5.




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



 :
 





 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Union
 


 [
 


 str
 


 ,
 




 int
 


 ,
 




 bool
 


 ]
 



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
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/qdrant#Qdrant.similarity_search)
[#](#langchain.vectorstores.Qdrant.similarity_search "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **filter** 
 – Filter by metadata. Defaults to None.




 Returns
 


 List of Documents most similar to the query.
 










 similarity_search_with_score
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *filter
 



 :
 





 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Union
 


 [
 


 str
 


 ,
 




 int
 


 ,
 




 bool
 


 ]
 



 ]
 



 ]
 






 =
 





 None*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/qdrant#Qdrant.similarity_search_with_score)
[#](#langchain.vectorstores.Qdrant.similarity_search_with_score "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **filter** 
 – Filter by metadata. Defaults to None.




 Returns
 


 List of Documents most similar to the query and score for each.
 










*class*


 langchain.vectorstores.
 



 Redis
 


 (
 
*redis_url
 



 :
 





 str*
 ,
 *index_name
 



 :
 





 str*
 ,
 *embedding_function
 



 :
 





 Callable*
 ,
 *content_key
 



 :
 





 str
 





 =
 





 'content'*
 ,
 *metadata_key
 



 :
 





 str
 





 =
 





 'metadata'*
 ,
 *vector_key
 



 :
 





 str
 





 =
 





 'content_vector'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/vectorstores/redis#Redis)
[#](#langchain.vectorstores.Redis "Permalink to this definition") 



 Wrapper around Redis vector database.
 



 To use, you should have the
 `redis`
 python package installed.
 



 Example
 





```
from langchain.vectorstores import Redis
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = Redis(
    redis_url="redis://username:password@localhost:6379"
    index_name="my-index",
    embedding_function=embeddings.embed_query,
)

```







 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *embeddings
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



 ]
 






 =
 





 None*
 ,
 *keys
 



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
 *batch_size
 



 :
 





 int
 





 =
 





 1000*
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
 



[[source]](../../_modules/langchain/vectorstores/redis#Redis.add_texts)
[#](#langchain.vectorstores.Redis.add_texts "Permalink to this definition") 



 Add more texts to the vectorstore.
 




 Parameters
 

* **texts** 
 (
 *Iterable* 
*[* 
*str* 
*]* 
 ) – Iterable of strings/text to add to the vectorstore.
* **metadatas** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*dict* 
*]* 
*]* 
*,* 
*optional* 
 ) – Optional list of metadatas.
Defaults to None.
* **embeddings** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*List* 
*[* 
*float* 
*]* 
*]* 
*]* 
*,* 
*optional* 
 ) – Optional pre-generated
embeddings. Defaults to None.
* **keys** 
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
 ) – Optional key values to use as ids.
Defaults to None.
* **batch_size** 
 (
 *int* 
*,* 
*optional* 
 ) – Batch size to use for writes. Defaults to 1000.




 Returns
 


 List of ids added to the vectorstore
 




 Return type
 


 List[str]
 










 as_retriever
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.schema.BaseRetriever
 


[[source]](../../_modules/langchain/vectorstores/redis#Redis.as_retriever)
[#](#langchain.vectorstores.Redis.as_retriever "Permalink to this definition") 






*static*


 drop_index
 


 (
 
*index_name
 



 :
 





 str*
 ,
 *delete_documents
 



 :
 





 bool*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 bool
 


[[source]](../../_modules/langchain/vectorstores/redis#Redis.drop_index)
[#](#langchain.vectorstores.Redis.drop_index "Permalink to this definition") 



 Drop a Redis search index.
 




 Parameters
 

* **index_name** 
 (
 *str* 
 ) – Name of the index to drop.
* **delete_documents** 
 (
 *bool* 
 ) – Whether to drop the associated documents.




 Returns
 


 Whether or not the drop was successful.
 




 Return type
 


 bool
 








*classmethod*


 from_existing_index
 


 (
 
*embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *index_name
 



 :
 





 str*
 ,
 *content_key
 



 :
 





 str
 





 =
 





 'content'*
 ,
 *metadata_key
 



 :
 





 str
 





 =
 





 'metadata'*
 ,
 *vector_key
 



 :
 





 str
 





 =
 





 'content_vector'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.redis.Redis](#langchain.vectorstores.Redis "langchain.vectorstores.redis.Redis")


[[source]](../../_modules/langchain/vectorstores/redis#Redis.from_existing_index)
[#](#langchain.vectorstores.Redis.from_existing_index "Permalink to this definition") 



 Connect to an existing Redis index.
 






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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *index_name
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *content_key
 



 :
 





 str
 





 =
 





 'content'*
 ,
 *metadata_key
 



 :
 





 str
 





 =
 





 'metadata'*
 ,
 *vector_key
 



 :
 





 str
 





 =
 





 'content_vector'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.redis.Redis](#langchain.vectorstores.Redis "langchain.vectorstores.redis.Redis")


[[source]](../../_modules/langchain/vectorstores/redis#Redis.from_texts)
[#](#langchain.vectorstores.Redis.from_texts "Permalink to this definition") 



 Create a Redis vectorstore from raw documents.
This is a user-friendly interface that:
 



> 
> 
> 1. Embeds documents.
> 2. Creates a new index for the embeddings in Redis.
> 3. Adds the documents to the newly created Redis index.
> 
> 
> 
> 



 This is intended to be a quick way to get started.
.. rubric:: Example
 








 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/redis#Redis.similarity_search)
[#](#langchain.vectorstores.Redis.similarity_search "Permalink to this definition") 



 Returns the most similar indexed documents to the query text.
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – The query text for which to find similar documents.
* **k** 
 (
 *int* 
 ) – The number of documents to return. Default is 4.




 Returns
 


 A list of documents that are most similar to the query text.
 




 Return type
 


 List[Document]
 










 similarity_search_limit_score
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *score_threshold
 



 :
 





 float
 





 =
 





 0.2*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/redis#Redis.similarity_search_limit_score)
[#](#langchain.vectorstores.Redis.similarity_search_limit_score "Permalink to this definition") 



 Returns the most similar indexed documents to the query text within the
score_threshold range.
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – The query text for which to find similar documents.
* **k** 
 (
 *int* 
 ) – The number of documents to return. Default is 4.
* **score_threshold** 
 (
 *float* 
 ) – The minimum matching score required for a document
* **0.2.** 
 (
 *to be considered a match. Defaults to* 
 ) –
* **similarity** 
 (
 *Because the similarity calculation algorithm is based on cosine* 
 ) –





 :param :
:param the smaller the angle:
:param the higher the similarity.:
 




 Returns
 


 A list of documents that are most similar to the query text,
including the match score for each document.
 




 Return type
 


 List[Document]
 






 Note
 



 If there are no documents that satisfy the score_threshold value,
an empty list is returned.
 









 similarity_search_with_score
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/redis#Redis.similarity_search_with_score)
[#](#langchain.vectorstores.Redis.similarity_search_with_score "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.




 Returns
 


 List of Documents most similar to the query and score for each
 










*class*


 langchain.vectorstores.
 



 SupabaseVectorStore
 


 (
 
*client
 



 :
 





 supabase.client.Client*
 ,
 *embedding
 



 :
 





 Embeddings*
 ,
 *table_name
 



 :
 





 str*
 ,
 *query_name
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 None
 


 ]
 






 =
 





 None*

 )
 
[[source]](../../_modules/langchain/vectorstores/supabase#SupabaseVectorStore)
[#](#langchain.vectorstores.SupabaseVectorStore "Permalink to this definition") 



 VectorStore for a Supabase postgres database. Assumes you have the
 
 pgvector
 
 extension installed and a
 
 match_documents
 
 (or similar) function. For more details:
 <https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase>




 You can implement your own
 
 match_documents
 
 function in order to limit the search
space to a subset of documents based on your own authorization or business logic.
 



 Note that the Supabase Python client does not yet support async operations.
 



 If you’d like to use
 
 max_marginal_relevance_search
 
 , please review the instructions
below on modifying the
 
 match_documents
 
 function to return matched embeddings.
 






 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 [
 


 Any
 


 ,
 




 Any
 


 ]
 



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
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/supabase#SupabaseVectorStore.add_texts)
[#](#langchain.vectorstores.SupabaseVectorStore.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the vectorstore.
* **metadatas** 
 – Optional list of metadatas associated with the texts.
* **kwargs** 
 – vectorstore specific parameters




 Returns
 


 List of ids from adding the texts into the vectorstore.
 










 add_vectors
 


 (
 
*vectors
 



 :
 





 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]*
 ,
 *documents
 



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
 



[[source]](../../_modules/langchain/vectorstores/supabase#SupabaseVectorStore.add_vectors)
[#](#langchain.vectorstores.SupabaseVectorStore.add_vectors "Permalink to this definition") 






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
 *embedding
 



 :
 





 Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *client
 



 :
 





 Optional
 


 [
 


 supabase.client.Client
 


 ]
 






 =
 





 None*
 ,
 *table_name
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 'documents'*
 ,
 *query_name
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 None
 


 ]
 






 =
 





 'match_documents'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[SupabaseVectorStore](#langchain.vectorstores.SupabaseVectorStore "langchain.vectorstores.SupabaseVectorStore")


[[source]](../../_modules/langchain/vectorstores/supabase#SupabaseVectorStore.from_texts)
[#](#langchain.vectorstores.SupabaseVectorStore.from_texts "Permalink to this definition") 



 Return VectorStore initialized from texts and embeddings.
 








 max_marginal_relevance_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/supabase#SupabaseVectorStore.max_marginal_relevance_search)
[#](#langchain.vectorstores.SupabaseVectorStore.max_marginal_relevance_search "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 



 Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5.




 Returns
 


 List of Documents selected by maximal marginal relevance.
 






 max_marginal_relevance_search
 
 requires that
 
 query_name
 
 returns matched
embeddings alongside the match documents. The following function function
demonstrates how to do this:
 [``](#id3)
[`](#id5)
 sql
CREATE FUNCTION match_documents_embeddings(query_embedding vector(1536),
 



> 
> 
> 
> > 
> > 
> > 
> >  match_count int)
> >  
> > 
> > 
> > 
> > 
> 
> 
> 
> 
>  RETURNS TABLE(
>  
> 
> 
>  id bigint,
> content text,
> metadata jsonb,
> embedding vector(1536),
> similarity float)
>  
> 
> 
> 
> 
> 
>  LANGUAGE plpgsql
> AS $$
> # variable_conflict use_column
>  
> 
> 
> 
> 




 BEGIN
 


 RETURN query
SELECT
 



> 
> 
> 
>  id,
> content,
> metadata,
> embedding,
> 1 -(docstore.embedding <=> query_embedding) AS similarity
>  
> 
> 
> 
> 




 FROM
 


 docstore
 




 ORDER BY
 


 docstore.embedding <=> query_embedding
 





 LIMIT match_count;
 





 END;
$$;```
 








 max_marginal_relevance_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/supabase#SupabaseVectorStore.max_marginal_relevance_search_by_vector)
[#](#langchain.vectorstores.SupabaseVectorStore.max_marginal_relevance_search_by_vector "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 



 Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
 




 Parameters
 

* **embedding** 
 – Embedding to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5.




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 query_name
 

*:
 




 str*
[#](#langchain.vectorstores.SupabaseVectorStore.query_name "Permalink to this definition") 








 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/supabase#SupabaseVectorStore.similarity_search)
[#](#langchain.vectorstores.SupabaseVectorStore.similarity_search "Permalink to this definition") 



 Return docs most similar to query.
 








 similarity_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/supabase#SupabaseVectorStore.similarity_search_by_vector)
[#](#langchain.vectorstores.SupabaseVectorStore.similarity_search_by_vector "Permalink to this definition") 



 Return docs most similar to embedding vector.
 




 Parameters
 

* **embedding** 
 – Embedding to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.




 Returns
 


 List of Documents most similar to the query vector.
 










 similarity_search_by_vector_returning_embeddings
 


 (
 
*query
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 Document
 


 ,
 




 float
 


 ,
 




 np.ndarray
 


 [
 


 np.float32
 


 ,
 




 Any
 


 ]
 



 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/supabase#SupabaseVectorStore.similarity_search_by_vector_returning_embeddings)
[#](#langchain.vectorstores.SupabaseVectorStore.similarity_search_by_vector_returning_embeddings "Permalink to this definition") 








 similarity_search_by_vector_with_relevance_scores
 


 (
 
*query
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/supabase#SupabaseVectorStore.similarity_search_by_vector_with_relevance_scores)
[#](#langchain.vectorstores.SupabaseVectorStore.similarity_search_by_vector_with_relevance_scores "Permalink to this definition") 








 similarity_search_with_relevance_scores
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/supabase#SupabaseVectorStore.similarity_search_with_relevance_scores)
[#](#langchain.vectorstores.SupabaseVectorStore.similarity_search_with_relevance_scores "Permalink to this definition") 



 Return docs and relevance scores in the range [0, 1].
 



 0 is dissimilar, 1 is most similar.
 








 table_name
 

*:
 




 str*
[#](#langchain.vectorstores.SupabaseVectorStore.table_name "Permalink to this definition") 








*class*


 langchain.vectorstores.
 



 Tair
 


 (
 
*embedding_function
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *url
 



 :
 





 str*
 ,
 *index_name
 



 :
 





 str*
 ,
 *content_key
 



 :
 





 str
 





 =
 





 'content'*
 ,
 *metadata_key
 



 :
 





 str
 





 =
 





 'metadata'*
 ,
 *search_params
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/vectorstores/tair#Tair)
[#](#langchain.vectorstores.Tair "Permalink to this definition") 






 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/tair#Tair.add_texts)
[#](#langchain.vectorstores.Tair.add_texts "Permalink to this definition") 



 Add texts data to an existing index.
 








 create_index_if_not_exist
 


 (
 
*dim
 



 :
 





 int*
 ,
 *distance_type
 



 :
 





 str*
 ,
 *index_type
 



 :
 





 str*
 ,
 *data_type
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 bool
 


[[source]](../../_modules/langchain/vectorstores/tair#Tair.create_index_if_not_exist)
[#](#langchain.vectorstores.Tair.create_index_if_not_exist "Permalink to this definition") 






*static*


 drop_index
 


 (
 
*index_name
 



 :
 





 str
 





 =
 





 'langchain'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 bool
 


[[source]](../../_modules/langchain/vectorstores/tair#Tair.drop_index)
[#](#langchain.vectorstores.Tair.drop_index "Permalink to this definition") 



 Drop an existing index.
 




 Parameters
 


**index_name** 
 (
 *str* 
 ) – Name of the index to drop.
 




 Returns
 


 True if the index is dropped successfully.
 




 Return type
 


 bool
 








*classmethod*


 from_documents
 


 (
 
*documents
 



 :
 





 List
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *index_name
 



 :
 





 str
 





 =
 





 'langchain'*
 ,
 *content_key
 



 :
 





 str
 





 =
 





 'content'*
 ,
 *metadata_key
 



 :
 





 str
 





 =
 





 'metadata'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.tair.Tair](#langchain.vectorstores.Tair "langchain.vectorstores.tair.Tair")


[[source]](../../_modules/langchain/vectorstores/tair#Tair.from_documents)
[#](#langchain.vectorstores.Tair.from_documents "Permalink to this definition") 



 Return VectorStore initialized from documents and embeddings.
 






*classmethod*


 from_existing_index
 


 (
 
*embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *index_name
 



 :
 





 str
 





 =
 





 'langchain'*
 ,
 *content_key
 



 :
 





 str
 





 =
 





 'content'*
 ,
 *metadata_key
 



 :
 





 str
 





 =
 





 'metadata'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.tair.Tair](#langchain.vectorstores.Tair "langchain.vectorstores.tair.Tair")


[[source]](../../_modules/langchain/vectorstores/tair#Tair.from_existing_index)
[#](#langchain.vectorstores.Tair.from_existing_index "Permalink to this definition") 



 Connect to an existing Tair index.
 






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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *index_name
 



 :
 





 str
 





 =
 





 'langchain'*
 ,
 *content_key
 



 :
 





 str
 





 =
 





 'content'*
 ,
 *metadata_key
 



 :
 





 str
 





 =
 





 'metadata'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.vectorstores.tair.Tair](#langchain.vectorstores.Tair "langchain.vectorstores.tair.Tair")


[[source]](../../_modules/langchain/vectorstores/tair#Tair.from_texts)
[#](#langchain.vectorstores.Tair.from_texts "Permalink to this definition") 



 Return VectorStore initialized from texts and embeddings.
 








 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/tair#Tair.similarity_search)
[#](#langchain.vectorstores.Tair.similarity_search "Permalink to this definition") 



 Returns the most similar indexed documents to the query text.
 




 Parameters
 

* **query** 
 (
 *str* 
 ) – The query text for which to find similar documents.
* **k** 
 (
 *int* 
 ) – The number of documents to return. Default is 4.




 Returns
 


 A list of documents that are most similar to the query text.
 




 Return type
 


 List[Document]
 










*class*


 langchain.vectorstores.
 



 VectorStore
 

[[source]](../../_modules/langchain/vectorstores/base#VectorStore)
[#](#langchain.vectorstores.VectorStore "Permalink to this definition") 



 Interface for vector stores.
 




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
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.aadd_documents)
[#](#langchain.vectorstores.VectorStore.aadd_documents "Permalink to this definition") 



 Run more documents through the embeddings and add to the vectorstore.
 




 Parameters
 


**(** 
**List** 
**[** 
**Document** 
**]** 
 (
 *documents* 
 ) – Documents to add to the vectorstore.
 




 Returns
 


 List of IDs of the added texts.
 




 Return type
 


 List[str]
 








*async*


 aadd_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.aadd_texts)
[#](#langchain.vectorstores.VectorStore.aadd_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 








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
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.add_documents)
[#](#langchain.vectorstores.VectorStore.add_documents "Permalink to this definition") 



 Run more documents through the embeddings and add to the vectorstore.
 




 Parameters
 


**(** 
**List** 
**[** 
**Document** 
**]** 
 (
 *documents* 
 ) – Documents to add to the vectorstore.
 




 Returns
 


 List of IDs of the added texts.
 




 Return type
 


 List[str]
 








*abstract*


 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.add_texts)
[#](#langchain.vectorstores.VectorStore.add_texts "Permalink to this definition") 



 Run more texts through the embeddings and add to the vectorstore.
 




 Parameters
 

* **texts** 
 – Iterable of strings to add to the vectorstore.
* **metadatas** 
 – Optional list of metadatas associated with the texts.
* **kwargs** 
 – vectorstore specific parameters




 Returns
 


 List of ids from adding the texts into the vectorstore.
 








*async
 



 classmethod*


 afrom_documents
 


 (
 
*documents
 



 :
 





 List
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.vectorstores.base.VST
 


[[source]](../../_modules/langchain/vectorstores/base#VectorStore.afrom_documents)
[#](#langchain.vectorstores.VectorStore.afrom_documents "Permalink to this definition") 



 Return VectorStore initialized from documents and embeddings.
 






*async
 



 classmethod*


 afrom_texts
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 


 langchain.vectorstores.base.VST
 


[[source]](../../_modules/langchain/vectorstores/base#VectorStore.afrom_texts)
[#](#langchain.vectorstores.VectorStore.afrom_texts "Permalink to this definition") 



 Return VectorStore initialized from texts and embeddings.
 






*async*


 amax_marginal_relevance_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.amax_marginal_relevance_search)
[#](#langchain.vectorstores.VectorStore.amax_marginal_relevance_search "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 






*async*


 amax_marginal_relevance_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.amax_marginal_relevance_search_by_vector)
[#](#langchain.vectorstores.VectorStore.amax_marginal_relevance_search_by_vector "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 








 as_retriever
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.schema.BaseRetriever
 


[[source]](../../_modules/langchain/vectorstores/base#VectorStore.as_retriever)
[#](#langchain.vectorstores.VectorStore.as_retriever "Permalink to this definition") 






*async*


 asearch
 


 (
 
*query
 



 :
 





 str*
 ,
 *search_type
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.asearch)
[#](#langchain.vectorstores.VectorStore.asearch "Permalink to this definition") 



 Return docs most similar to query using specified search type.
 






*async*


 asimilarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.asimilarity_search)
[#](#langchain.vectorstores.VectorStore.asimilarity_search "Permalink to this definition") 



 Return docs most similar to query.
 






*async*


 asimilarity_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.asimilarity_search_by_vector)
[#](#langchain.vectorstores.VectorStore.asimilarity_search_by_vector "Permalink to this definition") 



 Return docs most similar to embedding vector.
 






*classmethod*


 from_documents
 


 (
 
*documents
 



 :
 





 List
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.vectorstores.base.VST
 


[[source]](../../_modules/langchain/vectorstores/base#VectorStore.from_documents)
[#](#langchain.vectorstores.VectorStore.from_documents "Permalink to this definition") 



 Return VectorStore initialized from documents and embeddings.
 






*abstract
 



 classmethod*


 from_texts
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 


 langchain.vectorstores.base.VST
 


[[source]](../../_modules/langchain/vectorstores/base#VectorStore.from_texts)
[#](#langchain.vectorstores.VectorStore.from_texts "Permalink to this definition") 



 Return VectorStore initialized from texts and embeddings.
 








 max_marginal_relevance_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.max_marginal_relevance_search)
[#](#langchain.vectorstores.VectorStore.max_marginal_relevance_search "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 



 Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5.




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 max_marginal_relevance_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.max_marginal_relevance_search_by_vector)
[#](#langchain.vectorstores.VectorStore.max_marginal_relevance_search_by_vector "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 



 Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
 




 Parameters
 

* **embedding** 
 – Embedding to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5.




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 search
 


 (
 
*query
 



 :
 





 str*
 ,
 *search_type
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.search)
[#](#langchain.vectorstores.VectorStore.search "Permalink to this definition") 



 Return docs most similar to query using specified search type.
 






*abstract*


 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.similarity_search)
[#](#langchain.vectorstores.VectorStore.similarity_search "Permalink to this definition") 



 Return docs most similar to query.
 








 similarity_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.similarity_search_by_vector)
[#](#langchain.vectorstores.VectorStore.similarity_search_by_vector "Permalink to this definition") 



 Return docs most similar to embedding vector.
 




 Parameters
 

* **embedding** 
 – Embedding to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.




 Returns
 


 List of Documents most similar to the query vector.
 










 similarity_search_with_relevance_scores
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 Tuple
 


 [
 


 langchain.schema.Document
 


 ,
 




 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/vectorstores/base#VectorStore.similarity_search_with_relevance_scores)
[#](#langchain.vectorstores.VectorStore.similarity_search_with_relevance_scores "Permalink to this definition") 



 Return docs and relevance scores in the range [0, 1].
 



 0 is dissimilar, 1 is most similar.
 








*class*


 langchain.vectorstores.
 



 Weaviate
 


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
 *embedding
 



 :
 





 Optional
 


 [
 


 langchain.embeddings.base.Embeddings
 


 ]
 






 =
 





 None*
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
 
[[source]](../../_modules/langchain/vectorstores/weaviate#Weaviate)
[#](#langchain.vectorstores.Weaviate "Permalink to this definition") 



 Wrapper around Weaviate vector database.
 



 To use, you should have the
 `weaviate-client`
 python package installed.
 



 Example
 





```
import weaviate
from langchain.vectorstores import Weaviate
client = weaviate.Client(url=os.environ["WEAVIATE_URL"], ...)
weaviate = Weaviate(client, index_name, text_key)

```







 add_texts
 


 (
 
*texts
 



 :
 





 Iterable
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/weaviate#Weaviate.add_texts)
[#](#langchain.vectorstores.Weaviate.add_texts "Permalink to this definition") 



 Upload texts with metadata (properties) to Weaviate.
 






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
 *embedding
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


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
 

[langchain.vectorstores.weaviate.Weaviate](#langchain.vectorstores.Weaviate "langchain.vectorstores.weaviate.Weaviate")


[[source]](../../_modules/langchain/vectorstores/weaviate#Weaviate.from_texts)
[#](#langchain.vectorstores.Weaviate.from_texts "Permalink to this definition") 



 Construct Weaviate wrapper from raw documents.
 




 This is a user-friendly interface that:
 

1. Embeds documents.
2. Creates a new index for the embeddings in the Weaviate instance.
3. Adds the documents to the newly created Weaviate index.





 This is intended to be a quick way to get started.
 



 Example
 





```
from langchain.vectorstores.weaviate import Weaviate
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
weaviate = Weaviate.from_texts(
    texts,
    embeddings,
    weaviate_url="http://localhost:8080"
)

```









 max_marginal_relevance_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/weaviate#Weaviate.max_marginal_relevance_search)
[#](#langchain.vectorstores.Weaviate.max_marginal_relevance_search "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 



 Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5.




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 max_marginal_relevance_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *fetch_k
 



 :
 





 int
 





 =
 





 20*
 ,
 *lambda_mult
 



 :
 





 float
 





 =
 





 0.5*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/weaviate#Weaviate.max_marginal_relevance_search_by_vector)
[#](#langchain.vectorstores.Weaviate.max_marginal_relevance_search_by_vector "Permalink to this definition") 



 Return docs selected using the maximal marginal relevance.
 



 Maximal marginal relevance optimizes for similarity to query AND diversity
among selected documents.
 




 Parameters
 

* **embedding** 
 – Embedding to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.
* **fetch_k** 
 – Number of Documents to fetch to pass to MMR algorithm.
* **lambda_mult** 
 – Number between 0 and 1 that determines the degree
of diversity among the results with 0 corresponding
to maximum diversity and 1 to minimum diversity.
Defaults to 0.5.




 Returns
 


 List of Documents selected by maximal marginal relevance.
 










 similarity_search
 


 (
 
*query
 



 :
 





 str*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/weaviate#Weaviate.similarity_search)
[#](#langchain.vectorstores.Weaviate.similarity_search "Permalink to this definition") 



 Return docs most similar to query.
 




 Parameters
 

* **query** 
 – Text to look up documents similar to.
* **k** 
 – Number of Documents to return. Defaults to 4.




 Returns
 


 List of Documents most similar to the query.
 










 similarity_search_by_vector
 


 (
 
*embedding
 



 :
 





 List
 


 [
 


 float
 


 ]*
 ,
 *k
 



 :
 





 int
 





 =
 





 4*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/vectorstores/weaviate#Weaviate.similarity_search_by_vector)
[#](#langchain.vectorstores.Weaviate.similarity_search_by_vector "Permalink to this definition") 



 Look up similar documents by embedding vector in Weaviate.
 








*class*


 langchain.vectorstores.
 



 Zilliz
 


 (
 
*embedding_function
 



 :
 





 Embeddings*
 ,
 *collection_name
 



 :
 





 str
 





 =
 





 'LangChainCollection'*
 ,
 *connection_args
 



 :
 





 Optional
 


 [
 


 dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *consistency_level
 



 :
 





 str
 





 =
 





 'Session'*
 ,
 *index_params
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *search_params
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *drop_old
 



 :
 





 Optional
 


 [
 


 bool
 


 ]
 






 =
 





 False*

 )
 
[[source]](../../_modules/langchain/vectorstores/zilliz#Zilliz)
[#](#langchain.vectorstores.Zilliz "Permalink to this definition") 




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
 *embedding
 



 :
 





 Embeddings*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *collection_name
 



 :
 





 str
 





 =
 





 'LangChainCollection'*
 ,
 *connection_args
 



 :
 





 dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 






 =
 





 {}*
 ,
 *consistency_level
 



 :
 





 str
 





 =
 





 'Session'*
 ,
 *index_params
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *search_params
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *drop_old
 



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
 


 →
 

[Zilliz](#langchain.vectorstores.Zilliz "langchain.vectorstores.Zilliz")


[[source]](../../_modules/langchain/vectorstores/zilliz#Zilliz.from_texts)
[#](#langchain.vectorstores.Zilliz.from_texts "Permalink to this definition") 



 Create a Zilliz collection, indexes it with HNSW, and insert data.
 




 Parameters
 

* **texts** 
 (
 *List* 
*[* 
*str* 
*]* 
 ) – Text data.
* **embedding** 
 (
 *Embeddings* 
 ) – Embedding function.
* **metadatas** 
 (
 *Optional* 
*[* 
*List* 
*[* 
*dict* 
*]* 
*]* 
 ) – Metadata for each text if it exists.
Defaults to None.
* **collection_name** 
 (
 *str* 
*,* 
*optional* 
 ) – Collection name to use. Defaults to
“LangChainCollection”.
* **connection_args** 
 (
 *dict* 
*[* 
*str* 
*,* 
*Any* 
*]* 
*,* 
*optional* 
 ) – Connection args to use. Defaults
to DEFAULT_MILVUS_CONNECTION.
* **consistency_level** 
 (
 *str* 
*,* 
*optional* 
 ) – Which consistency level to use. Defaults
to “Session”.
* **index_params** 
 (
 *Optional* 
*[* 
*dict* 
*]* 
*,* 
*optional* 
 ) – Which index_params to use.
Defaults to None.
* **search_params** 
 (
 *Optional* 
*[* 
*dict* 
*]* 
*,* 
*optional* 
 ) – Which search params to use.
Defaults to None.
* **drop_old** 
 (
 *Optional* 
*[* 
*bool* 
*]* 
*,* 
*optional* 
 ) – Whether to drop the collection with
that name if it exists. Defaults to False.




 Returns
 


 Zilliz Vector Store
 




 Return type
 


[Zilliz](#langchain.vectorstores.Zilliz "langchain.vectorstores.Zilliz") 











