text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('../file_system/some_dir/dir/new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)
