# LLMCheckerChain
这个notebook演示了如何使用LLMCheckerChain。
```python
from langchain.chains import LLMCheckerChain
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.7)

text = "What type of mammal lays the biggest eggs?"

checker_chain = LLMCheckerChain.from_llm(llm, verbose=True)

checker_chain.run(text)
```
输出如下：
```
> 进入新的LLMCheckerChain链...

> 进入新的SequentialChain链...

> 链结束。

> 链结束。
```

```
没有哺乳动物能产下最大的蛋。长颈鹿鸟，这是一种巨鸟物种，产下了任何鸟的最大蛋。'
```