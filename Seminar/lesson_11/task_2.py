""" Задание №2
    📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
    📌 При нового экземпляра класса, старые данные из ранее созданных
       экземпляров сохраняются в пару списков архивов
    📌 list-архивы также являются свойствами экземпляра"""


# class Archive():
#     _instance = None
#     archive_list = []
#
#     def __new__(cls, name: str, number: int):
#         if cls._instance is None:
#             _instance = super().__new__(cls)
#         return _instance
#
#     def __init__(self, name: str, number: int):
#         self.name = name
#         self.number = number
#         self.archive = Archive.archive_list
#         self.archive_list.append((name, number))
#
#
# arch_1 = Archive('ssss', 1)
# arch_2 = Archive('dddd', 2)
# arch_3 = Archive('cccc', 3)
#
# print(Archive.archive_list)
# print(arch_2.archive)

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

    def __repr__(self):
        return f'{self.name} {self.age}'


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
    # help(Archive)
