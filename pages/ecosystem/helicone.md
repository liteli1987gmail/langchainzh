


 Helicone
 [#](#helicone "Permalink to this headline")
=======================================================



 This page covers how to use the
 [Helicone](https://helicone.ai) 
 ecosystem within LangChain.
 




 What is Helicone?
 [#](#what-is-helicone "Permalink to this headline")
------------------------------------------------------------------------



 Helicone is an
 [open source](https://github.com/Helicone/helicone) 
 observability platform that proxies your OpenAI traffic and provides you key insights into your spend, latency and usage.
 









 Quick start
 [#](#quick-start "Permalink to this headline")
-------------------------------------------------------------



 With your LangChain environment you can just add the following parameter.
 





```
export OPENAI_API_BASE="https://oai.hconeai.com/v1"

```




 Now head over to
 [helicone.ai](https://helicone.ai/onboarding?step=2) 
 to create your account, and add your OpenAI API key within our dashboard to view your logs.
 










 How to enable Helicone caching
 [#](#how-to-enable-helicone-caching "Permalink to this headline")
---------------------------------------------------------------------------------------------------





```
from langchain.llms import OpenAI
import openai
openai.api_base = "https://oai.hconeai.com/v1"

llm = OpenAI(temperature=0.9, headers={"Helicone-Cache-Enabled": "true"})
text = "What is a helicone?"
print(llm(text))

```




[Helicone caching docs](https://docs.helicone.ai/advanced-usage/caching) 






 How to use Helicone custom properties
 [#](#how-to-use-helicone-custom-properties "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------





```
from langchain.llms import OpenAI
import openai
openai.api_base = "https://oai.hconeai.com/v1"

llm = OpenAI(temperature=0.9, headers={
        "Helicone-Property-Session": "24",
        "Helicone-Property-Conversation": "support_issue_2",
        "Helicone-Property-App": "mobile",
      })
text = "What is a helicone?"
print(llm(text))

```




[Helicone property docs](https://docs.helicone.ai/advanced-usage/custom-properties) 






