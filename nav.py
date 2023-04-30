import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin



# 这是langchain的左侧菜单栏目
url = "https://python.langchain.com/en/latest/getting_started/getting_started.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

nav = soup.find("nav", class_="bd-links")  # 需要提取的 nav 标签
if nav is not None:
    links = [a['href'] for a in nav.find_all("a") if "href" in a.attrs]
    links = [urljoin(url, link) if not link.startswith("http") else link for link in links]
    print(links)
    with open("links.txt", "w") as f:
        for link in links:
            f.write(f"{link}\n")