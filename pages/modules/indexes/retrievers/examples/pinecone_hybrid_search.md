


 Pinecone Hybrid Search
 [#](#pinecone-hybrid-search "Permalink to this headline")
===================================================================================



 This notebook goes over how to use a retriever that under the hood uses Pinecone and Hybrid Search.
 



 The logic of this retriever is taken from
 [this documentaion](https://docs.pinecone.io/docs/hybrid-search) 








```
from langchain.retrievers import PineconeHybridSearchRetriever

```







 Setup Pinecone
 [#](#setup-pinecone "Permalink to this headline")
-------------------------------------------------------------------



 You should only have to do this part once.
 



 Note: it’s important to make sure that the “context” field that holds the document text in the metadata is not indexed. Currently you need to specify explicitly the fields you do want to index. For more information checkout Pinecone’s
 [docs](https://docs.pinecone.io/docs/manage-indexes#selective-metadata-indexing) 
 .
 







```
import os
import pinecone

api_key = os.getenv("PINECONE_API_KEY") or "PINECONE_API_KEY"
# find environment next to your API key in the Pinecone console
env = os.getenv("PINECONE_ENVIRONMENT") or "PINECONE_ENVIRONMENT"

index_name = "langchain-pinecone-hybrid-search"

pinecone.init(api_key=api_key, enviroment=env)
pinecone.whoami()

```








```
WhoAmIResponse(username='load', user_label='label', projectname='load-test')

```










```
 # create the index
pinecone.create_index(
   name = index_name,
   dimension = 1536,  # dimensionality of dense model
   metric = "dotproduct",  # sparse values supported only for dotproduct
   pod_type = "s1",
   metadata_config={"indexed": []}  # see explaination above
)

```






 Now that its created, we can use it
 







```
index = pinecone.Index(index_name)

```








 Get embeddings and sparse encoders
 [#](#get-embeddings-and-sparse-encoders "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------



 Embeddings are used for the dense vectors, tokenizer is used for the sparse vector
 







```
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

```






 To encode the text to sparse values you can either choose SPLADE or BM25. For out of domain tasks we recommend using BM25.
 



 For more information about the sparse encoders you can checkout pinecone-text library
 [docs](https://pinecone-io.github.io/pinecone-text/pinecone_text) 
 .
 







```
from pinecone_text.sparse import BM25Encoder
# or from pinecone_text.sparse import SpladeEncoder if you wish to work with SPLADE

# use default tf-idf values
bm25_encoder = BM25Encoder().default()

```






 The above code is using default tfids values. It’s highly recommended to fit the tf-idf values to your own corpus. You can do it as follow:
 





```
corpus = ["foo", "bar", "world", "hello"]

# fit tf-idf values on your corpus
bm25_encoder.fit(corpus)

# store the values to a json file
bm25_encoder.dump("bm25_values.json")

# load to your BM25Encoder object
bm25_encoder = BM25Encoder().load("bm25_values.json")

```






 Load Retriever
 [#](#load-retriever "Permalink to this headline")
-------------------------------------------------------------------



 We can now construct the retriever!
 







```
retriever = PineconeHybridSearchRetriever(embeddings=embeddings, sparse_encoder=bm25_encoder, index=index)

```








 Add texts (if necessary)
 [#](#add-texts-if-necessary "Permalink to this headline")
-------------------------------------------------------------------------------------



 We can optionally add texts to the retriever (if they aren’t already in there)
 







```
retriever.add_texts(["foo", "bar", "world", "hello"])

```








```
100%|██████████| 1/1 [00:02<00:00,  2.27s/it]

```








 Use Retriever
 [#](#use-retriever "Permalink to this headline")
-----------------------------------------------------------------



 We can now use the retriever!
 







```
result = retriever.get_relevant_documents("foo")

```










```
result[0]

```








```
Document(page_content='foo', metadata={})

```








