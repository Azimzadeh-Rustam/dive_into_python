import json
from pathlib import Path


def set_users(file: Path) -> None:
    u_ids = set()
    if not file.is_file():
        data = {str(i): {} for i in range(1, 7 + 1)}
    else:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for value in data.values():
            u_ids.update(value.keys())
    while True:
        name = input('Input name: ')
        if not name:
            break
        id = input("Input id: ")
        lvl = input("Input level from 1 to 7: ")
        if ~ (id in u_ids and data[lvl].get(id) is None):
            data[lvl].update({id : name})
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    PATH = ''
    set_users(Path(PATH))
