""" Задание №2
📌 Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите
код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг
друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара
бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от
1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если
бьют - ложь."""

""" проверка горизонтальная, вертикальная и диагональная 
# [(0, 3), (1, 4), (2, 0), (3, 4), (4, 5), (5, 7), (6, 1), (7, 0)]
n = 8
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            return False

в остальных случиях True """
import numpy as np
import random as rnd


matrix = np.full((8, 8), 1)
# print(matrix)

result = ([])
for i in range(8):
    result.append((i, rnd.randint(0, 8 - 1)))
# for x, y in result:
#     print(x, y)
print(result)   # [(0, 3), (1, 4), (2, 0), (3, 4), (4, 5), (5, 7), (6, 1), (7, 0)]

# coor = input()
board = [['.'] * 8 for _ in range(8)]
# x = ord(x) - 97
# y = n - int(y)
y = [y for x, y in result]
x = [x for x, y in result]
print(f'x = {x}')
print(f'y = {y}')
# for i in range(8):
#     for j in range(8):
#         if (y == i) or (x == j) or abs(y - i) == abs(x - j):
#             board[i][j] = '*'
# board[y][x] = 'Q'
# for line in board:
#     print(*line)

#
n = 8
# x = []
# y = []
print(x, y)
# for i in range(n):
#     new_x, new_y = [int(s) for s in input().split()]
x.append(x)
y.append(y)
#
correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')


# def make_row(rowdata, col, empty, full):
#     items = [col] * (2 * len(rowdata) + 1)
#     items[1::2] = (full if d else empty for d in rowdata)
#     return ''.join(items)
#
#
# def make_board(queens, col="|", row="---", empty="   ", full=" X "):
#     size = len(queens)
#     bar = make_row(queens, col, row, row)
#     board = [bar] * (2 * size + 1)
#     board[1::2] = (make_row([i == q for i in range(size)], col, empty, full) for q in queens)
#     return '\n'.join(board)


# queens = [0, 2, 6, 4, 7, 1, 5, 3]
# print(make_board(queens))


# n = 8
# x = []
# y = []
# for i in range(n):
#     new_x, new_y = [int(s) for s in input().split()]
#     x.append(new_x)
#     y.append(new_y)
#
# correct = True
# for i in range(n):
#     for j in range(i + 1, n):
#         if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
#             correct = False
#
# if correct:
#     print('NO')
# else:
#     print('YES')
