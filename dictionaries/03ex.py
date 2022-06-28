# Look for most common name in the array list with dictionaries
from simple_colors import *

names_list = [
    'Goku', 'Sasuke',
    'Sasuke', 'Heitor',
    'Naruto', 'Naruto',
    'Naruto', 'Sakura',
    'Heitor', 'Kakashi',
    'Heitor', 'Jiraiya',
    'Heitor', 'Jiraiya',
    'Sasuke', 'Heitor',
    'Heitor', 'Naruto',
    'Naruto', 'Rock Lee',
    'Sasuke', 'Sasuke',
    'Heitor', 'Itachi',
    'Naruto', 'Heitor'
]

name_counts = dict()

for name in names_list:
    name_counts[name] = name_counts.get(name, 0) + 1

keys = name_counts.keys()
items = name_counts.items()
values = name_counts.values()
print(keys)
print(items)
print(values)

# splitting terminal
print('#####################################################')

# elegant loop
for key, value in name_counts.items():
    print(key, value)


# splitting terminal
print('#####################################################')
# elegant way of getting most common word
count = None
most_common_name = None
for key, value in name_counts.items():
    if count is None or value > count:
        most_common_name = key
        count = value

print('THE MOST COMMON NAME IS {} REPEATING {} TIMES'
.format(red(most_common_name.upper()), yellow(count)))
