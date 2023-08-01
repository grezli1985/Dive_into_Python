""" Задание №3
    📌 Создайте класс-генератор.
    📌 Экземпляр класса должен генерировать факториал числа в
       диапазоне от start до stop с шагом step.
    📌 Если переданы два параметра, считаем step=1.
    📌 Если передан один параметр, также считаем start=1."""


class MyGenerator:

    def __init__(self, *args):
        start, stop, step, result = 1, 1, 1, 1
        if len(args) == 1:
            stop = args[0]
        elif len(args) == 2:
            start = args[0]
            stop = args[1]
        elif len(args) == 3:
            start = args[0]
            stop = args[1]
            step = args[2]
        else:
            raise AttributeError

        if start < stop:
            self.start = start
            self.stop = stop
            self.step = step
            self.result = result
            self.iter_step = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.result *= (self.start + self.step * self.iter_step)
        if self.start + self.step * self.iter_step >= self.stop:
            raise StopIteration
        self.iter_step += 1
        return self.result


if __name__ == '__main__':
    my_gener = MyGenerator(10, 51, 10)
    for i in my_gener:
        print(i)


# class FactGenerator:
#
#     def __init__(self, *args):
#         match len(args):
#             case 1:
#                 self.start = 1
#                 self.stop = args[0]
#                 self.step = 1
#             case 2:
#                 self.start = [0]
#                 self.stop = args[1]
#                 self.step = 1
#             case 3:
#                 self.start, self.stop, self.step = args
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.start < self.stop:
#             result = 1
#             for j in range(2, self.start + 1):
#                 result *= j
#             self.start += self.step
#             return result
#         raise StopIteration
#
#
# if __name__ == '__main__':
#     fg = FactGenerator(3)
#     for i in fg:
#         print(i)
