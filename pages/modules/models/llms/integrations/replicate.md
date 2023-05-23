
Replicate
=============================


> 
> [Replicate](https://replicate.com/blog/machine-learning-needs-better-tools)在云端运行机器学习模型。我们拥有一系列开源模型，只需几行代码即可运行。如果您正在构建自己的机器学习模型，Replicate可以轻松实现大规模部署。
> 
> 
> 

这个例子介绍了如何使用LangChain与`Replicate` [模型](https://replicate.com/explore)进行交互。

设置[#](#setup "永久链接到此标题")
------------------------

要运行此教程电脑，您需要创建一个[Replicate](https://replicate.com)账户并安装[replicate python客户端](https://github.com/replicate/replicate-python)。

```
!pip install replicate

```

```
# get a token: https://replicate.com/account

from getpass import getpass

REPLICATE_API_TOKEN = getpass()

```

```
 ········

```

```
import os

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

```

```
from langchain.llms import Replicate
from langchain import PromptTemplate, LLMChain

```

调用模型[#](#calling-a-model "永久链接到此标题")
------------------------------------

Find a model on the [replicate explore page](https://replicate.com/explore), and then paste in the model name and version in this format: model_name/version

For example, for this [dolly model](https://replicate.com/replicate/dolly-v2-12b), click on the API tab. The model name/version would be: `replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5`

Only the `model` param is required, but we can add other model params when initializing.

For example, if we were running stable diffusion and wanted to change the image dimensions:

```
Replicate(model="stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf", input={'image_dimensions': '512x512'})

```

*Note that only the first output of a model will be returned.*

```
llm = Replicate(model="replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5")

```

```
prompt = """
Answer the following yes/no question by reasoning step by step. 
Can a dog drive a car?
"""
llm(prompt)

```

```
'The legal driving age of dogs is 2. Cars are designed for humans to drive. Therefore, the final answer is yes.'

```

We can call any replicate model using this syntax. For example, we can call stable diffusion.

```
text2image = Replicate(model="stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf", 
                       input={'image_dimensions': '512x512'})

```

```
image_output = text2image("A cat riding a motorcycle by Picasso")
image_output

```

```
'https://replicate.delivery/pbxt/Cf07B1zqzFQLOSBQcKG7m9beE74wf7kuip5W9VxHJFembefKE/out-0.png'

```

The model spits out a URL. Let’s render it.

```
from PIL import Image
import requests
from io import BytesIO

response = requests.get(image_output)
img = Image.open(BytesIO(response.content))

img

```


Chaining Calls[#](#chaining-calls "Permalink to this headline")
---------------------------------------------------------------

The whole point of langchain is to… chain! Here’s an example of how do that.

```
from langchain.chains import SimpleSequentialChain

```

First, let’s define the LLM for this model as a flan-5, and text2image as a stable diffusion model.

```
dolly_llm = Replicate(model="replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5")
text2image = Replicate(model="stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")

```

First prompt in the chain

```
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

chain = LLMChain(llm=dolly_llm, prompt=prompt)

```

Second prompt to get the logo for company description

```
second_prompt = PromptTemplate(
    input_variables=["company_name"],
    template="Write a description of a logo for this company: {company_name}",
)
chain_two = LLMChain(llm=dolly_llm, prompt=second_prompt)

```

第三个提示，根据第二个提示输出的描述来创建图片

```
third_prompt = PromptTemplate(
    input_variables=["company_logo_description"],
    template="{company_logo_description}",
)
chain_three = LLMChain(llm=text2image, prompt=third_prompt)

```

现在让我们运行它！

```
# Run the chain specifying only the input variable for the first chain.
overall_chain = SimpleSequentialChain(chains=[chain, chain_two, chain_three], verbose=True)
catchphrase = overall_chain.run("colorful socks")
print(catchphrase)

```

```
> Entering new SimpleSequentialChain chain...
novelty socks
todd & co.
https://replicate.delivery/pbxt/BedAP1PPBwXFfkmeD7xDygXO4BcvApp1uvWOwUdHM4tcQfvCB/out-0.png

> Finished chain.
https://replicate.delivery/pbxt/BedAP1PPBwXFfkmeD7xDygXO4BcvApp1uvWOwUdHM4tcQfvCB/out-0.png

```

```
response = requests.get("https://replicate.delivery/pbxt/eq6foRJngThCAEBqse3nL3Km2MBfLnWQNd0Hy2SQRo2LuprCB/out-0.png")
img = Image.open(BytesIO(response.content))
img

```


