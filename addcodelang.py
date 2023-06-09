import os
import re

def process_markdown_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    line_indices_to_change = []
    for index, line in enumerate(lines):
        if line.strip().startswith("```"):
            line_indices_to_change.append(index)

    # 删除偶数索引的项，只保留奇数索引的项
    line_indices_to_change = line_indices_to_change[::2]

    # 替换要修改的行
    for index in line_indices_to_change:
        lines[index] = "```python\n"

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)

# 您可以替换为 Markdown 文件或 Markdown 文件集所在的目录。
file_dir = "./pages/use_cases"
default_language = "python"

for root, dirs, files in os.walk(file_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            process_markdown_lines(filepath)