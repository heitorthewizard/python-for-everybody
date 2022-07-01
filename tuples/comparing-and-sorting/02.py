# Sort by values instead of keys
sorted_by_key_dict = {'a': 10, 'b': 1, 'c': 22}
tuple_list = list()

for key, value in sorted_by_key_dict.items():
    tuple_list.append((value, key))

print(tuple_list)

tuple_list = sorted(tuple_list, reverse=True)
print('reversed sorted by value tuple_list:', tuple_list)

