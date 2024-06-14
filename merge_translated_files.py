# import os
# import re
# from collections import defaultdict

# def read_md_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return file.readlines()

# def merge_md_files(input_folder):
#     # 找到所有 .md 和 .mdx 文件
#     md_files = [os.path.join(root, file) for root, _, files in os.walk(input_folder) 
#                 for file in files if file.endswith(('.md', '.mdx'))]

#     # 按文件名的下划线之前部分分组
#     file_groups = defaultdict(list)
#     pattern = re.compile(r"(.*?)(?:_\d+)?(?:_\d+)?\..*")

#     for md_file in md_files:
#         base_name = pattern.match(os.path.basename(md_file))
#         if base_name:
#             file_groups[base_name.group(1)].append(md_file)

#     # 合并文件内容并删除原文件
#     for base_name, files in file_groups.items():
#         files.sort()  # 按文件名排序，确保顺序正确
#         merged_content = []
#         for file in files:
#             merged_content.extend(read_md_file(file))
        
#         new_file_name = os.path.join(input_folder, f"{base_name}.md")
#         with open(new_file_name, 'w', encoding='utf-8') as new_file:
#             new_file.writelines(merged_content)
        
#         # 删除原文件
#         for file in files:
#             os.remove(file)

import os
import re
from collections import defaultdict

def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def merge_md_files(input_folder):
    # 找到所有 .md 和 .mdx 文件
    md_files = [os.path.join(root, file) for root, _, files in os.walk(input_folder) 
                for file in files if file.endswith(('.md', '.mdx'))]

    # 按文件名前缀分组
    file_groups = defaultdict(list)
    pattern = re.compile(r"(.*?)(?:_\d+)?(?:_\d+)?\..*")

    for md_file in md_files:
        base_name = pattern.match(os.path.basename(md_file))
        if base_name:
            file_groups[base_name.group(1)].append(md_file)

    # 合并文件内容并删除原文件
    for base_name, files in file_groups.items():
        if len(files) > 1:  # 只处理有多个切分文件的情况
            files.sort()  # 按文件名排序，确保顺序正确
            merged_content = []
            for file in files:
                merged_content.extend(read_md_file(file))

            new_file_name = os.path.join(os.path.dirname(files[0]), f"{base_name}.md")
            with open(new_file_name, 'w', encoding='utf-8') as new_file:
                new_file.writelines(merged_content)

            # 删除原文件
            for file in files:
                os.remove(file)

# 使用示例
# merge_md_files('path_to_your_folder')


# 使用示例
merge_md_files('./pages/langsmith/')
