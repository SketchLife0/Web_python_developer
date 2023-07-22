# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def add_num_in_str16(r: str, inp: str) -> str:
    match inp:
        case "10":
            inp = "a"
        case "11":
            inp = "b"
        case "12":
            inp = "c"
        case "13":
            inp = "d"
        case "14":
            inp = "e"
        case "15":
            inp = "f"
    r += inp
    return r


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


result = ""
boolean = ""
while True:
    a = input("Введите число: ")
    if is_number(a):
        a = int(a)
        break
print(hex(a))
if a < 0:
    result += "-"
    a *= -1
while True:
    if a > 15:
        a, b = divmod(a, 16)
        boolean = add_num_in_str16(boolean, str(b))
    else:
        boolean = add_num_in_str16(boolean, str(a))
        break
for i in range(len(boolean) - 1, -1, -1):
    result += boolean[i]
print(result)
