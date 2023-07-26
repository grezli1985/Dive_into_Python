""" ● Передача аргументов в экземпляр
При создании экземпляра можно передать значения в конструктор и тем самым
добавить свойства, характерные для конкретного экземпляра."""


class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.name = }, {p1.race = }')
print(f'{p2.name = }, {p2.race = }')
print(f'{p3.name = }, {p3.race = }')

"""У __init__ определено три параметра. При этом первый параметр всегда self и он не
учитывается при передаче аргументов. Вызывая класс ожидаются два параметра,
при этом второй имеет значение по умолчанию. За исключением self логика такая
же как и при создании обычной функции. Все изученные в теме функции знания
применимы и к функциям класса."""
