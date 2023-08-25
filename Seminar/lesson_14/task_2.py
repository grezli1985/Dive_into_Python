"""Задание №2
    📌 Напишите для задачи 1 тесты doctest. Проверьте
       следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери
       символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов
    (кроме п. 1)"""
from string import ascii_lowercase


def removal_chars(text: str) -> str:
    """
    >>> removal_chars('WEFGHgfdeRT123G') == 'wefghgfdertg'
    True
    >>> removal_chars('ergh   G##f4') == 'ergh   gf'
    True
    >>> removal_chars('5 7 8 9  ))) ') == '      '
    True
    """
    result = ''
    for ch in text.lower():
        if ch in ascii_lowercase + ' ':
            result += ch

    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
