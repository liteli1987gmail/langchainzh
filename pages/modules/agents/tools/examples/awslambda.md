

AWS Lambda API[#](#aws-lambda-api "本标题的永久链接")
=============================================

本笔记介绍如何使用AWS Lambda Tool组件。

AWS Lambda是由亚马逊网络服务（AWS)提供的无服务器计算服务，旨在使开发人员能够构建和运行应用程序和服务，而无需预配或管理服务器。这种无服务器架构使您可以专注于编写和部署代码，而AWS会自动处理扩展、修补和管理运行应用程序所需的基础设施。

通过在提供给代理的工具列表中包含`awslambda`，您可以授予代理在您的AWS云中调用运行代码的能力，以满足您的各种需求。

当代理使用awslambda工具时，它将提供一个字符串类型的参数，该参数将通过事件参数传递到Lambda函数中。

首先，您需要安装`boto3` Python包。

```
!pip install boto3 > /dev/null

```

为了使代理使用该工具，您必须提供与您Lambda函数逻辑功能匹配的名称和描述。

您还必须提供函数的名称。

请注意，由于此工具实际上只是boto3库的包装器，因此您需要运行`aws configure`才能使用该工具。有关更多详细信息，请参见[此处](https://docs.aws.amazon.com/cli/index)

```
from langchain import OpenAI
from langchain.agents import load_tools, AgentType

llm = OpenAI(temperature=0)

tools = load_tools(
    ["awslambda"],
    awslambda_tool_name="email-sender",
    awslambda_tool_description="sends an email with the specified content to test@testing123.com",
    function_name="testFunction1"
)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("Send an email to test@testing123.com saying hello world.")

```

