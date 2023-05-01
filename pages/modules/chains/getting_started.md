

开始
====================================================================



在本教程中，我们将学习如何在 LangChain 创建简单的连锁店。我们将学习如何创建一个链，向其添加组件，并运行它。
 



在本教程中，我们将介绍:
 


* 使用简单的 LLM 链
* 创建连续链
* 创建定制链




为什么我们需要锁链？
----------------------------------------------------------------------------------



链允许我们将多个组件组合在一起，创建一个单一的、一致的应用程序。例如，我们可以创建一个链，该链接接受用户输入，使用 PromptTemplate 对其进行格式化，然后将格式化后的响应传递给 LLM。我们可以通过将多个链组合在一起，或者通过将链与其他组件组合在一起，来构建更复杂的链。
 





快速开始: 使用`LLMChain`
----------------------------------------------------------------------------------------------



LLMChain 是一个简单的链，它接受一个提示模板，使用用户输入对其进行格式化，并从 LLM 返回响应。

要使用 LLMChain，首先创建一个提示模板。
 







```
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

```






现在我们可以创建一个非常简单的链，它将接受用户输入，用它格式化提示符，然后将其发送到 LLM。
 







```
from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain only specifying the input variable.
print(chain.run("colorful socks"))

```








```
SockSplash!

```






你也可以在 LLMChain 中使用聊天模型:
 







```
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
human_message_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="What is a good name for a company that makes {product}?",
            input_variables=["product"],
        )
    )
chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])
chat = ChatOpenAI(temperature=0.9)
chain = LLMChain(llm=chat, prompt=chat_prompt_template)
print(chain.run("colorful socks"))

```








```
Rainbow Sox Co.

```








调用链的不同方式
-------------------------------------------------------------------------------------------------------



从 Chain 继承的所有类都提供了一些运行链逻辑的方法。最直接的方法是使用
 `__call__`
 :
 







```
chat = ChatOpenAI(temperature=0)
prompt_template = "Tell me a {adjective} joke"
llm_chain = LLMChain(
    llm=chat,
    prompt=PromptTemplate.from_template(prompt_template)
)

llm_chain(inputs={"adjective":"corny"})

```








```
{'adjective': 'corny',
 'text': 'Why did the tomato turn red? Because it saw the salad dressing!'}

```






默认情况下，`_ _ call _ _` 返回输入和输出键值。通过将 `return _ only _ output` 设置为`True`，可以将其配置为只返回输出键值。
 







```
llm_chain("corny", return_only_outputs=True)

```








```
{'text': 'Why did the tomato turn red? Because it saw the salad dressing!'}

```






如果 Chain 只输出一个输出键(即在 output _ key 中只有一个元素) ，则可以使用 run 方法。注意 run 输出的是字符串而不是字典。
 







```
# llm_chain only has one output key, so we can use run
llm_chain.output_keys

```








```
['text']

```










```
llm_chain.run({"adjective":"corny"})

```








```
'Why did the tomato turn red? Because it saw the salad dressing!'

```






对于一个输入键，您可以直接输入字符串，而无需指定输入映射。
 







```
# These two are equivalent
llm_chain.run({"adjective":"corny"})
llm_chain.run("corny")

# These two are also equivalent
llm_chain("corny")
llm_chain({"adjective":"corny"})

```








```
{'adjective': 'corny',
 'text': 'Why did the tomato turn red? Because it saw the salad dressing!'}

```






提示: 您可以通过 run 方法轻松地将 Chain 对象作为工具集成到您的 Agent 中。这里有一个例子。
 [here](../agents/tools/custom_tools)
 .
 





向链中添加内存
-------------------------------------------------------------------------------



Chain 支持将 BaseMemory 对象作为其内存参数，允许 Chain 对象跨多个调用持久存储数据。换句话说，它使 Chain 成为一个有状态对象。
 







```
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

conversation = ConversationChain(
    llm=chat,
    memory=ConversationBufferMemory()
)

conversation.run("Answer briefly. What are the first 3 colors of a rainbow?")
# -> The first three colors of a rainbow are red, orange, and yellow.
conversation.run("And the next 4?")
# -> The next four colors of a rainbow are green, blue, indigo, and violet.

```








```
'The next four colors of a rainbow are green, blue, indigo, and violet.'

```






实际上，BaseMemory 定义了一个长链存储内存的接口。它允许通过 load _ memory _ variable 方法读取存储的数据，并通过 save _ context 方法存储新数据。你可以在内存部分了解更多。
 [Memory](../memory/getting_started)
 





调试链
-------------------------------------------------------------



因为大多数 Chain 对象都涉及大量的输入提示预处理和 LLM 输出后处理，所以很难单独从它的输出调试 Chain 对象。如果详细设置为 True，将在 Chain 对象运行时打印出它的一些内部状态。
 







```
conversation = ConversationChain(
    llm=chat,
    memory=ConversationBufferMemory(),
    verbose=True
)
conversation.run("What is ChatGPT?")

```








```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

Human: What is ChatGPT?
AI:

> Finished chain.

```






```
'ChatGPT is an AI language model developed by OpenAI. It is based on the GPT-3 architecture and is capable of generating human-like responses to text prompts. ChatGPT has been trained on a massive amount of text data and can understand and respond to a wide range of topics. It is often used for chatbots, virtual assistants, and other conversational AI applications.'

```








 Combine chains with the
 `SequentialChain`
-----------------------------------------------------------------------------------------------------------------------



调用语言模型之后的下一步是对语言模型进行一系列调用。我们可以使用序列链来实现这一点，序列链是按照预定义的顺序执行链接的链。具体来说，我们将使用 SimpleSequentialChain。这是最简单的顺序链类型，其中每个步骤都有一个输入/输出，一个步骤的输出是下一个步骤的输入。
 



在本教程中，我们的顺序链将:

首先，为产品创建一个公司名称。我们将重用之前初始化的 LLMChain 来创建这个公司名称。

然后，为产品创建一个口号。我们将初始化一个新的 LLMChain 来创建这个口号，如下所示。







```
second_prompt = PromptTemplate(
    input_variables=["company_name"],
    template="Write a catchphrase for the following company: {company_name}",
)
chain_two = LLMChain(llm=llm, prompt=second_prompt)

```






现在我们可以组合这两个 LLMChains，这样我们就可以在一个步骤中创建一个公司名称和一个口号。
 







```
from langchain.chains import SimpleSequentialChain
overall_chain = SimpleSequentialChain(chains=[chain, chain_two], verbose=True)

# Run the chain specifying only the input variable for the first chain.
catchphrase = overall_chain.run("colorful socks")
print(catchphrase)

```








```
> Entering new SimpleSequentialChain chain...
Rainbow Socks Co.


"Step into Color with Rainbow Socks!"

> Finished chain.


"Step into Color with Rainbow Socks!"

```








类创建自定义链`Chain`类
-------------------------------------------------------------------------------------------------------------------------------



LangChain 提供了很多现成的链接，但是有时候您可能想要为您的特定用例创建一个自定义链接。对于此示例，我们将创建一个自定义链，用于连接2个 LLMChains 的输出。

为了创建自定义链:

首先从 Chain 类的子类化开始,

填写 input _ key 和 output _ key 属性,

添加显示如何执行链的 _ call 方法。

下面的例子说明了这些步骤:
 







```
from langchain.chains import LLMChain
from langchain.chains.base import Chain

from typing import Dict, List


class ConcatenateChain(Chain):
    chain_1: LLMChain
    chain_2: LLMChain

    @property
    def input_keys(self) -> List[str]:
        # Union of the input keys of the two chains.
        all_input_vars = set(self.chain_1.input_keys).union(set(self.chain_2.input_keys))
        return list(all_input_vars)

    @property
    def output_keys(self) -> List[str]:
        return ['concat_output']

    def _call(self, inputs: Dict[str, str]) -> Dict[str, str]:
        output_1 = self.chain_1.run(inputs)
        output_2 = self.chain_2.run(inputs)
        return {'concat_output': output_1 + output_2}

```






就是这样! 想了解更多关于如何使用链条做一些很酷的事情的细节，请查看链条使用指南。
 







```
prompt_1 = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
chain_1 = LLMChain(llm=llm, prompt=prompt_1)

prompt_2 = PromptTemplate(
    input_variables=["product"],
    template="What is a good slogan for a company that makes {product}?",
)
chain_2 = LLMChain(llm=llm, prompt=prompt_2)

concat_chain = ConcatenateChain(chain_1=chain_1, chain_2=chain_2)
concat_output = concat_chain.run("colorful socks")
print(f"Concatenated output:\n{concat_output}")

```








```
Concatenated output:


Socktastic Colors.

"Put Some Color in Your Step!"

```






 That’s it! For more details about how to do cool things with Chains, check out the
 [how-to guide](how_to_guides)
 for chains.
 





