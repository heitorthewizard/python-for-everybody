# using re.search()
import re
hand = open('lorem.txt')
for line in hand:
    line = line.rstrip()
    if re.search('Assumenda', line):
        print(line)

