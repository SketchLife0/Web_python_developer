# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def lists_size_check(matrix: list) -> bool:
    """
    Проверяет что все листы в листе одного размера. Пустой - ложь
    :param matrix: Матрица (лист листов)
    """
    if not matrix:
        return False
    for i in range(1, len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            return False
    return True


def matrix_flip(matrix: list):
    """
    Переворачивает матрицу
    :param matrix: Матрица (лист листов)
    """
    if lists_size_check(matrix):
        print(f"{MATRIX} -> ", end="")
        result = []
        for i in range(len(matrix[0])):
            bool_list = []
            for elem in matrix:
                bool_list.append(elem[i])
            result.append(bool_list)
        print(result)
    else:
        print(f"{MATRIX} не является матрицей")


if __name__ == "__main__":
    MATRIX = [[1, 2, 3], [4, 5, 6]]
    matrix_flip(MATRIX)
