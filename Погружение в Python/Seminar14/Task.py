from UserExceptions import *


class Matrix:
    """
    Класс для работы с матрицами.

    Args:
        matrix (list[list[int]]): Двумерный список, представляющий матрицу.

    Example:
        >>> matrix1 = Matrix([])
        Traceback (most recent call last):
        ...
        UserExceptions.MatricesEmpty: Матрица пуста

        >>> matrix1 = Matrix([[1, 2], [3, 4, 3]])
        Traceback (most recent call last):
        ...
        UserExceptions.IncorrectMatrixSize: Размеры вложенных списков не совпадают. Матрица не может быть создана.

        >>> matrix1 = Matrix([[1, 2], [3, 4]])
        >>> print(matrix1)
        [[1, 2], [3, 4]]

        >>> matrix2 = Matrix([[5, 6], [7, 8]])
        >>> print(matrix2)
        [[5, 6], [7, 8]]

        >>> matrix1 == matrix2
        False

        >>> matrix3 = Matrix([[1, 2], [3, 4]])
        >>> matrix3 == matrix1
        True

        >>> result_add = matrix1 + matrix2
        >>> result_add
        [[6, 8], [10, 12]]

        >>> result_mul = matrix1 * matrix2
        >>> result_mul
        [[19, 22], [43, 50]]
    """

    @staticmethod
    def __are_nested_lists_equal_size(lst):
        if not lst:
            raise MatricesEmpty(1)

        # Получите длину первого вложенного списка
        first_len = len(lst[0])

        # Проверьте длину всех остальных вложенных списков
        for sub_lst in lst[1:]:
            if len(sub_lst) != first_len:
                return False  # Если длины разные, вернуть False

        return True  # Если все длины равны, вернуть True

    def __init__(self, matrix: [[int]]):
        if self.__are_nested_lists_equal_size(matrix):
            self.matrix = matrix
        else:
            raise IncorrectMatrixSize

    def __str__(self):
        return str(self.matrix)

    def __eq__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise MatricesOfDifferentSizes

        if not len(self.matrix) and not len(other.matrix):
            raise MatricesEmpty(2)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise MatricesOfDifferentSizes

        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] + other.matrix[i][j])
        return result

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise MatricesOfDifferentSizes

        result = []
        for i in range(len(self.matrix)):
            result_row = []
            for j in range(len(other.matrix[0])):
                cell = 0
                for k in range(len(self.matrix[0])):
                    cell += self.matrix[i][k] * other.matrix[k][j]
                result_row.append(cell)
            result.append(result_row)
        return result


if __name__ == "__main__":
    import doctest
    # doctest.testmod(verbose=True)
    doctest.testfile("doc_file.txt", verbose=True)

