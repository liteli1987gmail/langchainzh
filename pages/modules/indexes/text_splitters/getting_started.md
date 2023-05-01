


开始
=====================================================================


默认推荐的文本分割器是 RecursivePersonterTextSplitter。此文本分割器接受字符列表。它试图根据第一个字符的分割来创建块，但是如果任何块太大，它就会移动到下一个字符，以此类推。默认情况下，它试图分割的字符是[“ n”、“ n”、“”、“”]

除了控制可以分割的字符之外，你还可以控制其他一些事情:
 In addition to controlling which characters you can split on, you can also control a few other things:
 


* `length_function`
 : 如何计算块的长度。默认情况下只计算字符数，但是在这里传递令牌计数器是很常见的。
* `chunk_size`
 : 块的最大大小(由长度函数测量)。
* `chunk_overlap`
 : 块之间的最大重叠。有一些重叠可以很好地保持块之间的一些连续性(例如做一个滑动窗口)。







```
# This is a long document we can split up.
with open('../../state_of_the_union.txt') as f:
    state_of_the_union = f.read()

```










```
from langchain.text_splitter import RecursiveCharacterTextSplitter

```










```
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 100,
    chunk_overlap  = 20,
    length_function = len,
)

```










```
texts = text_splitter.create_documents([state_of_the_union])
print(texts[0])
print(texts[1])

```








```
page_content='Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and' lookup_str='' metadata={} lookup_index=0
page_content='of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.' lookup_str='' metadata={} lookup_index=0

```







