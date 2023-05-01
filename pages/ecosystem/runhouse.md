


 Runhouse
 [#](#runhouse "Permalink to this headline")
=======================================================



 This page covers how to use the
 [Runhouse](https://github.com/run-house/runhouse) 
 ecosystem within LangChain.
It is broken into three parts: installation and setup, LLMs, and Embeddings.
 




 Installation and Setup
 [#](#installation-and-setup "Permalink to this headline")
-----------------------------------------------------------------------------------


* Install the Python SDK with
 `pip
 

 install
 

 runhouse`
* If you’d like to use on-demand cluster, check your cloud credentials with
 `sky
 

 check`





 Self-hosted LLMs
 [#](#self-hosted-llms "Permalink to this headline")
-----------------------------------------------------------------------



 For a basic self-hosted LLM, you can use the
 `SelfHostedHuggingFaceLLM`
 class. For more
custom LLMs, you can use the
 `SelfHostedPipeline`
 parent class.
 





```
from langchain.llms import SelfHostedPipeline, SelfHostedHuggingFaceLLM

```




 For a more detailed walkthrough of the Self-hosted LLMs, see
 [this notebook](../modules/models/llms/integrations/runhouse)






 Self-hosted Embeddings
 [#](#self-hosted-embeddings "Permalink to this headline")
-----------------------------------------------------------------------------------



 There are several ways to use self-hosted embeddings with LangChain via Runhouse.
 



 For a basic self-hosted embedding from a Hugging Face Transformers model, you can use
the
 `SelfHostedEmbedding`
 class.
 





```
from langchain.llms import SelfHostedPipeline, SelfHostedHuggingFaceLLM

```




 For a more detailed walkthrough of the Self-hosted Embeddings, see
 [this notebook](../modules/models/text_embedding/examples/self-hosted)






