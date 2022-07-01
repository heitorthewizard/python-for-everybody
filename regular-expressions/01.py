# Using regular expression module
# re.search() like find()

hand = open('lorem.txt')
for line in hand:
    line = line.rstrip()
    if line.find('Assumenda') >= 0:
        print(line)

