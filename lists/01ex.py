friend_list = [
    'Sasuke',
    'Naruto',
    'Madara',
    'Minato',
    'Itachi',
    'Jiraiya',
    'Hashirama'
]

for friend in friend_list:
    print(f'Happy new year, {friend}')


# looking inside with indexes
print(friend_list[0], friend_list[6])

# changing value at a index
friend_list[0] = 'Uchiha Sasuke'
friend_list[4] = 'Uchiha Itachi'

print(friend_list[0], 'and', friend_list[4])

# getting length and range
print(len(friend_list))
print(range(len(friend_list)))

# another way of doing a for loop
for i in range(len(friend_list)):
    friend = friend_list[i]
    print(f'Happy new year, {friend}')
