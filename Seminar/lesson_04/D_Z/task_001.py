import numpy as np

""" Задание 1 """
""" ✔ Напишите функцию для транспонирования матрицы """

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


def transparent_matrix(mat_rix: [[int]]):
    """С помощью цикла транспонирование можно реализовать следующим образом"""
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(mat_rix)):
        for j in range(len(mat_rix[0])):
            result[j][i] = mat_rix[i][j]
    return result


"""пример транспонирования с использованием метода transpose()"""
result_1 = np.transpose(matrix)

print('\nБыло\n')
print(matrix)
print('\nСтало\n')
print(transparent_matrix(matrix))
print('\n2\n')
print(result_1)
