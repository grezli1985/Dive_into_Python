""" Задание №5
    📌 Доработаем задачи 3 и 4. Создайте класс проекта, который
       имеет следующие методы:
    📌 загрузка данных (функция из задания 4)
    📌 вход в систему - требует указать имя и id пользователя. Для
       проверки наличия пользователя в множестве используйте
       магический метод проверки на равенство пользователей.
       Если такого пользователя нет, вызывайте исключение
       доступа. А если пользователь есть, получите его уровень из
       множества пользователей.
    📌 добавление пользователя. Если уровень пользователя
       меньше, чем ваш уровень, вызывайте исключение уровня
       доступа."""

import json
import random


class User:

    def __init__(self, name='', id=0, access_lvl=0):
        self.name = name
        self.id = id
        self.access_lvl = access_lvl
        self.users_list = []

    def user_input(self):
        user_list = []
        users_list = []

        while True:
            try:
                name = input('Name: ')
                if not str.istitle(name):
                    raise ValueError
            except Exception as e:
                print(e)
            if not name:
                for i in user_list:
                    users_list.append(User(*i))
                self.users_list = users_list
                break
            while True:
                user_id = random.randint(10_000, 100_000)
                if user_id not in [uid[2] for uid in user_list]:
                    break
            while True:
                lvl = input('lvl: ')
                if lvl.isdigit() and 0 < int(lvl) < 8:
                    user_list.append((name, user_id, lvl))
                    break

    def __str__(self):
        return f'{self.name} {self.id} {self.access_lvl}'

    def get_info(self):
        return [(user.name, user.id, user.access_lvl) for user in self.users_list]

    def json_write(self, file_name):
        result_dict = {}

        for user in self.users_list:
            result_dict[user.id] = [user.name, user.access_lvl]

        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(result_dict, f, indent=4, ensure_ascii=False)
        except EOFError as e:
            print(e)

    def json_read(self, file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
        except EOFError as e:
            print(e)

        for key in new_dict:
            self.users_list.append(User(new_dict[key][0], int(key), int(new_dict[key][1])))

    def log_id(self, name, input_id):
        work_list = self.get_info()
        for value in work_list:
            if name == value[0] and input_id == value[1]:
                self.name = value[0]
                self.id = value[1]
                self.access_lvl = value[2]
                return self.access_lvl
        raise Exception('В доступе отказано')

    def creat_new_user(self, name, lvl):
        if self.access_lvl < lvl:
            raise Exception('Уровень доступа не достаточен')
        while True:
            user_id = random.randint(10_000, 100_000)
            if user_id not in [uid.id for uid in self.users_list]:
                self.users_list.append(User(name, user_id, lvl))
                break


new_user = User('', '', '')
# new_user.user_input()
# new_user.json_write()
new_user.json_read('res_user.json')
for i in new_user.users_list:
    print(i)

print(new_user.get_info())
print(new_user.log_id('ccc', 27184))
new_user.creat_new_user('RERT', 4)
print(new_user.get_info())
