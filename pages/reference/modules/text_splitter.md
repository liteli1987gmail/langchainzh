




 Text Splitter
 [#](#module-langchain.text_splitter "Permalink to this headline")
==================================================================================



 Functionality for splitting text.
 




*class*


 langchain.text_splitter.
 



 CharacterTextSplitter
 


 (
 
*separator
 



 :
 





 str
 





 =
 





 '\n\n'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/text_splitter#CharacterTextSplitter)
[#](#langchain.text_splitter.CharacterTextSplitter "Permalink to this definition") 



 Implementation of splitting text that looks at characters.
 






 split_text
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/text_splitter#CharacterTextSplitter.split_text)
[#](#langchain.text_splitter.CharacterTextSplitter.split_text "Permalink to this definition") 



 Split incoming text and return chunks.
 








*class*


 langchain.text_splitter.
 



 LatexTextSplitter
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/text_splitter#LatexTextSplitter)
[#](#langchain.text_splitter.LatexTextSplitter "Permalink to this definition") 



 Attempts to split the text along Latex-formatted layout elements.
 






*class*


 langchain.text_splitter.
 



 MarkdownTextSplitter
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/text_splitter#MarkdownTextSplitter)
[#](#langchain.text_splitter.MarkdownTextSplitter "Permalink to this definition") 



 Attempts to split the text along Markdown-formatted headings.
 






*class*


 langchain.text_splitter.
 



 NLTKTextSplitter
 


 (
 
*separator
 



 :
 





 str
 





 =
 





 '\n\n'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/text_splitter#NLTKTextSplitter)
[#](#langchain.text_splitter.NLTKTextSplitter "Permalink to this definition") 



 Implementation of splitting text that looks at sentences using NLTK.
 






 split_text
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/text_splitter#NLTKTextSplitter.split_text)
[#](#langchain.text_splitter.NLTKTextSplitter.split_text "Permalink to this definition") 



 Split incoming text and return chunks.
 








*class*


 langchain.text_splitter.
 



 PythonCodeTextSplitter
 


 (
 
*\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/text_splitter#PythonCodeTextSplitter)
[#](#langchain.text_splitter.PythonCodeTextSplitter "Permalink to this definition") 



 Attempts to split the text along Python syntax.
 






*class*


 langchain.text_splitter.
 



 RecursiveCharacterTextSplitter
 


 (
 
*separators
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/text_splitter#RecursiveCharacterTextSplitter)
[#](#langchain.text_splitter.RecursiveCharacterTextSplitter "Permalink to this definition") 



 Implementation of splitting text that looks at characters.
 



 Recursively tries to split by different characters to find one
that works.
 






 split_text
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/text_splitter#RecursiveCharacterTextSplitter.split_text)
[#](#langchain.text_splitter.RecursiveCharacterTextSplitter.split_text "Permalink to this definition") 



 Split incoming text and return chunks.
 








*class*


 langchain.text_splitter.
 



 SpacyTextSplitter
 


 (
 
*separator
 



 :
 





 str
 





 =
 





 '\n\n'*
 ,
 *pipeline
 



 :
 





 str
 





 =
 





 'en_core_web_sm'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/text_splitter#SpacyTextSplitter)
[#](#langchain.text_splitter.SpacyTextSplitter "Permalink to this definition") 



 Implementation of splitting text that looks at sentences using Spacy.
 






 split_text
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/text_splitter#SpacyTextSplitter.split_text)
[#](#langchain.text_splitter.SpacyTextSplitter.split_text "Permalink to this definition") 



 Split incoming text and return chunks.
 








*class*


 langchain.text_splitter.
 



 TextSplitter
 


 (
 
*chunk_size:
 

 int
 

 =
 

 4000,
 

 chunk_overlap:
 

 int
 

 =
 

 200,
 

 length_function:
 

 typing.Callable[[str],
 

 int]
 

 =
 

 <built-in
 

 function
 

 len>*

 )
 
[[source]](../../_modules/langchain/text_splitter#TextSplitter)
[#](#langchain.text_splitter.TextSplitter "Permalink to this definition") 



 Interface for splitting text into chunks.
 




*async*


 atransform_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/text_splitter#TextSplitter.atransform_documents)
[#](#langchain.text_splitter.TextSplitter.atransform_documents "Permalink to this definition") 



 Asynchronously transform a sequence of documents by splitting them.
 








 create_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*
 ,
 *metadatas
 



 :
 





 Optional
 


 [
 


 List
 


 [
 


 dict
 


 ]
 



 ]
 






 =
 





 None*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/text_splitter#TextSplitter.create_documents)
[#](#langchain.text_splitter.TextSplitter.create_documents "Permalink to this definition") 



 Create documents from a list of texts.
 






*classmethod*


 from_huggingface_tokenizer
 


 (
 
*tokenizer
 



 :
 





 Any*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.text_splitter.TextSplitter](#langchain.text_splitter.TextSplitter "langchain.text_splitter.TextSplitter")


[[source]](../../_modules/langchain/text_splitter#TextSplitter.from_huggingface_tokenizer)
[#](#langchain.text_splitter.TextSplitter.from_huggingface_tokenizer "Permalink to this definition") 



 Text splitter that uses HuggingFace tokenizer to count length.
 






*classmethod*


 from_tiktoken_encoder
 


 (
 
*encoding_name
 



 :
 





 str
 





 =
 





 'gpt2'*
 ,
 *model_name
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *allowed_special
 



 :
 





 Union
 


 [
 


 Literal
 


 [
 



 'all'
 



 ]
 



 ,
 




 AbstractSet
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 {}*
 ,
 *disallowed_special
 



 :
 





 Union
 


 [
 


 Literal
 


 [
 



 'all'
 



 ]
 



 ,
 




 Collection
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 'all'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.text_splitter.TextSplitter](#langchain.text_splitter.TextSplitter "langchain.text_splitter.TextSplitter")


[[source]](../../_modules/langchain/text_splitter#TextSplitter.from_tiktoken_encoder)
[#](#langchain.text_splitter.TextSplitter.from_tiktoken_encoder "Permalink to this definition") 



 Text splitter that uses tiktoken encoder to count length.
 








 split_documents
 


 (
 
*documents
 



 :
 





 List
 


 [
 


 langchain.schema.Document
 


 ]*

 )
 


 →
 


 List
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/text_splitter#TextSplitter.split_documents)
[#](#langchain.text_splitter.TextSplitter.split_documents "Permalink to this definition") 



 Split documents.
 






*abstract*


 split_text
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/text_splitter#TextSplitter.split_text)
[#](#langchain.text_splitter.TextSplitter.split_text "Permalink to this definition") 



 Split text into multiple components.
 








 transform_documents
 


 (
 
*documents
 



 :
 





 Sequence
 


 [
 


 langchain.schema.Document
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 Sequence
 


 [
 


 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/text_splitter#TextSplitter.transform_documents)
[#](#langchain.text_splitter.TextSplitter.transform_documents "Permalink to this definition") 



 Transform sequence of documents by splitting them.
 








*class*


 langchain.text_splitter.
 



 TokenTextSplitter
 


 (
 
*encoding_name
 



 :
 





 str
 





 =
 





 'gpt2'*
 ,
 *model_name
 



 :
 





 Optional
 


 [
 


 str
 


 ]
 






 =
 





 None*
 ,
 *allowed_special
 



 :
 





 Union
 


 [
 


 Literal
 


 [
 



 'all'
 



 ]
 



 ,
 




 AbstractSet
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 {}*
 ,
 *disallowed_special
 



 :
 





 Union
 


 [
 


 Literal
 


 [
 



 'all'
 



 ]
 



 ,
 




 Collection
 


 [
 


 str
 


 ]
 



 ]
 






 =
 





 'all'*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 
[[source]](../../_modules/langchain/text_splitter#TokenTextSplitter)
[#](#langchain.text_splitter.TokenTextSplitter "Permalink to this definition") 



 Implementation of splitting text that looks at tokens.
 






 split_text
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 str
 


 ]
 



[[source]](../../_modules/langchain/text_splitter#TokenTextSplitter.split_text)
[#](#langchain.text_splitter.TokenTextSplitter.split_text "Permalink to this definition") 



 Split incoming text and return chunks.
 








