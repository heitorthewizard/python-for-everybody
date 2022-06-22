print('Finding the AVERAGE in a for loop')
array = [9, 41, 12, 3, 74, 15]

count = 0
sum = 0

print('Before', count, sum)

for value in array:
    count = count + 1
    sum = sum + value
    print('{} -> {} || {}'.format(count, sum, value))

print('After count:{}, sum:{}, average:{}'
      .format(count, sum,  (sum / count)))
