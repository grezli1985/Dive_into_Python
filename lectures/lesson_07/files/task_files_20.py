""" ● print в файл
Функция print по умолчанию выводит информацию в поток вывода. Обычно это
консоль. Но можно явно передать файловый объект для печати в файл. Для этого
надо воспользоваться ключевым параметром file."""

text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('../file_system/some_dir/dir/new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)

"""В отличии от методов записи в файл, функция print добавляет перенос строки.
Кроме того ничто не мешает явно изменить параметр end функции."""