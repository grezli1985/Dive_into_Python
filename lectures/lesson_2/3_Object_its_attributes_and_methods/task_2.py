'''Интерактивная работа со справкой, help()

Введите команду keywords, далее любое интересное вам ключевое слово
из списка. Прочитайте описание и напишите в чат пару слов о том, что узнали. '''
help()

'''     keywords
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 '''

# help> False
# Справка по логическому объекту:

'''
class bool(int)
 |  bool(x) -> bool
 |  
 |  Возвращает True, если аргумент x истинен, и False в противном случае.
 |  Встроенные функции True и False являются единственными двумя экземплярами класса bool.
 |  Класс bool является подклассом класса int и не может быть подклассом.
 |  
 |  Method resolution order: Порядок разрешения метода:
 |      bool
 |      int
 |      object
 |  
 |  Methods defined here: Определенные здесь методы:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here: Статические методы определены здесь:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |      Создать и вернуть новый объект. См. справку (тип) для точной подписи.
 |  ----------------------------------------------------------------------
 |  Methods inherited from int: Методы, унаследованные от int:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Default object formatter.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |     Возвращает self, преобразованный в целое число, если self подходит для использования в качестве индекса в списке.
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      Округление интеграла возвращает itself.
 |
 |      Rounding with an ndigits argument also returns an integer.
 |      Округление с аргументом ndigits также возвращает целое число.
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes. Возвращает размер в памяти в байтах.
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself. Усечение интеграла возвращает само себя.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Возвращает пару целых чисел, отношение которых в точности равно исходному int
 |      и с положительным знаменателем.
 |      
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |  
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |      Количество единиц в двоичном представлении абсолютного значения self.
 |
 |      Also known as the population count. Также известен как подсчет населения.
 |      
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |  
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |      Количество битов, необходимых для представления себя в двоичном формате.
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |      Возвращает self, комплексное сопряжение любого int.
 |  to_bytes(self, /, length=1, byteorder='big', *, signed=False)
 |      Return an array of bytes representing an integer.
 |      Возвращает массив байтов, представляющий целое число.
 |      length длина
 |        Длина используемого объекта в байтах. Ошибка OverflowError возникает, 
 |        если целое число не может быть представлено с заданным количеством байтов. 
 |        По умолчанию это длина 1.
 |      byteorder порядок байтов
 |        Порядок байтов, используемый для представления целого числа. 
 |           Если порядок байтов "большой", старший байт находится в начале массива байтов. 
 |           Если порядок байтов "маленький", старший байт находится в конце байтовый массив. 
 |           Чтобы запросить собственный порядок байтов хост-системы, используйте
 |           `sys.byteorder' как значение порядка байтов. По умолчанию используется «большой».
 |           подписал
 |           Определяет, используется ли дополнение до двух для представления целого числа.
 |           Если для signed установлено значение False и задано отрицательное целое число, 
 |           возникает ошибка OverflowError.
 |           Поднялся.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods inherited from int: Методы класса, унаследованные от int:
 |  
 |  from_bytes(bytes, byteorder='big', *, signed=False) from builtins.type
 |      Return the integer represented by the given array of bytes.
 |      Возвращает целое число, представленное данным массивом байтов.
 |      bytes байты
 |        Содержит массив байтов для преобразования. Аргумент должен либо
 |        поддерживать протокол буфера или быть итерируемым объектом, производящим байты.
 |        Bytes и bytearray являются примерами встроенных объектов, поддерживающих
 |        буферный протокол.
 |      byteorder порядок байтов
 |        Порядок байтов, используемый для представления целого числа. Если порядок байтов "большой",
 |        старший байт находится в начале массива байтов. Если
 |        порядок байтов "маленький", старший байт находится в конце
 |        байтовый массив. Чтобы запросить собственный порядок байтов хост-системы, используйте
 |        `sys.byteorder' как значение порядка байтов. По умолчанию используется «большой».
 |      signed подписал
 |        Указывает, используется ли дополнение до двух для представления целого числа.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from int: Дескрипторы данных, унаследованные от int:
 |  
 |  denominator знаменатель
 |      the denominator of a rational number in lowest terms
 |      знаменатель рационального числа в наименьших условиях
 |  imag изображение
 |      the imaginary part of a complex number
 |      мнимая часть комплексного числа
 |  numerator числитель
 |      the numerator of a rational number in lowest terms
 |      числитель рационального числа в наименьших условиях
 |  real настоящий
 |      the real part of a complex number
 |      действительная часть комплексного числа'''

