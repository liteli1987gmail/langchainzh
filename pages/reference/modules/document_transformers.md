




 Document Transformers
 [#](#module-langchain.document_transformers "Permalink to this headline")
==================================================================================================



 Transform documents
 




*pydantic
 

 model*


 langchain.document_transformers.
 



 EmbeddingsRedundantFilter
 

[[source]](../../_modules/langchain/document_transformers#EmbeddingsRedundantFilter)
[#](#langchain.document_transformers.EmbeddingsRedundantFilter "Permalink to this definition") 



 Filter that drops redundant documents by comparing their embeddings.
 




*field*


 embeddings
 

*:
 




 langchain.embeddings.base.Embeddings*
*[Required]*
[#](#langchain.document_transformers.EmbeddingsRedundantFilter.embeddings "Permalink to this definition") 



 Embeddings to use for embedding document contents.
 






*field*


 similarity_fn
 

*:
 




 Callable*
*=
 




 <function
 

 cosine_similarity>*
[#](#langchain.document_transformers.EmbeddingsRedundantFilter.similarity_fn "Permalink to this definition") 



 Similarity function for comparing documents. Function expected to take as input
two matrices (List[List[float]]) and return a matrix of scores where higher values
indicate greater similarity.
 






*field*


 similarity_threshold
 

*:
 




 float*
*=
 




 0.95*
[#](#langchain.document_transformers.EmbeddingsRedundantFilter.similarity_threshold "Permalink to this definition") 



 Threshold for determining when two documents are similar enough
to be considered redundant.
 






*async*


 atransform_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


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
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_transformers#EmbeddingsRedundantFilter.atransform_documents)
[#](#langchain.document_transformers.EmbeddingsRedundantFilter.atransform_documents "Permalink to this definition") 



 Asynchronously transform a list of documents.
 








 transform_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


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
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/document_transformers#EmbeddingsRedundantFilter.transform_documents)
[#](#langchain.document_transformers.EmbeddingsRedundantFilter.transform_documents "Permalink to this definition") 



 Filter down documents.
 










 langchain.document_transformers.
 



 get_stateful_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


 [
 


 langchain.schema.Document
 


 ]*

 )
 


 →
 


 Sequence
 


 [
 


 langchain.document_transformers._DocumentWithState
 


 ]
 



[[source]](../../_modules/langchain/document_transformers#get_stateful_documents)
[#](#langchain.document_transformers.get_stateful_documents "Permalink to this definition") 






