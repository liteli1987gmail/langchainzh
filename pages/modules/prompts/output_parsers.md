

输出解析器
======

注意

[概念指南](https://docs.langchain.com/docs/components/prompts/output-parser)

语言模型输出文本。但是很多时候，你可能想要获得比文本更结构化的信息。这就是输出解析器的作用。

输出解析器是帮助结构化语言模型响应的类。有两种主要的方法，一个输出解析器必须实现：

* `get_format_instructions() -> str`：一个方法，返回一个包含有关如何格式化语言模型输出的字符串。

* `parse(str) -> Any`：一个方法，接受一个字符串（假定为语言模型的响应）并将其解析为某个结构。

And then one optional one:

* `parse_with_prompt(str) -> Any`: A method which takes in a string (assumed to be the response from a language model) and a prompt (assumed to the prompt that generated such a response) and parses it into some structure. The prompt is largely provided in the event the OutputParser wants to retry or fix the output in some way, and needs information from the prompt to do so.

To start, we recommend familiarizing yourself with the Getting Started section

* [Output Parsers](output_parsers/getting_started.html)

After that, we provide deep dives on all the different types of output parsers.

* [逗号分隔列表输出解析器](output_parsers/examples/comma_separated.html)
* [输出修复解析器](output_parsers/examples/output_fixing_parser.html)

* [Pydantic输出解析器](output_parsers/examples/pydantic.html)

* [重试输出解析器](output_parsers/examples/retry.html)

* [结构化输出解析器](output_parsers/examples/structured.html)

