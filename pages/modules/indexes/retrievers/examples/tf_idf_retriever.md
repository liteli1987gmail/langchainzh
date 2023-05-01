


 TF-IDF Retriever
 [#](#tf-idf-retriever "Permalink to this headline")
=======================================================================



 This notebook goes over how to use a retriever that under the hood uses TF-IDF using scikit-learn.
 



 For more information on the details of TF-IDF see
 [this blog post](https://medium.com/data-science-bootcamp/tf-idf-basics-of-information-retrieval-48de122b2a4c) 
 .
 







```
from langchain.retrievers import TFIDFRetriever

```










```
# !pip install scikit-learn

```







 Create New Retriever with Texts
 [#](#create-new-retriever-with-texts "Permalink to this headline")
-----------------------------------------------------------------------------------------------------







```
retriever = TFIDFRetriever.from_texts(["foo", "bar", "world", "hello", "foo bar"])

```








 Use Retriever
 [#](#use-retriever "Permalink to this headline")
-----------------------------------------------------------------



 We can now use the retriever!
 







```
result = retriever.get_relevant_documents("foo")

```










```
result

```








```
[Document(page_content='foo', metadata={}),
 Document(page_content='foo bar', metadata={}),
 Document(page_content='hello', metadata={}),
 Document(page_content='world', metadata={})]

```








