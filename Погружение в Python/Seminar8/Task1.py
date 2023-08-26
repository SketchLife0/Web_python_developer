# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.


import os
import json
import pickle
import csv
import pprint


def format_adaptation(directory: str) -> list:
    data = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            dir_info = {
                "name": dirname,
                "parent": os.path.basename(dirpath),
                "type": "directory",
            }
            dir_size = get_folder_size(os.path.join(dirpath, dirname))
            dir_info["size"] = dir_size
            data.append(dir_info)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_info = {
                "name": filename,
                "parent": os.path.basename(dirpath),
                "type": "file",
                "size": os.path.getsize(file_path)
            }
            data.append(file_info)
    return data


def get_folder_size(folder_path: str) -> int:
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size


def save_to_file(type, data, filename):
    file_type = {
        "csv": save_to_csv,
        "json": save_to_json,
        "pickle": save_to_pickle,
    }
    try:
        func = file_type[type]
        func(data, filename)
    except KeyError:
        print("Формат не найден")


def save_to_json(data, filename):
    with open(filename, "w", encoding="UTF-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def save_to_pickle(data, filename):
    with open(filename, "wb") as pickle_file:
        pickle.dump(data, pickle_file)


def save_to_csv(data, filename):
    with open(filename, "w", encoding="UTF-8") as csv_file:
        fieldnames = ["name", "parent", "type", "size"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    data = format_adaptation(os.getcwd())
    pprint.pprint(data)
    save_to_file("csv", data, "output.csv")
    save_to_file("json", data, "output.json")
    save_to_file("pickle", data, "output.pkl")
