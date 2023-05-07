

Sequential Chains[#](#sequential-chains "Permalink to this headline")
=====================================================================

调用语言模型后的下一步是做一系列的调用。当您想要将一个调用的输出作为另一个调用的输入时，这是特别有用的。

在本笔记本中，我们将演示如何使用顺序链来完成一些示例。顺序链被定义为一系列链，按确定的顺序调用。有两种类型的顺序链：

* `SimpleSequentialChain`：最简单的顺序链形式，每个步骤都有一个单一的输入/输出，一个步骤的输出是下一个步骤的输入。

* `SequentialChain`：更一般的顺序链形式，允许多个输入/输出。

SimpleSequentialChain[#](#simplesequentialchain "Permalink to this headline")
-----------------------------------------------------------------------------

在这个链式结构中，每个链只有一个输入和一个输出，一个步骤的输出作为下一个步骤的输入。

我们来看一个玩具例子，第一个链接收一个虚构剧本的标题，然后生成该剧本的概要，第二个链接收该剧本的概要，然后生成一个虚构评论。

```
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

```

```
# This is an LLMChain to write a synopsis given a title of a play.
llm = OpenAI(temperature=.7)
template = """You are a playwright. Given the title of play, it is your job to write a synopsis for that title.

Title: {title}
Playwright: This is a synopsis for the above play:"""
prompt_template = PromptTemplate(input_variables=["title"], template=template)
synopsis_chain = LLMChain(llm=llm, prompt=prompt_template)

```

```
# This is an LLMChain to write a review of a play given a synopsis.
llm = OpenAI(temperature=.7)
template = """You are a play critic from the New York Times. Given the synopsis of play, it is your job to write a review for that play.

Play Synopsis:
{synopsis}
Review from a New York Times play critic of the above play:"""
prompt_template = PromptTemplate(input_variables=["synopsis"], template=template)
review_chain = LLMChain(llm=llm, prompt=prompt_template)

```

```
# This is the overall chain where we run these two chains in sequence.
from langchain.chains import SimpleSequentialChain
overall_chain = SimpleSequentialChain(chains=[synopsis_chain, review_chain], verbose=True)

```

```
review = overall_chain.run("Tragedy at sunset on the beach")

```

```
> Entering new SimpleSequentialChain chain...

Tragedy at Sunset on the Beach is a story of a young couple, Jack and Sarah, who are in love and looking forward to their future together. On the night of their anniversary, they decide to take a walk on the beach at sunset. As they are walking, they come across a mysterious figure, who tells them that their love will be tested in the near future. 

The figure then tells the couple that the sun will soon set, and with it, a tragedy will strike. If Jack and Sarah can stay together and pass the test, they will be granted everlasting love. However, if they fail, their love will be lost forever.

The play follows the couple as they struggle to stay together and battle the forces that threaten to tear them apart. Despite the tragedy that awaits them, they remain devoted to one another and fight to keep their love alive. In the end, the couple must decide whether to take a chance on their future together or succumb to the tragedy of the sunset.

Tragedy at Sunset on the Beach is an emotionally gripping story of love, hope, and sacrifice. Through the story of Jack and Sarah, the audience is taken on a journey of self-discovery and the power of love to overcome even the greatest of obstacles. 

The play's talented cast brings the characters to life, allowing us to feel the depths of their emotion and the intensity of their struggle. With its compelling story and captivating performances, this play is sure to draw in audiences and leave them on the edge of their seats. 

The play's setting of the beach at sunset adds a touch of poignancy and romanticism to the story, while the mysterious figure serves to keep the audience enthralled. Overall, Tragedy at Sunset on the Beach is an engaging and thought-provoking play that is sure to leave audiences feeling inspired and hopeful.

> Finished chain.

```

```
print(review)

```

```
Tragedy at Sunset on the Beach is an emotionally gripping story of love, hope, and sacrifice. Through the story of Jack and Sarah, the audience is taken on a journey of self-discovery and the power of love to overcome even the greatest of obstacles. 

The play's talented cast brings the characters to life, allowing us to feel the depths of their emotion and the intensity of their struggle. With its compelling story and captivating performances, this play is sure to draw in audiences and leave them on the edge of their seats. 

The play's setting of the beach at sunset adds a touch of poignancy and romanticism to the story, while the mysterious figure serves to keep the audience enthralled. Overall, Tragedy at Sunset on the Beach is an engaging and thought-provoking play that is sure to leave audiences feeling inspired and hopeful.

```

顺序链[#](#sequential-chain "Permalink to this headline")
------------------------------------------------------

当然，并不是所有的顺序链都像传递单个字符串参数并获取单个字符串输出那样简单。在下一个示例中，我们将尝试更复杂的链，涉及多个输入，以及多个最终输出。

特别重要的是如何命名输入/输出变量名。在上面的例子中，我们不必考虑这个问题，因为我们只是将一个链的输出直接作为下一个链的输入传递，但在这里，我们必须考虑这个问题，因为我们有多个输入。

```
# This is an LLMChain to write a synopsis given a title of a play and the era it is set in.
llm = OpenAI(temperature=.7)
template = """You are a playwright. Given the title of play and the era it is set in, it is your job to write a synopsis for that title.

Title: {title}
Era: {era}
Playwright: This is a synopsis for the above play:"""
prompt_template = PromptTemplate(input_variables=["title", 'era'], template=template)
synopsis_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="synopsis")

```

```
# This is an LLMChain to write a review of a play given a synopsis.
llm = OpenAI(temperature=.7)
template = """You are a play critic from the New York Times. Given the synopsis of play, it is your job to write a review for that play.

Play Synopsis:
{synopsis}
Review from a New York Times play critic of the above play:"""
prompt_template = PromptTemplate(input_variables=["synopsis"], template=template)
review_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="review")

```

```
# This is the overall chain where we run these two chains in sequence.
from langchain.chains import SequentialChain
overall_chain = SequentialChain(
    chains=[synopsis_chain, review_chain],
    input_variables=["era", "title"],
    # Here we return multiple variables
    output_variables=["synopsis", "review"],
    verbose=True)

```

```
overall_chain({"title":"Tragedy at sunset on the beach", "era": "Victorian England"})

```

```
> Entering new SequentialChain chain...

> Finished chain.

```

```
{'title': 'Tragedy at sunset on the beach',
 'era': 'Victorian England',
 'synopsis': "  The play follows the story of John, a young man from a wealthy Victorian family, who dreams of a better life for himself. He soon meets a beautiful young woman named Mary, who shares his dream. The two fall in love and decide to elope and start a new life together.  On their journey, they make their way to a beach at sunset, where they plan to exchange their vows of love. Unbeknownst to them, their plans are overheard by John's father, who has been tracking them. He follows them to the beach and, in a fit of rage, confronts them.   A physical altercation ensues, and in the struggle, John's father accidentally stabs Mary in the chest with his sword. The two are left in shock and disbelief as Mary dies in John's arms, her last words being a declaration of her love for him.  The tragedy of the play comes to a head when John, broken and with no hope of a future, chooses to take his own life by jumping off the cliffs into the sea below.   The play is a powerful story of love, hope, and loss set against the backdrop of 19th century England.",
 'review': "  The latest production from playwright X is a powerful and heartbreaking story of love and loss set against the backdrop of 19th century England. The play follows John, a young man from a wealthy Victorian family, and Mary, a beautiful young woman with whom he falls in love. The two decide to elope and start a new life together, and the audience is taken on a journey of hope and optimism for the future.  Unfortunately, their dreams are cut short when John's father discovers them and in a fit of rage, fatally stabs Mary. The tragedy of the play is further compounded when John, broken and without hope, takes his own life. The storyline is not only realistic, but also emotionally compelling, drawing the audience in from start to finish.  The acting was also commendable, with the actors delivering believable and nuanced performances. The playwright and director have successfully crafted a timeless tale of love and loss that will resonate with audiences for years to come. Highly recommended."}

```

### 顺序链中的记忆[#](#memory-in-sequential-chains "Permalink to this headline")

有时您可能想传递一些上下文以在链的每个步骤或链的后面部分中使用，但维护和链接输入/输出变量可能会很快变得混乱。使用 `SimpleMemory` 是一种方便的方式来管理这个问题并清理您的链。

举个例子，假设你使用之前介绍过的playwright SequentialChain，你想要在剧本中添加一些关于日期、时间和地点的上下文信息，并且使用生成的简介和评论来创建一些社交媒体发布文本。你可以将这些新的上下文变量添加为`input_variables`，或者我们可以添加一个`SimpleMemory`到链中来管理这个上下文：

```
from langchain.chains import SequentialChain
from langchain.memory import SimpleMemory

llm = OpenAI(temperature=.7)
template = """You are a social media manager for a theater company. Given the title of play, the era it is set in, the date,time and location, the synopsis of the play, and the review of the play, it is your job to write a social media post for that play.

Here is some context about the time and location of the play:
Date and Time: {time}
Location: {location}

Play Synopsis:
{synopsis}
Review from a New York Times play critic of the above play:
{review}

Social Media Post:
"""
prompt_template = PromptTemplate(input_variables=["synopsis", "review", "time", "location"], template=template)
social_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="social_post_text")

overall_chain = SequentialChain(
    memory=SimpleMemory(memories={"time": "December 25th, 8pm PST", "location": "Theater in the Park"}),
    chains=[synopsis_chain, review_chain, social_chain],
    input_variables=["era", "title"],
    # Here we return multiple variables
    output_variables=["social_post_text"],
    verbose=True)

overall_chain({"title":"Tragedy at sunset on the beach", "era": "Victorian England"})

```

```
> Entering new SequentialChain chain...

> Finished chain.

```

```
{'title': 'Tragedy at sunset on the beach',
 'era': 'Victorian England',
 'time': 'December 25th, 8pm PST',
 'location': 'Theater in the Park',
 'social_post_text': "\nSpend your Christmas night with us at Theater in the Park and experience the heartbreaking story of love and loss that is 'A Walk on the Beach'. Set in Victorian England, this romantic tragedy follows the story of Frances and Edward, a young couple whose love is tragically cut short. Don't miss this emotional and thought-provoking production that is sure to leave you in tears. #AWalkOnTheBeach #LoveAndLoss #TheaterInThePark #VictorianEngland"}

```

