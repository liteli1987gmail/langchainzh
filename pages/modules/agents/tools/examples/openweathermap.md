


 OpenWeatherMap API
 [#](#openweathermap-api "Permalink to this headline")
===========================================================================



 This notebook goes over how to use the OpenWeatherMap component to fetch weather information.
 



 First, you need to sign up for an OpenWeatherMap API key:
 


1. Go to OpenWeatherMap and sign up for an API key
 [here](https://openweathermap.org/api/)
2. pip install pyowm



 Then we will need to set some environment variables:
 


1. Save your API KEY into OPENWEATHERMAP_API_KEY env variable







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







