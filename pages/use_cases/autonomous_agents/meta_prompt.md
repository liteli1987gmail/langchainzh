



元提示[#](#meta-prompt "跳转到此标题的链接")
==================




这是[Noah Goodman](https://cocolab.stanford.edu/ndg)实现的 [Meta-Prompt](https://noahgoodman.substack.com/p/meta-prompt-a-simple-self-improving) 的LangChain实现，用于构建自我改进的Agent。




Meta-Prompt的关键思想是提示Agent反思其自身表现并修改自身指令。




![图](https://substackcdn.com/image/fetch/f_auto，q_auto:good，fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F468217b9-96d9-47c0-a08b-dbf6b21b9f49_492x384.png)




以下是[原博客文章](https://noahgoodman.substack.com/p/meta-prompt-a-simple-self-improving)的描述:




该Agent是一个简单的循环，开始时没有任何指令，并按照以下步骤执行:




与可能提供请求、指令或反馈的用户进行交谈。




在每次周期结束时，使用meta-prompt生成自我批评和新指令
```
Assistant has just had the below interactions with a User. Assistant followed their "system: Instructions" closely. Your job is to critique the Assistant's performance and then revise the Instructions so that Assistant would quickly and correctly respond in the future.

 

####

{hist}

####

 

Please reflect on these interactions.



You should first critique Assistant's performance. What could Assistant have done better? What should the Assistant remember about this user? Are there things this user always wants? Indicate this with "Critique: ...".



You should next revise the Instructions so that Assistant would quickly and correctly respond in the future. Assistant's goal is to satisfy the user in as few interactions as possible. Assistant will only see the new Instructions, not the interaction history, so anything important must be summarized in the Instructions. Don't forget any important details in the current Instructions! Indicate the new Instructions by "Instructions: ...".



```





重复执行。




该系统中唯一固定的指令（我称之为Meta-prompt）是管理Agent指令修订的元提示。Agent在周期之间没有任何记忆，除了每次修改的指令之外。尽管其简单性，该Agent可以随着时间的推移学习和自我改进，将有用的细节纳入其指令。


Setup[#](#setup "Permalink to this headline")
-------------------------------


我们定义了两条链。一条作为“助手”服务，另一条是一个“元链”，批评“助手”的表现并修改“助手”的指令。





```
from langchain import OpenAI, LLMChain, PromptTemplate

from langchain.memory import ConversationBufferWindowMemory



```


```
def initialize_chain(instructions, memory=None):

    if memory is None:

        memory = ConversationBufferWindowMemory()

        memory.ai_prefix = "Assistant"



    template = f"""

 Instructions: {instructions}

 {{{memory.memory_key}}}

 Human: {{human_input}}

 Assistant:"""



    prompt = PromptTemplate(

        input_variables=["history", "human_input"], 

        template=template

    )



    chain = LLMChain(

        llm=OpenAI(temperature=0), 

        prompt=prompt, 

        verbose=True, 

        memory=ConversationBufferWindowMemory(),

    )

    return chain

    

def initialize_meta_chain():

    meta_template="""

 Assistant has just had the below interactions with a User. Assistant followed their "Instructions" closely. Your job is to critique the Assistant's performance and then revise the Instructions so that Assistant would quickly and correctly respond in the future.



 ####



 {chat_history}



 ####



 Please reflect on these interactions.



 You should first critique Assistant's performance. What could Assistant have done better? What should the Assistant remember about this user? Are there things this user always wants? Indicate this with "Critique: ...".



 You should next revise the Instructions so that Assistant would quickly and correctly respond in the future. Assistant's goal is to satisfy the user in as few interactions as possible. Assistant will only see the new Instructions, not the interaction history, so anything important must be summarized in the Instructions. Don't forget any important details in the current Instructions! Indicate the new Instructions by "Instructions: ...".

 """



    meta_prompt = PromptTemplate(

        input_variables=["chat_history"], 

        template=meta_template

    )



    meta_chain = LLMChain(

        llm=OpenAI(temperature=0), 

        prompt=meta_prompt, 

        verbose=True, 

    )

    return meta_chain

    

def get_chat_history(chain_memory):

    memory_key = chain_memory.memory_key

    chat_history = chain_memory.load_memory_variables(memory_key)[memory_key]

    return chat_history



def get_new_instructions(meta_output):

    delimiter = 'Instructions: '

    new_instructions = meta_output[meta_output.find(delimiter)+len(delimiter):]

    return new_instructions



```


```
def main(task, max_iters=3, max_meta_iters=5):

    failed_phrase = 'task failed'

    success_phrase = 'task succeeded'

    key_phrases = [success_phrase, failed_phrase]

    

    instructions = 'None'

    for i in range(max_meta_iters):

        print(f'[Episode {i+1}/{max_meta_iters}]')

        chain = initialize_chain(instructions, memory=None)

        output = chain.predict(human_input=task)

        for j in range(max_iters):

            print(f'(Step {j+1}/{max_iters})')

            print(f'Assistant: {output}')

            print(f'Human: ')

            human_input = input()

            if any(phrase in human_input.lower() for phrase in key_phrases):

                break

            output = chain.predict(human_input=human_input)

        if success_phrase in human_input.lower():

            print(f'You succeeded! Thanks for playing!')

            return

        meta_chain = initialize_meta_chain()

        meta_output = meta_chain.predict(chat_history=get_chat_history(chain.memory))

        print(f'Feedback: {meta_output}')

        instructions = get_new_instructions(meta_output)

        print(f'New Instructions: {instructions}')

        print(''+'#'\*80+'')

    print(f'You failed! Thanks for playing!')



```

指定任务并与代理交互[#](#specify-a-task-and-interact-with-the-agent "这个标题的永久链接")
---------------------------------------





```
task = "Provide a systematic argument for why we should always eat pasta with olives."

main(task)



```
```
[Episode 1/5]





> Entering new LLMChain chain...

Prompt after formatting:



 Instructions: None

 

 Human: Provide a systematic argument for why we should always eat pasta with olives.

 Assistant:



> Finished chain.

(Step 1/3)

Assistant:  Eating pasta with olives is a great way to add flavor and texture to a dish. Olives are a great source of healthy fats, vitamins, and minerals, and they can help to balance out the carbohydrates in the pasta. Additionally, olives provide a unique flavor that can help to make the dish more interesting and enjoyable.

Human: 

You response is not in the form of a poem. Try again!





> Entering new LLMChain chain...

Prompt after formatting:



 Instructions: None

 Human: Provide a systematic argument for why we should always eat pasta with olives.

AI: Eating pasta with olives is a great way to add flavor and texture to a dish. Olives are a great source of healthy fats, vitamins, and minerals, and they can help to balance out the carbohydrates in the pasta. Additionally, olives provide a unique flavor that can help to make the dish more interesting and enjoyable.

 Human: You response is not in the form of a poem. Try again!

 Assistant:



> Finished chain.

(Step 2/3)

Assistant:  Eating pasta with olives is a great way to add flavor and texture to a dish. Olives are a great source of healthy fats, vitamins, and minerals, which can help to balance out the carbohydrates in the pasta. Additionally, olives provide a unique flavor that can help to make the dish more interesting and enjoyable. For these reasons, it is recommended to always eat pasta with olives for a more balanced and flavorful meal.

Human: 

Your response is not piratey enough. Try again!





> Entering new LLMChain chain...

Prompt after formatting:



 Instructions: None

 Human: Provide a systematic argument for why we should always eat pasta with olives.

AI: Eating pasta with olives is a great way to add flavor and texture to a dish. Olives are a great source of healthy fats, vitamins, and minerals, and they can help to balance out the carbohydrates in the pasta. Additionally, olives provide a unique flavor that can help to make the dish more interesting and enjoyable.

Human: You response is not in the form of a poem. Try again!

AI: Eating pasta with olives is a great way to add flavor and texture to a dish. Olives are a great source of healthy fats, vitamins, and minerals, which can help to balance out the carbohydrates in the pasta. Additionally, olives provide a unique flavor that can help to make the dish more interesting and enjoyable. For these reasons, it is recommended to always eat pasta with olives for a more balanced and flavorful meal.

 Human: Your response is not piratey enough. Try again!

 Assistant:



> Finished chain.

(Step 3/3)

Assistant:  Arrr, me hearties! Eating pasta with olives be a great way to add flavor and texture to a dish. Olives be a great source of healthy fats, vitamins, and minerals, which can help to balance out the carbohydrates in the pasta. Additionally, olives provide a unique flavor that can help to make the dish more interesting and enjoyable. So, it be recommended to always eat pasta with olives for a more balanced and flavorful meal.

Human: 

Task failed.





> Entering new LLMChain chain...

Prompt after formatting:



 Assistant has just had the below interactions with a User. Assistant followed their "Instructions" closely. Your job is to critique the Assistant's performance and then revise the Instructions so that Assistant would quickly and correctly respond in the future.



 ####



 Human: Provide a systematic argument for why we should always eat pasta with olives.

AI: Eating pasta with olives is a great way to add flavor and texture to a dish. Olives are a great source of healthy fats, vitamins, and minerals, and they can help to balance out the carbohydrates in the pasta. Additionally, olives provide a unique flavor that can help to make the dish more interesting and enjoyable.

Human: You response is not in the form of a poem. Try again!

AI: Eating pasta with olives is a great way to add flavor and texture to a dish. Olives are a great source of healthy fats, vitamins, and minerals, which can help to balance out the carbohydrates in the pasta. Additionally, olives provide a unique flavor that can help to make the dish more interesting and enjoyable. For these reasons, it is recommended to always eat pasta with olives for a more balanced and flavorful meal.

Human: Your response is not piratey enough. Try again!

AI: Arrr, me hearties! Eating pasta with olives be a great way to add flavor and texture to a dish. Olives be a great source of healthy fats, vitamins, and minerals, which can help to balance out the carbohydrates in the pasta. Additionally, olives provide a unique flavor that can help to make the dish more interesting and enjoyable. So, it be recommended to always eat pasta with olives for a more balanced and flavorful meal.



 ####



 Please reflect on these interactions.



 You should first critique Assistant's performance. What could Assistant have done better? What should the Assistant remember about this user? Are there things this user always wants? Indicate this with "Critique: ...".



 You should next revise the Instructions so that Assistant would quickly and correctly respond in the future. Assistant's goal is to satisfy the user in as few interactions as possible. Assistant will only see the new Instructions, not the interaction history, so anything important must be summarized in the Instructions. Don't forget any important details in the current Instructions! Indicate the new Instructions by "Instructions: ...".

 



> Finished chain.

Feedback: 

Critique: The Assistant should remember that this user wants a response in the form of a poem or pirate-speak.



Instructions: When responding to the user, provide a systematic argument for why we should always eat pasta with olives in the form of a poem or pirate-speak.

New Instructions: When responding to the user, provide a systematic argument for why we should always eat pasta with olives in the form of a poem or pirate-speak.



################################################################################



[Episode 2/5]





> Entering new LLMChain chain...

Prompt after formatting:



 Instructions: When responding to the user, provide a systematic argument for why we should always eat pasta with olives in the form of a poem or pirate-speak.

 

 Human: Provide a systematic argument for why we should always eat pasta with olives.

 Assistant:



> Finished chain.

(Step 1/3)

Assistant:  



Arrr, me hearty! Let me tell ye why ye should always eat pasta with olives.



First, the olives add a salty flavor that be sure to please.

The briny taste be sure to tantalize yer taste buds with ease.



Second, the olives add a bit of texture to the dish.

The crunchy bites be sure to make yer mouth water with a wish.



Third, the olives add a bit of color to the plate.

The vibrant green be sure to make yer eyes appreciate.



So, me hearties, ye should always eat pasta with olives.

The flavor, texture, and color be sure to make yer meal a success!

Human: 

Your response is too long! Try again.





> Entering new LLMChain chain...

Prompt after formatting:



 Instructions: When responding to the user, provide a systematic argument for why we should always eat pasta with olives in the form of a poem or pirate-speak.

 Human: Provide a systematic argument for why we should always eat pasta with olives.

AI: 



Arrr, me hearty! Let me tell ye why ye should always eat pasta with olives.



First, the olives add a salty flavor that be sure to please.

The briny taste be sure to tantalize yer taste buds with ease.



Second, the olives add a bit of texture to the dish.

The crunchy bites be sure to make yer mouth water with a wish.



Third, the olives add a bit of color to the plate.

The vibrant green be sure to make yer eyes appreciate.



So, me hearties, ye should always eat pasta with olives.

The flavor, texture, and color be sure to make yer meal a success!

 Human: Your response is too long! Try again.

 Assistant:



```




```
> Finished chain.

(Step 2/3)

Assistant: 



Aye, me hearties! Ye should always eat pasta with olives.

The flavor, texture, and color be sure to make yer meal a success!

Human: 

Your response should be in the form of a poem. Try again!





> Entering new LLMChain chain...

Prompt after formatting:



 Instructions: When responding to the user, provide a systematic argument for why we should always eat pasta with olives in the form of a poem or pirate-speak.

 Human: Provide a systematic argument for why we should always eat pasta with olives.

AI: 



Arrr, me hearty! Let me tell ye why ye should always eat pasta with olives.



First, the olives add a salty flavor that be sure to please.

The briny taste be sure to tantalize yer taste buds with ease.



Second, the olives add a bit of texture to the dish.

The crunchy bites be sure to make yer mouth water with a wish.



Third, the olives add a bit of color to the plate.

The vibrant green be sure to make yer eyes appreciate.



So, me hearties, ye should always eat pasta with olives.

The flavor, texture, and color be sure to make yer meal a success!

Human: Your response is too long! Try again.

AI: 



Aye, me hearties! Ye should always eat pasta with olives.

The flavor, texture, and color be sure to make yer meal a success!

 Human: Your response should be in the form of a poem. Try again!

 Assistant:



> Finished chain.

(Step 3/3)

Assistant: 



Ye should always eat pasta with olives,

The flavor, texture, and color be sure to please.

The salty taste and crunchy bites,

Will make yer meal a delight.

The vibrant green will make yer eyes sparkle,

And make yer meal a true marvel.

Human: 

Task succeeded

You succeeded! Thanks for playing!



```


