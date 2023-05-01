


 Weaviate
 [#](#weaviate "Permalink to this headline")
=======================================================



> 
> 
> 
> [Weaviate](https://weaviate.io/) 
>  is an open-source vector database. It allows you to store data objects and vector embeddings from your favorite ML-models, and scale seamlessly into billions of data objects.
>  
> 
> 
> 
> 



 This notebook shows how to use functionality related to the
 `Weaviate`
 vector database.
 



 See the
 `Weaviate`
[installation instructions](https://weaviate.io/developers/weaviate/installation) 
 .
 







```
!pip install weaviate-client

```






 We want to use
 `OpenAIEmbeddings`
 so we have to get the OpenAI API Key.
 







```
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

```










```
WEAVIATE_URL = getpass.getpass('WEAVIATE_URL:')

```










```
os.environ['WEAVIATE_API_KEY'] = getpass.getpass('WEAVIATE_API_KEY:')

```










```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Weaviate
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
import weaviate
import os

WEAVIATE_URL = ""
client = weaviate.Client(
    url=WEAVIATE_URL,
    additional_headers={
        'X-OpenAI-Api-Key': os.environ["OPENAI_API_KEY"]
    }
)

```










```
client.schema.delete_all()
client.schema.get()
schema = {
    "classes": [
        {
            "class": "Paragraph",
            "description": "A written paragraph",
            "vectorizer": "text2vec-openai",
              "moduleConfig": {
                "text2vec-openai": {
                  "model": "ada",
                  "modelVersion": "002",
                  "type": "text"
                }
              },
            "properties": [
                {
                    "dataType": ["text"],
                    "description": "The content of the paragraph",
                    "moduleConfig": {
                        "text2vec-openai": {
                          "skip": False,
                          "vectorizePropertyName": False
                        }
                      },
                    "name": "content",
                },
            ],
        },
    ]
}

client.schema.create(schema)

```










```
vectorstore = Weaviate(client, "Paragraph", "content")

```










```
query = "What did the president say about Ketanji Brown Jackson"
docs = vectorstore.similarity_search(query)

```










```
print(docs[0].page_content)

```







