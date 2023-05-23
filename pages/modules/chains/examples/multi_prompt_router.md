

路由器链：使用MultiPromptChain从多个提示中选择[#](#router-chains-selecting-from-multiple-prompts-with-multipromptchain "Permalink to this headline")
=====================================================================================================================================

本教程演示了如何使用RouterChain范例创建一个链，它动态地选择用于给定输入的提示。具体来说，我们展示了如何使用MultiPromptChain创建一个问答链，该链选择与给定问题最相关的提示，然后使用该提示回答问题。

```
from langchain.chains.router import MultiPromptChain
from langchain.llms import OpenAI

```

```
physics_template = """You are a very smart physics professor. \
You are great at answering questions about physics in a concise and easy to understand manner. \
When you don't know the answer to a question you admit that you don't know.

Here is a question:
{input}"""

math_template = """You are a very good mathematician. You are great at answering math questions. \
You are so good because you are able to break down hard problems into their component parts, \
answer the component parts, and then put them together to answer the broader question.

Here is a question:
{input}"""

```

```
prompt_infos = [
    {
        "name": "physics", 
        "description": "Good for answering questions about physics", 
        "prompt_template": physics_template
    },
    {
        "name": "math", 
        "description": "Good for answering math questions", 
        "prompt_template": math_template
    }
]

```

```
chain = MultiPromptChain.from_prompts(OpenAI(), prompt_infos, verbose=True)

```

```
print(chain.run("What is black body radiation?"))

```

```
> Entering new MultiPromptChain chain...
physics: {'input': 'What is black body radiation?'}
> Finished chain.

Black body radiation is the emission of electromagnetic radiation from a body due to its temperature. It is a type of thermal radiation that is emitted from the surface of all objects that are at a temperature above absolute zero. It is a spectrum of radiation that is influenced by the temperature of the body and is independent of the composition of the emitting material.

```

```
print(chain.run("What is the first prime number greater than 40 such that one plus the prime number is divisible by 3"))

```

```
> Entering new MultiPromptChain chain...
math: {'input': 'What is the first prime number greater than 40 such that one plus the prime number is divisible by 3'}
> Finished chain.
?

The first prime number greater than 40 such that one plus the prime number is divisible by 3 is 43. To solve this problem, we can break down the question into two parts: finding the first prime number greater than 40, and then finding a number that is divisible by 3. 

The first step is to find the first prime number greater than 40. A prime number is a number that is only divisible by 1 and itself. The next prime number after 40 is 41.

The second step is to find a number that is divisible by 3. To do this, we can add 1 to 41, which gives us 42. Now, we can check if 42 is divisible by 3. 42 divided by 3 is 14, so 42 is divisible by 3.

Therefore, the answer to the question is 43.

```

```
print(chain.run("What is the name of the type of cloud that rins"))

```

```
> Entering new MultiPromptChain chain...
None: {'input': 'What is the name of the type of cloud that rains?'}
> Finished chain.
The type of cloud that typically produces rain is called a cumulonimbus cloud. This type of cloud is characterized by its large vertical extent and can produce thunderstorms and heavy precipitation. Is there anything else you'd like to know?

```

