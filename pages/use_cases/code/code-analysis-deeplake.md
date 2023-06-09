

使用LangChain， GPT和Deep Lake 数据库，处理代码库[#](#use-langchain-gpt-and-deep-lake-to-work-with-code-base "标题的永久链接")
========================


在本教程中，我们将使用Langchain + Deep Lake和GPT，分析LangChain本身的代码库。



设计[#](#design "标题的永久链接")
-------------------


1. 准备数据:


- 1. 使用`langchain.document_loaders.TextLoader`上传所有Python项目文件。 我们将这些文件称为**文档**。
- 2. 使用`langchain.text_splitter.CharacterTextSplitter`将所有文档分成块。
- 3. 使用`langchain.embeddings.openai.OpenAIEmbeddings`和`langchain.vectorstores.DeepLake`嵌入这些块并上传到DeepLake。
2. 问答:


- 1. 使用`langchain.chat_models.ChatOpenAI`和`langchain.chains.ConversationalRetrievalChain`构建链。
- 2. 准备问题。
- 3. 运行链获得答案。




实现[#](#implementation "标题的永久链接")
-----------------------------------



### 集成准备[#](#integration-preparations "标题的永久链接")


我们需要为外部服务设置密钥并安装必要的Python库。





```
#!python3 -m pip install --upgrade langchain deeplake openai



```
设置OpenAI嵌入， Deep Lake 多模态向量存储API并进行身份验证。




有关Deep Lake的完整说明，请访问https://docs.activeloop.ai/和API参考https://docs.deeplake.ai/en/latest/




```

import os

from getpass import getpass



os.environ['OPENAI_API_KEY'] = getpass()

# Please manually enter OpenAI Key



```





```

 ········



```



如果您想创建自己的数据集并发布它，请在Deep Lake中进行身份验证。您可以从平台获得API密钥@[app.activeloop.ai]（https://app.activeloop.ai）




```

os.environ['ACTIVELOOP_TOKEN'] = getpass.getpass('Activeloop Token:')



```





```

 ········



```

### 准备数据[#](#prepare-data "此标题的永久链接")




加载所有存储库文件。 在这里，我们假设此文档是作为langchain分支的一部分下载的，我们使用`langchain`存储库的python文件工作。




如果要使用来自不同存储库的文件，请将`root_dir`更改为您的存储库的根目录。




```

from langchain.document_loaders import TextLoader



root_dir = '../../../..'



docs = []

for dirpath, dirnames, filenames in os.walk(root_dir):

    for file in filenames:

        if file.endswith('.py') and '/.venv/' not in dirpath:

            try: 

                loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')

                docs.extend(loader.load_and_split())

            except Exception as e: 

                pass

print(f'{len(docs)}')



```





```

1147



```



然后 块文件




```

from langchain.text_splitter import CharacterTextSplitter



text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

texts = text_splitter.split_documents(docs)

print(f"{len(texts)}")



```





```

Created a chunk of size 1620, which is longer than the specified 1000

Created a chunk of size 1213, which is longer than the specified 1000

Created a chunk of size 1263, which is longer than the specified 1000

Created a chunk of size 1448, which is longer than the specified 1000

Created a chunk of size 1120, which is longer than the specified 1000

Created a chunk of size 1148, which is longer than the specified 1000

Created a chunk of size 1826, which is longer than the specified 1000

Created a chunk of size 1260, which is longer than the specified 1000

Created a chunk of size 1195, which is longer than the specified 1000

Created a chunk of size 2147, which is longer than the specified 1000

Created a chunk of size 1410, which is longer than the specified 1000

Created a chunk of size 1269, which is longer than the specified 1000

Created a chunk of size 1030, which is longer than the specified 1000

Created a chunk of size 1046, which is longer than the specified 1000

Created a chunk of size 1024, which is longer than the specified 1000

Created a chunk of size 1026, which is longer than the specified 1000

Created a chunk of size 1285, which is longer than the specified 1000

Created a chunk of size 1370, which is longer than the specified 1000

Created a chunk of size 1031, which is longer than the specified 1000

Created a chunk of size 1999, which is longer than the specified 1000

Created a chunk of size 1029, which is longer than the specified 1000

Created a chunk of size 1120, which is longer than the specified 1000

Created a chunk of size 1033, which is longer than the specified 1000

Created a chunk of size 1143, which is longer than the specified 1000

Created a chunk of size 1416, which is longer than the specified 1000

Created a chunk of size 2482, which is longer than the specified 1000

Created a chunk of size 1890, which is longer than the specified 1000

Created a chunk of size 1418, which is longer than the specified 1000

Created a chunk of size 1848, which is longer than the specified 1000

Created a chunk of size 1069, which is longer than the specified 1000

Created a chunk of size 2369, which is longer than the specified 1000

Created a chunk of size 1045, which is longer than the specified 1000

Created a chunk of size 1501, which is longer than the specified 1000

Created a chunk of size 1208, which is longer than the specified 1000

Created a chunk of size 1950, which is longer than the specified 1000

Created a chunk of size 1283, which is longer than the specified 1000

Created a chunk of size 1414, which is longer than the specified 1000

Created a chunk of size 1304, which is longer than the specified 1000

Created a chunk of size 1224, which is longer than the specified 1000

Created a chunk of size 1060, which is longer than the specified 1000

Created a chunk of size 2461, which is longer than the specified 1000

Created a chunk of size 1099, which is longer than the specified 1000

Created a chunk of size 1178, which is longer than the specified 1000

Created a chunk of size 1449, which is longer than the specified 1000

Created a chunk of size 1345, which is longer than the specified 1000

Created a chunk of size 3359, which is longer than the specified 1000

Created a chunk of size 2248, which is longer than the specified 1000

Created a chunk of size 1589, which is longer than the specified 1000

Created a chunk of size 2104, which is longer than the specified 1000

Created a chunk of size 1505, which is longer than the specified 1000

Created a chunk of size 1387, which is longer than the specified 1000

Created a chunk of size 1215, which is longer than the specified 1000

Created a chunk of size 1240, which is longer than the specified 1000

Created a chunk of size 1635, which is longer than the specified 1000

Created a chunk of size 1075, which is longer than the specified 1000

Created a chunk of size 2180, which is longer than the specified 1000

Created a chunk of size 1791, which is longer than the specified 1000

Created a chunk of size 1555, which is longer than the specified 1000

Created a chunk of size 1082, which is longer than the specified 1000

Created a chunk of size 1225, which is longer than the specified 1000

Created a chunk of size 1287, which is longer than the specified 1000

Created a chunk of size 1085, which is longer than the specified 1000

Created a chunk of size 1117, which is longer than the specified 1000

Created a chunk of size 1966, which is longer than the specified 1000

Created a chunk of size 1150, which is longer than the specified 1000

Created a chunk of size 1285, which is longer than the specified 1000

Created a chunk of size 1150, which is longer than the specified 1000

Created a chunk of size 1585, which is longer than the specified 1000

Created a chunk of size 1208, which is longer than the specified 1000

Created a chunk of size 1267, which is longer than the specified 1000

Created a chunk of size 1542, which is longer than the specified 1000

Created a chunk of size 1183, which is longer than the specified 1000

Created a chunk of size 2424, which is longer than the specified 1000

Created a chunk of size 1017, which is longer than the specified 1000

Created a chunk of size 1304, which is longer than the specified 1000

Created a chunk of size 1379, which is longer than the specified 1000

Created a chunk of size 1324, which is longer than the specified 1000

Created a chunk of size 1205, which is longer than the specified 1000

Created a chunk of size 1056, which is longer than the specified 1000

Created a chunk of size 1195, which is longer than the specified 1000

Created a chunk of size 3608, which is longer than the specified 1000

Created a chunk of size 1058, which is longer than the specified 1000

Created a chunk of size 1075, which is longer than the specified 1000

Created a chunk of size 1217, which is longer than the specified 1000

Created a chunk of size 1109, which is longer than the specified 1000

Created a chunk of size 1440, which is longer than the specified 1000

Created a chunk of size 1046, which is longer than the specified 1000

Created a chunk of size 1220, which is longer than the specified 1000

Created a chunk of size 1403, which is longer than the specified 1000

Created a chunk of size 1241, which is longer than the specified 1000

Created a chunk of size 1427, which is longer than the specified 1000

Created a chunk of size 1049, which is longer than the specified 1000

Created a chunk of size 1580, which is longer than the specified 1000

Created a chunk of size 1565, which is longer than the specified 1000

Created a chunk of size 1131, which is longer than the specified 1000

Created a chunk of size 1425, which is longer than the specified 1000

Created a chunk of size 1054, which is longer than the specified 1000

Created a chunk of size 1027, which is longer than the specified 1000

Created a chunk of size 2559, which is longer than the specified 1000

Created a chunk of size 1028, which is longer than the specified 1000

Created a chunk of size 1382, which is longer than the specified 1000

Created a chunk of size 1888, which is longer than the specified 1000

Created a chunk of size 1475, which is longer than the specified 1000

Created a chunk of size 1652, which is longer than the specified 1000

Created a chunk of size 1891, which is longer than the specified 1000

Created a chunk of size 1899, which is longer than the specified 1000

Created a chunk of size 1021, which is longer than the specified 1000

Created a chunk of size 1085, which is longer than the specified 1000

Created a chunk of size 1854, which is longer than the specified 1000

Created a chunk of size 1672, which is longer than the specified 1000

Created a chunk of size 2537, which is longer than the specified 1000

Created a chunk of size 1251, which is longer than the specified 1000

Created a chunk of size 1734, which is longer than the specified 1000

Created a chunk of size 1642, which is longer than the specified 1000

Created a chunk of size 1376, which is longer than the specified 1000

Created a chunk of size 1253, which is longer than the specified 1000

Created a chunk of size 1642, which is longer than the specified 1000

Created a chunk of size 1419, which is longer than the specified 1000

Created a chunk of size 1438, which is longer than the specified 1000

Created a chunk of size 1427, which is longer than the specified 1000

Created a chunk of size 1684, which is longer than the specified 1000

Created a chunk of size 1760, which is longer than the specified 1000

Created a chunk of size 1157, which is longer than the specified 1000

Created a chunk of size 2504, which is longer than the specified 1000

Created a chunk of size 1082, which is longer than the specified 1000

Created a chunk of size 2268, which is longer than the specified 1000

Created a chunk of size 1784, which is longer than the specified 1000

Created a chunk of size 1311, which is longer than the specified 1000

Created a chunk of size 2972, which is longer than the specified 1000

Created a chunk of size 1144, which is longer than the specified 1000

Created a chunk of size 1825, which is longer than the specified 1000

Created a chunk of size 1508, which is longer than the specified 1000

Created a chunk of size 2901, which is longer than the specified 1000

Created a chunk of size 1715, which is longer than the specified 1000

Created a chunk of size 1062, which is longer than the specified 1000

Created a chunk of size 1206, which is longer than the specified 1000

Created a chunk of size 1102, which is longer than the specified 1000

Created a chunk of size 1184, which is longer than the specified 1000

Created a chunk of size 1002, which is longer than the specified 1000

Created a chunk of size 1065, which is longer than the specified 1000

Created a chunk of size 1871, which is longer than the specified 1000

Created a chunk of size 1754, which is longer than the specified 1000

Created a chunk of size 2413, which is longer than the specified 1000

Created a chunk of size 1771, which is longer than the specified 1000

Created a chunk of size 2054, which is longer than the specified 1000

Created a chunk of size 2000, which is longer than the specified 1000

Created a chunk of size 2061, which is longer than the specified 1000

Created a chunk of size 1066, which is longer than the specified 1000

Created a chunk of size 1419, which is longer than the specified 1000

Created a chunk of size 1368, which is longer than the specified 1000

Created a chunk of size 1008, which is longer than the specified 1000

Created a chunk of size 1227, which is longer than the specified 1000

Created a chunk of size 1745, which is longer than the specified 1000

Created a chunk of size 2296, which is longer than the specified 1000

Created a chunk of size 1083, which is longer than the specified 1000



```

```

3477



```

然后嵌入块并将它们上传到DeepLake。
Then embed chunks and upload them to the DeepLake.





This can take several minutes.




```
from langchain.embeddings.openai import OpenAIEmbeddings



embeddings = OpenAIEmbeddings()

embeddings



```
```
OpenAIEmbeddings(client=<class 'openai.api_resources.embedding.Embedding'>, model='text-embedding-ada-002', document_model_name='text-embedding-ada-002', query_model_name='text-embedding-ada-002', embedding_ctx_length=8191, openai_api_key=None, openai_organization=None, allowed_special=set(), disallowed_special='all', chunk_size=1000, max_retries=6)



```


```
from langchain.vectorstores import DeepLake



db = DeepLake.from_documents(texts, embeddings, dataset_path=f"hub://{DEEPLAKE_ACCOUNT_NAME}/langchain-code")

db



```

### 问答


首先加载数据集，构建检索器，然后再构建会话序列





```
db = DeepLake(dataset_path=f"hub://{DEEPLAKE_ACCOUNT_NAME}/langchain-code", read_only=True, embedding_function=embeddings)



```
```
-



```




```
This dataset can be visualized in Jupyter Notebook by ds.visualize() or at https://app.activeloop.ai/user_name/langchain-code



```




```
/



```




```
hub://user_name/langchain-code loaded successfully.



```




```
Deep Lake Dataset in hub://user_name/langchain-code already exists, loading from the storage



```




```
Dataset(path='hub://user_name/langchain-code', read_only=True, tensors=['embedding', 'ids', 'metadata', 'text'])



  tensor     htype      shape       dtype  compression

  -------   -------    -------     -------  ------- 

 embedding  generic  (3477, 1536)  float32   None   

    ids      text     (3477, 1)      str     None   

 metadata    json     (3477, 1)      str     None   

   text      text     (3477, 1)      str     None   



```


```
retriever = db.as_retriever()

retriever.search_kwargs['distance_metric'] = 'cos'

retriever.search_kwargs['fetch_k'] = 20

retriever.search_kwargs['maximal_marginal_relevance'] = True

retriever.search_kwargs['k'] = 20



```





您还可以使用[Deep Lake过滤器](https://docs.deeplake.ai/en/latest/deeplake.core.dataset.html#deeplake.core.dataset.Dataset.filter)指定用户定义的函数





```
def filter(x):

    # filter based on source code

    if 'something' in x['text'].data()['value']:

        return False

    

    # filter based on path e.g. extension

    metadata =  x['metadata'].data()['value']

    return 'only_this' in metadata['source'] or 'also_that' in metadata['source']



### turn on below for custom filtering

# retriever.search_kwargs['filter'] = filter



```


```
from langchain.chat_models import ChatOpenAI

from langchain.chains import ConversationalRetrievalChain



model = ChatOpenAI(model_name='gpt-3.5-turbo') # 'ada' 'gpt-3.5-turbo' 'gpt-4',

qa = ConversationalRetrievalChain.from_llm(model,retriever=retriever)



```


```
questions = [

    "What is the class hierarchy?",

    # "What classes are derived from the Chain class?",

    # "What classes and functions in the ./langchain/utilities/ forlder are not covered by unit tests?",

    # "What one improvement do you propose in code in relation to the class herarchy for the Chain class?",

] 

chat_history = []



for question in questions:  

    result = qa({"question": question, "chat_history": chat_history})

    chat_history.append((question, result['answer']))

    print(f"-> \*\*Question\*\*: {question} ")

    print(f"\*\*Answer\*\*: {result['answer']} ")



```





-> **问题**: 什么是类层次结构？

**回答**: 提供的代码中有几个类层次结构，以下是其中一些:


1.`BaseModel` -> `ConstitutionalPrinciple`: `ConstitutionalPrinciple`是`BaseModel`的子类。
1. `BaseModel` -> `ConstitutionalPrinciple`: `ConstitutionalPrinciple` is a subclass of `BaseModel`.

2. `BasePromptTemplate` -> `StringPromptTemplate`， `AIMessagePromptTemplate`， `BaseChatPromptTemplate`， `ChatMessagePromptTemplate`， `ChatPromptTemplate`， `HumanMessagePromptTemplate`， `MessagesPlaceholder`， `SystemMessagePromptTemplate`， `FewShotPromptTemplate`， `FewShotPromptWithTemplates`， `Prompt`， `PromptTemplate`# 所有这些类都是 `BasePromptTemplate` 的子类。
3. `APIChain`， `Chain`， `MapReduceDocumentsChain`， `MapRerankDocumentsChain`， `RefineDocumentsChain`， `StuffDocumentsChain`， `HypotheticalDocumentEmbedder`， `LLMChain`， `LLMBashChain`， `LLMCheckerChain`， `LLMMathChain`， `LLMRequestsChain`， `PALChain`， `QAWithSourcesChain`， `VectorDBQAWithSourcesChain`， `VectorDBQA`， `SQLDatabaseChain`# 所有这些类都是 `Chain` 的子类。
4. `BaseLoader`# `BaseLoader` 是 `ABC` 的子类。
5. `BaseTracer` -> `ChainRun`， `LLMRun`， `SharedTracer`， `ToolRun`， `Tracer`， `TracerException`， `TracerSession`# 所有这些类都是 `BaseTracer` 的子类。
6. `OpenAIEmbeddings`， `HuggingFaceEmbeddings`， `CohereEmbeddings`， `JinaEmbeddings`， `LlamaCppEmbeddings`， `HuggingFaceHubEmbeddings`， `TensorflowHubEmbeddings`， `SagemakerEndpointEmbeddings`， `HuggingFaceInstructEmbeddings`， `SelfHostedEmbeddings`， `SelfHostedHuggingFaceEmbeddings`， `SelfHostedHuggingFaceInstructEmbeddings`， `FakeEmbeddings`， `AlephAlphaAsymmetricSemanticEmbedding`， `AlephAlphaSymmetricSemanticEmbedding`# 所有这些类都是 `BaseLLM` 的子类。




-> **问题**# 有哪些类是从 Chain 类派生的？




**答案**# 有多个类从 Chain 类派生。其中一些是:




* APIChain
* AnalyzeDocumentChain

* ChatVectorDBChain（聊天向量数据库链）
* CombineDocumentsChain（合并文件链）
* ConstitutionalChain（宪法链）
* ConversationChain（对话链）
* GraphQAChain（图形问答链）
* HypotheticalDocumentEmbedder（假设文档嵌入器）
* LLMChain（LLM链）
* LLMCheckerChain（LLM检查链）
* LLMRequestsChain（LLM请求链）
* LLMSummarizationCheckerChain（LLM摘要检查链）
* MapReduceChain（MapReduce链）
* OpenAPIEndpointChain（OpenAPI端点链）
* PALChain（PAL链）
* QAWithSourcesChain（带源问答链）
* RetrievalQA（检索问答）
* RetrievalQAWithSourcesChain（带源检索问答链）
* SequentialChain（顺序链）
* SQLDatabaseChain（SQL数据库链）
* TransformChain（转换链）
* VectorDBQA（向量数据库问答）
* VectorDBQAWithSourcesChain（带源向量数据库问答链）




可能会有更多派生自Chain类的类，因为可能创建自定义类来扩展Chain类。（There might be more classes that are derived from the Chain class as it is possible to create custom classes that extend the Chain class.）




-> **问题**: 在./langchain/utilities/文件夹中，哪些类和函数没有被单元测试覆盖？（-> **Question**: What classes and functions in the ./langchain/utilities/ forlder are not covered by unit tests?）




**Answer**: All classes and functions in the `./langchain/utilities/` folder seem to have unit tests written for them.





