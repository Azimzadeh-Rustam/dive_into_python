from os import chdir
from pathlib import Path


def sort_files(path: str | Path, groups: dict[Path, list[str]] = None) -> None:
    chdir(path)
    if groups is None:
        groups = {
            Path('video'): ['mp4', 'avi', 'mkv', 'mov'],
            Path('image'): ['jpeg', 'jpg', 'png', 'gif'],
            Path('music'): ['mp3', 'wav', 'flac', 'm4a'],
            Path('text'): ['txt', 'doc']
        }

    reverse_groups = {}
    for directory, extension_list in groups.items():
        if not directory.is_dir():
            directory.mkdir()
        for extentions in extension_list:
            reverse_groups[f'.{extentions}'] = directory
    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)


if __name__ == '__main__':
    file_path = ''
    sort_files(Path(file_path))