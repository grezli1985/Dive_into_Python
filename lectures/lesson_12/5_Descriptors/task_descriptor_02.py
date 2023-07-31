"""Напишем класс, который хранит имя ученика, его возраст,
номер класса (от 1 до 11) и номер кабинета, в котором сидит класс."""


class Student:
    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age}, ' \
               f'grade={self.grade}, office={self.office})'


std1 = Student('Шурик', 7, 1, 12)
print(std1)

"""А теперь внимательно посмотрим на числовые значения.
➢ возраст должен быть больше нуля
➢ класс должен быть от 1 до 11
➢ кабинет должен быть номером в каком-то диапазоне. Предположим, что в
нашей школе кабинеты нумеруются от 3 до 42"""
