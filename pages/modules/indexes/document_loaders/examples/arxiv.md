

Arxiv[#](#arxiv "Permalink to this headline")
=============================================

> 
> [arXiv](https://arxiv.org/) is an open-access archive for 2 million scholarly articles in the fields of physics, mathematics, computer science, quantitative biology, quantitative finance, statistics, electrical engineering and systems science, and economics.
> 
> 
> 

This notebook shows how to load scientific articles from `Arxiv.org` into a document format that we can use downstream.

Installation[#](#installation "Permalink to this headline")
-----------------------------------------------------------

First, you need to install `arxiv` python package.

```
#!pip install arxiv

```

Second, you need to install `PyMuPDF` python package which transform PDF files from the `arxiv.org` site into the text format.

```
#!pip install pymupdf

```

Examples[#](#examples "Permalink to this headline")
---------------------------------------------------

`ArxivLoader` has these arguments:

* `query`: free text which used to find documents in the Arxiv

* 可选的 `load_max_docs`: 默认值为100。用于限制下载文档的数量。下载所有100个文档需要时间，因此在实验中使用较小的数字。

* 可选的 `load_all_available_meta`: 默认值为False。默认情况下，仅下载最重要的字段：`Published`（文档发布/最后更新日期)，`Title`，`Authors`，`Summary`。如果为True，则还会下载其他字段。

```
from langchain.document_loaders import ArxivLoader

```

```
docs = ArxivLoader(query="1605.08386", load_max_docs=2).load()
len(docs)

```

```
docs[0].metadata  # meta-information of the Document

```

```
{'Published': '2016-05-26',
 'Title': 'Heat-bath random walks with Markov bases',
 'Authors': 'Caprice Stanley, Tobias Windisch',
 'Summary': 'Graphs on lattice points are studied whose edges come from a finite set of\nallowed moves of arbitrary length. We show that the diameter of these graphs on\nfibers of a fixed integer matrix can be bounded from above by a constant. We\nthen study the mixing behaviour of heat-bath random walks on these graphs. We\nalso state explicit conditions on the set of moves so that the heat-bath random\nwalk, a generalization of the Glauber dynamics, is an expander in fixed\ndimension.'}

```

```
docs[0].page_content[:400]  # all pages of the Document content

```

```
'arXiv:1605.08386v1  [math.CO]  26 May 2016\nHEAT-BATH RANDOM WALKS WITH MARKOV BASES\nCAPRICE STANLEY AND TOBIAS WINDISCH\nAbstract. Graphs on lattice points are studied whose edges come from a ﬁnite set of\nallowed moves of arbitrary length. We show that the diameter of these graphs on ﬁbers of a\nﬁxed integer matrix can be bounded from above by a constant. We then study the mixing\nbehaviour of heat-b'

```

