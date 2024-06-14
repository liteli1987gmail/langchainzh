# 将日志记录到文件
这个示例展示了如何将日志打印到文件中。它展示了如何使用`FileCallbackHandler`，它与[`StdOutCallbackHandler`](/modules/callbacks/#get-started)做的事情相同，但是将输出写入文件。它还使用了`loguru`库来记录处理程序未捕获的其他输出。


```python
from langchain.callbacks import FileCallbackHandler
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from loguru import logger

logfile = "output.log"

logger.add(logfile, colorize=True, enqueue=True)
handler = FileCallbackHandler(logfile)

llm = OpenAI()
prompt = PromptTemplate.from_template("1 + {number} = ")

# 这个链既会打印到标准输出（因为verbose=True），又会写入到'output.log'
# 如果verbose=False，FileCallbackHandler仍将写入到'output.log'
chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler], verbose=True)
answer = chain.run(number=2)
logger.info(answer)
```

    
    
    [1m> 进入新的LLMChain链...[0m
    格式化后的提示:
    [32;1m[1;3m1 + 2 = [0m
    

    [32m2023-06-01 18:36:38.929[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m20[0m - [1m
    
    3[0m
    

    
    [1m> 链结束。[0m
    

现在我们可以打开文件`output.log`来查看已捕获的输出。


```python
%pip install --upgrade --quiet  ansi2html > /dev/null
```


```python
from ansi2html import Ansi2HTMLConverter
from IPython.display import HTML, display

with open("output.log", "r") as f:
    content = f.read()

conv = Ansi2HTMLConverter()
html = conv.convert(content, full=True)

display(HTML(html))
```

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title></title>
<style type="text/css">
.ansi2html-content { display: inline; white-space: pre-wrap; word-wrap: break-word; }
.body_foreground { color: #AAAAAA; }
.body_background { background-color: #000000; }
.inv_foreground { color: #000000; }
.inv_background { background-color: #AAAAAA; }
.ansi1 { font-weight: bold; }
.ansi3 { font-style: italic; }
.ansi32 { color: #00aa00; }
.ansi36 { color: #00aaaa; }
</style>
</head>
<body class="body_foreground body_background" style="font-size: normal;" >
<pre class="ansi2html-content">


<span class="ansi1">&gt; 进入新的LLMChain链...</span>
格式化后的提示:
<span class="ansi1 ansi32"></span><span class="ansi1 ansi3 ansi32">1 + 2 = </span>

<span class="ansi1">&gt; 链结束。</span>
<span class="ansi32">2023-06-01 18:36:38.929</span> | <span class="ansi1">INFO    </span> | <span class="ansi36">__main__</span>:<span class="ansi36">&lt;module&gt;</span>:<span class="ansi36">20</span> - <span class="ansi1">

3</span>

</pre>
</body>

</html>
```

