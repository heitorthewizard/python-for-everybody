# Look for most common name in the array list with dictionaries
names_list = [
    'Heitor', 'Sasuke',
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

print(name_counts)
