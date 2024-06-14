import os
import json

def load_translated_meta(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def update_meta_file(meta_file_path, translated_meta):
    with open(meta_file_path, 'r', encoding='utf-8') as file:
        current_meta = json.load(file)

    updated_meta = {key: translated_meta.get(key, value) for key, value in current_meta.items()}

    with open(meta_file_path, 'w', encoding='utf-8') as file:
        json.dump(updated_meta, file, ensure_ascii=False, indent=2)

def update_all_meta_files(root_dir, translated_meta):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        meta_file_path = os.path.join(dirpath, '_meta.json')
        if os.path.exists(meta_file_path):
            update_meta_file(meta_file_path, translated_meta)
            print(f"Updated _meta.json in {dirpath}")


folders = 'expression_language'
root_directory = './pages/'+ folders # Replace with your root directory
translated_meta_file = './aggregated_meta.json'  # Path to the translated meta JSON file

# Load the translated meta content
translated_meta = load_translated_meta(translated_meta_file)

# Update all _meta.json files in the specified directory
update_all_meta_files(root_directory, translated_meta)
