


 AtlasDB
 [#](#atlasdb "Permalink to this headline")
=====================================================



 This notebook shows you how to use functionality related to the
 `AtlasDB`
 .
 



> 
> 
> 
> [MongoDB‘s](https://www.mongodb.com/) 
> [Atlas](https://www.mongodb.com/cloud/atlas) 
>  is an on-demand fully managed service.
>  `MongoDB
>  
> 
>  Atlas`
>  runs on
>  `AWS`
>  ,
>  `Microsoft
>  
> 
>  Azure`
>  , and
>  `Google
>  
> 
>  Cloud
>  
> 
>  Platform`
>  .
>  
> 
> 
> 
> 







```
!pip install spacy

```










```
!python3 -m spacy download en_core_web_sm

```










```
!pip install nomic

```










```
import time
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import AtlasDB
from langchain.document_loaders import TextLoader

```










```
ATLAS_TEST_API_KEY = '7xDPkYXSYDc1_ErdTPIcoAR9RNd8YDlkS3nVNXcVoIMZ6'

```










```
loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = SpacyTextSplitter(separator='|')
texts = []
for doc in text_splitter.split_documents(documents):
    texts.extend(doc.page_content.split('|'))
                 
texts = [e.strip() for e in texts]

```










```
db = AtlasDB.from_texts(texts=texts,
                        name='test_index_'+str(time.time()), # unique name for your vector store
                        description='test_index', #a description for your vector store
                        api_key=ATLAS_TEST_API_KEY,
                        index_kwargs={'build_topic_model': True})

```










```
db.project.wait_for_project_lock()

```










```
db.project

```






**[test_index_1677255228.136989](https://atlas.nomic.ai/dashboard/project/ee2354a3-7f9a-4c6b-af43-b0cda09d7198)**
  

 A description for your project 508 datums inserted.
   

 1 index built.
   

**Projections** 
* test_index_1677255228.136989_index. Status Completed.
 [view online](https://atlas.nomic.ai/map/ee2354a3-7f9a-4c6b-af43-b0cda09d7198/db996d77-8981-48a0-897a-ff2c22bbf541)




---



 destroy = function() {
 document.getElementById("iframedb996d77-8981-48a0-897a-ff2c22bbf541").remove()
 }
 
#### 
 Projection ID: db996d77-8981-48a0-897a-ff2c22bbf541




 Hide embedded project
 

[Explore on atlas.nomic.ai](https://atlas.nomic.ai/map/ee2354a3-7f9a-4c6b-af43-b0cda09d7198/db996d77-8981-48a0-897a-ff2c22bbf541) 





 .iframe {
 /\* vh can be \*\*very\*\* large in vscode ipynb. \*/
 height: min(75vh, 66vw);
 width: 100%;
 }
 

 .actions {
 display: block;
 }
 .action {
 min-height: 18px;
 margin: 5px;
 transition: all 500ms ease-in-out;
 }
 .action:hover {
 cursor: pointer;
 }
 #hide:hover::after {
 content: " X";
 }
 #out:hover::after {
 content: "";
 }
 





