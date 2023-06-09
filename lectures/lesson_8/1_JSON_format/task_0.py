""" Термины лекции """
""" ● Сериализация — это процесс преобразования объекта в поток байтов для
      сохранения или передачи в память, базу данных или файл.
    ● Десериализация — восстановление объектов из байт, сохранение которых
      было произведено ранее. Процедура выгрузки «зафиксированной»
      информации пользователем."""

""" Как несложно заметить JSON похож на словарь Python. В целом верно, но есть
небольшие отличия. Некоторые типы данных Python не совпадают с типами в
формате JSON. Поэтому при конвертации словаря в JSON и последующей
конвертации в словарь типы данных могут оказаться иными.

    Python    ->    JSON      ->    Python
    dict            object          dict
    list, tuple     array           list
    str             string          str
    int             number          (int) int
    float           number (float)  float
    True            true            True
    False           false           False
    None            null            None

Обратите внимание, что list и tuple конвертируется в массив array, а при обратной
конвертации получаем только list.
Если мы храним несколько JSON объектов, в Python обычно используют list. Для
JSON в этом случае используется array — в квадратных скобках записываются JSON
объекты разделённые запятыми.    """