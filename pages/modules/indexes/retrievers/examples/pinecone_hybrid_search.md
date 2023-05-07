如何使用一个检索器
===

本文档介绍了如何使用一个检索器，该检索器在幕后使用松果和混合搜索。

这个检索器的逻辑来自于[此文档](https://docs.pinecone.io/docs/hybrid-search)

```
from langchain.retrievers import PineconeHybridSearchRetriever

```

设置松果[#](#setup-pinecone "到这个标题的永久链接")
-------------------------------------

您只需要执行这一步。

注意：重要的是确保在元数据中保存文档文本的“上下文”字段未被索引。目前，您需要明确指定要索引的字段。有关更多信息，请查看松果的[文档](https://docs.pinecone.io/docs/manage-indexes#selective-metadata-indexing)。

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

现在创建完成了，我们可以使用它了

```
index = pinecone.Index(index_name)

```

获取嵌入和稀疏编码器[#](#get-embeddings-and-sparse-encoders "到这个标题的永久链接")
---------------------------------------------------------------

嵌入用于密集向量，令牌化器用于稀疏向量

```
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

```

To encode the text to sparse values you can either choose SPLADE or BM25. For out of domain tasks we recommend using BM25.

For more information about the sparse encoders you can checkout pinecone-text library [docs](https://pinecone-io.github.io/pinecone-text/pinecone_text）.

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

Load Retriever[#](#load-retriever "Permalink to this headline")
---------------------------------------------------------------

We can now construct the retriever!

```
retriever = PineconeHybridSearchRetriever(embeddings=embeddings, sparse_encoder=bm25_encoder, index=index)

```

Add texts (if necessary)[#](#add-texts-if-necessary "Permalink to this headline")
---------------------------------------------------------------------------------

We can optionally add texts to the retriever (if they aren’t already in there)

```
retriever.add_texts(["foo", "bar", "world", "hello"])

```

```
100%|██████████| 1/1 [00:02<00:00,  2.27s/it]

```

Use Retriever[#](#use-retriever "Permalink to this headline")
-------------------------------------------------------------

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

