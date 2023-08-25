data = [25, -42, 146, 73, -100, 12]

print(list(map(str, data)))
print(max(data, key=lambda x: -x))
print(*filter(lambda x: not x[0].startswith('__'), globals().items()))

# ['25', '-42', '146', '73', '-100', '12']
# -100
# ('data', [25, -42, 146, 73, -100, 12])
