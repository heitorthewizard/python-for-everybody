print ('Finding the smallest number')

smallest_number = None

for val in [41, 53, 12, 15, 74, 13, 3, 24, 64, 66, 98, 76, 45]:
    if smallest_number is None:
        smallest_number = val

    elif val < smallest_number:
        smallest_number = val

print('The smallest number is {}'.format(smallest_number))
