"""Задание №4
    📌 Напишите для задачи 1 тесты pytest. Проверьте следующие
       варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери
       символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов
    (кроме п. 1)"""
import pytest
from task_1 import removal_chars


def test_1():
    assert removal_chars('hello') == 'hello'


def test_2():
    assert removal_chars('he,,!l.lo') == 'hello'


def test_3():
    assert removal_chars('WERtЕР') != 'WERtер'


def test_4():
    assert removal_chars('he,,!l.lЕРo world') == 'hello world'


if __name__ == '__main__':
    pytest.main(['-v'])

