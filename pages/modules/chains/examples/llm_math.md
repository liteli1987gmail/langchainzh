# LLM Math
这个notebook演示了如何使用LLMs和Python REPLs来解决复杂的数学问题。
```python
from langchain import OpenAI, LLMMathChain

llm = OpenAI(temperature=0)
llm_math = LLMMathChain.from_llm(llm, verbose=True)

llm_math.run("What is 13 raised to the .3432 power?")
```
输出如下：
```
> 进入新的LLMMathChain链...
13的0.3432次方是多少？
```text
13 ** .3432
```
...numexpr.evaluate("13 ** .3432")...

答案：2.4116004626599237
> 链结束。
```
'答案：2.4116004626599237'