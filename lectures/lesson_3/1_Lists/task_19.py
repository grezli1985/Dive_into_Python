my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:6:2])               # [6, 8]
print(my_list.pop())                # 18
print(my_list.extend([314, 42]))    # None
print(my_list.sort(reverse=False))  # None
print(my_list)                      # [2, 2, 4, 6, 8, 10, 12, 14, 16, 42, 314]
