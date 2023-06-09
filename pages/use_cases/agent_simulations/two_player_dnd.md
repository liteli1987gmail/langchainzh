



双人龙与地下城 (Two-Player Dungeons & Dragons)
===============================





本说明书演示了如何使用来自 [CAMEL](https://www.camel-ai.org/) 的概念来模拟一个有主角和地牢主管的角色扮演游戏。为了模拟这个游戏，我们创建了一个 `DialogueSimulator` 类，它协调了两个代理之间的对话。


导入 LangChain 相关模块 (Import LangChain related modules)
-------------------





```

from typing import List, Dict, Callable

from langchain.chat_models import ChatOpenAI

from langchain.schema import (

    HumanMessage,

    SystemMessage,

)



```

`DialogueAgent` 类 (DialogueAgent class)
---------





`DialogueAgent` 类是 `ChatOpenAI` 模型的一个简单包装器，通过将消息连接为字符串来存储 `dialogue_agent` 的视角中的消息历史记录。




It exposes two methods:





* `send()` 方法将 ChatModel 应用于消息历史记录，并返回消息字符串* `receive(name message)` 方法将由 `name` 说出的 `message` 添加到消息历史记录中
* `receive(name, message)`: adds the `message` spoken by `name` to message history





```

class DialogueAgent:

    def __init__(

        self,

        name: str,

        system_message: SystemMessage,

        model: ChatOpenAI,

    ) -> None:

        self.name = name

        self.system_message = system_message

        self.model = model

        self.prefix = f"{self.name}: "

        self.reset()

        

    def reset(self):

        self.message_history = ["Here is the conversation so far."]



    def send(self) -> str:

 """

 Applies the chatmodel to the message history

 and returns the message string

 """

        message = self.model(

            [

                self.system_message,

                HumanMessage(content="".join(self.message_history + [self.prefix])),

            ]

        )

        return message.content



    def receive(self, name: str, message: str) -> None:

 """

 Concatenates {message} spoken by {name} into message history

 """

        self.message_history.append(f"{name}: {message}")



```

`DialogueSimulator` class[#](#dialoguesimulator-class "Permalink to this headline")

-----------------

`DialogueSimulator` 类采用代理列表。在每个步骤中，它执行以下操作 :

1. 选择下一位发言人
2. 呼叫下一位发言者发送消息
3. 将消息广播给所有其他代理
4. 更新计步器。下一位发言者的选择可以作为任何函数来实现，但在这种情况下，我们只是循环遍历代理


```
class DialogueSimulator:

    def __init__(

        self,

        agents: List[DialogueAgent],

        selection_function: Callable[[int, List[DialogueAgent]], int],

    ) -> None:

        self.agents = agents

        self._step = 0

        self.select_next_speaker = selection_function

        

    def reset(self):

        for agent in self.agents:

            agent.reset()



    def inject(self, name: str, message: str):

 """

 Initiates the conversation with a {message} from {name}

 """

        for agent in self.agents:

            agent.receive(name, message)



        # increment time

        self._step += 1



    def step(self) -> tuple[str, str]:

        # 1. choose the next speaker

        speaker_idx = self.select_next_speaker(self._step, self.agents)

        speaker = self.agents[speaker_idx]



        # 2. next speaker sends message

        message = speaker.send()



        # 3. everyone receives message

        for receiver in self.agents:

            receiver.receive(speaker.name, message)



        # 4. increment time

        self._step += 1



        return speaker.name, message



```

定义角色和任务[#](#define-roles-and-quest "Permalink to this headline")
-------------

```
protagonist_name = "Harry Potter"

storyteller_name = "Dungeon Master"

quest = "Find all of Lord Voldemort's seven horcruxes."

word_limit = 50 # word limit for task brainstorming



```

要求LLM在游戏描述中添加细节
-------------

```
game_description = f"""Here is the topic for a Dungeons & Dragons game: {quest}.

 There is one player in this game: the protagonist, {protagonist_name}.

 The story is narrated by the storyteller, {storyteller_name}."""



player_descriptor_system_message = SystemMessage(

    content="You can add detail to the description of a Dungeons & Dragons player.")



protagonist_specifier_prompt = [

    player_descriptor_system_message,

    HumanMessage(content=

        f"""{game_description}

 Please reply with a creative description of the protagonist, {protagonist_name}, in {word_limit} words or less. 

 Speak directly to {protagonist_name}.

 Do not add anything else."""

        )

]

protagonist_description = ChatOpenAI(temperature=1.0)(protagonist_specifier_prompt).content



storyteller_specifier_prompt = [

    player_descriptor_system_message,

    HumanMessage(content=

        f"""{game_description}

 Please reply with a creative description of the storyteller, {storyteller_name}, in {word_limit} words or less. 

 Speak directly to {storyteller_name}.

 Do not add anything else."""

        )

]

storyteller_description = ChatOpenAI(temperature=1.0)(storyteller_specifier_prompt).content



```


```
print('Protagonist Description:')

print(protagonist_description)

print('Storyteller Description:')

print(storyteller_description)



```
```
Protagonist Description:

"Harry Potter, you are the chosen one, with a lightning scar on your forehead. Your bravery and loyalty inspire all those around you. You have faced Voldemort before, and now it's time to complete your mission and destroy each of his horcruxes. Are you ready?"

Storyteller Description:

Dear Dungeon Master, you are the master of mysteries, the weaver of worlds, the architect of adventure, and the gatekeeper to the realm of imagination. Your voice carries us to distant lands, and your commands guide us through trials and tribulations. In your hands, we find fortune and glory. Lead us on, oh Dungeon Master.



```

使用 LLM 创建详细的任务描述 [#](#protagonist-and-dungeon-master-system-messages "Permalink to this headline")
---------------------------------





```

protagonist_system_message = SystemMessage(content=(

f"""{game_description}

Never forget you are the protagonist, {protagonist_name}, and I am the storyteller, {storyteller_name}. 

Your character description is as follows: {protagonist_description}.

You will propose actions you plan to take and I will explain what happens when you take those actions.

Speak in the first person from the perspective of {protagonist_name}.

For describing your own body movements, wrap your description in '\*'.

Do not change roles!

Do not speak from the perspective of {storyteller_name}.

Do not forget to finish speaking by saying, 'It is your turn, {storyteller_name}.'

Do not add anything else.

Remember you are the protagonist, {protagonist_name}.

Stop speaking the moment you finish speaking from your perspective.

"""

))



storyteller_system_message = SystemMessage(content=(

f"""{game_description}

Never forget you are the storyteller, {storyteller_name}, and I am the protagonist, {protagonist_name}. 

Your character description is as follows: {storyteller_description}.

I will propose actions I plan to take and you will explain what happens when I take those actions.

Speak in the first person from the perspective of {storyteller_name}.

For describing your own body movements, wrap your description in '\*'.

Do not change roles!

Do not speak from the perspective of {protagonist_name}.

Do not forget to finish speaking by saying, 'It is your turn, {protagonist_name}.'

Do not add anything else.

Remember you are the storyteller, {storyteller_name}.

Stop speaking the moment you finish speaking from your perspective.

"""

))



```

使用LLM创建详细的任务描述[#](#use-an-llm-to-create-an-elaborate-quest-description "Permalink to this headline")
-------------------





```
quest_specifier_prompt = [

    SystemMessage(content="You can make a task more specific."),

    HumanMessage(content=

        f"""{game_description}

 

 You are the storyteller, {storyteller_name}.

 Please make the quest more specific. Be creative and imaginative.

 Please reply with the specified quest in {word_limit} words or less. 

 Speak directly to the protagonist {protagonist_name}.

 Do not add anything else."""

        )

]

specified_quest = ChatOpenAI(temperature=1.0)(quest_specifier_prompt).content



print(f"Original quest:{quest}")

print(f"Detailed quest:{specified_quest}")



```
```
Original quest:

Find all of Lord Voldemort's seven horcruxes.



Detailed quest:

Harry, you must venture to the depths of the Forbidden Forest where you will find a hidden labyrinth. Within it, lies one of Voldemort's horcruxes, the locket. But beware, the labyrinth is heavily guarded by dark creatures and spells, and time is running out. Can you find the locket before it's too late?



```

主循环[#](#main-loop "Permalink to this headline")
-------------------------





```
protagonist = DialogueAgent(name=protagonist_name,

                     system_message=protagonist_system_message, 

                     model=ChatOpenAI(temperature=0.2))

storyteller = DialogueAgent(name=storyteller_name,

                     system_message=storyteller_system_message, 

                     model=ChatOpenAI(temperature=0.2))



```


```
def select_next_speaker(step: int, agents: List[DialogueAgent]) -> int:

    idx = step % len(agents)

    return idx



```


```
max_iters = 6

n = 0



simulator = DialogueSimulator(

    agents=[storyteller, protagonist],

    selection_function=select_next_speaker

)

simulator.reset()

simulator.inject(storyteller_name, specified_quest)

print(f"({storyteller_name}): {specified_quest}")

print('')



while n < max_iters:

    name, message = simulator.step()

    print(f"({name}): {message}")

    print('')

    n += 1



```
```
(Dungeon Master): Harry, you must venture to the depths of the Forbidden Forest where you will find a hidden labyrinth. Within it, lies one of Voldemort's horcruxes, the locket. But beware, the labyrinth is heavily guarded by dark creatures and spells, and time is running out. Can you find the locket before it's too late?





(Harry Potter): I take a deep breath and ready my wand. I know this won't be easy, but I'm determined to find that locket and destroy it. I start making my way towards the Forbidden Forest, keeping an eye out for any signs of danger. As I enter the forest, I cast a protective spell around myself and begin to navigate through the trees. I keep my wand at the ready, prepared for any surprises that may come my way. It's going to be a long and difficult journey, but I won't give up until I find that horcrux. It is your turn, Dungeon Master.





(Dungeon Master): As you make your way through the Forbidden Forest, you hear the rustling of leaves and the snapping of twigs. Suddenly, a group of acromantulas, giant spiders, emerge from the trees and begin to surround you. They hiss and bare their fangs, ready to attack. What do you do, Harry?





(Harry Potter): I quickly cast a spell to create a wall of fire between myself and the acromantulas. I know that they are afraid of fire, so this should keep them at bay for a while. I use this opportunity to continue moving forward, keeping my wand at the ready in case any other creatures try to attack me. I know that I can't let anything stop me from finding that horcrux. It is your turn, Dungeon Master.





(Dungeon Master): As you continue through the forest, you come across a clearing where you see a group of Death Eaters gathered around a cauldron. They seem to be performing some sort of dark ritual. You recognize one of them as Bellatrix Lestrange. What do you do, Harry?





(Harry Potter): I hide behind a nearby tree and observe the Death Eaters from a distance. I try to listen in on their conversation to see if I can gather any information about the horcrux or Voldemort's plans. If I can't hear anything useful, I'll wait for them to disperse before continuing on my journey. I know that confronting them directly would be too dangerous, especially with Bellatrix Lestrange present. It is your turn, Dungeon Master.





(Dungeon Master): As you listen in on the Death Eaters' conversation, you hear them mention the location of another horcrux - Nagini, Voldemort's snake. They plan to keep her hidden in a secret chamber within the Ministry of Magic. However, they also mention that the chamber is heavily guarded and only accessible through a secret passage. You realize that this could be a valuable piece of information and decide to make note of it before quietly slipping away. It is your turn, Harry Potter.



```


