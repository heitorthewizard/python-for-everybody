# like a file...
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
total_words = 0

for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        total_words += 1

lst = list()

for key, val in counts.items():
    lst.append((val, key))

lst.sort(reverse=True)

most_used_words = list()

for item in lst[:3]:
    most_used_words.append(item[1])

for key, val in lst:
    print(key, val)

print(f'total words: {total_words}')
print('most used words: {}, {}, {}'.
format(most_used_words[0], most_used_words[1], most_used_words[2]))


