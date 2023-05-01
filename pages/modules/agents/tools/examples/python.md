


 Python REPL
 [#](#python-repl "Permalink to this headline")
=============================================================



 Sometimes, for complex calculations, rather than have an LLM generate the answer directly, it can be better to have the LLM generate code to calculate the answer, and then run that code to get the answer. In order to easily do that, we provide a simple Python REPL to execute commands in.
 



 This interface will only return things that are printed - therefor, if you want to use it to calculate an answer, make sure to have it print out the answer.
 







```
from langchain.agents import Tool
from langchain.utilities import PythonREPL

```










```
python_repl = PythonREPL()

```










```
python_repl.run("print(1+1)")

```








```
'2\n'

```










```
# You can create the tool to pass to an agent
repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
    func=python_repl
)

```







