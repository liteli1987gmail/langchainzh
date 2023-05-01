




 Embeddings
 [#](#module-langchain.embeddings "Permalink to this headline")
============================================================================



 Wrappers around embedding modules.
 




*pydantic
 

 model*


 langchain.embeddings.
 



 AlephAlphaAsymmetricSemanticEmbedding
 

[[source]](../../_modules/langchain/embeddings/aleph_alpha#AlephAlphaAsymmetricSemanticEmbedding)
[#](#langchain.embeddings.AlephAlphaAsymmetricSemanticEmbedding "Permalink to this definition") 



 Wrapper for Aleph Alpha’s Asymmetric Embeddings
AA provides you with an endpoint to embed a document and a query.
The models were optimized to make the embeddings of documents and
the query for a document as similar as possible.
To learn more, check out:
 <https://docs.aleph-alpha.com/docs/tasks/semantic_embed/>




 Example
 





```
from aleph_alpha import AlephAlphaAsymmetricSemanticEmbedding

embeddings = AlephAlphaSymmetricSemanticEmbedding()

document = "This is a content of the document"
query = "What is the content of the document?"

doc_result = embeddings.embed_documents([document])
query_result = embeddings.embed_query(query)

```





*field*


 compress_to_size
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 128*
[#](#langchain.embeddings.AlephAlphaAsymmetricSemanticEmbedding.compress_to_size "Permalink to this definition") 



 Should the returned embeddings come back as an original 5120-dim vector,
or should it be compressed to 128-dim.
 






*field*


 contextual_control_threshold
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.embeddings.AlephAlphaAsymmetricSemanticEmbedding.contextual_control_threshold "Permalink to this definition") 



 Attention control parameters only apply to those tokens that have
explicitly been set in the request.
 






*field*


 control_log_additive
 

*:
 




 Optional
 


 [
 


 bool
 


 ]*
*=
 




 True*
[#](#langchain.embeddings.AlephAlphaAsymmetricSemanticEmbedding.control_log_additive "Permalink to this definition") 



 Apply controls on prompt items by adding the log(control_factor)
to attention scores.
 






*field*


 hosting
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 'https://api.aleph-alpha.com'*
[#](#langchain.embeddings.AlephAlphaAsymmetricSemanticEmbedding.hosting "Permalink to this definition") 



 Optional parameter that specifies which datacenters may process the request.
 






*field*


 model
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 'luminous-base'*
[#](#langchain.embeddings.AlephAlphaAsymmetricSemanticEmbedding.model "Permalink to this definition") 



 Model name to use.
 






*field*


 normalize
 

*:
 




 Optional
 


 [
 


 bool
 


 ]*
*=
 




 True*
[#](#langchain.embeddings.AlephAlphaAsymmetricSemanticEmbedding.normalize "Permalink to this definition") 



 Should returned embeddings be normalized
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/aleph_alpha#AlephAlphaAsymmetricSemanticEmbedding.embed_documents)
[#](#langchain.embeddings.AlephAlphaAsymmetricSemanticEmbedding.embed_documents "Permalink to this definition") 



 Call out to Aleph Alpha’s asymmetric Document endpoint.
 




 Parameters
 


**texts** 
 – The list of texts to embed.
 




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/aleph_alpha#AlephAlphaAsymmetricSemanticEmbedding.embed_query)
[#](#langchain.embeddings.AlephAlphaAsymmetricSemanticEmbedding.embed_query "Permalink to this definition") 



 Call out to Aleph Alpha’s asymmetric, query embedding endpoint
:param text: The text to embed.
 




 Returns
 


 Embeddings for the text.
 










*pydantic
 

 model*


 langchain.embeddings.
 



 AlephAlphaSymmetricSemanticEmbedding
 

[[source]](../../_modules/langchain/embeddings/aleph_alpha#AlephAlphaSymmetricSemanticEmbedding)
[#](#langchain.embeddings.AlephAlphaSymmetricSemanticEmbedding "Permalink to this definition") 



 The symmetric version of the Aleph Alpha’s semantic embeddings.
 



 The main difference is that here, both the documents and
queries are embedded with a SemanticRepresentation.Symmetric
.. rubric:: Example
 






 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/aleph_alpha#AlephAlphaSymmetricSemanticEmbedding.embed_documents)
[#](#langchain.embeddings.AlephAlphaSymmetricSemanticEmbedding.embed_documents "Permalink to this definition") 



 Call out to Aleph Alpha’s Document endpoint.
 




 Parameters
 


**texts** 
 – The list of texts to embed.
 




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/aleph_alpha#AlephAlphaSymmetricSemanticEmbedding.embed_query)
[#](#langchain.embeddings.AlephAlphaSymmetricSemanticEmbedding.embed_query "Permalink to this definition") 



 Call out to Aleph Alpha’s asymmetric, query embedding endpoint
:param text: The text to embed.
 




 Returns
 


 Embeddings for the text.
 










*pydantic
 

 model*


 langchain.embeddings.
 



 CohereEmbeddings
 

[[source]](../../_modules/langchain/embeddings/cohere#CohereEmbeddings)
[#](#langchain.embeddings.CohereEmbeddings "Permalink to this definition") 



 Wrapper around Cohere embedding models.
 



 To use, you should have the
 `cohere`
 python package installed, and the
environment variable
 `COHERE_API_KEY`
 set with your API key or pass it
as a named parameter to the constructor.
 



 Example
 





```
from langchain.embeddings import CohereEmbeddings
cohere = CohereEmbeddings(model="medium", cohere_api_key="my-api-key")

```





*field*


 model
 

*:
 




 str*
*=
 




 'large'*
[#](#langchain.embeddings.CohereEmbeddings.model "Permalink to this definition") 



 Model name to use.
 






*field*


 truncate
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.embeddings.CohereEmbeddings.truncate "Permalink to this definition") 



 Truncate embeddings that are too long from start or end (“NONE”|”START”|”END”)
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/cohere#CohereEmbeddings.embed_documents)
[#](#langchain.embeddings.CohereEmbeddings.embed_documents "Permalink to this definition") 



 Call out to Cohere’s embedding endpoint.
 




 Parameters
 


**texts** 
 – The list of texts to embed.
 




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/cohere#CohereEmbeddings.embed_query)
[#](#langchain.embeddings.CohereEmbeddings.embed_query "Permalink to this definition") 



 Call out to Cohere’s embedding endpoint.
 




 Parameters
 


**text** 
 – The text to embed.
 




 Returns
 


 Embeddings for the text.
 










*pydantic
 

 model*


 langchain.embeddings.
 



 FakeEmbeddings
 

[[source]](../../_modules/langchain/embeddings/fake#FakeEmbeddings)
[#](#langchain.embeddings.FakeEmbeddings "Permalink to this definition") 






 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/fake#FakeEmbeddings.embed_documents)
[#](#langchain.embeddings.FakeEmbeddings.embed_documents "Permalink to this definition") 



 Embed search docs.
 








 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/fake#FakeEmbeddings.embed_query)
[#](#langchain.embeddings.FakeEmbeddings.embed_query "Permalink to this definition") 



 Embed query text.
 








*pydantic
 

 model*


 langchain.embeddings.
 



 HuggingFaceEmbeddings
 

[[source]](../../_modules/langchain/embeddings/huggingface#HuggingFaceEmbeddings)
[#](#langchain.embeddings.HuggingFaceEmbeddings "Permalink to this definition") 



 Wrapper around sentence_transformers embedding models.
 



 To use, you should have the
 `sentence_transformers`
 python package installed.
 



 Example
 





```
from langchain.embeddings import HuggingFaceEmbeddings

model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
hf = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)

```





*field*


 cache_folder
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.embeddings.HuggingFaceEmbeddings.cache_folder "Permalink to this definition") 



 Path to store models.
Can be also set by SENTENCE_TRANSFORMERS_HOME enviroment variable.
 






*field*


 model_kwargs
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
*[Optional]*
[#](#langchain.embeddings.HuggingFaceEmbeddings.model_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model.
 






*field*


 model_name
 

*:
 




 str*
*=
 




 'sentence-transformers/all-mpnet-base-v2'*
[#](#langchain.embeddings.HuggingFaceEmbeddings.model_name "Permalink to this definition") 



 Model name to use.
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/huggingface#HuggingFaceEmbeddings.embed_documents)
[#](#langchain.embeddings.HuggingFaceEmbeddings.embed_documents "Permalink to this definition") 



 Compute doc embeddings using a HuggingFace transformer model.
 




 Parameters
 


**texts** 
 – The list of texts to embed.
 




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/huggingface#HuggingFaceEmbeddings.embed_query)
[#](#langchain.embeddings.HuggingFaceEmbeddings.embed_query "Permalink to this definition") 



 Compute query embeddings using a HuggingFace transformer model.
 




 Parameters
 


**text** 
 – The text to embed.
 




 Returns
 


 Embeddings for the text.
 










*pydantic
 

 model*


 langchain.embeddings.
 



 HuggingFaceHubEmbeddings
 

[[source]](../../_modules/langchain/embeddings/huggingface_hub#HuggingFaceHubEmbeddings)
[#](#langchain.embeddings.HuggingFaceHubEmbeddings "Permalink to this definition") 



 Wrapper around HuggingFaceHub embedding models.
 



 To use, you should have the
 `huggingface_hub`
 python package installed, and the
environment variable
 `HUGGINGFACEHUB_API_TOKEN`
 set with your API token, or pass
it as a named parameter to the constructor.
 



 Example
 





```
from langchain.embeddings import HuggingFaceHubEmbeddings
repo_id = "sentence-transformers/all-mpnet-base-v2"
hf = HuggingFaceHubEmbeddings(
    repo_id=repo_id,
    task="feature-extraction",
    huggingfacehub_api_token="my-api-key",
)

```





*field*


 model_kwargs
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.embeddings.HuggingFaceHubEmbeddings.model_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model.
 






*field*


 repo_id
 

*:
 




 str*
*=
 




 'sentence-transformers/all-mpnet-base-v2'*
[#](#langchain.embeddings.HuggingFaceHubEmbeddings.repo_id "Permalink to this definition") 



 Model name to use.
 






*field*


 task
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 'feature-extraction'*
[#](#langchain.embeddings.HuggingFaceHubEmbeddings.task "Permalink to this definition") 



 Task to call the model with.
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/huggingface_hub#HuggingFaceHubEmbeddings.embed_documents)
[#](#langchain.embeddings.HuggingFaceHubEmbeddings.embed_documents "Permalink to this definition") 



 Call out to HuggingFaceHub’s embedding endpoint for embedding search docs.
 




 Parameters
 


**texts** 
 – The list of texts to embed.
 




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/huggingface_hub#HuggingFaceHubEmbeddings.embed_query)
[#](#langchain.embeddings.HuggingFaceHubEmbeddings.embed_query "Permalink to this definition") 



 Call out to HuggingFaceHub’s embedding endpoint for embedding query text.
 




 Parameters
 


**text** 
 – The text to embed.
 




 Returns
 


 Embeddings for the text.
 










*pydantic
 

 model*


 langchain.embeddings.
 



 HuggingFaceInstructEmbeddings
 

[[source]](../../_modules/langchain/embeddings/huggingface#HuggingFaceInstructEmbeddings)
[#](#langchain.embeddings.HuggingFaceInstructEmbeddings "Permalink to this definition") 



 Wrapper around sentence_transformers embedding models.
 



 To use, you should have the
 `sentence_transformers`
 and
 `InstructorEmbedding`
 python package installed.
 



 Example
 





```
from langchain.embeddings import HuggingFaceInstructEmbeddings

model_name = "hkunlp/instructor-large"
model_kwargs = {'device': 'cpu'}
hf = HuggingFaceInstructEmbeddings(
    model_name=model_name, model_kwargs=model_kwargs
)

```





*field*


 cache_folder
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.embeddings.HuggingFaceInstructEmbeddings.cache_folder "Permalink to this definition") 



 Path to store models.
Can be also set by SENTENCE_TRANSFORMERS_HOME enviroment variable.
 






*field*


 embed_instruction
 

*:
 




 str*
*=
 




 'Represent
 

 the
 

 document
 

 for
 

 retrieval:
 

 '*
[#](#langchain.embeddings.HuggingFaceInstructEmbeddings.embed_instruction "Permalink to this definition") 



 Instruction to use for embedding documents.
 






*field*


 model_kwargs
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
*[Optional]*
[#](#langchain.embeddings.HuggingFaceInstructEmbeddings.model_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model.
 






*field*


 model_name
 

*:
 




 str*
*=
 




 'hkunlp/instructor-large'*
[#](#langchain.embeddings.HuggingFaceInstructEmbeddings.model_name "Permalink to this definition") 



 Model name to use.
 






*field*


 query_instruction
 

*:
 




 str*
*=
 




 'Represent
 

 the
 

 question
 

 for
 

 retrieving
 

 supporting
 

 documents:
 

 '*
[#](#langchain.embeddings.HuggingFaceInstructEmbeddings.query_instruction "Permalink to this definition") 



 Instruction to use for embedding query.
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/huggingface#HuggingFaceInstructEmbeddings.embed_documents)
[#](#langchain.embeddings.HuggingFaceInstructEmbeddings.embed_documents "Permalink to this definition") 



 Compute doc embeddings using a HuggingFace instruct model.
 




 Parameters
 


**texts** 
 – The list of texts to embed.
 




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/huggingface#HuggingFaceInstructEmbeddings.embed_query)
[#](#langchain.embeddings.HuggingFaceInstructEmbeddings.embed_query "Permalink to this definition") 



 Compute query embeddings using a HuggingFace instruct model.
 




 Parameters
 


**text** 
 – The text to embed.
 




 Returns
 


 Embeddings for the text.
 










*pydantic
 

 model*


 langchain.embeddings.
 



 LlamaCppEmbeddings
 

[[source]](../../_modules/langchain/embeddings/llamacpp#LlamaCppEmbeddings)
[#](#langchain.embeddings.LlamaCppEmbeddings "Permalink to this definition") 



 Wrapper around llama.cpp embedding models.
 



 To use, you should have the llama-cpp-python library installed, and provide the
path to the Llama model as a named parameter to the constructor.
Check out:
 [abetlen/llama-cpp-python](https://github.com/abetlen/llama-cpp-python) 




 Example
 





```
from langchain.embeddings import LlamaCppEmbeddings
llama = LlamaCppEmbeddings(model_path="/path/to/model.bin")

```





*field*


 f16_kv
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.embeddings.LlamaCppEmbeddings.f16_kv "Permalink to this definition") 



 Use half-precision for key/value cache.
 






*field*


 logits_all
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.embeddings.LlamaCppEmbeddings.logits_all "Permalink to this definition") 



 Return logits for all tokens, not just the last token.
 






*field*


 n_batch
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 8*
[#](#langchain.embeddings.LlamaCppEmbeddings.n_batch "Permalink to this definition") 



 Number of tokens to process in parallel.
Should be a number between 1 and n_ctx.
 






*field*


 n_ctx
 

*:
 




 int*
*=
 




 512*
[#](#langchain.embeddings.LlamaCppEmbeddings.n_ctx "Permalink to this definition") 



 Token context window.
 






*field*


 n_parts
 

*:
 




 int*
*=
 




 -1*
[#](#langchain.embeddings.LlamaCppEmbeddings.n_parts "Permalink to this definition") 



 Number of parts to split the model into.
If -1, the number of parts is automatically determined.
 






*field*


 n_threads
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.embeddings.LlamaCppEmbeddings.n_threads "Permalink to this definition") 



 Number of threads to use. If None, the number
of threads is automatically determined.
 






*field*


 seed
 

*:
 




 int*
*=
 




 -1*
[#](#langchain.embeddings.LlamaCppEmbeddings.seed "Permalink to this definition") 



 Seed. If -1, a random seed is used.
 






*field*


 use_mlock
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.embeddings.LlamaCppEmbeddings.use_mlock "Permalink to this definition") 



 Force system to keep model in RAM.
 






*field*


 vocab_only
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.embeddings.LlamaCppEmbeddings.vocab_only "Permalink to this definition") 



 Only load the vocabulary, no weights.
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/llamacpp#LlamaCppEmbeddings.embed_documents)
[#](#langchain.embeddings.LlamaCppEmbeddings.embed_documents "Permalink to this definition") 



 Embed a list of documents using the Llama model.
 




 Parameters
 


**texts** 
 – The list of texts to embed.
 




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/llamacpp#LlamaCppEmbeddings.embed_query)
[#](#langchain.embeddings.LlamaCppEmbeddings.embed_query "Permalink to this definition") 



 Embed a query using the Llama model.
 




 Parameters
 


**text** 
 – The text to embed.
 




 Returns
 


 Embeddings for the text.
 










*pydantic
 

 model*


 langchain.embeddings.
 



 OpenAIEmbeddings
 

[[source]](../../_modules/langchain/embeddings/openai#OpenAIEmbeddings)
[#](#langchain.embeddings.OpenAIEmbeddings "Permalink to this definition") 



 Wrapper around OpenAI embedding models.
 



 To use, you should have the
 `openai`
 python package installed, and the
environment variable
 `OPENAI_API_KEY`
 set with your API key or pass it
as a named parameter to the constructor.
 



 Example
 





```
from langchain.embeddings import OpenAIEmbeddings
openai = OpenAIEmbeddings(openai_api_key="my-api-key")

```




 In order to use the library with Microsoft Azure endpoints, you need to set
the OPENAI_API_TYPE, OPENAI_API_BASE, OPENAI_API_KEY and optionally and
API_VERSION.
The OPENAI_API_TYPE must be set to ‘azure’ and the others correspond to
the properties of your endpoint.
In addition, the deployment name must be passed as the model parameter.
 



 Example
 





```
import os
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_BASE"] = "https://<your-endpoint.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "your AzureOpenAI key"

from langchain.embeddings.openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(
    deployment="your-embeddings-deployment-name",
    model="your-embeddings-model-name"
)
text = "This is a test query."
query_result = embeddings.embed_query(text)

```





*field*


 chunk_size
 

*:
 




 int*
*=
 




 1000*
[#](#langchain.embeddings.OpenAIEmbeddings.chunk_size "Permalink to this definition") 



 Maximum number of texts to embed in each batch
 






*field*


 max_retries
 

*:
 




 int*
*=
 




 6*
[#](#langchain.embeddings.OpenAIEmbeddings.max_retries "Permalink to this definition") 



 Maximum number of retries to make when generating.
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *chunk_size
 



 :
 





 Optional
 


 [
 


 int
 


 ]
 






 =
 





 0*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/openai#OpenAIEmbeddings.embed_documents)
[#](#langchain.embeddings.OpenAIEmbeddings.embed_documents "Permalink to this definition") 



 Call out to OpenAI’s embedding endpoint for embedding search docs.
 




 Parameters
 

* **texts** 
 – The list of texts to embed.
* **chunk_size** 
 – The chunk size of embeddings. If None, will use the chunk size
specified by the class.




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/openai#OpenAIEmbeddings.embed_query)
[#](#langchain.embeddings.OpenAIEmbeddings.embed_query "Permalink to this definition") 



 Call out to OpenAI’s embedding endpoint for embedding query text.
 




 Parameters
 


**text** 
 – The text to embed.
 




 Returns
 


 Embedding for the text.
 










*pydantic
 

 model*


 langchain.embeddings.
 



 SagemakerEndpointEmbeddings
 

[[source]](../../_modules/langchain/embeddings/sagemaker_endpoint#SagemakerEndpointEmbeddings)
[#](#langchain.embeddings.SagemakerEndpointEmbeddings "Permalink to this definition") 



 Wrapper around custom Sagemaker Inference Endpoints.
 



 To use, you must supply the endpoint name from your deployed
Sagemaker model & the region where it is deployed.
 



 To authenticate, the AWS client uses the following methods to
automatically load credentials:
 <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials>




 If a specific credential profile should be used, you must pass
the name of the profile from the ~/.aws/credentials file that is to be used.
 



 Make sure the credentials / roles used have the required policies to
access the Sagemaker endpoint.
See:
 <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies>





*field*


 content_handler
 

*:
 




 langchain.embeddings.sagemaker_endpoint.EmbeddingsContentHandler*
*[Required]*
[#](#langchain.embeddings.SagemakerEndpointEmbeddings.content_handler "Permalink to this definition") 



 The content handler class that provides an input and
output transform functions to handle formats between LLM
and the endpoint.
 






*field*


 credentials_profile_name
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.embeddings.SagemakerEndpointEmbeddings.credentials_profile_name "Permalink to this definition") 



 The name of the profile in the ~/.aws/credentials or ~/.aws/config files, which
has either access keys or role information specified.
If not specified, the default credential profile or, if on an EC2 instance,
credentials from IMDS will be used.
See:
 <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials>







*field*


 endpoint_kwargs
 

*:
 




 Optional
 


 [
 


 Dict
 


 ]*
*=
 




 None*
[#](#langchain.embeddings.SagemakerEndpointEmbeddings.endpoint_kwargs "Permalink to this definition") 



 Optional attributes passed to the invoke_endpoint
function. See
 [`boto3`_](#id1)
 . docs for more info.
.. _boto3: <
 <https://boto3.amazonaws.com/v1/documentation/api/latest/index>
 >
 






*field*


 endpoint_name
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.embeddings.SagemakerEndpointEmbeddings.endpoint_name "Permalink to this definition") 



 The name of the endpoint from the deployed Sagemaker model.
Must be unique within an AWS Region.
 






*field*


 model_kwargs
 

*:
 




 Optional
 


 [
 


 Dict
 


 ]*
*=
 




 None*
[#](#langchain.embeddings.SagemakerEndpointEmbeddings.model_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model.
 






*field*


 region_name
 

*:
 




 str*
*=
 




 ''*
[#](#langchain.embeddings.SagemakerEndpointEmbeddings.region_name "Permalink to this definition") 



 The aws region where the Sagemaker model is deployed, eg.
 
 us-west-2
 
 .
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *chunk_size
 



 :
 





 int
 





 =
 





 64*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/sagemaker_endpoint#SagemakerEndpointEmbeddings.embed_documents)
[#](#langchain.embeddings.SagemakerEndpointEmbeddings.embed_documents "Permalink to this definition") 



 Compute doc embeddings using a SageMaker Inference Endpoint.
 




 Parameters
 

* **texts** 
 – The list of texts to embed.
* **chunk_size** 
 – The chunk size defines how many input texts will
be grouped together as request. If None, will use the
chunk size specified by the class.




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/sagemaker_endpoint#SagemakerEndpointEmbeddings.embed_query)
[#](#langchain.embeddings.SagemakerEndpointEmbeddings.embed_query "Permalink to this definition") 



 Compute query embeddings using a SageMaker inference endpoint.
 




 Parameters
 


**text** 
 – The text to embed.
 




 Returns
 


 Embeddings for the text.
 










*pydantic
 

 model*


 langchain.embeddings.
 



 SelfHostedEmbeddings
 

[[source]](../../_modules/langchain/embeddings/self_hosted#SelfHostedEmbeddings)
[#](#langchain.embeddings.SelfHostedEmbeddings "Permalink to this definition") 



 Runs custom embedding models on self-hosted remote hardware.
 



 Supported hardware includes auto-launched instances on AWS, GCP, Azure,
and Lambda, as well as servers specified
by IP address and SSH credentials (such as on-prem, or another
cloud like Paperspace, Coreweave, etc.).
 



 To use, you should have the
 `runhouse`
 python package installed.
 




 Example using a model load function:
 




```
from langchain.embeddings import SelfHostedEmbeddings
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import runhouse as rh

gpu = rh.cluster(name="rh-a10x", instance_type="A100:1")
def get_pipeline():
    model_id = "facebook/bart-large"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    return pipeline("feature-extraction", model=model, tokenizer=tokenizer)
embeddings = SelfHostedEmbeddings(
    model_load_fn=get_pipeline,
    hardware=gpu
    model_reqs=["./", "torch", "transformers"],
)

```





 Example passing in a pipeline path:
 




```
from langchain.embeddings import SelfHostedHFEmbeddings
import runhouse as rh
from transformers import pipeline

gpu = rh.cluster(name="rh-a10x", instance_type="A100:1")
pipeline = pipeline(model="bert-base-uncased", task="feature-extraction")
rh.blob(pickle.dumps(pipeline),
    path="models/pipeline.pkl").save().to(gpu, path="models")
embeddings = SelfHostedHFEmbeddings.from_pipeline(
    pipeline="models/pipeline.pkl",
    hardware=gpu,
    model_reqs=["./", "torch", "transformers"],
)

```







 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 inference_fn
 

*:
 




 Callable*
*=
 




 <function
 

 _embed_documents>*
[#](#langchain.embeddings.SelfHostedEmbeddings.inference_fn "Permalink to this definition") 



 Inference function to extract the embeddings on the remote hardware.
 






*field*


 inference_kwargs
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.embeddings.SelfHostedEmbeddings.inference_kwargs "Permalink to this definition") 



 Any kwargs to pass to the model’s inference function.
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/self_hosted#SelfHostedEmbeddings.embed_documents)
[#](#langchain.embeddings.SelfHostedEmbeddings.embed_documents "Permalink to this definition") 



 Compute doc embeddings using a HuggingFace transformer model.
 




 Parameters
 


**texts** 
 – The list of texts to embed.s
 




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/self_hosted#SelfHostedEmbeddings.embed_query)
[#](#langchain.embeddings.SelfHostedEmbeddings.embed_query "Permalink to this definition") 



 Compute query embeddings using a HuggingFace transformer model.
 




 Parameters
 


**text** 
 – The text to embed.
 




 Returns
 


 Embeddings for the text.
 










*pydantic
 

 model*


 langchain.embeddings.
 



 SelfHostedHuggingFaceEmbeddings
 

[[source]](../../_modules/langchain/embeddings/self_hosted_hugging_face#SelfHostedHuggingFaceEmbeddings)
[#](#langchain.embeddings.SelfHostedHuggingFaceEmbeddings "Permalink to this definition") 



 Runs sentence_transformers embedding models on self-hosted remote hardware.
 



 Supported hardware includes auto-launched instances on AWS, GCP, Azure,
and Lambda, as well as servers specified
by IP address and SSH credentials (such as on-prem, or another cloud
like Paperspace, Coreweave, etc.).
 



 To use, you should have the
 `runhouse`
 python package installed.
 



 Example
 





```
from langchain.embeddings import SelfHostedHuggingFaceEmbeddings
import runhouse as rh
model_name = "sentence-transformers/all-mpnet-base-v2"
gpu = rh.cluster(name="rh-a10x", instance_type="A100:1")
hf = SelfHostedHuggingFaceEmbeddings(model_name=model_name, hardware=gpu)

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 hardware
 

*:
 




 Any*
*=
 




 None*
[#](#langchain.embeddings.SelfHostedHuggingFaceEmbeddings.hardware "Permalink to this definition") 



 Remote hardware to send the inference function to.
 






*field*


 inference_fn
 

*:
 




 Callable*
*=
 




 <function
 

 _embed_documents>*
[#](#langchain.embeddings.SelfHostedHuggingFaceEmbeddings.inference_fn "Permalink to this definition") 



 Inference function to extract the embeddings.
 






*field*


 load_fn_kwargs
 

*:
 




 Optional
 


 [
 


 dict
 


 ]*
*=
 




 None*
[#](#langchain.embeddings.SelfHostedHuggingFaceEmbeddings.load_fn_kwargs "Permalink to this definition") 



 Key word arguments to pass to the model load function.
 






*field*


 model_id
 

*:
 




 str*
*=
 




 'sentence-transformers/all-mpnet-base-v2'*
[#](#langchain.embeddings.SelfHostedHuggingFaceEmbeddings.model_id "Permalink to this definition") 



 Model name to use.
 






*field*


 model_load_fn
 

*:
 




 Callable*
*=
 




 <function
 

 load_embedding_model>*
[#](#langchain.embeddings.SelfHostedHuggingFaceEmbeddings.model_load_fn "Permalink to this definition") 



 Function to load the model remotely on the server.
 






*field*


 model_reqs
 

*:
 




 List
 


 [
 


 str
 


 ]*
*=
 




 ['./',
 

 'sentence_transformers',
 

 'torch']*
[#](#langchain.embeddings.SelfHostedHuggingFaceEmbeddings.model_reqs "Permalink to this definition") 



 Requirements to install on hardware to inference the model.
 








*pydantic
 

 model*


 langchain.embeddings.
 



 SelfHostedHuggingFaceInstructEmbeddings
 

[[source]](../../_modules/langchain/embeddings/self_hosted_hugging_face#SelfHostedHuggingFaceInstructEmbeddings)
[#](#langchain.embeddings.SelfHostedHuggingFaceInstructEmbeddings "Permalink to this definition") 



 Runs InstructorEmbedding embedding models on self-hosted remote hardware.
 



 Supported hardware includes auto-launched instances on AWS, GCP, Azure,
and Lambda, as well as servers specified
by IP address and SSH credentials (such as on-prem, or another
cloud like Paperspace, Coreweave, etc.).
 



 To use, you should have the
 `runhouse`
 python package installed.
 



 Example
 





```
from langchain.embeddings import SelfHostedHuggingFaceInstructEmbeddings
import runhouse as rh
model_name = "hkunlp/instructor-large"
gpu = rh.cluster(name='rh-a10x', instance_type='A100:1')
hf = SelfHostedHuggingFaceInstructEmbeddings(
    model_name=model_name, hardware=gpu)

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 embed_instruction
 

*:
 




 str*
*=
 




 'Represent
 

 the
 

 document
 

 for
 

 retrieval:
 

 '*
[#](#langchain.embeddings.SelfHostedHuggingFaceInstructEmbeddings.embed_instruction "Permalink to this definition") 



 Instruction to use for embedding documents.
 






*field*


 model_id
 

*:
 




 str*
*=
 




 'hkunlp/instructor-large'*
[#](#langchain.embeddings.SelfHostedHuggingFaceInstructEmbeddings.model_id "Permalink to this definition") 



 Model name to use.
 






*field*


 model_reqs
 

*:
 




 List
 


 [
 


 str
 


 ]*
*=
 




 ['./',
 

 'InstructorEmbedding',
 

 'torch']*
[#](#langchain.embeddings.SelfHostedHuggingFaceInstructEmbeddings.model_reqs "Permalink to this definition") 



 Requirements to install on hardware to inference the model.
 






*field*


 query_instruction
 

*:
 




 str*
*=
 




 'Represent
 

 the
 

 question
 

 for
 

 retrieving
 

 supporting
 

 documents:
 

 '*
[#](#langchain.embeddings.SelfHostedHuggingFaceInstructEmbeddings.query_instruction "Permalink to this definition") 



 Instruction to use for embedding query.
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/self_hosted_hugging_face#SelfHostedHuggingFaceInstructEmbeddings.embed_documents)
[#](#langchain.embeddings.SelfHostedHuggingFaceInstructEmbeddings.embed_documents "Permalink to this definition") 



 Compute doc embeddings using a HuggingFace instruct model.
 




 Parameters
 


**texts** 
 – The list of texts to embed.
 




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/self_hosted_hugging_face#SelfHostedHuggingFaceInstructEmbeddings.embed_query)
[#](#langchain.embeddings.SelfHostedHuggingFaceInstructEmbeddings.embed_query "Permalink to this definition") 



 Compute query embeddings using a HuggingFace instruct model.
 




 Parameters
 


**text** 
 – The text to embed.
 




 Returns
 


 Embeddings for the text.
 












 langchain.embeddings.
 



 SentenceTransformerEmbeddings
 

[#](#langchain.embeddings.SentenceTransformerEmbeddings "Permalink to this definition") 



 alias of
 [`langchain.embeddings.huggingface.HuggingFaceEmbeddings`](#langchain.embeddings.HuggingFaceEmbeddings "langchain.embeddings.huggingface.HuggingFaceEmbeddings")







*pydantic
 

 model*


 langchain.embeddings.
 



 TensorflowHubEmbeddings
 

[[source]](../../_modules/langchain/embeddings/tensorflow_hub#TensorflowHubEmbeddings)
[#](#langchain.embeddings.TensorflowHubEmbeddings "Permalink to this definition") 



 Wrapper around tensorflow_hub embedding models.
 



 To use, you should have the
 `tensorflow_text`
 python package installed.
 



 Example
 





```
from langchain.embeddings import TensorflowHubEmbeddings
url = "https://tfhub.dev/google/universal-sentence-encoder-multilingual/3"
tf = TensorflowHubEmbeddings(model_url=url)

```





*field*


 model_url
 

*:
 




 str*
*=
 




 'https://tfhub.dev/google/universal-sentence-encoder-multilingual/3'*
[#](#langchain.embeddings.TensorflowHubEmbeddings.model_url "Permalink to this definition") 



 Model name to use.
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/embeddings/tensorflow_hub#TensorflowHubEmbeddings.embed_documents)
[#](#langchain.embeddings.TensorflowHubEmbeddings.embed_documents "Permalink to this definition") 



 Compute doc embeddings using a TensorflowHub embedding model.
 




 Parameters
 


**texts** 
 – The list of texts to embed.
 




 Returns
 


 List of embeddings, one for each text.
 










 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/embeddings/tensorflow_hub#TensorflowHubEmbeddings.embed_query)
[#](#langchain.embeddings.TensorflowHubEmbeddings.embed_query "Permalink to this definition") 



 Compute query embeddings using a TensorflowHub embedding model.
 




 Parameters
 


**text** 
 – The text to embed.
 




 Returns
 


 Embeddings for the text.
 










