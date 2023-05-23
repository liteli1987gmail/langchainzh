

图问题回答[#](#graph-qa "Permalink to this headline")
================================================

本教程介绍如何在图数据结构上进行问题回答。

创建图[#](#create-the-graph "Permalink to this headline")
------------------------------------------------------

在本节中，我们构建一个示例图。目前，这适用于小段文本。

```
from langchain.indexes import GraphIndexCreator
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader

```

```
index_creator = GraphIndexCreator(llm=OpenAI(temperature=0))

```

```
with open("../../state_of_the_union.txt") as f:
    all_text = f.read()

```

我们只使用一个小片段，因为提取知识三元组稍微有些费力。

```
text = "\n".join(all_text.split("  ")[105:108])

```

```
text

```

```
'It won’t look like much, but if you stop and look closely, you’ll see a “Field of dreams,” the ground on which America’s future will be built. \nThis is where Intel, the American company that helped build Silicon Valley, is going to build its $20 billion semiconductor “mega site”. \nUp to eight state-of-the-art factories in one place. 10,000 new good-paying jobs. '

```

```
graph = index_creator.from_text(text)

```

我们可以查看创建的图。

```
graph.get_triples()

```

```
[('Intel', '$20 billion semiconductor "mega site"', 'is going to build'),
 ('Intel', 'state-of-the-art factories', 'is building'),
 ('Intel', '10,000 new good-paying jobs', 'is creating'),
 ('Intel', 'Silicon Valley', 'is helping build'),
 ('Field of dreams',
  "America's future will be built",
  'is the ground on which')]

```

查询图[#](#querying-the-graph "Permalink to this headline")
--------------------------------------------------------

现在我们可以使用图QA链来问图的问题

```
from langchain.chains import GraphQAChain

```

```
chain = GraphQAChain.from_llm(OpenAI(temperature=0), graph=graph, verbose=True)

```

```
chain.run("what is Intel going to build?")

```

```
> Entering new GraphQAChain chain...
Entities Extracted:
 Intel
Full Context:
Intel is going to build $20 billion semiconductor "mega site"
Intel is building state-of-the-art factories
Intel is creating 10,000 new good-paying jobs
Intel is helping build Silicon Valley

> Finished chain.

```

```
' Intel is going to build a $20 billion semiconductor "mega site" with state-of-the-art factories, creating 10,000 new good-paying jobs and helping to build Silicon Valley.'

```

保存图[#](#save-the-graph "Permalink to this headline")
----------------------------------------------------

我们也可以保存和加载图。

```
graph.write_to_gml("graph.gml")

```

```
from langchain.indexes.graph import NetworkxEntityGraph

```

```
loaded_graph = NetworkxEntityGraph.from_gml("graph.gml")

```

```
loaded_graph.get_triples()

```

```
[('Intel', '$20 billion semiconductor "mega site"', 'is going to build'),
 ('Intel', 'state-of-the-art factories', 'is building'),
 ('Intel', '10,000 new good-paying jobs', 'is creating'),
 ('Intel', 'Silicon Valley', 'is helping build'),
 ('Field of dreams',
  "America's future will be built",
  'is the ground on which')]

```

