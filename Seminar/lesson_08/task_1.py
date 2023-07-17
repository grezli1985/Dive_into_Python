""" Задание №1 """
import json

""" 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
       текстовый файл с псевдо именами и произведением чисел.
    📌 Напишите функцию, которая создаёт из созданного ранее
       файла новый с данными в формате JSON.
    📌 Имена пишите с большой буквы.
    📌 Каждую пару сохраняйте с новой строки."""

with open('test.txt', 'r', encoding='utf-8') as f:
    lines = f.readline()

result_dict = {}
for line in lines:
    line = line.strip().split()
    result_dict[line[0].title()] = line[1]

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result_dict, f, indent=4, ensure_ascii=False)

