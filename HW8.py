# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
#
# -   Для дочерних объектов указывайте родительскую директорию.
# -   Для каждого объекта укажите файл это или директория.
# -   Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
# с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle
from pathlib import Path


def dir_size(path='.') -> int:
    result = 0
    with os.scandir(path) as it:
        for i in it:
            if i.is_file():
                result += i.stat().st_size
            elif i.is_dir():
                result += dir_size(i.path)
    return result

def item_size(path='.') -> int:
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return dir_size(path)


def dir_scan(direct: Path):
    json_data = {}
    fieldnames = ['name', 'path', 'size', 'file_or_dir']
    rows = []
    with open('direct_info.json', 'w') as f_json, \
            open('direct_info.csv', 'w', newline='', encoding='utf-8') as f_csv,\
            open('direct_info.pickle', 'wb') as f_pickle:
        for dir_path, dir_name, file_name in os.walk(direct):
            json_data.setdefault(dir_path, {})
            for item in dir_name:
                size = item_size(dir_path + '/' + item)
                json_data[dir_path].update({item: {'size': size, 'file_or_dir': 'directory'}})
                rows.append({'name': item, 'path': dir_path, 'size': size, 'file_or_dir': 'directory'})
            for item in file_name:
                size = item_size(dir_path + '/' + item)
                json_data[dir_path].update({item: {'size': size, 'file_or_dir': 'file'}})
                rows.append({'name': item, 'path': dir_path, 'size': size, 'file_or_dir': 'file'})

        json.dump(json_data, f_json, indent=2)
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        pickle.dump(f'{pickle.dumps(json_data)}', f_pickle)


dir_scan(Path('C:\PycharmProjects'))
