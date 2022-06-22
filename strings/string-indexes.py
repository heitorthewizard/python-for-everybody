fruit = 'banana'
letter = fruit[0]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

def split_str(s) :
    return [c for c in s]

splitted_fruit = split_str(fruit)

for idx, val in enumerate(splitted_fruit) :
   print('letter {} = {}'.format(idx, val))

print('length:', len(fruit))
