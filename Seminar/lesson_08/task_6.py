""" Задание №6 """
import csv
import os
import pickle

""" 📌 Напишите функцию, которая преобразует pickle файл хранящий список 
       словарей в табличный csv файл. 
    📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара. 
    📌 Функция должна извлекать ключи словаря для заголовков столбца 
       из переданного файла."""

nes_extension = 'pickle'


def pickle_to_csv(path):
    for file in (os.listdir()):
        if os.path.isfile(file):
            initial_name, initial_ext = os.path.join(file).split('.')
            if initial_ext == nes_extension:
                with open(file, 'rb') as f:
                    new_dict = pickle.load(f)
                    # print(f'{new_dict = }')
                    # print(f'{type(new_dict) = }')
                    initial_name = initial_name + '.csv'
                    with open(initial_name, 'w') as f1:
                        csv_write = csv.DictWriter(f1,
                                                   fieldnames=[value for value in new_dict[0]],
                                                   dialect='excel',
                                                   quoting=csv.QUOTE_ALL)
                        csv_write.writeheader()
                        all_data = []
                        for dict_row in new_dict:
                            all_data.append(dict_row)
                        csv_write.writerows(all_data)


if __name__ == '__main__':
    pickle_to_csv(os.path.join(os.getcwd()))
