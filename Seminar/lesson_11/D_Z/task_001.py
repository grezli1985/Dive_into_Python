""" 📌 Создайте класс Матрица. Добавьте методы для:
    ○ вывода на печать,
    ○ сравнения,
    ○ сложения,
    ○ *умножения матриц"""


class Matrix:
    """Класс матрица. Действия сложение, вычитание, умножение, сравнение."""

    def __init__(self, rows: int = 2, cols: int = 2, init_value: int = 0, *, matrix: list[list[int]] = None):
        """Инициализация матрицы"""
        if matrix is None:
            self.__matrix = []
            for _ in range(rows):
                self.__matrix.append([init_value for _ in range(cols)])
        else:
            rows = len(matrix)
            cols = len(matrix[0])
            self.__matrix = matrix

        self.__cols = cols
        self.__rows = rows

    def __add__(self, other):
        """Сложение матриц. Одной размерности."""
        if self.__rows != other.__rows or self.__cols != other.__cols:
            return None

        result = Matrix(self.__rows, self.__cols)
        for i in range(result.__rows):
            for j in range(result.__cols):
                result.__matrix[i][j] = self.__matrix[i][j] + other.__matrix[i][j]

        return result

    def __sub__(self, other):
        """Вычитание матриц. Одной размерности."""
        if self.__rows != other.__rows or self.__cols != other.__cols:
            return None

        result = Matrix(self.__rows, self.__cols)
        for i in range(result.__rows):
            for j in range(result.__cols):
                result.__matrix[i][j] = self.__matrix[i][j] - other.__matrix[i][j]

        return result

    def __str__(self):
        """Вывод матрицы на печать."""
        result = []
        for row in self.__matrix:
            for val in row:
                result.append(f"{val:2}\t")
            result.append("\n")
        return "".join(result)

    def __repr__(self):
        """Отображение матрицы."""
        return f"Matrix(matrix={self.__matrix})"

    def __eq__(self, other):
        """Сравнение матриц."""
        result = True
        if self.__rows != other.__rows or self.__cols != other.__cols:
            result = False
        else:
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if self.__matrix[i][j] != other.__matrix[i][j]:
                        result = False
                        break
                if not result:
                    break

        return result

    def __mul__(self, other):
        """Умножение матриц."""
        if self.__cols != other.__rows:
            return None

        result = Matrix(self.__rows, other.__cols)
        for i in range(result.__rows):
            for j in range(result.__cols):
                for k in range(result.__cols):
                    result.__matrix[i][j] = self.__matrix[i][k] * other.__matrix[j][k]

        return result


if __name__ == '__main__':
    matrix_1 = Matrix(matrix=[[2, 3, 8], [4, 6, 9], [5, 7, 1]])
    matrix_2 = Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])

    print("Матрица 1")
    print(matrix_1)
    print("Матрица 2")
    print(matrix_2)
    print(f"{matrix_1 = }")
    print(f"{matrix_2 = }")

    matrix_3 = matrix_1 + matrix_2
    matrix_4 = matrix_1 - matrix_2

    print("Сложение matrix_1 + matrix_2")
    print(matrix_3)
    print("Вычитание matrix_1 - matrix_2")
    print(matrix_4)

    print(f"Сравнение matrix_1 == matrix_1 - {matrix_1 == matrix_1}")
    print(f"Сравнение matrix_1 == matrix_2 - {matrix_1 == matrix_2}")

    matrix_5 = Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])
    matrix_6 = Matrix(matrix=[[4, 8], [1, 5], [2, 3]])
    matrix_7 = Matrix(matrix=[[4, 2, 8], [7, 1, 5]])

    print("Матрица 5")
    print(matrix_5)
    print("Матрица 6")
    print(matrix_6)

    print("matrix_1 * matrix_5")
    print(matrix_1 * matrix_5)
    print("matrix_1 * matrix_6")
    print(matrix_1 * matrix_6)
