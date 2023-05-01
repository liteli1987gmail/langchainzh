


 Zilliz
 [#](#zilliz "Permalink to this headline")
===================================================



> 
> 
> 
> [Zilliz Cloud](https://zilliz.com/doc/quick_start) 
>  is a fully managed service on cloud for
>  `LF
>  
> 
>  AI
>  
> 
>  Milvus®`
>  ,
>  
> 
> 
> 
> 



 This notebook shows how to use functionality related to the Zilliz Cloud managed vector database.
 



 To run, you should have a
 `Zilliz
 

 Cloud`
 instance up and running. Here are the
 [installation instructions](https://zilliz.com/cloud) 








```
!pip install pymilvus

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
# replace 
ZILLIZ_CLOUD_URI = "" # example: "https://in01-17f69c292d4a5sa.aws-us-west-2.vectordb.zillizcloud.com:19536"
ZILLIZ_CLOUD_USERNAME = ""  # example: "username"
ZILLIZ_CLOUD_PASSWORD = ""  # example: "\*\*\*\*\*\*\*\*\*"

```










```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Milvus
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
vector_db = Milvus.from_documents(
    docs,
    embeddings,
    connection_args={
        "uri": ZILLIZ_CLOUD_URI,
        "username": ZILLIZ_CLOUD_USERNAME,
        "password": ZILLIZ_CLOUD_PASSWORD,
        "secure": True
    }
)

```










```
docs = vector_db.similarity_search(query)

```










```
docs[0]

```







