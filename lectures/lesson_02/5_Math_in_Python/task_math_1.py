import math

""" Математические модули

В Python есть несколько модулей в стандартной
библиотеке, которые облегчают математические
расчёты. Для доступа к ним необходимо выполнить
импорт в начале файла.
import math
import decimal
import fractions"""

""" Модуль math

Константы: e, inf, nan, pi, tau
Математические функции: acos, acosh, asin, asinh,
atan, atan2, atanh, ceil, comb, copysign, cos, cosh,
degrees, dist, erf, erfc, exp, expm1, fabs, factorial, floor,
fmod, frexp, fsum, gamma, gcd, hypot, isclose, isfinite,
isinf, isnan, isqrt, lcm, ldexp, lgamma, log, log10, log1p,
log2, modf, nextafter, perm, pow, prod, radians,
remainder, sin, sinh, sqrt, tan, tanh, trunc, ulp"""

print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')

print(dir(math))
print(help(math.gcd))


# 3.141592653589793
# 2.718281828459045
# inf
# nan
# 6.283185307179586

# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
# 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil',
# 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc',
# 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
# 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt',
# 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter',
# 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan',
# 'tanh', 'tau', 'trunc', 'ulp']


# gcd(*integers)
#     Greatest Common Divisor.
#     Наибольший общий делитель.
