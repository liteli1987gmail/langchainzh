


 QA Generation
 [#](#qa-generation "Permalink to this headline")
=================================================================



 This notebook shows how to use the
 `QAGenerationChain`
 to come up with question-answer pairs over a specific document.
This is important because often times you may not have data to evaluate your question-answer system over, so this is a cheap and lightweight way to generate it!
 







```
from langchain.document_loaders import TextLoader

```










```
loader = TextLoader("../../modules/state_of_the_union.txt")

```










```
doc = loader.load()[0]

```










```
from langchain.chat_models import ChatOpenAI
from langchain.chains import QAGenerationChain
chain = QAGenerationChain.from_llm(ChatOpenAI(temperature = 0))

```










```
qa = chain.run(doc.page_content)

```










```
qa[1]

```








```
{'question': 'What is the U.S. Department of Justice doing to combat the crimes of Russian oligarchs?',
 'answer': 'The U.S. Department of Justice is assembling a dedicated task force to go after the crimes of Russian oligarchs.'}

```







