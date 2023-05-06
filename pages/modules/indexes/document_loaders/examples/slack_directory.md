# Slack (本地导出Zip文件)

本笔记本介绍了如何从Slack导出的Zip文件中加载文档。

为了获得这个Slack导出文件，请按照以下说明操作：

🧑 摄入自己的数据集的说明

导出您的Slack数据。您可以通过转到Workspace Management页面并单击导入/导出选项（{your_slack_domain}.slack.com/services/export）来完成此操作。然后，选择正确的日期范围，然后单击“Start export”。当导出准备就绪时，Slack会向您发送电子邮件和DM。

下载将在您的下载文件夹中生成.zip文件（或者根据您的操作系统配置，可以在任何地方找到下载文件）。

复制.zip文件的路径，并将其分配为下面的LOCAL_ZIPFILE。

``` python
from langchain.document_loaders import SlackDirectoryLoader
```

``` python
# 可选择设置你的Slack URL，这将在文档中为您提供正确的URL。
SLACK_WORKSPACE_URL = "https://xxx.slack.com"
LOCAL_ZIPFILE = "" # 将本地路径粘贴到Slack zip文件中。

loader = SlackDirectoryLoader(LOCAL_ZIPFILE, SLACK_WORKSPACE_URL)
```

``` python
docs = loader.load()
docs
```