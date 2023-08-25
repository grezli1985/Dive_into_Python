import pytest
from matrix import Matrix

NEW_MATRIX_SQR = Matrix(matrix=[[1, 2, 3], [3, 2, 1], [4, 5, 6]])
NEW_MATRIX_SQR_MUL_TEN_ANS = Matrix(matrix=[[10, 20, 30], [30, 20, 10], [40, 50, 60]])
NEW_MATRIX_RCT = Matrix(matrix=[[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]])
NEW_MATRIX_MUL_L = Matrix(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
NEW_MATRIX_MUL_R = Matrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
MATRIX_MUL_ANS = Matrix(matrix=[[1, 8, 21, 40], [10, 30, 56, 88], [27, 60, 99, 144]])
MATRIX_RCT_SUM_ANS = Matrix(matrix=[[2, 4, 6, 8], [8, 10, 12, 14], [16, 18, 20, 22]])


@pytest.mark.parametrize('expected, actual', [
    (NEW_MATRIX_SQR, [[1, 2, 3], [3, 2, 1], [4, 5, 6]]),
    (NEW_MATRIX_RCT, [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]), ])
def test_create_success(expected, actual):
    assert (expected == Matrix(actual))
    assert (id(expected) != id(Matrix(actual)))


@pytest.mark.parametrize('matrix_left, matrix_right, expected', [
    (NEW_MATRIX_MUL_L, NEW_MATRIX_MUL_R, MATRIX_MUL_ANS)
])
def test_matrix_mul_success(matrix_left, matrix_right, expected):
    assert (matrix_left * matrix_right == expected)


@pytest.mark.parametrize('matrix_left, number, expected', [
    (NEW_MATRIX_SQR, 10, NEW_MATRIX_SQR_MUL_TEN_ANS)
])
def test_matrix_mul_by_num_success(matrix_left, number, expected):
    assert (matrix_left * number == expected)


@pytest.mark.parametrize('matrix_left, matrix_right, expected', [
    (NEW_MATRIX_RCT, NEW_MATRIX_RCT, MATRIX_RCT_SUM_ANS)
])
def test_matrix_sum_success(matrix_left, matrix_right, expected):
    assert ((tmp := matrix_left + matrix_right) == expected)
    assert (id(tmp) != id(expected))


if __name__ == '__main__':
    pytest.main(['-v'])
