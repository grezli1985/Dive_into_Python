from mathematical import base_math as bm
from mathematical.advanced_math import exp

x = bm.div(12, 5)
z = exp(2, 3)

print(x)
print(z)

"""В первом случае импортировали модуль base_math под именем bm. Во-втором —
функцию exp из модуля advanced_math пакета mathematical.
Отдельно стоит упомянуть особенности импорта внутри подпакетов. Например
импорт модуля other_module в другой модуль того же пакета можно осуществить
через относительный импорт:

from . import other_module

А если модулю надо выйти из своего пакета в пакет верхнего уровня, используют
вторую точку:

from .. import other_module

Или так

from ..other_package import other_module

🔥 Важно! Модуль, который является основным в вашем проекте должен
использовать только абсолютные имена пакетов и модулей. Связано это с тем,
что у запускаемого модуля в переменной __name__ хранится значение
“__main__”, а не имя модуля."""