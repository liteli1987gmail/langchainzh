

Python REPL

有时，对于复杂的计算，与其让LLM直接生成答案，不如让LLM生成计算答案的代码，然后运行该代码以获得答案。为了便于执行该操作，我们提供了一个简单的Python REPL来执行命令。

该界面只会返回已打印的内容-因此，如果要使用它计算答案，请确保它打印出答案。

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
    func=python_repl.run
)

```

