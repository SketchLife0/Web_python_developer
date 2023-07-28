# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь:
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def rev_kwargs(**kwargs):
    dict_kwargs = {}
    for k, v in kwargs.items():
        if not has_hash(k):
            k = str(k)
        if not has_hash(v):
            v = str(v)
        dict_kwargs.update({v: k})
    return dict_kwargs


def has_hash(s):
    try:
        hash(s)
        return True
    except TypeError:
        return False


if __name__ == "__main__":
    d = rev_kwargs(res=1, reverse=[1, 2, 3])
    print(d)
