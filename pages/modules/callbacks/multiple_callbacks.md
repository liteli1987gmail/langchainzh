# 多重回调

在前面的例子中，我们使用`callbacks=`在创建对象时传入回调处理程序。在这种情况下，回调处理程序将被限定在该特定对象范围内。

然而，在许多情况下，通过在运行对象时传入处理程序更有优势。当我们使用`callbacks`关键字参数传递`CallbackHandlers`来执行一个运行操作时，这些回调将被所有嵌套对象中的执行所发出。例如，当一个处理程序被传递给`Agent`时，它将被用于与代理相关的所有回调以及代理执行中涉及的所有对象，即`Tools`、`LLMChain`和`LLM`。

这样我们就不必手动将处理程序附加到每个单独的嵌套对象上。

```python
from typing import Any, Dict, List, Union

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.agents import AgentAction
from langchain_openai import OpenAI


# 首先，定义自定义的回调处理程序实现
class MyCustomHandlerOne(BaseCallbackHandler):
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        print(f"on_llm_start {serialized['name']}")

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        print(f"on_new_token {token}")

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """LLM错误时运行"""

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        print(f"on_chain_start {serialized['name']}")

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        print(f"on_tool_start {serialized['name']}")

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        print(f"on_agent_action {action}")


class MyCustomHandlerTwo(BaseCallbackHandler):
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        print(f"on_llm_start （我是第二个处理程序！）{serialized['name']}")


# 实例化处理程序
handler1 = MyCustomHandlerOne()
handler2 = MyCustomHandlerTwo()

# 设置代理。只有`llm`会通过handler2发出回调
llm = OpenAI(temperature=0, streaming=True, callbacks=[handler2])
tools = load_tools(["llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# handler1的回调将由与代理执行相关的每个对象发出（llm、llmchain、tool、agent executor）
agent.run("2的0.235次方是多少？", callbacks=[handler1])
```

    on_chain_start AgentExecutor
    on_chain_start LLMChain
    on_llm_start OpenAI
    on_llm_start （我是第二个处理程序！）OpenAI
    on_new_token  我
    on_new_token  需要
    on_new_token  使用
    on_new_token  计算器
    on_new_token  来
    on_new_token  解决
    on_new_token  这个
    on_new_token  。
    on_new_token  
    on_agent_action AgentAction(tool='Calculator', tool_input='2^0.235', log=' 我需要使用计算器来解决这个。\nAction: Calculator\nAction Input: 2^0.235')
    on_tool_start Calculator
    on_chain_start LLMMathChain
    on_chain_start LLMChain
    on_llm_start OpenAI
    on_llm_start （我是第二个处理程序！）OpenAI
    on_new_token  
    on_new_token ```text
    on_new_token 
    on_new_token 2
    on_new_token **
    on_new_token 0
    on_new_token .
    on_new_token 235
    on_new_token 
    on_new_token ```
    
    on_new_token ...
    on_new_token num
    on_new_token expr
    on_new_token .
    on_new_token evaluate
    on_new_token ("
    on_new_token 2
    on_new_token **
    on_new_token 0
    on_new_token .
    on_new_token 235
    on_new_token ")
    on_new_token ...
    on_new_token  
    on_chain_start LLMChain
    on_llm_start OpenAI
    on_llm_start （我是第二个处理程序！）OpenAI
    on_new_token  我
    on_new_token  现在
    on_new_token  知道
    on_new_token  最终
    on_new_token  的
    on_new_token  答案
    on_new_token  。
    on_new_token  
    on_new_token 最终
    on_new_token  答案
    on_new_token  ：
    on_new_token  1
    on_new_token  .
    on_new_token 17
    on_new_token 690
    on_new_token 67
    on_new_token 372
    on_new_token 187
    on_new_token 674
    on_new_token 
    




    '1.1769067372187674'

