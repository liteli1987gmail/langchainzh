OpenWeatherMap
=================

本教程将介绍如何使用OpenWeatherMap组件获取天气信息。

首先，您需要注册OpenWeatherMap API密钥：

1. 前往OpenWeatherMap并注册API密钥 [这里](https://openweathermap.org/api/)
2. 安装pyowm：'pip install pyowm'

然后，我们需要设置一些环境变量：

1. 将您的API KEY保存到OPENWEATHERMAP_API_KEY环境变量中

```
pip install pyowm

```

```
import os
os.environ["OPENWEATHERMAP_API_KEY"] = ""

```

```
from langchain.utilities import OpenWeatherMapAPIWrapper

```

```
weather = OpenWeatherMapAPIWrapper()

```

```
weather_data = weather.run("London,GB")

```

```
print(weather_data)

```

```
In London,GB, the current weather is as follows:
Detailed status: overcast clouds
Wind speed: 4.63 m/s, direction: 150°
Humidity: 67%
Temperature: 
  - Current: 5.35°C
  - High: 6.26°C
  - Low: 3.49°C
  - Feels like: 1.95°C
Rain: {}
Heat index: None
Cloud cover: 100%

```

