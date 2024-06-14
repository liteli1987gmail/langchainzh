# 在多输入链中的记忆

大多数记忆对象都假设只有一个输入。在本文档中，我们将介绍如何向具有多个输入的链中添加记忆。我们将为问答链添加记忆。该链将相关文档和用户问题作为输入。

```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
```

```python
with open("../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(state_of_the_union)

embeddings = OpenAIEmbeddings()
```

```python
docsearch = Chroma.from_texts(
    texts, embeddings, metadatas=[{"source": i} for i in range(len(texts))]
)
```

正在使用直接本地API运行Chroma。

正在使用内存中的DuckDB进行数据库操作。数据将是临时的。
```python
query = "The president said about Justice Breyer"
docs = docsearch.similarity_search(query)
```

```python
from langchain.chains.question_answering import load_qa_chain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
```

```python
template = """您是一个与人对话的聊天机器人。

给定以下长文档的提取部分和一个问题，请生成最终的答案。

{context}

{chat_history}
人类: {human_input}
聊天机器人:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input", "context"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history", input_key="human_input")
chain = load_qa_chain(
    OpenAI(temperature=0), chain_type="stuff", memory=memory, prompt=prompt
)
```

```python
query = "The president said about Justice Breyer"
chain({"input_documents": docs, "human_input": query}, return_only_outputs=True)
```

```python
print(chain.memory.buffer)
```

人类: 问题：总统说了些什么关于布雷耶法官
AI: 今晚，我想向一个致力于为这个国家服务的人致敬：司法部长斯蒂芬·布雷耶 —— 一个陆军老兵、宪法学者和即将退休的美国最高法院法官。谢谢你的服务。

