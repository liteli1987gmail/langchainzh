


 Installation
 [#](#installation "Permalink to this headline")
===============================================================




官方发布版本
-----------------------------

LangChain可在PyPi上获取，因此可以使用以下命令轻松安装：

```
pip install langchain
```

这将安装LangChain的最小要求。
LangChain的很多价值在于将其与各种模型提供程序、数据存储等集成。
默认情况下，并没有安装执行这些操作所需的依赖项。
但是，还有两种其他安装LangChain的方法，可以带来这些依赖项。

要安装用于常见LLM提供程序的模块，请运行：


```
pip install langchain[llms]

```




 To install all modules needed for all integrations, run:
 





```
pip install langchain[all]

```




 Note that if you are using
 `zsh`
 , you’ll need to quote square brackets when passing them as an argument to a command, for example:
 





```
pip install 'langchain[all]'

```






 Installing from source
 [#](#installing-from-source "Permalink to this headline")
-----------------------------------------------------------------------------------



 If you want to install from source, you can do so by cloning the repo and running:
 





```
pip install -e .

```






