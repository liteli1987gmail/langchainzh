


 Agent Benchmarking: Search + Calculator
 [#](#agent-benchmarking-search-calculator "Permalink to this headline")
==================================================================================================================



 Here we go over how to benchmark performance of an agent on tasks where it has access to a calculator and a search tool.
 



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
dataset = load_dataset("agent-search-calculator")

```








 Setting up a chain
 [#](#setting-up-a-chain "Permalink to this headline")
---------------------------------------------------------------------------



 Now we need to load an agent capable of answering these questions.
 







```
from langchain.llms import OpenAI
from langchain.chains import LLMMathChain
from langchain.agents import initialize_agent, Tool, load_tools
from langchain.agents import AgentType

tools = load_tools(['serpapi', 'llm-math'], llm=OpenAI(temperature=0))
agent = initialize_agent(tools, OpenAI(temperature=0), agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

```








 Make a prediction
 [#](#make-a-prediction "Permalink to this headline")
-------------------------------------------------------------------------



 First, we can make predictions one datapoint at a time. Doing it at this level of granularity allows use to explore the outputs in detail, and also is a lot cheaper than running over multiple datapoints
 







```
print(dataset[0]['question'])
agent.run(dataset[0]['question'])

```








 Make many predictions
 [#](#make-many-predictions "Permalink to this headline")
---------------------------------------------------------------------------------



 Now we can make predictions
 







```
agent.run(dataset[4]['question'])

```










```
predictions = []
predicted_dataset = []
error_dataset = []
for data in dataset:
    new_data = {"input": data["question"], "answer": data["answer"]}
    try:
        predictions.append(agent(new_data))
        predicted_dataset.append(new_data)
    except Exception as e:
        predictions.append({"output": str(e), \*\*new_data})
        error_dataset.append(new_data)

```








 Evaluate performance
 [#](#evaluate-performance "Permalink to this headline")
-------------------------------------------------------------------------------



 Now we can evaluate the predictions. The first thing we can do is look at them by eye.
 







```
predictions[0]

```






 Next, we can use a language model to score them programatically
 







```
from langchain.evaluation.qa import QAEvalChain

```










```
llm = OpenAI(temperature=0)
eval_chain = QAEvalChain.from_llm(llm)
graded_outputs = eval_chain.evaluate(dataset, predictions, question_key="question", prediction_key="output")

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






 We can also filter the datapoints to the incorrect examples and look at them.
 







```
incorrect = [pred for pred in predictions if pred['grade'] == " INCORRECT"]

```










```
incorrect

```








