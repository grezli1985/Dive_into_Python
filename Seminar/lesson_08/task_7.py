""" Задание №7 """
import csv
import pickle

""" 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
    📌 Распечатайте его как pickle строку."""


with open('new_file.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        line = pickle.dumps(line, protocol=pickle.DEFAULT_PROTOCOL)
        print(line)
        # print(type(line))
