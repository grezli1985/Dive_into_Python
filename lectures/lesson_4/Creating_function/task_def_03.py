""" Аргументы функции """
""" Рассмотрим функцию с параметрами, т.е. принимающую на вход значения.
Вспомним как в школе решали квадратные уравнения. Заодно разберём
особенности создания функций в Python."""


def quadratic_equations(a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | str:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return 'Нет решений'


print(quadratic_equations(2, -3, -9))       # (3.0, -1.5)

""" Во первых воспользовались аннотацией типов. Указали, что на вход ожидаем три
значения целого или вещественного типа. Далее после стрелки указано, что
функция может вернуть кортеж с парой вещественных значений, т.е. два корня
уравнения, либо одно число когда дискриминант равен нулю, либо строку — фразу
нет решений.

🔥 Внимание! Обратите внимание, что смешивать текст и числа в выводе —
не лучшая идея. Тот, кто будет использовать функцию будет вынужден делать
проверки на тип возвращаемого значения. Логичнее возвращать None, если
уравнение не имеет решений. В таком случае первая строка будет записана
как:

def quadratic_equations(a: int | float, b: int | float, c: int |
float) -> tuple[float, float] | float | None:

А в последней строке вернём ничего:

return None

Кстати без указания типов первая строка могла быть записана как:

def quadratic_equations(a, b, c):

🔥 PEP-8! Обратите внимание на пустые строки между функцией и её
вызовом. Рекомендуется оставлять по 2 пустых строки как после, так и до
функции.

В нашем примере мы указали 3 позиционных параметра. При вызове функции
значения попадают в соответствующие позиции переменные. При попытке
передать отличное от указанного в описании функции число аргументов получим
ошибку TypeError.

print(quadratic_equations(2,   -3)) # TypeError: quadratic_equations() missing 1 required positional argument: 'c'"""


