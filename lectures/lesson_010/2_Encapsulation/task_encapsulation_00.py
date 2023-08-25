""" Инкапсуляция """
"""В ряде языков программирования под инкапсуляцией понимается сокрытие части
свойств и методов класса от доступа извне класса. Как вы понимаете пользователи
программы не пишут код. Они используют графический или консольный интерфейс.
Или даже пользуются программой даже не догадываясь об этом, к примеру получая
данные от программы-сервера во время сёрфинга в интернете. Следовательно
инкапсуляция нужна одним разработчикам для сокрытия от других разработчиков и
самих себя.
Python исповедует принципы разумного программирования. Если один разработчик
решает внести изменения в код другого, он понимает что делает. В результате в
Python нет строгой инкапсуляции как в ряде других языков. Часть инкапсуляции
прописана как соглашения. И мы сталкивались с ними, когда разбирали модули и
импорт переменных и функций из модулей."""

""" Модификаторы доступа

В классическом ООП выделяют следующие модификаторы доступа:
    
    ● public — публичный доступ, т.е. возможность обратиться к свойству или
      методу из любого другого класса и экземпляра
    ● protected — защищённый доступ, позволяющий обращаться к свойствам и
      методам из класса и из классов наследников.
    ● private — приватный доступ, т.е. отсутствие возможности обратиться к свойству
      или методы из другого класса или экземпляра.

В Python по умолчанию все свойства и методы публичные. Однако существуют
соглашения по стилю имён, которые делают атрибуты защищёнными/приватным.
Речь в очередной раз пойдёт о символе подчеркивания."""