

分析文档[#](#analyze-document "此标题的永久链接")
=====================================

分析文档链更像是一个结束链。该链接收单个文档，将其拆分，然后通过合并文档链运行它。这可以用作更多的端到端链。

```
with open("../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()

```

总结[#](#summarize "此标题的永久链接")
----------------------------

让我们看看它在下面的示例中的使用，使用它来总结一个长文档。

```
from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain

llm = OpenAI(temperature=0)
summary_chain = load_summarize_chain(llm, chain_type="map_reduce")

```

```
from langchain.chains import AnalyzeDocumentChain

```

```
summarize_document_chain = AnalyzeDocumentChain(combine_docs_chain=summary_chain)

```

```
summarize_document_chain.run(state_of_the_union)

```

```
" In this speech, President Biden addresses the American people and the world, discussing the recent aggression of Russia's Vladimir Putin in Ukraine and the US response. He outlines economic sanctions and other measures taken to hold Putin accountable, and announces the US Department of Justice's task force to go after the crimes of Russian oligarchs. He also announces plans to fight inflation and lower costs for families, invest in American manufacturing, and provide military, economic, and humanitarian assistance to Ukraine. He calls for immigration reform, protecting the rights of women, and advancing the rights of LGBTQ+ Americans, and pays tribute to military families. He concludes with optimism for the future of America."

```

问答[#](#question-answering "此标题的永久链接")
-------------------------------------

让我们使用问答链来看看它。

```
from langchain.chains.question_answering import load_qa_chain

```

```
qa_chain = load_qa_chain(llm, chain_type="map_reduce")

```

```
qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)

```

```
qa_document_chain.run(input_document=state_of_the_union, question="what did the president say about justice breyer?")

```

```
' The president thanked Justice Breyer for his service.'

```

