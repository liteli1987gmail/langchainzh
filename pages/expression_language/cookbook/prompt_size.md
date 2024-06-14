# 管理提示窗口大小

代理动态调用工具。这些工具的调用结果被添加回提示内容，以便代理可以计划下一步动作。根据所使用的工具和调用方式，代理提示可能会比模型上下文窗口更大。

使用LCEL，可以轻松添加自定义功能，以管理链或代理内提示的大小。让我们看一个简单的代理示例，该代理可以搜索维基百科获取信息。


```python
%pip install --upgrade --quiet  langchain langchain-openai wikipedia
```


```python
from operator import itemgetter

from langchain.agents import AgentExecutor, load_tools
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.prompt_values import ChatPromptValue
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
```


```python
wiki = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=10_000)
)
tools = [wiki]
```


```python
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo")
```

让我们尝试一个没有处理提示大小的多步问题：


```python
agent = (
    {
        "input": itemgetter("input"),
        "agent_scratchpad": lambda x: format_to_openai_function_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm.bind_functions(tools)
    | OpenAIFunctionsAgentOutputParser()
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke(
    {
        "input": "Who is the current US president? What's their home state? What's their home state's bird? What's that bird's scientific name?"
    }
)
```

```

文件~/langchain/libs/langchain/langchain/agents/agent.py:1097， in AgentExecutor._take_next_step(self, name_to_tool_map, color_mapping, inputs, intermediate_steps, run_manager)
   1088 def _take_next_step(
   1089     self,
   1090     name_to_tool_map: Dict[str, BaseTool],
   (...)
   1094     run_manager: Optional[CallbackManagerForChainRun] = None,
   1095 ) -> Union[AgentFinish, List[Tuple[AgentAction, str]]]:
   1096     return self._consume_next_step(
-> 1097         [
   1098             a
   1099             for a in self._iter_next_step(
   1100                 name_to_tool_map,
   1101                 color_mapping,
   1102                 inputs,
   1103                 intermediate_steps,
   1104                 run_manager,
   1105             )
   1106         ]
   1107     )


文件~/langchain/libs/langchain/langchain/agents/agent.py:1097， in <listcomp>(.0)
   1088 def _take_next_step(
   1089     self,
   1090     name_to_tool_map: Dict[str, BaseTool],
   (...)
   1094     run_manager: Optional[CallbackManagerForChainRun] = None,
   1095 ) -> Union[AgentFinish, List[Tuple[AgentAction, str]]]:
   1096     return self._consume_next_step(
-> 1097         [
   1098             a
   1099             for a in self._iter_next_step(
   1100                 name_to_tool_map,
   1101                 color_mapping,
   1102                 inputs,
   1103                 intermediate_steps,
   1104                 run_manager,
   1105             )
   1106         ]
   1107     )


文件~/langchain/libs/langchain/langchain/agents/agent.py:1125， in AgentExecutor._iter_next_step(self, name_to_tool_map, color_mapping, inputs, intermediate_steps, run_manager)
   1122     intermediate_steps = self._prepare_intermediate_steps(intermediate_steps)
   1124     # Call the LLM to see what to do.
-> 1125     output = self.agent.plan(
   1126         intermediate_steps,
   1127         callbacks=run_manager.get_child() if run_manager else None,
   1128         **inputs,
   1129     )
   1130 except OutputParserException as e:
   1131     if isinstance(self.handle_parsing_errors, bool):

文件~/langchain/libs/langchain/langchain/agents/agent.py:387， in RunnableAgent.plan(self, intermediate_steps, callbacks, **kwargs)
    381 # Use streaming to make sure that the underlying LLM is invoked in a streaming
    382 # fashion to make it possible to get access to the individual LLM tokens
    383 # when using stream_log with the Agent Executor.
    384 # Because the response from the plan is not a generator, we need to
    385 # accumulate the output into final output and return that.
    386 final_output: Any = None
--> 387 for chunk in self.runnable.stream(inputs, config={"callbacks": callbacks}):
    388     if final_output is None:
    389         final_output = chunk

文件~/langchain/libs/core/langchain_core/runnables/base.py:2424， in RunnableSequence.stream(self, input, config, **kwargs)
   2418 def stream(
   2419     self,
   2420     input: Input,
   2421     config: Optional[RunnableConfig] = None,
   2422     **kwargs: Optional[Any],
   2423 ) -> Iterator[Output]:
-> 2424     yield from self.transform(iter([input]), config, **kwargs)

文件~/langchain/libs/core/langchain_core/runnables/base.py:2411， in RunnableSequence.transform(self, input, config, **kwargs)
   2405 def transform(
   2406     self,
   2407     input: Iterator[Input],
   2408     config: Optional[RunnableConfig] = None,
   2409     **kwargs: Optional[Any],
   2410 ) -> Iterator[Output]:
-> 2411     yield from self._transform_stream_with_config(
   2412         input,
   2413         self._transform,
   2414         patch_config(config, run_name=(config or {}).get("run_name") or self.name),
   2415         **kwargs,
   2416     )

文件~/langchain/libs/core/langchain_core/runnables/base.py:1497， in Runnable._transform_stream_with_config(self, input, transformer, config, run_type, **kwargs)
   1495 try:
   1496     while True:
-> 1497         chunk: Output = context.run(next, iterator)  # type: ignore
   1498         yield chunk
   1499         if final_output_supported:

文件~/langchain/libs/core/langchain_core/runnables/base.py:2375， in RunnableSequence._transform(self, input, run_manager, config)
   2366 for step in steps:
   2367     final_pipeline = step.transform(
   2368         final_pipeline,
   2369         patch_config(
   (...)
   2372         ),
   2373     )
-> 2375 for output in final_pipeline:
   2376     yield output

文件~/langchain/libs/core/langchain_core/runnables/base.py:1035， in Runnable.transform(self, input, config, **kwargs)
   1032 final: Input
   1033 got_first_val = False
-> 1035 for chunk in input:
   1036     if not got_first_val:
   1037         final = chunk

文件~/langchain/libs/core/langchain_core/runnables/base.py:3991， in RunnableBindingBase.transform(self, input, config, **kwargs)
   3985 def transform(
   3986     self,
   3987     input: Iterator[Input],
   3988     config: Optional[RunnableConfig] = None,
   3989     **kwargs: Any,
   3990 ) -> Iterator[Output]:
-> 3991     yield from self.bound.transform(
   3992         input,
   3993         self._merge_configs(config),
   3994         **{**self.kwargs, **kwargs},
   3995     )

文件~/langchain/libs/core/langchain_core/runnables/base.py:1045， in Runnable.transform(self, input, config, **kwargs)
   1042         final = final + chunk  # type: ignore[operator]
   1044 if got_first_val:
-> 1045     yield from self.stream(final, config, **kwargs)

文件~/langchain/libs/core/langchain_core/language_models/chat_models.py:249， in BaseChatModel.stream(self, input, config, stop, **kwargs)
   242 except BaseException as e:
   243     run_manager.on_llm_error(
   244         e,
   245         response=LLMResult(
   246             generations=[[generation]] if generation else []
   247         ),
   248     )
--> 249     raise e
   250 else:
   251     run_manager.on_llm_end(LLMResult(generations=[[generation]]))

文件~/langchain/libs/core/langchain_core/language_models/chat_models.py:233， in BaseChatModel.stream(self, input, config, stop, **kwargs)
   231 generation: Optional[ChatGenerationChunk] = None
   232 try:
--> 233     for chunk in self._stream(
   234         messages, stop=stop, run_manager=run_manager, **kwargs
   235     ):
   236         yield chunk.message
   237         if generation is None:

文件~/langchain/libs/partners/openai/langchain_openai/chat_models/base.py:403， in ChatOpenAI._stream(self, messages, stop, run_manager, **kwargs)
   400 params = {**params, **kwargs, "stream": True}
   402 default_chunk_class = AIMessageChunk
--> 403 for chunk in self.client.create(messages=message_dicts, **params):
   404     if not isinstance(chunk, dict):
   405         chunk = chunk.dict()

文件~/langchain/.venv/lib/python3.9/site-packages/openai/_utils/_utils.py:271， in required_args.<locals>.inner.<locals>.wrapper(*args, **kwargs)
   269             msg = f"Missing required argument: {quote(missing[0])}"
   270     raise TypeError(msg)
--> 271 return func(*args, **kwargs)

文件~/langchain/.venv/lib/python3.9/site-packages/openai/resources/chat/completions.py:648， in Completions.create(self, messages, model, frequency_penalty, function_call, functions, logit_bias, logprobs, max_tokens, n, presence_penalty, response_format, seed, stop, stream, temperature, tool_choice, tools, top_logprobs, top_p, user, extra_headers, extra_query, extra_body, timeout)
   599 @required_args(["messages", "model"], ["messages", "model", "stream"])
   600 def create(
   601     self,
   (...)
    646     timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
   647 ) -> ChatCompletion | Stream[ChatCompletionChunk]:
--> 648     return self._post(
   649         "/chat/completions",
   650         body=maybe_transform(
   651             {
   652                 "messages": messages,
   653                 "model": model,
   654                 "frequency_penalty": frequency_penalty,
   655                 "function_call": function_call,
   656                 "functions": functions,
   657                 "logit_bias": logit_bias,
   658                 "logprobs": logprobs,
   659                 "max_tokens": max_tokens,
   660                 "n": n,
   661                 "presence_penalty": presence_penalty,
   662                 "response_format": response_format,
   663                 "seed": seed,
   664                 "stop": stop,
   665                 "stream": stream,
   666                 "temperature": temperature,
   667                 "tool_choice": tool_choice,
   668                 "tools": tools,
   669                 "top_logprobs": top_logprobs,
   670                 "top_p": top_p,
   671                 "user": user,
   672             },
   673             completion_create_params.CompletionCreateParams,
   674         ),
   675         options=make_request_options(
   676             extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
   677         ),
   678         cast_to=ChatCompletion,
   679         stream=stream or False,
   680         stream_cls=Stream[ChatCompletionChunk],
   681     )
    

    文件 ~/langchain/.venv/lib/python3.9/site-packages/openai/_base_client.py:1179, in SyncAPIClient.post(self, path, cast_to, body, options, files, stream, stream_cls)
       1165 def post(
       1166     self,
       1167     path: str,
       (...)
       1174     stream_cls: type[_StreamT] | None = None,
       1175 ) -> ResponseT | _StreamT:
       1176     opts = FinalRequestOptions.construct(
       1177         method="post", url=path, json_data=body, files=to_httpx_files(files), **options
       1178     )
    -> 1179     return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
    

    文件 ~/langchain/.venv/lib/python3.9/site-packages/openai/_base_client.py:868, in SyncAPIClient.request(self, cast_to, options, remaining_retries, stream, stream_cls)
        859 def request(
        860     self,
        861     cast_to: Type[ResponseT],
       (...)
        866     stream_cls: type[_StreamT] | None = None,
        867 ) -> ResponseT | _StreamT:
    --> 868     return self._request(
        869         cast_to=cast_to,
        870         options=options,
        871         stream=stream,
        872         stream_cls=stream_cls,
        873         remaining_retries=remaining_retries,
        874     )
    

    文件 ~/langchain/.venv/lib/python3.9/site-packages/openai/_base_client.py:959, in SyncAPIClient._request(self, cast_to, options, remaining_retries, stream, stream_cls)
        956         err.response.read()
        958     log.debug("Re-raising status error")
    --> 959     raise self._make_status_error_from_response(err.response) from None
        961 return self._process_response(
        962     cast_to=cast_to,
        963     options=options,
       (...)
        966     stream_cls=stream_cls,
        967 )
    

    BadRequestError: 错误代码: 400 - {'error': {'message': "The maximum context length for this model is 4097 tokens. However, your messages resulted in 5487 tokens (5419 in the messages, 68 in the functions). Please reduce the length of the messages or functions.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}
```

:::

[LangSmith 追踪](https://smith.langchain.com/public/60909eae-f4f1-43eb-9f96-354f5176f66f/r)

:::

很不幸，在我们的模型上下文窗口耗尽之前，代理就无法得出最终答案。现在让我们添加一些提示处理逻辑。为了保持简单，如果我们的消息包含的标记太多，我们将开始删除聊天历史中最早的AI、功能消息对（这是模型工具调用消息和随后的工具输出消息）。


```python
def condense_prompt(prompt: ChatPromptValue) -> ChatPromptValue:
    messages = prompt.to_messages()
    num_tokens = llm.get_num_tokens_from_messages(messages)
    ai_function_messages = messages[2:]
    while num_tokens > 4_000:
        ai_function_messages = ai_function_messages[2:]
        num_tokens = llm.get_num_tokens_from_messages(
            messages[:2] + ai_function_messages
        )
    messages = messages[:2] + ai_function_messages
    return ChatPromptValue(messages=messages)


agent = (
    {
        "input": itemgetter("input"),
        "agent_scratchpad": lambda x: format_to_openai_function_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | condense_prompt
    | llm.bind_functions(tools)
    | OpenAIFunctionsAgentOutputParser()
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke(
    {
        "input": "Who is the current US president? What's their home state? What's their home state's bird? What's that bird's scientific name?"
    }
)
```

    
    
    [1m> Entering new AgentExecutor chain...[0m
    [32;1m[1;3m
    Invoking: `Wikipedia` with `List of presidents of the United States`
    
    
    [0m[36;1m[1;3mPage: List of presidents of the United States
    Summary: The president of the United States is the head of state and head of government of the United States, indirectly elected to a four-year term via the Electoral College. The officeholder leads the executive branch of the federal government and is the commander-in-chief of the United States Armed Forces. Since the office was established in 1789, 45 men have served in 46 presidencies. The first president, George Washington, won a unanimous vote of the Electoral College. Grover Cleveland served two non-consecutive terms and is therefore counted as the 22nd and 24th president of the United States, giving rise to the discrepancy between the number of presidencies and the number of individuals who have served as president. The incumbent president is Joe Biden.The presidency of William Henry Harrison, who died 31 days after taking office in 1841, was the shortest in American history. Franklin D. Roosevelt served the longest, over twelve years, before dying early in his fourth term in 1945. He is the only U.S. president to have served more than two terms. Since the ratification of the Twenty-second Amendment to the United States Constitution in 1951, no person may be elected president more than twice, and no one who has served more than two years of a term to which someone else was elected may be elected more than once.Four presidents died in office of natural causes (William Henry Harrison, Zachary Taylor, Warren G. Harding, and Franklin D. Roosevelt), four were assassinated (Abraham Lincoln, James A. Garfield, William McKinley, and John F. Kennedy), and one resigned (Richard Nixon, facing impeachment and removal from office). John Tyler was the first vice president to assume the presidency during a presidential term, and set the precedent that a vice president who does so becomes the fully functioning president with his presidency.Throughout most of its history, American politics has been dominated by political parties. The Constitution is silent on the issue of political parties, and at the time it came into force in 1789, no organized parties existed. Soon after the 1st Congress convened, political factions began rallying around dominant Washington administration officials, such as Alexander Hamilton and Thomas Jefferson. Concerned about the capacity of political parties to destroy the fragile unity holding the nation together, Washington remained unaffiliated with any political faction or party throughout his eight-year presidency. He was, and remains, the only U.S. president never affiliated with a political party.
    
    Page: List of presidents of the United States by age
    Summary: In this list of presidents of the United States by age, the first table charts the age of each president of the United States at the time of presidential inauguration (first inauguration if elected to multiple and consecutive terms), upon leaving office, and at the time of death. Where the president is still living, their lifespan and post-presidency timespan are calculated up to January 25, 2024.
    
    Page: List of vice presidents of the United States
    Summary: There have been 49 vice presidents of the United States since the office was created in 1789. Originally, the vice president was the person who received the second-most votes for president in the Electoral College. But after the election of 1800 produced a tie between Thomas Jefferson and Aaron Burr, requiring the House of Representatives to choose between them, lawmakers acted to prevent such a situation from recurring. The Twelfth Amendment was added to the Constitution in 1804, creating the current system where electors cast a separate ballot for the vice presidency.The vice president is the first person in the presidential line of succession—that is, they assume the presidency if the president dies, resigns, or is impeached and removed from office. Nine vice presidents have ascended to the presidency in this way: eight (John Tyler, Millard Fillmore, Andrew Johnson, Chester A. Arthur, Theodore Roosevelt, Calvin Coolidge, Harry S. Truman, and Lyndon B. Johnson) through the president's death and one (Gerald Ford) through the president's resignation. The vice president also serves as the president of the Senate and may choose to cast a tie-breaking vote on decisions made by the Senate. Vice presidents have exercised this latter power to varying extents over the years.Before adoption of the Twenty-fifth Amendment in 1967, an intra-term vacancy in the office of the vice president could not be filled until the next post-election inauguration. Several such vacancies occurred: seven vice presidents died, one resigned and eight succeeded to the presidency. This amendment allowed for a vacancy to be filled through appointment by the president and confirmation by both chambers of the Congress. Since its ratification, the vice presidency has been vacant twice (both in the context of scandals surrounding the Nixon administration) and was filled both times through this process, namely in 1973 following Spiro Agnew's resignation, and again in 1974 after Gerald Ford succeeded to the presidency. The amendment also established a procedure whereby a vice president may, if the president is unable to discharge the powers and duties of the office, temporarily assume the powers and duties of the office as acting president. Three vice presidents have briefly acted as president under the 25th Amendment: George H. W. Bush on July 13, 1985; Dick Cheney on June 29, 2002, and on July 21, 2007; and Kamala Harris on November 19, 2021.
    The persons who have served as vice president were born in or primarily affiliated with 27 states plus the District of Columbia. New York has produced the most of any state as eight have been born there and three others considered it their home state. Most vice presidents have been in their 50s or 60s and had political experience before assuming the office. Two vice presidents—George Clinton and John C. Calhoun—served under more than one president. Ill with tuberculosis and recovering in Cuba on Inauguration Day in 1853, William R. King, by an Act of Congress, was allowed to take the oath outside the United States. He is the only vice president to take his oath of office in a foreign country.
    
    Page: List of presidents of the United States by net worth
    Summary: The list of presidents of the United States by net worth at peak varies greatly. Debt and depreciation often means that presidents' net worth is less than $0 at the time of death. Most presidents before 1845 were extremely wealthy, especially Andrew Jackson and George Washington. 	 
    Presidents since 1929, when Herbert Hoover took office, have generally been wealthier than presidents of the late nineteenth and early twentieth centuries; with the exception of Harry S. Truman, all presidents since this time have been millionaires. These presidents have often received income from autobiographies and other writing. Except for Franklin D. Roosevelt and John F. Kennedy (both of whom died while in office), all presidents beginning with Calvin Coolidge have written autobiographies. In addition, many presidents—including Bill Clinton—have earned considerable income from public speaking after leaving office.The richest president in history may be Donald Trump. However, his net worth is not precisely known because the Trump Organization is privately held.Truman was among the poorest U.S. presidents, with a net worth considerably less than $1 million. His financial situation contributed to the doubling of the presidential salary to $100,000 in 1949. In addition, the presidential pension was created in 1958 when Truman was again experiencing financial difficulties. Harry and Bess Truman received the first Medicare cards in 1966 via the Social Security Act of 1965.
    
    Page: List of presidents of the United States by home state
    Summary: These lists give the states of primary affiliation and of birth for each president of the United States.[0m[32;1m[1;3mThe current US president is Joe Biden. His home state is Delaware. The home state bird of Delaware is the Delaware Blue Hen. The scientific name of the Delaware Blue Hen is Gallus gallus domesticus.[0m

    [1m> Finished chain.[0m{'input': 'Who is the current US president? What\'s their home state? What\'s their home state\'s bird? What\'s that bird\'s scientific name?', 

```
'output': '谁是当前的美国总统？他们的家乡是哪个州？他们家乡州的鸟是什么？那只鸟的科学名字是什么？'}```