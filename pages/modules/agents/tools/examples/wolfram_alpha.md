

Wolfram Alpha
====================

本笔记本将介绍如何使用Wolfram Alpha组件。

首先，您需要设置Wolfram Alpha开发人员帐户并获取您的APP ID：

1. 前往Wolfram Alpha并注册开发人员帐户 [这里](https://developer.wolframalpha.com/)
2. 创建应用程序并获取您的APP ID。
3. 安装wolframalpha：'pip install wolframalpha'

然后，我们需要设置一些环境变量：

1. 将您的APP ID保存到WOLFRAM_ALPHA_APPID环境变量中

```
pip install wolframalpha

```

```
import os
os.environ["WOLFRAM_ALPHA_APPID"] = ""

```

```
from langchain.utilities.wolfram_alpha import WolframAlphaAPIWrapper

```

```
wolfram = WolframAlphaAPIWrapper()

```

```
wolfram.run("What is 2x+5 = -3x + 7?")

```

```
'x = 2/5'

```

