"""Массивы поддерживают методы списка list, поэтому использование их интуитивно
понятно. Привыкать надо лишь к указанию хранимого типа данных."""
from array import array

long_array = array('l', [-6000, 800, 100500])
long_array.append(42)

print(long_array)
print(long_array[2])
print(long_array.pop())

"""При этом массив не позволит добавить значение, если оно выходит за пределы
диапазона, заданного кодом типа при создании. Так же будет поднята ошибка при
несоответствии типа."""
