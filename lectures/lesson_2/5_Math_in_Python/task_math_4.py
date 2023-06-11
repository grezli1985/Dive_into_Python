""" Комплексные числа

complex([real[, imag]]) — комплексное число
из действительной real и мнимой imag частей."""

a = complex(2, 3)
b = complex('2+3j')
print(a, b, a == b, sep='\n')

# (2+3j)
# (2+3j)
# True
