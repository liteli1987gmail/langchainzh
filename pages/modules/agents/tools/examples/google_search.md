


 Google Search
 [#](#google-search "Permalink to this headline")
=================================================================



 This notebook goes over how to use the google search component.
 



 First, you need to set up the proper API keys and environment variables. To set it up, create the GOOGLE_API_KEY in the Google Cloud credential console (https://console.cloud.google.com/apis/credentials) and a GOOGLE_CSE_ID using the Programmable Search Enginge (https://programmablesearchengine.google.com/controlpanel/create). Next, it is good to follow the instructions found
 [here](https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search) 
 .
 



 Then we will need to set some environment variables.
 







```
import os
os.environ["GOOGLE_CSE_ID"] = ""
os.environ["GOOGLE_API_KEY"] = ""

```










```
from langchain.utilities import GoogleSearchAPIWrapper

```










```
search = GoogleSearchAPIWrapper()

```










```
search.run("Obama's first name?")

```








```
'1 Child\'s First Name. 2. 6. 7d. Street Address. 71. (Type or print). BARACK. Sex. 3. This Birth. 4. If Twin or Triplet,. Was Child Born. Barack Hussein Obama II is an American retired politician who served as the 44th president of the United States from 2009 to 2017. His full name is Barack Hussein Obama II. Since the “II” is simply because he was named for his father, his last name is Obama. Feb 9, 2015 ... Michael Jordan misspelled Barack Obama\'s first name on 50th-birthday gift ... Knowing Obama is a Chicagoan and huge basketball fan,\xa0... Aug 18, 2017 ... It took him several seconds and multiple clues to remember former President Barack Obama\'s first name. Miller knew that every answer had to end\xa0... First Lady Michelle LaVaughn Robinson Obama is a lawyer, writer, and the wife of the 44th President, Barack Obama. She is the first African-American First\xa0... Barack Obama, in full Barack Hussein Obama II, (born August 4, 1961, Honolulu, Hawaii, U.S.), 44th president of the United States (2009–17) and the first\xa0... When Barack Obama was elected president in 2008, he became the first African American to hold ... The Middle East remained a key foreign policy challenge. Feb 27, 2020 ... President Barack Obama was born Barack Hussein Obama, II, as shown here on his birth certificate here . As reported by Reuters here , his\xa0... Jan 16, 2007 ... 4, 1961, in Honolulu. His first name means "one who is blessed" in Swahili. While Obama\'s father, Barack Hussein Obama Sr., was from Kenya, his\xa0...'

```







 Number of Results
 [#](#number-of-results "Permalink to this headline")
-------------------------------------------------------------------------



 You can use the
 `k`
 parameter to set the number of results
 







```
search = GoogleSearchAPIWrapper(k=1)

```










```
search.run("python")

```








```
'The official home of the Python Programming Language.'

```






 ‘The official home of the Python Programming Language.’
 





 Metadata Results
 [#](#metadata-results "Permalink to this headline")
-----------------------------------------------------------------------



 Run query through GoogleSearch and return snippet, title, and link metadata.
 


* Snippet: The description of the result.
* Title: The title of the result.
* Link: The link to the result.







```
search = GoogleSearchAPIWrapper()

```










```
search.results("apples", 5)

```








```
[{'snippet': 'Discover the innovative world of Apple and shop everything iPhone, iPad, Apple Watch, Mac, and Apple TV, plus explore accessories, entertainment,\xa0...',
  'title': 'Apple',
  'link': 'https://www.apple.com/'},
 {'snippet': "Jul 10, 2022 ... Whether or not you're up on your apple trivia, no doubt you know how delicious this popular fruit is, and how nutritious. Apples are rich in\xa0...",
  'title': '25 Types of Apples and What to Make With Them - Parade ...',
  'link': 'https://parade.com/1330308/bethlipton/types-of-apples/'},
 {'snippet': 'An apple is an edible fruit produced by an apple tree (Malus domestica). Apple trees are cultivated worldwide and are the most widely grown species in the\xa0...',
  'title': 'Apple - Wikipedia',
  'link': 'https://en.wikipedia.org/wiki/Apple'},
 {'snippet': 'Apples are a popular fruit. They contain antioxidants, vitamins, dietary fiber, and a range of other nutrients. Due to their varied nutrient content,\xa0...',
  'title': 'Apples: Benefits, nutrition, and tips',
  'link': 'https://www.medicalnewstoday.com/articles/267290'},
 {'snippet': "An apple is a crunchy, bright-colored fruit, one of the most popular in the United States. You've probably heard the age-old saying, “An apple a day keeps\xa0...",
  'title': 'Apples: Nutrition & Health Benefits',
  'link': 'https://www.webmd.com/food-recipes/benefits-apples'}]

```








