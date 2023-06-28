""" Задание №5 """
""" ✔ Напишите программу, которая выводит
    на экран числа от 1 до 100.
    ✔ При этом вместо чисел, кратных трем,
    программа должна выводить слово «Fizz»
    ✔ Вместо чисел, кратных пяти — слово «Buzz».
    ✔ Если число кратно и 3, и 5, то программа
    должна выводить слово «FizzBuzz».
    ✔ *Превратите решение в генераторное выражение."""


def fizz_buzz():
    for i in range(1, 101):
        if i % 15 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield i


# result = iter(fizz_buzz())
#
# for _ in range(101):
#     print(next(result))

print(*("FizzBuzz" if i % 15 == 0 else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 == 0 else
        i for i in range(1, 101)), sep='\n')
