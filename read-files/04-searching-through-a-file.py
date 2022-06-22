fhand = open('random-file.txt')

for line in fhand:
    line = line.rstrip() # to throw away white space or empyt lines
    if line.startswith('from'):
        print(line)

