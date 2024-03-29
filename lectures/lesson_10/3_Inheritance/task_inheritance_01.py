""" Наследование """
"""В Python все объекты являются наследниками класса object. В начале лекции мы
рассмотрели пример создания класса: """


class Person:
    pass


"""Представленная запись создания класса является упрощённой. На самом деле
класс Person наследуется от класса object. Т.е. object — родительский класс для
Person, а Person — дочерний класс для object. """


class Person(object):
    pass


"""🔥 Важно! Наследование от object принято опускать при создании класса."""
