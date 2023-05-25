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
  useNextSeoProps:() =>{
      const { asPath } = useRouter()
      if (asPath !== '/') {
        return {
          titleTemplate: '%s – LangChain中文网'
        }
      }
    },
  head: () => {
      const { asPath, defaultLocale, locale } = useRouter()
      const { frontMatter } = useConfig()
      const url =
        'https://www.langchain.com.cn' +
        (defaultLocale === locale ? asPath : `/${locale}${asPath}`)
   
      return <>
        <title>LangChain中文网：500页超详细中文文档教程，助力LLM／chatGPT应用开发</title>
        <meta name="keywords" content="langchain,LLM,chatGPT,应用开发" />
        <meta name="description" content="LangChain中文站，助力大语言模型LLM应用开发、chatGPT应用开发。" />
        <meta property="og:url" content={url} />
        <meta property="og:title" content={frontMatter.title || 'Nextra'} />
        <meta property="og:description" content={frontMatter.description || 'The next site builder'} />
      </>
    },
  banner: {
    key: '2.0-release',
    text: <a href="https://www.Langchain.com.cn/about" target="_blank">🎉 学 LangChain 免费领 openAI GPT key  限额1000名 →</a>,
  }, 
  toc: {
    float: true,
    extraContent:(
      <div>
        <img src="https://pic1.zhimg.com/80/v2-31131dcb1732cb5bca7c182c9e8da046_r.jpg" alt="扫我，入群" />
      </div>
    )
  },
  footer: {
    text: <div><span>MIT {new Date().getFullYear()} © <a href="https://www.Langchain.com.cn" target="_blank">Langchain中文网</a>. 跟着langchain学AI应用开发    </span>
    <span><a href="https://www.Langchain.com" target="_blank">Langchain英文官网    </a></span>
    <span><a href="https://github.com/hwchase17/langchain" target="_blank">GitHub    </a></span>
    <span><a href="http://www.r-p-a.com/llm-gpt-kaifa/" target="_blank">LLM/GPT应用外包开发    </a></span></div>
  }
}

export default config