import os
import json
import csv
import pickle
from pathlib import Path


def directory_traversal(path, parent=None):
    if parent is None:
        parent = str(path.parent)

    if path.is_dir():
        item_type = 'directory'
        size = 0
        contents = []
        for item in path.iterdir():
            child_data = directory_traversal(item, parent=str(path))
            contents.append(child_data)
            size += child_data['size']
    else:
        item_type = 'file'
        size = path.stat().st_size
        contents = None

    return {
        'path': str(path),
        'parent': parent,
        'type': item_type,
        'size': size,
        'contents': contents
    }


def save_to_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def save_to_csv(data, output_path):
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Path', 'Parent', 'Type', 'Size'])
        def write_row(item):
            csv_writer.writerow([item['path'], item['parent'], item['type'], item['size']])
            if item['type'] == 'directory' and item['contents'] is not None:
                for content in item['contents']:
                    write_row(content)
        write_row(data)


def save_to_pickle(data, output_path):
    with open(output_path, 'wb') as f:
        pickle.dump(data, f)


def process_directory(root_path):
    root = Path(root_path)
    data = directory_traversal(root)
    save_to_json(data, root / 'directory_data.json')
    save_to_csv(data, root / 'directory_data.csv')
    save_to_pickle(data, root / 'directory_data.pickle')


def main():
    PATH = '/path/to/directory'
    process_directory(PATH)


if __name__ == '__main__':
    main()
