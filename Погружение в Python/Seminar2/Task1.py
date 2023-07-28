# Напишите программу банкомат
# 1. Начальная сумма равно 0
# 2. Допустимые действия: пополнить, снять, выйти
# 3. Сумма пополнения и снятия кратны 50 у.е.
# 4. Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# 5. После каждой 3 операции пополнения или снятия начисляются проценты - 3 %
# 6. Нельзя снять больше, чем на счёте
# 7. При превышении суммы в 5млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# 8. Любое действие выводит сумму денег

from datetime import datetime

balance = 0.0
"""Баланс клиента"""
operation = 0
"""Счётчик операций"""
log_operation = []
"""Логирование операций"""
PERCENT_DIVIDENDS = 3
"""Процент начислений"""
MAX_OPERATION = 3
"""Количество операций перед начислением процента"""
ACTIONS = 4
"""Количество действий программы"""
MULTIPLICITY = 50
"""Кратность выдачи денег"""
PERCENT_COMMISSION = 1.5
"""Процент комиссии"""
MIN_COMMISSION = 30
"""Минимальная единоразовая коммисия"""
MAX_COMMISSION = 600
"""Максимальная единоразовая коммисия"""
RICH_LINE = 5000000
"""Граница богатства"""
RICH_TAX = 10
"""Процент налога на богатство"""


def help_operation() -> int:
    while True:
        print("1 - Снять средства\n" +
              "2 - Посмотреть балданс\n" +
              "3 - Пополнить счёт\n" +
              "4 - Выйти")
        act = input("Выберите действие: ")
        if act.isdigit():
            a = int(act)
            if 0 < a < ACTIONS + 1:
                return a
        print("Неккоректный ввод!")


def log(act: str, money: float):
    a = {
        'Снятие': " Были сняты средства в размере ",
        "Начисление": " Были начислены средства в размере ",
        "Дивиденды": " Были начислены дивиденды в размере ",
        'Налог': " Был снят налог в размере ",
    }
    log_action = str(datetime.now()) + a[act] + str(money)
    global log_operation
    log_operation.append(log_action)


def add():
    """Пополнить счёт"""
    bullying_rich()
    a = ""
    while not a.isdigit():
        a = input("Сколько добавить: ")
    a = float(a)
    global operation, balance
    balance += round(a, 2)
    log("Начисление", round(a, 2))
    operation += 1
    add_perceint()
    balance_correcting()
    show_money()


def balance_correcting():
    """Корректировка баланса из-за кривого float"""
    global balance
    balance = round(balance, 2)


def add_perceint():
    """Начисление процентов"""
    global operation, balance
    if operation == MAX_OPERATION:
        dividends = round(balance/100 * PERCENT_DIVIDENDS, 2)
        balance += dividends
        log("Дивиденды", dividends)
        balance_correcting()
        print(f"Начисляется процент на остаток по счёте в размере {PERCENT_DIVIDENDS}%. Это составляет {dividends}")
        operation = 0


def bullying_rich():
    """Начисление налога на богатство"""
    global balance
    if balance > RICH_LINE:
        tax = round(balance / 100 * RICH_TAX, 2)
        balance -= tax
        log('Налог', tax)
        balance_correcting()
        print(f"Взымается налог на богатство - {RICH_TAX}%. Это составляет {tax}")
        show_money()


def show_money():
    """Вывести баланс на экран"""
    print(f"Остаток на счёте составляет: {balance}")


def drop():
    """Снять деньги со счёта"""
    bullying_rich()
    print(f"Комиссия за снятие - {PERCENT_COMMISSION}%\n" +
          f"Минимальная комиссия - {MIN_COMMISSION}\n" +
          f"Максимальная комиссия - {MAX_COMMISSION}")
    a = ""
    while not (a.isdigit() and float(a) != 0 and float(a)% MULTIPLICITY == 0):
        a = input(f"Введите сумму к снятию (кратную {MULTIPLICITY}): ")
    a = float(a)
    preliminary_commission = round(a / 100 * PERCENT_COMMISSION, 2)
    if MIN_COMMISSION < preliminary_commission < MAX_COMMISSION:
        a += preliminary_commission
    elif MIN_COMMISSION > preliminary_commission:
        a += MIN_COMMISSION
    else:
        a += MAX_COMMISSION
    print(f"Сумма к снятию с учётом коммисии: {a}")
    global balance, operation
    if balance > a:
        operation += 1
        balance -= round(a, 2)
        log('Снятие', a)
        print("Деньги выданы")
        add_perceint()
        balance_correcting()
    else:
        print("Недостаточно средств")
    show_money()


print("Добрый день!")
while True:
    action = help_operation()
    match action:
        case 1:
            drop()
        case 2:
            show_money()
        case 3:
            add()
        case 4:
            exit()
