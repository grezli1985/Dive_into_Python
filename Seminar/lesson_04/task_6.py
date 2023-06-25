""" Задание №6 """

""" ✔ Функция получает на вход список чисел и два индекса.
    ✔ Вернуть сумму чисел между между переданными индексами.
    ✔ Если индекс выходит за пределы списка, сумма считается
      до конца и/или начала списка."""


def sum_nums(list_numbers, start, end):
    if start < 0:
        start = 0
    if start > len(list_numbers):
        return None

    return sum(list_numbers[start + 1:end])


print(sum_nums([1, 33, 0, -345, 9], 4, 15))
