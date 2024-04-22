// import '../styles/global.css';
// import Layout from '../components/Layout';

// function MyApp({ Component, pageProps }) {
//   return (
//     <Layout>
//       <Component {...pageProps} />
//     </Layout>
//   );
// }

// export default MyApp;


// // pages/_app.js
// import '../styles/global.css'; // 替换为你的全局样式文件路径

// export default function MyApp({ Component, pageProps }) {
//   return (
//     <>
//       <div style={{ width: '100%', height: '60px', backgroundColor: 'red' }}>
        
//       </div>
//       <Component {...pageProps} />);
//     </>
  
// }


import '../styles/global.css';
import Head from 'next/head';

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Head>
        <meta name="baidu-site-verification" content="codeva-vVWLPfYJJm" />
        <script>
          {
            `(function() {
         var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?e60fb290e204e04c5cb6f79b0ac1e697";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
       })();`
          }
        </script>
      </Head>
      <Component {...pageProps} />
    </>
  );
}

export default MyApp;