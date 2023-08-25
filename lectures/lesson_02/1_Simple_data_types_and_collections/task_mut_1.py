'''Изменяемые и неизменяемые типы
    Неизменяемые
Числа: int, bool, float, complex
Последовательности: str, tuple, bytes
Множества: set'''

a = 5
print(a, id(a))    # 5 4368534744
a += 1
print(a, id(a))    # 6 4368534776

# txt = "hello world"   # TypeError: 'str' object does not support item assignment
# txt[5] = '_'          # TypeError: объект 'str' не поддерживает назначение элемента

txt = 'hello world!'
print(txt, id(txt))          # hello world! 4443150064
txt = txt.replace(' ', '_')
print(txt, id(txt))          # hello_world! 4443149936

