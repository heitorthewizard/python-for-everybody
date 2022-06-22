fhand = open('random-file.txt')

for line in fhand:
    line = line.rstrip()
    if not 'from' in line:
        continue
    print(line)

