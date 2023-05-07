

提示[#](#prompts "永久链接到此标题")
==========================

注意

[概念指南](https://docs.langchain.com/docs/components/prompts)

编程模型的新方式是通过提示进行的。
“提示”指的是模型的输入。
这个输入很少是硬编码的，而是通常从多个组件构建而成的。
PromptTemplate负责构建这个输入。
LangChain提供了几个类和函数，使构建和处理提示变得容易。

本文档的这一部分分为四个部分：

**LLM提示模板**

如何使用PromptTemplates提示语言模型。

**聊天提示模板**

如何使用PromptTemplates提示聊天模型。

**示例选择器**

通常情况下，在提示中包含示例很有用。
这些示例可以是硬编码的，但如果它们是动态选择的，则通常更有力。
本节介绍示例选择。

**输出解析器**

语言模型（和聊天模型)输出文本。
但是，很多时候，您可能希望获得比仅文本更结构化的信息。
这就是输出解析器的作用。
输出解析器负责（1)指示模型应该如何格式化输出，
（2)将输出解析为所需的格式（如果必要，包括重试)。

深入[#](#go-deeper "永久链接到此标题")
----------------------------

* [Prompt Templates](prompts/prompt_templates)

* [Chat Prompt Template](prompts/chat_prompt_template)

* [Example Selectors](prompts/example_selectors)

* [Output Parsers](prompts/output_parsers)

