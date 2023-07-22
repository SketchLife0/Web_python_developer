# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

def is_number(s):
    """Проверка является ли строка числом с учётом знака"""
    try:
        int(s)
        return True
    except ValueError:
        return False


def input_fraction() -> tuple:
    """Получить строку формата дроби"""
    while True:
        inp = input("Введите дробь в формате а/b: ").split("/")
        if len(inp) == 2:
            a, b = inp
            if is_number(a) and is_number(b):
                print("Принято!")
                return int(a), int(b)


def simplify_fraction(x, y):
    """Сокращение дроби"""
    d = gcd(x, y)
    return x // d, y // d


def sum_fractions(x1: int, y1: int, x2: int, y2: int) -> tuple:
    """Сумма дробей"""
    if y1 != y2:
        lcm = y1 * y2 // gcd(y1, y2)
        x1 *= lcm // y1
        x2 *= lcm // y2
        y1 = lcm
    x = x1 + x2
    return simplify_fraction(x, y1)


def product_fractions(x1: int, y1: int, x2: int, y2: int) -> tuple:
    """Произведение дробей"""
    x = x1 * x2 // gcd(x1, x2)
    y = y1 * y2 // gcd(y1, y2)
    return simplify_fraction(x, y)


def gcd(a, b):
    """Нахождение найбольшего общего знаменателя"""
    while b != 0:
        a, b = b, a % b
    return a


x1, y1 = input_fraction()
x2, y2 = input_fraction()
x_sum, y_sum = sum_fractions(x1, y1, x2, y2)
print(f"Сумма дробей равна {x_sum}/{y_sum}")
x_product, y_product = product_fractions(x1, y1, x2, y2)
print(f"Произведение дробей равно {x_product}/{y_product}")
