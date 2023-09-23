import unittest
import doctest
from Task import *


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite("doc_file.txt"))
    return tests


class TestTask(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix1 = Matrix([[1, 2], [3, 4]])
        self.matrix2 = Matrix([[5, 6], [7, 8]])

    def test_create_empty_matrix(self):
        self.assertRaises(MatricesEmpty, Matrix, [])

    def test_create_broken_matrix(self):
        self.assertRaises(IncorrectMatrixSize, Matrix, [[1, 2], [3, 4, 3]])

    def test_matrix_equality(self):
        matrix3 = Matrix([[1, 2], [3, 4]])
        self.assertFalse(self.matrix1 == self.matrix2)
        self.assertTrue(matrix3 == self.matrix1)

    def test_matrix_addition(self):
        result_add = self.matrix1 + self.matrix2
        self.assertEqual(result_add, [[6, 8], [10, 12]])

    def test_matrix_multiplication(self):
        result_mul = self.matrix1 * self.matrix2
        self.assertEqual(result_mul, [[19, 22], [43, 50]])


if __name__ == "_main__":
    # Не понимаю почему нет подробного вывода если нет ошибок как в лекции
    unittest.main(verbosity=2)
