print('Use # at the beginning to not print')
word = ''

while True:
    word = input('What should I print? ')

    if word[0] == '#':
        continue

    if word == 'stop':
        break

    print(word)

print('done')

