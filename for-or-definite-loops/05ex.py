print ('Finding the largest number with for loop')

array = [41, 53, 12, 15, 74, 13, 24, 64, 66, 98, 76, 45]
largest_number = array[0]

for val in array:
    if val > largest_number:
        largest_number = val

print('The largest number in {} is {}'.format(array, largest_number))
