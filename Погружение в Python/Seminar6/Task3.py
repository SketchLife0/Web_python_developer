# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random as r


def zeroing():
    return [[0 for _ in range(8)] for _ in range(8)]


def position_setting(chess: int):
    result = 0
    empty_positions = [(x, y) for x in range(8) for y in range(8)]
    while result < chess and empty_positions:
        x, y = r.choice(empty_positions)
        _CHESSBOARD[x][y] = 1
        result += 1
        empty_positions.remove((x, y))


def attack_check(position: [int, int]) -> bool:
    x, y = position
    for i in range(8):
        if _CHESSBOARD[x][i] == 1 and i != y:
            return True
        if _CHESSBOARD[i][y] == 1 and i != x:
            return True
    for i in range(8):
        for j in range(8):
            if (i != x or j != y) and (abs(x - i) == abs(y - j) and _CHESSBOARD[i][j] == 1):
                return True
    return False


def world_peace():
    for i in range(len(_CHESSBOARD)):
        for j in range(len(_CHESSBOARD[i])):
            if _CHESSBOARD[i][j] == 1 and attack_check([i, j]):
                return False
    return True


def search_peace(variable: int, chess: int) -> list:
    global _CHESSBOARD
    result = []
    step = 0
    while step < variable:
        position_setting(chess)
        if world_peace():
            result.append([pos[:] for pos in _CHESSBOARD])
            step += 1
        else:
            _CHESSBOARD = zeroing()
    return result


_CHESSBOARD = zeroing()
if __name__ == "__main__":
    # position_setting(8)
    # print(*_CHESSBOARD, sep="\n")
    # if world_peace():
    #     print("Мир да благодать")
    # else:
    #     print("Идёт война")

    # _CHESSBOARD[0][0] = 1
    # _CHESSBOARD[6][1] = 1
    # _CHESSBOARD[4][2] = 1
    # _CHESSBOARD[7][3] = 1
    # _CHESSBOARD[1][4] = 1
    # _CHESSBOARD[3][5] = 1
    # _CHESSBOARD[5][6] = 1
    # _CHESSBOARD[2][7] = 1
    print(*search_peace(1, 8), sep='\n')
# Короче оно работает. И вроде как даже правильно. Но из-за того что позиции выбираются случайно то
# 8 ферзей это колоссальное время даже на 1 проход
