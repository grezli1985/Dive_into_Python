'''Функция isinstance(object, classinfo)
Принимает на вход объект и класс и возвращает истину, если объект
является экземпляром прямого или косвенного подкласса'''

data = 42
print(isinstance(data, int))

data = True
print(isinstance(data, int))

data = 3.14
print(isinstance(data, (int, float, complex)))
