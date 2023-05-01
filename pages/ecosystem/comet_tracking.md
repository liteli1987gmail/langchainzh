


 Comet
 [#](#comet "Permalink to this headline")
=================================================






 In this guide we will demonstrate how to track your Langchain Experiments, Evaluation Metrics, and LLM Sessions with
 [Comet](https://www.comet.com/site/?utm_source=langchain&utm_medium=referral&utm_campaign=comet_notebook) 
 .
 


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hwchase17/langchain/blob/master/docs/ecosystem/comet_tracking.ipynb)

**Example Project:** 
[Comet with LangChain](https://www.comet.com/examples/comet-example-langchain/view/b5ZThK6OFdhKWVSP3fDfRtrNF/panels?utm_source=langchain&utm_medium=referral&utm_campaign=comet_notebook) 





 Install Comet and Dependencies
 [#](#install-comet-and-dependencies "Permalink to this headline")
---------------------------------------------------------------------------------------------------







```
%pip install comet_ml langchain openai google-search-results spacy textstat pandas

import sys
!{sys.executable} -m spacy download en_core_web_sm

```








 Initialize Comet and Set your Credentials
 [#](#initialize-comet-and-set-your-credentials "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------



 You can grab your
 [Comet API Key here](https://www.comet.com/signup?utm_source=langchain&utm_medium=referral&utm_campaign=comet_notebook) 
 or click the link after initializing Comet
 







```
import comet_ml

comet_ml.init(project_name="comet-example-langchain")

```








 Set OpenAI and SerpAPI credentials
 [#](#set-openai-and-serpapi-credentials "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------



 You will need an
 [OpenAI API Key](https://platform.openai.com/account/api-keys) 
 and a
 [SerpAPI API Key](https://serpapi.com/dashboard) 
 to run the following examples
 







```
import os

os.environ["OPENAI_API_KEY"] = "..."
#os.environ["OPENAI_ORGANIZATION"] = "..."
os.environ["SERPAPI_API_KEY"] = "..."

```








 Scenario 1: Using just an LLM
 [#](#scenario-1-using-just-an-llm "Permalink to this headline")
------------------------------------------------------------------------------------------------







```
from datetime import datetime

from langchain.callbacks import CometCallbackHandler, StdOutCallbackHandler
from langchain.llms import OpenAI

comet_callback = CometCallbackHandler(
    project_name="comet-example-langchain",
    complexity_metrics=True,
    stream_logs=True,
    tags=["llm"],
    visualizations=["dep"],
)
callbacks = [StdOutCallbackHandler(), comet_callback]
llm = OpenAI(temperature=0.9, callbacks=callbacks, verbose=True)

llm_result = llm.generate(["Tell me a joke", "Tell me a poem", "Tell me a fact"] \* 3)
print("LLM result", llm_result)
comet_callback.flush_tracker(llm, finish=True)

```








 Scenario 2: Using an LLM in a Chain
 [#](#scenario-2-using-an-llm-in-a-chain "Permalink to this headline")
------------------------------------------------------------------------------------------------------------







```
from langchain.callbacks import CometCallbackHandler, StdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

comet_callback = CometCallbackHandler(
    complexity_metrics=True,
    project_name="comet-example-langchain",
    stream_logs=True,
    tags=["synopsis-chain"],
)
callbacks = [StdOutCallbackHandler(), comet_callback]
llm = OpenAI(temperature=0.9, callbacks=callbacks)

template = """You are a playwright. Given the title of play, it is your job to write a synopsis for that title.
Title: {title}
Playwright: This is a synopsis for the above play:"""
prompt_template = PromptTemplate(input_variables=["title"], template=template)
synopsis_chain = LLMChain(llm=llm, prompt=prompt_template, callbacks=callbacks)

test_prompts = [{"title": "Documentary about Bigfoot in Paris"}]
print(synopsis_chain.apply(test_prompts))
comet_callback.flush_tracker(synopsis_chain, finish=True)

```








 Scenario 3: Using An Agent with Tools
 [#](#scenario-3-using-an-agent-with-tools "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------







```
from langchain.agents import initialize_agent, load_tools
from langchain.callbacks import CometCallbackHandler, StdOutCallbackHandler
from langchain.llms import OpenAI

comet_callback = CometCallbackHandler(
    project_name="comet-example-langchain",
    complexity_metrics=True,
    stream_logs=True,
    tags=["agent"],
)
callbacks = [StdOutCallbackHandler(), comet_callback]
llm = OpenAI(temperature=0.9, callbacks=callbacks)

tools = load_tools(["serpapi", "llm-math"], llm=llm, callbacks=callbacks)
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    callbacks=callbacks,
    verbose=True,
)
agent.run(
    "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"
)
comet_callback.flush_tracker(agent, finish=True)

```








 Scenario 4: Using Custom Evaluation Metrics
 [#](#scenario-4-using-custom-evaluation-metrics "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------



 The
 `CometCallbackManager`
 also allows you to define and use Custom Evaluation Metrics to assess generated outputs from your model. Let’s take a look at how this works.
 



 In the snippet below, we will use the
 [ROUGE](https://huggingface.co/spaces/evaluate-metric/rouge) 
 metric to evaluate the quality of a generated summary of an input prompt.
 







```
%pip install rouge-score

```










```
from rouge_score import rouge_scorer

from langchain.callbacks import CometCallbackHandler, StdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


class Rouge:
    def __init__(self, reference):
        self.reference = reference
        self.scorer = rouge_scorer.RougeScorer(["rougeLsum"], use_stemmer=True)

    def compute_metric(self, generation, prompt_idx, gen_idx):
        prediction = generation.text
        results = self.scorer.score(target=self.reference, prediction=prediction)

        return {
            "rougeLsum_score": results["rougeLsum"].fmeasure,
            "reference": self.reference,
        }


reference = """
The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building.
It was the first structure to reach a height of 300 metres.

It is now taller than the Chrysler Building in New York City by 5.2 metres (17 ft)
Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France .
"""
rouge_score = Rouge(reference=reference)

template = """Given the following article, it is your job to write a summary.
Article:
{article}
Summary: This is the summary for the above article:"""
prompt_template = PromptTemplate(input_variables=["article"], template=template)

comet_callback = CometCallbackHandler(
    project_name="comet-example-langchain",
    complexity_metrics=False,
    stream_logs=True,
    tags=["custom_metrics"],
    custom_metrics=rouge_score.compute_metric,
)
callbacks = [StdOutCallbackHandler(), comet_callback]
llm = OpenAI(temperature=0.9)

synopsis_chain = LLMChain(llm=llm, prompt=prompt_template)

test_prompts = [
    {
        "article": """
 The tower is 324 metres (1,063 ft) tall, about the same height as
 an 81-storey building, and the tallest structure in Paris. Its base is square,
 measuring 125 metres (410 ft) on each side.
 During its construction, the Eiffel Tower surpassed the
 Washington Monument to become the tallest man-made structure in the world,
 a title it held for 41 years until the Chrysler Building
 in New York City was finished in 1930.

 It was the first structure to reach a height of 300 metres.
 Due to the addition of a broadcasting aerial at the top of the tower in 1957,
 it is now taller than the Chrysler Building by 5.2 metres (17 ft).

 Excluding transmitters, the Eiffel Tower is the second tallest
 free-standing structure in France after the Millau Viaduct.
 """
    }
]
print(synopsis_chain.apply(test_prompts, callbacks=callbacks))
comet_callback.flush_tracker(synopsis_chain, finish=True)

```








