""" Итераторы"""
"""С итераторами мы уже знакомы. Любая Python коллекция будь то список, словарь,
строка и т.п. предоставляют интерфейс итератора. Если коллекцию можно передать
в цикл for in для последовательного перебора элементов, значит коллекция
итерируемая, поддержи вает интерфейс итарации. При этом у каждой коллекции
может быть свой интерфейс. Списки, строки, кортежи возвращают элементы слева
направо, от нулевого индекса к последнему. Множества возвращают элементы в
случайном порядке.

💡 Секрет! На самом деле порядок вывода элементов множества не
случаен. Он зависит от результата работы встроенного хэша. Хэш функция
определяет в какое место множества будет помещён элемент и возвращает их
в порядке возрастания хеша.

Просто этот порядок может не совпадать со значением элементов.
Что касается словарей, они поддерживают сразу три интерфейса итерации: по
ключам, по значениям и по парам ключ-значение. Вспомните методы keys, values и
items."""

""" Функции iter() и next()
В Python объект является итерируемым, если поддерживает работу дандер методов
__iter__ (или __getitem__) и __next__. Первый метод должен возвращать объект
итератор. Второй, next — возвращает очередной элемент коллекции или
исключение StopIteration. Рассмотрим подробнее."""

""" Функция iter """

""" Функция iter имеет формат iter(object[, sentinel]). object является обязательным
аргументом. Если объект не реализует интерфейс итерации через методы __iter__
или __getitem__, получим ошибку TypeError."""

a = 42
# iter(a)  # TypeError: 'int' object is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

""" Напрямую извлечь данные из итератора не получится. Python сообщает, что
переменная list_iter указывает на <list_iterator object at 0x0000025383D29400>, т.е.
объект итератор списка. Для кортежа функция iter вернёт tuple_iterator, для
множеств set_iterator, а например для dict.items() вернётся dict_itemiterator.
Один из простейших способов получить элементы - распаковать итератор через
звёздочку."""

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)

""" 🔥 Внимание! Обратите внимание, что итератор является одноразовым
объектом. Получив все элементы коллекции один раз он перестаёт работать.
Для повторного извлечения элементов необходимо создать новый итератор."""