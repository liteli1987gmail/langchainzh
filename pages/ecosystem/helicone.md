

Helicone[#](#helicone "跳转到标题")
==============================

本页介绍如何在LangChain中使用[Helicone](https://helicone.ai)生态系统。

什么是Helicone?[#](#what-is-helicone "跳转到标题")
------------------------------------------

Helicone是一个[开源](https://github.com/Helicone/helicone)的可观察平台，代理您的OpenAI流量，并为您提供有关您的开支、延迟和使用情况的关键见解。



快速入门[#](#quick-start "跳转到标题")
-----------------------------

在您的LangChain环境中，您只需添加以下参数。

```
export OPENAI_API_BASE="https://oai.hconeai.com/v1"

```

现在前往[helicone.ai](https://helicone.ai/onboarding?step=2)创建您的帐户，并在我们的仪表板中添加您的OpenAI API密钥以查看您的日志。



如何启用Helicone缓存[#](#how-to-enable-helicone-caching "跳转到标题")
----------------------------------------------------------

```
from langchain.llms import OpenAI
import openai
openai.api_base = "https://oai.hconeai.com/v1"

llm = OpenAI(temperature=0.9, headers={"Helicone-Cache-Enabled": "true"})
text = "What is a helicone?"
print(llm(text))

```

[Helicone缓存文档](https://docs.helicone.ai/advanced-usage/caching)

如何使用Helicone自定义属性[#](#how-to-use-helicone-custom-properties "Permalink to this headline")
-----------------------------------------------------------------------------------------

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

[Helicone属性文档](https://docs.helicone.ai/advanced-usage/custom-properties)

