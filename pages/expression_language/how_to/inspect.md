# 检查你的可运行实体

一旦你使用LCEL创建了一个可运行实体，你可能经常想要检查它以更好地了解正在进行的事情。本笔记本介绍了一些方法来进行此操作。

首先，让我们创建一个示例LCEL。我们将创建一个进行检索的实体


```python
%pip install --upgrade --quiet  langchain langchain-openai faiss-cpu tiktoken
```


```python
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
```


```python
vectorstore = FAISS.from_texts(
    ["harrison worked at kensho"], embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

template = """根据以下上下文回答问题：
{context}

问题：{question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI()
```


```python
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)
```

## 获取图形

您可以获取可运行实体的图形


```python
chain.get_graph()
```

## 打印图形

尽管这并没有非常易读，但您可以打印它以获得更易于理解的显示


```python
chain.get_graph().print_ascii()
```

               +---------------------------------+         
               | 并行<context,question>输入 |         
               +---------------------------------+         
                        **               **                
                     ***                   ***             
                   **                         **           
    +----------------------+              +-------------+  
    | VectorStoreRetriever |              | Passthrough |  
    +----------------------+              +-------------+  
                        **               **                
                          ***         ***                  
                             **     **                     
               +----------------------------------+        
               | 并行<context,question>输出 |        
               +----------------------------------+        
                                 *                         
                                 *                         
                                 *                         
                      +--------------------+               
                      | ChatPromptTemplate |               
                      +--------------------+               
                                 *                         
                                 *                         
                                 *                         
                          +------------+                   
                          | ChatOpenAI |                   
                          +------------+                   
                                 *                         
                                 *                         
                                 *                         
                       +-----------------+                 
                       | StrOutputParser |                 
                       +-----------------+                 
                                 *                         
                                 *                         
                                 *                         
                    +-----------------------+              
                    | StrOutputParserOutput |              
                    +-----------------------+              
    

## 获取提示

每个链中的提示是重要的部分。您可以获取链中的提示：


```python
chain.get_prompts()
```




    [ChatPromptTemplate(input_variables=['context', 'question'], messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['context', 'question'], template='根据以下上下文回答问题：\n{context}\n\n问题：{question}\n'))])]



