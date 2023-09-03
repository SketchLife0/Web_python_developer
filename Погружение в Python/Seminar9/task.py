# equation_roots: Нахождение корней квадратного уравнения
# generate_csv: Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# @bulk_search: Декоратор, запускающий нахождение корней квадратного уравнения с каждой тройкой чисел из csv файла.
# @repeat_in_json: Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
import random
from typing import Callable


def repeat_to_json(name):
    def dec_repeat_to_json(func: Callable):
        def generate_json(*args, **kwargs):
            data = func(*args, **kwargs)
            with open(name, "w", encoding="UTF-8") as json_file:
                json.dump(data, json_file, indent="\t", ensure_ascii=False)
        return generate_json
    return dec_repeat_to_json


def bulk_search(func: Callable):
    data = {}

    def roots_from_csv(*args):
        if len(args) == 0:
            with open('example.csv', 'r', encoding='UTF-8') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    try:
                        a, b, c = int(row[0]), int(row[1]), int(row[2])
                        result = func(a, b, c)
                        data[f"{a},{b},{c}"] = result
                        print(f"Для элементов {a, b, c} корни будут равны {result}")
                    except (ValueError, IndexError):
                        continue
        elif len(args) == 3:
            result = func(*args)
            data[f"{args}"] = result
            print(f"Для элементов {args} корни будут равны {result}")
        else:
            print("Ошибка")
        return data
    return roots_from_csv


@repeat_to_json('example.json')
@bulk_search
def equation_roots(a: float, b: float, c: float) -> [float]:
    """
    Нахождение корней квадратного уравнения
    :return: Список корней
    """
    result = []
    if a == 0 or b == 0:
        return result
    d = b**2 - 4*a*c
    if d > 0:
        result.append((-b + d ** 0.5)/(2*a))
        result.append((-b - d ** 0.5)/(2*a))
    elif d == 0:
        result.append(-b / (2*a))
    return result


def generate_csv(filename, size):
    with open(filename, "w", encoding="UTF-8") as f:
        fieldnames = ["a", "b", "c"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        data = []
        for _ in range(size):
            row = {"a": random.randint(-10, 10), "b": random.randint(-10, 10), "c": random.randint(-10, 10)}
            data.append(row)
        writer.writerows(data)


if __name__ == "__main__":
    generate_csv("example.csv", 1000)
    equation_roots()
