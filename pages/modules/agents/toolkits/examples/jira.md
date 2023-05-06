

# 使用Jira工具[#](#jira-tool "Permalink to this headline")

本笔记本将介绍如何使用Jira工具。

Jira工具允许代理与给定的Jira实例交互，执行诸如搜索问题和创建问题等操作，该工具包装了atlassian-python-api库，了解更多请参见：https://atlassian-python-api.readthedocs.io/jira

要使用此工具，必须首先设置以下环境变量：

`JIRA_API_TOKEN`

`JIRA_USERNAME`

`JIRA_INSTANCE_URL`
 







```
%pip install atlassian-python-api

```










```
import os
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits.jira.toolkit import JiraToolkit
from langchain.llms import OpenAI
from langchain.utilities.jira import JiraAPIWrapper

```










```
os.environ["JIRA_API_TOKEN"] = "abc"
os.environ["JIRA_USERNAME"] = "123"
os.environ["JIRA_INSTANCE_URL"] = "https://jira.atlassian.com"
os.environ["OPENAI_API_KEY"] = "xyz"

```










```
llm = OpenAI(temperature=0)
jira = JiraAPIWrapper()
toolkit = JiraToolkit.from_jira_api_wrapper(jira)
agent = initialize_agent(
    toolkit.get_tools(),
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

```










```
agent.run("make a new issue in project PW to remind me to make more fried rice")

```








```
> Entering new AgentExecutor chain...
 I need to create an issue in project PW
Action: Create Issue
Action Input: {"summary": "Make more fried rice", "description": "Reminder to make more fried rice", "issuetype": {"name": "Task"}, "priority": {"name": "Low"}, "project": {"key": "PW"}}
Observation: None
Thought: I now know the final answer
Final Answer: A new issue has been created in project PW with the summary "Make more fried rice" and description "Reminder to make more fried rice".

> Finished chain.

```






```
'A new issue has been created in project PW with the summary "Make more fried rice" and description "Reminder to make more fried rice".'

```







