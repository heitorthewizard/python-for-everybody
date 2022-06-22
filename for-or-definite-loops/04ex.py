print('Filtering numbers less than 20 with for loop')

array = [9, 41, 12, 3, 74, 15]
filtered_array = []

for value in array:
    if value < 20:
        filtered_array.append(value)

print('numbers less than 20: {}'.format(filtered_array))
