# 递归拆分JSON

这个json拆分器按照深度优先的方式遍历json数据并构建较小的json块。它尝试保持嵌套的json对象完整，但如果需要时会对它们进行拆分，以保持块在最小块大小和最大块大小之间。如果值不是嵌套的json，而是一个非常大的字符串，则该字符串不会被拆分。如果您需要对块大小进行硬性限制，可以考虑在这些块上跟随递归文本拆分器的操作。还有一个可选的预处理步骤，可以通过先将列表转换为json（字典），然后将其拆分为这种形式。

1. 文本如何拆分：json值。
2. 块大小如何测量：按字符数。

```python
%pip install -qU langchain-text-splitters
```

```python
import json

import requests
```

```python
# 这是一个大的嵌套json对象，将被加载为python字典
json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()
```

```python
from langchain_text_splitters import RecursiveJsonSplitter
```

```python
splitter = RecursiveJsonSplitter(max_chunk_size=300)
```

```python
# 递归拆分json数据 - 如果需要访问/操作较小的json块
json_chunks = splitter.split_json(json_data=json_data)
```

```python
# 拆分器还可以输出文档
docs = splitter.create_documents(texts=[json_data])

# 或者一个字符串列表
texts = splitter.split_text(json_data=json_data)

print(texts[0])
print(texts[1])
```
```
{"openapi": "3.0.2", "info": {"title": "LangChainPlus", "version": "0.1.0"}, "paths": {"/sessions/{session_id}": {"get": {"tags": ["tracer-sessions"], "summary": "Read Tracer Session", "description": "Get a specific session.", "operationId": "read_tracer_session_sessions__session_id__get"}}}}
{"paths": {"/sessions/{session_id}": {"get": {"parameters": [{"required": true, "schema": {"title": "Session Id", "type": "string", "format": "uuid"}, "name": "session_id", "in": "path"}, {"required": false, "schema": {"title": "Include Stats", "type": "boolean", "default": false}, "name": "include_stats", "in": "query"}, {"required": false, "schema": {"title": "Accept", "type": "string"}, "name": "accept", "in": "header"}]}}}}
```
```python
# 让我们看一下这些块的大小
print([len(text) for text in texts][:10])

# 检查一个比较大的块，我们会发现里面有一个列表对象
print(texts[1])
```
```
[293, 431, 203, 277, 230, 194, 162, 280, 223, 193]
{"paths": {"/sessions/{session_id}": {"get": {"parameters": [{"required": true, "schema": {"title": "Session Id", "type": "string", "format": "uuid"}, "name": "session_id", "in": "path"}, {"required": false, "schema": {"title": "Include Stats", "type": "boolean", "default": false}, "name": "include_stats", "in": "query"}, {"required": false, "schema": {"title": "Accept", "type": "string"}, "name": "accept", "in": "header"}]}}}}
```
```python
# 默认情况下，json拆分器不会拆分列表
# 以下操作将预处理json并将列表转换为索引:值对的字典
texts = splitter.split_text(json_data=json_data, convert_lists=True)
```

```python
# 让我们看一下这些块的大小。现在它们都在最大块以下
print([len(text) for text in texts][:10])
```

[293, 431, 203, 277, 230, 194, 162, 280, 223, 193]

```python
# 这个列表已经被转换为字典，但即使被拆分成多个块，它仍保留所有需要的上下文信息
print(texts[1])
```
```
{"paths": {"/sessions/{session_id}": {"get": {"parameters": [{"required": true, "schema": {"title": "Session Id", "type": "string", "format": "uuid"}, "name": "session_id", "in": "path"}, {"required": false, "schema": {"title": "Include Stats", "type": "boolean", "default": false}, "name": "include_stats", "in": "query"}, {"required": false, "schema": {"title": "Accept", "type": "string"}, "name": "accept", "in": "header"}]}}}}
```
```python
# 我们还可以查看文档
docs[1]
```