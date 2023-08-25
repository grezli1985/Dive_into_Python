""" Доступ к значению словаря """
""" Для получения доступа к значению необходимо указать ключ в квадратных скобках
после или переменной."""

""" ✔ dict[key] — доступ через квадратные скобки [] """

TEN = 'ten'
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict['two'])   # 2
print(my_dict[TEN])     # 10
print(my_dict[1])       # KeyError: 1

""" Ключ может быть указан явно или передам как содержимое переменной,
константы. При попытке обратиться к несуществующему ключу получаем ошибку:
KeyError.
Доступ к ключу позволяет изменять значения. Для этого используем операцию
присваивания как и в случае с добавлением новой пары ключ-значение.

🔥 Важно! Получить доступ к ключу по значению невозможно."""