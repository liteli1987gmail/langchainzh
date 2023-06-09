import os
import re

def replace_extension(folder_path):
    # 递归遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                print(file_path)

                # 将文件名 .md 替换为 .mdx
                new_filename = re.sub('\.md$', '.mdx', filename)
                new_file_path = os.path.join(root, new_filename)

                # 读取文件并插入 JavaScript 代码
                with open(file_path, 'r',encoding='utf-8') as f_in:
                    file_content = f_in.read()

                with open(new_file_path, 'w',encoding='utf-8') as f_out:
                    # 插入 JavaScript 代码
                    js_code = """
import Head from 'next/head'

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

![LangChain](https://pica.zhimg.com/50/v2-56e8bbb52aa271012541c1fe1ceb11a2_r.gif)"""

                    # 如果新文件不存在，则在新文件中写入 JavaScript 代码和原始文件内容
                    if not os.path.exists(new_file_path):
                        f_out.write(js_code + '\n\n' + file_content)
                    # 如果新文件已经存在，则只写入 JavaScript 代码和原始文件内容
                    else:
                        with open(new_file_path, 'r',encoding='utf-8') as f:
                            existing_content = f.read()
                        f_out.write(js_code + '\n\n' + existing_content + '\n\n' + file_content)

                print(f'Renamed {filename} to {new_filename}')
                

def delete_md_files(folder_path):
    # 递归遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)

                # 删除文件
                os.remove(file_path)



# replace_extension('./pages/use_cases/')
delete_md_files('./pages/use_cases/')