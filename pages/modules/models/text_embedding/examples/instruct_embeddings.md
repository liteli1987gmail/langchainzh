
InstructEmbeddings[#](#instructembeddings "此标题的永久链接")
=======================================================================

让我们加载HuggingFace instruct嵌入类。

```
from langchain.embeddings import HuggingFaceInstructEmbeddings

```

```
embeddings = HuggingFaceInstructEmbeddings(
    query_instruction="Represent the query for retrieval: "
)

```

```
load INSTRUCTOR_Transformer
max_seq_length  512

```

```
text = "This is a test document."

```

```
query_result = embeddings.embed_query(text)

```

