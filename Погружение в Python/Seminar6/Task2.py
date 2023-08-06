# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# from datetime import datetime
import sys


# def is_valid_date(date_string: str) -> bool:
#     try:
#         datetime.strptime(date_string, '%d.%m.%Y')
#         return True
#     except ValueError:
#         return False
#
#
# def is_date(date_string: str) -> bool:
#     if is_valid_date(date_string):
#         print("Введенная строка является датой.")
#     else:
#         print("Введенная строка не является датой или некорректный формат.")


def is_date(date_string: str) -> bool:
    try:
        day, month, year = map(int, date_string.split("."))
        if not (0 < day < 32 and 0 < month < 13 and year > 0):
            raise ValueError("Неверный формат")
        days_in_month = [31, 28 + int(leap_year(year)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return day <= days_in_month[month - 1]
    except (ValueError, IndexError):
        return False


def leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    print(is_date(sys.argv[1]))
