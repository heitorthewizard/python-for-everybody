xfile = open('random-file.txt')

line_count = 0

for line in xfile:
    line_count = line_count + 1
    print(line)

print(line_count)

