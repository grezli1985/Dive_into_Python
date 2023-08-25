"""Задание №5
    📌 На семинарах по ООП был создан класс прямоугольник
       хранящий длину и ширину, а также вычисляющую периметр,
       площадь и позволяющий складывать и вычитать
       прямоугольники беря за основу периметр.
    📌 Напишите 3-7 тестов unittest для данного класса."""
import unittest
from Seminar.lesson_11.task_6 import Square


class TestSquare(unittest.TestCase):

    def setUp(self) -> None:
        self.test_square = Square(10, 5)
        self.test_kvadrat = Square(10)

    def test_1(self):
        self.assertEqual(self.test_kvadrat.width, 10)

    def test_2(self):
        self.assertFalse(self.test_kvadrat.width is None)

    def test_area(self):
        self.assertEqual(self.test_square.square(), 50)

    def test_perimetr(self):
        self.assertEqual(self.test_square.perimetr(), 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
