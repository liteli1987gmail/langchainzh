# 人在循环中

有些工具我们不相信模型能够独立执行。在这种情况下，我们可以要求在调用工具之前进行人工批准。

## 设置

我们需要安装以下软件包:


```python
%pip install --upgrade --quiet langchain langchain-openai
```

并设置以下环境变量:


```python
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

# 如果您想使用LangSmith，请取消注释以下内容:
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
```

## 链

假设我们有以下（虚拟的）工具和工具调用链：

```python
from operator import itemgetter

from langchain.output_parsers import JsonOutputToolsParser
from langchain_core.runnables import Runnable, RunnableLambda, RunnablePassthrough
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


@tool
def count_emails(last_n_days: int) -> int:
    """将两个整数相乘。"""
    return last_n_days * 2


@tool
def send_email(message: str, recipient: str) -> str:
    "将两个整数相加。"
    return f"成功将电子邮件发送至{recipient}。"


tools = [count_emails, send_email]
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0).bind_tools(tools)


def call_tool(tool_invocation: dict) -> Runnable:
    """根据模型选择的工具动态构建链的结尾的函数。"""
    tool_map = {tool.name: tool for tool in tools}
    tool = tool_map[tool_invocation["type"]]
    return RunnablePassthrough.assign(output=itemgetter("args") | tool)


# .map() 允许我们将函数应用于输入列表。
call_tool_list = RunnableLambda(call_tool).map()
chain = model | JsonOutputToolsParser() | call_tool_list
chain.invoke("我在过去5天内收到了多少封电子邮件？")
```




    [{'type': 'count_emails', 'args': {'last_n_days': 5}, 'output': 10}]



## 添加人工批准

我们可以将一个简单的人工批准步骤添加到我们的 tool_chain 函数中：

```python
import json


def human_approval(tool_invocations: list) -> Runnable:
    tool_strs = "\n\n".join(
        json.dumps(tool_call, indent=2) for tool_call in tool_invocations
    )
    msg = (
        f"您是否批准以下工具调用\n\n{tool_strs}\n\n"
        "除了 'Y'/'Yes'（不区分大小写）之外的任何响应都将被视为不批准。"
    )
    resp = input(msg)
    if resp.lower() not in ("yes", "y"):
        raise ValueError(f"未批准工具调用:\n\n{tool_strs}")
    return tool_invocations
```


```python
chain = model | JsonOutputToolsParser() | human_approval | call_tool_list
chain.invoke("我在过去5天内收到了多少封电子邮件？")
```

    您是否批准以下工具调用
    
    {
      "type": "count_emails",
      "args": {
        "last_n_days": 5
      }
    }
    
    除了 'Y'/'Yes'（不区分大小写）之外的任何响应都将被视为不批准。 y
    




    [{'type': 'count_emails', 'args': {'last_n_days': 5}, 'output': 10}]




```python
chain.invoke("给sally@gmail.com发送一封邮件，内容是'你好，朋友'")
```

    您是否批准以下工具调用
    
    {
      "type": "send_email",
      "args": {
        "message": "你好，朋友",
        "recipient": "sally@gmail.com"
      }
    }
    
    除了 'Y'/'Yes'（不区分大小写）之外的任何响应都将被视为不批准。 no
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[32], line 1
    ----> 1 chain.invoke("给sally@gmail.com发送一封邮件，内容是'你好，朋友'")
    

    File ~/langchain/libs/core/langchain_core/runnables/base.py:1774, in RunnableSequence.invoke(self, input, config)
       1772 try:
       1773     for i, step in enumerate(self.steps):
    -> 1774         input = step.invoke(
       1775             input,
       1776             # mark each step as a child run
       1777             patch_config(
       1778                 config, callbacks=run_manager.get_child(f"seq:step:{i+1}")
       1779             ),
       1780         )
       1781 # finish the root run
       1782 except BaseException as e:
    

    File ~/langchain/libs/core/langchain_core/runnables/base.py:3074, in RunnableLambda.invoke(self, input, config, **kwargs)
       3072 """Invoke this runnable synchronously."""
       3073 if hasattr(self, "func"):
    -> 3074     return self._call_with_config(
       3075         self._invoke,
       3076         input,
       3077         self._config(config, self.func),
       3078         **kwargs,
       3079     )
       3080 else:
       3081     raise TypeError(
       3082         "Cannot invoke a coroutine function synchronously."
       3083         "Use `ainvoke` instead."
       3084     )
    

    File ~/langchain/libs/core/langchain_core/runnables/base.py:975, in Runnable._call_with_config(self, func, input, config, run_type, **kwargs)
        971     context = copy_context()
        972     context.run(var_child_runnable_config.set, child_config)
        973     output = cast(
        974         Output,
    --> 975         context.run(
        976             call_func_with_variable_args,
        977             func,  # type: ignore[arg-type]
        978             input,  # type: ignore[arg-type]
        979             config,
        980             run_manager,
        981             **kwargs,
        982         ),
        983     )
        984 except BaseException as e:
        985     run_manager.on_chain_error(e)
    

    File ~/langchain/libs/core/langchain_core/runnables/base.py:948, in Runnable._call_with_config(self, func, input, config, run_type, **kwargs)
        944 if arguments_schema is not None:
        945     input = cast(Dict[str, Any], arguments_schema.load(input))
    --> 946 return func(input, config=config, type=run_type, **kwargs)
        947 else:
        948     return func(input, config=config, run_type=run_type, **kwargs)
        949 else:
        950 # if configuration supplied update the type
        951 return self._as_runnable(
    

    <ipython-input-31-d74dd1dd2f0f>:12, in human_approval(tool_invocations)
          9         json.dumps(tool_call, indent=2) for tool_call in tool_invocations
         10     )
    ---> 11     resp = input(msg)
         12     if resp.lower() not in ("yes", "y"):
         13         raise ValueError(f"未批准工具调用:\n\n{tool_strs}")
    

    ~/miniconda3/envs/assistant/lib/python3.7/site-packages/ipykernel/kernelbase.py:855, in Kernel.getpass(self, prompt, stream, cache, echo, **kwargs)
        850 def getpass(self, prompt='', stream=None, cache=False, echo=True, **kwargs):
        851     """Forward getpass to frontends
        852 
        853     Raises
        854     ------
    --> 855     StdinNotImplementedError if active frontend doesn't support stdin.
        856 
        857     """
        858     if stream is not None:
        859         try:

    StdinNotImplementedError: getpass was called with input_request="Do you approve of the following tool invocations\n\n{\n  \"type\": \"send_email\",\n  \"args\": {\n    \"message\": \"What's up homie\",\n    \"recipient\": \"sally@gmail.com\"\n  }\n}\n\nAnything except 'Y'/'Yes' (case-insensitive) will be treated as a no.", but this frontend does not support stdin.
    [
      {
        "type": "send_email",
        "args": {
          "message": "What's up homie",
          "recipient": "sally@gmail.com"
        }
      }
    ]
    File ~/langchain/libs/core/langchain_core/runnables/config.py:323, in call_func_with_variable_args(func, input, config, run_manager, **kwargs)
        321 if run_manager is not None and accepts_run_manager(func):
        322     kwargs["run_manager"] = run_manager
    --> 323 return func(input, **kwargs)
    

    File ~/langchain/libs/core/langchain_core/runnables/base.py:2950, in RunnableLambda._invoke(self, input, run_manager, config, **kwargs)
       2948                 output = chunk
       2949 else:
    -> 2950     output = call_func_with_variable_args(
       2951         self.func, input, config, run_manager, **kwargs
       2952     )
       2953 # If the output is a runnable, invoke it
       2954 if isinstance(output, Runnable):
    

    File ~/langchain/libs/core/langchain_core/runnables/config.py:323, in call_func_with_variable_args(func, input, config, run_manager, **kwargs)
        321 if run_manager is not None and accepts_run_manager(func):
        322     kwargs["run_manager"] = run_manager
    --> 323 return func(input, **kwargs)
    

    Cell In[30], line 11, in human_approval(tool_invocations)
          9 resp = input(msg)
         10 if not resp.lower() in ("yes", "y"):
    ---> 11     raise ValueError(f"Tool invocations not approved:\n\n{tool_strs}")
         12 return tool_invocations
    

    ValueError: Tool invocations not approved:
    
    {
      "type": "send_email",
      "args": {
        "message": "What's up homie",
        "recipient": "sally@gmail.com"
      }
    }








