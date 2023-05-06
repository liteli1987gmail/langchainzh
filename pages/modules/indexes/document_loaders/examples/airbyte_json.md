

Airbyte JSON[#](#airbyte-json "跳转到标题")
======================================

> 
> [Airbyte](https://github.com/airbytehq/airbyte)是一个数据集成平台，可将API、数据库和文件的ELT数据管道传输到数据仓库和数据湖中。它拥有最大的ELT连接器目录，可用于数据仓库和数据库。
> 
> 
> 

本文介绍如何将Airbyte中的任何来源加载到本地JSON文件中，以便作为文档读取。

先决条件：安装了Docker桌面版

步骤：

- 从GitHub上克隆Airbyte - `git clone https://github.com/airbytehq/airbyte.git`

- 切换到Airbyte目录 - `cd airbyte`

- 启动Airbyte - `docker compose up`

- 在浏览器中，只需访问 http://localhost:8000。您将被要求输入用户名和密码。默认情况下，用户名是 `airbyte` ，密码是 `password`。

- 设置任何您想要的源。

- 将目标设置为本地JSON，指定目标路径-假设为`/json_data`。设置手动同步。

- 运行连接。

- 要查看创建了哪些文件，可以导航到：`file:///tmp/airbyte_local`

- 找到您的数据并复制路径。该路径应保存在下面的文件变量中。它应该以`/tmp/airbyte_local`开头

```
from langchain.document_loaders import AirbyteJSONLoader

```

```
!ls /tmp/airbyte_local/json_data/

```

```
_airbyte_raw_pokemon.jsonl

```

```
loader = AirbyteJSONLoader('/tmp/airbyte_local/json_data/_airbyte_raw_pokemon.jsonl')

```

```
data = loader.load()

```

```
print(data[0].page_content[:500])

```

```
abilities: 
ability: 
name: blaze
url: https://pokeapi.co/api/v2/ability/66/

is_hidden: False
slot: 1

ability: 
name: solar-power
url: https://pokeapi.co/api/v2/ability/94/

is_hidden: True
slot: 3

base_experience: 267
forms: 
name: charizard
url: https://pokeapi.co/api/v2/pokemon-form/6/

game_indices: 
game_index: 180
version: 
name: red
url: https://pokeapi.co/api/v2/version/1/

game_index: 180
version: 
name: blue
url: https://pokeapi.co/api/v2/version/2/

game_index: 180
version: 
n

```

