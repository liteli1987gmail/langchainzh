

路由器链：使用MultiRetrievalQAChain从多个提示中选择[#](#router-chains-selecting-from-multiple-prompts-with-multiretrievalqachain "Permalink to this headline")
===============================================================================================================================================

本笔记本演示如何使用 `RouterChain` 范例创建一个动态选择使用哪个检索系统的链。具体而言，我们展示了如何使用 `MultiRetrievalQAChain` 创建一个问答链，该链选择对于给定问题最相关的检索QA链，然后使用它回答问题。

```
from langchain.chains.router import MultiRetrievalQAChain
from langchain.llms import OpenAI

```

```
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS

sou_docs = TextLoader('../../state_of_the_union.txt').load_and_split()
sou_retriever = FAISS.from_documents(sou_docs, OpenAIEmbeddings()).as_retriever()

pg_docs = TextLoader('../../paul_graham_essay.txt').load_and_split()
pg_retriever = FAISS.from_documents(pg_docs, OpenAIEmbeddings()).as_retriever()

personal_texts = [
    "I love apple pie",
    "My favorite color is fuchsia",
    "My dream is to become a professional dancer",
    "I broke my arm when I was 12",
    "My parents are from Peru",
]
personal_retriever = FAISS.from_texts(personal_texts, OpenAIEmbeddings()).as_retriever()

```

```
retriever_infos = [
    {
        "name": "state of the union", 
        "description": "Good for answering questions about the 2023 State of the Union address", 
        "retriever": sou_retriever
    },
    {
        "name": "pg essay", 
        "description": "Good for answer quesitons about Paul Graham's essay on his career", 
        "retriever": pg_retriever
    },
    {
        "name": "personal", 
        "description": "Good for answering questions about me", 
        "retriever": personal_retriever
    }
]

```

```
chain = MultiRetrievalQAChain.from_retrievers(OpenAI(), retriever_infos, verbose=True)

```

```
print(chain.run("What did the president say about the economy?"))

```

```
> Entering new MultiRetrievalQAChain chain...
state of the union: {'query': 'What did the president say about the economy in the 2023 State of the Union address?'}
> Finished chain.
 The president said that the economy was stronger than it had been a year prior, and that the American Rescue Plan helped create record job growth and fuel economic relief for millions of Americans. He also proposed a plan to fight inflation and lower costs for families, including cutting the cost of prescription drugs and energy, providing investments and tax credits for energy efficiency, and increasing access to child care and Pre-K.

```

```
print(chain.run("What is something Paul Graham regrets about his work?"))

```

```
> Entering new MultiRetrievalQAChain chain...
pg essay: {'query': 'What is something Paul Graham regrets about his work?'}
> Finished chain.
 Paul Graham regrets that he did not take a vacation after selling his company, instead of immediately starting to paint.

```

```
print(chain.run("What is my background?"))

```

```
> Entering new MultiRetrievalQAChain chain...
personal: {'query': 'What is my background?'}
> Finished chain.
 Your background is Peruvian.

```

```
print(chain.run("What year was the Internet created in?"))

```

```
> Entering new MultiRetrievalQAChain chain...
None: {'query': 'What year was the Internet created in?'}
> Finished chain.
The Internet was created in 1969 through a project called ARPANET, which was funded by the United States Department of Defense. However, the World Wide Web, which is often confused with the Internet, was created in 1989 by British computer scientist Tim Berners-Lee.

```

