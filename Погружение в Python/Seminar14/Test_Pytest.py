import pytest
from Task import *


@pytest.fixture()
def matrix1():
    return Matrix([[1, 2], [3, 4]])


@pytest.fixture()
def matrix2():
    return Matrix([[5, 6], [7, 8]])


def test_create_empty_matrix():
    with pytest.raises(MatricesEmpty):
        Matrix([])


def test_create_broken_matrix():
    with pytest.raises(IncorrectMatrixSize):
        Matrix([[1, 2], [3, 4, 3]])


def test_matrix_equality(matrix1, matrix2):
    matrix3 = Matrix([[1, 2], [3, 4]])
    assert matrix1 != matrix2
    assert matrix3 == matrix1


def test_matrix_addition(matrix1, matrix2):
    result_add = matrix1 + matrix2
    assert result_add == [[6, 8], [10, 12]]


def test_matrix_multiplication(matrix1, matrix2):
    result_mul = matrix1 * matrix2
    assert result_mul == [[19, 22], [43, 50]]


if __name__ == "__main__":
    pytest.main(["-v"])
