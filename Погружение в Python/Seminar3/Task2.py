# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# (Может помочь метод translate из модуля string)

import operator


def remove_digits(input_string: str) -> str:
    # Создаем таблицу перевода, в которой все цифры заменяются на None (удаляются)
    translation_table = str.maketrans('', '', '0123456789,./?<>{}[]`~!@#$%^&*()_-+=;:'"\|—")
    # Применяем таблицу перевода к строке и возвращаем результат
    return input_string.translate(translation_table)


def string_conversion(input_string: str) -> list:
    input_string = input_string.upper()
    input_string = remove_digits(input_string)
    ls = input_string.split(" ")
    ls = [x for x in ls if x.strip() != '']
    return ls


result = {}
FILE_NAME = "pancakes.txt"

with open(FILE_NAME, "r", encoding="UTF-8") as f:
    for line in f:
        st = string_conversion(line)
        for elem in st:
            value = result.get(elem, None)
            if value:
                result[elem] += 1
            else:
                result[elem] = 1

result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
for elem in result[:10]:
    print(elem)
