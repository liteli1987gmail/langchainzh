import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urlparse

from markdownify import markdownify

# url的网页规律：<article class="bd-article" role="main">
# modules use_cases reference ecosystem
modules = 'modules'
with open(modules +".txt", "r") as f:
    links = [line.strip() for line in f]

print(links)

# 定义函数将 HTML 内容转换为 Markdown 并保存到文件中
def html_to_mdx(url):
    # 请求目标网页并将其解析为 BeautifulSoup 对象
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到需要转换成 Markdown 格式并保存到文件的内容<article class="bd-article" role="main">
    section = soup.find("article", class_="bd-article")
    md = markdownify(section.prettify())
    non_blank_lines = []
    for line in md.split("\n"):
        if line.strip():
            non_blank_lines.append(line)
    # cleaned_content = "\n".join(non_blank_lines)
    cleaned_content = md.replace("\\_", "_").replace(".html", "")

    # 解析文件路径并创建文件夹
    # 解析URL，提取目录结构和文件名
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split("/")
    path_parts = [x for x in path_parts if x]  # 删除空字符串
    path_parts = ["pages"] + path_parts[2:]
    file_name = os.path.splitext(path_parts[-1])[0] + ".md"

    # 根据目录结构创建本地目录路径并保存文件
    dir_path = os.path.join(*path_parts[:-1])
    file_path = os.path.join(dir_path, file_name)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    # file_name = os.path.splitext(os.path.basename(url))[0] + ".md"
    # file_path = os.path.join("md", file_name)

    # 将转换后的 Markdown 内容保存到文件
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(cleaned_content)

    return file_path


# 测试函数:10每次只执行前面的10个。

for url in links[:100]:
    file_path = html_to_mdx(url)
    print(f"Markdown 文件已保存为：{file_path}")


# url = "https://python.langchain.com/en/latest/index.html"
# file_path = html_to_mdx(url)
# print(f"Markdown 文件已保存为：{file_path}")




