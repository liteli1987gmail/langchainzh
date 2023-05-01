import os
import asyncio
import aiohttp
import aiofiles
import json
import requests

# 遍历的文件夹路径
orignType = ".md"
folder_path = "./pages/modules/memory/examples"

# 接口请求地址
api_url = "https://api.openai.com/v1/chat/completions"

# 定义chat连接池
async def chat(session, url, headers, payload):
    async with session.post(url, headers=headers, json=payload) as response:
        response_data = await response.json()
        if 'choices' in response_data:
            messages = response_data['choices'][0]['message']['content']
            return messages
        return ''

# 定义异步的接口请求方法
async def get_responses(content):
    async with aiohttp.ClientSession() as session:
        url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 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" 
        }
        tasks = []
        p = """
        请将以下markdown格式的内容，翻译为中文，代码块不用翻译，请保持markdown格式输出。需要翻译的内容是：
        """ + content
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "text": p}],
            "temperature": 0.7
        }
        task = asyncio.ensure_future(await chat(session, url, headers, payload))
        tasks.append(task)
        responses = await asyncio.gather(*tasks)
        return responses


# 这个模板为getOpenAIapi函数
async def getOpenAIapi(encontent):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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" 
    }
    p = """
    请将以下markdown格式的内容，翻译为中文，代码块不用翻译，请保持markdown格式输出。需要翻译的内容是：
    """ + encontent
    payload = {
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": p}],
     "temperature": 0.7
   }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response)
    response_data = response.json()
    if 'choices' in response_data:
        messages = response_data['choices'][0]['message']['content']
        return messages
    return ''
    # return response.json()['choices'][0]['message']['content']

async def fetch(session, url, data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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" 
    }
    async with session.post(url,headers=headers, json=data) as response:
        response_data = response.json()
        if 'choices' in response_data:
            messages = response_data['choices'][0]['message']['content']
            return messages
        return None
        # return await response.json()['choices'][0]['message']['content']
    

# 定义异步的写入文件方法
async def write_file(file_path, content):
    print('定义异步的写入文件方法')
    async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
        await f.write(content)

# 遍历文件夹及文件，将文件内容异步切割、异步发送接口请求、异步写入mdx文件
async def process_file(file_path):
    print(file_path)
    # 读取文件内容
    async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
        content = await f.read()
    print('判断文件内容长度是否超过1000个字符' + str(len(content)))
    # 判断文件内容长度是否超过1000个字符
    if len(content) > 1000:
        # 将内容切割成块
        chunks = [content[i:i+1000] for i in range(0, len(content), 1000)]
    else:
        chunks = [content]
    print(chunks)
    # 创建Session
    async with aiohttp.ClientSession() as session:
        # 异步发送接口请求并处理结果
        tasks = []
        prefix = "请将以下markdown格式的内容，翻译为中文，代码块不用翻译，请保持markdown格式输出。需要翻译的内容是："
        for chunk in chunks:
            # data = {"content": prefix + chunk }
            await asyncio.sleep(10)
            task = asyncio.create_task(getOpenAIapi(prefix + chunk))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        print(results)
        result = "".join(results)

    # 构造新文件名
    new_file_path = file_path.replace(orignType , ".mdx")

    # 异步写入mdx文件
    await write_file(new_file_path, result)

# 遍历文件夹
async def process_folder():
    print('遍历文件夹')
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 判断文件是否为md类型
            if file.endswith(".mdx"):
                file_path = os.path.join(root, file)
                await process_file(file_path)

# 运行异步任务
async def main():
    await process_folder()

asyncio.run(main())