


 SQL Question Answering Benchmarking: Chinook
 [#](#sql-question-answering-benchmarking-chinook "Permalink to this headline")
==============================================================================================================================



 Here we go over how to benchmark performance on a question answering task over a SQL database.
 



 It is highly reccomended that you do any evaluation/benchmarking with tracing enabled. See
 [here](https://langchain.readthedocs.io/en/latest/tracing) 
 for an explanation of what tracing is and how to set it up.
 







```
# Comment this out if you are NOT using tracing
import os
os.environ["LANGCHAIN_HANDLER"] = "langchain"

```







 Loading the data
 [#](#loading-the-data "Permalink to this headline")
-----------------------------------------------------------------------



 First, let’s load the data.
 







```
from langchain.evaluation.loading import load_dataset
dataset = load_dataset("sql-qa-chinook")

```






 {"model_id": "b220d07ee5d14909bc842b4545cdc0de", "version_major": 2, "version_minor": 0}
 



```
Downloading and preparing dataset json/LangChainDatasets--sql-qa-chinook to /Users/harrisonchase/.cache/huggingface/datasets/LangChainDatasets___json/LangChainDatasets--sql-qa-chinook-7528565d2d992b47/0.0.0/0f7e3662623656454fcd2b650f34e886a7db4b9104504885bd462096cc7a9f51...

```




 {"model_id": "e89e3c8ef76f49889c4b39c624828c71", "version_major": 2, "version_minor": 0}
 

 {"model_id": "a8421df6c26045e8978c7086cb418222", "version_major": 2, "version_minor": 0}
 

 {"model_id": "d1fb6becc3324a85bf039a53caf30924", "version_major": 2, "version_minor": 0}
 

 {"model_id": "", "version_major": 2, "version_minor": 0}
 



```
Dataset json downloaded and prepared to /Users/harrisonchase/.cache/huggingface/datasets/LangChainDatasets___json/LangChainDatasets--sql-qa-chinook-7528565d2d992b47/0.0.0/0f7e3662623656454fcd2b650f34e886a7db4b9104504885bd462096cc7a9f51. Subsequent calls will reuse this data.

```




 {"model_id": "9d68ad1b3e4a4bd79f92597aac4d3cc9", "version_major": 2, "version_minor": 0}
 







```
dataset[0]

```








```
{'question': 'How many employees are there?', 'answer': '8'}

```








 Setting up a chain
 [#](#setting-up-a-chain "Permalink to this headline")
---------------------------------------------------------------------------



 This uses the example Chinook database.
To set it up follow the instructions on https://database.guide/2-sample-databases-sqlite/, placing the
 `.db`
 file in a notebooks folder at the root of this repository.
 



 Note that here we load a simple chain. If you want to experiment with more complex chains, or an agent, just create the
 `chain`
 object in a different way.
 







```
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

```










```
db = SQLDatabase.from_uri("sqlite:///../../../notebooks/Chinook.db")
llm = OpenAI(temperature=0)

```






 Now we can create a SQL database chain.
 







```
chain = SQLDatabaseChain(llm=llm, database=db, input_key="question")

```








 Make a prediction
 [#](#make-a-prediction "Permalink to this headline")
-------------------------------------------------------------------------



 First, we can make predictions one datapoint at a time. Doing it at this level of granularity allows use to explore the outputs in detail, and also is a lot cheaper than running over multiple datapoints
 







```
chain(dataset[0])

```








```
{'question': 'How many employees are there?',
 'answer': '8',
 'result': ' There are 8 employees.'}

```








 Make many predictions
 [#](#make-many-predictions "Permalink to this headline")
---------------------------------------------------------------------------------



 Now we can make predictions. Note that we add a try-except because this chain can sometimes error (if SQL is written incorrectly, etc)
 







```
predictions = []
predicted_dataset = []
error_dataset = []
for data in dataset:
    try:
        predictions.append(chain(data))
        predicted_dataset.append(data)
    except:
        error_dataset.append(data)

```








 Evaluate performance
 [#](#evaluate-performance "Permalink to this headline")
-------------------------------------------------------------------------------



 Now we can evaluate the predictions. We can use a language model to score them programatically
 







```
from langchain.evaluation.qa import QAEvalChain

```










```
llm = OpenAI(temperature=0)
eval_chain = QAEvalChain.from_llm(llm)
graded_outputs = eval_chain.evaluate(predicted_dataset, predictions, question_key="question", prediction_key="result")

```






 We can add in the graded output to the
 `predictions`
 dict and then get a count of the grades.
 







```
for i, prediction in enumerate(predictions):
    prediction['grade'] = graded_outputs[i]['text']

```










```
from collections import Counter
Counter([pred['grade'] for pred in predictions])

```








```
Counter({' CORRECT': 3, ' INCORRECT': 4})

```






 We can also filter the datapoints to the incorrect examples and look at them.
 







```
incorrect = [pred for pred in predictions if pred['grade'] == " INCORRECT"]

```










```
incorrect[0]

```








```
{'question': 'How many employees are also customers?',
 'answer': 'None',
 'result': ' 59 employees are also customers.',
 'grade': ' INCORRECT'}

```








