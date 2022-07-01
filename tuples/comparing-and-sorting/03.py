fhand = open('lorem.txt')
counts = dict()

# getting all words from file and counting them
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()

# creating a tuple with the words
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

# sorting them so show up in reverse order like 10 to 1
lst = sorted(lst, reverse=True)

# printing out the result
for val, key in lst[:20]:
    print(key, val)

