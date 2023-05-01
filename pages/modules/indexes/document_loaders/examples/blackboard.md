


 Blackboard
 [#](#blackboard "Permalink to this headline")
===========================================================



 This covers how to load data from a Blackboard Learn instance.
 







```
from langchain.document_loaders import BlackboardLoader

loader = BlackboardLoader(
    blackboard_course_url="https://blackboard.example.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_123456_1",
    bbrouter="expires:12345...",
    load_all_recursively=True,
)
documents = loader.load()

```







