# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

from UserExceptions import *
import logging


class Matrix:


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
            logger.info(f'Матрица инициализирована с размерами {matrix}')
            self.matrix = matrix
        else:
            logger.critical('Размеры вложенных списков не совпадают. Матрица не может быть создана.')
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


def parse_matrix(matrix_string):
    rows = matrix_string.strip().split(';')  # Разбиваем входную строку по точкам с запятой
    matrix = []
    for row in rows:
        try:
            row_values = [int(val) for val in row.split(',')]  # Разбиваем строку по запятым и преобразуем в целые числа
        except ValueError:
            logger.critical("ValueError: invalid literal for int()")
            exit()
        else:
            matrix.append(row_values)
    return matrix


if __name__ == "__main__":
    FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
            'в строке {lineno:03d} функция "{funcName}()" ' \
            'в {created} секунд записала сообщение: {msg}'
    logging.basicConfig(format=FORMAT, style='{', filename='project.log.', filemode='a', encoding='utf-8', level=logging.NOTSET)
    logger = logging.getLogger(__name__)

    logger.info('Старт работы')

    import argparse
    parser = argparse.ArgumentParser(description="Create matrix")
    parser.add_argument('matrix_string', type=str, help="Матрица в виде строки, например, '1,2,3;4,5,6;7,8,9'")
    args = parser.parse_args()
    matrix = parse_matrix(args.matrix_string)
    m = Matrix(matrix)
    print("Матрица успешно инициализирована:")
    print(m)

    logger.info("Программа успешно завершила работу")

