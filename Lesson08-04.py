import csv
import json
from pathlib import Path


def csv_to_json(csv_file: Path, json_file: Path) -> None:
    json_list = []
    with open(csv_file, 'r', encoding='utf-8', newline='') as f:
        csv_read = csv.reader(f, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            json_dict = {}
            if i != 0:
                level, id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f'{int(id):010}'
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f"{json_dict['id']}{json_dict['name']}")
                json_list.append(json_dict)

    with open(json_file, 'w', newline='', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2)


if __name__ == '__main__':
    CSV_PATH = ''
    JSON_PATH = ''
    csv_to_json(Path(CSV_PATH), Path(JSON_PATH))
