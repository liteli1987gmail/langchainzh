# 使用本地模型

像[PrivateGPT](https://github.com/imartinez/privateGPT)，[llama.cpp](https://github.com/ggerganov/llama.cpp)，[GPT4All](https://github.com/nomic-ai/gpt4all)和[llamafile](https://github.com/Mozilla-Ocho/llamafile)这样的项目的流行性凸显了在本地运行LLM的重要性。

LangChain与许多开源LLM集成，可以在本地运行。

有关这些LLM的设置说明，请参见[这里](/docs/guides/development/local_llms)。

例如，在这里，我们展示了如何使用本地嵌入和本地LLM在本地（例如，您的笔记本电脑上）运行`GPT4All`或`LLaMA2`。

## 文档加载

首先，安装本地嵌入和向量存储所需的软件包。

```python
%pip install --upgrade --quiet  langchain langchain-community langchainhub gpt4all chromadb 
```

加载并拆分示例文档。

我们将使用有关代理的博客文章作为示例。

```python
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)
```

接下来，以下步骤将在本地下载`GPT4All`嵌入（如果您尚未拥有它们）。

```python
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import Chroma

vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())
```

测试相似性搜索是否使用我们的本地嵌入正常工作。

```python
question = "什么是任务分解的方法？"
docs = vectorstore.similarity_search(question)
len(docs)
```

```python
docs[0]
```

## 模型

### LLaMA2

注意：新版本的`llama-cpp-python`使用GGUF模型文件（参见[这里](https://github.com/abetlen/llama-cpp-python/pull/633)）。

如果您已经拥有现有的GGML模型，参见[这里](/docs/integrations/llms/llamacpp)以了解如何进行GGUF转换的说明。

或者，您可以下载转换后的GGUF模型（例如，在[这里](https://huggingface.co/TheBloke)）。

最后，如[这里](/docs/guides/development/local_llms)中所述详细安装`llama-cpp-python`。

```python
%pip install --upgrade --quiet  llama-cpp-python
```

要在Apple Silicon上启用GPU，请按照[这里](https://github.com/abetlen/llama-cpp-python/blob/main/docs/install/macos.md)的步骤使用支持Metal的Python绑定。

特别是，请确保`conda`使用您创建的正确的虚拟环境（`miniforge3`）。

例如，对我来说：

```
conda activate /Users/rlm/miniforge3/envs/llama
```

确认后：

```python
! CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 /Users/rlm/miniforge3/envs/llama/bin/pip install -U llama-cpp-python --no-cache-dir
```

```python
from langchain_community.llms import LlamaCpp
```

根据[llama.cpp文档](/docs/integrations/llms/llamacpp)中的说明设置模型参数。

```python
n_gpu_layers = 1  # Metal设置为1就足够了。
n_batch = 512  # 应该在1和n_ctx之间，考虑您的Apple Silicon芯片的RAM的数量。

# 确保您的系统上模型路径正确！
llm = LlamaCpp(
    model_path="/Users/rlm/Desktop/Code/llama.cpp/models/llama-2-13b-chat.ggufv3.q4_0.bin",
    n_gpu_layers=n_gpu_layers,
    n_batch=n_batch,
    n_ctx=2048,
    f16_kv=True,  # 必须设置为True，否则在调用几次后会遇到问题
    verbose=True,
)
```

注意，这些指示[正确启用了Metal](/docs/integrations/llms/llamacpp)：

```
ggml_metal_init: allocating
ggml_metal_init: using MPS
```

```python
llm.invoke("模拟Stephen Colbert和John Oliver之间的一场饶舌战")
```

### GPT4All

类似地，我们可以使用`GPT4All`。

[下载GPT4All模型二进制文件](/docs/integrations/llms/gpt4all)。

[GPT4All](https://gpt4all.io/index.html)上的模型资源管理器是选择和下载模型的好方式。

然后，指定您下载到的路径。

例如，对于我来说，模型位于此位置：

`/Users/rlm/Desktop/Code/gpt4all/models/nous-hermes-13b.ggmlv3.q4_0.bin`

```python
from langchain_community.llms import GPT4All

gpt4all = GPT4All(
    model="/Users/rlm/Desktop/Code/gpt4all/models/nous-hermes-13b.ggmlv3.q4_0.bin",
    max_tokens=2048,
)
```

### llamafile

在本地运行LLM的最简单方法之一是使用[llamafile](https://github.com/Mozilla-Ocho/llamafile)。您只需要：

1）从[HuggingFace](https://huggingface.co/models?other=llamafile)下载llamafile。
2）将文件设置为可执行文件。
3）运行文件。

llamafiles将模型权重和[特殊编译](https://github.com/Mozilla-Ocho/llamafile?tab=readme-ov-file#technical-details)版的[`llama.cpp`](https://github.com/ggerganov/llama.cpp)打包到一个单独的文件中，可以在大多数计算机上运行，不需要任何其他依赖项。它们还附带了一个嵌入式推断服务器，为您的模型提供了一个[API](https://github.com/Mozilla-Ocho/llamafile/blob/main/llama.cpp/server/README.md#api-endpoints)来进行交互。

这是一个展示所有3个设置步骤的简单bash脚本：

```bash# 从HuggingFace下载llamafile
wget https://huggingface.co/jartine/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile

# 将文件设置为可执行文件。在Windows上，只需将文件重命名为以".exe"结尾。
chmod +x TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile

# 启动模型服务器。默认情况下监听http://localhost:8080。
./TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile --server --nobrowser
```

在运行上述设置步骤后，您可以通过LangChain与模型进行交互:


```python
from langchain_community.llms.llamafile import Llamafile

llamafile = Llamafile()

llamafile.invoke("这是我奶奶心爱的意大利面和肉丸的食谱:")
```


    '\n-1 1/2 (8 盎司) 碎牛肉，煎炒并煮至不再粉红\n-3 杯全麦意大利面\n-4 (10 盎司) 罐装蒜和罗勒番茄粒\n-2个鸡蛋，打散\n-1 杯 grated parmesan 乳酪\n-1/2 茶匙盐\n-1/4 茶匙黑胡椒粉\n-1 杯面包碎屑 (16 盎司)\n-2 汤匙橄榄油\n\n步骤:\n1. 根据包装说明煮意大利面。沥干并放在一边。\n2. 在一个大平底锅中，用中火将碎牛肉煎炒至不再粉红。倾去多余的油脂。\n3. 搅拌蒜和罗勒番茄粒，加入盐和胡椒粉调味。烹饪5至7分钟，或直到酱汁加热。搁置一边。\n4. 在一个大碗中，用叉子或搅拌器打散鸡蛋，直到变蓬松。加入奶酪、盐和黑胡椒，搁置一边。\n5. 在另一个碗中，混合面包屑和橄榄油。将每根意大利面条都浸入蛋液中，然后沾上面包屑混合物。将涂有烘焙纸的烤盘上，防止粘连。重复操作，直到所有意大利面都裹上面包屑。\n6. 烤箱预热至375华氏度。烘烤18至20分钟，或至轻微金黄色。\n7. 热腾腾地配上肉丸和酱汁。享受吧！'



## 在链中使用

我们可以通过传入检索到的文档和一个简单的提示来创建一个摘要链。

它使用提供的输入键值对格式化提示模板，并将格式化的字符串传递给`GPT4All`、`LLama-V2`或其他指定的LLM。


```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# 提示
prompt = PromptTemplate.from_template(
    "总结这些检索到的文档中的主要主题: {docs}"
)


# 链
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


chain = {"docs": format_docs} | prompt | llm | StrOutputParser()

# 运行
question = "解任务分解的方法有哪些?"
docs = vectorstore.similarity_search(question)
chain.invoke(docs)
```


    Llama.generate: prefix-match hit
    

    
    根据检索到的文档，主要主题包括:
    1. 任务分解: 将复杂的任务分解为更小的子任务，由LLM或其他代理系统的组件处理。
    2. LLM作为核心控制器: 使用大型语言模型（LLM）作为自主代理系统的主要控制器，辅以其他关键组件，如知识图和规划器。
    3. LLM的潜力: LLM不仅可以生成精心编写的副本，还可以用作强大的通用问题解决器，用于解决复杂任务和实现人类一样的智能。
    4. 长期规划中的挑战: 长期规划中的挑战包括在漫长的历史中进行规划和有效地探索解空间，这是当前基于LLM的自主代理系统的重要限制。

    
    llama_print_timings:        load time =  1191.88 ms
    llama_print_timings:      sample time =   134.47 ms /   193 runs   (    0.70 ms per token,  1435.25 tokens per second)
    llama_print_timings: prompt eval time = 39470.18 ms /  1055 tokens (   37.41 ms per token,    26.73 tokens per second)
    llama_print_timings:        eval time =  8090.85 ms /   192 runs   (   42.14 ms per token,    23.73 tokens per second)
    llama_print_timings:       total time = 47943.12 ms
    




    '\n根据检索到的文档，主要主题包括:\n1. 任务分解: 将复杂的任务分解为更小的子任务，由LLM或其他代理系统的组件处理。\n2. LLM作为核心控制器: 使用大型语言模型（LLM）作为自主代理系统的主要控制器，辅以其他关键组件，如知识图和规划器。\n3. LLM的潜力: LLM不仅可以生成精心编写的副本，还可以用作强大的通用问题解决器，用于解决复杂任务和实现人类一样的智能。\n4. 长期规划中的挑战: 长期规划中的挑战包括在漫长的历史中进行规划和有效地探索解空间，这是当前基于LLM的自主代理系统的重要限制。'



## 问答 

我们还可以使用LangChain Prompt Hub存储和获取特定于模型的提示。

让我们尝试使用默认的RAG提示，[在此](https://smith.langchain.com/hub/rlm/rag-prompt)。


```python
from langchain import hub

rag_prompt = hub.pull("rlm/rag-prompt")
rag_prompt.messages
```


    [HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['context', 'question'], template="您是一个用于问答任务的助手。使用以下检索到的上下文片段来回答问题。如果您不知道答案，只需说不知道即可。答案最多三句话，请保持简练。\n问题: {question} \n上下文: {context} \n答案:"))]




```python
from langchain_core.runnables import RunnablePassthrough, RunnablePick

# 链
chain = (
    RunnablePassthrough.assign(context=RunnablePick("context") | format_docs)
    | rag_prompt
    | llm
    | StrOutputParser()
)

# 运行
chain.invoke({"context": docs, "question": question})
```


    Llama.generate: prefix-match hit
    

    
    您好，我很乐意帮忙！根据上下文，以下是一些任务分解的方法:
    
    1. 使用简单提示的LLM: 使用大型模型（LLM）和简单提示，如“XYZ的步骤”或“实现XYZ的子目标的方法”，将任务分解为较小的步骤。
    2. 任务特定方法: 另一种方法是使用任务特定的提示，例如“撰写小说大纲”以指导撰写小说等任务。
    3. 人工输入: 在需要高度创造力或专业知识的情况下，可以使用人工输入来补充处理过程。
    
    在长期规划和任务方面，面临的一个主要挑战是LLM在面临错误时需要调整计划，这使得它们对于通过试错学习的人类来说不够稳健。

    
    llama_print_timings:        load time = 11326.20 ms
    llama_print_timings:      sample time =    33.03 ms /    47 runs   (    0.70 ms per token,  1422.86 tokens per second)
    llama_print_timings: prompt eval time =  1387.31 ms /   242 tokens (    5.73 ms per token,   174.44 tokens per second)
    llama_print_timings:        eval time =  1321.62 ms /    46 runs   (   28.73 ms per token,    34.81 tokens per second)
    llama_print_timings:       total time =  2801.08 ms
    




    {'output_text': '  您好，我很乐意帮忙！根据上下文，以下是一些任务分解的方法:\n\n1. 使用简单提示的LLM: 使用大型模型（LLM）和简单提示，如“XYZ的步骤”或“实现XYZ的子目标的方法”，将任务分解为较小的步骤。\n2. 任务特定方法: 另一种方法是使用任务特定的提示，例如“撰写小说大纲”以指导撰写小说等任务。\n3. 人工输入: 在需要高度创造力或专业知识的情况下，可以使用人工输入来补充处理过程。\n\n在长期规划和任务方面，面临的一个主要挑战是LLM在面临错误时需要调整计划，这使得它们对于通过试错学习的人类来说不够稳健。'}



现在，让我们尝试用[专门为LLaMA设计的提示](https://smith.langchain.com/hub/rlm/rag-prompt-llama)，其中[包含特殊令牌](https://huggingface.co/blog/llama2#how-to-prompt-llama-2)。


```python
# 提示
rag_prompt_llama = hub.pull("rlm/rag-prompt-llama")
rag_prompt_llama.messages
```


    ChatPromptTemplate(input_variables=['question', 'context'], output_parser=None, partial_variables={}, messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['question', 'context'], output_parser=None, partial_variables={}, template="[INST]<<SYS>> 您是一个用于问答任务的助手。使用以下检索到的上下文来回答问题。如果您不知道答案，只需说不知道即可。答案最多三句话，请保持简练。<</SYS>> \n问题: {question} \n上下文: {context} \n答案: [/INST]", template_format='f-string', validate_template=True), additional_kwargs={})])




```python
# 链
chain = (
    RunnablePassthrough.assign(context=RunnablePick("context") | format_docs)
    | rag_prompt_llama
    | llm
    | StrOutputParser()
)

# 运行
chain.invoke({"context": docs, "question": question})
```


    Llama.generate: prefix-match hit
    

      当然，我很乐意帮助！根据上下文，以下是一些建议的任务分解方法:

    1. 使用简单提示的LLM: 使用大型语言模型（LLM），如"GPT4All"，并使用像"针对 XYZ 的步骤"或"实现 XYZ 的子目标的方法"这样的简单提示，将复杂任务分解为更小的任务。
    2. 任务特定方法: 另一种方法是为特定任务使用专门的提示。例如，针对"撰写小说"这个任务，可以使用"撰写小说的大纲"这样的提示来指导。
    3. 人工输入: 在某些情况下，如果任务需要很高的创造力或专业知识，可以使用人工输入作为辅助工具进行任务分解。

    在长期规划和任务方面，面临的一个主要挑战是LLM需要在面临错误时调整计划，这使其对像人类一样通过试错学习的个体不够稳健。

    
    llama_print_timings:        load time = 11326.20 ms
    llama_print_timings:      sample time =   144.81 ms /   207 runs   (    0.70 ms per token,  1429.47 tokens per second)
    llama_print_timings: prompt eval time =  1506.13 ms /   258 tokens (    5.73 ms per token,   171.30 tokens per second)
    llama_print_timings:        eval time =  6231.92 ms /   206 runs   (   30.25 ms per token,    33.06 tokens per second)
    llama_print_timings:       total time =  8158.41 ms
    




    {'output_text': '  当然，我很乐意帮助！根据上下文，以下是一些建议的任务分解方法:\n\n1. 使用简单提示的LLM: 使用大型语言模型（LLM），如"GPT4All"，并使用像"针对 XYZ 的步骤"或"实现 XYZ 的子目标的方法"这样的简单提示，将复杂任务分解为更小的任务。\n2. 任务特定方法: 另一种方法是为特定任务使用专门的提示。例如，针对"撰写小说"这个任务，可以使用"撰写小说的大纲"这样的提示来指导。\n3. 人工输入: 在某些情况下，如果任务需要很高的创造力或专业知识，可以使用人工输入作为辅助工具进行任务分解。\n\n在长期规划和任务方面，面临的一个主要挑战是LLM需要在面临错误时调整计划，这使其对像人类一样通过试错学习的个体不够稳健。'}



## 带有检索的问答

我们可以自动从向量存储中检索文档，而不是手动传入文档，检索的依据是用户的问题。

这将使用一个默认的问答提示（显示[在这里](https://github.com/langchain-ai/langchain/blob/275b926cf745b5668d3ea30236635e20e7866442/langchain/chains/retrieval_qa/prompt.py#L4)）并从向量数据库检索。

```python
retriever = vectorstore.as_retriever()
qa_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)
```

```python
qa_chain.invoke(question)
```

```
Llama.generate: prefix-match hit

  Sure! Based on the context, here's my answer to your:

There are several approaches to task decomposition:

1. LLM-based with simple prompting, such as "Steps for XYZ" or "What are the subgoals for achieving XYZ?"
2. Task-specific, like "Write a story outline" for writing a novel.
3. Human inputs to guide the process.

These can be used to decompose complex tasks into smaller, more manageable subtasks, which can help improve the efficiency and effectiveness of a task. However, there can be challenges in long-term planning and task exploration due to the need to plan over a lengthy history and explore the solution space. LLMs may struggle to adjust plans when faced with errors, making them less robust compared to human learners who can learn from trial and error.

llama_print_timings: load time = 11326.20 ms
llama_print_timings: sample time =   139.20 ms /   200 runs   (    0.70 ms per token,  1436.76 tokens per second)
llama_print_timings: prompt eval time =  1532.26 ms /   258 tokens (    5.94 ms per token,   168.38 tokens per second)
llama_print_timings: eval time =  5977.62 ms /   199 runs   (   30.04 ms per token,    33.29 tokens per second)
llama_print_timings: total time =  7916.21 ms

{'query': 'What are the approaches to Task Decomposition?', 'result': '  Sure! Based on the context, here\'s my answer to your:\n\nThere are several approaches to task decomposition:\n\n1. LLM-based with simple prompting, such as "Steps for XYZ" or "What are the subgoals for achieving XYZ?"\n2. Task-specific, like "Write a story outline" for writing a novel.\n3. Human inputs to guide the process.\n\nThese can be used to decompose complex tasks into smaller, more manageable subtasks, which can help improve the efficiency and effectiveness of a task. However, there can be challenges in long-term planning and task exploration due to the need to plan over a lengthy history and explore the solution space. LLMs may struggle to adjust plans when faced with errors, making them less robust compared to human learners who can learn from trial and error.'}
```