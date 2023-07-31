# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def rewarding(names: list[str], salaries: list[int], bonus: list[str]) -> dict | str:
    try:
        original_size = len(names)
        names = [s for s in names if s.isalpha()]
        if original_size != len(names):
            raise ValueError
        if len(names) > 0 and len(names) == len(salaries) == len(bonus):
            return {names[i]: salaries[i] / 100 * float(bonus[i].rstrip('%')) for i in range(len(names))}
        else:
            raise IndexError
    except (AttributeError, ValueError, TypeError):
        return "Ошибка: Неверный формат данных"
    except IndexError:
        return "Ошибка: Неправильный размер списков"


# Ну или просто
# def rewarding(names: list[str], salaries: list[int], bonus: list[str]) -> dict | str:
#     return {names[i]: salaries[i] * float(bonus[i].rstrip('%')) / 100 for i in range(len(names))}


if __name__ == "__main__":
    print(rewarding(["asd", "Сергей", "Иван"], [424242, 12300, 200250], ["51", "123", "12.2%"]))
    print(rewarding(["123d", "Сергей", "Иван"], [424242, 12300, 200250], ["51", "123", "12.2%"]))
    print(rewarding(["asd", "Сергей", "Иван"], [12300, 200250], ["51", "123", "12.2%"]))
    print(rewarding([], [424242, 12300, 200250], ["51", "123", "12.2%"]))
    print(rewarding(["Сергей", "Иван"], [424242, 12300, 200250], ["51", "123", "12.2%"]))
