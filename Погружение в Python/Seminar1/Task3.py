# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def input_number() -> int:
    number = input(f"Введите число от 0 до 100000: ").strip()
    while True:
        if number.isdigit() and 0 < int(number) < 100000:
            return int(number)
        else:
            number = input("Некоректный ввод. Введите число от 0 до 100000: ").strip()


def simplicity_check(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


a = input_number()
if simplicity_check(a):
    print("Это простое число")
else:
    print("Это не простое число")