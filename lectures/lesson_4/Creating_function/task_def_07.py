""" Возврат значения """
""" Как вы уже заметили внутри функции на печать ничего не выводится. Мы не
используем print в теле, а выводим на печать результат работы функции. Такой
подход предпочтительнее. Ведь результат можно сохранить в переменную для
дальнейшей работы с ним.
Для возврата результатов используется зарезервированное слово return. Указанные
после слова объекты возвращаются как результат работы функции.
    ● Если указан один объект — возвращается именно этот объект.
    ● Если указано несколько значений через запятую, возвращается кортеж с перечисленными значениями
    ● Если ничего не указано после return — возвращается None
После выполнения строки с командой return работа функции завершается, даже
если это не последняя строка в теле функции."""


def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    # return None


""" Мы убрали else, т.к. последний возврат будет выполнен только в том случае, когда
не сработала ни одно условие выше и следовательно не получилось выйти из
функции через другой return. По этой же причине заменили elif на if."""