print('What\'s the biggest number?')

numbers = [64,3,4,3,54,656,744,24,3,54,6567,768]
largest_number = 0

for number in numbers :
    if number > largest_number:
        largest_number = number

print('The biggest number is: ', largest_number)
    
