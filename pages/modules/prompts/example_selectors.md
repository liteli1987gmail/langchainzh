Example Selectors
======

注意

[概念指南](https://docs.langchain.com/docs/components/prompts/example-selectors)

如果您有大量的示例，您可能需要选择包含在提示中的示例。ExampleSelector是负责执行此操作的类。

基本接口定义如下：

```
class BaseExampleSelector(ABC):
 """Interface for selecting examples to include in prompts."""

    @abstractmethod
    def select_examples(self, input_variables: Dict[str, str]) -> List[dict]:
 """Select which examples to use based on the inputs."""

```

ExampleSelector唯一需要公开的方法是`select_examples`。该方法接受输入变量，然后返回一个示例列表。如何选择这些示例取决于每个具体实现。以下是一些示例。

请参见下面的示例选择器列表。

* [How to create a custom example selector](example_selectors/examples/custom_example_selector)
* [LengthBased ExampleSelector](example_selectors/examples/length_based)
* [最大边际相关性 ExampleSelector](example_selectors/examples/mmr)
* [NGram 重叠 ExampleSelector](example_selectors/examples/ngram_overlap)

* [相似度 ExampleSelector](example_selectors/examples/similarity)

