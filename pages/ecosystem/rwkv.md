

RWKV-4[#](#rwkv-4 "永久链接到该标题")
=============================

本页面介绍如何在LangChain中使用`RWKV-4`包装器。它分为两个部分：安装和设置，以及带有示例的使用。

安装和设置[#](#installation-and-setup "永久链接到该标题")
--------------------------------------------

* 使用`pip install rwkv`安装Python包

* 使用`pip install tokenizer`安装分词器Python包

* 下载一个[RWKV模型](https://huggingface.co/BlinkDL/rwkv-4-raven/tree/main)并将其放置在所需的目录中

* 下载[tokens文件](https://raw.githubusercontent.com/BlinkDL/ChatRWKV/main/20B_tokenizer.json)

用法[#](#usage "Permalink to this headline")
------------------------------------------

### RWKV[#](#rwkv "Permalink to this headline")

要使用RWKV包装器，您需要提供预训练模型文件的路径和tokenizer的配置。

```
from langchain.llms import RWKV

# Test the model

```python

def generate_prompt(instruction, input=None):
    if input:
        return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

# Instruction:
{instruction}

# Input:
{input}

# Response:
"""
    else:
        return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

# Instruction:
{instruction}

# Response:
"""

model = RWKV(model="./models/RWKV-4-Raven-3B-v7-Eng-20230404-ctx4096.pth", strategy="cpu fp32", tokens_path="./rwkv/20B_tokenizer.json")
response = model(generate_prompt("Once upon a time, "))

```

模型文件[#](#model-file "Permalink to this headline")
-------------------------------------------------

您可以在[RWKV-4-Raven](https://huggingface.co/BlinkDL/rwkv-4-raven/tree/main)存储库中找到模型文件下载链接。

### Rwkv-4 models -> 推荐VRAM[#](#rwkv-4-models-recommended-vram "Permalink to this headline")

```
RWKV VRAM
Model | 8bit | bf16/fp16 | fp32
14B   | 16GB | 28GB      | >50GB
7B    | 8GB  | 14GB      | 28GB
3B    | 2.8GB| 6GB       | 12GB
1b5   | 1.3GB| 3GB       | 6GB

```

查看[rwkv pip](https://pypi.org/project/rwkv/)页面获取更多关于策略的信息，包括流处理和cuda支持。
