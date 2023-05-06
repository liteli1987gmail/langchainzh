

本文介绍如何从URL列表中加载HTML文档，以便我们可以在下游使用。

```
 from langchain.document_loaders import UnstructuredURLLoader

```

```
urls = [
    "https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment-february-8-2023",
    "https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment-february-9-2023"
]

```

```
loader = UnstructuredURLLoader(urls=urls)

```

```
data = loader.load()

```

Selenium URL 加载器[#](#selenium-url-loader "永久链接到这个标题")
=====================================================

本文介绍如何使用`SeleniumURLLoader`从URL列表中加载HTML文档。

使用Selenium可以加载需要JavaScript渲染的页面。

设置[#](#setup "永久链接到这个标题")
-------------------------

要使用`SeleniumURLLoader`，您需要安装`selenium`和`unstructured`。

```
from langchain.document_loaders import SeleniumURLLoader

```

```
urls = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://goo.gl/maps/NDSHwePEyaHMFGwh8"
]

```

```
loader = SeleniumURLLoader(urls=urls)

```

```
data = loader.load()

```

Playwright URL 加载器[#](#playwright-url-loader "永久链接到这个标题")
=========================================================

本文介绍如何使用`PlaywrightURLLoader`从URL列表中加载HTML文档。

与Selenium类似，Playwright可以加载需要JavaScript渲染的页面。

设置[#](#id1 "永久链接到这个标题")
-----------------------

To use the `PlaywrightURLLoader`, you will need to install `playwright` and `unstructured`. Additionally, you will need to install the Playwright Chromium browser:

```
# Install playwright
!pip install "playwright"
!pip install "unstructured"
!playwright install

```

```
from langchain.document_loaders import PlaywrightURLLoader

```

```
urls = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://goo.gl/maps/NDSHwePEyaHMFGwh8"
]

```

```
loader = PlaywrightURLLoader(urls=urls, remove_selectors=["header", "footer"])

```

```
data = loader.load()

```

