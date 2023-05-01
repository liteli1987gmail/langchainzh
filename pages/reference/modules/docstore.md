




 Docstore
 [#](#module-langchain.docstore "Permalink to this headline")
========================================================================



 Wrappers on top of docstores.
 




*class*


 langchain.docstore.
 



 InMemoryDocstore
 


 (
 
*_dict
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 langchain.schema.Document
 


 ]*

 )
 
[[source]](../../_modules/langchain/docstore/in_memory#InMemoryDocstore)
[#](#langchain.docstore.InMemoryDocstore "Permalink to this definition") 



 Simple in memory docstore in the form of a dict.
 






 add
 


 (
 
*texts
 



 :
 





 Dict
 


 [
 


 str
 


 ,
 




 langchain.schema.Document
 


 ]*

 )
 


 →
 


 None
 


[[source]](../../_modules/langchain/docstore/in_memory#InMemoryDocstore.add)
[#](#langchain.docstore.InMemoryDocstore.add "Permalink to this definition") 



 Add texts to in memory dictionary.
 








 search
 


 (
 
*search
 



 :
 





 str*

 )
 


 →
 


 Union
 


 [
 


 str
 


 ,
 




 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/docstore/in_memory#InMemoryDocstore.search)
[#](#langchain.docstore.InMemoryDocstore.search "Permalink to this definition") 



 Search via direct lookup.
 








*class*


 langchain.docstore.
 



 Wikipedia
 

[[source]](../../_modules/langchain/docstore/wikipedia#Wikipedia)
[#](#langchain.docstore.Wikipedia "Permalink to this definition") 



 Wrapper around wikipedia API.
 






 search
 


 (
 
*search
 



 :
 





 str*

 )
 


 →
 


 Union
 


 [
 


 str
 


 ,
 




 langchain.schema.Document
 


 ]
 



[[source]](../../_modules/langchain/docstore/wikipedia#Wikipedia.search)
[#](#langchain.docstore.Wikipedia.search "Permalink to this definition") 



 Try to search for wiki page.
 



 If page exists, return the page summary, and a PageWithLookups object.
If page does not exist, return similar entries.
 








