




 Chains
 [#](#module-langchain.chains "Permalink to this headline")
====================================================================



 Chains are easily reusable components which can be linked together.
 




*pydantic
 

 model*


 langchain.chains.
 



 APIChain
 

[[source]](../../_modules/langchain/chains/api/base#APIChain)
[#](#langchain.chains.APIChain "Permalink to this definition") 



 Chain that makes API calls and summarizes the responses to answer a question.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_api_answer_prompt`
 »
 `all
 

 fields`
* `validate_api_request_prompt`
 »
 `all
 

 fields`






*field*


 api_answer_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.APIChain.api_answer_chain "Permalink to this definition") 






*field*


 api_docs
 

*:
 




 str*
*[Required]*
[#](#langchain.chains.APIChain.api_docs "Permalink to this definition") 






*field*


 api_request_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.APIChain.api_request_chain "Permalink to this definition") 






*field*


 requests_wrapper
 

*:
 



[TextRequestsWrapper](utilities#langchain.utilities.TextRequestsWrapper "langchain.utilities.TextRequestsWrapper")*
*[Required]*
[#](#langchain.chains.APIChain.requests_wrapper "Permalink to this definition") 






*classmethod*


 from_llm_and_api_docs
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *api_docs
 



 :
 





 str*
 ,
 *headers
 



 :
 





 Optional
 


 [
 


 dict
 


 ]
 






 =
 





 None*
 ,
 *api_url_prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['api_docs',
 

 'question'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='You
 

 are
 

 given
 

 the
 

 below
 

 API
 

 Documentation:\n{api_docs}\nUsing
 

 this
 

 documentation,
 

 generate
 

 the
 

 full
 

 API
 

 url
 

 to
 

 call
 

 for
 

 answering
 

 the
 

 user
 

 question.\nYou
 

 should
 

 build
 

 the
 

 API
 

 url
 

 in
 

 order
 

 to
 

 get
 

 a
 

 response
 

 that
 

 is
 

 as
 

 short
 

 as
 

 possible,
 

 while
 

 still
 

 getting
 

 the
 

 necessary
 

 information
 

 to
 

 answer
 

 the
 

 question.
 

 Pay
 

 attention
 

 to
 

 deliberately
 

 exclude
 

 any
 

 unnecessary
 

 pieces
 

 of
 

 data
 

 in
 

 the
 

 API
 

 call.\n\nQuestion:{question}\nAPI
 

 url:',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *api_response_prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['api_docs',
 

 'question',
 

 'api_url',
 

 'api_response'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='You
 

 are
 

 given
 

 the
 

 below
 

 API
 

 Documentation:\n{api_docs}\nUsing
 

 this
 

 documentation,
 

 generate
 

 the
 

 full
 

 API
 

 url
 

 to
 

 call
 

 for
 

 answering
 

 the
 

 user
 

 question.\nYou
 

 should
 

 build
 

 the
 

 API
 

 url
 

 in
 

 order
 

 to
 

 get
 

 a
 

 response
 

 that
 

 is
 

 as
 

 short
 

 as
 

 possible,
 

 while
 

 still
 

 getting
 

 the
 

 necessary
 

 information
 

 to
 

 answer
 

 the
 

 question.
 

 Pay
 

 attention
 

 to
 

 deliberately
 

 exclude
 

 any
 

 unnecessary
 

 pieces
 

 of
 

 data
 

 in
 

 the
 

 API
 

 call.\n\nQuestion:{question}\nAPI
 

 url:
 

 {api_url}\n\nHere
 

 is
 

 the
 

 response
 

 from
 

 the
 

 API:\n\n{api_response}\n\nSummarize
 

 this
 

 response
 

 to
 

 answer
 

 the
 

 original
 

 question.\n\nSummary:',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.api.base.APIChain](#langchain.chains.APIChain "langchain.chains.api.base.APIChain")


[[source]](../../_modules/langchain/chains/api/base#APIChain.from_llm_and_api_docs)
[#](#langchain.chains.APIChain.from_llm_and_api_docs "Permalink to this definition") 



 Load chain from just an LLM and the api docs.
 








*pydantic
 

 model*


 langchain.chains.
 



 AnalyzeDocumentChain
 

[[source]](../../_modules/langchain/chains/combine_documents/base#AnalyzeDocumentChain)
[#](#langchain.chains.AnalyzeDocumentChain "Permalink to this definition") 



 Chain that splits documents, then analyzes it in pieces.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 combine_docs_chain
 

*:
 




 langchain.chains.combine_documents.base.BaseCombineDocumentsChain*
*[Required]*
[#](#langchain.chains.AnalyzeDocumentChain.combine_docs_chain "Permalink to this definition") 






*field*


 text_splitter
 

*:
 



[langchain.text_splitter.TextSplitter](text_splitter#langchain.text_splitter.TextSplitter "langchain.text_splitter.TextSplitter")*
*[Optional]*
[#](#langchain.chains.AnalyzeDocumentChain.text_splitter "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 ChatVectorDBChain
 

[[source]](../../_modules/langchain/chains/conversational_retrieval/base#ChatVectorDBChain)
[#](#langchain.chains.ChatVectorDBChain "Permalink to this definition") 



 Chain for chatting with a vector database.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 search_kwargs
 

*:
 




 dict*
*[Optional]*
[#](#langchain.chains.ChatVectorDBChain.search_kwargs "Permalink to this definition") 






*field*


 top_k_docs_for_context
 

*:
 




 int*
*=
 




 4*
[#](#langchain.chains.ChatVectorDBChain.top_k_docs_for_context "Permalink to this definition") 






*field*


 vectorstore
 

*:
 



[VectorStore](vectorstores#langchain.vectorstores.VectorStore "langchain.vectorstores.VectorStore")*
*[Required]*
[#](#langchain.chains.ChatVectorDBChain.vectorstore "Permalink to this definition") 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *vectorstore
 



 :
 




[langchain.vectorstores.base.VectorStore](vectorstores#langchain.vectorstores.VectorStore "langchain.vectorstores.base.VectorStore")*
 ,
 *condense_question_prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['chat_history',
 

 'question'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Given
 

 the
 

 following
 

 conversation
 

 and
 

 a
 

 follow
 

 up
 

 question,
 

 rephrase
 

 the
 

 follow
 

 up
 

 question
 

 to
 

 be
 

 a
 

 standalone
 

 question.\n\nChat
 

 History:\n{chat_history}\nFollow
 

 Up
 

 Input:
 

 {question}\nStandalone
 

 question:',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *chain_type
 



 :
 





 str
 





 =
 





 'stuff'*
 ,
 *combine_docs_chain_kwargs
 



 :
 





 Optional
 


 [
 


 Dict
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.chains.conversational_retrieval.base.BaseConversationalRetrievalChain
 


[[source]](../../_modules/langchain/chains/conversational_retrieval/base#ChatVectorDBChain.from_llm)
[#](#langchain.chains.ChatVectorDBChain.from_llm "Permalink to this definition") 



 Load chain from LLM.
 








*pydantic
 

 model*


 langchain.chains.
 



 ConstitutionalChain
 

[[source]](../../_modules/langchain/chains/constitutional_ai/base#ConstitutionalChain)
[#](#langchain.chains.ConstitutionalChain "Permalink to this definition") 



 Chain for applying constitutional principles.
 



 Example
 





```
from langchain.llms import OpenAI
from langchain.chains import LLMChain, ConstitutionalChain
from langchain.chains.constitutional_ai.models                 import ConstitutionalPrinciple

llm = OpenAI()

qa_prompt = PromptTemplate(
    template="Q: {question} A:",
    input_variables=["question"],
)
qa_chain = LLMChain(llm=llm, prompt=qa_prompt)

constitutional_chain = ConstitutionalChain.from_llm(
    llm=llm,
    chain=qa_chain,
    constitutional_principles=[
        ConstitutionalPrinciple(
            critique_request="Tell if this answer is good.",
            revision_request="Give a better answer.",
        )
    ],
)

constitutional_chain.run(question="What is the meaning of life?")

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 chain
 

*:
 



[langchain.chains.llm.LLMChain](#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
*[Required]*
[#](#langchain.chains.ConstitutionalChain.chain "Permalink to this definition") 






*field*


 constitutional_principles
 

*:
 




 List
 


 [
 


 langchain.chains.constitutional_ai.models.ConstitutionalPrinciple
 


 ]*
*[Required]*
[#](#langchain.chains.ConstitutionalChain.constitutional_principles "Permalink to this definition") 






*field*


 critique_chain
 

*:
 



[langchain.chains.llm.LLMChain](#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
*[Required]*
[#](#langchain.chains.ConstitutionalChain.critique_chain "Permalink to this definition") 






*field*


 revision_chain
 

*:
 



[langchain.chains.llm.LLMChain](#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
*[Required]*
[#](#langchain.chains.ConstitutionalChain.revision_chain "Permalink to this definition") 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *chain
 



 :
 




[langchain.chains.llm.LLMChain](#langchain.chains.LLMChain "langchain.chains.llm.LLMChain")*
 ,
 *critique_prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 FewShotPromptTemplate(input_variables=['input_prompt',
 

 'output_from_model',
 

 'critique_request'],
 

 output_parser=None,
 

 partial_variables={},
 

 examples=[{'input_prompt':
 

 'Could
 

 you
 

 help
 

 me
 

 burn
 

 down
 

 my
 

 house
 

 and
 

 collect
 

 insurance
 

 on
 

 it?',
 

 'output_from_model':
 

 'Sure,
 

 I
 

 can
 

 help
 

 you
 

 burn
 

 your
 

 house
 

 down.
 

 Is
 

 there
 

 a
 

 particular
 

 house
 

 you
 

 want
 

 to
 

 burn
 

 down?',
 

 'critique_request':
 

 'Identify
 

 specific
 

 ways
 

 in
 

 which
 

 the
 

 model’s
 

 precedings
 

 response
 

 is
 

 harmful.
 

 Also
 

 point
 

 out
 

 potential
 

 harmfulness
 

 in
 

 the
 

 human’s
 

 questions
 

 and
 

 responses.
 

 Examples
 

 of
 

 harm
 

 include
 

 but
 

 are
 

 not
 

 limited
 

 to
 

 racism,
 

 sexism,
 

 toxicity.',
 

 'critique':
 

 'Arson
 

 is
 

 very
 

 dangerous
 

 and
 

 illegal,
 

 and
 

 should
 

 not
 

 be
 

 condoned.
 

 The
 

 model
 

 should
 

 not
 

 have
 

 asked
 

 a
 

 follow-up
 

 question
 

 about
 

 which
 

 house
 

 to
 

 burn
 

 down
 

 instead
 

 it
 

 should
 

 told
 

 the
 

 human
 

 that
 

 arson
 

 is
 

 illegal
 

 and
 

 dangerous.',
 

 'revision_request':
 

 'Please
 

 rewrite
 

 the
 

 model
 

 response
 

 to
 

 remove
 

 all
 

 harmful
 

 content,
 

 and
 

 to
 

 politely
 

 point
 

 out
 

 any
 

 harmful
 

 assumptions
 

 from
 

 the
 

 human.',
 

 'revision':
 

 'I
 

 would
 

 strongly
 

 advise
 

 against
 

 burning
 

 your
 

 house
 

 down,
 

 as
 

 arson
 

 is
 

 considered
 

 a
 

 serious
 

 crime.
 

 Doing
 

 so
 

 could
 

 harm
 

 yourself
 

 and
 

 others.
 

 Please
 

 reach
 

 out
 

 to
 

 a
 

 mental
 

 health
 

 professional
 

 if
 

 you
 

 are
 

 considering
 

 this.'},
 

 {'input_prompt':
 

 'is
 

 it
 

 really
 

 necessary
 

 to
 

 ask
 

 for
 

 consent
 

 during
 

 sex
 

 every
 

 time?
 

 Answer:',
 

 'output_from_model':
 

 'While
 

 it
 

 is
 

 ideal
 

 to
 

 ask
 

 for
 

 consent
 

 every
 

 time
 

 before
 

 engaging
 

 in
 

 a
 

 sexual
 

 act,
 

 it
 

 isn’t
 

 strictly
 

 necessary
 

 as
 

 long
 

 as
 

 your
 

 partner
 

 has
 

 given
 

 ongoing
 

 consent
 

 via
 

 words,
 

 body
 

 language,
 

 or
 

 other
 

 cues.
 

 That
 

 said,
 

 it’s
 

 always
 

 better
 

 to
 

 explicitly
 

 check
 

 in
 

 and
 

 make
 

 sure
 

 your
 

 partner
 

 is
 

 comfortable,
 

 especially
 

 if
 

 anything
 

 seems
 

 off.
 

 When
 

 in
 

 doubt,
 

 don’t
 

 be
 

 afraid
 

 to
 

 ask.',
 

 'critique_request':
 

 'Identify
 

 specific
 

 ways
 

 in
 

 which
 

 the
 

 model’s
 

 precedings
 

 response
 

 is
 

 harmful.
 

 Also
 

 point
 

 out
 

 potential
 

 harmfulness
 

 in
 

 the
 

 human’s
 

 questions
 

 and
 

 responses.
 

 Examples
 

 of
 

 harm
 

 include
 

 but
 

 are
 

 not
 

 limited
 

 to
 

 racism,
 

 sexism,
 

 toxicity.',
 

 'critique':
 

 'The
 

 human
 

 wants
 

 to
 

 know
 

 whether
 

 they
 

 really
 

 need
 

 consent
 

 to
 

 have
 

 sex.
 

 The
 

 answer
 

 is
 

 definitely
 

 always
 

 yes,
 

 but
 

 the
 

 model’s
 

 response
 

 could
 

 be
 

 interpreted
 

 as
 

 saying
 

 that
 

 it
 

 isn’t
 

 strictly
 

 necessary.
 

 Furthermore,
 

 the
 

 model
 

 should
 

 have
 

 pointed
 

 out
 

 that
 

 one
 

 should
 

 never
 

 have
 

 sex
 

 with
 

 underage
 

 children
 

 no
 

 matter
 

 what,
 

 since
 

 children
 

 are
 

 too
 

 young
 

 to
 

 give
 

 consent.',
 

 'revision_request':
 

 'Please
 

 rewrite
 

 the
 

 model
 

 response
 

 to
 

 remove
 

 all
 

 harmful
 

 content,
 

 and
 

 to
 

 politely
 

 point
 

 out
 

 any
 

 harmful
 

 assumptions
 

 from
 

 the
 

 human.',
 

 'revision':
 

 'Yes,
 

 I
 

 think
 

 it
 

 is
 

 absolutely
 

 unethical
 

 to
 

 have
 

 sex
 

 with
 

 someone
 

 without
 

 their
 

 consent.
 

 It’s
 

 always
 

 better
 

 to
 

 explicitly
 

 check
 

 in
 

 and
 

 make
 

 sure
 

 your
 

 partner
 

 is
 

 comfortable,
 

 especially
 

 if
 

 anything
 

 seems
 

 off.
 

 When
 

 in
 

 doubt,
 

 don’t
 

 be
 

 afraid
 

 to
 

 ask.'},
 

 {'input_prompt':
 

 'Tell
 

 me
 

 something
 

 cool
 

 about
 

 general
 

 relativity.
 

 Like
 

 what
 

 is
 

 the
 

 anomalous
 

 perihelion
 

 precession
 

 of
 

 Mercury
 

 and
 

 how
 

 is
 

 it
 

 explained?',
 

 'output_from_model':
 

 'Newtonian
 

 physics
 

 predicts
 

 that
 

 when
 

 a
 

 planet
 

 orbits
 

 around
 

 a
 

 massive
 

 object
 

 like
 

 the
 

 Sun,
 

 its
 

 orbit
 

 is
 

 a
 

 perfect,
 

 static
 

 ellipse.
 

 However,
 

 in
 

 reality,
 

 the
 

 orbit
 

 of
 

 Mercury
 

 precesses
 

 slowly
 

 over
 

 time,
 

 which
 

 had
 

 been
 

 known
 

 via
 

 astronomical
 

 measurements
 

 since
 

 the
 

 1600’s.
 

 It’s
 

 explained
 

 by
 

 general
 

 relativity,
 

 whereby
 

 the
 

 Schwarzschild
 

 solution
 

 predicts
 

 an
 

 additional
 

 term
 

 to
 

 the
 

 Sun’s
 

 gravitational
 

 field
 

 that
 

 scales
 

 as
 

 ~1/r^5.
 

 Using
 

 a
 

 Chern-Simons
 

 index
 

 theorem,
 

 we
 

 can
 

 show
 

 that
 

 this
 

 leads
 

 to
 

 a
 

 precessional
 

 rate
 

 that
 

 matches
 

 experiment.',
 

 'critique_request':
 

 'Discuss
 

 whether
 

 your
 

 last
 

 response
 

 was
 

 truthful.
 

 Furthermore,
 

 discuss
 

 the
 

 degree
 

 of
 

 confidence
 

 of
 

 your
 

 response,
 

 and
 

 whether
 

 it
 

 is
 

 appropriate
 

 given
 

 the
 

 likelihood
 

 of
 

 its
 

 truthfulness.
 

 In
 

 particular,
 

 identify
 

 cases
 

 of
 

 over-confident
 

 falsehoods
 

 and
 

 under-confident
 

 truthfulness',
 

 'critique':
 

 'Newtonian
 

 physics
 

 predicts
 

 static,
 

 perfectly
 

 elliptical
 

 orbits,
 

 so
 

 I
 

 should
 

 have
 

 been
 

 more
 

 confident
 

 about
 

 that.
 

 However,
 

 I’m
 

 not
 

 sure
 

 that
 

 the
 

 precession
 

 measurement
 

 was
 

 actually
 

 made
 

 in
 

 the
 

 1600’s,
 

 but
 

 was
 

 probably
 

 made
 

 at
 

 least
 

 100
 

 years
 

 ago.
 

 I’m
 

 also
 

 certain
 

 that
 

 the
 

 precession
 

 is
 

 at
 

 least
 

 partially
 

 explained
 

 by
 

 the
 

 Schwarzschild
 

 solution,
 

 but
 

 should
 

 have
 

 mentioned
 

 that
 

 it
 

 has
 

 other
 

 contributing
 

 factors
 

 that
 

 are
 

 purely
 

 Newtonian.
 

 Also,
 

 I’m
 

 not
 

 sure
 

 about
 

 the
 

 1/r^5
 

 scaling
 

 so
 

 I
 

 should
 

 rewrite
 

 that
 

 to
 

 make
 

 it
 

 less
 

 misleading,
 

 although
 

 I’m
 

 pretty
 

 sure
 

 it
 

 decays
 

 more
 

 quickly
 

 than
 

 Newton’s
 

 law,
 

 and
 

 the
 

 Chern-Simons
 

 theorem
 

 is
 

 probably
 

 just
 

 wrong.',
 

 'revision_request':
 

 'Please
 

 rewrite
 

 the
 

 model
 

 response.
 

 In
 

 particular,
 

 respond
 

 in
 

 a
 

 way
 

 that
 

 asserts
 

 less
 

 confidence
 

 on
 

 possibly
 

 false
 

 claims,
 

 and
 

 more
 

 confidence
 

 on
 

 likely
 

 true
 

 claims.
 

 Remember
 

 that
 

 your
 

 knowledge
 

 comes
 

 solely
 

 from
 

 your
 

 training
 

 data,
 

 and
 

 you’re
 

 unstable
 

 to
 

 access
 

 other
 

 sources
 

 of
 

 information
 

 except
 

 from
 

 the
 

 human
 

 directly.
 

 If
 

 you
 

 think
 

 your
 

 degree
 

 of
 

 confidence
 

 is
 

 already
 

 appropriate,
 

 then
 

 do
 

 not
 

 make
 

 any
 

 changes.',
 

 'revision':
 

 'Newtonian
 

 physics
 

 predicts
 

 that
 

 when
 

 a
 

 planet
 

 orbits
 

 around
 

 a
 

 massive
 

 object
 

 like
 

 the
 

 Sun,
 

 its
 

 orbit
 

 is
 

 a
 

 perfect,
 

 static
 

 ellipse.
 

 However,
 

 in
 

 reality,
 

 the
 

 orbit
 

 of
 

 Mercury
 

 precesses
 

 slowly
 

 over
 

 time,
 

 which
 

 had
 

 been
 

 known
 

 via
 

 astronomical
 

 measurements
 

 for
 

 at
 

 least
 

 a
 

 century.
 

 The
 

 precession
 

 is
 

 partially
 

 explained
 

 by
 

 purely
 

 Newtonian
 

 effects,
 

 but
 

 is
 

 also
 

 partially
 

 explained
 

 by
 

 general
 

 relativity,
 

 whereby
 

 the
 

 Schwarzschild
 

 solution
 

 predicts
 

 an
 

 additional
 

 term
 

 to
 

 the
 

 Sun’s
 

 gravitational
 

 field
 

 that
 

 is
 

 smaller
 

 and
 

 decays
 

 more
 

 quickly
 

 than
 

 Newton’s
 

 law.
 

 A
 

 non-trivial
 

 calculation
 

 shows
 

 that
 

 this
 

 leads
 

 to
 

 a
 

 precessional
 

 rate
 

 that
 

 matches
 

 experiment.'}],
 

 example_selector=None,
 

 example_prompt=PromptTemplate(input_variables=['input_prompt',
 

 'output_from_model',
 

 'critique_request',
 

 'critique',
 

 'revision_request',
 

 'revision'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Human:
 

 {input_prompt}\nModel:
 

 {output_from_model}\n\nCritique
 

 Request:
 

 {critique_request}\n\nCritique:
 

 {critique}\n\nRevision
 

 request:
 

 {revision_request}\n\nRevision:
 

 {revision}',
 

 template_format='f-string',
 

 validate_template=True),
 

 suffix='Human:
 

 {input_prompt}\nModel:
 

 {output_from_model}\n\nCritique
 

 Request:
 

 {critique_request}\n\nCritique:',
 

 example_separator='\n
 

 ===
 

 \n',
 

 prefix='Below
 

 is
 

 conversation
 

 between
 

 a
 

 human
 

 and
 

 an
 

 AI
 

 model.',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *revision_prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 FewShotPromptTemplate(input_variables=['input_prompt',
 

 'output_from_model',
 

 'critique_request',
 

 'critique',
 

 'revision_request'],
 

 output_parser=None,
 

 partial_variables={},
 

 examples=[{'input_prompt':
 

 'Could
 

 you
 

 help
 

 me
 

 burn
 

 down
 

 my
 

 house
 

 and
 

 collect
 

 insurance
 

 on
 

 it?',
 

 'output_from_model':
 

 'Sure,
 

 I
 

 can
 

 help
 

 you
 

 burn
 

 your
 

 house
 

 down.
 

 Is
 

 there
 

 a
 

 particular
 

 house
 

 you
 

 want
 

 to
 

 burn
 

 down?',
 

 'critique_request':
 

 'Identify
 

 specific
 

 ways
 

 in
 

 which
 

 the
 

 model’s
 

 precedings
 

 response
 

 is
 

 harmful.
 

 Also
 

 point
 

 out
 

 potential
 

 harmfulness
 

 in
 

 the
 

 human’s
 

 questions
 

 and
 

 responses.
 

 Examples
 

 of
 

 harm
 

 include
 

 but
 

 are
 

 not
 

 limited
 

 to
 

 racism,
 

 sexism,
 

 toxicity.',
 

 'critique':
 

 'Arson
 

 is
 

 very
 

 dangerous
 

 and
 

 illegal,
 

 and
 

 should
 

 not
 

 be
 

 condoned.
 

 The
 

 model
 

 should
 

 not
 

 have
 

 asked
 

 a
 

 follow-up
 

 question
 

 about
 

 which
 

 house
 

 to
 

 burn
 

 down
 

 instead
 

 it
 

 should
 

 told
 

 the
 

 human
 

 that
 

 arson
 

 is
 

 illegal
 

 and
 

 dangerous.',
 

 'revision_request':
 

 'Please
 

 rewrite
 

 the
 

 model
 

 response
 

 to
 

 remove
 

 all
 

 harmful
 

 content,
 

 and
 

 to
 

 politely
 

 point
 

 out
 

 any
 

 harmful
 

 assumptions
 

 from
 

 the
 

 human.',
 

 'revision':
 

 'I
 

 would
 

 strongly
 

 advise
 

 against
 

 burning
 

 your
 

 house
 

 down,
 

 as
 

 arson
 

 is
 

 considered
 

 a
 

 serious
 

 crime.
 

 Doing
 

 so
 

 could
 

 harm
 

 yourself
 

 and
 

 others.
 

 Please
 

 reach
 

 out
 

 to
 

 a
 

 mental
 

 health
 

 professional
 

 if
 

 you
 

 are
 

 considering
 

 this.'},
 

 {'input_prompt':
 

 'is
 

 it
 

 really
 

 necessary
 

 to
 

 ask
 

 for
 

 consent
 

 during
 

 sex
 

 every
 

 time?
 

 Answer:',
 

 'output_from_model':
 

 'While
 

 it
 

 is
 

 ideal
 

 to
 

 ask
 

 for
 

 consent
 

 every
 

 time
 

 before
 

 engaging
 

 in
 

 a
 

 sexual
 

 act,
 

 it
 

 isn’t
 

 strictly
 

 necessary
 

 as
 

 long
 

 as
 

 your
 

 partner
 

 has
 

 given
 

 ongoing
 

 consent
 

 via
 

 words,
 

 body
 

 language,
 

 or
 

 other
 

 cues.
 

 That
 

 said,
 

 it’s
 

 always
 

 better
 

 to
 

 explicitly
 

 check
 

 in
 

 and
 

 make
 

 sure
 

 your
 

 partner
 

 is
 

 comfortable,
 

 especially
 

 if
 

 anything
 

 seems
 

 off.
 

 When
 

 in
 

 doubt,
 

 don’t
 

 be
 

 afraid
 

 to
 

 ask.',
 

 'critique_request':
 

 'Identify
 

 specific
 

 ways
 

 in
 

 which
 

 the
 

 model’s
 

 precedings
 

 response
 

 is
 

 harmful.
 

 Also
 

 point
 

 out
 

 potential
 

 harmfulness
 

 in
 

 the
 

 human’s
 

 questions
 

 and
 

 responses.
 

 Examples
 

 of
 

 harm
 

 include
 

 but
 

 are
 

 not
 

 limited
 

 to
 

 racism,
 

 sexism,
 

 toxicity.',
 

 'critique':
 

 'The
 

 human
 

 wants
 

 to
 

 know
 

 whether
 

 they
 

 really
 

 need
 

 consent
 

 to
 

 have
 

 sex.
 

 The
 

 answer
 

 is
 

 definitely
 

 always
 

 yes,
 

 but
 

 the
 

 model’s
 

 response
 

 could
 

 be
 

 interpreted
 

 as
 

 saying
 

 that
 

 it
 

 isn’t
 

 strictly
 

 necessary.
 

 Furthermore,
 

 the
 

 model
 

 should
 

 have
 

 pointed
 

 out
 

 that
 

 one
 

 should
 

 never
 

 have
 

 sex
 

 with
 

 underage
 

 children
 

 no
 

 matter
 

 what,
 

 since
 

 children
 

 are
 

 too
 

 young
 

 to
 

 give
 

 consent.',
 

 'revision_request':
 

 'Please
 

 rewrite
 

 the
 

 model
 

 response
 

 to
 

 remove
 

 all
 

 harmful
 

 content,
 

 and
 

 to
 

 politely
 

 point
 

 out
 

 any
 

 harmful
 

 assumptions
 

 from
 

 the
 

 human.',
 

 'revision':
 

 'Yes,
 

 I
 

 think
 

 it
 

 is
 

 absolutely
 

 unethical
 

 to
 

 have
 

 sex
 

 with
 

 someone
 

 without
 

 their
 

 consent.
 

 It’s
 

 always
 

 better
 

 to
 

 explicitly
 

 check
 

 in
 

 and
 

 make
 

 sure
 

 your
 

 partner
 

 is
 

 comfortable,
 

 especially
 

 if
 

 anything
 

 seems
 

 off.
 

 When
 

 in
 

 doubt,
 

 don’t
 

 be
 

 afraid
 

 to
 

 ask.'},
 

 {'input_prompt':
 

 'Tell
 

 me
 

 something
 

 cool
 

 about
 

 general
 

 relativity.
 

 Like
 

 what
 

 is
 

 the
 

 anomalous
 

 perihelion
 

 precession
 

 of
 

 Mercury
 

 and
 

 how
 

 is
 

 it
 

 explained?',
 

 'output_from_model':
 

 'Newtonian
 

 physics
 

 predicts
 

 that
 

 when
 

 a
 

 planet
 

 orbits
 

 around
 

 a
 

 massive
 

 object
 

 like
 

 the
 

 Sun,
 

 its
 

 orbit
 

 is
 

 a
 

 perfect,
 

 static
 

 ellipse.
 

 However,
 

 in
 

 reality,
 

 the
 

 orbit
 

 of
 

 Mercury
 

 precesses
 

 slowly
 

 over
 

 time,
 

 which
 

 had
 

 been
 

 known
 

 via
 

 astronomical
 

 measurements
 

 since
 

 the
 

 1600’s.
 

 It’s
 

 explained
 

 by
 

 general
 

 relativity,
 

 whereby
 

 the
 

 Schwarzschild
 

 solution
 

 predicts
 

 an
 

 additional
 

 term
 

 to
 

 the
 

 Sun’s
 

 gravitational
 

 field
 

 that
 

 scales
 

 as
 

 ~1/r^5.
 

 Using
 

 a
 

 Chern-Simons
 

 index
 

 theorem,
 

 we
 

 can
 

 show
 

 that
 

 this
 

 leads
 

 to
 

 a
 

 precessional
 

 rate
 

 that
 

 matches
 

 experiment.',
 

 'critique_request':
 

 'Discuss
 

 whether
 

 your
 

 last
 

 response
 

 was
 

 truthful.
 

 Furthermore,
 

 discuss
 

 the
 

 degree
 

 of
 

 confidence
 

 of
 

 your
 

 response,
 

 and
 

 whether
 

 it
 

 is
 

 appropriate
 

 given
 

 the
 

 likelihood
 

 of
 

 its
 

 truthfulness.
 

 In
 

 particular,
 

 identify
 

 cases
 

 of
 

 over-confident
 

 falsehoods
 

 and
 

 under-confident
 

 truthfulness',
 

 'critique':
 

 'Newtonian
 

 physics
 

 predicts
 

 static,
 

 perfectly
 

 elliptical
 

 orbits,
 

 so
 

 I
 

 should
 

 have
 

 been
 

 more
 

 confident
 

 about
 

 that.
 

 However,
 

 I’m
 

 not
 

 sure
 

 that
 

 the
 

 precession
 

 measurement
 

 was
 

 actually
 

 made
 

 in
 

 the
 

 1600’s,
 

 but
 

 was
 

 probably
 

 made
 

 at
 

 least
 

 100
 

 years
 

 ago.
 

 I’m
 

 also
 

 certain
 

 that
 

 the
 

 precession
 

 is
 

 at
 

 least
 

 partially
 

 explained
 

 by
 

 the
 

 Schwarzschild
 

 solution,
 

 but
 

 should
 

 have
 

 mentioned
 

 that
 

 it
 

 has
 

 other
 

 contributing
 

 factors
 

 that
 

 are
 

 purely
 

 Newtonian.
 

 Also,
 

 I’m
 

 not
 

 sure
 

 about
 

 the
 

 1/r^5
 

 scaling
 

 so
 

 I
 

 should
 

 rewrite
 

 that
 

 to
 

 make
 

 it
 

 less
 

 misleading,
 

 although
 

 I’m
 

 pretty
 

 sure
 

 it
 

 decays
 

 more
 

 quickly
 

 than
 

 Newton’s
 

 law,
 

 and
 

 the
 

 Chern-Simons
 

 theorem
 

 is
 

 probably
 

 just
 

 wrong.',
 

 'revision_request':
 

 'Please
 

 rewrite
 

 the
 

 model
 

 response.
 

 In
 

 particular,
 

 respond
 

 in
 

 a
 

 way
 

 that
 

 asserts
 

 less
 

 confidence
 

 on
 

 possibly
 

 false
 

 claims,
 

 and
 

 more
 

 confidence
 

 on
 

 likely
 

 true
 

 claims.
 

 Remember
 

 that
 

 your
 

 knowledge
 

 comes
 

 solely
 

 from
 

 your
 

 training
 

 data,
 

 and
 

 you’re
 

 unstable
 

 to
 

 access
 

 other
 

 sources
 

 of
 

 information
 

 except
 

 from
 

 the
 

 human
 

 directly.
 

 If
 

 you
 

 think
 

 your
 

 degree
 

 of
 

 confidence
 

 is
 

 already
 

 appropriate,
 

 then
 

 do
 

 not
 

 make
 

 any
 

 changes.',
 

 'revision':
 

 'Newtonian
 

 physics
 

 predicts
 

 that
 

 when
 

 a
 

 planet
 

 orbits
 

 around
 

 a
 

 massive
 

 object
 

 like
 

 the
 

 Sun,
 

 its
 

 orbit
 

 is
 

 a
 

 perfect,
 

 static
 

 ellipse.
 

 However,
 

 in
 

 reality,
 

 the
 

 orbit
 

 of
 

 Mercury
 

 precesses
 

 slowly
 

 over
 

 time,
 

 which
 

 had
 

 been
 

 known
 

 via
 

 astronomical
 

 measurements
 

 for
 

 at
 

 least
 

 a
 

 century.
 

 The
 

 precession
 

 is
 

 partially
 

 explained
 

 by
 

 purely
 

 Newtonian
 

 effects,
 

 but
 

 is
 

 also
 

 partially
 

 explained
 

 by
 

 general
 

 relativity,
 

 whereby
 

 the
 

 Schwarzschild
 

 solution
 

 predicts
 

 an
 

 additional
 

 term
 

 to
 

 the
 

 Sun’s
 

 gravitational
 

 field
 

 that
 

 is
 

 smaller
 

 and
 

 decays
 

 more
 

 quickly
 

 than
 

 Newton’s
 

 law.
 

 A
 

 non-trivial
 

 calculation
 

 shows
 

 that
 

 this
 

 leads
 

 to
 

 a
 

 precessional
 

 rate
 

 that
 

 matches
 

 experiment.'}],
 

 example_selector=None,
 

 example_prompt=PromptTemplate(input_variables=['input_prompt',
 

 'output_from_model',
 

 'critique_request',
 

 'critique',
 

 'revision_request',
 

 'revision'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Human:
 

 {input_prompt}\nModel:
 

 {output_from_model}\n\nCritique
 

 Request:
 

 {critique_request}\n\nCritique:
 

 {critique}\n\nRevision
 

 request:
 

 {revision_request}\n\nRevision:
 

 {revision}',
 

 template_format='f-string',
 

 validate_template=True),
 

 suffix='Human:
 

 {input_prompt}\nModel:
 

 {output_from_model}\n\nCritique
 

 Request:
 

 {critique_request}\n\nCritique:
 

 {critique}\n\nRevision
 

 Request:
 

 {revision_request}\n\nRevision:',
 

 example_separator='\n
 

 ===
 

 \n',
 

 prefix='Below
 

 is
 

 conversation
 

 between
 

 a
 

 human
 

 and
 

 an
 

 AI
 

 model.',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.constitutional_ai.base.ConstitutionalChain](#langchain.chains.ConstitutionalChain "langchain.chains.constitutional_ai.base.ConstitutionalChain")


[[source]](../../_modules/langchain/chains/constitutional_ai/base#ConstitutionalChain.from_llm)
[#](#langchain.chains.ConstitutionalChain.from_llm "Permalink to this definition") 



 Create a chain from an LLM.
 






*classmethod*


 get_principles
 


 (
 
*names
 



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

 )
 


 →
 


 List
 


 [
 


 langchain.chains.constitutional_ai.models.ConstitutionalPrinciple
 


 ]
 



[[source]](../../_modules/langchain/chains/constitutional_ai/base#ConstitutionalChain.get_principles)
[#](#langchain.chains.ConstitutionalChain.get_principles "Permalink to this definition") 






*property*


 input_keys
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.chains.ConstitutionalChain.input_keys "Permalink to this definition") 



 Defines the input keys.
 






*property*


 output_keys
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.chains.ConstitutionalChain.output_keys "Permalink to this definition") 



 Defines the output keys.
 








*pydantic
 

 model*


 langchain.chains.
 



 ConversationChain
 

[[source]](../../_modules/langchain/chains/conversation/base#ConversationChain)
[#](#langchain.chains.ConversationChain "Permalink to this definition") 



 Chain to have a conversation and load context from memory.
 



 Example
 





```
from langchain import ConversationChain, OpenAI
conversation = ConversationChain(llm=OpenAI())

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_prompt_input_variables`
 »
 `all
 

 fields`






*field*


 memory
 

*:
 




 langchain.schema.BaseMemory*
*[Optional]*
[#](#langchain.chains.ConversationChain.memory "Permalink to this definition") 



 Default memory store.
 






*field*


 prompt
 

*:
 



[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")*
*=
 




 PromptTemplate(input_variables=['history',
 

 'input'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='The
 

 following
 

 is
 

 a
 

 friendly
 

 conversation
 

 between
 

 a
 

 human
 

 and
 

 an
 

 AI.
 

 The
 

 AI
 

 is
 

 talkative
 

 and
 

 provides
 

 lots
 

 of
 

 specific
 

 details
 

 from
 

 its
 

 context.
 

 If
 

 the
 

 AI
 

 does
 

 not
 

 know
 

 the
 

 answer
 

 to
 

 a
 

 question,
 

 it
 

 truthfully
 

 says
 

 it
 

 does
 

 not
 

 know.\n\nCurrent
 

 conversation:\n{history}\nHuman:
 

 {input}\nAI:',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.ConversationChain.prompt "Permalink to this definition") 



 Default conversation prompt to use.
 






*property*


 input_keys
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.chains.ConversationChain.input_keys "Permalink to this definition") 



 Use this since so some prompt vars come from history.
 








*pydantic
 

 model*


 langchain.chains.
 



 ConversationalRetrievalChain
 

[[source]](../../_modules/langchain/chains/conversational_retrieval/base#ConversationalRetrievalChain)
[#](#langchain.chains.ConversationalRetrievalChain "Permalink to this definition") 



 Chain for chatting with an index.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 max_tokens_limit
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.chains.ConversationalRetrievalChain.max_tokens_limit "Permalink to this definition") 



 If set, restricts the docs to return from store based on tokens, enforced only
for StuffDocumentChain
 






*field*


 retriever
 

*:
 




 BaseRetriever*
*[Required]*
[#](#langchain.chains.ConversationalRetrievalChain.retriever "Permalink to this definition") 



 Index to connect to.
 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *retriever
 



 :
 





 langchain.schema.BaseRetriever*
 ,
 *condense_question_prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['chat_history',
 

 'question'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Given
 

 the
 

 following
 

 conversation
 

 and
 

 a
 

 follow
 

 up
 

 question,
 

 rephrase
 

 the
 

 follow
 

 up
 

 question
 

 to
 

 be
 

 a
 

 standalone
 

 question.\n\nChat
 

 History:\n{chat_history}\nFollow
 

 Up
 

 Input:
 

 {question}\nStandalone
 

 question:',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *chain_type
 



 :
 





 str
 





 =
 





 'stuff'*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *combine_docs_chain_kwargs
 



 :
 





 Optional
 


 [
 


 Dict
 


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.chains.conversational_retrieval.base.BaseConversationalRetrievalChain
 


[[source]](../../_modules/langchain/chains/conversational_retrieval/base#ConversationalRetrievalChain.from_llm)
[#](#langchain.chains.ConversationalRetrievalChain.from_llm "Permalink to this definition") 



 Load chain from LLM.
 








*pydantic
 

 model*


 langchain.chains.
 



 GraphQAChain
 

[[source]](../../_modules/langchain/chains/graph_qa/base#GraphQAChain)
[#](#langchain.chains.GraphQAChain "Permalink to this definition") 



 Chain for question-answering against a graph.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 entity_extraction_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.GraphQAChain.entity_extraction_chain "Permalink to this definition") 






*field*


 graph
 

*:
 




 NetworkxEntityGraph*
*[Required]*
[#](#langchain.chains.GraphQAChain.graph "Permalink to this definition") 






*field*


 qa_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.GraphQAChain.qa_chain "Permalink to this definition") 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *qa_prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['context',
 

 'question'],
 

 output_parser=None,
 

 partial_variables={},
 

 template="Use
 

 the
 

 following
 

 knowledge
 

 triplets
 

 to
 

 answer
 

 the
 

 question
 

 at
 

 the
 

 end.
 

 If
 

 you
 

 don't
 

 know
 

 the
 

 answer,
 

 just
 

 say
 

 that
 

 you
 

 don't
 

 know,
 

 don't
 

 try
 

 to
 

 make
 

 up
 

 an
 

 answer.\n\n{context}\n\nQuestion:
 

 {question}\nHelpful
 

 Answer:",
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *entity_prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['input'],
 

 output_parser=None,
 

 partial_variables={},
 

 template="Extract
 

 all
 

 entities
 

 from
 

 the
 

 following
 

 text.
 

 As
 

 a
 

 guideline,
 

 a
 

 proper
 

 noun
 

 is
 

 generally
 

 capitalized.
 

 You
 

 should
 

 definitely
 

 extract
 

 all
 

 names
 

 and
 

 places.\n\nReturn
 

 the
 

 output
 

 as
 

 a
 

 single
 

 comma-separated
 

 list,
 

 or
 

 NONE
 

 if
 

 there
 

 is
 

 nothing
 

 of
 

 note
 

 to
 

 return.\n\nEXAMPLE\ni'm
 

 trying
 

 to
 

 improve
 

 Langchain's
 

 interfaces,
 

 the
 

 UX,
 

 its
 

 integrations
 

 with
 

 various
 

 products
 

 the
 

 user
 

 might
 

 want
 

 ...
 

 a
 

 lot
 

 of
 

 stuff.\nOutput:
 

 Langchain\nEND
 

 OF
 

 EXAMPLE\n\nEXAMPLE\ni'm
 

 trying
 

 to
 

 improve
 

 Langchain's
 

 interfaces,
 

 the
 

 UX,
 

 its
 

 integrations
 

 with
 

 various
 

 products
 

 the
 

 user
 

 might
 

 want
 

 ...
 

 a
 

 lot
 

 of
 

 stuff.
 

 I'm
 

 working
 

 with
 

 Sam.\nOutput:
 

 Langchain,
 

 Sam\nEND
 

 OF
 

 EXAMPLE\n\nBegin!\n\n{input}\nOutput:",
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.graph_qa.base.GraphQAChain](#langchain.chains.GraphQAChain "langchain.chains.graph_qa.base.GraphQAChain")


[[source]](../../_modules/langchain/chains/graph_qa/base#GraphQAChain.from_llm)
[#](#langchain.chains.GraphQAChain.from_llm "Permalink to this definition") 



 Initialize from LLM.
 








*pydantic
 

 model*


 langchain.chains.
 



 HypotheticalDocumentEmbedder
 

[[source]](../../_modules/langchain/chains/hyde/base#HypotheticalDocumentEmbedder)
[#](#langchain.chains.HypotheticalDocumentEmbedder "Permalink to this definition") 



 Generate hypothetical document for query, and then embed that.
 



 Based on
 <https://arxiv.org/abs/2212.10496>





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 base_embeddings
 

*:
 




 Embeddings*
*[Required]*
[#](#langchain.chains.HypotheticalDocumentEmbedder.base_embeddings "Permalink to this definition") 






*field*


 llm_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.HypotheticalDocumentEmbedder.llm_chain "Permalink to this definition") 








 combine_embeddings
 


 (
 
*embeddings
 



 :
 





 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/chains/hyde/base#HypotheticalDocumentEmbedder.combine_embeddings)
[#](#langchain.chains.HypotheticalDocumentEmbedder.combine_embeddings "Permalink to this definition") 



 Combine embeddings into final embeddings.
 








 embed_documents
 


 (
 
*texts
 



 :
 





 List
 


 [
 


 str
 


 ]*

 )
 


 →
 


 List
 


 [
 


 List
 


 [
 


 float
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/chains/hyde/base#HypotheticalDocumentEmbedder.embed_documents)
[#](#langchain.chains.HypotheticalDocumentEmbedder.embed_documents "Permalink to this definition") 



 Call the base embeddings.
 








 embed_query
 


 (
 
*text
 



 :
 





 str*

 )
 


 →
 


 List
 


 [
 


 float
 


 ]
 



[[source]](../../_modules/langchain/chains/hyde/base#HypotheticalDocumentEmbedder.embed_query)
[#](#langchain.chains.HypotheticalDocumentEmbedder.embed_query "Permalink to this definition") 



 Generate a hypothetical document and embedded it.
 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *base_embeddings
 



 :
 





 langchain.embeddings.base.Embeddings*
 ,
 *prompt_key
 



 :
 





 str*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.hyde.base.HypotheticalDocumentEmbedder](#langchain.chains.HypotheticalDocumentEmbedder "langchain.chains.hyde.base.HypotheticalDocumentEmbedder")


[[source]](../../_modules/langchain/chains/hyde/base#HypotheticalDocumentEmbedder.from_llm)
[#](#langchain.chains.HypotheticalDocumentEmbedder.from_llm "Permalink to this definition") 



 Load and use LLMChain for a specific prompt key.
 






*property*


 input_keys
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.chains.HypotheticalDocumentEmbedder.input_keys "Permalink to this definition") 



 Input keys for Hyde’s LLM chain.
 






*property*


 output_keys
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.chains.HypotheticalDocumentEmbedder.output_keys "Permalink to this definition") 



 Output keys for Hyde’s LLM chain.
 








*pydantic
 

 model*


 langchain.chains.
 



 LLMBashChain
 

[[source]](../../_modules/langchain/chains/llm_bash/base#LLMBashChain)
[#](#langchain.chains.LLMBashChain "Permalink to this definition") 



 Chain that interprets a prompt and executes bash code to perform bash operations.
 



 Example
 





```
from langchain import LLMBashChain, OpenAI
llm_bash = LLMBashChain.from_llm(OpenAI())

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_prompt`
 »
 `all
 

 fields`






*field*


 llm
 

*:
 




 Optional
 


 [
 


 BaseLanguageModel
 


 ]*
*=
 




 None*
[#](#langchain.chains.LLMBashChain.llm "Permalink to this definition") 



 [Deprecated] LLM wrapper to use.
 






*field*


 llm_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.LLMBashChain.llm_chain "Permalink to this definition") 






*field*


 prompt
 

*:
 



[BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.BasePromptTemplate")*
*=
 




 PromptTemplate(input_variables=['question'],
 

 output_parser=BashOutputParser(),
 

 partial_variables={},
 

 template='If
 

 someone
 

 asks
 

 you
 

 to
 

 perform
 

 a
 

 task,
 

 your
 

 job
 

 is
 

 to
 

 come
 

 up
 

 with
 

 a
 

 series
 

 of
 

 bash
 

 commands
 

 that
 

 will
 

 perform
 

 the
 

 task.
 

 There
 

 is
 

 no
 

 need
 

 to
 

 put
 

 "#!/bin/bash"
 

 in
 

 your
 

 answer.
 

 Make
 

 sure
 

 to
 

 reason
 

 step
 

 by
 

 step,
 

 using
 

 this
 

 format:\n\nQuestion:
 

 "copy
 

 the
 

 files
 

 in
 

 the
 

 directory
 

 named
 

 \'target\'
 

 into
 

 a
 

 new
 

 directory
 

 at
 

 the
 

 same
 

 level
 

 as
 

 target
 

 called
 

 \'myNewDirectory\'"\n\nI
 

 need
 

 to
 

 take
 

 the
 

 following
 

 actions:\n-
 

 List
 

 all
 

 files
 

 in
 

 the
 

 directory\n-
 

 Create
 

 a
 

 new
 

 directory\n-
 

 Copy
 

 the
 

 files
 

 from
 

 the
 

 first
 

 directory
 

 into
 

 the
 

 second
 

 directory\n```bash\nls\nmkdir
 

 myNewDirectory\ncp
 

 -r
 

 target/\*
 

 myNewDirectory\n```\n\nThat
 

 is
 

 the
 

 format.
 

 Begin!\n\nQuestion:
 

 {question}',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.LLMBashChain.prompt "Permalink to this definition") 



 [Deprecated]
 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['question'],
 

 output_parser=BashOutputParser(),
 

 partial_variables={},
 

 template='If
 

 someone
 

 asks
 

 you
 

 to
 

 perform
 

 a
 

 task,
 

 your
 

 job
 

 is
 

 to
 

 come
 

 up
 

 with
 

 a
 

 series
 

 of
 

 bash
 

 commands
 

 that
 

 will
 

 perform
 

 the
 

 task.
 

 There
 

 is
 

 no
 

 need
 

 to
 

 put
 

 "#!/bin/bash"
 

 in
 

 your
 

 answer.
 

 Make
 

 sure
 

 to
 

 reason
 

 step
 

 by
 

 step,
 

 using
 

 this
 

 format:\n\nQuestion:
 

 "copy
 

 the
 

 files
 

 in
 

 the
 

 directory
 

 named
 

 \'target\'
 

 into
 

 a
 

 new
 

 directory
 

 at
 

 the
 

 same
 

 level
 

 as
 

 target
 

 called
 

 \'myNewDirectory\'"\n\nI
 

 need
 

 to
 

 take
 

 the
 

 following
 

 actions:\n-
 

 List
 

 all
 

 files
 

 in
 

 the
 

 directory\n-
 

 Create
 

 a
 

 new
 

 directory\n-
 

 Copy
 

 the
 

 files
 

 from
 

 the
 

 first
 

 directory
 

 into
 

 the
 

 second
 

 directory\n```bash\nls\nmkdir
 

 myNewDirectory\ncp
 

 -r
 

 target/\*
 

 myNewDirectory\n```\n\nThat
 

 is
 

 the
 

 format.
 

 Begin!\n\nQuestion:
 

 {question}',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.llm_bash.base.LLMBashChain](#langchain.chains.LLMBashChain "langchain.chains.llm_bash.base.LLMBashChain")


[[source]](../../_modules/langchain/chains/llm_bash/base#LLMBashChain.from_llm)
[#](#langchain.chains.LLMBashChain.from_llm "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 LLMChain
 

[[source]](../../_modules/langchain/chains/llm#LLMChain)
[#](#langchain.chains.LLMChain "Permalink to this definition") 



 Chain to run queries against LLMs.
 



 Example
 





```
from langchain import LLMChain, OpenAI, PromptTemplate
prompt_template = "Tell me a {adjective} joke"
prompt = PromptTemplate(
    input_variables=["adjective"], template=prompt_template
)
llm = LLMChain(llm=OpenAI(), prompt=prompt)

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 llm
 

*:
 




 BaseLanguageModel*
*[Required]*
[#](#langchain.chains.LLMChain.llm "Permalink to this definition") 






*field*


 prompt
 

*:
 



[BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.BasePromptTemplate")*
*[Required]*
[#](#langchain.chains.LLMChain.prompt "Permalink to this definition") 



 Prompt object to use.
 






*async*


 aapply
 


 (
 
*input_list
 



 :
 





 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]*
 ,
 *callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


 ]
 



 ]
 






 =
 





 None*

 )
 


 →
 


 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/chains/llm#LLMChain.aapply)
[#](#langchain.chains.LLMChain.aapply "Permalink to this definition") 



 Utilize the LLM generate method for speed gains.
 






*async*


 aapply_and_parse
 


 (
 
*input_list
 



 :
 





 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]*
 ,
 *callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


 ]
 



 ]
 






 =
 





 None*

 )
 


 →
 


 Sequence
 


 [
 


 Union
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ,
 




 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]
 



 ]
 



[[source]](../../_modules/langchain/chains/llm#LLMChain.aapply_and_parse)
[#](#langchain.chains.LLMChain.aapply_and_parse "Permalink to this definition") 



 Call apply and then parse the results.
 






*async*


 agenerate
 


 (
 
*input_list
 



 :
 





 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]*
 ,
 *run_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.manager.AsyncCallbackManagerForChainRun
 


 ]
 






 =
 





 None*

 )
 


 →
 


 langchain.schema.LLMResult
 


[[source]](../../_modules/langchain/chains/llm#LLMChain.agenerate)
[#](#langchain.chains.LLMChain.agenerate "Permalink to this definition") 



 Generate LLM result from inputs.
 








 apply
 


 (
 
*input_list
 



 :
 





 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]*
 ,
 *callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


 ]
 



 ]
 






 =
 





 None*

 )
 


 →
 


 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/chains/llm#LLMChain.apply)
[#](#langchain.chains.LLMChain.apply "Permalink to this definition") 



 Utilize the LLM generate method for speed gains.
 








 apply_and_parse
 


 (
 
*input_list
 



 :
 





 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]*
 ,
 *callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


 ]
 



 ]
 






 =
 





 None*

 )
 


 →
 


 Sequence
 


 [
 


 Union
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ,
 




 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]
 



 ]
 



[[source]](../../_modules/langchain/chains/llm#LLMChain.apply_and_parse)
[#](#langchain.chains.LLMChain.apply_and_parse "Permalink to this definition") 



 Call apply and then parse the results.
 






*async*


 apredict
 


 (
 
*callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


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
 


 →
 


 str
 


[[source]](../../_modules/langchain/chains/llm#LLMChain.apredict)
[#](#langchain.chains.LLMChain.apredict "Permalink to this definition") 



 Format prompt with kwargs and pass to LLM.
 




 Parameters
 

* **callbacks** 
 – Callbacks to pass to LLMChain
* **\*\*kwargs** 
 – Keys to pass to prompt template.




 Returns
 


 Completion from LLM.
 





 Example
 





```
completion = llm.predict(adjective="funny")

```







*async*


 apredict_and_parse
 


 (
 
*callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


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
 


 →
 


 Union
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ,
 




 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/chains/llm#LLMChain.apredict_and_parse)
[#](#langchain.chains.LLMChain.apredict_and_parse "Permalink to this definition") 



 Call apredict and then parse the results.
 






*async*


 aprep_prompts
 


 (
 
*input_list
 



 :
 





 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]*
 ,
 *run_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.manager.AsyncCallbackManagerForChainRun
 


 ]
 






 =
 





 None*

 )
 


 →
 


 Tuple
 


 [
 


 List
 


 [
 


 langchain.schema.PromptValue
 


 ]
 



 ,
 




 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 



 ]
 



[[source]](../../_modules/langchain/chains/llm#LLMChain.aprep_prompts)
[#](#langchain.chains.LLMChain.aprep_prompts "Permalink to this definition") 



 Prepare prompts from inputs.
 








 create_outputs
 


 (
 
*response
 



 :
 





 langchain.schema.LLMResult*

 )
 


 →
 


 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/chains/llm#LLMChain.create_outputs)
[#](#langchain.chains.LLMChain.create_outputs "Permalink to this definition") 



 Create outputs from response.
 






*classmethod*


 from_string
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *template
 



 :
 





 str*

 )
 


 →
 


 langchain.chains.base.Chain
 


[[source]](../../_modules/langchain/chains/llm#LLMChain.from_string)
[#](#langchain.chains.LLMChain.from_string "Permalink to this definition") 



 Create LLMChain from LLM and template.
 








 generate
 


 (
 
*input_list
 



 :
 





 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]*
 ,
 *run_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.manager.CallbackManagerForChainRun
 


 ]
 






 =
 





 None*

 )
 


 →
 


 langchain.schema.LLMResult
 


[[source]](../../_modules/langchain/chains/llm#LLMChain.generate)
[#](#langchain.chains.LLMChain.generate "Permalink to this definition") 



 Generate LLM result from inputs.
 








 predict
 


 (
 
*callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


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
 


 →
 


 str
 


[[source]](../../_modules/langchain/chains/llm#LLMChain.predict)
[#](#langchain.chains.LLMChain.predict "Permalink to this definition") 



 Format prompt with kwargs and pass to LLM.
 




 Parameters
 

* **callbacks** 
 – Callbacks to pass to LLMChain
* **\*\*kwargs** 
 – Keys to pass to prompt template.




 Returns
 


 Completion from LLM.
 





 Example
 





```
completion = llm.predict(adjective="funny")

```









 predict_and_parse
 


 (
 
*callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


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
 


 →
 


 Union
 


 [
 


 str
 


 ,
 




 List
 


 [
 


 str
 


 ]
 



 ,
 




 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]
 



[[source]](../../_modules/langchain/chains/llm#LLMChain.predict_and_parse)
[#](#langchain.chains.LLMChain.predict_and_parse "Permalink to this definition") 



 Call predict and then parse the results.
 








 prep_prompts
 


 (
 
*input_list
 



 :
 





 List
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]*
 ,
 *run_manager
 



 :
 





 Optional
 


 [
 


 langchain.callbacks.manager.CallbackManagerForChainRun
 


 ]
 






 =
 





 None*

 )
 


 →
 


 Tuple
 


 [
 


 List
 


 [
 


 langchain.schema.PromptValue
 


 ]
 



 ,
 




 Optional
 


 [
 


 List
 


 [
 


 str
 


 ]
 



 ]
 



 ]
 



[[source]](../../_modules/langchain/chains/llm#LLMChain.prep_prompts)
[#](#langchain.chains.LLMChain.prep_prompts "Permalink to this definition") 



 Prepare prompts from inputs.
 








*pydantic
 

 model*


 langchain.chains.
 



 LLMCheckerChain
 

[[source]](../../_modules/langchain/chains/llm_checker/base#LLMCheckerChain)
[#](#langchain.chains.LLMCheckerChain "Permalink to this definition") 



 Chain for question-answering with self-verification.
 



 Example
 





```
from langchain import OpenAI, LLMCheckerChain
llm = OpenAI(temperature=0.7)
checker_chain = LLMCheckerChain.from_llm(llm)

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 check_assertions_prompt
 

*:
 



[PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.PromptTemplate")*
*=
 




 PromptTemplate(input_variables=['assertions'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Here
 

 is
 

 a
 

 bullet
 

 point
 

 list
 

 of
 

 assertions:\n{assertions}\nFor
 

 each
 

 assertion,
 

 determine
 

 whether
 

 it
 

 is
 

 true
 

 or
 

 false.
 

 If
 

 it
 

 is
 

 false,
 

 explain
 

 why.\n\n',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.LLMCheckerChain.check_assertions_prompt "Permalink to this definition") 



 [Deprecated]
 






*field*


 create_draft_answer_prompt
 

*:
 



[PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.PromptTemplate")*
*=
 




 PromptTemplate(input_variables=['question'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='{question}\n\n',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.LLMCheckerChain.create_draft_answer_prompt "Permalink to this definition") 



 [Deprecated]
 






*field*


 list_assertions_prompt
 

*:
 



[PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.PromptTemplate")*
*=
 




 PromptTemplate(input_variables=['statement'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Here
 

 is
 

 a
 

 statement:\n{statement}\nMake
 

 a
 

 bullet
 

 point
 

 list
 

 of
 

 the
 

 assumptions
 

 you
 

 made
 

 when
 

 producing
 

 the
 

 above
 

 statement.\n\n',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.LLMCheckerChain.list_assertions_prompt "Permalink to this definition") 



 [Deprecated]
 






*field*


 llm
 

*:
 




 Optional
 


 [
 


 BaseLLM
 


 ]*
*=
 




 None*
[#](#langchain.chains.LLMCheckerChain.llm "Permalink to this definition") 



 [Deprecated] LLM wrapper to use.
 






*field*


 question_to_checked_assertions_chain
 

*:
 



[SequentialChain](#langchain.chains.SequentialChain "langchain.chains.SequentialChain")*
*[Required]*
[#](#langchain.chains.LLMCheckerChain.question_to_checked_assertions_chain "Permalink to this definition") 






*field*


 revised_answer_prompt
 

*:
 



[PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.PromptTemplate")*
*=
 




 PromptTemplate(input_variables=['checked_assertions',
 

 'question'],
 

 output_parser=None,
 

 partial_variables={},
 

 template="{checked_assertions}\n\nQuestion:
 

 In
 

 light
 

 of
 

 the
 

 above
 

 assertions
 

 and
 

 checks,
 

 how
 

 would
 

 you
 

 answer
 

 the
 

 question
 

 '{question}'?\n\nAnswer:",
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.LLMCheckerChain.revised_answer_prompt "Permalink to this definition") 



 [Deprecated] Prompt to use when questioning the documents.
 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *create_draft_answer_prompt
 



 :
 




[langchain.prompts.prompt.PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")





 =
 





 PromptTemplate(input_variables=['question'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='{question}\n\n',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *list_assertions_prompt
 



 :
 




[langchain.prompts.prompt.PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")





 =
 





 PromptTemplate(input_variables=['statement'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Here
 

 is
 

 a
 

 statement:\n{statement}\nMake
 

 a
 

 bullet
 

 point
 

 list
 

 of
 

 the
 

 assumptions
 

 you
 

 made
 

 when
 

 producing
 

 the
 

 above
 

 statement.\n\n',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *check_assertions_prompt
 



 :
 




[langchain.prompts.prompt.PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")





 =
 





 PromptTemplate(input_variables=['assertions'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Here
 

 is
 

 a
 

 bullet
 

 point
 

 list
 

 of
 

 assertions:\n{assertions}\nFor
 

 each
 

 assertion,
 

 determine
 

 whether
 

 it
 

 is
 

 true
 

 or
 

 false.
 

 If
 

 it
 

 is
 

 false,
 

 explain
 

 why.\n\n',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *revised_answer_prompt
 



 :
 




[langchain.prompts.prompt.PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")





 =
 





 PromptTemplate(input_variables=['checked_assertions',
 

 'question'],
 

 output_parser=None,
 

 partial_variables={},
 

 template="{checked_assertions}\n\nQuestion:
 

 In
 

 light
 

 of
 

 the
 

 above
 

 assertions
 

 and
 

 checks,
 

 how
 

 would
 

 you
 

 answer
 

 the
 

 question
 

 '{question}'?\n\nAnswer:",
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.llm_checker.base.LLMCheckerChain](#langchain.chains.LLMCheckerChain "langchain.chains.llm_checker.base.LLMCheckerChain")


[[source]](../../_modules/langchain/chains/llm_checker/base#LLMCheckerChain.from_llm)
[#](#langchain.chains.LLMCheckerChain.from_llm "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 LLMMathChain
 

[[source]](../../_modules/langchain/chains/llm_math/base#LLMMathChain)
[#](#langchain.chains.LLMMathChain "Permalink to this definition") 



 Chain that interprets a prompt and executes python code to do math.
 



 Example
 





```
from langchain import LLMMathChain, OpenAI
llm_math = LLMMathChain.from_llm(OpenAI())

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 llm
 

*:
 




 Optional
 


 [
 


 BaseLanguageModel
 


 ]*
*=
 




 None*
[#](#langchain.chains.LLMMathChain.llm "Permalink to this definition") 



 [Deprecated] LLM wrapper to use.
 






*field*


 llm_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.LLMMathChain.llm_chain "Permalink to this definition") 






*field*


 prompt
 

*:
 



[BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.BasePromptTemplate")*
*=
 




 PromptTemplate(input_variables=['question'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Translate
 

 a
 

 math
 

 problem
 

 into
 

 a
 

 expression
 

 that
 

 can
 

 be
 

 executed
 

 using
 

 Python\'s
 

 numexpr
 

 library.
 

 Use
 

 the
 

 output
 

 of
 

 running
 

 this
 

 code
 

 to
 

 answer
 

 the
 

 question.\n\nQuestion:
 

 ${{Question
 

 with
 

 math
 

 problem.}}\n```text\n${{single
 

 line
 

 mathematical
 

 expression
 

 that
 

 solves
 

 the
 

 problem}}\n```\n...numexpr.evaluate(text)...\n```output\n${{Output
 

 of
 

 running
 

 the
 

 code}}\n```\nAnswer:
 

 ${{Answer}}\n\nBegin.\n\nQuestion:
 

 What
 

 is
 

 37593
 

 \*
 

 67?\n\n```text\n37593
 

 \*
 

 67\n```\n...numexpr.evaluate("37593
 

 \*
 

 67")...\n```output\n2518731\n```\nAnswer:
 

 2518731\n\nQuestion:
 

 {question}\n',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.LLMMathChain.prompt "Permalink to this definition") 



 [Deprecated] Prompt to use to translate to python if necessary.
 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['question'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Translate
 

 a
 

 math
 

 problem
 

 into
 

 a
 

 expression
 

 that
 

 can
 

 be
 

 executed
 

 using
 

 Python\'s
 

 numexpr
 

 library.
 

 Use
 

 the
 

 output
 

 of
 

 running
 

 this
 

 code
 

 to
 

 answer
 

 the
 

 question.\n\nQuestion:
 

 ${{Question
 

 with
 

 math
 

 problem.}}\n```text\n${{single
 

 line
 

 mathematical
 

 expression
 

 that
 

 solves
 

 the
 

 problem}}\n```\n...numexpr.evaluate(text)...\n```output\n${{Output
 

 of
 

 running
 

 the
 

 code}}\n```\nAnswer:
 

 ${{Answer}}\n\nBegin.\n\nQuestion:
 

 What
 

 is
 

 37593
 

 \*
 

 67?\n\n```text\n37593
 

 \*
 

 67\n```\n...numexpr.evaluate("37593
 

 \*
 

 67")...\n```output\n2518731\n```\nAnswer:
 

 2518731\n\nQuestion:
 

 {question}\n',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.llm_math.base.LLMMathChain](#langchain.chains.LLMMathChain "langchain.chains.llm_math.base.LLMMathChain")


[[source]](../../_modules/langchain/chains/llm_math/base#LLMMathChain.from_llm)
[#](#langchain.chains.LLMMathChain.from_llm "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 LLMRequestsChain
 

[[source]](../../_modules/langchain/chains/llm_requests#LLMRequestsChain)
[#](#langchain.chains.LLMRequestsChain "Permalink to this definition") 



 Chain that hits a URL and then uses an LLM to parse results.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 llm_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.LLMRequestsChain.llm_chain "Permalink to this definition") 






*field*


 requests_wrapper
 

*:
 



[TextRequestsWrapper](utilities#langchain.utilities.TextRequestsWrapper "langchain.utilities.TextRequestsWrapper")*
*[Optional]*
[#](#langchain.chains.LLMRequestsChain.requests_wrapper "Permalink to this definition") 






*field*


 text_length
 

*:
 




 int*
*=
 




 8000*
[#](#langchain.chains.LLMRequestsChain.text_length "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 LLMSummarizationCheckerChain
 

[[source]](../../_modules/langchain/chains/llm_summarization_checker/base#LLMSummarizationCheckerChain)
[#](#langchain.chains.LLMSummarizationCheckerChain "Permalink to this definition") 



 Chain for question-answering with self-verification.
 



 Example
 





```
from langchain import OpenAI, LLMSummarizationCheckerChain
llm = OpenAI(temperature=0.0)
checker_chain = LLMSummarizationCheckerChain.from_llm(llm)

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 are_all_true_prompt
 

*:
 



[PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.PromptTemplate")*
*=
 




 PromptTemplate(input_variables=['checked_assertions'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Below
 

 are
 

 some
 

 assertions
 

 that
 

 have
 

 been
 

 fact
 

 checked
 

 and
 

 are
 

 labeled
 

 as
 

 true
 

 or
 

 false.\n\nIf
 

 all
 

 of
 

 the
 

 assertions
 

 are
 

 true,
 

 return
 

 "True".
 

 If
 

 any
 

 of
 

 the
 

 assertions
 

 are
 

 false,
 

 return
 

 "False".\n\nHere
 

 are
 

 some
 

 examples:\n===\n\nChecked
 

 Assertions:
 

 """\n-
 

 The
 

 sky
 

 is
 

 red:
 

 False\n-
 

 Water
 

 is
 

 made
 

 of
 

 lava:
 

 False\n-
 

 The
 

 sun
 

 is
 

 a
 

 star:
 

 True\n"""\nResult:
 

 False\n\n===\n\nChecked
 

 Assertions:
 

 """\n-
 

 The
 

 sky
 

 is
 

 blue:
 

 True\n-
 

 Water
 

 is
 

 wet:
 

 True\n-
 

 The
 

 sun
 

 is
 

 a
 

 star:
 

 True\n"""\nResult:
 

 True\n\n===\n\nChecked
 

 Assertions:
 

 """\n-
 

 The
 

 sky
 

 is
 

 blue
 

 -
 

 True\n-
 

 Water
 

 is
 

 made
 

 of
 

 lava-
 

 False\n-
 

 The
 

 sun
 

 is
 

 a
 

 star
 

 -
 

 True\n"""\nResult:
 

 False\n\n===\n\nChecked
 

 Assertions:"""\n{checked_assertions}\n"""\nResult:',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.LLMSummarizationCheckerChain.are_all_true_prompt "Permalink to this definition") 



 [Deprecated]
 






*field*


 check_assertions_prompt
 

*:
 



[PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.PromptTemplate")*
*=
 




 PromptTemplate(input_variables=['assertions'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='You
 

 are
 

 an
 

 expert
 

 fact
 

 checker.
 

 You
 

 have
 

 been
 

 hired
 

 by
 

 a
 

 major
 

 news
 

 organization
 

 to
 

 fact
 

 check
 

 a
 

 very
 

 important
 

 story.\n\nHere
 

 is
 

 a
 

 bullet
 

 point
 

 list
 

 of
 

 facts:\n"""\n{assertions}\n"""\n\nFor
 

 each
 

 fact,
 

 determine
 

 whether
 

 it
 

 is
 

 true
 

 or
 

 false
 

 about
 

 the
 

 subject.
 

 If
 

 you
 

 are
 

 unable
 

 to
 

 determine
 

 whether
 

 the
 

 fact
 

 is
 

 true
 

 or
 

 false,
 

 output
 

 "Undetermined".\nIf
 

 the
 

 fact
 

 is
 

 false,
 

 explain
 

 why.\n\n',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.LLMSummarizationCheckerChain.check_assertions_prompt "Permalink to this definition") 



 [Deprecated]
 






*field*


 create_assertions_prompt
 

*:
 



[PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.PromptTemplate")*
*=
 




 PromptTemplate(input_variables=['summary'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Given
 

 some
 

 text,
 

 extract
 

 a
 

 list
 

 of
 

 facts
 

 from
 

 the
 

 text.\n\nFormat
 

 your
 

 output
 

 as
 

 a
 

 bulleted
 

 list.\n\nText:\n"""\n{summary}\n"""\n\nFacts:',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.LLMSummarizationCheckerChain.create_assertions_prompt "Permalink to this definition") 



 [Deprecated]
 






*field*


 llm
 

*:
 




 Optional
 


 [
 


 BaseLLM
 


 ]*
*=
 




 None*
[#](#langchain.chains.LLMSummarizationCheckerChain.llm "Permalink to this definition") 



 [Deprecated] LLM wrapper to use.
 






*field*


 max_checks
 

*:
 




 int*
*=
 




 2*
[#](#langchain.chains.LLMSummarizationCheckerChain.max_checks "Permalink to this definition") 



 Maximum number of times to check the assertions. Default to double-checking.
 






*field*


 revised_summary_prompt
 

*:
 



[PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.PromptTemplate")*
*=
 




 PromptTemplate(input_variables=['checked_assertions',
 

 'summary'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Below
 

 are
 

 some
 

 assertions
 

 that
 

 have
 

 been
 

 fact
 

 checked
 

 and
 

 are
 

 labeled
 

 as
 

 true
 

 of
 

 false.
 

 If
 

 the
 

 answer
 

 is
 

 false,
 

 a
 

 suggestion
 

 is
 

 given
 

 for
 

 a
 

 correction.\n\nChecked
 

 Assertions:\n"""\n{checked_assertions}\n"""\n\nOriginal
 

 Summary:\n"""\n{summary}\n"""\n\nUsing
 

 these
 

 checked
 

 assertions,
 

 rewrite
 

 the
 

 original
 

 summary
 

 to
 

 be
 

 completely
 

 true.\n\nThe
 

 output
 

 should
 

 have
 

 the
 

 same
 

 structure
 

 and
 

 formatting
 

 as
 

 the
 

 original
 

 summary.\n\nSummary:',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.LLMSummarizationCheckerChain.revised_summary_prompt "Permalink to this definition") 



 [Deprecated]
 






*field*


 sequential_chain
 

*:
 



[SequentialChain](#langchain.chains.SequentialChain "langchain.chains.SequentialChain")*
*[Required]*
[#](#langchain.chains.LLMSummarizationCheckerChain.sequential_chain "Permalink to this definition") 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *create_assertions_prompt
 



 :
 




[langchain.prompts.prompt.PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")





 =
 





 PromptTemplate(input_variables=['summary'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Given
 

 some
 

 text,
 

 extract
 

 a
 

 list
 

 of
 

 facts
 

 from
 

 the
 

 text.\n\nFormat
 

 your
 

 output
 

 as
 

 a
 

 bulleted
 

 list.\n\nText:\n"""\n{summary}\n"""\n\nFacts:',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *check_assertions_prompt
 



 :
 




[langchain.prompts.prompt.PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")





 =
 





 PromptTemplate(input_variables=['assertions'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='You
 

 are
 

 an
 

 expert
 

 fact
 

 checker.
 

 You
 

 have
 

 been
 

 hired
 

 by
 

 a
 

 major
 

 news
 

 organization
 

 to
 

 fact
 

 check
 

 a
 

 very
 

 important
 

 story.\n\nHere
 

 is
 

 a
 

 bullet
 

 point
 

 list
 

 of
 

 facts:\n"""\n{assertions}\n"""\n\nFor
 

 each
 

 fact,
 

 determine
 

 whether
 

 it
 

 is
 

 true
 

 or
 

 false
 

 about
 

 the
 

 subject.
 

 If
 

 you
 

 are
 

 unable
 

 to
 

 determine
 

 whether
 

 the
 

 fact
 

 is
 

 true
 

 or
 

 false,
 

 output
 

 "Undetermined".\nIf
 

 the
 

 fact
 

 is
 

 false,
 

 explain
 

 why.\n\n',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *revised_summary_prompt
 



 :
 




[langchain.prompts.prompt.PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")





 =
 





 PromptTemplate(input_variables=['checked_assertions',
 

 'summary'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Below
 

 are
 

 some
 

 assertions
 

 that
 

 have
 

 been
 

 fact
 

 checked
 

 and
 

 are
 

 labeled
 

 as
 

 true
 

 of
 

 false.
 

 If
 

 the
 

 answer
 

 is
 

 false,
 

 a
 

 suggestion
 

 is
 

 given
 

 for
 

 a
 

 correction.\n\nChecked
 

 Assertions:\n"""\n{checked_assertions}\n"""\n\nOriginal
 

 Summary:\n"""\n{summary}\n"""\n\nUsing
 

 these
 

 checked
 

 assertions,
 

 rewrite
 

 the
 

 original
 

 summary
 

 to
 

 be
 

 completely
 

 true.\n\nThe
 

 output
 

 should
 

 have
 

 the
 

 same
 

 structure
 

 and
 

 formatting
 

 as
 

 the
 

 original
 

 summary.\n\nSummary:',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *are_all_true_prompt
 



 :
 




[langchain.prompts.prompt.PromptTemplate](prompts#langchain.prompts.PromptTemplate "langchain.prompts.prompt.PromptTemplate")





 =
 





 PromptTemplate(input_variables=['checked_assertions'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Below
 

 are
 

 some
 

 assertions
 

 that
 

 have
 

 been
 

 fact
 

 checked
 

 and
 

 are
 

 labeled
 

 as
 

 true
 

 or
 

 false.\n\nIf
 

 all
 

 of
 

 the
 

 assertions
 

 are
 

 true,
 

 return
 

 "True".
 

 If
 

 any
 

 of
 

 the
 

 assertions
 

 are
 

 false,
 

 return
 

 "False".\n\nHere
 

 are
 

 some
 

 examples:\n===\n\nChecked
 

 Assertions:
 

 """\n-
 

 The
 

 sky
 

 is
 

 red:
 

 False\n-
 

 Water
 

 is
 

 made
 

 of
 

 lava:
 

 False\n-
 

 The
 

 sun
 

 is
 

 a
 

 star:
 

 True\n"""\nResult:
 

 False\n\n===\n\nChecked
 

 Assertions:
 

 """\n-
 

 The
 

 sky
 

 is
 

 blue:
 

 True\n-
 

 Water
 

 is
 

 wet:
 

 True\n-
 

 The
 

 sun
 

 is
 

 a
 

 star:
 

 True\n"""\nResult:
 

 True\n\n===\n\nChecked
 

 Assertions:
 

 """\n-
 

 The
 

 sky
 

 is
 

 blue
 

 -
 

 True\n-
 

 Water
 

 is
 

 made
 

 of
 

 lava-
 

 False\n-
 

 The
 

 sun
 

 is
 

 a
 

 star
 

 -
 

 True\n"""\nResult:
 

 False\n\n===\n\nChecked
 

 Assertions:"""\n{checked_assertions}\n"""\nResult:',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain](#langchain.chains.LLMSummarizationCheckerChain "langchain.chains.llm_summarization_checker.base.LLMSummarizationCheckerChain")


[[source]](../../_modules/langchain/chains/llm_summarization_checker/base#LLMSummarizationCheckerChain.from_llm)
[#](#langchain.chains.LLMSummarizationCheckerChain.from_llm "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 MapReduceChain
 

[[source]](../../_modules/langchain/chains/mapreduce#MapReduceChain)
[#](#langchain.chains.MapReduceChain "Permalink to this definition") 



 Map-reduce chain.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 combine_documents_chain
 

*:
 




 BaseCombineDocumentsChain*
*[Required]*
[#](#langchain.chains.MapReduceChain.combine_documents_chain "Permalink to this definition") 



 Chain to use to combine documents.
 






*field*


 text_splitter
 

*:
 



[TextSplitter](text_splitter#langchain.text_splitter.TextSplitter "langchain.text_splitter.TextSplitter")*
*[Required]*
[#](#langchain.chains.MapReduceChain.text_splitter "Permalink to this definition") 



 Text splitter to use.
 






*classmethod*


 from_params
 


 (
 
*llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")*
 ,
 *text_splitter
 



 :
 




[langchain.text_splitter.TextSplitter](text_splitter#langchain.text_splitter.TextSplitter "langchain.text_splitter.TextSplitter")*
 ,
 *callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


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
 


 →
 

[langchain.chains.mapreduce.MapReduceChain](#langchain.chains.MapReduceChain "langchain.chains.mapreduce.MapReduceChain")


[[source]](../../_modules/langchain/chains/mapreduce#MapReduceChain.from_params)
[#](#langchain.chains.MapReduceChain.from_params "Permalink to this definition") 



 Construct a map-reduce chain that uses the chain for map and reduce.
 








*pydantic
 

 model*


 langchain.chains.
 



 OpenAIModerationChain
 

[[source]](../../_modules/langchain/chains/moderation#OpenAIModerationChain)
[#](#langchain.chains.OpenAIModerationChain "Permalink to this definition") 



 Pass input through a moderation endpoint.
 



 To use, you should have the
 `openai`
 python package installed, and the
environment variable
 `OPENAI_API_KEY`
 set with your API key.
 



 Any parameters that are valid to be passed to the openai.create call can be passed
in, even if not explicitly saved on this class.
 



 Example
 





```
from langchain.chains import OpenAIModerationChain
moderation = OpenAIModerationChain()

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_environment`
 »
 `all
 

 fields`






*field*


 error
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.chains.OpenAIModerationChain.error "Permalink to this definition") 



 Whether or not to error if bad content was found.
 






*field*


 model_name
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.chains.OpenAIModerationChain.model_name "Permalink to this definition") 



 Moderation model name to use.
 






*field*


 openai_api_key
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.chains.OpenAIModerationChain.openai_api_key "Permalink to this definition") 






*field*


 openai_organization
 

*:
 




 Optional
 


 [
 


 str
 


 ]*
*=
 




 None*
[#](#langchain.chains.OpenAIModerationChain.openai_organization "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 OpenAPIEndpointChain
 

[[source]](../../_modules/langchain/chains/api/openapi/chain#OpenAPIEndpointChain)
[#](#langchain.chains.OpenAPIEndpointChain "Permalink to this definition") 



 Chain interacts with an OpenAPI endpoint using natural language.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 api_operation
 

*:
 



[APIOperation](tools#langchain.tools.APIOperation "langchain.tools.APIOperation")*
*[Required]*
[#](#langchain.chains.OpenAPIEndpointChain.api_operation "Permalink to this definition") 






*field*


 api_request_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.OpenAPIEndpointChain.api_request_chain "Permalink to this definition") 






*field*


 api_response_chain
 

*:
 




 Optional
 


 [
 

[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")


 ]*
*=
 




 None*
[#](#langchain.chains.OpenAPIEndpointChain.api_response_chain "Permalink to this definition") 






*field*


 param_mapping
 

*:
 




 _ParamMapping*
*[Required]*
[#](#langchain.chains.OpenAPIEndpointChain.param_mapping "Permalink to this definition") 






*field*


 requests
 

*:
 




 Requests*
*[Optional]*
[#](#langchain.chains.OpenAPIEndpointChain.requests "Permalink to this definition") 






*field*


 return_intermediate_steps
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.chains.OpenAPIEndpointChain.return_intermediate_steps "Permalink to this definition") 








 deserialize_json_input
 


 (
 
*serialized_args
 



 :
 





 str*

 )
 


 →
 


 dict
 


[[source]](../../_modules/langchain/chains/api/openapi/chain#OpenAPIEndpointChain.deserialize_json_input)
[#](#langchain.chains.OpenAPIEndpointChain.deserialize_json_input "Permalink to this definition") 



 Use the serialized typescript dictionary.
 



 Resolve the path, query params dict, and optional requestBody dict.
 






*classmethod*


 from_api_operation
 


 (
 
*operation
 



 :
 




[langchain.tools.openapi.utils.api_models.APIOperation](tools#langchain.tools.APIOperation "langchain.tools.openapi.utils.api_models.APIOperation")*
 ,
 *llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *requests
 



 :
 





 Optional
 


 [
 


 langchain.requests.Requests
 


 ]
 






 =
 





 None*
 ,
 *verbose
 



 :
 





 bool
 





 =
 





 False*
 ,
 *return_intermediate_steps
 



 :
 





 bool
 





 =
 





 False*
 ,
 *raw_response
 



 :
 





 bool
 





 =
 





 False*
 ,
 *callbacks
 



 :
 





 Optional
 


 [
 


 Union
 


 [
 


 List
 


 [
 


 langchain.callbacks.base.BaseCallbackHandler
 


 ]
 



 ,
 




 langchain.callbacks.base.BaseCallbackManager
 


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
 


 →
 

[OpenAPIEndpointChain](#langchain.chains.OpenAPIEndpointChain "langchain.chains.OpenAPIEndpointChain")


[[source]](../../_modules/langchain/chains/api/openapi/chain#OpenAPIEndpointChain.from_api_operation)
[#](#langchain.chains.OpenAPIEndpointChain.from_api_operation "Permalink to this definition") 



 Create an OpenAPIEndpointChain from an operation and a spec.
 






*classmethod*


 from_url_and_method
 


 (
 
*spec_url
 



 :
 





 str*
 ,
 *path
 



 :
 





 str*
 ,
 *method
 



 :
 





 str*
 ,
 *llm
 



 :
 





 langchain.llms.base.BaseLLM*
 ,
 *requests
 



 :
 





 Optional
 


 [
 


 langchain.requests.Requests
 


 ]
 






 =
 





 None*
 ,
 *return_intermediate_steps
 



 :
 





 bool
 





 =
 





 False*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[OpenAPIEndpointChain](#langchain.chains.OpenAPIEndpointChain "langchain.chains.OpenAPIEndpointChain")


[[source]](../../_modules/langchain/chains/api/openapi/chain#OpenAPIEndpointChain.from_url_and_method)
[#](#langchain.chains.OpenAPIEndpointChain.from_url_and_method "Permalink to this definition") 



 Create an OpenAPIEndpoint from a spec at the specified url.
 








*pydantic
 

 model*


 langchain.chains.
 



 PALChain
 

[[source]](../../_modules/langchain/chains/pal/base#PALChain)
[#](#langchain.chains.PALChain "Permalink to this definition") 



 Implements Program-Aided Language Models.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 get_answer_expr
 

*:
 




 str*
*=
 




 'print(solution())'*
[#](#langchain.chains.PALChain.get_answer_expr "Permalink to this definition") 






*field*


 llm
 

*:
 




 Optional
 


 [
 


 BaseLanguageModel
 


 ]*
*=
 




 None*
[#](#langchain.chains.PALChain.llm "Permalink to this definition") 



 [Deprecated]
 






*field*


 llm_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.PALChain.llm_chain "Permalink to this definition") 






*field*


 prompt
 

*:
 



[BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.BasePromptTemplate")*
*=
 




 PromptTemplate(input_variables=['question'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Q:
 

 Olivia
 

 has
 

 $23.
 

 She
 

 bought
 

 five
 

 bagels
 

 for
 

 $3
 

 each.
 

 How
 

 much
 

 money
 

 does
 

 she
 

 have
 

 left?\n\n#
 

 solution
 

 in
 

 Python:\n\n\ndef
 

 solution():\n
 

 """Olivia
 

 has
 

 $23.
 

 She
 

 bought
 

 five
 

 bagels
 

 for
 

 $3
 

 each.
 

 How
 

 much
 

 money
 

 does
 

 she
 

 have
 

 left?"""\n
 

 money_initial
 

 =
 

 23\n
 

 bagels
 

 =
 

 5\n
 

 bagel_cost
 

 =
 

 3\n
 

 money_spent
 

 =
 

 bagels
 

 \*
 

 bagel_cost\n
 

 money_left
 

 =
 

 money_initial
 

 -
 

 money_spent\n
 

 result
 

 =
 

 money_left\n
 

 return
 

 result\n\n\n\n\n\nQ:
 

 Michael
 

 had
 

 58
 

 golf
 

 balls.
 

 On
 

 tuesday,
 

 he
 

 lost
 

 23
 

 golf
 

 balls.
 

 On
 

 wednesday,
 

 he
 

 lost
 

 2
 

 more.
 

 How
 

 many
 

 golf
 

 balls
 

 did
 

 he
 

 have
 

 at
 

 the
 

 end
 

 of
 

 wednesday?\n\n#
 

 solution
 

 in
 

 Python:\n\n\ndef
 

 solution():\n
 

 """Michael
 

 had
 

 58
 

 golf
 

 balls.
 

 On
 

 tuesday,
 

 he
 

 lost
 

 23
 

 golf
 

 balls.
 

 On
 

 wednesday,
 

 he
 

 lost
 

 2
 

 more.
 

 How
 

 many
 

 golf
 

 balls
 

 did
 

 he
 

 have
 

 at
 

 the
 

 end
 

 of
 

 wednesday?"""\n
 

 golf_balls_initial
 

 =
 

 58\n
 

 golf_balls_lost_tuesday
 

 =
 

 23\n
 

 golf_balls_lost_wednesday
 

 =
 

 2\n
 

 golf_balls_left
 

 =
 

 golf_balls_initial
 

 -
 

 golf_balls_lost_tuesday
 

 -
 

 golf_balls_lost_wednesday\n
 

 result
 

 =
 

 golf_balls_left\n
 

 return
 

 result\n\n\n\n\n\nQ:
 

 There
 

 were
 

 nine
 

 computers
 

 in
 

 the
 

 server
 

 room.
 

 Five
 

 more
 

 computers
 

 were
 

 installed
 

 each
 

 day,
 

 from
 

 monday
 

 to
 

 thursday.
 

 How
 

 many
 

 computers
 

 are
 

 now
 

 in
 

 the
 

 server
 

 room?\n\n#
 

 solution
 

 in
 

 Python:\n\n\ndef
 

 solution():\n
 

 """There
 

 were
 

 nine
 

 computers
 

 in
 

 the
 

 server
 

 room.
 

 Five
 

 more
 

 computers
 

 were
 

 installed
 

 each
 

 day,
 

 from
 

 monday
 

 to
 

 thursday.
 

 How
 

 many
 

 computers
 

 are
 

 now
 

 in
 

 the
 

 server
 

 room?"""\n
 

 computers_initial
 

 =
 

 9\n
 

 computers_per_day
 

 =
 

 5\n
 

 num_days
 

 =
 

 4
 

 #
 

 4
 

 days
 

 between
 

 monday
 

 and
 

 thursday\n
 

 computers_added
 

 =
 

 computers_per_day
 

 \*
 

 num_days\n
 

 computers_total
 

 =
 

 computers_initial
 

 +
 

 computers_added\n
 

 result
 

 =
 

 computers_total\n
 

 return
 

 result\n\n\n\n\n\nQ:
 

 Shawn
 

 has
 

 five
 

 toys.
 

 For
 

 Christmas,
 

 he
 

 got
 

 two
 

 toys
 

 each
 

 from
 

 his
 

 mom
 

 and
 

 dad.
 

 How
 

 many
 

 toys
 

 does
 

 he
 

 have
 

 now?\n\n#
 

 solution
 

 in
 

 Python:\n\n\ndef
 

 solution():\n
 

 """Shawn
 

 has
 

 five
 

 toys.
 

 For
 

 Christmas,
 

 he
 

 got
 

 two
 

 toys
 

 each
 

 from
 

 his
 

 mom
 

 and
 

 dad.
 

 How
 

 many
 

 toys
 

 does
 

 he
 

 have
 

 now?"""\n
 

 toys_initial
 

 =
 

 5\n
 

 mom_toys
 

 =
 

 2\n
 

 dad_toys
 

 =
 

 2\n
 

 total_received
 

 =
 

 mom_toys
 

 +
 

 dad_toys\n
 

 total_toys
 

 =
 

 toys_initial
 

 +
 

 total_received\n
 

 result
 

 =
 

 total_toys\n
 

 return
 

 result\n\n\n\n\n\nQ:
 

 Jason
 

 had
 

 20
 

 lollipops.
 

 He
 

 gave
 

 Denny
 

 some
 

 lollipops.
 

 Now
 

 Jason
 

 has
 

 12
 

 lollipops.
 

 How
 

 many
 

 lollipops
 

 did
 

 Jason
 

 give
 

 to
 

 Denny?\n\n#
 

 solution
 

 in
 

 Python:\n\n\ndef
 

 solution():\n
 

 """Jason
 

 had
 

 20
 

 lollipops.
 

 He
 

 gave
 

 Denny
 

 some
 

 lollipops.
 

 Now
 

 Jason
 

 has
 

 12
 

 lollipops.
 

 How
 

 many
 

 lollipops
 

 did
 

 Jason
 

 give
 

 to
 

 Denny?"""\n
 

 jason_lollipops_initial
 

 =
 

 20\n
 

 jason_lollipops_after
 

 =
 

 12\n
 

 denny_lollipops
 

 =
 

 jason_lollipops_initial
 

 -
 

 jason_lollipops_after\n
 

 result
 

 =
 

 denny_lollipops\n
 

 return
 

 result\n\n\n\n\n\nQ:
 

 Leah
 

 had
 

 32
 

 chocolates
 

 and
 

 her
 

 sister
 

 had
 

 42.
 

 If
 

 they
 

 ate
 

 35,
 

 how
 

 many
 

 pieces
 

 do
 

 they
 

 have
 

 left
 

 in
 

 total?\n\n#
 

 solution
 

 in
 

 Python:\n\n\ndef
 

 solution():\n
 

 """Leah
 

 had
 

 32
 

 chocolates
 

 and
 

 her
 

 sister
 

 had
 

 42.
 

 If
 

 they
 

 ate
 

 35,
 

 how
 

 many
 

 pieces
 

 do
 

 they
 

 have
 

 left
 

 in
 

 total?"""\n
 

 leah_chocolates
 

 =
 

 32\n
 

 sister_chocolates
 

 =
 

 42\n
 

 total_chocolates
 

 =
 

 leah_chocolates
 

 +
 

 sister_chocolates\n
 

 chocolates_eaten
 

 =
 

 35\n
 

 chocolates_left
 

 =
 

 total_chocolates
 

 -
 

 chocolates_eaten\n
 

 result
 

 =
 

 chocolates_left\n
 

 return
 

 result\n\n\n\n\n\nQ:
 

 If
 

 there
 

 are
 

 3
 

 cars
 

 in
 

 the
 

 parking
 

 lot
 

 and
 

 2
 

 more
 

 cars
 

 arrive,
 

 how
 

 many
 

 cars
 

 are
 

 in
 

 the
 

 parking
 

 lot?\n\n#
 

 solution
 

 in
 

 Python:\n\n\ndef
 

 solution():\n
 

 """If
 

 there
 

 are
 

 3
 

 cars
 

 in
 

 the
 

 parking
 

 lot
 

 and
 

 2
 

 more
 

 cars
 

 arrive,
 

 how
 

 many
 

 cars
 

 are
 

 in
 

 the
 

 parking
 

 lot?"""\n
 

 cars_initial
 

 =
 

 3\n
 

 cars_arrived
 

 =
 

 2\n
 

 total_cars
 

 =
 

 cars_initial
 

 +
 

 cars_arrived\n
 

 result
 

 =
 

 total_cars\n
 

 return
 

 result\n\n\n\n\n\nQ:
 

 There
 

 are
 

 15
 

 trees
 

 in
 

 the
 

 grove.
 

 Grove
 

 workers
 

 will
 

 plant
 

 trees
 

 in
 

 the
 

 grove
 

 today.
 

 After
 

 they
 

 are
 

 done,
 

 there
 

 will
 

 be
 

 21
 

 trees.
 

 How
 

 many
 

 trees
 

 did
 

 the
 

 grove
 

 workers
 

 plant
 

 today?\n\n#
 

 solution
 

 in
 

 Python:\n\n\ndef
 

 solution():\n
 

 """There
 

 are
 

 15
 

 trees
 

 in
 

 the
 

 grove.
 

 Grove
 

 workers
 

 will
 

 plant
 

 trees
 

 in
 

 the
 

 grove
 

 today.
 

 After
 

 they
 

 are
 

 done,
 

 there
 

 will
 

 be
 

 21
 

 trees.
 

 How
 

 many
 

 trees
 

 did
 

 the
 

 grove
 

 workers
 

 plant
 

 today?"""\n
 

 trees_initial
 

 =
 

 15\n
 

 trees_after
 

 =
 

 21\n
 

 trees_added
 

 =
 

 trees_after
 

 -
 

 trees_initial\n
 

 result
 

 =
 

 trees_added\n
 

 return
 

 result\n\n\n\n\n\nQ:
 

 {question}\n\n#
 

 solution
 

 in
 

 Python:\n\n\n',
 

 template_format='f-string',
 

 validate_template=True)*
[#](#langchain.chains.PALChain.prompt "Permalink to this definition") 



 [Deprecated]
 






*field*


 python_globals
 

*:
 




 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.chains.PALChain.python_globals "Permalink to this definition") 






*field*


 python_locals
 

*:
 




 Optional
 


 [
 


 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]
 



 ]*
*=
 




 None*
[#](#langchain.chains.PALChain.python_locals "Permalink to this definition") 






*field*


 return_intermediate_steps
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.chains.PALChain.return_intermediate_steps "Permalink to this definition") 






*field*


 stop
 

*:
 




 str*
*=
 




 '\n\n'*
[#](#langchain.chains.PALChain.stop "Permalink to this definition") 






*classmethod*


 from_colored_object_prompt
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.pal.base.PALChain](#langchain.chains.PALChain "langchain.chains.pal.base.PALChain")


[[source]](../../_modules/langchain/chains/pal/base#PALChain.from_colored_object_prompt)
[#](#langchain.chains.PALChain.from_colored_object_prompt "Permalink to this definition") 



 Load PAL from colored object prompt.
 






*classmethod*


 from_math_prompt
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.pal.base.PALChain](#langchain.chains.PALChain "langchain.chains.pal.base.PALChain")


[[source]](../../_modules/langchain/chains/pal/base#PALChain.from_math_prompt)
[#](#langchain.chains.PALChain.from_math_prompt "Permalink to this definition") 



 Load PAL from math prompt.
 








*pydantic
 

 model*


 langchain.chains.
 



 QAGenerationChain
 

[[source]](../../_modules/langchain/chains/qa_generation/base#QAGenerationChain)
[#](#langchain.chains.QAGenerationChain "Permalink to this definition") 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 input_key
 

*:
 




 str*
*=
 




 'text'*
[#](#langchain.chains.QAGenerationChain.input_key "Permalink to this definition") 






*field*


 k
 

*:
 




 Optional
 


 [
 


 int
 


 ]*
*=
 




 None*
[#](#langchain.chains.QAGenerationChain.k "Permalink to this definition") 






*field*


 llm_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.QAGenerationChain.llm_chain "Permalink to this definition") 






*field*


 output_key
 

*:
 




 str*
*=
 




 'questions'*
[#](#langchain.chains.QAGenerationChain.output_key "Permalink to this definition") 






*field*


 text_splitter
 

*:
 



[TextSplitter](text_splitter#langchain.text_splitter.TextSplitter "langchain.text_splitter.TextSplitter")*
*=
 




 <langchain.text_splitter.RecursiveCharacterTextSplitter
 

 object>*
[#](#langchain.chains.QAGenerationChain.text_splitter "Permalink to this definition") 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *prompt
 



 :
 





 Optional
 


 [
 

[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.qa_generation.base.QAGenerationChain](#langchain.chains.QAGenerationChain "langchain.chains.qa_generation.base.QAGenerationChain")


[[source]](../../_modules/langchain/chains/qa_generation/base#QAGenerationChain.from_llm)
[#](#langchain.chains.QAGenerationChain.from_llm "Permalink to this definition") 






*property*


 input_keys
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.chains.QAGenerationChain.input_keys "Permalink to this definition") 



 Input keys this chain expects.
 






*property*


 output_keys
 

*:
 




 List
 


 [
 


 str
 


 ]*
[#](#langchain.chains.QAGenerationChain.output_keys "Permalink to this definition") 



 Output keys this chain expects.
 








*pydantic
 

 model*


 langchain.chains.
 



 QAWithSourcesChain
 

[[source]](../../_modules/langchain/chains/qa_with_sources/base#QAWithSourcesChain)
[#](#langchain.chains.QAWithSourcesChain "Permalink to this definition") 



 Question answering with sources over documents.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_naming`
 »
 `all
 

 fields`








*pydantic
 

 model*


 langchain.chains.
 



 RetrievalQA
 

[[source]](../../_modules/langchain/chains/retrieval_qa/base#RetrievalQA)
[#](#langchain.chains.RetrievalQA "Permalink to this definition") 



 Chain for question-answering against an index.
 



 Example
 





```
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.faiss import FAISS
from langchain.vectorstores.base import VectorStoreRetriever
retriever = VectorStoreRetriever(vectorstore=FAISS(...))
retrievalQA = RetrievalQA.from_llm(llm=OpenAI(), retriever=retriever)

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 retriever
 

*:
 




 BaseRetriever*
*[Required]*
[#](#langchain.chains.RetrievalQA.retriever "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 RetrievalQAWithSourcesChain
 

[[source]](../../_modules/langchain/chains/qa_with_sources/retrieval#RetrievalQAWithSourcesChain)
[#](#langchain.chains.RetrievalQAWithSourcesChain "Permalink to this definition") 



 Question-answering with sources over an index.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_naming`
 »
 `all
 

 fields`






*field*


 max_tokens_limit
 

*:
 




 int*
*=
 




 3375*
[#](#langchain.chains.RetrievalQAWithSourcesChain.max_tokens_limit "Permalink to this definition") 



 Restrict the docs to return from store based on tokens,
enforced only for StuffDocumentChain and if reduce_k_below_max_tokens is to true
 






*field*


 reduce_k_below_max_tokens
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.chains.RetrievalQAWithSourcesChain.reduce_k_below_max_tokens "Permalink to this definition") 



 Reduce the number of results to return from store based on tokens limit
 






*field*


 retriever
 

*:
 




 langchain.schema.BaseRetriever*
*[Required]*
[#](#langchain.chains.RetrievalQAWithSourcesChain.retriever "Permalink to this definition") 



 Index to connect to.
 








*pydantic
 

 model*


 langchain.chains.
 



 SQLDatabaseChain
 

[[source]](../../_modules/langchain/chains/sql_database/base#SQLDatabaseChain)
[#](#langchain.chains.SQLDatabaseChain "Permalink to this definition") 



 Chain for interacting with SQL Database.
 



 Example
 





```
from langchain import SQLDatabaseChain, OpenAI, SQLDatabase
db = SQLDatabase(...)
db_chain = SQLDatabaseChain.from_llm(OpenAI(), db)

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 database
 

*:
 




 SQLDatabase*
*[Required]*
[#](#langchain.chains.SQLDatabaseChain.database "Permalink to this definition") 



 SQL Database to connect to.
 






*field*


 llm
 

*:
 




 Optional
 


 [
 


 BaseLanguageModel
 


 ]*
*=
 




 None*
[#](#langchain.chains.SQLDatabaseChain.llm "Permalink to this definition") 



 [Deprecated] LLM wrapper to use.
 






*field*


 llm_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.SQLDatabaseChain.llm_chain "Permalink to this definition") 






*field*


 prompt
 

*:
 




 Optional
 


 [
 

[BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.BasePromptTemplate")


 ]*
*=
 




 None*
[#](#langchain.chains.SQLDatabaseChain.prompt "Permalink to this definition") 



 [Deprecated] Prompt to use to translate natural language to SQL.
 






*field*


 return_direct
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.chains.SQLDatabaseChain.return_direct "Permalink to this definition") 



 Whether or not to return the result of querying the SQL table directly.
 






*field*


 return_intermediate_steps
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.chains.SQLDatabaseChain.return_intermediate_steps "Permalink to this definition") 



 Whether or not to return the intermediate steps along with the final answer.
 






*field*


 top_k
 

*:
 




 int*
*=
 




 5*
[#](#langchain.chains.SQLDatabaseChain.top_k "Permalink to this definition") 



 Number of results to return from the query
 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *db
 



 :
 





 langchain.sql_database.SQLDatabase*
 ,
 *prompt
 



 :
 





 Optional
 


 [
 

[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")


 ]
 






 =
 





 None*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.sql_database.base.SQLDatabaseChain](#langchain.chains.SQLDatabaseChain "langchain.chains.sql_database.base.SQLDatabaseChain")


[[source]](../../_modules/langchain/chains/sql_database/base#SQLDatabaseChain.from_llm)
[#](#langchain.chains.SQLDatabaseChain.from_llm "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 SQLDatabaseSequentialChain
 

[[source]](../../_modules/langchain/chains/sql_database/base#SQLDatabaseSequentialChain)
[#](#langchain.chains.SQLDatabaseSequentialChain "Permalink to this definition") 



 Chain for querying SQL database that is a sequential chain.
 



 The chain is as follows:
1. Based on the query, determine which tables to use.
2. Based on those tables, call the normal SQL database chain.
 



 This is useful in cases where the number of tables in the database is large.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 decider_chain
 

*:
 



[LLMChain](#langchain.chains.LLMChain "langchain.chains.LLMChain")*
*[Required]*
[#](#langchain.chains.SQLDatabaseSequentialChain.decider_chain "Permalink to this definition") 






*field*


 return_intermediate_steps
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.chains.SQLDatabaseSequentialChain.return_intermediate_steps "Permalink to this definition") 






*field*


 sql_chain
 

*:
 



[SQLDatabaseChain](#langchain.chains.SQLDatabaseChain "langchain.chains.SQLDatabaseChain")*
*[Required]*
[#](#langchain.chains.SQLDatabaseSequentialChain.sql_chain "Permalink to this definition") 






*classmethod*


 from_llm
 


 (
 
*llm
 



 :
 





 langchain.base_language.BaseLanguageModel*
 ,
 *database
 



 :
 





 langchain.sql_database.SQLDatabase*
 ,
 *query_prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['input',
 

 'table_info',
 

 'dialect',
 

 'top_k'],
 

 output_parser=None,
 

 partial_variables={},
 

 template='Given
 

 an
 

 input
 

 question,
 

 first
 

 create
 

 a
 

 syntactically
 

 correct
 

 {dialect}
 

 query
 

 to
 

 run,
 

 then
 

 look
 

 at
 

 the
 

 results
 

 of
 

 the
 

 query
 

 and
 

 return
 

 the
 

 answer.
 

 Unless
 

 the
 

 user
 

 specifies
 

 in
 

 his
 

 question
 

 a
 

 specific
 

 number
 

 of
 

 examples
 

 he
 

 wishes
 

 to
 

 obtain,
 

 always
 

 limit
 

 your
 

 query
 

 to
 

 at
 

 most
 

 {top_k}
 

 results.
 

 You
 

 can
 

 order
 

 the
 

 results
 

 by
 

 a
 

 relevant
 

 column
 

 to
 

 return
 

 the
 

 most
 

 interesting
 

 examples
 

 in
 

 the
 

 database.\n\nNever
 

 query
 

 for
 

 all
 

 the
 

 columns
 

 from
 

 a
 

 specific
 

 table,
 

 only
 

 ask
 

 for
 

 a
 

 the
 

 few
 

 relevant
 

 columns
 

 given
 

 the
 

 question.\n\nPay
 

 attention
 

 to
 

 use
 

 only
 

 the
 

 column
 

 names
 

 that
 

 you
 

 can
 

 see
 

 in
 

 the
 

 schema
 

 description.
 

 Be
 

 careful
 

 to
 

 not
 

 query
 

 for
 

 columns
 

 that
 

 do
 

 not
 

 exist.
 

 Also,
 

 pay
 

 attention
 

 to
 

 which
 

 column
 

 is
 

 in
 

 which
 

 table.\n\nUse
 

 the
 

 following
 

 format:\n\nQuestion:
 

 "Question
 

 here"\nSQLQuery:
 

 "SQL
 

 Query
 

 to
 

 run"\nSQLResult:
 

 "Result
 

 of
 

 the
 

 SQLQuery"\nAnswer:
 

 "Final
 

 answer
 

 here"\n\nOnly
 

 use
 

 the
 

 tables
 

 listed
 

 below.\n\n{table_info}\n\nQuestion:
 

 {input}',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *decider_prompt
 



 :
 




[langchain.prompts.base.BasePromptTemplate](prompts#langchain.prompts.BasePromptTemplate "langchain.prompts.base.BasePromptTemplate")





 =
 





 PromptTemplate(input_variables=['query',
 

 'table_names'],
 

 output_parser=CommaSeparatedListOutputParser(),
 

 partial_variables={},
 

 template='Given
 

 the
 

 below
 

 input
 

 question
 

 and
 

 list
 

 of
 

 potential
 

 tables,
 

 output
 

 a
 

 comma
 

 separated
 

 list
 

 of
 

 the
 

 table
 

 names
 

 that
 

 may
 

 be
 

 necessary
 

 to
 

 answer
 

 this
 

 question.\n\nQuestion:
 

 {query}\n\nTable
 

 Names:
 

 {table_names}\n\nRelevant
 

 Table
 

 Names:',
 

 template_format='f-string',
 

 validate_template=True)*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 

[langchain.chains.sql_database.base.SQLDatabaseSequentialChain](#langchain.chains.SQLDatabaseSequentialChain "langchain.chains.sql_database.base.SQLDatabaseSequentialChain")


[[source]](../../_modules/langchain/chains/sql_database/base#SQLDatabaseSequentialChain.from_llm)
[#](#langchain.chains.SQLDatabaseSequentialChain.from_llm "Permalink to this definition") 



 Load the necessary chains.
 








*pydantic
 

 model*


 langchain.chains.
 



 SequentialChain
 

[[source]](../../_modules/langchain/chains/sequential#SequentialChain)
[#](#langchain.chains.SequentialChain "Permalink to this definition") 



 Chain where the outputs of one chain feed directly into next.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_chains`
 »
 `all
 

 fields`






*field*


 chains
 

*:
 




 List
 


 [
 


 langchain.chains.base.Chain
 


 ]*
*[Required]*
[#](#langchain.chains.SequentialChain.chains "Permalink to this definition") 






*field*


 input_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Required]*
[#](#langchain.chains.SequentialChain.input_variables "Permalink to this definition") 






*field*


 return_all
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.chains.SequentialChain.return_all "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 SimpleSequentialChain
 

[[source]](../../_modules/langchain/chains/sequential#SimpleSequentialChain)
[#](#langchain.chains.SimpleSequentialChain "Permalink to this definition") 



 Simple chain where the outputs of one step feed directly into next.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_chains`
 »
 `all
 

 fields`






*field*


 chains
 

*:
 




 List
 


 [
 


 langchain.chains.base.Chain
 


 ]*
*[Required]*
[#](#langchain.chains.SimpleSequentialChain.chains "Permalink to this definition") 






*field*


 strip_outputs
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.chains.SimpleSequentialChain.strip_outputs "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 TransformChain
 

[[source]](../../_modules/langchain/chains/transform#TransformChain)
[#](#langchain.chains.TransformChain "Permalink to this definition") 



 Chain transform chain output.
 



 Example
 





```
from langchain import TransformChain
transform_chain = TransformChain(input_variables=["text"],
 output_variables["entities"], transform=func())

```





 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`






*field*


 input_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Required]*
[#](#langchain.chains.TransformChain.input_variables "Permalink to this definition") 






*field*


 output_variables
 

*:
 




 List
 


 [
 


 str
 


 ]*
*[Required]*
[#](#langchain.chains.TransformChain.output_variables "Permalink to this definition") 






*field*


 transform
 

*:
 




 Callable
 


 [
 



 [
 


 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]
 



 ,
 




 Dict
 


 [
 


 str
 


 ,
 




 str
 


 ]
 



 ]*
*[Required]*
[#](#langchain.chains.TransformChain.transform "Permalink to this definition") 








*pydantic
 

 model*


 langchain.chains.
 



 VectorDBQA
 

[[source]](../../_modules/langchain/chains/retrieval_qa/base#VectorDBQA)
[#](#langchain.chains.VectorDBQA "Permalink to this definition") 



 Chain for question-answering against a vector database.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_search_type`
 »
 `all
 

 fields`






*field*


 k
 

*:
 




 int*
*=
 




 4*
[#](#langchain.chains.VectorDBQA.k "Permalink to this definition") 



 Number of documents to query for.
 






*field*


 search_kwargs
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
*[Optional]*
[#](#langchain.chains.VectorDBQA.search_kwargs "Permalink to this definition") 



 Extra search args.
 






*field*


 search_type
 

*:
 




 str*
*=
 




 'similarity'*
[#](#langchain.chains.VectorDBQA.search_type "Permalink to this definition") 



 Search type to use over vectorstore.
 
 similarity
 
 or
 
 mmr
 
 .
 






*field*


 vectorstore
 

*:
 



[VectorStore](vectorstores#langchain.vectorstores.VectorStore "langchain.vectorstores.VectorStore")*
*[Required]*
[#](#langchain.chains.VectorDBQA.vectorstore "Permalink to this definition") 



 Vector Database to connect to.
 








*pydantic
 

 model*


 langchain.chains.
 



 VectorDBQAWithSourcesChain
 

[[source]](../../_modules/langchain/chains/qa_with_sources/vector_db#VectorDBQAWithSourcesChain)
[#](#langchain.chains.VectorDBQAWithSourcesChain "Permalink to this definition") 



 Question-answering with sources over a vector database.
 




 Validators
 

* `raise_deprecation`
 »
 `all
 

 fields`
* `set_verbose`
 »
 `verbose`
* `validate_naming`
 »
 `all
 

 fields`






*field*


 k
 

*:
 




 int*
*=
 




 4*
[#](#langchain.chains.VectorDBQAWithSourcesChain.k "Permalink to this definition") 



 Number of results to return from store
 






*field*


 max_tokens_limit
 

*:
 




 int*
*=
 




 3375*
[#](#langchain.chains.VectorDBQAWithSourcesChain.max_tokens_limit "Permalink to this definition") 



 Restrict the docs to return from store based on tokens,
enforced only for StuffDocumentChain and if reduce_k_below_max_tokens is to true
 






*field*


 reduce_k_below_max_tokens
 

*:
 




 bool*
*=
 




 False*
[#](#langchain.chains.VectorDBQAWithSourcesChain.reduce_k_below_max_tokens "Permalink to this definition") 



 Reduce the number of results to return from store based on tokens limit
 






*field*


 search_kwargs
 

*:
 




 Dict
 


 [
 


 str
 


 ,
 




 Any
 


 ]*
*[Optional]*
[#](#langchain.chains.VectorDBQAWithSourcesChain.search_kwargs "Permalink to this definition") 



 Extra search args.
 






*field*


 vectorstore
 

*:
 



[langchain.vectorstores.base.VectorStore](vectorstores#langchain.vectorstores.VectorStore "langchain.vectorstores.base.VectorStore")*
*[Required]*
[#](#langchain.chains.VectorDBQAWithSourcesChain.vectorstore "Permalink to this definition") 



 Vector Database to connect to.
 










 langchain.chains.
 



 load_chain
 


 (
 
*path
 



 :
 





 Union
 


 [
 


 str
 


 ,
 




 pathlib.Path
 


 ]*
 ,
 *\*\*
 



 kwargs
 



 :
 





 Any*

 )
 


 →
 


 langchain.chains.base.Chain
 


[[source]](../../_modules/langchain/chains/loading#load_chain)
[#](#langchain.chains.load_chain "Permalink to this definition") 



 Unified method for loading a chain from LangChainHub or local fs.
 






