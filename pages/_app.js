// pages/_app.js
import '../styles/global.css'; // 替换为你的全局样式文件路径

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}