# Создайте класс Матрица.
# Добавьте методы для: - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц

class Matrix:
    @staticmethod
    def __are_nested_lists_equal_size(lst):
        if not lst:
            return True  # Пустой список считается равного размера

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
            raise ValueError("Размеры вложенных списков не совпадают. Матрица не может быть создана.")

    def __str__(self):
        return str(self.matrix)

    def __eq__(self, other):
        # Если сами матрицы или их строки разной длины относительно друг друга, то False
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return False

        # Если обе матрицы пусты - True
        if not len(self.matrix) and not len(other.matrix):
            return True

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return None

        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] + other.matrix[i][j])
        return result

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            return None

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
    a = Matrix([[1, 2],
                [2, 3],
                [3, 4]])
    b = Matrix([[1, 2, 3],
                [2, 8, 4]])
    print(a)
    print(b)
    print(a == b)
    print(a + b)
    print(a * b)

