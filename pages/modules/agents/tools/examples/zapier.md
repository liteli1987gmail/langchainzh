
Zapier
================

完整文档在此处：https://nla.zapier.com/api/v1/docs

**Zapier自然语言操作**通过自然语言API接口为您提供对Zapier平台上5k+应用程序和20k+操作的访问权限。

NLA支持Gmail、Salesforce、Trello、Slack、Asana、HubSpot、Google Sheets、Microsoft Teams等应用程序以及数千个其他应用程序：https://zapier.com/apps。

Zapier NLA处理所有底层API授权和自然语言翻译- >基础API调用- >返回简化输出的操作。关键思想是，您或您的用户通过类似于OAuth的设置窗口公开一组动作，然后可以通过REST API查询和执行。

NLA为签署NLA API请求提供API密钥和OAuth。

1. 服务器端（API密钥）：用于快速入门，测试和生产场景，其中LangChain仅使用开发人员Zapier帐户中公开的操作（并将使用开发人员在Zapier.com上连接的帐户）

2. 面向用户（Oauth）：用于部署面向最终用户的应用程序并且LangChain需要访问Zapier.com上最终用户的操作和连接账户的生产场景。

为简洁起见，此快速入门将重点关注服务器端用例。查看完整文档或联系nla@zapier.com获取面向用户的oauth开发者支持。

此示例介绍如何使用Zapier集成`SimpleSequentialChain`，然后使用`Agent`。
下面是代码：

```
%load_ext autoreload
%autoreload 2

```

```
import os

# get from https://platform.openai.com/
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "")

# get from https://nla.zapier.com/demo/provider/debug (under User Information, after logging in): 
os.environ["ZAPIER_NLA_API_KEY"] = os.environ.get("ZAPIER_NLA_API_KEY", "")

```

使用Agent的示例[#](#example-with-agent "此标题的永久链接")
---------------------------------------------

Zapier工具可与代理一起使用。请参见下面的示例。

```
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.agents import AgentType
from langchain.utilities.zapier import ZapierNLAWrapper

```

```
## step 0. expose gmail 'find email' and slack 'send channel message' actions

# first go here, log in, expose (enable) the two actions: https://nla.zapier.com/demo/start -- for this example, can leave all fields "Have AI guess"
# in an oauth scenario, you'd get your own <provider> id (instead of 'demo') which you route your users through first

```

```
llm = OpenAI(temperature=0)
zapier = ZapierNLAWrapper()
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent = initialize_agent(toolkit.get_tools(), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

```

```
agent.run("Summarize the last email I received regarding Silicon Valley Bank. Send the summary to the #test-zapier channel in slack.")

```

```
> Entering new AgentExecutor chain...
 I need to find the email and summarize it.
Action: Gmail: Find Email
Action Input: Find the latest email from Silicon Valley Bank
Observation: {"from__name": "Silicon Valley Bridge Bank, N.A.", "from__email": "sreply@svb.com", "body_plain": "Dear Clients, After chaotic, tumultuous & stressful days, we have clarity on path for SVB, FDIC is fully insuring all deposits & have an ask for clients & partners as we rebuild. Tim Mayopoulos <https://eml.svb.com/NjEwLUtBSy0yNjYAAAGKgoxUeBCLAyF_NxON97X4rKEaNBLG", "reply_to__email": "sreply@svb.com", "subject": "Meet the new CEO Tim Mayopoulos", "date": "Tue, 14 Mar 2023 23:42:29 -0500 (CDT)", "message_url": "https://mail.google.com/mail/u/0/#inbox/186e393b13cfdf0a", "attachment_count": "0", "to__emails": "ankush@langchain.dev", "message_id": "186e393b13cfdf0a", "labels": "IMPORTANT, CATEGORY_UPDATES, INBOX"}
Thought: I need to summarize the email and send it to the #test-zapier channel in Slack.
Action: Slack: Send Channel Message
Action Input: Send a slack message to the #test-zapier channel with the text "Silicon Valley Bank has announced that Tim Mayopoulos is the new CEO. FDIC is fully insuring all deposits and they have an ask for clients and partners as they rebuild."
Observation: {"message__text": "Silicon Valley Bank has announced that Tim Mayopoulos is the new CEO. FDIC is fully insuring all deposits and they have an ask for clients and partners as they rebuild.", "message__permalink": "https://langchain.slack.com/archives/C04TSGU0RA7/p1678859932375259", "channel": "C04TSGU0RA7", "message__bot_profile__name": "Zapier", "message__team": "T04F8K3FZB5", "message__bot_id": "B04TRV4R74K", "message__bot_profile__deleted": "false", "message__bot_profile__app_id": "A024R9PQM", "ts_time": "2023-03-15T05:58:52Z", "message__bot_profile__icons__image_36": "https://avatars.slack-edge.com/2022-08-02/3888649620612_f864dc1bb794cf7d82b0_36.png", "message__blocks[]block_id": "kdZZ", "message__blocks[]elements[]type": "['rich_text_section']"}
Thought: I now know the final answer.
Final Answer: I have sent a summary of the last email from Silicon Valley Bank to the #test-zapier channel in Slack.

> Finished chain.

```

```
'I have sent a summary of the last email from Silicon Valley Bank to the #test-zapier channel in Slack.'

```

使用SimpleSequentialChain的示例[#](#example-with-simplesequentialchain "此标题的永久链接")
=============================================================================

如果需要更明确的控制，请使用如下所示的链。

```
from langchain.llms import OpenAI
from langchain.chains import LLMChain, TransformChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain.tools.zapier.tool import ZapierNLARunAction
from langchain.utilities.zapier import ZapierNLAWrapper

```

```
## step 0. expose gmail 'find email' and slack 'send direct message' actions

# first go here, log in, expose (enable) the two actions: https://nla.zapier.com/demo/start -- for this example, can leave all fields "Have AI guess"
# in an oauth scenario, you'd get your own <provider> id (instead of 'demo') which you route your users through first

actions = ZapierNLAWrapper().list()

```

```
## step 1. gmail find email

GMAIL_SEARCH_INSTRUCTIONS = "Grab the latest email from Silicon Valley Bank"

def nla_gmail(inputs):
    action = next((a for a in actions if a["description"].startswith("Gmail: Find Email")), None)
    return {"email_data": ZapierNLARunAction(action_id=action["id"], zapier_description=action["description"], params_schema=action["params"]).run(inputs["instructions"])}
gmail_chain = TransformChain(input_variables=["instructions"], output_variables=["email_data"], transform=nla_gmail)

```

```
## step 2. generate draft reply

template = """You are an assisstant who drafts replies to an incoming email. Output draft reply in plain text (not JSON).

Incoming email:
{email_data}

Draft email reply:"""

prompt_template = PromptTemplate(input_variables=["email_data"], template=template)
reply_chain = LLMChain(llm=OpenAI(temperature=.7), prompt=prompt_template)

```

```
## step 3. send draft reply via a slack direct message

SLACK_HANDLE = "@Ankush Gola"

def nla_slack(inputs):
    action = next((a for a in actions if a["description"].startswith("Slack: Send Direct Message")), None)
    instructions = f'Send this to {SLACK_HANDLE} in Slack: {inputs["draft_reply"]}'
    return {"slack_data": ZapierNLARunAction(action_id=action["id"], zapier_description=action["description"], params_schema=action["params"]).run(instructions)}
slack_chain = TransformChain(input_variables=["draft_reply"], output_variables=["slack_data"], transform=nla_slack)

```

```
## finally, execute

overall_chain = SimpleSequentialChain(chains=[gmail_chain, reply_chain, slack_chain], verbose=True)
overall_chain.run(GMAIL_SEARCH_INSTRUCTIONS)

```

```
> Entering new SimpleSequentialChain chain...
{"from__name": "Silicon Valley Bridge Bank, N.A.", "from__email": "sreply@svb.com", "body_plain": "Dear Clients, After chaotic, tumultuous & stressful days, we have clarity on path for SVB, FDIC is fully insuring all deposits & have an ask for clients & partners as we rebuild. Tim Mayopoulos <https://eml.svb.com/NjEwLUtBSy0yNjYAAAGKgoxUeBCLAyF_NxON97X4rKEaNBLG", "reply_to__email": "sreply@svb.com", "subject": "Meet the new CEO Tim Mayopoulos", "date": "Tue, 14 Mar 2023 23:42:29 -0500 (CDT)", "message_url": "https://mail.google.com/mail/u/0/#inbox/186e393b13cfdf0a", "attachment_count": "0", "to__emails": "ankush@langchain.dev", "message_id": "186e393b13cfdf0a", "labels": "IMPORTANT, CATEGORY_UPDATES, INBOX"}

Dear Silicon Valley Bridge Bank, 

Thank you for your email and the update regarding your new CEO Tim Mayopoulos. We appreciate your dedication to keeping your clients and partners informed and we look forward to continuing our relationship with you. 

Best regards, 
[Your Name]
{"message__text": "Dear Silicon Valley Bridge Bank,   Thank you for your email and the update regarding your new CEO Tim Mayopoulos. We appreciate your dedication to keeping your clients and partners informed and we look forward to continuing our relationship with you.   Best regards, \n[Your Name]", "message__permalink": "https://langchain.slack.com/archives/D04TKF5BBHU/p1678859968241629", "channel": "D04TKF5BBHU", "message__bot_profile__name": "Zapier", "message__team": "T04F8K3FZB5", "message__bot_id": "B04TRV4R74K", "message__bot_profile__deleted": "false", "message__bot_profile__app_id": "A024R9PQM", "ts_time": "2023-03-15T05:59:28Z", "message__blocks[]block_id": "p7i", "message__blocks[]elements[]elements[]type": "[['text']]", "message__blocks[]elements[]type": "['rich_text_section']"}

> Finished chain.

```

```
'{"message__text": "Dear Silicon Valley Bridge Bank, \\n\\nThank you for your email and the update regarding your new CEO Tim Mayopoulos. We appreciate your dedication to keeping your clients and partners informed and we look forward to continuing our relationship with you. \\n\\nBest regards, \\n[Your Name]", "message__permalink": "https://langchain.slack.com/archives/D04TKF5BBHU/p1678859968241629", "channel": "D04TKF5BBHU", "message__bot_profile__name": "Zapier", "message__team": "T04F8K3FZB5", "message__bot_id": "B04TRV4R74K", "message__bot_profile__deleted": "false", "message__bot_profile__app_id": "A024R9PQM", "ts_time": "2023-03-15T05:59:28Z", "message__blocks[]block_id": "p7i", "message__blocks[]elements[]elements[]type": "[[\'text\']]", "message__blocks[]elements[]type": "[\'rich_text_section\']"}'

```

