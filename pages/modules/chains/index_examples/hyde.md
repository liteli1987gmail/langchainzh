HyDE
=============

本笔记介绍如何使用假设性文档嵌入（HyDE），如[本文](https://arxiv.org/abs/2212.10496)所述。

在高层次上，HyDE是一种嵌入技术，它接收查询，生成假设的答案，然后嵌入生成的文档，并将其用作最终示例。

为了使用HyDE，因此我们需要提供一个基本嵌入模型，以及一个可以用于生成这些文档的LLMChain。默认情况下，HyDE类带有一些默认提示（有关详细信息，请参见本文），但我们也可以创建自己的提示。

```
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import LLMChain, HypotheticalDocumentEmbedder
from langchain.prompts import PromptTemplate

```

```
base_embeddings = OpenAIEmbeddings()
llm = OpenAI()

```

```
# Load with `web_search` prompt
embeddings = HypotheticalDocumentEmbedder.from_llm(llm, base_embeddings, "web_search")

```

```
# Now we can use it as any embedding class!
result = embeddings.embed_query("Where is the Taj Mahal?")

```

多次生成[#](#multiple-generations "本标题的永久链接")
-----------------------------------------

我们也可以生成多个文档，然后组合这些文档的嵌入。默认情况下，我们通过取平均值来组合这些文档。我们可以通过更改用于生成文档的LLM来实现此目的，从而返回多个内容。

```
multi_llm = OpenAI(n=4, best_of=4)

```

```
embeddings = HypotheticalDocumentEmbedder.from_llm(multi_llm, base_embeddings, "web_search")

```

```
result = embeddings.embed_query("Where is the Taj Mahal?")

```

使用自己的提示[#](#using-our-own-prompts "本标题的永久链接")
---------------------------------------------

Besides using preconfigured prompts, we can also easily construct our own prompts and use those in the LLMChain that is generating the documents. This can be useful if we know the domain our queries will be in, as we can condition the prompt to generate text more similar to that.

In the example below, let’s condition it to generate text about a state of the union address (because we will use that in the next example).

```
prompt_template = """Please answer the user's question about the most recent state of the union address
Question: {question}
Answer:"""
prompt = PromptTemplate(input_variables=["question"], template=prompt_template)
llm_chain = LLMChain(llm=llm, prompt=prompt)

```

```
embeddings = HypotheticalDocumentEmbedder(llm_chain=llm_chain, base_embeddings=base_embeddings)

```

```
result = embeddings.embed_query("What did the president say about Ketanji Brown Jackson")

```

Using HyDE[#](#using-hyde "Permalink to this headline")
-------------------------------------------------------

Now that we have HyDE, we can use it as we would any other embedding class! Here is using it to find similar passages in the state of the union example.

```
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

with open("../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(state_of_the_union)

```

```
docsearch = Chroma.from_texts(texts, embeddings)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)

```

```
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.

```

```
print(docs[0].page_content)

```

```
In state after state, new laws have been passed, not only to suppress the vote, but to subvert entire elections. 

We cannot let this happen. 

Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```

