Reddit
==========================================================

Reddit是一家美国社交新闻汇总、内容评级和讨论网站。

此载入器使用Python包'praw'从Subreddit或Reddit用户的帖子中获取文本。

需要先创建[Reddit应用程序](https://www.reddit.com/prefs/apps/)，并使用您的Reddit API凭据初始化载入器。

用法：

```
from langchain.document_loaders import RedditPostsLoader

# load using 'subreddit' mode
loader = RedditPostsLoader(
    client_id="YOUR CLIENT ID",
    client_secret="YOUR CLIENT SECRET",
    user_agent="extractor by u/Master_Ocelot8179",
    categories=['new', 'hot'],                              # List of categories to load posts from
    mode = 'subreddit',
    search_queries=['investing', 'wallstreetbets'],         # List of subreddits to load posts from
    number_posts=20                                         # Default value is 10
    )

# # or load using 'username' mode
# loader = RedditPostsLoader(
# client_id="YOUR CLIENT ID",
# client_secret="YOUR CLIENT SECRET",
# user_agent="extractor by u/Master_Ocelot8179",
# categories=['new', 'hot'], 
# mode = 'username',
# search_queries=['ga3far', 'Master_Ocelot8179'], # List of usernames to load posts from
# number_posts=20
# )

# Note: Categories can be only of following value - "controversial" "hot" "new" "rising" "top"

documents = loader.load()
```

返回结果是一个Document对象列表，其中每个对象包含帖子的内容、元数据和索引。