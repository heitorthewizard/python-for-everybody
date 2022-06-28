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

# first way (manually)
# for name in names_list:
#     if name not in name_counts:
#         name_counts[name] = 1
#     else:
#         name_counts[name] += 1


# second way (using get method)
for name in names_list:
    name_counts[name] = name_counts.get(name, 0) + 1

for key in name_counts:
    print(key, name_counts[key])


# getting the most common name
counter = 0
most_common_name = ''

for name in name_counts:
    if name_counts[name] > counter:
        counter = name_counts[name]
        most_common_name = name

print(f"MOST COMMON NAME IS {blue(most_common_name.upper())}. APPEARED {red(counter)} TIMES")

