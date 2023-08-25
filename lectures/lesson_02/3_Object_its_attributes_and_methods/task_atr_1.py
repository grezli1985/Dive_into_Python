'''Атрибуты и методы

Атрибуты и методы есть практически у всех объектов в Python.

Атрибуты — это переменные, конкретные
характеристики объекта, такие как цвет поля
или имя пользователя.

Методы — это функции, которые описаны
внутри объекта или класса. Они относятся
к определенному объекту и позволяют
взаимодействовать с ними или другими
частями кода.'''


print("Hello world!".__doc__)
print(str.__doc__)



# str(object='') -> str
# str(bytes_or_buffer[, encoding[, errors]]) -> str
#
# Create a new string object from the given object. If encoding or
# errors is specified, then the object must expose a data buffer
# that will be decoded using the given encoding and error handler.
# Otherwise, returns the result of object.__str__() (if defined)
# or repr(object).
# encoding defaults to sys.getdefaultencoding().
# errors defaults to 'strict'.


# Создайте новый строковый объект из данного объекта. Если кодировать или
# ошибок, то объект должен предоставить буфер данных
# который будет декодирован с использованием данной кодировки и обработчика ошибок.
# В противном случае возвращает результат object.__str__() (если определено)
# или repr(object).
# Кодировка по умолчанию — sys.getdefaultencoding().
# ошибки по умолчанию «strict».
