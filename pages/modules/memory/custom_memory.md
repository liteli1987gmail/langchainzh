# 自定义内存

虽然在LangChain中有一些预定义的内存类型，但你很可能希望添加自己的内存类型，以使其最适合你的应用程序。本笔记本介绍了如何做到这一点。

对于这个笔记本，我们将向`ConversationChain`添加一个自定义内存类型。为了添加一个自定义内存类，我们需要导入基本内存类并对其进行子类化。

```python
from typing import Any, Dict, List

from langchain.chains import ConversationChain
from langchain.schema import BaseMemory
from langchain_openai import OpenAI
from pydantic import BaseModel
```

在这个例子中，我们将编写一个自定义内存类，它使用spaCy来提取实体并在一个简单的散列表中保存有关它们的信息。然后，在对话过程中，我们将查看输入文本，提取任何实体，并将任何关于它们的信息放入上下文中。

* 请注意，这个实现相当简单和脆弱，可能在生产环境中没有用处。它的目的是展示您可以添加自定义内存实现的方式。

为此，我们需要spaCy。

```python
%pip install --upgrade --quiet  spacy
# !python -m spacy download en_core_web_lg
```

```python
import spacy

nlp = spacy.load("en_core_web_lg")
```

```python
class SpacyEntityMemory(BaseMemory, BaseModel):
    """存储关于实体信息的内存类。"""

    # 定义存储实体信息的字典。
    entities: dict = {}
    # 定义将实体信息传递到提示中的键。
    memory_key: str = "entities"

    def clear(self):
        self.entities = {}

    @property
    def memory_variables(self) -> List[str]:
        """定义我们向提示提供的变量。"""
        return [self.memory_key]

    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        """加载内存变量，这里是实体键。"""
        # 获取输入文本并通过spaCy运行
        doc = nlp(inputs[list(inputs.keys())[0]])
        # 提取已知的实体信息，如果存在。
        entities = [
            self.entities[str(ent)] for ent in doc.ents if str(ent) in self.entities
        ]
        # 返回关于实体的组合信息以放入上下文中。
        return {self.memory_key: "\n".join(entities)}

    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        """将此对话的上下文保存到缓冲区。"""
        # 获取输入文本并通过spaCy运行
        text = inputs[list(inputs.keys())[0]]
        doc = nlp(text)
        # 对于提到的每个实体，将此信息保存到字典中。
        for ent in doc.ents:
            ent_str = str(ent)
            if ent_str in self.entities:
                self.entities[ent_str] += f"\n{text}"
            else:
                self.entities[ent_str] = text
```

现在我们定义一个提示，它接收有关实体的信息以及用户输入。

```python
from langchain.prompts.prompt import PromptTemplate

template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know. You are provided with information about entities the Human mentions, if relevant.

Relevant entity information:
{entities}

Conversation:
Human: {input}
AI:"""
prompt = PromptTemplate(input_variables=["entities", "input"], template=template)
```

现在我们将它们整合在一起！

```python
llm = OpenAI(temperature=0)
conversation = ConversationChain(
    llm=llm, prompt=prompt, verbose=True, memory=SpacyEntityMemory()
)
```

在第一个示例中，没有关于Harrison的先前知识，“相关实体信息”部分为空。

```python
conversation.predict(input="Harrison likes machine learning")
```

```
[1m> 进入新的ConversationChain链...[0m
格式化后的提示：
[32;1m[1;3m以下是一个友好的人机对话。 AI很健谈，提供了许多具体的上下文细节。如果AI不知道问题的答案，它会诚实地说不知道。如果相关，您将获得有关人类提到的实体的信息。

相关实体信息：
Conversation:
Human: Harrison likes machine learning
AI:[0m

[1m> 完成ConversationChain链。[0m
```

```
"那太棒了！机器学习是一个令人着迷的研究领域。它涉及使用算法分析数据并进行预测。你有没有学过机器学习，Harrison？"
```

现在在第二个示例中，我们可以看到它提取了有关Harrison的信息。

```python
conversation.predict(
    input="What do you think Harrison's favorite subject in college was?"
)
```

```
[1m> 进入新的ConversationChain链...[0m
格式化后的提示：
[32;1m[1;3m以下是一个友好的人机对话。 AI很健谈，提供了许多具体的上下文细节。如果AI不知道问题的答案，它会诚实地说不知道。如果相关，您将获得有关人类提到的实体的信息。

相关实体信息：
Harrison likes machine learning

Conversation:
Human: What do you think Harrison's favorite subject in college was?
AI:[0m

[1m> 完成ConversationChain链。[0m
```

```
"根据我对Harrison的了解，我认为他在大学最喜欢的科目是机器学习。他对这门学科表达了浓厚的兴趣，并经常提到它。"
```

请再次注意，这个实现相当简单和脆弱，可能在生产环境中没有用处。它的目的是展示您可以添加自定义内存实现的方式。