# list = a linear collection of value that stay in order
# dictionary = a "bag" of values, each with its own label
# very similar to objects in javascript

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)

purse['candy'] = purse['candy'] + 2
print(purse)

bag = {
    'pen': 5,
    'pencil': 2,
    'eraser': 1,
    'book': 1,
    'notebook': 2,
    'laptop': 1
}

keys = bag.keys()
print(keys)

people = {
    'Heitor': {
        'name': 'Heitor Macedo',
        'age': 22,
        'height': 1.80,
        'arms': 2,
        'legs': 2,
        'head': 1,
        'biological sexy': 'male',
        'beauty level': 'super handsome',
        'hair color': 'black',
        'eyes color': 'black',
        'skin color': 'white'
    },
    'Julia': {
        'name': 'Júlia Macedo',
        'age': 18,
        'height': 1.70,
        'arms': 2,
        'legs': 2,
        'head': 1,
        'biological sexy': 'female',
        'beauty level': 'super beautiful',
        'hair color': 'black',
        'eyes color': 'brown',
        'skin color': 'white'
    }
}

print(f"{people['Heitor']['name']} is {people['Heitor']['age']}")

for item in bag:
    print(item)

word_meaning = {}
word_meaning['love'] = 'A terrible painful wonderful great feeling',
word_meaning['Courage'] = 'To act despite the fear'
print(word_meaning)

numbers = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five'
}

for number in numbers:
    print(numbers[number])
