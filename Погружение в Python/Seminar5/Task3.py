# Создайте функцию генератор чисел Фибоначчи

def fibonachi_gen(elems: int):
    a, b = 0, 1
    for i in range(elems + 1):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    while True:
        num = input("Введите число: ")
        if num.isdigit():
            generator = fibonachi_gen(int(num))
            for elem in generator:
                print(elem)
