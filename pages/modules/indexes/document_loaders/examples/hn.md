


 Hacker News
 [#](#hacker-news "Permalink to this headline")
=============================================================



 How to pull page data and comments from Hacker News
 







```
from langchain.document_loaders import HNLoader

```










```
loader = HNLoader("https://news.ycombinator.com/item?id=34817881")

```










```
data = loader.load()

```










```
data

```








```
[Document(page_content="delta_p_delta_x 18 hours ago  \n             | next [–] \n\nAstrophysical and cosmological simulations are often insightful. They're also very cross-disciplinary; besides the obvious astrophysics, there's networking and sysadmin, parallel computing and algorithm theory (so that the simulation programs are actually fast but still accurate), systems design, and even a bit of graphic design for the visualisations.Some of my favourite simulation projects:- IllustrisTNG: https://www.tng-project.org/- SWIFT: https://swift.dur.ac.uk/- CO5BOLD: https://www.astro.uu.se/~bf/co5bold_main (which produced these animations of a red-giant star: https://www.astro.uu.se/~bf/movie/AGBmovie)- AbacusSummit: https://abacussummit.readthedocs.io/en/latest/And I can add the simulations in the article, too.\n \nreply", lookup_str='', metadata={'source': 'https://news.ycombinator.com/item?id=34817881', 'title': 'What Lights the Universe’s Standard Candles?'}, lookup_index=0),
 Document(page_content="andrewflnr 19 hours ago  \n             | prev | next [–] \n\nWhoa. I didn't know the accretion theory of Ia supernovae was dead, much less that it had been since 2011.\n \nreply", lookup_str='', metadata={'source': 'https://news.ycombinator.com/item?id=34817881', 'title': 'What Lights the Universe’s Standard Candles?'}, lookup_index=0),
 Document(page_content='andreareina 18 hours ago  \n             | prev | next [–] \n\nThis seems  to be the paper https://academic.oup.com/mnras/article/517/4/5260/6779709\n \nreply', lookup_str='', metadata={'source': 'https://news.ycombinator.com/item?id=34817881', 'title': 'What Lights the Universe’s Standard Candles?'}, lookup_index=0),
 Document(page_content="andreareina 18 hours ago  \n             | prev [–] \n\nWouldn't double detonation show up as variance in the brightness?\n \nreply", lookup_str='', metadata={'source': 'https://news.ycombinator.com/item?id=34817881', 'title': 'What Lights the Universe’s Standard Candles?'}, lookup_index=0)]

```







