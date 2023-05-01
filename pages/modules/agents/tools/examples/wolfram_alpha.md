


 Wolfram Alpha
 [#](#wolfram-alpha "Permalink to this headline")
=================================================================



 This notebook goes over how to use the wolfram alpha component.
 



 First, you need to set up your Wolfram Alpha developer account and get your APP ID:
 


1. Go to wolfram alpha and sign up for a developer account
 [here](https://developer.wolframalpha.com/)
2. Create an app and get your APP ID
3. pip install wolframalpha



 Then we will need to set some environment variables:
 


1. Save your APP ID into WOLFRAM_ALPHA_APPID env variable







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







