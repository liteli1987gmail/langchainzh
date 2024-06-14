import os
import json

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def generate_meta_content(dir_path):
    meta_content = {}
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        item_name, item_ext = os.path.splitext(item)
        if os.path.isdir(item_path):
            key = item
            value = f"{item}（{to_camel_case(item)}）"
        elif item_ext in ['.md', '.mdx']:
            key = item_name
            value = f"{item_name}（{to_camel_case(item_name)}）"
        else:
            continue
        meta_content[key] = value
    return meta_content

def create_meta_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        meta_path = os.path.join(dirpath, '_meta.json')
        if os.path.exists(meta_path):
            print(f"Skipping existing _meta.json in {dirpath}")
            continue
        meta_content = generate_meta_content(dirpath)
        with open(meta_path, 'w', encoding='utf-8') as meta_file:
            json.dump(meta_content, meta_file, ensure_ascii=False, indent=2)
        print(f"Created _meta.json in {dirpath}")



root_directory = './pages/langsmith/'  # Replace with your root directory
create_meta_files(root_directory)
