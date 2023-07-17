""" Задание №3 """
import csv
from task_2 import user_input

""" 📌 Напишите функцию, которая сохраняет созданный в
       прошлом задании файл в формате CSV."""


def csv_write():
    user_list = user_input()
    result_dict = {}

    for user in user_list:
        if user[1] in result_dict:
            result_dict[user[1]].update({user[2]: user[0]})
        else:
            result_dict[user[1]] = {user[2]: user[0]}

    with open('res.csv', 'w', encoding='utf-8') as f:
        csv_writ = csv.writer(f, dialect='excel', quoting=csv.QUOTE_ALL)
        csv_writ.writerow(('name', 'id', 'access level'))
        for user in user_list:
            csv_writ.writerow(user)


if __name__ == '__main__':
    csv_write()
