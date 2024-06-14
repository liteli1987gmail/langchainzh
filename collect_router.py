import os
import json

def collect_meta_files(root_dir):
    aggregated_meta = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        meta_path = os.path.join(dirpath, '_meta.json')
        if os.path.exists(meta_path):
            with open(meta_path, 'r', encoding='utf-8') as meta_file:
                meta_content = json.load(meta_file)
                aggregated_meta.update(meta_content)
    return aggregated_meta

def save_aggregated_meta(aggregated_meta, output_path):
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(aggregated_meta, output_file, ensure_ascii=False, indent=2)
    print(f"Aggregated meta content saved to {output_path}")

folders = 'langsmith'
root_directory = './pages/'+ folders # Replace with your root directory
output_file_path = folders+ '_meta.json'  # Path to save the aggregated meta content

aggregated_meta = collect_meta_files(root_directory)
save_aggregated_meta(aggregated_meta, output_file_path)
