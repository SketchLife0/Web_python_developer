# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
# Дополнительное:
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# * Какие вещи взяли все три друга
# * Какие вещи уникальны, есть только у одного друга
# * Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# * Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

import random


def find_combinations(items: list, max_weight: int, result: list, current_combination=dict(), index=0):
    """
    Считает все возможные варианты вещей
    :param items: лист кортежей вещей и их вес
    :param max_weight: максимальный вес что можно взять
    :param current_combination: новый словарь вещей и веса
    :param index: индекс с какой вещи начинать
    :param result: список списков всех комбинаций
    """
    # Проверяем, если текущая комбинация веса не превышает максимальный вес
    if sum(current_combination.values()) <= max_weight:
        result.append(list(current_combination.keys()))  # Добавляем копию текущей комбинации в результат
    # Рекурсивно перебираем комбинации с добавлением и без добавления текущей вещи
    for i in range(index, len(items)):
        current_combination[items[i][0]] = items[i][1]
        find_combinations(items, max_weight, result, current_combination, i + 1)
        del current_combination[items[i][0]]  # Удаляем текущую вещь из комбинации, чтобы пробовать другие варианты


def combatorics(combo: list, max_weight):
    """Выводит все комбинации на экран"""
    for combination in combo:
        print(combination)
    print(f"Всего вариантов собрать рюкзак весом до {max_weight / 1000} кг - {len(combo)}")


def assembly(camp: dict, items: list, names: list):
    """
    Выводит кто что взял
    :param camp: словарь друзей и их вещей
    :param items: список списков всех возможные вариантов вещей
    :param names: список имён друзей
    """
    all_items = set()
    for i in range(len(names)):
        item = random.choice(items)
        all_items.update(item)
        camp[names[i]] = item
        print(f"{names[i]} взял {item}")
    print(f"Вместе они все взяли {all_items}")


def search_unique(d: dict, n: list):
    """
    Поиск уникальных элементов у человека
    :param d: словарь всех людей с их вещами
    :param n: список имён
    """
    for i in range(len(n)):
        one_person = d[n[i]]
        name_one_person = n[i]
        other_persons = set()
        for k, v in d.items():
            if n[i] != k:
                other_persons.update(v)
        unique_items = list(set(one_person) - other_persons)
        print(f"Только у {name_one_person} есть: {unique_items}")


def detached_objects(d: dict, n: list):
    """
    Поиск каких вещей нет только у одного человека
    :param d: словарь всех людей с их вещами
    :param n: список имён
    """
    items = {}
    for v in d.values():
        for elem in v:
            if elem in items:
                items[elem] += 1
            else:
                items[elem] = 1
    for i in range(len(n)):
        result = []
        one_person = d[n[i]]
        name_one_person = n[i]
        for k, v in items.items():
            if v == len(n) - 1 and k not in one_person:
                result.append(k)
        print(f"Только у {name_one_person} нет {result}")


stuff = {
    "Куртка": 1000,
    "Палатка": 2000,
    "Топор": 800,
    "Нож": 200,
    "Еда": 3000,
    "Вода": 2000,
    "Горелка": 1800,
    "Лопатка": 700,
    "Верёвка": 500,
    "Спрей": 300
}
MAX_WAIGHT = 10000
NAMES = ['Андрей', 'Cергей', "Никита", "Вася"]  # Добавьте сюда ещё одно имя и друзей станет больше
combinations = []
camping = {}
find_combinations(list(stuff.items()), MAX_WAIGHT, combinations)

# 1 Верните все возможные варианты комплектации рюкзака
combatorics(combinations, MAX_WAIGHT)

# 2 Какие вещи взяли все три друга
assembly(camping, combinations, NAMES)

# 3 Какие вещи уникальны, есть только у одного друга
search_unique(camping, NAMES)

# 4 Какие вещи есть у всех друзей кроме одного
detached_objects(camping, NAMES)
