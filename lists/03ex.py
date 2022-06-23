# ways of creating a list statement
list = list()
print(type(list))

# adding item to list
list.append('item-1')
list.append('item-2')
print(list)

# dir()
# If called without an argument, return the names in the current scope. Else, return an alphabetized list of names comprising (some of) the attributes of the given object, and of attributes reachable from it. If the object supplies a method named __dir__, it will be used; otherwise the default dir() logic is used and returns:
#   for a module object: the module's attributes.
#   for a class object: its attributes, and recursively the attributes
#     of its bases.
#   for any other object: its attributes, its class's attributes, and
#     recursively the attributes of its class's base classes.

print(dir(list)) # it'll print out all methods available for the type of variable

# another way of statement for creating a list
list_2 = []
print(type(list_2))

list_2.append('item-1')
list_2.append('item-2')
list_2.append('item-3')
print(list_2)

# removing item
list_2.remove('item-2')
print(list_2)

