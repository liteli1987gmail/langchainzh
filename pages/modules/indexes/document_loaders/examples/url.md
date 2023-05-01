


 URL
 [#](#url "Permalink to this headline")
=============================================



 This covers how to load HTML documents from a list of URLs into a document format that we can use downstream.
 







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








 Selenium URL Loader
 [#](#selenium-url-loader "Permalink to this headline")
=============================================================================



 This covers how to load HTML documents from a list of URLs using the
 `SeleniumURLLoader`
 .
 



 Using selenium allows us to load pages that require JavaScript to render.
 




 Setup
 [#](#setup "Permalink to this headline")
-------------------------------------------------



 To use the
 `SeleniumURLLoader`
 , you will need to install
 `selenium`
 and
 `unstructured`
 .
 







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









 Playwright URL Loader
 [#](#playwright-url-loader "Permalink to this headline")
=================================================================================



 This covers how to load HTML documents from a list of URLs using the
 `PlaywrightURLLoader`
 .
 



 As in the Selenium case, Playwright allows us to load pages that need JavaScript to render.
 




 Setup
 [#](#id1 "Permalink to this headline")
-----------------------------------------------



 To use the
 `PlaywrightURLLoader`
 , you will need to install
 `playwright`
 and
 `unstructured`
 . Additionally, you will need to install the Playwright Chromium browser:
 







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








