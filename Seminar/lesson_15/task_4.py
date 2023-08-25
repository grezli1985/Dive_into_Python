"""Задание №4
    📌 Функция получает на вход текст вида: “1-й четверг ноября”,
       “3-я среда мая” и т.п.
    📌 Преобразуйте его в дату в текущем году.
    📌 Логируйте ошибки, если текст не соответсвует формату."""
# from datetime import datetime
#
#
# def parse_str(text: str):
#     DAYS_IN_MONTH = 30
#     week, day, month = text.split()
#     week = int(week[0])
#     day = parse_day(day)
#     month = parse_month(month)
#     year = datetime.now().year
#     week_counter = 0
#     for i in range(1, DAYS_IN_MONTH + 1):
#         data = datetime(day=i, month=month, year=year)
#         if data.weekday() == day:
#             week_counter += 1
#             if week_counter == week:
#                 return data
#
#
# def parse_month(month: str) -> int:
#     months = {'янв': 1, 'фев': 2, 'мар': 3, "апр": 4, "мая": 5, "июн": 6, "июл": 7, "авг": 8, "сен": 9,
#               "окт": 10, "ноя": 11, "дек": 12}
#     return months.get(month[:3], None)
#
#
# def parse_day(day: str) -> int:
#     match day.lower():
#         case "понедельник":
#             return 0
#         case "вторник":
#             return 1
#         case "среда":
#             return 2
#         case "четверг":
#             return 3
#         case "пятница":
#             return 4
#         case "суббота":
#             return 5
#         case "воскресенье":
#             return 6
#
#
# if __name__ == '__main__':
#     print(parse_str("1-й четверг ноября"))
#     print(parse_str("3-я среда мая"))

import logging
from datetime import datetime, date

logging.basicConfig(filename='error.log',
                    filemode='w',
                    encoding='utf-8',
                    level=logging.INFO)
logger = logging.getLogger()

months = {'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4, 'май': 5,
          'июн': 6, 'июл': 7, 'авг': 8, 'сен': 9, 'окт': 10,
          'ноя': 11, 'дек': 12}
weekdays = {'пон': 1, 'вто': 2, 'сре': 3, 'чет': 4, 'пят': 5,
            'суб': 6, 'вос': 7}


def text_to_date(text: str):
    try:
        year = datetime.now().year
        count, weekday_, month_ = text.split()
        month = months[month_[:3]]
        weekday = weekdays[weekday_[:3]] - 1
        count = int(count[0])
    except Exception as exc:
        logger.info(f'{count}-й  {weekday_}  {month_} {year} =  ошибка: {exc}')

    count_week = 0
    for day in range(1, 31 + 1):
        result = date(year=year, month=month, day=day)
        if result.weekday() == weekday:
            count_week += 1
            if count_week == count:
                logger.info(f'{count}-й {weekday_} {month_} {year} = {result} ')
                return result


if __name__ == '__main__':
    print('2-й вторник мая:', text_to_date('2-й понедельник май'))
    print('3-й четверг ноября:', text_to_date('3-й вторник ноября'))
    print('4-я среда мая:', text_to_date('4-я среда май'))
