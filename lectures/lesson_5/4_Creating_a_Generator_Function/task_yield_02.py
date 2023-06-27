""" Команда yield """
"""Как вы помните команда return возвращает готовый результат работы функции и
завершает её работу. Зарезервированное слово yield превращает функцию в
генератор. Значение после yield возвращается из функции. Сама функция
запоминает своё состояние: строку, на которой остановилось выполнение, значения
локальных переменных. Повторный вызов функции продолжает работу с момента
остановки.

Изменим функцию для получения факториала чисел, превратив её в генератор."""


def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

"""Теперь внутри функции не создаётся пустой список для результатов. В цикле
вычисляется факториал очередного числа. Далее команда yield возвращает
значение. Следующий вызов вернёт функцию к циклу for для вычисления
очередного числа.
Как вы помните, если в функции отсутствует команда return Python в конце тела
функции добавляет return None. Явная или неявная, как в нашем примере, команда
return завершает работу генератора вызовом исключения StopIteration."""