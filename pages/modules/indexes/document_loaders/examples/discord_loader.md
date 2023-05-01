


 Discord
 [#](#discord "Permalink to this headline")
=====================================================



 You can follow the below steps to download your Discord data:
 


1. Go to your
 **User Settings**
2. Then go to
 **Privacy and Safety**
3. Head over to the
 **Request all of my Data** 
 and click on
 **Request Data** 
 button



 It might take 30 days for you to receive your data. You’ll receive an email at the address which is registered with Discord. That email will have a download button using which you would be able to download your personal Discord data.
 







```
import pandas as pd
import os

```










```
path = input("Please enter the path to the contents of the Discord \"messages\" folder: ")
li = []
for f in os.listdir(path):
    expected_csv_path = os.path.join(path, f, 'messages.csv')
    csv_exists = os.path.isfile(expected_csv_path)
    if csv_exists:
        df = pd.read_csv(expected_csv_path, index_col=None, header=0)
        li.append(df)

df = pd.concat(li, axis=0, ignore_index=True, sort=False)

```










```
from langchain.document_loaders.discord import DiscordChatLoader

```










```
loader = DiscordChatLoader(df, user_id_col="ID")
print(loader.load())

```







