""" Задание №4
    📌 Создайте модуль с функцией внутри.
    📌 Функция получает на вход загадку, список с возможными вариантами
       отгадок и количество попыток на угадывание.
    📌 Программа возвращает номер попытки, с которой была отгадана загадка
       или ноль, если попытки исчерпаны."""


def zagadka(sagadka: str, answers: list, count: int = 5):
    print(f'Загадка - {sagadka}')
    try_ = 1

    while count:
        user_answer = input('Ваш ответ: ').lower()

        if user_answer in answers:
            return try_
        else:
            print('попробуйте снова')
        try_ += 1
        count -= 1

    return 0
