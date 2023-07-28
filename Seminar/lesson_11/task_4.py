""" Задание №4
    📌 Доработаем класс Архив из задачи 2.
    📌 Добавьте методы представления экземпляра для программиста и для пользователя."""


class Archive:
    """Строка документации для класса архив, который хранит пару свойств и сохраняет
    в список свойства"""
    _instance = None
    _archive = []

    def __new__(cls, name: str, age: int):
        instance = super().__new__(cls)
        if cls._instance is None:
            cls._instance = instance
        else:
            cls._archive.append(cls._instance)
            cls._instance = instance
        instance.archive = cls._archive.copy()
        return cls._instance

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Игрок по имени {self.name} ({self.age} лет). ' \
               f'До него были созданы игроки: {[pl.name for pl in self.archive]}'

    def __repr__(self):
        return f'Архив: {self.name} {self.age}'


def main():
    player1 = Archive('Stone', 39)
    player2 = Archive('Karina', 18)
    player3 = Archive('Misha', 25)
    player4 = Archive('Dima', 30)
    player5 = Archive('Ser', 33)
    print(player1)
    print(player1.archive)
    print(player2)
    print(player2.archive)
    print(player3)
    print(player3.archive)
    player1.name = 'Oleg'
    print(player4)
    print(player4.archive)
    print(player5)
    print(player5.archive)


if __name__ == '__main__':
    main()
