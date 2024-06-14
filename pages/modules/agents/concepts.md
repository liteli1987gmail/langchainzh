# 概念

代理的核心思想是使用语言模型选择一系列要执行的操作。
在链式操作中，一系列操作是硬编码的（在代码中）。
在代理中，语言模型被用作推理引擎，确定要执行的操作及其顺序。

这里有几个关键组件：

## 架构

LangChain有几个抽象，使代理操作变得简单。

### 代理操作

这是一个代理应该执行的动作的数据类。
它有一个 `tool` 属性（应该调用的工具的名称）和一个 `tool_input` 属性（该工具的输入）

### 代理完成

这代表了代理的最终结果，当它准备好返回给用户时。
它包含了一个 `return_values` 键值映射，其中包含最终代理输出。
通常，这包括一个 `output` 键，其中包含代理的响应字符串。

### 中间步骤

代表了本代理运行中之前的代理操作和相应的输出。
这些对于传递给未来的迭代非常重要，这样代理就知道它已经做了哪些工作。
这被定义为 `List[Tuple[AgentAction, Any]]`。
请注意，观察目前保留为类型`Any`以获得最大的灵活性。
实际上，这通常是一个字符串。

## 代理

这是决定下一步要采取的链。
它通常由一个语言模型、一个提示和一个输出解析器驱动。

不同的代理具有不同的推理风格、不同的编码输入方式和不同的输出解析方式。
要查看内置代理的完整列表，请参见[代理类型](/modules/agents/agent_types/)。
如果需要更多控制，您也可以**轻松创建自定义代理**。

### 代理输入

代理的输入是一个键值映射。
只有一个必需的键：`intermediate_steps`，对应于上面描述的 `Intermediate Steps`。

通常，PromptTemplate负责将这些对转换为可以最好传递到LLM中的格式。

### 代理输出

输出是下一个要采取的动作或发送给用户的最终响应（`AgentAction`或`AgentFinish`）。
具体来说，这可以被定义为 `Union[AgentAction, List[AgentAction], AgentFinish]`。

输出解析器负责将原始LLM输出转换为这三种类型之一。

## 代理执行器

代理执行器是代理的运行时。
这实际上是调用代理、执行它选择的动作、将动作输出传回给代理并重复此过程的部分。
伪代码大致如下：

```python
next_action = agent.get_action(...)
while next_action != AgentFinish:
    observation = run(next_action)
    next_action = agent.get_action(..., next_action, observation)
return next_action
```

虽然这看起来简单，但此运行时为您处理了一些复杂性，包括：

1. 处理代理选择不存在的工具的情况
2. 处理工具出错的情况
3. 处理代理产生的无法解析为工具调用的输出的情况
4. 对所有级别（代理决策、工具调用）的日志记录和可观察性输出到标准输出和/或[LangSmith](/langsmith)。

## 工具

工具是代理可以调用的函数。
`Tool`抽象包括两个组成部分：

1. 工具的输入架构。这告诉LLM调用工具需要什么参数。没有这个，它将不知道正确的输入是什么。这些参数应该命名合理并进行描述。
2. 运行的函数。通常只是一个被调用的Python函数。

### 考虑因素

工具周围有两个重要的设计考虑：

1. 给代理访问正确的工具
2. 以对代理最有帮助的方式描述工具

如果不考虑这两点，您将无法构建一个可用的代理。
如果不给代理访问正确的工具，它永远无法达到您给定的目标。
如果您描述工具不够好，代理将不知道如何正确使用它们。

LangChain提供了各种内置工具，但也可以轻松定义自己的工具（包括自定义描述）。
要查看内置工具的完整列表，请参见[工具集成部分](/docs/integrations/tools/)

## 工具包

对于许多常见任务，代理需要一组相关的工具。
为此，LangChain提供了工具包的概念 - 一组大约3-5个工具，用于实现特定目标。
例如，GitHub工具包包含一个用于搜索GitHub问题的工具，一个用于阅读文件的工具，一个用于评论的工具等。

LangChain提供了大量的工具集，让您开始使用。
要查看内置工具包的完整列表，请参见[工具包集成部分](/docs/integrations/toolkits/)

# 先导概念

任何语言模型应用的核心元素是...模型。LangChain为您提供接口与任何语言模型进行交互的构建模块。本节内容主要是让与模型的工作更容易。这主要涉及到一个清晰的模型接口，辅助工具用于构建模型的输入，以及辅助工具用于处理模型的输出。

## 模型

LangChain集成的模型主要有两种类型：LLMs和聊天模型。它们通过它们的输入和输出类型来定义。

### LLMs

LangChain中的LLMs指的是纯文本完成模型。它们封装的API接受一个字符串提示作为输入，并输出一个字符串完成。OpenAI的GPT-3是实现为LLM。

### 聊天模型

聊天模型通常由LLMs支持，但专门针对进行对话进行了调整。关键是，它们的提供商API使用与纯文本完成模型不同的接口。它们不仅接受一个字符串作为输入，还可以接受一个聊天消息列表，并返回一个AI消息作为输出。请参阅下面的部分，以了解消息的具体内容。GPT-4和Anthropic的Claude-2都实现为聊天模型。

### 考虑因素

这两种API类型具有非常不同的输入和输出模式。这意味着与它们交互的最佳方法可能会有很大不同。尽管LangChain使它们能够互换使用，但这并不意味着您应该这样做。特别是，LLMs与ChatModels的提示策略可能会有很大不同。这意味着您需要确保您使用的提示是为您要处理的模型类型而设计的。

此外，并非所有模型都相同。不同的模型有不同的最佳提示策略。例如，Anthropic的模型最适合使用XML，而OpenAI的最适合使用JSON。这意味着您用于一个模型的提示可能无法转移到其他模型。LangChain提供了许多默认提示，然而这并不能保证与您使用的模型很好地配合。历史上，大多数提示在OpenAI上都能很好地工作，但在其他模型上并没有经过严格测试。这是我们正在努力解决的问题，但这是您应该记住的一点。

## 消息

ChatModels接受一个消息列表作为输入，并返回一个消息。消息有几种不同类型。所有消息都有`role`和`content`属性。`role`描述了是谁说了这条消息。LangChain为不同的角色提供不同的消息类。`content`属性描述了消息的内容。这可以是一些不同的内容：

- 一个字符串（大多数模型是这样的）
- 一个字典列表（这用于多模式输入，其中字典包含关于该输入类型和输入位置的信息）

此外，消息还有一个`additional_kwargs`属性。这是可以传递有关消息的其他信息的地方。这主要用于*特定于提供商*的输入参数，而不是通用的参数。这方面的最佳示例是OpenAI的`function_call`。

### HumanMessage

这代表用户发送的消息。通常只包含内容。

### AIMessage

这代表模型发送的消息。这可能包含`additional_kwargs` - 例如，使用OpenAI函数调用时可能包含`functional_call`。

### SystemMessage

这代表系统消息。只有一些模型支持这个。这告诉模型如何行为。通常只包含内容。

### FunctionMessage

这代表函数调用的结果。除了`role`和`content`，这个消息还有一个`name`参数，表示生成此结果的被调用函数的名称。

### ToolMessage

这代表工具调用的结果。为了匹配OpenAI的`function`和`tool`消息类型，这与FunctionMessage不同。除了`role`和`content`，这个消息还有一个`tool_call_id`参数，表示被调用以生成此结果的工具的ID。

## 提示

语言模型的输入通常被称为提示。通常情况下，您应用程序中的用户输入并不是直接输入到模型的输入中。相反，他们的输入以某种方式转换为生成字符串或消息列表作为模型的输入。将用户输入转换为最终字符串或消息的对象称为“提示模板”。LangChain提供了几种抽象以使处理提示更容易。

### PromptValue

ChatModels和LLMs接受不同的输入类型。PromptValue是一个设计用于两者之间可互操作的类。它公开了一种方法，将其转换为字符串（与LLMs一起使用），以及另一种方法将其转换为消息列表（与ChatModels一起使用）。

### PromptTemplate

[这里](/modules/model_io/prompts/quick_start#prompttemplate)是一个提示模板的示例。它包括一个模板字符串。然后，该字符串与用户输入格式化，生成最终字符串。

### MessagePromptTemplate

这种类型的模板包括一个**消息**模板 - 意味着具有特定角色和PromptTemplate的一个特定消息。然后，这个PromptTemplate与用户输入格式化，生成最终字符串，成为此消息的`content`。

#### HumanMessagePromptTemplate

这是生成HumanMessage的MessagePromptTemplate。

#### AIMessagePromptTemplate

这是生成AIMessage的MessagePromptTemplate。

#### SystemMessagePromptTemplate

这是生成SystemMessage的MessagePromptTemplate。

### MessagesPlaceholder

通常，提示的输入可以是消息列表。这时您将使用MessagesPlaceholder。这些对象的一个参数是`variable_name`。与此`variable_name`值相同的输入应该是一个消息列表。

### ChatPromptTemplate

[这里](/modules/model_io/prompts/quick_start#chatprompttemplate)是一个提示模板的示例。它包括一系列MessagePromptTemplates或MessagePlaceholders。这些然后与用户输入格式化，生成最终消息列表。

## 输出解析器

模型的输出通常是字符串或消息。通常情况下，该字符串或消息包含格式化信息，以便在下游使用（例如，逗号分隔列表或JSON blob）。输出解析器负责接收模型的输出并将其转换为更可用的形式。这些通常对输出消息的`content`进行操作，但有时也会对`additional_kwargs`字段中的值进行操作。

### StrOutputParser

这是一个简单的输出解析器，它只是将语言模型（LLM或ChatModel）的输出转换为字符串。如果模型是LLM（因此输出一个字符串），它只需传递该字符串。如果输出是一个ChatModel（因此输出一个消息），它将通过消息的`.content`属性传递。

### OpenAI函数解析器

有一些专门用于处理OpenAI函数调用的解析器。它们接收`function_call`和`arguments`参数的输出（这些参数位于`additional_kwargs`中）并处理这些参数，通常忽略内容。

### 代理输出解析器

[代理](/modules/agents/)是使用语言模型确定要采取哪些步骤的系统。因此，语言模型的输出需要被解析成能够表示应该采取什么行动（如果有的话）的某种模式。AgentOutputParsers负责将原始LLM或ChatModel输出解析为该模式。这些输出解析器内部的逻辑可能会根据使用的模型和提示策略而有所不同。