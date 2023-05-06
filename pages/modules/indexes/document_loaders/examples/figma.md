Figma [#](#figma "Permalink to this headline")
=================================================

本文介绍如何从Figma REST API加载数据并将数据转换成可用于LangChain的格式，以及用于代码生成的示例用法。

```
import os
from langchain.document_loaders.figma import FigmaFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import ConversationChain, LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
```

要使用 Figma API，需要接入令牌(access token)、节点ID(node_ids)和文件键(file key)。

文件键(file key)可以从URL中提取。URL格式为https://www.figma.com/file/{filekey}/sampleFilename。

节点ID(node_ids)也可以在URL中提取。点击各项，查找 " ?node-id={node_id}" 参数。

有关访问令牌的说明请参见 Figma 帮助中心文章: https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens

```
figma_loader = FigmaFileLoader(
    os.environ.get('ACCESS_TOKEN'),
    os.environ.get('NODE_IDS'),
    os.environ.get('FILE_KEY')
)
```

```
# see https://python.langchain.com/en/latest/modules/indexes/getting_started for more details
index = VectorstoreIndexCreator().from_loaders([figma_loader])
figma_doc_retriever = index.vectorstore.as_retriever()
```

生成代码：

```
def generate_code(human_input):
    system_prompt_template = """You are expert coder Jon Carmack. Use the provided design context to create idomatic HTML/CSS code as possible based on the user request.
 Everything must be inline in one file and your response must be directly renderable by the browser.
 Figma file nodes and metadata: {context}"""

    human_prompt_template = "Code the {text}. Ensure it's mobile responsive"
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_prompt_template)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_prompt_template)
    gpt_4 = ChatOpenAI(temperature=.02, model_name='gpt-4')
    relevant_nodes = figma_doc_retriever.get_relevant_documents(human_input)
    conversation = [system_message_prompt, human_message_prompt]
    chat_prompt = ChatPromptTemplate.from_messages(conversation)
    response = gpt_4(chat_prompt.format_prompt(
        context=relevant_nodes,
        text=human_input).to_messages())
    return response
```

返回的结果将存储在 `response.content` 中，示例如下：

```
<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <style>\n        @import url(\'https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Inter:wght@600&display=swap\');\n\n        body {\n            margin: 0;\n            font-family: \'DM Sans\', sans-serif;\n        }\n\n        .header {\n            display: flex;\n            justify-content: space-between;\n            align-items: center;\n            padding: 20px;\n            background-color: #fff;\n            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);\n        }\n\n        .header h1 {\n            font-size: 16px;\n            font-weight: 700;\n            margin: 0;\n        }\n\n        .header nav {\n            display: flex;\n            align-items: center;\n        }\n\n        .header nav a {\n            font-size: 14px;\n            font-weight: 500;\n            text-decoration: none;\n            color: #000;\n            margin-left: 20px;\n        }\n\n        @media (max-width: 768px) {\n            .header nav {\n                display: none;\n            }\n        }\n    </style>\n</head>\n<body>\n    <header class="header">\n        <h1>Company Contact</h1>\n        <