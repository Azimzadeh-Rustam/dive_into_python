import csv
import json
from pathlib import Path


def json_to_csv(file: Path) -> None:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    list_rows = []
    for level, id_name_dict in data.items():
        for id, name in id_name_dict.items():
            list_rows.append({'level': int(level), 'id': int(id), 'name': name})

    with open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(list_rows)



if __name__ == '__main__':
    PATH = ''
    json_to_csv(Path(PATH))
