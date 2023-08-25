"""Задание №3
    📌 Напишите для задачи 1 тесты unittest. Проверьте
       следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери
       символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов
    (кроме п. 1)"""
import unittest
from task_1 import removal_chars


class TestFunc(unittest.TestCase):

    def test_1(self):
        self.assertTrue(removal_chars('hello') == 'hello')

    def test_2(self):
        self.assertEqual(removal_chars('he,,!l.lo'), 'hello')

    def test_3(self):
        self.assertFalse(removal_chars('WERtЕР') == 'WERtер')

    def test_4(self):
        self.assertEqual(removal_chars('he,,!l.lЕРo world'), 'hello world')


if __name__ == '__main__':
    unittest.main(verbosity=2)
