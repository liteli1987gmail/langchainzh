


 PowerBI Dataset Agent
 [#](#powerbi-dataset-agent "Permalink to this headline")
=================================================================================



 This notebook showcases an agent designed to interact with a Power BI Dataset. The agent is designed to answer more general questions about a dataset, as well as recover from errors.
 



 Note that, as this agent is in active development, all answers might not be correct. It runs against the
 [executequery endpoint](https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/execute-queries) 
 , which does not allow deletes.
 




 Some notes
 [#](#some-notes "Permalink to this headline")
-----------------------------------------------------------


* It relies on authentication with the azure.identity package, which can be installed with
 `pip
 

 install
 

 azure-identity`
 . Alternatively you can create the powerbi dataset with a token as a string without supplying the credentials.
* You can also supply a username to impersonate for use with datasets that have RLS enabled.
* The toolkit uses a LLM to create the query from the question, the agent uses the LLM for the overall execution.
* Testing was done mostly with a
 `text-davinci-003`
 model, codex models did not seem to perform ver well.





 Initialization
 [#](#initialization "Permalink to this headline")
-------------------------------------------------------------------







```
from langchain.agents.agent_toolkits import create_pbi_agent
from langchain.agents.agent_toolkits import PowerBIToolkit
from langchain.utilities.powerbi import PowerBIDataset
from langchain.llms.openai import AzureOpenAI
from langchain.agents import AgentExecutor
from azure.identity import DefaultAzureCredential

```










```
fast_llm = AzureOpenAI(temperature=0.5, max_tokens=1000, deployment_name="gpt-35-turbo", verbose=True)
smart_llm = AzureOpenAI(temperature=0, max_tokens=100, deployment_name="gpt-4", verbose=True)

toolkit = PowerBIToolkit(
    powerbi=PowerBIDataset(dataset_id="<dataset_id>", table_names=['table1', 'table2'], credential=DefaultAzureCredential()), 
    llm=smart_llm
)

agent_executor = create_pbi_agent(
    llm=fast_llm,
    toolkit=toolkit,
    verbose=True,
)

```








 Example: describing a table
 [#](#example-describing-a-table "Permalink to this headline")
--------------------------------------------------------------------------------------------







```
agent_executor.run("Describe table1")

```








 Example: simple query on a table
 [#](#example-simple-query-on-a-table "Permalink to this headline")
------------------------------------------------------------------------------------------------------



 In this example, the agent actually figures out the correct query to get a row count of the table.
 







```
agent_executor.run("How many records are in table1?")

```








 Example: running queries
 [#](#example-running-queries "Permalink to this headline")
--------------------------------------------------------------------------------------







```
agent_executor.run("How many records are there by dimension1 in table2?")

```










```
agent_executor.run("What unique values are there for dimensions2 in table2")

```








 Example: add your own few-shot prompts
 [#](#example-add-your-own-few-shot-prompts "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------







```
#fictional example
few_shots = """
Question: How many rows are in the table revenue?
DAX: EVALUATE ROW("Number of rows", COUNTROWS(revenue_details))
----
Question: How many rows are in the table revenue where year is not empty?
DAX: EVALUATE ROW("Number of rows", COUNTROWS(FILTER(revenue_details, revenue_details[year] <> "")))
----
Question: What was the average of value in revenue in dollars?
DAX: EVALUATE ROW("Average", AVERAGE(revenue_details[dollar_value]))
----
"""
toolkit = PowerBIToolkit(
    powerbi=PowerBIDataset(dataset_id="<dataset_id>", table_names=['table1', 'table2'], credential=DefaultAzureCredential()), 
    llm=smart_llm,
    examples=few_shots,
)
agent_executor = create_pbi_agent(
    llm=fast_llm,
    toolkit=toolkit,
    verbose=True,
)

```










```
agent_executor.run("What was the maximum of value in revenue in dollars in 2022?")

```








