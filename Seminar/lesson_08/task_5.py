""" Задание №5 """
import json
import os
import pickle

""" 📌 Напишите функцию, которая ищет json файлы в указанной директории и 
       сохраняет их содержимое в виде одноимённых pickle файлов."""

nes_extension = 'json'


def json_to_pickle(path):
    for file in (os.listdir(path)):
        if os.path.isfile(file):
            initial_name, initial_ext = os.path.join(file).split('.')
            if initial_ext == nes_extension:
                with open(file, 'r', encoding='utf-8') as f:
                    new_dict = json.load(f)
                    initial_name = initial_name + '.pickle'
                    with open(initial_name, 'wb') as f1:
                        pickle.dump(new_dict, f1)


if __name__ == '__main__':
    json_to_pickle(os.path.join(os.getcwd()))
