#built-in functions for lists
nums = [3, 41, 12, 9, 74, 15]
print('len', len(nums))
print('max', max(nums))
print('min', min(nums))
print('sum', sum(nums))
print('sum/len', sum(nums)/len(nums))


# getting average in different ways
# uncomment to see the code running

# first way and better

# total = 0
# count = 0
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1

# average = total / count
# print('Average: ', average)


# second way using built-in methods

num_list = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    num_list.append(value)

average = sum(num_list) / len(num_list)
print(f'Average: {average}')

# The trade off of using the second way is because it's storing all
# the numbers in a array list. Which takes more space. So if you were
# getting the average of 1 billion numbers, that would take a lot of space
# when the first way use only one space assigned overwriting every time it
# sums with another number.
