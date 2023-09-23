class IncorrectMatrixSize(Exception):
    def __str__(self):
        return "Размеры вложенных списков не совпадают. Матрица не может быть создана."


class MatricesOfDifferentSizes(Exception):
    def __str__(self):
        return "Матрицы неподходящего размера"


class MatricesEmpty(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == 1:
            return "Матрица пуста"
        else:
            return "Матрицы пусты"

