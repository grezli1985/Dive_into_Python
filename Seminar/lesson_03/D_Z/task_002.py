from string import punctuation

""" Задание 2 """

""" ✔ В большой текстовой строке подсчитать количество встречаемых
    слов и вернуть 10 самых частых. Не учитывать знаки препинания
    и регистр символов. За основу возьмите любую статью
    из википедии или из документации к языку."""

txt = 'В большой текстовой строке подсчитать количество встречаемых \
    слов и вернуть 10 самых частых. Не учитывать знаки препинания \
    и регистр символов. За основу возьмите любую статью \
    из википедии или из документации к языку. \
    Создайте словарь со списком вещей для похода в качестве \
    ключа и их массой в качестве значения. Определите какие \
    вещи влезут в рюкзак передав его максимальную \
    грузоподъёмность. Достаточно вернуть один допустимый вариант.'


new_txt = [i.rstrip(punctuation).lower() for i in txt.split() if len(i.rstrip(punctuation)) > 3]
print(sorted(list(new_txt), key=lambda x: x[1], reverse=True)[:10], sep='\n')


















"""---2---"""

# def clean_text(some_text: str, min_length: int = 0) -> list[str]:
#     result = []
#     for ch in list(punctuation) + ['\n']:
#         some_text = some_text.replace(ch, '')
#     for word in some_text.split():
#         word = word.lower().strip()
#         if len(word) >= min_length:
#             result.append(word)
#     return result
#
#
# def counter(word_list: list[str]) -> dict[str, int]:
#     count_dict = {}
#     for word in word_list:
#         count_dict[word] = count_dict.get(word, 0) + 1
#     return count_dict
#
#
# def words_counter(count_dict: dict[str, int], top: int) -> str:
#     result = [f'Топ {top} слов в тексте: ']
#     top_words = sorted(list(count_dict.items()), key=lambda x: x[1], reverse=True)[:top]
#     max_length = len(max(top_words, key=lambda x: len(x[0]))[0])
#     for i, word in enumerate(top_words, 1):
#         result.append(f'{i:>3}. {word[0]:.<{max_length}} {word[1]:<3}')
#     return '\n'.join(result)
#
#
# print(words_counter(counter(clean_text(txt, 3)), 10))
