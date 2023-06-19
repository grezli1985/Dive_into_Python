my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
print(len(my_set))
print(my_set - {1, 2, 3})
print(my_set.union({2, 4, 6, 8}))
print(my_set & {2, 4, 6, 8})
print(my_set.discard(10))

# 7
# frozenset({4, 5, 6, 7})
# frozenset({1, 2, 3, 4, 5, 6, 7, 8})
# frozenset({2, 4, 6})
# AttributeError: 'frozenset' object has no attribute 'discard'
