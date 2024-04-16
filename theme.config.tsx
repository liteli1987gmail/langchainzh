import React from 'react'
import { useRouter } from 'next/router'
import { useConfig } from 'nextra-theme-docs'
import { DocsThemeConfig } from 'nextra-theme-docs'


const config: DocsThemeConfig = {
  logo: <span>LangChain 🦜️🔗 中文网，跟着LangChain一起学LLM/GPT开发</span>,
  project: {
    link: 'https://github.com/liteli1987gmail/langchainzh'
  },
  docsRepositoryBase: 'https://github.com/liteli1987gmail/langchainzh',
  head: () => {
      const { asPath, defaultLocale, locale } = useRouter()
      const { frontMatter } = useConfig()
      console.log(frontMatter)
      const url =
        'https://www.langchain.com.cn' +
        (defaultLocale === locale ? asPath : `/${locale}${asPath}`)
   
      return <>
        <link data-rh="true" rel="icon" href="https://js.langchain.com/img/favicon.ico"></link>
        <meta name="keywords" content="langchain,LLM,chatGPT,应用开发" />
        <meta name="description" content="LangChain中文站，助力大语言模型LLM应用开发、chatGPT应用开发。" />
        <meta property="og:url" content={url} />
        <meta property="og:description" content="LangChain中文站，助力大语言模型LLM应用开发、chatGPT应用开发。" />
      </>
    },
    useNextSeoProps:() =>{
      const { asPath } = useRouter()
      if (asPath !== '/') {
        return {
          titleTemplate: '%s – LangChain中文网'
        }
      }
    },
  banner: {
    key: '2.0-release',
    text: <a href="https://www.aiqbh.com/dalibao.html" target="_blank">🎉 学 LangChain 免费领 openAI GPT key  限额1000名 →</a>,
  }, 
  toc: {
    float: true,
    extraContent:(
      <div>
        <img src="https://www.aiqbh.com/qun.png" alt="扫我，入群" />
        <img src="https://pic2.zhimg.com/100/v2-23e6630a548c962582265f27e8967cd1_qhd.jpg" alt="扫我，找书" />
      </div>
    )
  },
  footer: {
    text: <div><span>MIT {new Date().getFullYear()} © <a href="https://www.langchain.com.cn/" target="_blank">Langchain中文网</a>. 跟着langchain学AI应用开发    </span>
    <span><a href="https://github.com/hwchase17/langchain" target="_blank">    GitHub    |</a></span>
    <span><a href="https://www.r-p-a.com/llm-gpt-kaifa/" target="_blank">    LLM/GPT应用外包开发    |</a></span>
    <span><a href="https://www.openaidoc.com.cn" target="_blank">    OpenAI 文档    |</a></span>
    <span><a href="https://www.milvus-io.com" target="_blank">    Milvus 文档    |</a></span>
    <span><a href="https://www.pinecone-io.com/ " target="_blank">    Pinecone 文档 </a></span>
    <p>
      <span><a href="https://www.Langchain.com" target="_blank">    Langchain英文站  </a></span>
      <span><a href="https://js.langchain.com.cn/docs/">    Langchain JS/TS 文档 </a></span>
      <a href="https://langchain.com.cn"><span><img style={{ display: "inline-block",height: "19px" }} src="https://mbdp01.bdstatic.com/static/landing-pc/img/icon_police.7296bdfd.png" alt="" />  沪ICP备2023014280号-3</span></a></p>
    </div>
  }
}

export default config