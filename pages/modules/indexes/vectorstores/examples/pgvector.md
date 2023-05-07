PGVector[#](#pgvector "Permalink to this headline")
===================================================

> 
> [PGVector](https://github.com/pgvector/pgvector)是用于`Postgres`的开源向量相似度搜索
> 
> 
> 

它支持：

* 精确和近似最近邻搜索

* L2距离，内积和余弦距离

本笔记本演示了如何使用Postgres向量数据库（`PGVector`）。

请参阅[安装指令](https://github.com/pgvector/pgvector)。

```
!pip install pgvector

```

我们想使用`OpenAIEmbeddings`，因此必须获取OpenAI API密钥。

```
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API密钥：')

```

```
## 加载环境变量
from typing import List, Tuple
from dotenv import load_dotenv
load_dotenv()

```

```
False

```

```
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.pgvector import PGVector
from langchain.document_loaders import TextLoader
from langchain.docstore.document import Document

```

```
loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

```

```
## PGVector需要数据库的连接字符串。
## 我们将从环境变量中加载它。
import os
CONNECTION_STRING = PGVector.connection_string_from_db_params(
    driver=os.environ.get("PGVECTOR_DRIVER", "psycopg2"),
    host=os.environ.get("PGVECTOR_HOST", "localhost"),
    port=int(os.environ.get("PGVECTOR_PORT", "5432")),
    database=os.environ.get("PGVECTOR_DATABASE", "postgres"),
    user=os.environ.get("PGVECTOR_USER", "postgres"),
    password=os.environ.get("PGVECTOR_PASSWORD", "postgres"),
)

## 示例
# postgresql+psycopg2://username:password@localhost:5432/database_name

```

带分数的相似性搜索[#](#similarity-search-with-score "Permalink to this headline")
-------------------------------------------------------------------------------------------

### 使用欧几里得距离进行相似性搜索（默认）[#](#similarity-search-with-euclidean-distance-default "Permalink to this headline")

```
# PGVector模块将尝试使用集合名称创建表。因此，请确保集合名称唯一且用户有
# 权限创建表。

db = PGVector.from_documents(
    embedding=embeddings,
    documents=docs,
    collection_name="state_of_the_union",
    connection_string=CONNECTION_STRING,
)

query = "总统对Ketanji Brown Jackson说了什么"
docs_with_score: List[Tuple[Document, float]] = db.similarity_search_with_score(query)

```

```
for doc, score in docs_with_score:
    print("-" * 80)
    print("分数：", score)
    print(doc.page_content)
    print("-" * 80)

```

```
--------------------------------------------------------------------------------
分数： 0.6076628081132506
今晚。我呼吁参议院：通过《自由投票法》。通过约翰·刘易斯选票权法案。当你在那里时，通过《揭示法》，以便美国人可以知道谁在资助我们的选举。

今晚，我想向一位献身于为这个国家服务的人致敬：史蒂芬·布雷耶法官——陆军退伍军人，宪法学者，美国最高法院即将退休的法官。布雷耶法官，谢谢您的服务。

总统最重要的宪法责任之一是提名人担任美国最高法院大法官。

4天前，当我提名电路法院法官Ketanji Brown Jackson时，我就做到了。

```