""" Основы doctest
Инструмент doctest встроен в Python и не требует дополнительных манипуляций по
установке и настройке. Как заявляют сами разработчики языка doctest можно
использовать для следующих задач:
    ● Проверка актуальности строк документации модуля путем проверки того, что
    все интерактивные примеры по-прежнему работают в соответствии с
    документацией.
    ● Для регрессионного тестирования. Чтобы убедиться, что интерактивные
    примеры из тестового файла или тестового объекта работают должным
    образом.
    ● Позволяют написать учебную документацию для пакета, обильно
    иллюстрированную примерами ввода-вывода. В зависимости от того, что
    выделено — примеры или пояснительный текст, это может быть что-то вроде
    “грамотного тестирования” или “исполняемой документации”.

Проверка примеров в документации,
регрессионное тестирование
Как вы помните из прошлых лекций, тройные двойные кавычки сразу после
заголовка класса, функции или метода превращают текст внутри в строку
документации соответствующего объекта. Например так может выглядеть
простейшая (без оптимизации) функция, проверяющая является ли число простым
или составным используя нахождение остатка от деления."""


def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    Проверяет число P для простоты, используя нахождение
    остаток от деления в диапазоне [2, P)
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


help(is_prime)

# Запустим код в консоли в режиме интерпретатора Python

""" 
>>> from main import is_prime
Help on function is_prime in module main:
is_prime(p: int) -> bool
        Checks the number P for simplicity using finding the
remainder of the division in the range [2, P).
>>> is_prime(42)
False
>>> is_prime(73)
True

    1. Мы сразу вспомнили, что команда import запускает импортируемый файл. У
    нас сработал вызов справки, потому что мы не спрятали его в __name__ ==
    “__main__”
    2. Вызов функции в режиме интерпретатора позволяет получить ответ для
    любых значений."""
