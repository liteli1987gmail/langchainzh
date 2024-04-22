import React from 'react';

const Banner = () => {
  return (
    <div className="my-custom-banner">
          {/* 链接和图片 1 */}
          <a href="https://www.aiqbh.com/NVIDIA-H100-server.html" style={{ flex: 1 }}>
        <img src="https://www.aiqbh.com/8xH100.png" style={{ width: '100%', height: 'auto' }} alt="英伟达8xH100" />
      </a>
      {/* 链接和图片 2 */}
      <a href="https://www.aiqbh.com/aiday/today.html" style={{ flex: 1 }}>
        <img src="http://www.aiqbh.com/ainews.png" style={{ width: '100%', height: 'auto' }} alt="每日AI新闻持续更新" />
      </a>
      {/* 链接和图片 3 */}
      <a href="https://www.aiqbh.com/KYW.png" style={{ flex: 1 }}>
        <img src="https://www.aiqbh.com/zhaozu1.png" style={{ width: '100%', height: 'auto' }} alt="10000个AI开发者在社群等你" />
      </a>
  </div>
  );
};

export default Banner;