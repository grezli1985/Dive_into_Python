""" Функции “из коробки” """
""" В Python есть ряд встроенных функций. Они доступны всегда, без импортов и
других подготовительных операций. Перечислим их в алфавитном порядке:
abs(), aiter(), all(), any(), anext(), ascii(), bin(), bool(), breakpoint(), 
bytearray(), bytes(), callable(), chr(), classmethod(), compile(), complex(), 
delattr(), dict(), dir(), divmod(), enumerate(), eval(), exec(), filter(), float(), 
format(), frozenset(), getattr(), globals(), hasattr(), hash(), help(), hex(), 
id(), input(), int(), isinstance(), issubclass(), iter(), len(), list(), locals(), 
map(), max(), memoryview(), min(), next(), object(), oct(), open(), ord(), pow(), 
print(), property(), range(), repr(), reversed(), round(), set(), setattr(), slice(),
sorted(), staticmethod(), str(), sum(), super(), tuple(), type(), vars(), zip().

Часть функций мы уже разбирали на прошлых лекциях. Ещё часть разберём
сегодня. О некоторых функциях поговорим на следующих лекциях курса.

🔥 Важно! Не используйте имена встроенных функций в качестве имён
переменных.

💡 PEP-8! Если очень хочется, добавляйте к имени переменной символ
подчёркивания. Не sum, a sum_. Не max, а max_"""

""" Функция map() """

""" map(function, iterable) — принимает на вход функцию и последовательность.
Функция применяется к каждому элементу последовательности и возвращает map итератор."""

texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts)
print(*res)

""" В качестве функции использовали лямбду для вызова метода lower у каждого из
переданных объектов. Объект итератор res был распакован в функцию print через
символ “звёздочка”."""