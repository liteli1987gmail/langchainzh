# LangSmith 演练
[![在 Colab 中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docslangsmith/walkthrough.ipynb)

LangChain 使原型 LLM 应用程序和代理程序易于生成。然而，将 LLM 应用程序投入生产可能会变得难以预料。您将不得不在提示、链和其他组件上进行迭代，以构建高质量的产品。

LangSmith 使得调试、测试和持续改进您的 LLM 应用程序变得轻松。

在什么情况下可能会有用？当您想要快速调试一个新的链、代理程序或一套工具，创建和管理用于微调、少量支撑提示和评估的数据集，为了自信地开发，运行回归测试以捕获生产分析以获取产品洞察力和持续改进。

## 先决条件

**[创建 LangSmith 帐户](https://smith.langchain.com/) 并创建 API 密钥 (参见左下角)。通过查看 [文档](https://docs.smith.langchain.com/) 熟悉平台。**

请注意, LangSmith 正在进行封闭测试；我们正在逐步向更多用户推出。但是，您可以填写网站上的表格以获得加快访问速度。

现在，让我们开始吧!

## 在 LangSmith 中记录运行信息

首先，配置您的环境变量，以告诉 LangChain 记录追踪信息。这可以通过将 `LANGCHAIN_TRACING_V2` 环境变量设置为 true 来完成。
您可以通过设置 `LANGCHAIN_PROJECT` 环境变量来告诉 LangChain 要记录到哪个项目 (如果未设置该变量，则运行将被记录到 `default` 项目)。如果该项目不存在，它将自动为您创建。您还必须设置 `LANGCHAIN_ENDPOINT` 和 `LANGCHAIN_API_KEY` 环境变量。

有关其他设置追踪方式的更多信息，请参考[LangSmith文档](https://docs.smith.langchain.com/docs/)

**注意：** 您还可以使用python中的上下文管理器使用

```python
from langchain_core.tracers.context import tracing_v2_enabled

with tracing_v2_enabled(project_name="My Project"):
    agent.run("截至2023年加拿大有多少人口？")
```

但在本例中，我们将使用环境变量。

```python
%pip install --upgrade --quiet  langchain langsmith langchainhub --quiet
%pip install --upgrade --quiet  langchain-openai tiktoken pandas duckduckgo-search --quiet
```

```python
import os
from uuid import uuid4

unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = f"Tracing Walkthrough - {unique_id}"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = "<YOUR-API-KEY>"  # 更改为您的 API 密钥

# 在本教程中代理程序使用
os.environ["OPENAI_API_KEY"] = "<YOUR-OPENAI-API-KEY>"
```

创建 langsmith 客户端以与 API 交互。

```python
from langsmith import Client

client = Client()
```

创建 LangChain 组件并将运行信息记录到平台上。在本例中，我们将创建一个具有通用搜索工具 (DuckDuckGo) 访问权限的 ReAct 风格代理程序。代理程序的提示可以在 [Hub 这里](https://smith.langchain.com/hub/wfh/langsmith-agent-prompt) 查看。

```python
from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_openai import ChatOpenAI

# 获取此提示的最新版本
prompt = hub.pull("wfh/langsmith-agent-prompt:5d466cbc")

llm = ChatOpenAI(
    model="gpt-3.5-turbo-16k",
    temperature=0,
)

tools = [
    DuckDuckGoSearchResults(
        name="duck_duck_go"
    ),  # 使用 DuckDuckGo 进行常规互联网搜索
]

llm_with_tools = llm.bind_tools(tools)

runnable_agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)

agent_executor = AgentExecutor(
    agent=runnable_agent, tools=tools, handle_parsing_errors=True
)
```

我们同时在多个输入上并行运行代理程序以减小延迟。运行信息会在后台记录到 LangSmith 中，因此执行延迟不受影响。

```python
inputs = [
    "LangChain 是什么？",
    "LangSmith 是什么？",
    "Llama-v2 是什么时候发布的？",
    "langsmith cookbook 是什么？",
    "langchain 什么时候首次宣布了 hub？",
]

results = agent_executor.batch([{"input": x} for x in inputs], return_exceptions=True)
```

```python
results[:2]
```

假设您已经成功设置了环境，您的代理程序追踪应该显示在 [app](https://smith.langchain.com/) 的 `Projects` 部分。恭喜！

![Initial Runs](/img/log_traces.png)

不过，看起来代理程序并没有有效地使用工具。让我们进行评估，以便有一个基准。

## 评估代理程序

除了记录运行信息外，LangSmith 还允许您测试和评估 LLM 应用程序。

在本节中，您将利用 LangSmith 创建一个基准数据集，并在代理程序上运行 AI 辅助评估器来评估其输出。您将按照以下的几个步骤完成：

1. 创建一个数据集
2. 初始化一个用于基准测试的新代理程序
3. 配置评估器以对代理程序的输出进行评分
4. 使用数据集运行代理程序并评估结果

### 1. 创建一个 LangSmith 数据集

下面，我们使用 LangSmith 客户端从上述的输入问题和标签列表创建一个数据集。之后，您将使用这些信息来衡量一个新代理程序的性能。数据集是一组示例，这些示例仅仅是您可以用作应用程序测试用例的输入-输出对。

有关数据集的更多信息，包括如何从 CSV 或其他文件创建它们，或者如何在平台上创建它们，请参阅 [LangSmith 文档](https://docs.smith.langchain.com/)。

```python
outputs = [
    "LangChain 是一个使用大型语言模型构建应用程序的开源框架。它还是正在构建 LangSmith 的公司的名称。",
    "LangSmith 是一个由 LangChain 提供支持的用于调试、测试和监控语言模型应用程序和代理程序的统一平台",
    "2023 年 7 月 18 日",
    "langsmith cookbook 是一个包含如何使用 LangSmith 调试、评估和监控大型语言模型应用程序的详细示例的 GitHub 存储库。",
    "2023 年 9 月 5 日",
]
```

```python
dataset_name = f"agent-qa-{unique_id}"

dataset = client.create_dataset(
    dataset_name,
    description="一个关于 LangSmith 文档的示例问题数据集。",
)

client.create_examples(
    inputs=[{"input": query} for query in inputs],
    outputs=[{"output": answer} for answer in outputs],
    dataset_id=dataset.id,
)
```

### 2. 初始化一个用于基准测试的新代理程序

LangSmith 允许您评估任何 LLM、链、代理程序，甚至是自定义函数。对话式代理程序是有状态的 (它们有内存)；为了确保此状态不在数据集运行之间共享，我们将通过传递一个 `chain_factory` (也称为 `constructor`) 函数来初始化每次调用时都会初始化的链。

在本例中，我们将测试一个使用 OpenAI 的函数调用端点的代理程序。

```python
from langchain import hub
from langchain.agents import AgentExecutor, AgentType, initialize_agent, load_tools
from langchain_openai import ChatOpenAI

-----# 由于链式调用可能具有状态（例如，它们可以具有内存），因此我们提供了一种在数据集中对每一行初始化新链的方法。这是通过传入一个返回每一行新链的工厂函数来完成的。
     
def create_agent(prompt, llm_with_tools):
    runnable_agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_tool_messages(
                x["intermediate_steps"]
            ),
        }
        | prompt
        | llm_with_tools
        | OpenAIToolsAgentOutputParser()
    )
    return AgentExecutor(agent=runnable_agent, tools=tools, handle_parsing_errors=True)
```

### 3. 配置评估

在UI中手动比较链式的结果是有效的，但可能会耗费时间。使用自动化指标和AI辅助反馈来评估组件的性能可能会更有帮助。

下面，我们将创建一个自定义的运行评估器，记录启发式评估。

**启发式评估器**


```python
from langsmith.evaluation import EvaluationResult
from langsmith.schemas import Example, Run


def check_not_idk(run: Run, example: Example):
    """Illustration of a custom evaluator."""
    agent_response = run.outputs["output"]
    if "don't know" in agent_response or "not sure" in agent_response:
        score = 0
    else:
        score = 1
    # You can access the dataset labels in example.outputs[key]
    # You can also access the model inputs in run.inputs[key]
    return EvaluationResult(
        key="not_uncertain",
        score=score,
    )
```

#### 批量评估器

有些指标在完整的“测试”上进行了聚合，而没有分配给单个运行/示例。这些指标可以是简单的分类指标，如精确度、召回率或AUC，也可以是其他自定义的聚合指标。

您可以通过定义一个函数（或任何可调用对象）来在整个测试级别上定义任何批量指标，该函数接受一组Runs（系统跟踪）和Example（数据集记录）。


```python
from typing import List


def max_pred_length(runs: List[Run], examples: List[Example]):
    predictions = [len(run.outputs["output"]) for run in runs]
    return EvaluationResult(key="max_pred_length", score=max(predictions))
```

下面，我们将使用上述自定义评估器以及一些预设的运行评估器来配置评估，这些评估器可以执行以下操作：
- 将结果与参考标签进行比较。
- 使用嵌入距离度量语义（不）相似性
- 使用自定义标准以无参考方式评估代理响应的“方面”。

关于如何为您的用例选择合适的评估器以及如何创建自定义评估器的更长讨论，请参阅[LangSmith文档](https://docs.smith.langchain.com/)。


```python
from langchain.evaluation import EvaluatorType
from langchain.smith import RunEvalConfig

evaluation_config = RunEvalConfig(
    # Evaluators can either be an evaluator type (e.g., "qa", "criteria", "embedding_distance", etc.) or a configuration for that evaluator
    evaluators=[
        check_not_idk,
        # Measures whether a QA response i对的“criteria”
        # You can select a default one such as "helpfulness" or provide your own.
        RunEvalConfig.LabeledCriteria("helpfulness"),
        # The LabeledScoreString evaluator outputs a score on a scale from 1-10.
        # You can use default criteria or write our own rubric
        RunEvalConfig.LabeledScoreString(
            {
                "accuracy": """
Score 1: The answer is completely unrelated to the reference.
Score 3: The answer has minor relevance but does not align with the reference.
Score 5: The answer has moderate relevance but contains inaccuracies.
Score 7: The answer aligns with the reference but has minor errors or omissions.
Score 10: The answer is completely accurate and aligns perfectly with the reference."""
            },
            normalize_by=10,
        ),
        EvaluatorType.QA,
        EvaluatorType.EMBEDDING_DISTANCE
    ],
    batch_evaluators=[max_pred_length],
)
```

### 4. 运行代理和评估器

使用[run_on_dataset](https://api.python.langchain.com/en/latest/smith/langchain.smith.evaluation.runner_utils.run_on_dataset.html#langchain.smith.evaluation.runner_utils.run_on_dataset)（或异步的[arun_on_dataset](https://api.python.langchain.com/en/latest/smith/langchain.smith.evaluation.runner_utils.arun_on_dataset.html#langchain.smith.evaluation.runner_utils.arun_on_dataset)）函数来评估模型。这将：
1. 从指定的数据集中获取示例行。
2. 在每个示例上运行您的代理程序（或任何自定义函数）。
3. 对生成的运行跟踪和相应的参考示例应用评估器以生成自动化反馈。

结果将在LangSmith应用中可见。


```python
from langchain import hub

# We will test this version of the prompt
prompt = hub.pull("wfh/langsmith-agent-prompt:798e7324")
```


```python
import functools

from langchain.smith import arun_on_dataset, run_on_dataset

chain_results = run_on_dataset(
    dataset_name=dataset_name,
    llm_or_chain_factory=functools.partial(
        create_agent, prompt=prompt, llm_with_tools=llm_with_tools
    ),
    evaluation=evaluation_config,
    verbose=True,
    client=client,
    project_name=f"tools-agent-test-5d466cbc-{unique_id}",
    # Project metadata communicates the experiment parameters,
    # Useful for reviewing the test results
    project_metadata={
        "env": "testing-notebook",
        "model": "gpt-3.5-turbo",
        "prompt": "5d466cbc",
    },
)

# 有时，由于解析问题、不兼容的工具输入等，代理会出现错误。
# 这些错误会在此处记录为警告，并在追踪UI中捕获为错误。

### 审查测试结果

你可以通过点击上面的输出URL或导航到LangSmith的“Testing & Datasets”页面，查看 **"agent-qa-{unique_id}"** 数据集的追踪UI中的测试结果。

![测试结果](/img/test_results.png)

这将显示新运行的结果以及从选定评估者记录的反馈。你还可以在下表中查看结果的摘要。

```python
chain_results.to_dataframe()
```

### （可选）与另一个提示进行比较

现在我们有了测试运行结果，我们可以对代理进行修改并对其进行基准测试。让我们用不同的提示再次尝试，看看结果。

```python
candidate_prompt = hub.pull("wfh/langsmith-agent-prompt:39f3bbd0")

chain_results = run_on_dataset(
    dataset_name=dataset_name,
    llm_or_chain_factory=functools.partial(
        create_agent, prompt=candidate_prompt, llm_with_tools=llm_with_tools
    ),
    evaluation=evaluation_config,
    verbose=True,
    client=client,
    project_name=f"tools-agent-test-39f3bbd0-{unique_id}",
    project_metadata={
        "env": "testing-notebook",
        "model": "gpt-3.5-turbo",
        "prompt": "39f3bbd0",
    },
)
```

## 导出数据集和运行结果

LangSmith 允许你在Web应用中直接将数据导出为常见格式如CSV或JSONL。你还可以使用客户端获取运行结果进行进一步分析，存储在自己的数据库中，或与他人分享。让我们从评估运行中获取运行追踪。

**注意：所有运行结果在可访问之前可能需要一些时间。**

```python
runs = client.list_runs(project_name=chain_results["project_name"], execution_order=1)


# 结果测试存储在一个项目中。可以通过编程方式访问测试的重要元数据，例如运行的数据集版本或应用程序的修订ID。
client.read_project(project_name=chain_results["project_name"]).metadata

```

```python
# 一段时间后，测试指标也会被填充。
client.read_project(project_name=chain_results["project_name"]).feedback_stats
```

## 结论


恭喜！您成功跟踪和评估了一个使用LangSmith的代理！

这是一个快速入门指南，但是使用LangSmith有很多其他的方式来加快开发流程并产生更好的结果。

要了解如何最大限度地发挥LangSmith的作用，请查看[LangSmith documentation](https://docs.smith.langchain.com/)，如果有任何问题、功能请求或反馈，请通过[support@langchain.dev](mailto:support@langchain.dev)联系我们。