# YouTube

如何从YouTube字幕中加载文档。

``` python
from langchain.document_loaders import YoutubeLoader
```

``` python
# !pip install youtube-transcript-api

loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=QsYGlZkevEg", add_video_info=True)
```

``` python
loader.load()
```

添加视频信息

``` python
# ! pip install pytube

loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=QsYGlZkevEg", add_video_info=True)

loader.load()
```

从Google Cloud中的YouTube加载器

### 预备条件

1. 创建一个Google Cloud项目或使用现有项目
2. 启用Youtube API
3. 为桌面应用程序授权凭据
4. `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib youtube-transcript-api`

``` python
from langchain.document_loaders import GoogleApiClient, GoogleApiYoutubeLoader
from pathlib import Path

# 初始化GoogleApiClient
google_api_client = GoogleApiClient(credentials_path=Path("your_path_creds.json"))

# 使用频道
youtube_loader_channel = GoogleApiYoutubeLoader(google_api_client=google_api_client, channel_name="Reducible",captions_language="en")

# 使用Youtube ID
youtube_loader_ids = GoogleApiYoutubeLoader(google_api_client=google_api_client, video_ids=["TrdevFK_am4"], add_video_info=True)

# 返回文档列表
youtube_loader_channel.load()
```