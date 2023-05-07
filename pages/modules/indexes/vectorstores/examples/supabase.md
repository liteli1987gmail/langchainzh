
Supabase
===


> 
> [Supabase](https://supabase.com/docs)是一种开源的Firebase替代方案。
> 
> 
> 

这个笔记本展示了如何使用`Supabase`和`pgvector`作为你的VectorStore。

运行这个笔记本，请确保：

* `pgvector`扩展已启用

* 你已经安装了`supabase-py`包

* 你已经在你的数据库中创建了一个`match_documents`函数

* 你的`public`模式中存在一个类似下面的`documents`表。

The following function determines cosine similarity, but you can adjust to your needs.

```
       -- Enable the pgvector extension to work with embedding vectors
       create extension vector;

       -- Create a table to store your documents
       create table documents (
       id bigserial primary key,
       content text, -- corresponds to Document.pageContent
       metadata jsonb, -- corresponds to Document.metadata
       embedding vector(1536) -- 1536 works for OpenAI embeddings, change if needed
       );

       CREATE FUNCTION match_documents(query_embedding vector(1536), match_count int)
           RETURNS TABLE(
               id bigint,
               content text,
               metadata jsonb,
               -- we return matched vectors to enable maximal marginal relevance searches
               embedding vector(1536),
               similarity float)
           LANGUAGE plpgsql
           AS $$
           # variable_conflict use_column
       BEGIN
           RETURN query
           SELECT
               id,
               content,
               metadata,
               embedding,
               1 -(documents.embedding <=> query_embedding) AS similarity
           FROM
               documents
           ORDER BY
               documents.embedding <=> query_embedding
           LIMIT match_count;
       END;
       $$;

```

```
# with pip
!pip install supabase

# with conda
# !conda install -c conda-forge supabase

```

We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

```
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

```

```
os.environ['SUPABASE_URL'] = getpass.getpass('Supabase URL:')

```

```
os.environ['SUPABASE_SERVICE_KEY'] = getpass.getpass('Supabase Service Key:')

```

```
# If you're storing your Supabase and OpenAI API keys in a .env file, you can load them with dotenv
from dotenv import load_dotenv

load_dotenv()

```

```
True

```

```
import os
from supabase.client import Client, create_client

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_SERVICE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

```

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import SupabaseVectorStore
from langchain.document_loaders import TextLoader

```

```
2023-04-19 20:12:28,593:INFO - NumExpr defaulting to 8 threads.

```

```
from langchain.document_loaders import TextLoader

loader = TextLoader("../../../state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

```

```
# We're using the default `documents` table here. You can modify this by passing in a `table_name` argument to the `from_documents` method.
vector_store = SupabaseVectorStore.from_documents(
    docs, embeddings, client=supabase
)

```

```
query = "What did the president say about Ketanji Brown Jackson"
matched_docs = vector_store.similarity_search(query)

```

```
print(matched_docs[0].page_content)

```

```
Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

```

Similarity search with score[#](#similarity-search-with-score "Permalink to this headline")
-------------------------------------------------------------------------------------------

```
matched_docs = vector_store.similarity_search_with_relevance_scores(query)

```

```
matched_docs[0]

```

```
(Document(page_content='Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', metadata={'source': '../../../state_of_the_union.txt'}),
 0.802509746274066)

```

Retriever options[#](#retriever-options "Permalink to this headline")
---------------------------------------------------------------------

This section goes over different options for how to use SupabaseVectorStore as a retriever.

### Maximal Marginal Relevance Searches[#](#maximal-marginal-relevance-searches "Permalink to this headline")

In addition to using similarity search in the retriever object, you can also use `mmr`.

```
retriever = vector_store.as_retriever(search_type="mmr")

```

```
matched_docs = retriever.get_relevant_documents(query)

```

```
for i, d in enumerate(matched_docs):
    print(f"\n## Document {i}\n")
    print(d.page_content)

```

```
## Document 0

Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. 

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. 

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. 

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

## Document 1

One was stationed at bases and breathing in toxic smoke from “burn pits” that incinerated wastes of war—medical and hazard material, jet fuel, and more. 

When they came home, many of the world’s fittest and best trained warriors were never the same. 

Headaches. Numbness. Dizziness. 

A cancer that would put them in a flag-draped coffin. 

I know. 

One of those soldiers was my son Major Beau Biden. 

We don’t know for sure if a burn pit was the cause of his brain cancer, or the diseases of so many of our troops. 

But I’m committed to finding out everything we can. 

Committed to military families like Danielle Robinson from Ohio. 

The widow of Sergeant First Class Heath Robinson.  

He was born a soldier. Army National Guard. Combat medic in Kosovo and Iraq. 

Stationed near Baghdad, just yards from burn pits the size of football fields. 

Heath’s widow Danielle is here with us tonight. They loved going to Ohio State football games. He loved building Legos with their daughter.

## Document 2

And I’m taking robust action to make sure the pain of our sanctions  is targeted at Russia’s economy. And I will use every tool at our disposal to protect American businesses and consumers. 

Tonight, I can announce that the United States has worked with 30 other countries to release 60 Million barrels of oil from reserves around the world.  

America will lead that effort, releasing 30 Million barrels from our own Strategic Petroleum Reserve. And we stand ready to do more if necessary, unified with our allies.  

These steps will help blunt gas prices here at home. And I know the news about what’s happening can seem alarming. 

But I want you to know that we are going to be okay. 

When the history of this era is written Putin’s war on Ukraine will have left Russia weaker and the rest of the world stronger. 

While it shouldn’t have taken something so terrible for people around the world to see what’s at stake now everyone sees it clearly.

## Document 3

We can’t change how divided we’ve been. But we can change how we move forward—on COVID-19 and other issues we must face together. 

I recently visited the New York City Police Department days after the funerals of Officer Wilbert Mora and his partner, Officer Jason Rivera. 

They were responding to a 9-1-1 call when a man shot and killed them with a stolen gun. 

Officer Mora was 27 years old. 

Officer Rivera was 22. 

Both Dominican Americans who’d grown up on the same streets they later chose to patrol as police officers. 

I spoke with their families and told them that we are forever in debt for their sacrifice, and we will carry on their mission to restore the trust and safety every community deserves. 

I’ve worked on these issues a long time. 

I know what works: Investing in crime preventionand community police officers who’ll walk the beat, who’ll know the neighborhood, and who can restore trust and safety.

```

