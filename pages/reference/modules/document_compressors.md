




 Document Compressors
 [#](#module-langchain.retrievers.document_compressors "Permalink to this headline")
===========================================================================================================




*pydantic
 

 model*


 langchain.retrievers.document_compressors.
 



 DocumentCompressorPipeline
 

[[source]](../../_modules/langchain/retrievers/document_compressors/base#DocumentCompressorPipeline)
[#](#langchain.retrievers.document_compressors.DocumentCompressorPipeline "Permalink to this definition") 



 Document compressor that uses a pipeline of transformers.
 




*field*


 transformers
 

*:
 




 List
 


 [
 


 Union
 


 [
 


 langchain.schema.BaseDocumentTransformer
 


 ,
 




 langchain.retrievers.document_compressors.base.BaseDocumentCompressor
 


 ]
 



 ]*
*[Required]*
[#](#langchain.retrievers.document_compressors.DocumentCompressorPipeline.transformers "Permalink to this definition") 



 List of document filters that are chained together and run in sequence.
 






*async*


 acompress_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *query
 



 :
 





 str*

 )
 


 →
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/document_compressors/base#DocumentCompressorPipeline.acompress_documents)
[#](#langchain.retrievers.document_compressors.DocumentCompressorPipeline.acompress_documents "Permalink to this definition") 



 Compress retrieved documents given the query context.
 








 compress_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *query
 



 :
 





 str*

 )
 


 →
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/document_compressors/base#DocumentCompressorPipeline.compress_documents)
[#](#langchain.retrievers.document_compressors.DocumentCompressorPipeline.compress_documents "Permalink to this definition") 



 Transform a list of documents.
 








*pydantic
 

 model*


 langchain.retrievers.document_compressors.
 



 EmbeddingsFilter
 

[[source]](../../_modules/langchain/retrievers/document_compressors/embeddings_filter#EmbeddingsFilter)
[#](#langchain.retrievers.document_compressors.EmbeddingsFilter "Permalink to this definition") 




*field*


 embeddings
 

*:
 




 langchain.embeddings.base.Embeddings*
*[Required]*
[#](#langchain.retrievers.document_compressors.EmbeddingsFilter.embeddings "Permalink to this definition") 



 Embeddings to use for embedding document contents and queries.
 






*field*


 k
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 20*
[#](#langchain.retrievers.document_compressors.EmbeddingsFilter.k "Permalink to this definition") 



 The number of relevant documents to return. Can be set to None, in which case
 
 similarity_threshold
 
 must be specified. Defaults to 20.
 






*field*


 similarity_fn
 

*:
 




 Callable*
*=
 




 <function
 

 cosine_similarity>*
[#](#langchain.retrievers.document_compressors.EmbeddingsFilter.similarity_fn "Permalink to this definition") 



 Similarity function for comparing documents. Function expected to take as input
two matrices (List[List[float]]) and return a matrix of scores where higher values
indicate greater similarity.
 






*field*


 similarity_threshold
 

*:
 




 Optional
 


 [
 


 float
 


 ]*
*=
 




 None*
[#](#langchain.retrievers.document_compressors.EmbeddingsFilter.similarity_threshold "Permalink to this definition") 



 Threshold for determining when two documents are similar enough
to be considered redundant. Defaults to None, must be specified if
 
 k
 
 is set
to None.
 






*async*


 acompress_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *query
 



 :
 





 str*

 )
 


 →
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/document_compressors/embeddings_filter#EmbeddingsFilter.acompress_documents)
[#](#langchain.retrievers.document_compressors.EmbeddingsFilter.acompress_documents "Permalink to this definition") 



 Filter down documents.
 








 compress_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *query
 



 :
 





 str*

 )
 


 →
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/document_compressors/embeddings_filter#EmbeddingsFilter.compress_documents)
[#](#langchain.retrievers.document_compressors.EmbeddingsFilter.compress_documents "Permalink to this definition") 



 Filter documents based on similarity of their embeddings to the query.
 








*pydantic
 

 model*


 langchain.retrievers.document_compressors.
 



 LLMChainExtractor
 

[[source]](../../_modules/langchain/retrievers/document_compressors/chain_extract#LLMChainExtractor)
[#](#langchain.retrievers.document_compressors.LLMChainExtractor "Permalink to this definition") 




*field*


 get_input
 

*:
 




 Callable
 


 [
 



 [
 


 str
 


 ,
 




 langchain.schema.Document
 


 ]
 



 ,
 




 dict
 


 ]*
*=
 




 <function
 

 default_get_input>*
[#](#langchain.retrievers.document_compressors.LLMChainExtractor.get_input "Permalink to this definition") 



 Callable for constructing the chain input from the query and a Document.
 






*field*


 llm_chain
 

*:
 



[langchain.chains.llm.LLMChain](chains#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
*[Required]*
[#](#langchain.retrievers.document_compressors.LLMChainExtractor.llm_chain "Permalink to this definition") 



 LLM wrapper to use for compressing documents.
 






*async*


 acompress_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *query
 



 :
 





 str*

 )
 


 →
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/document_compressors/chain_extract#LLMChainExtractor.acompress_documents)
[#](#langchain.retrievers.document_compressors.LLMChainExtractor.acompress_documents "Permalink to this definition") 



 Compress retrieved documents given the query context.
 








 compress_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *query
 



 :
 





 str*

 )
 


 →
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/document_compressors/chain_extract#LLMChainExtractor.compress_documents)
[#](#langchain.retrievers.document_compressors.LLMChainExtractor.compress_documents "Permalink to this definition") 



 Compress page content of raw documents.
 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *prompt
 



 :
 





 Optional
 


 [
 

[langchain.prompts.prompt.PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")


 ]
 






 =
 





 None*
 ,
 *get_input
 



 :
 





 Optional
 


 [
 


 Callable
 


 [
 



 [
 


 str
 


 ,
 




 langchain.schema.Document
 


 ]
 



 ,
 




 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *llm_chain_kwargs
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*

 )
 


 →
 

[langchain.retrievers.document_compressors.chain_extract.LLMChainExtractor](#langchain.retrievers.document_compressors.LLMChainExtractor "langchain.retrievers.document_compressors.chain_extract.LLMChainExtractor")


[[source]](../../_modules/langchain/retrievers/document_compressors/chain_extract#LLMChainExtractor.from_llm)
[#](#langchain.retrievers.document_compressors.LLMChainExtractor.from_llm "Permalink to this definition") 



 Initialize from LLM.
 








*pydantic
 

 model*


 langchain.retrievers.document_compressors.
 



 LLMChainFilter
 

[[source]](../../_modules/langchain/retrievers/document_compressors/chain_filter#LLMChainFilter)
[#](#langchain.retrievers.document_compressors.LLMChainFilter "Permalink to this definition") 



 Filter that drops documents that aren’t relevant to the query.
 




*field*


 get_input
 

*:
 




 Callable
 


 [
 



 [
 


 str
 


 ,
 




 langchain.schema.Document
 


 ]
 



 ,
 




 dict
 


 ]*
*=
 




 <function
 

 default_get_input>*
[#](#langchain.retrievers.document_compressors.LLMChainFilter.get_input "Permalink to this definition") 



 Callable for constructing the chain input from the query and a Document.
 






*field*


 llm_chain
 

*:
 



[langchain.chains.llm.LLMChain](chains#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
*[Required]*
[#](#langchain.retrievers.document_compressors.LLMChainFilter.llm_chain "Permalink to this definition") 



 LLM wrapper to use for filtering documents.
The chain prompt is expected to have a BooleanOutputParser.
 






*async*


 acompress_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *query
 



 :
 





 str*

 )
 


 →
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/document_compressors/chain_filter#LLMChainFilter.acompress_documents)
[#](#langchain.retrievers.document_compressors.LLMChainFilter.acompress_documents "Permalink to this definition") 



 Filter down documents.
 








 compress_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *query
 



 :
 





 str*

 )
 


 →
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/retrievers/document_compressors/chain_filter#LLMChainFilter.compress_documents)
[#](#langchain.retrievers.document_compressors.LLMChainFilter.compress_documents "Permalink to this definition") 



 Filter down documents based on their relevance to the query.
 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *prompt
 



 :
 





 Optional
 


 [
 

[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")


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
 

[langchain.retrievers.document_compressors.chain_filter.LLMChainFilter](#langchain.retrievers.document_compressors.LLMChainFilter "langchain.retrievers.document_compressors.chain_filter.LLMChainFilter")


[[source]](../../_modules/langchain/retrievers/document_compressors/chain_filter#LLMChainFilter.from_llm)
[#](#langchain.retrievers.document_compressors.LLMChainFilter.from_llm "Permalink to this definition") 








