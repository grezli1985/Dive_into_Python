""" Работа со словарями """
""" Метод keys() - возвращает объект-итератор dict_keys"""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())       # dict_keys(['one', 'two', 'three', 'four', 'ten'])
for key in my_dict.keys():
    print(key)              # one
                            # two
                            # three
                            # four
                            # ten


""" Обычно объект не используют напрямую. Метод keys применяется в связке с
циклом for для перебора ключей словаря.

🔥 Важно! Запись цикла for key in my_dict: отработает аналогично. По
умолчанию словарь возвращает ключи для итерации в цикле.

💡 Внимание! В отличии от списков, кортежей и строк доступ к
элементу-значению осуществляется не по индексу, а по ключу. При этом
начиная с версии Python 3.7 словарь сохраняет порядок добавления ключей. 
В каком порядке ключи были добавлены, в том порядке они будут возвращены в
случае итерации по словарю."""
