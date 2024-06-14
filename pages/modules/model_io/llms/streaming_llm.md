# 流式处理

所有`LLM`都实现了`Runnable`接口，默认实现了所有方法，即ainvoke、batch、abatch、stream、astream。这使得所有`LLM`都具有基本的流式处理支持。

流式处理默认返回迭代器（在异步流式处理的情况下是AsyncIterator），其值为底层`LLM`提供程序返回的最终结果。这显然不能实现逐个标记的流式处理，这需要`LLM`提供程序的原生支持，但确保您的代码可以对任何我们的`LLM`集成进行标记迭代。

查看[哪些集成支持逐个标记的流式处理](/docs/integrations/llms/)。

```python
from langchain_openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0, max_tokens=512)
for chunk in llm.stream("Write me a song about sparkling water."):
    print(chunk, end="", flush=True)
```

    
    诗歌 1:
    水中舞动的气泡
    清澈而爽脆，简直太美好
    清爽的味道，像是梦一般
    汇聚成，我的喜悦，泉水
    
    重奏:
    噢，泉水，你是我的乐趣
    每一口，让我如此舒适
    你就像我的嘴里的派对
    我欲罢不能，我已无法自拔
    
    诗歌 2:
    无糖，无卡路里，纯粹的幸福
    你是完美的饮料，我必须承认
    从柠檬到青柠，有多种口味可供选择
    泉水，你总能让我感到惊喜
    
    重奏:
    噢，泉水，你是我的乐趣
    每一口，让我如此舒适
    你就像我的嘴里的派对
    我欲罢不能，我已无法自拔
    
    桥段:
    有些人可能会说你只是普通的水
    但对我而言，你是如此地重要
    你给我的每一天带来了一点闪耀
    在每一个方面
    
    重奏:
    噢，泉水，你是我的乐趣
    每一口，让我如此舒适
    你就像我的嘴里的派对
    我欲罢不能，我已无法自拔
    
    尾声:
    因此，致敬你，我亲爱的泉水
    你永远是我永远的最爱
    你的气泡和清新的味道
    你永远都有一个特殊的位置。

