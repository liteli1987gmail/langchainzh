


 Weights & Biases
 [#](#weights-biases "Permalink to this headline")
=====================================================================



 This notebook goes over how to track your LangChain experiments into one centralized Weights and Biases dashboard. To learn more about prompt engineering and the callback please refer to this Report which explains both alongside the resultant dashboards you can expect to see.
 



 Run in Colab: https://colab.research.google.com/drive/1DXH4beT4HFaRKy_Vm4PoxhXVDRf7Ym8L?usp=sharing
 



 View Report: https://wandb.ai/a-sh0ts/langchain_callback_demo/reports/Prompt-Engineering-LLMs-with-LangChain-and-W-B–VmlldzozNjk1NTUw#👋-how-to-build-a-callback-in-langchain-for-better-prompt-engineering
 







```
!pip install wandb
!pip install pandas
!pip install textstat
!pip install spacy
!python -m spacy download en_core_web_sm

```










```
import os
os.environ["WANDB_API_KEY"] = ""
# os.environ["OPENAI_API_KEY"] = ""
# os.environ["SERPAPI_API_KEY"] = ""

```










```
from datetime import datetime
from langchain.callbacks import WandbCallbackHandler, StdOutCallbackHandler
from langchain.llms import OpenAI

```








```
Callback Handler that logs to Weights and Biases.

Parameters:
    job_type (str): The type of job.
    project (str): The project to log to.
    entity (str): The entity to log to.
    tags (list): The tags to log.
    group (str): The group to log to.
    name (str): The name of the run.
    notes (str): The notes to log.
    visualize (bool): Whether to visualize the run.
    complexity_metrics (bool): Whether to log complexity metrics.
    stream_logs (bool): Whether to stream callback actions to W&B

```






```
Default values for WandbCallbackHandler(...)

visualize: bool = False,
complexity_metrics: bool = False,
stream_logs: bool = False,

```




 NOTE: For beta workflows we have made the default analysis based on textstat and the visualizations based on spacy
 







```
"""Main function.

This function is used to try the callback handler.
Scenarios:
1. OpenAI LLM
2. Chain with multiple SubChains on multiple generations
3. Agent with Tools
"""
session_group = datetime.now().strftime("%m.%d.%Y_%H.%M.%S")
wandb_callback = WandbCallbackHandler(
    job_type="inference",
    project="langchain_callback_demo",
    group=f"minimal_{session_group}",
    name="llm",
    tags=["test"],
)
callbacks = [StdOutCallbackHandler(), wandb_callback]
llm = OpenAI(temperature=0, callbacks=callbacks)

```








```
wandb: Currently logged in as: harrison-chase. Use `wandb login --relogin` to force relogin

```




 Tracking run with wandb version 0.14.0
 

 Run data is saved locally in
 `/Users/harrisonchase/workplace/langchain/docs/ecosystem/wandb/run-20230318_150408-e47j1914` 


 Syncing run
 **[llm](https://wandb.ai/harrison-chase/langchain_callback_demo/runs/e47j1914)**
 to
 [Weights & Biases](https://wandb.ai/harrison-chase/langchain_callback_demo) 
 (
 [docs](https://wandb.me/run) 
 )
   



 View project at
 <https://wandb.ai/harrison-chase/langchain_callback_demo>


 View run at
 <https://wandb.ai/harrison-chase/langchain_callback_demo/runs/e47j1914>




```
wandb: WARNING The wandb callback is currently in beta and is subject to change based on updates to `langchain`. Please report any issues to https://github.com/wandb/wandb/issues with the tag `langchain`.

```








```
# Defaults for WandbCallbackHandler.flush_tracker(...)

reset: bool = True,
finish: bool = False,

```




 The
 `flush_tracker`
 function is used to log LangChain sessions to Weights & Biases. It takes in the LangChain module or agent, and logs at minimum the prompts and generations alongside the serialized form of the LangChain module to the specified Weights & Biases project. By default we reset the session as opposed to concluding the session outright.
 







```
# SCENARIO 1 - LLM
llm_result = llm.generate(["Tell me a joke", "Tell me a poem"] \* 3)
wandb_callback.flush_tracker(llm, name="simple_sequential")

```






 Waiting for W&B process to finish...
 **(success).** 


 View run
 **llm** 
 at:
 <https://wandb.ai/harrison-chase/langchain_callback_demo/runs/e47j1914>
  

 Synced 5 W&B file(s), 2 media file(s), 5 artifact file(s) and 0 other file(s)
 

 Find logs at:
 `./wandb/run-20230318_150408-e47j1914/logs` 


 {"model_id": "0d7b4307ccdb450ea631497174fca2d1", "version_major": 2, "version_minor": 0}
 

 Tracking run with wandb version 0.14.0
 

 Run data is saved locally in
 `/Users/harrisonchase/workplace/langchain/docs/ecosystem/wandb/run-20230318_150534-jyxma7hu` 


 Syncing run
 **[simple_sequential](https://wandb.ai/harrison-chase/langchain_callback_demo/runs/jyxma7hu)**
 to
 [Weights & Biases](https://wandb.ai/harrison-chase/langchain_callback_demo) 
 (
 [docs](https://wandb.me/run) 
 )
   



 View project at
 <https://wandb.ai/harrison-chase/langchain_callback_demo>


 View run at
 <https://wandb.ai/harrison-chase/langchain_callback_demo/runs/jyxma7hu>








```
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

```










```
# SCENARIO 2 - Chain
template = """You are a playwright. Given the title of play, it is your job to write a synopsis for that title.
Title: {title}
Playwright: This is a synopsis for the above play:"""
prompt_template = PromptTemplate(input_variables=["title"], template=template)
synopsis_chain = LLMChain(llm=llm, prompt=prompt_template, callbacks=callbacks)

test_prompts = [
    {
        "title": "documentary about good video games that push the boundary of game design"
    },
    {"title": "cocaine bear vs heroin wolf"},
    {"title": "the best in class mlops tooling"},
]
synopsis_chain.apply(test_prompts)
wandb_callback.flush_tracker(synopsis_chain, name="agent")

```






 Waiting for W&B process to finish...
 **(success).** 


 View run
 **simple_sequential** 
 at:
 <https://wandb.ai/harrison-chase/langchain_callback_demo/runs/jyxma7hu>
  

 Synced 4 W&B file(s), 2 media file(s), 6 artifact file(s) and 0 other file(s)
 

 Find logs at:
 `./wandb/run-20230318_150534-jyxma7hu/logs` 


 {"model_id": "dbdbf28fb8ed40a3a60218d2e6d1a987", "version_major": 2, "version_minor": 0}
 

 Tracking run with wandb version 0.14.0
 

 Run data is saved locally in
 `/Users/harrisonchase/workplace/langchain/docs/ecosystem/wandb/run-20230318_150550-wzy59zjq` 


 Syncing run
 **[agent](https://wandb.ai/harrison-chase/langchain_callback_demo/runs/wzy59zjq)**
 to
 [Weights & Biases](https://wandb.ai/harrison-chase/langchain_callback_demo) 
 (
 [docs](https://wandb.me/run) 
 )
   



 View project at
 <https://wandb.ai/harrison-chase/langchain_callback_demo>


 View run at
 <https://wandb.ai/harrison-chase/langchain_callback_demo/runs/wzy59zjq>








```
from langchain.agents import initialize_agent, load_tools
from langchain.agents import AgentType

```










```
# SCENARIO 3 - Agent with Tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)
agent.run(
    "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?",
    callbacks=callbacks,
)
wandb_callback.flush_tracker(agent, reset=False, finish=True)

```








```
> Entering new AgentExecutor chain...
 I need to find out who Leo DiCaprio's girlfriend is and then calculate her age raised to the 0.43 power.
Action: Search
Action Input: "Leo DiCaprio girlfriend"
Observation: DiCaprio had a steady girlfriend in Camila Morrone. He had been with the model turned actress for nearly five years, as they were first said to be dating at the end of 2017. And the now 26-year-old Morrone is no stranger to Hollywood.
Thought: I need to calculate her age raised to the 0.43 power.
Action: Calculator
Action Input: 26^0.43
Observation: Answer: 4.059182145592686

Thought: I now know the final answer.
Final Answer: Leo DiCaprio's girlfriend is Camila Morrone and her current age raised to the 0.43 power is 4.059182145592686.

> Finished chain.

```




 Waiting for W&B process to finish...
 **(success).** 


 View run
 **agent** 
 at:
 <https://wandb.ai/harrison-chase/langchain_callback_demo/runs/wzy59zjq>
  

 Synced 5 W&B file(s), 2 media file(s), 7 artifact file(s) and 0 other file(s)
 

 Find logs at:
 `./wandb/run-20230318_150550-wzy59zjq/logs` 





