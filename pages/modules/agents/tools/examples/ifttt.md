
IFTTT Webhooks
=================


这篇笔记展示了如何使用IFTTT Webhooks。

来自https://github.com/SidU/teams-langchain-js/wiki/Connecting-IFTTT-Services。

创建Webhook[#](#creating-a-webhook "Permalink to this headline")
--------------------------------------------------------------

* 访问https://ifttt.com/create

配置“If This”[#](#configuring-the-if-this "Permalink to this headline")
---------------------------------------------------------------------

* 在IFTTT界面上单击“If This”按钮。

* 在搜索栏中搜索“Webhooks”。

* 选择“接收带有JSON有效负载的Web请求”的第一个选项。

* 选择一个与您计划连接的服务具体相关的事件名称。这将使您更容易管理Webhook URL。例如，如果您连接到Spotify，您可以使用“Spotify”作为您的事件名称。
* Click the “Create Trigger” button to save your settings and create your webhook.

配置“那么”（Then That)

* 在IFTTT界面中点击“那么”按钮。
* 搜索您要连接的服务，如Spotify。
* 选择要从服务中执行的操作，例如“添加到播放列表”。
* 通过指定必要的细节来配置操作，例如播放列表名称，例如“来自AI的歌曲”。
* 在操作中引用Webhook接收到的JSON负载。对于Spotify场景，将“{{JsonPayload}}”作为您的搜索查询。
* 单击“创建操作”按钮以保存您的操作设置。

* 一旦您完成操作的配置，请单击“完成”按钮以完成设置。

* 恭喜！您已成功将Webhook连接到所需的服务，现在您可以开始接收数据并触发操作 🎉

完成[#](#finishing-up "Permalink to this headline")
-------------------------------------------------

* 要获取您的Webhook URL，请访问https://ifttt.com/maker_webhooks/settings

* 从那里复制IFTTT密钥值。 URL的格式为
https://maker.ifttt.com/use/YOUR_IFTTT_KEY。获取YOUR_IFTTT_KEY值。

```
from langchain.tools.ifttt import IFTTTWebhook

```

```
import os
key = os.environ["IFTTTKey"]
url = f"https://maker.ifttt.com/trigger/spotify/json/with/key/{key}"
tool = IFTTTWebhook(name="Spotify", description="Add a song to spotify playlist", url=url)

```

```
tool.run("taylor swift")

```

```
"Congratulations! You've fired the spotify JSON event"

```

