""" ● Функция zip() """
""" zip(*iterables, strict=False) — принимает несколько последовательностей и
итерируется по ним параллельно.

Если передать ключевой аргумент strict=True, вызовет ошибку ValueError в случае
разного числа элементов в каждой из последовательностей."""

names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')

""" Последовательно получаем имена, зарплату и процент премии из каждого списка.
Итерация идёт слева направо."""