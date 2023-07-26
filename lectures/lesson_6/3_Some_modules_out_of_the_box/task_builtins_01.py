""" Некоторые модули “из коробки”
Рассмотрим несколько модулей из стандартной библиотеки Python. Точнее даже не
модули целиком, а некоторые функции из модулей."""

"""Модуль sys
С модулем sys мы уже познакомились. Он относится к группе служебных в Python.
Модуль sys обеспечивает доступ к некоторым переменным, используемым или
поддерживаемым интерпретатором, а также к функциям, тесно
взаимодействующим с интерпретатором. Изучать все переменные и функции не
имеет смысла. Даже опытные разработчики не пользуются всеми, а их в модуле
около сотни. При необходимости вы всегда сможете найти описание той или иной
функции или переменной в официальной документации. Рассмотрим лишь одну
переменную модуля — argv."""

""" Запуск скрипта с параметрами
Python позволяет запускать скрипты с параметрами. Для этого после имени
исполняемого файла указываются ключи и/или значения через пробел.
Например создадим файл script.py со следующим кодом."""

print('start')
print('stop')

"""Открываем консоль операционный системы и вводим команду на запуск.
python3 script.py

🔥 Важно! Для UNIX ОС используем команду python3. В Windows — python.

🔥 Важно! Не перепутайте консоль ОС и терминал интерпретатора Python.
Терминал выдаёт в начале строки приветствие на ввод — тройную стрелку >>>.

Скрипт вывел текст в консоль и завершил работу. Научим его принимать значения
из командной строки."""