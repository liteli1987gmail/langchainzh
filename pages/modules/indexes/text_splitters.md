


 Text Splitters
 [#](#text-splitters "Permalink to this headline")
===================================================================




 Note
 



[Conceptual Guide](https://docs.langchain.com/docs/components/indexing/text-splitter) 





 When you want to deal with long pieces of text, it is necessary to split up that text into chunks.
As simple as this sounds, there is a lot of potential complexity here. Ideally, you want to keep the semantically related pieces of text together. What “semantically related” means could depend on the type of text.
This notebook showcases several ways to do that.
 



 At a high level, text splitters work as following:
 


1. Split the text up into small, semantically meaningful chunks (often sentences).
2. Start combining these small chunks into a larger chunk until you reach a certain size (as measured by some function).
3. Once you reach that size, make that chunk its own piece of text and then start creating a new chunk of text with some overlap (to keep context between chunks).



 That means there two different axes along which you can customize your text splitter:
 


1. How the text is split
2. How the chunk size is measured



 For an introduction to the default text splitter and generic functionality see:
 



* [Getting Started](text_splitters/getting_started)




 We also have documentation for all the types of text splitters that are supported.
Please see below for that list.
 



* [Character Text Splitter](text_splitters/examples/character_text_splitter)
* [Hugging Face Length Function](text_splitters/examples/huggingface_length_function)
* [Latex Text Splitter](text_splitters/examples/latex)
* [Markdown Text Splitter](text_splitters/examples/markdown)
* [NLTK Text Splitter](text_splitters/examples/nltk)
* [Python Code Text Splitter](text_splitters/examples/python)
* [RecursiveCharacterTextSplitter](text_splitters/examples/recursive_text_splitter)
* [Spacy Text Splitter](text_splitters/examples/spacy)
* [tiktoken (OpenAI) Length Function](text_splitters/examples/tiktoken)
* [TiktokenText Splitter](text_splitters/examples/tiktoken_splitter)





